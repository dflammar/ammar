@echo off
echo ===============================================
echo    Check Firewall Settings
echo ===============================================
echo.

echo Checking Windows Firewall status...
netsh advfirewall show allprofiles state

echo.
echo Checking if Python is allowed through the firewall...
netsh advfirewall firewall show rule name=all | findstr /i python

echo.
echo Checking if ports 3000, 8000, 8080, and 8888 are allowed...
netsh advfirewall firewall show rule name=all | findstr /i "3000 8000 8080 8888"

echo.
echo Firewall check complete!
echo.
echo If Python is not listed above, you may need to add it to the firewall exceptions.
echo.
echo To add Python to firewall exceptions:
echo 1. Open Windows Defender Firewall with Advanced Security
echo 2. Click on "Inbound Rules" on the left
echo 3. Click "New Rule..." on the right
echo 4. Select "Program" and click Next
echo 5. Browse to your Python executable (usually in C:\Python3x or C:\Users\YourUsername\AppData\Local\Programs\Python)
echo 6. Allow the connection and give it a name like "Python"
echo.
echo Press any key to exit...
pause > nul
