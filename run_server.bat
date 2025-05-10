@echo off
echo Starting Django server...

REM Activate the virtual environment
if exist "myenv\Scripts\activate.bat" (
    call myenv\Scripts\activate.bat
) else if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo No virtual environment found.
)

REM Install required packages
pip install requests django-allauth

REM Run the server
python manage.py runserver 8080

REM Keep the window open
pause
