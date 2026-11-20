#!/usr/bin/env python3
"""Check OSL docs and wiki pages against the house style.

This script is shared, byte for byte, by osuosl/docs and osuosl/wiki. The
rules it checks are written up for people in the docs repo's
source/metadocs/rst_guide.rst and the wiki's source/contributing.rst.

Usage:
    scripts/check_style.py [--warn-only] [--public] [--width N] PATH...

PATH can be .rst files or directories. Exit status is 1 when an error is
found, unless --warn-only is given. --warn-only never downgrades the
--public checks (internal details on the public wiki and frozen labels).

A line can opt out of one check with a comment on the line before it:

    .. style-ok: <check> <why>

for example ``.. style-ok: private-ip users must ping the VPN gateway``.
"""

import argparse
import os
import re
import sys

# The Python Developer's Guide convention the Sphinx primer recommends, with a
# page title as the "section" level: = then - then ^ then ".
HEADING_CHARS = "=-^\""
# Two characters are enough for the heading set (an "RT" title); other
# characters need three, so a bare "::" line is not an underline.
ADORNMENT = re.compile(r"^(?:([=\-~^\"])\1+|([`#*+.:'_])\2{2,})\s*$")
SIMPLE_BORDER = re.compile(r"^\s*=+(\s+=+)+\s*$")
BULLET = re.compile(r"^\s*[*\-+] +\S")
# List markers as docutils reads them: bullets, and enumerators like 1. #. a)
# (iv). A list-table row chains two ("* - cell"). One or more spaces follow.
_ENUM = r"(?:\d+|#|[a-zA-Z]|[ivxlcdmIVXLCDM]+)"
_MARK1 = rf"(?:[*\-+]|{_ENUM}[.)]|\({_ENUM}\))"
LIST_MARK = re.compile(rf"^(\s*)((?:{_MARK1} +)+)(?=\S)")
ENUM_MARK = re.compile(rf"^\s*(?:{_ENUM}[.)]|\({_ENUM}\)) +\S")
LABEL = re.compile(r"^\.\. _([^:]+):\s*$")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DIRECTIVE = re.compile(r"^(\s*)\.\. ([a-zA-Z0-9_:-]+)::(.*)$")
OPT_OUT = re.compile(r"^\s*\.\. style-ok: (\S+)")
URL = re.compile(r"https?://")

# Directives whose body is not prose, so line length is not checked.
LITERAL_DIRECTIVES = {
    "code-block", "code", "sourcecode", "literalinclude", "csv-table", "graphviz",
    "graph", "digraph", "raw", "math", "parsed-literal",
}

# Internal details that do not belong on the public wiki.
PUBLIC_PATTERNS = [
    ("internal-domain", re.compile(r"\b[\w.-]+\.(bak|oob)\b|\bosuosl\.(bak|oob)\b")),
    ("private-ip", re.compile(
        r"\b(10\.\d{1,3}|172\.(1[6-9]|2\d|3[01])|192\.168)\.\d{1,3}\.\d{1,3}\b")),
    ("rt-link", re.compile(r"support\.osuosl\.org/Ticket")),
    ("admin-account", re.compile(r"\bosuadmin\b")),
    ("secrets-location", re.compile(r"\b(data_bags?|firfile|encrypted data bag)\b", re.I)),
]


