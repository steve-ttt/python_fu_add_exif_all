#!/usr/bin/env python

# exiv2 -M"set Exif.Image.Make Rolleiflex" -M"set Exif.Image.Model SL35e" 
# -M"set Exif.Image.Software Adox Silvermax" -M"set Exif.Image.Artist me" $i;

from gimpfu import *
import gtk
import os 


# A way to show errors to the user:
warning_label = None

# Text entries containing the filenames:
entries = []



def python_add_exif_all(strMake, strModel, strFilm, strName, strCopyRt) :
    for i, img in enumerate(gimp.image_list()):
        #print(img.filename)     #to see this print message run gimp from the command line
        cmd = 'exiv2 -M"set Exif.Image.Make %s" -M"set Exif.Image.Model %s" \
            -M"set Exif.Image.Software %s" -M"set Exif.Image.Artist %s" -M"set Exif.Image.Copyright %s" %s' % (strMake, strModel, strFilm, strName, strCopyRt, img.filename)
        #print(cmd)
        returned_value = os.system(cmd)             # returns the exit code in unix
        #print('returned value:', returned_value)





register(
    "python_fu_add_exif_all",
    "Modify exif data to all open images (exiv2 must be installed)",
    "Modify exif data to all open images (exiv2 must be installed)",
    "Stephen THORLEY",
    "Stephen THORLEY",
    "2018",
    "Add Exif all...",
    "*",      # Create a new image, don't work on an existing one
    [
        (PF_STRING, "string", "Make", 'Rolleiflex'),
        (PF_STRING, "string", "Model", '2.8FX'),
        (PF_STRING, "string", "image software(film)", 'Kodak Tmax 400'),
        (PF_STRING, "string", "Artist", 'Me'),
        (PF_STRING, "string", "Copyright", "Copyright, me, 2018")
        
    ],
    [],
    python_add_exif_all,
    menu="<Image>/Film Tools")

main()
