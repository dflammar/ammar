@echo off
echo ===============================================
echo    Check Port Usage
echo ===============================================
echo.

echo Checking if common web server ports are in use...
echo.

echo Checking port 3000...
netstat -ano | findstr :3000
if %ERRORLEVEL% EQU 0 (
    echo Port 3000 is in use!
) else (
    echo Port 3000 is available.
)

echo.
echo Checking port 8000...
netstat -ano | findstr :8000
if %ERRORLEVEL% EQU 0 (
    echo Port 8000 is in use!
) else (
    echo Port 8000 is available.
)

echo.
echo Checking port 8080...
netstat -ano | findstr :8080
if %ERRORLEVEL% EQU 0 (
    echo Port 8080 is in use!
) else (
    echo Port 8080 is available.
)

echo.
echo Checking port 8888...
netstat -ano | findstr :8888
if %ERRORLEVEL% EQU 0 (
    echo Port 8888 is in use!
) else (
    echo Port 8888 is available.
)

echo.
echo Port check complete!
echo.
echo Press any key to exit...
pause > nul
