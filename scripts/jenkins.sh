#! /bin/bash

# Update repo
git checkout master
git pull -q --ff-only

# Enable venv
if [ ! -d venv ]; then
    python3.11 -m venv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build docs
make html

# Disable venv
deactivate
