from django.urls import path
from django.shortcuts import render
from . import views
from . import views_simple  # Import our simple views for testing

app_name = 'core'

urlpatterns = [
    # Simple test views
    path('simple/', views_simple.home_view, name='simple_home'),
    path('simple/test/', views_simple.test_view, name='simple_test'),
    path('simple/video/', views_simple.video_test, name='simple_video'),
    # Authentication URLs
    path('', views.home, name='home'),
    path('test/', views.test_view, name='test'),
    path('register/', views.register_view, name='register'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Content browsing URLs
    path('grades/', views.grades_view, name='grades'),
    path('grade/<int:grade_id>/', views.grade_detail_view, name='grade_detail'),
    path('courses/', views.course_list_view, name='course_list'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('lesson/<int:lesson_id>/', views.lesson_detail_view, name='lesson_detail'),
    path('video/<int:video_id>/', views.video_detail_view, name='video_detail'),
    path('video/<int:video_id>/stream/', views.video_stream_view, name='video_stream'),

    # Admin URLs
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('video/<int:video_id>/generate-code/', views.generate_video_code, name='generate_video_code'),
    path('admin/add-teacher/', views.add_teacher, name='add_teacher'),
    path('admin/generate-bulk-codes/', views.generate_bulk_access_codes, name='generate_bulk_access_codes'),
    path('admin/bulk-codes-result/', views.bulk_codes_result, name='bulk_codes_result'),

    # Teacher evaluation URLs
    path('teachers/', views.teachers_list_view, name='teachers_list'),
    path('teacher/<int:teacher_id>/', views.teacher_detail_view, name='teacher_detail'),
    path('teacher/<int:teacher_id>/review/', views.teacher_review_view, name='teacher_review'),

    # Teacher dashboard URLs
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher-dashboard/course/<int:course_id>/', views.teacher_course_detail, name='teacher_course_detail'),
    path('teacher-dashboard/edit-profile/', views.edit_teacher_profile, name='edit_teacher_profile'),

    # Payment URLs
    path('payment/', views.payment_view, name='payment'),

    # Notification URLs
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/<int:notification_id>/mark-read/', views.mark_notification_read, name='mark_notification_read'),

    # Profile URLs
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # Assignment URLs
    path('assignments/create/', views.create_assignment_view, name='create_assignment'),

    # Contact form URL
    path('contact/', views.contact_view, name='contact'),

    # API endpoints
    path('api/check-phone-exists/', views.check_phone_exists, name='check_phone_exists'),
    path('api/video-analytics/', views.video_analytics, name='video_analytics'),
    path('api/grade/<int:grade_id>/courses/', views.get_courses_by_grade, name='get_courses_by_grade'),
    path('api/courses/<int:course_id>/lessons/', views.get_lessons_by_course, name='get_lessons_by_course'),

    # Test views
    path('test-video/', lambda request: render(request, 'core/test_video.html'), name='test_video'),
]
