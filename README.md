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


