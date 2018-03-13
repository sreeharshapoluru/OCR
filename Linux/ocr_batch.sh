for file in ../sample_small/*.tif
do
echo "Conversion start..."

convert $file temp.pbm
convert temp.pbm temp.tif
tesseract temp.tif output
cat output.txt | tr -d " \t\n\r" > out.txt 
rm temp.tif	
rm temp.pbm
rm output.txt

echo "Conversion end..."

echo "OCR start..."

egrep -oh 'R(e|E)(g|G)[\.,]N(o|O)[\.,][0-9],[0-9]{3},[0-9]{3}' out.txt >> extracted.txt

echo "OCR end..."

done




