@echo off
echo ===============================================
echo    Simple HTTP Server Test
echo ===============================================
echo.

set PORT=8888

echo Starting simple HTTP server on port %PORT%...
echo.
echo Server will be available at: http://127.0.0.1:%PORT%/
echo.
echo Press Ctrl+C to stop the server
echo.

python -m http.server %PORT%

echo.
echo Server stopped. Press any key to exit...
pause > nul
