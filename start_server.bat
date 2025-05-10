@echo off
echo ===============================================
echo    Teaching Platform Server Startup Script
echo ===============================================
echo.

REM Set the port
set PORT=8888

REM Check if port is already in use
netstat -ano | findstr ":%PORT%" > nul
if %ERRORLEVEL% EQU 0 (
    echo WARNING: Port %PORT% is already in use!
    echo The server may not start properly.
    echo.
    echo You can:
    echo 1. Close the application using port %PORT%
    echo 2. Edit this script to use a different port
    echo.
    echo Press any key to continue anyway...
    pause > nul
)

echo Server will be available at: http://127.0.0.1:%PORT%/
echo.
echo Press Ctrl+C to stop the server
echo.

REM Activate the virtual environment if it exists
if exist "myenv\Scripts\activate.bat" (
    echo Activating virtual environment: myenv
    call myenv\Scripts\activate.bat
) else if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment: .venv
    call .venv\Scripts\activate.bat
) else if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment: venv
    call venv\Scripts\activate.bat
) else (
    echo No virtual environment found. Using system Python.
)

REM Check if Python is installed
python --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python and try again.
    echo.
    echo Press any key to exit...
    pause > nul
    exit /b 1
)

REM Check if Django is installed
python -c "import django" > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo WARNING: Django is not installed.
    echo Attempting to install Django...
    pip install django
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to install Django.
        echo Please install Django manually and try again.
        echo.
        echo Press any key to exit...
        pause > nul
        exit /b 1
    )
)

REM Check if manage.py exists
if not exist "manage.py" (
    echo ERROR: manage.py not found in current directory.
    echo Please make sure you are in the correct directory.
    echo.
    echo Press any key to exit...
    pause > nul
    exit /b 1
)

echo Starting Django server on port %PORT%...
echo.
echo ===============================================
echo.

REM Run the server
python manage.py runserver 0.0.0.0:%PORT%

REM If the server exits with an error
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ===============================================
    echo ERROR: The server exited with an error.
    echo.
    echo Possible solutions:
    echo 1. Check if port %PORT% is already in use
    echo 2. Verify that all dependencies are installed
    echo 3. Check the error message above for details
    echo.
    echo Press any key to exit...
    pause > nul
)
