#! /bin/bash
set -e

# Enable venv (recreate it if missing or built with a different python)
if [ ! -x venv/bin/python3.12 ]; then
    rm -rf venv
    python3.12 -m venv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build docs
make -e rsync_copy

# Disable venv
deactivate
