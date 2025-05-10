@echo off
echo ===============================================
echo    Fix Hosts File
echo ===============================================
echo.

echo This script will fix your hosts file to properly resolve localhost.
echo You need to run this script as Administrator.
echo.

echo Creating temporary hosts file...
echo # Copyright (c) 1993-2009 Microsoft Corp. > %TEMP%\hosts.new
echo # >> %TEMP%\hosts.new
echo # This is a sample HOSTS file used by Microsoft TCP/IP for Windows. >> %TEMP%\hosts.new
echo # >> %TEMP%\hosts.new
echo # This file contains the mappings of IP addresses to host names. Each >> %TEMP%\hosts.new
echo # entry should be kept on an individual line. The IP address should >> %TEMP%\hosts.new
echo # be placed in the first column followed by the corresponding host name. >> %TEMP%\hosts.new
echo # The IP address and the host name should be separated by at least one >> %TEMP%\hosts.new
echo # space. >> %TEMP%\hosts.new
echo # >> %TEMP%\hosts.new
echo # Additionally, comments (such as these) may be inserted on individual >> %TEMP%\hosts.new
echo # lines or following the machine name denoted by a '#' symbol. >> %TEMP%\hosts.new
echo # >> %TEMP%\hosts.new
echo # For example: >> %TEMP%\hosts.new
echo # >> %TEMP%\hosts.new
echo #      102.54.94.97     rhino.acme.com          # source server >> %TEMP%\hosts.new
echo #       38.25.63.10     x.acme.com              # x client host >> %TEMP%\hosts.new
echo. >> %TEMP%\hosts.new
echo # localhost name resolution is handled within DNS itself. >> %TEMP%\hosts.new
echo 127.0.0.1       localhost >> %TEMP%\hosts.new
echo ::1             localhost >> %TEMP%\hosts.new

echo.
echo Attempting to copy the new hosts file...
echo.
echo Please run this script as Administrator by right-clicking on it and selecting "Run as administrator"
echo.

copy %TEMP%\hosts.new C:\Windows\System32\drivers\etc\hosts
if %ERRORLEVEL% NEQ 0 (
    echo Failed to copy the hosts file. Please run this script as Administrator.
    echo.
    echo Alternatively, you can manually edit the hosts file:
    echo 1. Open Notepad as Administrator
    echo 2. Open the file: C:\Windows\System32\drivers\etc\hosts
    echo 3. Uncomment these lines by removing the # at the beginning:
    echo    127.0.0.1       localhost
    echo    ::1             localhost
    echo 4. Save the file
) else (
    echo Hosts file updated successfully!
)

echo.
echo Press any key to exit...
pause > nul
