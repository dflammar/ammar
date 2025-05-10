"""
Simple views for testing the server.
"""

from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    """Simple home view for testing."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>منصة التعليم</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                text-align: center;
                background-color: #f5f5f5;
                direction: rtl;
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
                color: #3f51b5;
            }
            .success {
                color: green;
                font-weight: bold;
            }
            .btn {
                display: inline-block;
                background-color: #3f51b5;
                color: white;
                padding: 10px 15px;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>منصة التعليم</h1>
            <p class="success">✓ الخادم يعمل بنجاح!</p>
            <p>إذا كنت ترى هذه الصفحة، فإن خادم Django يعمل بشكل صحيح.</p>
            <p>هذه صفحة بسيطة للتأكد من أن الخادم يعمل.</p>
            <a href="/admin/" class="btn">لوحة التحكم</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def test_view(request):
    """Simple test view."""
    return HttpResponse("<h1>صفحة الاختبار</h1><p>هذه صفحة اختبار بسيطة.</p>")

def video_test(request):
    """Test view for video page."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>اختبار الفيديو</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                text-align: center;
                background-color: #f5f5f5;
                direction: rtl;
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
                color: #3f51b5;
            }
            .video-container {
                position: relative;
                padding-bottom: 56.25%;
                height: 0;
                overflow: hidden;
                margin: 20px 0;
            }
            .video-container iframe {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }
            .btn {
                display: inline-block;
                background-color: #3f51b5;
                color: white;
                padding: 10px 15px;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>اختبار الفيديو</h1>
            <div class="video-container">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <p>هذه صفحة اختبار لعرض الفيديو.</p>
            <a href="/" class="btn">العودة للصفحة الرئيسية</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
