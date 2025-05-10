"""
Simple HTTP server using a high port number (50000) to avoid conflicts.
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os

# HTML content
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>High Port Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            text-align: center;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1 {
            color: #4285f4;
        }
        .success {
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>High Port Test Server</h1>
        <p class="success">✓ Server is working on port 50000!</p>
        <p>If you can see this page, your server and browser are working correctly.</p>
        <p>This server is using port 50000, which is in the dynamic port range and should not be blocked.</p>
        <p>Current time: <span id="current-time"></span></p>
    </div>
    
    <script>
        // Display current time
        function updateTime() {
            document.getElementById('current-time').textContent = new Date().toLocaleTimeString();
        }
        updateTime();
        setInterval(updateTime, 1000);
    </script>
</body>
</html>
"""

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML.encode())
    
    def log_message(self, format, *args):
        # Override to provide more detailed logging
        print(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}")

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:50000')

if __name__ == "__main__":
    PORT = 50000
    
    print("="*50)
    print("High Port Test Server")
    print("="*50)
    print(f"Current directory: {os.getcwd()}")
    
    # Check if port is available
    try:
        with socketserver.TCPServer(("", PORT), None) as test_server:
            pass
        print(f"Port {PORT} is available")
    except OSError:
        print(f"WARNING: Port {PORT} is already in use")
        print("Please close any applications using this port and try again")
        input("Press Enter to exit...")
        exit()
    
    # Start server
    try:
        # Open browser in a separate thread
        threading.Thread(target=open_browser).start()
        
        # Create and start server
        print(f"\nStarting server on port {PORT}...")
        print(f"Access the server at: http://127.0.0.1:{PORT}/")
        print("Press Ctrl+C to stop the server")
        print("="*50)
        
        with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"\nError: {str(e)}")
    
    print("\nServer stopped. Press Enter to exit...")
    input()
