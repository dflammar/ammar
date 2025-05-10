import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teacher_platform.settings')
django.setup()

# Import models
from core.models import Teacher, Course, Lesson, Video, VideoView, AccessCode, TeacherReview, Student, StudentVideoAccess

# Test Teacher model
print("Testing Teacher model...")
teachers = Teacher.objects.all()
print(f"Found {len(teachers)} teachers")

# Test Course model
print("\nTesting Course model...")
courses = Course.objects.all()
print(f"Found {len(courses)} courses")

# Test Lesson model
print("\nTesting Lesson model...")
lessons = Lesson.objects.all()
print(f"Found {len(lessons)} lessons")

# Test Video model
print("\nTesting Video model...")
videos = Video.objects.all()
print(f"Found {len(videos)} videos")

# Test AccessCode model
print("\nTesting AccessCode model...")
access_codes = AccessCode.objects.all()
print(f"Found {len(access_codes)} access codes")

# Test StudentVideoAccess model
print("\nTesting StudentVideoAccess model...")
student_video_access = StudentVideoAccess.objects.all()
print(f"Found {len(student_video_access)} student video access records")

print("\nAll tests completed successfully!")
