import argparse
from crop import crop

def main():
    description = 'Extract part of image which specified by bounding box of non background pixels' \
                  + 'and save it to same filename in chosen folder.'
    parser = argparse.ArgumentParser(prog="image_auto_crop", description=description)



    parser.add_argument('-p', '--path',  metavar='STRING', help='Path to source dir', required=True)
    parser.add_argument('-d', '--dest',  metavar='STRING', help='Path to destination dir', required=True)
    parser.add_argument('-c', '--clear', default=False, action='store_true',
                        help='Clear destination directory if destination!=source')
    parser.add_argument('-m', '--margin', metavar=('LEFT','TOP','RIGHT','BOTTOM'), type=int, nargs=4, default=(0,0,0,0),
                        help='Cropped image margin')

    parser.add_argument('-w', '--width', default=-1, metavar='INT', type=int
        , help='Max width for cropped image.')

    parser.add_argument('-b', '--background', metavar=('R','G','B'), type=int, nargs=3, default=(255, 255, 255),
                        help='Image background(dominant) color')

    parser.add_argument('-f', '--format', metavar='STRING', default="PNG", help='PIL supported output format')

    parser.add_argument('-q', '--quality', metavar='INT',type=int, default=100, help='Image quality 0-100')
    args = parser.parse_args()

    print args
    crop(args.path, args.dest, maxwith=args.width, margin=args.margin, remove_destination=args.clear,
         background_color=args.background, format=args.format, quality=args.quality)

if __name__ == "__main__":
    main()
