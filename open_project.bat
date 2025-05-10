@echo off
echo ===============================================
echo    Open Teaching Platform Project
echo ===============================================
echo.

echo This script will help you open your project files.
echo.

:menu
echo Please select an option:
echo 1. Open project folder in File Explorer
echo 2. Open project in Visual Studio Code (if installed)
echo 3. Open project in PyCharm (if installed)
echo 4. Open HTML files directly in browser
echo 5. Exit
echo.

set /p choice=Enter your choice (1-5): 

if "%choice%"=="1" goto open_folder
if "%choice%"=="2" goto open_vscode
if "%choice%"=="3" goto open_pycharm
if "%choice%"=="4" goto open_html
if "%choice%"=="5" goto end

echo Invalid choice. Please try again.
echo.
goto menu

:open_folder
echo Opening project folder...
start explorer "%~dp0"
goto end

:open_vscode
echo Checking if Visual Studio Code is installed...
where code >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Opening project in Visual Studio Code...
    start code "%~dp0"
) else (
    echo Visual Studio Code is not installed or not in PATH.
    echo You can download it from: https://code.visualstudio.com/
)
goto end

:open_pycharm
echo Checking for PyCharm installation...
if exist "C:\Program Files\JetBrains\PyCharm*" (
    echo Opening project in PyCharm...
    start "" "C:\Program Files\JetBrains\PyCharm*\bin\pycharm64.exe" "%~dp0"
) else (
    echo PyCharm not found in the default installation directory.
    echo You can download it from: https://www.jetbrains.com/pycharm/
)
goto end

:open_html
echo Opening HTML files directly in browser...
echo.
echo Select which HTML file to open:
echo 1. Main page (index.html)
echo 2. Login page
echo 3. Registration page
echo 4. Back to main menu
echo.

set /p html_choice=Enter your choice (1-4): 

if "%html_choice%"=="1" (
    if exist "%~dp0\templates\index.html" (
        start "" "%~dp0\templates\index.html"
    ) else if exist "%~dp0\core\templates\core\index.html" (
        start "" "%~dp0\core\templates\core\index.html"
    ) else if exist "%~dp0\core\templates\core\home.html" (
        start "" "%~dp0\core\templates\core\home.html"
    ) else (
        echo Could not find index.html file.
    )
) else if "%html_choice%"=="2" (
    if exist "%~dp0\core\templates\core\login.html" (
        start "" "%~dp0\core\templates\core\login.html"
    ) else (
        echo Could not find login.html file.
    )
) else if "%html_choice%"=="3" (
    if exist "%~dp0\core\templates\core\register.html" (
        start "" "%~dp0\core\templates\core\register.html"
    ) else (
        echo Could not find register.html file.
    )
) else if "%html_choice%"=="4" (
    goto menu
) else (
    echo Invalid choice.
)
goto end

:end
echo.
echo Press any key to exit...
pause > nul
