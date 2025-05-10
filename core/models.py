from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
import os
import random
import datetime
from django.utils import timezone
from django.db.models import Avg

def video_upload_path(instance, filename):
    """Generate a unique path for uploaded videos"""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('videos', filename)

# We'll implement the custom user model later
# For now, we'll use the default User model

class Student(models.Model):
    """Model representing a student profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True)
    grades = models.ManyToManyField('Grade', related_name='student_profiles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Track which videos this student has accessed
    accessed_videos = models.ManyToManyField('Video', through='StudentVideoAccess', related_name='accessed_by_students')

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}'s Profile"

    def get_courses(self):
        """Get all courses available to this student based on their grades"""
        from django.db.models import Q

        # Get courses from student's grades
        courses = Course.objects.filter(grade__in=self.grades.all())

        # Also include courses the student has access to via access codes
        used_codes = AccessCode.objects.filter(
            used_by=self.user,
            is_used=True
        )
        course_ids_from_codes = used_codes.values_list('course_id', flat=True)

        # Combine both sets of courses
        return courses.filter(Q(id__in=course_ids_from_codes) | Q(grade__in=self.grades.all())).distinct()

    def has_access_to_video(self, video):
        """Check if the student has access to a specific video"""
        return StudentVideoAccess.objects.filter(student=self, video=video).exists()

class Grade(models.Model):
    """Model representing a grade (e.g., First Preparatory Grade)"""
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)  # Arabic name
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)  # For ordering grades
    students = models.ManyToManyField(User, related_name='grades', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Course(models.Model):
    """Model representing a course within a grade"""
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)  # Arabic name
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # For ordering courses
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['grade__order', 'order']

    def __str__(self):
        return f"{self.grade.name} - {self.name}"

class Lesson(models.Model):
    """Model representing a lesson within a course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)  # Arabic title
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='lesson_thumbnails/', blank=True, null=True, help_text="صورة غلاف الدرس")
    order = models.PositiveIntegerField(default=0)  # For ordering lessons
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['course__grade__order', 'course__order', 'order']

    def __str__(self):
        return f"{self.course.name} - {self.title}"

class Video(models.Model):
    """Model for video content uploaded by teachers"""
    VIDEO_TYPE_CHOICES = (
        ('upload', 'Uploaded Video'),
        ('youtube', 'YouTube Video'),
    )

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)  # Arabic title
    description = models.TextField(blank=True)

    # Video source
    video_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default='upload')
    video_file = models.FileField(upload_to=video_upload_path, blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True, help_text="YouTube video URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)")
    youtube_id = models.CharField(max_length=20, blank=True, null=True, help_text="YouTube video ID (automatically extracted from URL)")

    # Display and security
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True, help_text="صورة غلاف الفيديو (ستظهر في قائمة الفيديوهات)")
    cover_image = models.ImageField(upload_to='video_covers/', blank=True, null=True, help_text="صورة غلاف كبيرة للفيديو (ستظهر في صفحة تفاصيل الفيديو)")
    secret_code = models.CharField(max_length=20, unique=True)
    order = models.PositiveIntegerField(default=0)  # For ordering videos

    # Metadata
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Analytics
    view_count = models.PositiveIntegerField(default=0)
    duration = models.PositiveIntegerField(default=0, help_text="Video duration in seconds")

    class Meta:
        ordering = ['lesson__course__grade__order', 'lesson__course__order', 'lesson__order', 'order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Extract YouTube ID from URL if provided
        if self.video_type == 'youtube' and self.youtube_url and not self.youtube_id:
            import re
            youtube_regex = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
            match = re.search(youtube_regex, self.youtube_url)
            if match:
                self.youtube_id = match.group(1)

        # Ensure at least one video source is provided
        if self.video_type == 'upload' and not self.video_file:
            raise ValueError("Uploaded video file is required for upload video type")
        elif self.video_type == 'youtube' and not self.youtube_url:
            raise ValueError("YouTube URL is required for YouTube video type")

        super().save(*args, **kwargs)

    def generate_secret_code(self):
        """Generate a random secret code for the video"""
        code = str(uuid.uuid4())[:8].upper()
        self.secret_code = code
        self.save()
        return code

    def increment_view_count(self):
        """Increment the view count for this video"""
        self.view_count += 1
        self.save(update_fields=['view_count'])
        return self.view_count

class VideoView(models.Model):
    """Model to track video views"""
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)

    # Analytics data
    watch_duration = models.PositiveIntegerField(default=0, help_text="Time watched in seconds")
    completed = models.BooleanField(default=False, help_text="Whether the video was watched to completion")
    device_type = models.CharField(max_length=20, blank=True, help_text="Device type (desktop, mobile, tablet)")

    class Meta:
        ordering = ['-viewed_at']

    def __str__(self):
        return f"{self.user.username} viewed {self.video.title} at {self.viewed_at}"

    def save(self, *args, **kwargs):
        # Increment video view count on first save
        if not self.pk:  # If this is a new record
            self.video.increment_view_count()

        # Detect device type from user agent
        if self.user_agent and not self.device_type:
            ua_lower = self.user_agent.lower()
            if 'mobile' in ua_lower:
                self.device_type = 'mobile'
            elif 'tablet' in ua_lower:
                self.device_type = 'tablet'
            else:
                self.device_type = 'desktop'

        super().save(*args, **kwargs)


