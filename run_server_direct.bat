@echo off
echo ===============================================
echo    Direct Django Server
echo ===============================================
echo.

echo This script runs Django directly with minimal configuration.
echo.

set PORT=4000

echo Starting Django server on port %PORT%...
echo.
echo Server will be available at: http://127.0.0.1:%PORT%/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 0.0.0.0:%PORT% --noreload --insecure

echo.
echo Server stopped. Press any key to exit...
pause > nul
