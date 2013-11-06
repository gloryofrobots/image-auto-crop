image-auto-crop
===============
I wrote this simple python script when i need to extract a small parts from large image  that is crop it from it`s background.

Program get bounding box of all non-background colors in image. Then crop this BB scale result if needs and apply margin.
Program apply this procedure for all images in source directory and save results with same names in destination directory. Carefully if source == destination you can overwrite sources.

DEPENDENCY: Python2.7,PIL

RUN: python image_auto_crop.py

usage: image_auto_crop [-h] -p STRING -d STRING [-c]
                       [-m LEFT TOP RIGHT BOTTOM] [-w INT] [-b R G B]
                       [-f STRING] [-q INT]

Extract part of image which specified by bounding box of non background pixels
and save it to same filename in chosen folder.

optional arguments:
  -h, --help            show this help message and exit
  -p STRING, --path STRING
                        Path to source dir
  -d STRING, --dest STRING
                        Path to destination dir
  -c, --clear           Clear destination directory if destination!=source
  -m LEFT TOP RIGHT BOTTOM, --margin LEFT TOP RIGHT BOTTOM
                        Cropped image margin
  -w INT, --width INT   Max width for cropped image.
  -b R G B, --background R G B
                        Image background(dominant) color
  -f STRING, --format STRING
                        PIL supported output format
  -q INT, --quality INT
                        Image quality 0-100

