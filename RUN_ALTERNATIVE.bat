@echo off
echo ===============================================
echo    STARTING DJANGO SERVER (ALTERNATIVE METHOD)
echo ===============================================
echo.

cd "%~dp0"
echo Current directory: %CD%
echo.

echo Activating virtual environment if it exists...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else if exist "myenv\Scripts\activate.bat" (
    call myenv\Scripts\activate.bat
) else if exist "env\Scripts\activate.bat" (
    call env\Scripts\activate.bat
) else (
    echo No virtual environment found, using system Python.
)
echo.

echo Starting Django server on port 9000...
echo.
echo Server will be available at: http://127.0.0.1:9000/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 127.0.0.1:9000 --noreload --insecure

echo.
echo Server stopped. Press any key to exit...
pause > nul
