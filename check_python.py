"""
Simple script to check if Python is working correctly.
"""

import sys
import os
import platform

print("="*50)
print("Python Diagnostic Tool")
print("="*50)
print()

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Operating system: {platform.system()} {platform.release()}")
print(f"Current directory: {os.getcwd()}")

print("\nChecking for Django installation...")
try:
    import django
    print(f"Django version: {django.get_version()}")
except ImportError:
    print("Django is not installed.")

print("\nChecking for other key packages...")
packages = ["sqlite3", "json", "datetime", "requests"]
for package in packages:
    try:
        __import__(package)
        print(f"✓ {package} is available")
    except ImportError:
        print(f"✗ {package} is not available")

print("\nPython is working correctly!")
print("\nPress Enter to exit...")
input()
