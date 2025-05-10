import os
import sys
import django

print(f"Django version: {django.get_version()}")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print(f"Python path: {sys.path}")
