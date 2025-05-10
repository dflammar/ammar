"""
Simple Flask server to test if a different web framework works.
"""

try:
    from flask import Flask, render_template_string
    print("Flask is installed!")
except ImportError:
    print("Flask is not installed. Installing...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask, render_template_string
    print("Flask installed successfully!")

import webbrowser
import threading
import time
import os

# Create Flask app
app = Flask(__name__)

# HTML template
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Test</title>
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
        <h1>Flask Test Server</h1>
        <p class="success">✓ Flask server is working!</p>
        <p>If you can see this page, the Flask server is running correctly.</p>
        <p>This is a different web framework than Django.</p>
        <p>Current time: {{ current_time }}</p>
    </div>
</body>
</html>
"""

# Define route
@app.route('/')
def home():
    from datetime import datetime
    return render_template_string(HTML, current_time=datetime.now().strftime('%H:%M:%S'))

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:3000')

if __name__ == '__main__':
    print("="*50)
    print("Flask Test Server")
    print("="*50)
    print(f"Current directory: {os.getcwd()}")
    
    # Open browser in a separate thread
    threading.Thread(target=open_browser).start()
    
    # Run Flask app
    print("Starting Flask server on port 3000...")
    print("Access the server at: http://127.0.0.1:3000/")
    app.run(host='0.0.0.0', port=3000)
