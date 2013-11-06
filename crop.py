from PIL import Image
import os
import shutil


def crop(path, destination, remove_destination=False, margin=(0, 0, 0, 0), maxwith=-1, background_color=(255, 255, 255),
         format="PNG",
         quality=100):
    if not os.path.isdir(destination):
        os.mkdir(destination)

    path = os.path.normpath(path)
    destination = os.path.normpath(destination)
    #It`s a bad idea to delete source path  :)
    if path == destination:
        remove_destination = False

    crop.count_images = 0
    crop.current_image = 0

    def crop_files_in_dir(path, destination):
        if remove_destination:
            shutil.rmtree(destination)

        if not os.path.isdir(destination):
            os.mkdir(destination)
        
        #collect all filenames first for preventing recursive overflow
        image_files = []

        for root, dirs, files in os.walk(path):
            for name in files:
                filename = os.path.join(root, name)
                image_files.append(filename)
        
        crop.count_images = len(image_files) 

        for filename in image_files:
            crop.current_image+=1
            img = crop_image(filename)
            if img is None:
                continue
            save_cropped_image(img, filename, destination)
            pass

    def crop_image(path):
        try:
            img = Image.open(path)
            img.load()
        except IOError as e:
            print e,path
            return None

        width = img.size[0]
        height = img.size[1]

        #set max values for variables for compare with pixels
        left = width
        top = height
        right = 0
        bottom = 0

        data = img.getdata()

        for y in range(height):
            for x in range(width):
                index = x + y * width
                color = data[index]
                if color == background_color:
                    continue
                if x < left:
                    left = x
                if x > right:
                    right = x
                if y < top:
                    top = y
                if y > bottom:
                    bottom = y
                    pass
                pass
            pass

        if left == width or right == 0 or top == height or bottom == 0:
            raise BaseException("Incorrect image data left:%i top:%i right:%i bottom:%i" % (left, top, right, bottom))

        cropped = img.crop((left, top, right, bottom))

        if maxwith == -1 or cropped.size[0] <= maxwith:
            return cropped

        width_ratio = (maxwith / float(width))
        scaled_height = int(height * width_ratio)
        cropped.thumbnail((maxwith, scaled_height), Image.ANTIALIAS)
        scaled = cropped
        if margin[0] == 0 and margin[1] == 0 and margin[2] == 0 and margin[3] == 0:
            return scaled

        shifted_width = margin[0] + margin[2] + scaled.size[0]
        shifted_height = margin[1] + margin[3] + scaled.size[1]

        shifted = Image.new(scaled.mode, (shifted_width, shifted_height), background_color)
        shifted.paste(scaled, (margin[0], margin[1]))
        return shifted

    def save_cropped_image(img, oldpath, destination):
        parts_path = os.path.split(oldpath)
        parts_file = os.path.splitext(parts_path[1])

        new_name = parts_file[0] + "." + format.lower()
        filepath = os.path.join(destination, new_name)
        img.save(filepath, format, quality=quality)
        print "cropped %i/%i=>%s" % (crop.count_images,crop.current_image, filepath)
    crop_files_in_dir(path, destination)

