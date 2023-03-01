#! /bin/bash

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv -p python3
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build docs
make -e rsync_copy

if [ $? -eq 0 ]
then
  deactivate
else
  deactivate
  exit 1
fi
