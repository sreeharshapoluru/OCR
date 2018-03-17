import pytesseract;
import sys;
from PIL import Image;
import re;
import os;
import csv;


img = sys.argv[1]
 
# use tesseract convert tiff to .txt file
textFile = open('output.txt','w');
text = pytesseract.image_to_string(Image.open(img));
textFile.write(text.encode('utf-8'));
textFile.close();

# use the regex to search for the text format
tempFile = open('output.txt','r');
temp = tempFile.read();
tempFile.close();
toSearch = ''.join(temp.split());
regExpression = "R(e|E)(g|G)[\.,]N(o|O)[\.,][0-9],[0-9]{3},[0-9]{3}";
tempNum = re.search(regExpression,toSearch,re.IGNORECASE).group();
regNum = re.search("[0-9],[0-9]{3},[0-9]{3}",tempNum,re.IGNORECASE).group();

# output each filename and the corresponding extracted quantity into a csv file.
with open("regnum.csv","a") as csvFile:
    csvFileWriter = csv.writer(csvFile,dialect="excel");
    csvFileWriter.writerow([img,regNum]);
csvFile.close();

# remove all extra stuff you created...close all files.....etc.
os.remove('output.txt');