#! /bin/bash
set -e

# Enable venv
if [ ! -d venv ]; then
    python3.11 -m venv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build docs
make -e rsync_copy

# Disable venv
deactivate
