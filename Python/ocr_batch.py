# -*- coding: utf-8 -*-
import pytesseract
import sys
from PIL import Image
import re
import os
import csv
import string


# read files from the directory and perform the OCR operation on them
for files in sorted(os.listdir("../sample_small")):
    # convert tiff file to a grayscale tiff file
    # TODO get the img here!!!!
    cmd1 = "convert ../sample_small/"+files+" temp.pbm"
    cmd2 = "convert temp.pbm temp.tif"
    os.system(cmd1)
    os.system(cmd2)

    # use tesseract convert tiff to .txt file
    textFile = open('output.txt','w')
    text = pytesseract.image_to_string(Image.open("temp.tif"))
    textFile.write(text.encode('utf-8'))
    textFile.close()

    # use the regex to search for the text format
    tempFile = open('output.txt','r')
    temp = tempFile.read()
    tempFile.close()
    tempStr = ''.join(temp.split())
    toSearch = string.replace(tempStr,"’",",")
    regExpression = "reg.no.[0-9].[0-9]{3}.[0-9]{3}"
    try:
        tempNum = re.search(regExpression,toSearch.lower()).group()
        regNum = re.search("[0-9].[0-9]{3}.[0-9]{3}",tempNum.lower()).group()

    # output each filename and the corresponding extracted quantity into a csv file.
        with open("regnum.csv","a") as csvFile:
            csvFileWriter = csv.writer(csvFile,dialect="excel")
            csvFileWriter.writerow([files,regNum])
            csvFile.close()
    except Exception:
        continue

    # remove all extra stuff created...close all files.....etc.
    os.remove('output.txt')
    os.remove("temp.tif")
    os.remove("temp.pbm")
    

print "DONE!!!"