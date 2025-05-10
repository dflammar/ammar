@echo off
echo ===============================================
echo    Check Proxy Settings
echo ===============================================
echo.

echo Checking Windows proxy settings...
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer

echo.
echo If ProxyEnable is 0x1, proxy is enabled.
echo If ProxyEnable is 0x0, proxy is disabled.
echo.
echo If proxy is enabled, you may need to disable it or add exceptions for localhost.
echo.
echo To disable proxy in Firefox:
echo 1. Open Firefox
echo 2. Click the menu button (three lines) in the top right
echo 3. Select "Settings"
echo 4. Scroll down to "Network Settings" and click "Settings..."
echo 5. Select "No proxy" or "Use system proxy settings"
echo 6. Click "OK"
echo.
echo Press any key to exit...
pause > nul
