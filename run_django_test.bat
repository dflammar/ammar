@echo off
echo ===============================================
echo    Django Configuration Test
echo ===============================================
echo.

echo This script will check if Django is installed and configured correctly.
echo It will also try to start a Django development server on port 9999.
echo.

echo Running Django test...
echo.

python django_test.py

echo.
echo Test completed. Press any key to exit...
pause > nul
