@echo off
echo Running Django Server Diagnostic...

REM Try to activate the virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else if exist "myenv\Scripts\activate.bat" (
    call myenv\Scripts\activate.bat
) else if exist "django_env\Scripts\activate.bat" (
    call django_env\Scripts\activate.bat
) else (
    echo No virtual environment found, using system Python
)

REM Run the diagnostic script
python diagnose_server.py

REM Keep the window open
echo.
echo Diagnostic complete. Press any key to exit.
pause
