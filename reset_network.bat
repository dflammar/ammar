@echo off
echo ===============================================
echo    Reset Network Stack
echo ===============================================
echo.

echo This script will reset your network stack.
echo You need to run this script as Administrator.
echo.
echo WARNING: Your internet connection will be temporarily disconnected.
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause > nul

echo.
echo Resetting Winsock...
netsh winsock reset

echo.
echo Resetting IP stack...
netsh int ip reset

echo.
echo Releasing IP address...
ipconfig /release

echo.
echo Renewing IP address...
ipconfig /renew

echo.
echo Flushing DNS cache...
ipconfig /flushdns

echo.
echo Network stack reset complete!
echo.
echo Please restart your computer for the changes to take effect.
echo.
echo Press any key to exit...
pause > nul