def is_list_item(lines, i, marker=None):
    """True if line i starts a real list item, not paragraph text.

    reStructuredText starts a list only after a blank line, a section
    heading, or a sibling item at the same indent; a marker on a continuation
    line renders as text (the classic sub-bullet that "doesn't render"). An
    enumerator also needs a blank, indented or item line after it, or
    docutils reads it as text ("A. Einstein ...").
    """
    if not LIST_MARK.match(lines[i]):
        return False
    ind = len(lines[i]) - len(lines[i].lstrip())
    if ENUM_MARK.match(lines[i]) and i + 1 < len(lines) and lines[i + 1].strip():
        nxt = lines[i + 1]
        if len(nxt) - len(nxt.lstrip()) <= ind and not LIST_MARK.match(nxt):
            return False
    k = i - 1
    while k >= 0 and lines[k].strip():
        prev = lines[k]
        kind = len(prev) - len(prev.lstrip())
        if kind < ind:
            # Indented under a line whose text starts left of the marker: an
            # indented block (definition, quote), where the list is real.
            # Exactly at the parent item's text column: a continuation.
            m = LIST_MARK.match(prev)
            textcol = len(m.group(0)) if m else kind
            return textcol < ind
        if kind == ind:
            if re.match(r"^\s*(?:([=\-~^\"])\1+|([`#*+.:'_])\2{2,})\s*$", prev):
                return True  # right under a section heading
            # a sibling counts only if it is a real item itself
            return is_list_item(lines, k)
        k -= 1
    return True


def first_content_line(lines):
    """Index of the first line that is not blank or part of a comment.

    A comment is a ".." line that is not a label or directive, plus the
    indented lines that continue it (like the sphinx-quickstart header).
    """
    i, n = 0, len(lines)
    while i < n:
        s = lines[i].strip()
        if not s or s.startswith(":orphan:"):
            i += 1
            continue
        if s.startswith("..") and not re.match(r"^\.\. _[^:]+:\s*$", s) and "::" not in s:
            i += 1
            while i < n and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                if not lines[i].strip() and (i + 1 >= n or not lines[i + 1].startswith((" ", "\t"))):
                    break
                i += 1
            continue
        return i
    return None


