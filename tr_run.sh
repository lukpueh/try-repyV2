#! /bin/bash

if [ $# -ne 2 ]
  then
    echo "Usage: $0 </path/to/seattle_repy> <serverport>" >&2
    exit 1
fi

if [ ! -d "$1" ]
  then
    echo "Usage: $0 </path/to/seattle_repy> <serverport>" >&2
    exit 2
fi

echo "Copying files from 'build' to 'seattle_repy' directory..."
cp build/* $1
echo "Changing to $1"
cd $1
echo "Running: python repy.py restrictions.tryrepy dylink.r2py tr_webcontroller.r2py $2"
python repy.py restrictions.tryrepy dylink.r2py tr_webcontroller.r2py $2

exit 0
