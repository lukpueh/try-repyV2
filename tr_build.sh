#! /bin/bash
# "Usage: $0 [</path/to/seattle_repy>"]


if [ -d build ]
  then
    echo "Removing 'build' directory..."
    rm -rf build
fi

seattle_repy="$1"

echo "Creating new 'build' directory..."
mkdir build

python tr_convertfiles.py

echo "Copying Try RepyV2 Python and r2py files to 'build'..."
cp tr_webcontroller.r2py build
cp restrictions.tryrepy build
cp tr_sandbox.r2py build
cp tr_fileabstraction.r2py build
cp upper_dot_lower.py build

if [ $# -gt 0 ]
  then
    echo "Copying RepyV2 modules to 'build' directory..."
    cp "${1}/dylink.r2py" build
    cp "${1}/base64.r2py" build
    cp "${1}/httpserver.r2py" build
    cp "${1}/librepy.r2py" build
    cp "${1}/librepyrunloop.r2py" build
    cp "${1}/priority_queue.r2py" build
    cp "${1}/librepyfile.r2py" build
    cp "${1}/librepyrandom.r2py" build
    cp "${1}/librepythread.r2py" build
    cp "${1}/librepysocket.r2py" build
    cp "${1}/urllib.r2py" build
    cp "${1}/urlparse.r2py" build
    cp "${1}/uniqueid.r2py" build
    cp "${1}/sockettimeout.r2py" build
    cp "${1}/random.r2py" build
    cp "${1}/math.r2py" build
    cp "${1}/httpretrieve.r2py" build
fi

exit 0