class AccessCode(models.Model):
    """Model for access codes that can be used to unlock videos"""
    CODE_TYPES = (
        ('video', 'كود فيديو'),
        ('course', 'كود كورس'),
        ('single', 'كود فيديو واحد فقط')
    )

    code = models.CharField(max_length=20, unique=True)
    code_type = models.CharField(max_length=10, choices=CODE_TYPES, default='video', help_text="نوع الكود")
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='access_codes')
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='access_codes', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    used_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='used_codes')
    used_at = models.DateTimeField(null=True, blank=True)
    is_used = models.BooleanField(default=False)
    expires_at = models.DateTimeField(null=True, blank=True, help_text="تاريخ انتهاء صلاحية الكود (يستخدم مرة واحدة فقط)")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        status = "مستخدم" if self.is_used else "غير مستخدم"
        if self.video:
            return f"كود {self.code} - {self.video.title_ar} - {status}"
        else:
            return f"كود {self.code} - {self.course.name_ar} - {status}"

    def mark_as_used(self, user, expiry_days=14):
        """Mark this code as used by a specific user"""
        if not self.is_used:
            self.is_used = True
            self.used_by = user
            self.used_at = timezone.now()

            # Set expiry date if specified (default: 14 days)
            if expiry_days > 0:
                self.expires_at = self.used_at + datetime.timedelta(days=expiry_days)

            # كود يستخدم مرة واحدة فقط
            self.save()
            return True
        return False

    def is_expired(self):
        """Check if the access code has expired"""
        # If expires_at is not set, the code never expires
        if not self.expires_at:
            return False

        # Check if the code has expired
        return timezone.now() > self.expires_at

    def set_expiry(self, days=14):
        """Set the expiry date for this code"""
        if not self.used_at:
            return False

        # Set expiry date from used_at date
        self.expires_at = self.used_at + datetime.timedelta(days=days)
        self.save(update_fields=['expires_at'])
        return True

    @classmethod
    def generate_codes(cls, count, created_by, video=None, course=None, code_type=None):
        """Generate a specified number of random access codes for a specific video or course"""
        if not video and not course:
            raise ValueError("يجب تحديد فيديو أو كورس لإنشاء الأكواد")

        if video:
            course = video.lesson.course

        # تحديد نوع الكود
        if not code_type:
            if video:
                code_type = 'video'
            else:
                code_type = 'course'

        codes = []
        for _ in range(count):
            while True:
                # Generate a random 8-character code
                code = ''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ23456789', k=8))
                if not cls.objects.filter(code=code).exists():
                    break

            access_code = cls.objects.create(
                code=code,
                code_type=code_type,
                course=course,
                video=video,
                created_by=created_by
            )
            codes.append(code)  # Append the code string, not the object

        return codes


