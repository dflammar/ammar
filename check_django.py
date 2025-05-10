import os
import sys
import django

print("Python version:", sys.version)
print("Django version:", django.get_version())
print("Current working directory:", os.getcwd())

# Try to set up Django
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teacher_platform.settings')
    django.setup()
    print("Django setup successful")
    
    # Try to import models
    try:
        from core.models import Grade, Course, Lesson, Video
        print("Models imported successfully")
        print("Grades:", Grade.objects.count())
        print("Courses:", Course.objects.count())
        print("Lessons:", Lesson.objects.count())
        print("Videos:", Video.objects.count())
    except Exception as e:
        print("Error importing models:", str(e))
        
except Exception as e:
    print("Django setup error:", str(e))
    
# Check if manage.py exists
if os.path.exists("manage.py"):
    print("manage.py exists")
else:
    print("manage.py does not exist")
    
# List all Python files in the current directory
print("\nPython files in current directory:")
for file in os.listdir("."):
    if file.endswith(".py"):
        print(file)
        
# List all directories
print("\nDirectories in current directory:")
for item in os.listdir("."):
    if os.path.isdir(item):
        print(item)
