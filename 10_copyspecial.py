#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def special_path(dir):
  path1=[]
  for entry in os.listdir(dir):
      match = re.search(r'__(\w+)__', entry)
      print(match)
      if match:
        path1.append(os.path.abspath(os.path.join(dir, entry)))
  print(path1)
  return path1

def copy_to(paths,dir):
 # newdir = '/Users/jean-/Desktop/New1'
  if os.path.exists(dir)==False:
      os.mkdir(dir)  
  for spath in paths:
      file = os.path.basename(spath)
      shutil.copy(spath, os.path.join(dir,file))

def zip_to(paths, zipfile):
  archived = shutil.make_archive('zipfile', 'zip', '/Users/jean-/Desktop/New')
  if os.path.exists('E:/Zipped file.zip'):
    print(archived) 
  else: 
    print("ZIP file not created")

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args and args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths=[]
 # search = '/Users/jean-/Desktop/CopySpecial'
  for dirname in args:
    paths.extend(special_path(dirname))
 # paths=special_path(search)
  print(paths)
  copy_to(paths, todir)
  zip_to(paths,tozip)
if __name__ == '__main__':
  main()
