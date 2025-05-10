"""
Simple HTTP server using Python's built-in http.server module.
This doesn't require Django or any other framework.
"""

import http.server
import socketserver
import os
import webbrowser
import threading
import time

# Create a very simple HTML file to serve
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Python Server Test</title>
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
        <h1>Simple Python Server Test</h1>
        <p class="success">✓ Server is working!</p>
        <p>If you can see this page, your Python HTTP server is running correctly.</p>
        <p>This is a very basic server that doesn't require Django or any other framework.</p>
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

# Write the HTML file
with open("test_server.html", "w") as f:
    f.write(html_content)

# Define the port
PORT = 7000

# Create a custom handler
class TestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override to provide more detailed logging
        print(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}")

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open(f'http://127.0.0.1:{PORT}/test_server.html')

if __name__ == "__main__":
    print("="*50)
    print("Simple Python HTTP Server")
    print("="*50)
    print(f"Current directory: {os.getcwd()}")
    
    # Start server
    try:
        # Open browser in a separate thread
        threading.Thread(target=open_browser).start()
        
        # Create and start server
        print(f"\nStarting server on port {PORT}...")
        print(f"Access the server at: http://127.0.0.1:{PORT}/test_server.html")
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
