@echo off
echo Converting the file c:\PhotoWork\PhotoOrig\%1
del c:\PhotoWork\PhotoConv\%1 /Q
convert c:\PhotoWork\PhotoOrig\%1 -resize "200x200^" -gravity center -crop "200x200+0+0" c:\PhotoWork\PhotoConv\%1