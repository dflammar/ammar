@echo off
echo Starting Django server with logging...
python manage.py runserver > server_log.txt 2>&1
echo Server started with logging to server_log.txt
pause
