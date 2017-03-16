#! /bin/bash

echo "Building Try Repy..."
if [ $# -ne 1 -o ! -d "$1" ]
  then
    echo "Usage: $0 </path/to/seattle_repy>" >&2
    exit 1
fi

if [ -d build ]
  then
    echo "Removing build directory..."
    rm -rf build
fi

seattle_repy="$1"

echo "Creating new build directory..."
mkdir build

echo "Calling python script to flat out web directory..."
python tr_convertfiles.py

echo "Copying needed py and r2py file to build directory..."
cp tr_webcontroller.r2py build
cp restrictions.tryrepy build
cp tr_sandbox.r2py build
cp tr_fileabstraction.r2py build
cp upper_dot_lower.py build


echo "Copying runtime parts..."
cp "${seattle_repy}/dylink.r2py" build
cp "${seattle_repy}/base64.r2py" build
cp "${seattle_repy}/upper_dot_lower.py" build
cp "${seattle_repy}/httpserver.r2py" build
cp "${seattle_repy}/librepy.r2py" build
cp "${seattle_repy}/librepyrunloop.r2py" build
cp "${seattle_repy}/priority_queue.r2py" build
cp "${seattle_repy}/librepyfile.r2py" build
cp "${seattle_repy}/librepyrandom.r2py" build
cp "${seattle_repy}/librepythread.r2py" build
cp "${seattle_repy}/librepysocket.r2py" build
cp "${seattle_repy}/urllib.r2py" build
cp "${seattle_repy}/urlparse.r2py" build
cp "${seattle_repy}/uniqueid.r2py" build
cp "${seattle_repy}/sockettimeout.r2py" build
cp "${seattle_repy}/random.r2py" build
cp "${seattle_repy}/math.r2py" build
cp "${seattle_repy}/httpretrieve.r2py" build

echo "Finished building! You can now run tr_run.sh </path/to/seattle_repy> <serverport>"

exit 0