class Page:
    def __init__(self, path, public):
        self.path = path
        self.public = public
        with open(path, encoding="utf-8") as f:
            self.lines = f.read().split("\n")
        self.findings = []

    def add(self, lineno, level, check, msg):
        prev = self.lines[lineno - 2] if lineno >= 2 else ""
        m = OPT_OUT.match(prev)
        if m and m.group(1) in (check, "all"):
            return
        self.findings.append((self.path, lineno, level, check, msg))

    def literal_mask(self):
        """Return a list of booleans: True where a line is code or a literal block."""
        mask = [False] * len(self.lines)
        i = 0
        n = len(self.lines)
        while i < n:
            line = self.lines[i]
            d = DIRECTIVE.match(line)
            starts_literal = False
            indent = len(line) - len(line.lstrip())
            if d and d.group(2) in LITERAL_DIRECTIVES:
                starts_literal = True
            elif line.rstrip().endswith("::") and not d and not line.lstrip().startswith(".."):
                starts_literal = True
            if starts_literal:
                j = i + 1
                while j < n:
                    nxt = self.lines[j]
                    if nxt.strip() and (len(nxt) - len(nxt.lstrip())) <= indent:
                        break
                    mask[j] = True
                    j += 1
                i = j
                continue
            if re.match(r"^\s*[+|]", line):  # grid table row or border
                mask[i] = True
            elif SIMPLE_BORDER.match(line):  # simple table: mask to the closing border
                j = i + 1
                while j < n and not (SIMPLE_BORDER.match(self.lines[j]) and
                                     (j + 1 >= n or not self.lines[j + 1].strip())):
                    j += 1
                for k in range(i, min(j + 1, n)):
                    mask[k] = True
                i = j + 1
                continue
            i += 1
        return mask

    def directive_body_mask(self, names):
        """True for lines inside the body of any of the named directives."""
        mask = [False] * len(self.lines)
        for i, line in enumerate(self.lines):
            d = DIRECTIVE.match(line)
            if not d or d.group(2) not in names:
                continue
            indent = len(d.group(1))
            j = i + 1
            while j < len(self.lines):
                nxt = self.lines[j]
                if nxt.strip() and (len(nxt) - len(nxt.lstrip())) <= indent:
                    break
                mask[j] = True
                j += 1
        return mask

    def check(self, width):
        mask = self.literal_mask()
        self.list_tables = self.directive_body_mask({"list-table"})
        self.check_whitespace(mask)
        self.check_label()
        self.check_headings(mask)
        self.check_lines(mask, width)
        self.check_directives()
        if self.public:
            self.check_public()

    def check_whitespace(self, mask):
        for i, line in enumerate(self.lines, 1):
            if "\t" in line and not mask[i - 1]:
                self.add(i, "E", "tab", "tab character; indent with spaces")
            if line != line.rstrip():
                self.add(i, "E", "trailing-space", "trailing whitespace")

    def check_label(self):
        idx = first_content_line(self.lines)
        if idx is None:
            return
        m = LABEL.match(self.lines[idx].strip())
        if not m:
            self.add(idx + 1, "E", "page-label", "page does not start with a `.. _label:` line")
        elif not KEBAB.match(m.group(1)):
            self.add(idx + 1, "E", "label-style", f"page label `{m.group(1)}` is not kebab-case")

    def check_headings(self, mask):
        seen = []
        n = len(self.lines)
        for i in range(1, n):
            line = self.lines[i]
            if mask[i] or not ADORNMENT.match(line):
                continue
            title = self.lines[i - 1]
            if not title.strip() or ADORNMENT.match(title) or title.startswith(" "):
                # possibly an overline or a transition
                if i + 2 < n and self.lines[i + 1].strip() and ADORNMENT.match(self.lines[i + 2]):
                    self.add(i + 1, "E", "heading", "overlined title; use an underline only")
                elif not title.strip() and (i + 1 >= n or not self.lines[i + 1].strip()):
                    self.add(i + 1, "E", "transition", "transition line; use a section heading instead")
                continue
            ch = line.strip()[0]
            lineno = i + 1
            if len(line.rstrip()) < len(title.rstrip()):
                self.add(lineno, "E", "heading", "underline shorter than the heading")
            if ch not in HEADING_CHARS:
                self.add(lineno, "E", "heading", f"heading uses `{ch}`; use = - ^ \" in that order")
                continue
            level = HEADING_CHARS.index(ch)
            if not seen:
                if level != 0:
                    self.add(lineno, "E", "heading", "page title must be underlined with `=`")
                seen.append(level)
                continue
            if level == 0:
                self.add(lineno, "E", "heading", "second `=` heading; a page has one title")
                continue
            deepest = max(seen)
            if level > deepest + 1:
                self.add(lineno, "E", "heading",
                         f"heading `{ch}` skips a level; after `{HEADING_CHARS[deepest]}` use "
                         f"`{HEADING_CHARS[deepest + 1]}`")
            seen.append(level)

    def check_lines(self, mask, width):
        for i, line in enumerate(self.lines, 1):
            if mask[i - 1]:
                continue
            s = line.strip()
            if len(line) > width and not URL.search(line) and not ADORNMENT.match(line) \
                    and not LABEL.match(s) and not s.startswith(".. _") \
                    and not self._is_heading(i - 1) and len(s.split()) > 1:
                self.add(i, "E", "line-length", f"line is {len(line)} columns; wrap prose at {width}")
            if LIST_MARK.match(line) and not self.list_tables[i - 1] and not self._is_heading(i - 1):
                if not is_list_item(self.lines, i - 1):
                    if BULLET.match(line) or re.match(r"^\s*(#|\d+)\. ", line):
                        self.add(i, "W", "broken-list",
                                 "looks like a list item but continues the line above, so it renders as "
                                 "text; add a blank line before it (and indent a sub-list to the parent's text)")
                elif re.match(r"^\s*- \S", line):
                    self.add(i, "E", "bullet", "bullet uses `-`; use `*`")
                elif re.match(r"^\s*\d+\. \S", line):
                    self.add(i, "W", "ordered-list", "numbered list item; prefer `#.`")
            if "http://" in line and not re.search(r"http://(localhost|127\.0\.0\.1|<)", line):
                self.add(i, "W", "http", "http:// link; use https:// where the site supports it")
            if ":doc:`" in line:
                self.add(i, "W", "doc-role", ":doc: breaks when pages move; prefer :ref:")

    def _is_heading(self, idx):
        return idx + 1 < len(self.lines) and ADORNMENT.match(self.lines[idx + 1] or "") is not None

    def check_directives(self):
        n = len(self.lines)
        for i, line in enumerate(self.lines):
            d = DIRECTIVE.match(line)
            if not d:
                continue
            name, arg = d.group(2), d.group(3).strip()
            lineno = i + 1
            if name in ("code-block", "sourcecode") and not arg:
                self.add(lineno, "E", "code-language",
                         "code-block without a language; use `::` for commands, or name the language")
            if name == "contents":
                self.add(lineno, "E", "contents", "Furo builds the page contents; remove `.. contents::`")
            if name in ("image", "figure"):
                indent = len(d.group(1))
                j = i + 1
                has_alt = False
                while j < n and (not self.lines[j].strip() or
                                 len(self.lines[j]) - len(self.lines[j].lstrip()) > indent):
                    if not self.lines[j].strip():
                        if name == "image":
                            break
                    elif self.lines[j].strip().startswith(":alt:"):
                        has_alt = True
                    j += 1
                if not has_alt:
                    self.add(lineno, "E", "image-alt", f"{name} has no `:alt:` text")

    def check_public(self):
        for i, line in enumerate(self.lines, 1):
            for check, rx in PUBLIC_PATTERNS:
                if rx.search(line):
                    self.add(i, "P", check,
                             "internal detail on the public wiki; move it to docs or opt out with "
                             f"`.. style-ok: {check} <why>`")


