import http.server
import socketserver
import os
import sys

print("=== Simple HTTP Server Test ===")
print(f"Current directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

PORT = 8888
Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server started successfully!")
        print(f"Access the server at: http://127.0.0.1:{PORT}")
        print("Press Ctrl+C to stop the server")
        print("="*50)
        httpd.serve_forever()
except Exception as e:
    print(f"Error starting server: {str(e)}")
    input("Press Enter to exit...")