class Teacher(models.Model):
    """Model representing a teacher"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)  # Arabic name
    bio = models.TextField(blank=True)
    bio_ar = models.TextField(blank=True)  # Arabic bio
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True)
    specialization_ar = models.CharField(max_length=100, blank=True)  # Arabic specialization
    courses = models.ManyToManyField(Course, related_name='teachers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def average_rating(self):
        """Calculate the average rating for this teacher"""
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    def total_reviews(self):
        """Get the total number of reviews for this teacher"""
        return self.reviews.count()


class TeacherReview(models.Model):
    """Model for student reviews of teachers"""
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        # Ensure a student can only review a teacher once
        unique_together = ['teacher', 'student']

    def __str__(self):
        return f"{self.student.username}'s review of {self.teacher.name} - {self.rating} stars"


class PaymentMethod(models.Model):
    """Model for payment methods"""
    name = models.CharField(max_length=100)  # e.g., "Vodafone Cash"
    name_ar = models.CharField(max_length=100)  # Arabic name
    phone_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default="fas fa-money-bill")  # Font Awesome icon
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_ar}: {self.phone_number}"


class PaymentPackage(models.Model):
    """Model for payment packages"""
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_codes = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_ar} - {self.price} جنيه - {self.number_of_codes} كود"


class Assignment(models.Model):
    """Model for assignments and exams"""
    ASSIGNMENT_TYPES = (
        ('homework', 'واجب منزلي'),
        ('exam', 'امتحان'),
        ('quiz', 'اختبار قصير'),
        ('project', 'مشروع'),
    )

    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)  # Arabic title
    description = models.TextField(blank=True)
    assignment_type = models.CharField(max_length=20, choices=ASSIGNMENT_TYPES, default='homework')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    google_sheet_url = models.URLField(blank=True, null=True, help_text="رابط ملف Google Sheets للواجب أو الامتحان")
    google_form_url = models.URLField(blank=True, null=True, help_text="رابط نموذج Google Forms للواجب أو الامتحان")
    due_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_assignments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title_ar} - {self.get_assignment_type_display()}"


class StudentVideoAccess(models.Model):
    """Model to track which videos a student has accessed with which codes"""
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='video_access_records')
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='student_access_records')
    access_code = models.ForeignKey('AccessCode', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_access_records')
    access_date = models.DateTimeField(auto_now_add=True)
    last_viewed = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['student', 'video']
        ordering = ['-access_date']

    def __str__(self):
        return f"{self.student.user.username} accessed {self.video.title} with code {self.access_code.code if self.access_code else 'N/A'}"

    def increment_view_count(self):
        """Increment the view count for this access record"""
        self.view_count += 1
        self.save(update_fields=['view_count', 'last_viewed'])
        return self.view_count


class Notification(models.Model):
    """Model for notifications to users"""
    NOTIFICATION_TYPES = (
        ('info', 'معلومات'),
        ('success', 'نجاح'),
        ('warning', 'تحذير'),
        ('danger', 'خطر'),
    )

    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES, default='info')
    icon = models.CharField(max_length=50, default="fas fa-bell")  # Font Awesome icon
    url = models.CharField(max_length=200, blank=True)  # Optional URL to redirect to

    # Target audience
    all_users = models.BooleanField(default=False)  # Send to all users
    specific_users = models.ManyToManyField(User, related_name='user_notifications', blank=True)  # Or specific users
    specific_grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True, related_name='grade_notifications')  # Or specific grade

    is_read = models.BooleanField(default=False)  # Whether the notification has been read
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Get the URL for this notification"""
        if self.url:
            return self.url
        return "#"
