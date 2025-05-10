@echo off
echo ===============================================
echo    TEACHING PLATFORM LAUNCHER
echo ===============================================
echo.

:menu
echo Please select an option:
echo 1. Run Django server (port 8000)
echo 2. Run Django server (alternative port 9000)
echo 3. Open project folder
echo 4. Exit
echo.

set /p choice=Enter your choice (1-4): 

if "%choice%"=="1" goto run_django
if "%choice%"=="2" goto run_alternative
if "%choice%"=="3" goto open_folder
if "%choice%"=="4" goto end

echo Invalid choice. Please try again.
echo.
goto menu

:run_django
echo.
echo Starting Django server on port 8000...
echo.
start cmd /k "cd /d "%~dp0" && python manage.py runserver"
echo.
echo Server started! Opening browser...
timeout /t 3 > nul
start http://127.0.0.1:8000/
goto end

:run_alternative
echo.
echo Starting Django server on alternative port 9000...
echo.
start cmd /k "cd /d "%~dp0" && python manage.py runserver 127.0.0.1:9000 --noreload --insecure"
echo.
echo Server started! Opening browser...
timeout /t 3 > nul
start http://127.0.0.1:9000/
goto end

:open_folder
echo.
echo Opening project folder...
explorer "%~dp0"
goto end

:end
echo.
echo Thank you for using the Teaching Platform Launcher!
echo.
pause
