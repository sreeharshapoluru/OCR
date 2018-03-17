echo "Conversion start..."
# removing the aplha layer from the tiff images
convert *.tif temp.pbm
convert temp.pbm temp.tif
# using tessearct to convert tiff to text
tesseract temp.tif output
#removing all the spaces from the text
cat output.txt | tr -d " \t\n\r" > out.txt 
#remove temporary files
rm temp.tif	
rm temp.pbm
rm output
echo "Conversion end..."

echo "OCR start..."
# using grep search for the pattern
egrep -oh 'R(e|E)(g|G)[\.,]N(o|O)[\.,][0-9],[0-9]{3},[0-9]{3}' out.txt >> extractedregnums.txt
#remove temp files
rm out
echo "OCR end..."
