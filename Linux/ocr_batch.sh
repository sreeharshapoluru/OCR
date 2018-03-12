
for file in ../sample_small/*.tif
do
echo "Conversion start..."

convert $file temp.pbm
convert temp.pbm temp.tif
tesseract temp.tif output
rm temp.tif	
rm temp.pbm

echo "Conversion end..."

echo "OCR start..."

egrep 'R(e|E)(g|G)\. N(o|O)\. [0-9],[0-9]{3},[0-9]{3}$' output.txt >>  extracted.txt

echo "OCR end..."

done




