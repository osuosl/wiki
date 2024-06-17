#!/bin/bash

# Enable venv
if [ ! -d venv ]; then
    python3.11 -m venv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

if [ -n "${CHECK_LINT}" ]; then
  make -e lint_changed
fi

# Build docs
make -e rsync_copy

if [ $? -eq 0 ]
then
  deactivate
else
  deactivate
  exit 1
fi
