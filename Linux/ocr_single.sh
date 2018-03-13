convert *.tif temp.pbm
convert temp.pbm temp.tif
tesseract temp.tif output
cat output.txt | tr -d " \t\n\r" > out.txt 
rm temp.tif	
rm temp.pbm
rm output
rm out

echo "Conversion end..."


egrep -oh 'R(e|E)(g|G)[\.,]N(o|O)[\.,][0-9],[0-9]{3},[0-9]{3}' out.txt >> extracted.txt

echo "OCR end..."
