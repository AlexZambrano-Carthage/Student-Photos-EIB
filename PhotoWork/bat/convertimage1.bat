del c:\PhotoWork\PhotoConv\* /Q
del c:\PhotoWork\PhotoOrig\* /Q 
xcopy C:\PhotoWork\Photos\*.* c:\PhotoWork\PhotoOrig\
for /f %%a in ('dir c:\PhotoWork\PhotoOrig\*.* /b') do call c:\PhotoWork\bat\convertimage2.bat %%a
