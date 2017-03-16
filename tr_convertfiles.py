"""
<Program Name>
  tr_convertfiles.py

<Started>
  March, 2011

<Author>
  Lukas Puehringer, University of Vienna
  lukas.puehringer@univie.ac.at

<Purpose>
  Flattens out the 'web' directory and copies all its files to the 'build'
  directory, representing the username 'system' and each file's relative path
  to the base64 encoded filename.

"""
import os
import sys
import base64
import shutil
import upper_dot_lower

# This directory contains all webfiles HTML, JS, CSS
DIR_SRC = "web"

# To this directory the name converted files web files will be saved
DIR_DEST = "build"

SYSTEM_USER = "system"

def _encode_path(path):
  # Base64 encode a path with a user prefix (urlsafe, -_)
  path_enc = base64.urlsafe_b64encode(path)

  # Replace trailing output padding equal sign(s) with dots
  # for RepyV2 valid filenames (part 1)
  path_enc = path_enc.replace("=", ".")

  # Replace upper case with dot-lower for RepyV2
  # valid filenames (part 2)
  return upper_dot_lower.encode_dot_lower(path_enc)



def main():

  print "Flattening and encoding files in 'web' and copying to 'build'..."

  if not (os.path.isdir(DIR_SRC) and os.path.isdir(DIR_DEST)):
    print "Requires subdirs 'web' and 'build' in the current directory."
    sys.exit(1)

  for root, dirs, files in os.walk(DIR_SRC):
    for file in files:

      # Ignore hidden files
      if file.startswith("."):
        continue


      # Construct the relative source paths
      src_path = os.path.relpath(os.path.join(root, file))
      # Construct the relative virtual source path
      # These paths can be used in TryRepy
      virtual_path = src_path[len(DIR_SRC) + 1:]

      # Encode the virtual paths as SYSTEM_USER files
      # These are the filenames as the files are in the vessels
      encoded_path = _encode_path(SYSTEM_USER + virtual_path)

      dest_path = os.path.join(DIR_DEST, encoded_path)

      # Copy the files to the build directory using the encoded user prefixed fn
      shutil.copyfile(src_path, dest_path)

if __name__ == "__main__":
  main()


