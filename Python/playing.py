import pytesseract
import sys
from PIL import Image
import re
import os
import csv


# read files from the directory and perform the OCR operation on them
for files in sorted(os.listdir("../sample_small")):
    # convert tiff file to a grayscale tiff file
    # TODO get the img here!!!!
    cmd1 = "convert ../sample_small/"+files+" temp.pbm"
    cmd2 = "convert temp.pbm temp.tif"
    os.system(cmd1)
    os.system(cmd2)
    img = Image.open("temp.tif")
    img.show()