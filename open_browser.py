"""
Simple script to open a web browser to test if basic browser functionality works.
"""

import webbrowser
import time
import os

print("="*50)
print("Browser Test Script")
print("="*50)
print(f"Current directory: {os.getcwd()}")

# Wait a moment
print("Opening browser in 3 seconds...")
time.sleep(3)

# Try to open a browser to a known website
try:
    print("Opening Google...")
    webbrowser.open("https://www.google.com")
    print("Browser opened successfully!")
except Exception as e:
    print(f"Error opening browser: {str(e)}")

print("\nPress Enter to exit...")
input()
