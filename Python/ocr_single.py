import pytesseract
import sys
from PIL import Image
import re
import os
import csv

#read file from the arguments
img = sys.argv[1]
cmd1 = "convert "+ img +" temp.pbm"
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
toSearch = ''.join(temp.split())
regExpression = "reg.no.[0-9].[0-9]{3}.[0-9]{3}"
print toSearch.lower()
tempNum = re.search(regExpression,toSearch.lower(),re.DOTALL).group()
regNum = re.search("[0-9].[0-9]{3}.[0-9]{3}",tempNum.lower(),re.DOTALL).group()

print tempNum
print regNum
# remove all extra stuff you created...close all files.....etc.
os.remove('output.txt')
os.remove("temp.tif")
os.remove("temp.pbm")