"""
Simple HTTP server to test if basic networking works.
This doesn't require Django, just Python's standard library.
"""

import http.server
import socketserver
import os
import webbrowser
from urllib.parse import urlparse, parse_qs

# HTML template for the test page
HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>اختبار الخادم</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #3f51b5;
        }
        .success {
            color: green;
            font-weight: bold;
        }
        button {
            background-color: #3f51b5;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 20px;
        }
        button:hover {
            background-color: #303f9f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>اختبار الخادم</h1>
        <p class="success">✓ الخادم يعمل بنجاح!</p>
        <p>هذا يعني أن جهازك يمكنه تشغيل خادم ويب بشكل صحيح.</p>
        <p>المشكلة قد تكون متعلقة بإعدادات Django أو البيئة الافتراضية.</p>
        
        <h2>الخطوات التالية:</h2>
        <ol style="text-align: right;">
            <li>تأكد من تثبيت Django بشكل صحيح</li>
            <li>تحقق من وجود ملف manage.py في المجلد الصحيح</li>
            <li>تأكد من تنشيط البيئة الافتراضية قبل تشغيل الخادم</li>
            <li>جرب استخدام منفذ مختلف (مثل 8080 أو 8888)</li>
        </ol>
        
        <button onclick="window.location.href='/?test=1'">اختبار الاتصال</button>
        
        <div id="test-result" style="margin-top: 20px;"></div>
    </div>
    
    <script>
        // Check if this is a test request
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('test')) {
            document.getElementById('test-result').innerHTML = 
                '<p class="success">✓ اختبار الاتصال ناجح! الخادم يستجيب للطلبات بشكل صحيح.</p>';
        }
    </script>
</body>
</html>
"""

class TestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML.encode('utf-8'))

def run_server(port=8000):
    try:
        with socketserver.TCPServer(("", port), TestHandler) as httpd:
            print(f"Server running at http://127.0.0.1:{port}/")
            print("If this works but Django doesn't, the issue is with Django, not your network.")
            print("Press Ctrl+C to stop the server.")
            
            # Open browser
            webbrowser.open(f"http://127.0.0.1:{port}/")
            
            # Keep the server running
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"Port {port} is already in use. Trying another port...")
            run_server(port + 1)
        else:
            print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Server stopped.")

if __name__ == "__main__":
    run_server()