def frozen_labels(source_dir, labels_file):
    """Labels other repos link to through intersphinx must keep existing."""
    if not os.path.exists(labels_file):
        return []
    wanted = []
    with open(labels_file, encoding="utf-8") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if line:
                wanted.append(line)
    defined = set()
    for root, _, files in os.walk(source_dir):
        for fn in files:
            if fn.endswith(".rst"):
                with open(os.path.join(root, fn), encoding="utf-8") as f:
                    for line in f:
                        m = LABEL.match(line.strip())
                        if m:
                            defined.add(m.group(1).lower())
    return [(labels_file, 0, "P", "frozen-label",
             f"label `{lab}` is linked from osuosl/docs (intersphinx `public:{lab}`) but no longer exists")
            for lab in wanted if lab.lower() not in defined]


def collect(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if not d.startswith((".", "_"))]
                for fn in sorted(files):
                    if fn.endswith(".rst"):
                        yield os.path.join(root, fn)
        elif p.endswith(".rst") and os.path.exists(p):
            yield p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", default=["source"])
    ap.add_argument("--width", type=int, default=80)
    ap.add_argument("--warn-only", action="store_true",
                    help="report style errors without failing (public checks still fail)")
    ap.add_argument("--public", action="store_true",
                    help="also check for internal details and frozen labels (the wiki)")
    ap.add_argument("--frozen-labels", default="scripts/frozen_labels.txt")
    ap.add_argument("--summary", action="store_true", help="print counts per check instead of each finding")
    args = ap.parse_args()

    findings = []
    for path in collect(args.paths):
        page = Page(path, args.public)
        page.check(args.width)
        findings.extend(page.findings)
    if args.public:
        findings.extend(frozen_labels("source", args.frozen_labels))

    if args.summary:
        counts = {}
        for _, _, level, check, _ in findings:
            counts[(level, check)] = counts.get((level, check), 0) + 1
        for (level, check), c in sorted(counts.items()):
            print(f"{level} {check}: {c}")
    else:
        for path, lineno, level, check, msg in findings:
            print(f"{path}:{lineno}: {level} [{check}] {msg}")

    errors = [f for f in findings if f[2] == "P" or (f[2] == "E" and not args.warn_only)]
    if findings and not args.summary:
        e = sum(1 for f in findings if f[2] in "EP")
        w = sum(1 for f in findings if f[2] == "W")
        print(f"{e} error(s), {w} warning(s)" + (" (style errors not fatal: --warn-only)"
                                               if args.warn_only else ""), file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
