#!/bin/bash

# Script for building the wiki repo locally for testing feature branches and
# the like.  Can be run from any directory in the wiki repo.

# Run in correct dir
DIR=`dirname $0`/../
cd $DIR

# Enable venv (recreate it if missing or built with a different python)
if [ ! -x venv/bin/python3.12 ]; then
    rm -rf venv
    python3.12 -m venv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build docs
SPHINXOPTS="-W" make -e html

# Disable venv
deactivate
