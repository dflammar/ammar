from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.contrib import messages
from django.template.response import TemplateResponse
from django.db.models import Count, Sum
from django.contrib.admin.models import LogEntry
from .models import (
    Grade, Course, Lesson, Video, VideoView, AccessCode,
    PaymentMethod, PaymentPackage, Teacher, TeacherReview,
    Notification, Student, StudentVideoAccess
)

# Custom Admin Site
class EducationAdminSite(admin.AdminSite):
    """Custom admin site with enhanced dashboard"""
    site_header = 'منصة التعليم - لوحة التحكم'
    site_title = 'منصة التعليم'
    index_title = 'لوحة التحكم الرئيسية'

    # تغيير اللغة إلى العربية
    def get_app_list(self, request):
        """
        تخصيص قائمة التطبيقات في لوحة الإدارة
        """
        app_list = super().get_app_list(request)

        # ترجمة أسماء التطبيقات
        app_translations = {
            'Core': 'المنصة التعليمية',
            'Authentication and Authorization': 'المستخدمين والصلاحيات',
            'Account': 'الحسابات',
            'Admin interface': 'واجهة الإدارة',
            'Sites': 'المواقع',
            'Social accounts': 'حسابات التواصل الاجتماعي',
        }

        # ترجمة أسماء النماذج
        model_translations = {
            'Users': 'المستخدمين',
            'Groups': 'المجموعات',
            'Grades': 'الصفوف الدراسية',
            'Courses': 'الكورسات',
            'Lessons': 'الدروس',
            'Videos': 'الفيديوهات',
            'Video views': 'مشاهدات الفيديو',
            'Access codes': 'أكواد الوصول',
            'Teachers': 'المدرسين',
            'Teacher reviews': 'تقييمات المدرسين',
            'Payment methods': 'طرق الدفع',
            'Payment packages': 'باقات الدفع',
            'Notifications': 'الإشعارات',
        }

        # تطبيق الترجمة
        for app in app_list:
            app_label = app['name']
            if app_label in app_translations:
                app['name'] = app_translations[app_label]

            for model in app['models']:
                model_name = model['name']
                if model_name in model_translations:
                    model['name'] = model_translations[model_name]

        return app_list

    def index(self, request, extra_context=None):
        """Override the index to show a custom dashboard"""
        # Get counts for dashboard cards
        student_count = User.objects.filter(is_staff=False).count()
        video_count = Video.objects.count()
        access_code_count = AccessCode.objects.filter(is_used=False).count()
        view_count = VideoView.objects.count()

        # Get course and grade counts
        grade_count = Grade.objects.count()
        course_count = Course.objects.count()
        lesson_count = Lesson.objects.count()

        # Get recent activity
        recent_logs = LogEntry.objects.select_related('content_type', 'user').order_by('-action_time')[:10]

        # Get quick links for common tasks
        quick_links = [
            {
                'title': 'إضافة فيديو جديد',
                'url': '/admin/core/video/add/',
                'icon': 'fas fa-video',
                'color': 'primary',
                'description': 'إضافة فيديو تعليمي جديد'
            },
            {
                'title': 'إنشاء أكواد وصول',
                'url': '/admin/core/accesscode/',
                'icon': 'fas fa-key',
                'color': 'success',
                'description': 'إنشاء أكواد وصول جديدة للطلاب'
            },
            {
                'title': 'إرسال إشعار',
                'url': '/admin/core/notification/add/',
                'icon': 'fas fa-bell',
                'color': 'info',
                'description': 'إرسال إشعار للطلاب'
            },
            {
                'title': 'إضافة طريقة دفع',
                'url': '/admin/core/paymentmethod/add/',
                'icon': 'fas fa-money-bill',
                'color': 'warning',
                'description': 'إضافة طريقة دفع جديدة'
            }
        ]

        # Get helpful tips for admins
        admin_tips = [
            'يمكنك إنشاء 100 كود وصول دفعة واحدة من صفحة أكواد الوصول',
            'تأكد من إضافة صورة مصغرة للفيديوهات لتحسين مظهر المنصة',
            'يمكنك إرسال إشعارات للطلاب لإبلاغهم بالتحديثات الجديدة',
            'تذكر أن الأكواد صالحة لمدة 30 يوم فقط من تاريخ الاستخدام',
            'يمكنك تنظيم الدروس والكورسات باستخدام حقل الترتيب (order)'
        ]

        extra_context = extra_context or {}
        extra_context.update({
            'student_count': student_count,
            'video_count': video_count,
            'access_code_count': access_code_count,
            'view_count': view_count,
            'grade_count': grade_count,
            'course_count': course_count,
            'lesson_count': lesson_count,
            'recent_logs': recent_logs,
            'quick_links': quick_links,
            'admin_tips': admin_tips,
            'title': 'لوحة التحكم الرئيسية',
        })

        return super().index(request, extra_context)

# Create custom admin site instance
admin_site = EducationAdminSite(name='admin')

# Register models with custom admin site
admin_site.register(User, UserAdmin)
admin_site.register(Group)
admin.site.index_title = 'إدارة المنصة'

# Unregister default Group model
admin.site.unregister(Group)

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    """Enhanced User Admin with additional fields and features"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_active', 'date_joined', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    def get_queryset(self, request):
        """Only show non-superuser accounts to regular staff"""
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False)
        return qs

# Re-register User with custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class CourseInline(admin.TabularInline):
    """Inline admin for courses within a grade"""
    model = Course
    extra = 1
    show_change_link = True
    fields = ('name', 'name_ar', 'order')

class LessonInline(admin.TabularInline):
    """Inline admin for lessons within a course"""
    model = Lesson
    extra = 1
    show_change_link = True
    fields = ('title', 'title_ar', 'order')

class VideoInline(admin.TabularInline):
    """Inline admin for videos within a lesson"""
    model = Video
    extra = 1
    show_change_link = True
    readonly_fields = ('secret_code', 'video_preview', 'youtube_id')
    fields = ('title', 'title_ar', 'video_type', 'video_file', 'youtube_url', 'video_preview', 'secret_code', 'order')

    def video_preview(self, obj):
        """Show video thumbnail or placeholder"""
        if obj.thumbnail:
            return format_html('<img src="{}" width="100" />', obj.thumbnail.url)
        elif obj.video_type == 'youtube' and obj.youtube_id:
            return format_html(
                '<a href="https://www.youtube.com/watch?v={}" target="_blank">'
                '<img src="https://img.youtube.com/vi/{}/0.jpg" width="100" />'
                '</a>',
                obj.youtube_id, obj.youtube_id
            )
        elif obj.video_file:
            return format_html('<div style="width:100px;height:60px;background:#000;color:#fff;text-align:center;line-height:60px;">فيديو</div>')
        return "-"
    video_preview.short_description = "معاينة"

@admin.register(Grade, site=admin_site)
class GradeAdmin(admin.ModelAdmin):
    """Admin configuration for Grade model"""
    list_display = ('name', 'name_ar', 'order', 'course_count', 'created_at')
    search_fields = ('name', 'name_ar', 'description')
    list_filter = ('created_at',)
    ordering = ('order',)
    inlines = [CourseInline]

    def course_count(self, obj):
        """Count courses in this grade"""
        count = obj.courses.count()
        return format_html('<span class="badge bg-info">{}</span>', count)
    course_count.short_description = "عدد الكورسات"

@admin.register(Course, site=admin_site)
class CourseAdmin(admin.ModelAdmin):
    """Admin configuration for Course model"""
    list_display = ('name', 'name_ar', 'grade', 'thumbnail_preview', 'lesson_count', 'order', 'created_at')
    search_fields = ('name', 'name_ar', 'description', 'grade__name')
    list_filter = ('grade', 'created_at')
    ordering = ('grade__order', 'order')
    inlines = [LessonInline]

    fieldsets = (
        (None, {
            'fields': ('grade', 'name', 'name_ar', 'description', 'order')
        }),
        ('صورة الغلاف', {
            'fields': ('thumbnail', 'thumbnail_preview'),
            'description': 'أضف صورة غلاف للكورس (ستظهر في قائمة الكورسات)'
        }),
        ('معلومات إضافية', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('thumbnail_preview', 'created_at', 'updated_at')

    def thumbnail_preview(self, obj):
        """Show course thumbnail preview"""
        if obj.thumbnail:
            return format_html('<img src="{}" width="100" />', obj.thumbnail.url)
        return "-"
    thumbnail_preview.short_description = "صورة الغلاف"

    def lesson_count(self, obj):
        """Count lessons in this course"""
        count = obj.lessons.count()
        return format_html('<span class="badge bg-info">{}</span>', count)
    lesson_count.short_description = "عدد الدروس"

@admin.register(Lesson, site=admin_site)
class LessonAdmin(admin.ModelAdmin):
    """Admin configuration for Lesson model"""
    list_display = ('title', 'title_ar', 'course', 'thumbnail_preview', 'video_count', 'order', 'created_at')
    search_fields = ('title', 'title_ar', 'description', 'course__name')
    list_filter = ('course__grade', 'course', 'created_at')
    ordering = ('course__grade__order', 'course__order', 'order')
    inlines = [VideoInline]

    fieldsets = (
        (None, {
            'fields': ('course', 'title', 'title_ar', 'description', 'order')
        }),
        ('صورة الغلاف', {
            'fields': ('thumbnail', 'thumbnail_preview'),
            'description': 'أضف صورة غلاف للدرس (ستظهر في قائمة الدروس)'
        }),
        ('معلومات إضافية', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('thumbnail_preview', 'created_at', 'updated_at')

    def thumbnail_preview(self, obj):
        """Show lesson thumbnail preview"""
        if obj.thumbnail:
            return format_html('<img src="{}" width="100" />', obj.thumbnail.url)
        return "-"
    thumbnail_preview.short_description = "صورة الغلاف"

    def video_count(self, obj):
        """Count videos in this lesson"""
        count = obj.videos.count()
        return format_html('<span class="badge bg-info">{}</span>', count)
    video_count.short_description = "عدد الفيديوهات"

@admin.register(Video, site=admin_site)
class VideoAdmin(admin.ModelAdmin):
    """Admin configuration for Video model"""
    list_display = ('title', 'title_ar', 'lesson', 'thumbnail_preview', 'video_type', 'secret_code', 'view_count', 'uploaded_by', 'created_at', 'generate_access_codes_button')
    search_fields = ('title', 'title_ar', 'description', 'secret_code', 'lesson__title', 'youtube_id')
    list_filter = ('lesson__course__grade', 'lesson__course', 'lesson', 'video_type', 'created_at')
    readonly_fields = ('secret_code', 'video_preview', 'thumbnail_preview', 'cover_preview', 'view_count', 'youtube_id', 'generate_access_codes_button')
    ordering = ('lesson__course__grade__order', 'lesson__course__order', 'lesson__order', 'order')

    def generate_access_codes_button(self, obj):
        """Button to generate access codes for this video"""
        return format_html(
            '<a href="/admin/core/accesscode/?video={}" class="button" style="background-color: #d9534f; color: white;">'
            '<i class="fas fa-key"></i> إنشاء أكواد وصول</a>',
            obj.id
        )
    generate_access_codes_button.short_description = "أكواد الوصول"
    fieldsets = (
        (None, {
            'fields': ('lesson', 'title', 'title_ar', 'description', 'order')
        }),
        ('نوع الفيديو', {
            'fields': ('video_type',),
            'description': 'اختر نوع الفيديو: ملف مرفوع أو فيديو من يوتيوب'
        }),
        ('ملف فيديو', {
            'fields': ('video_file',),
            'classes': ('collapse',),
            'description': 'ارفع ملف فيديو مباشرة إلى الخادم (فقط إذا كان نوع الفيديو "ملف مرفوع")'
        }),
        ('فيديو يوتيوب', {
            'fields': ('youtube_url', 'youtube_id'),
            'description': 'أدخل رابط فيديو يوتيوب (سيتم استخراج معرف الفيديو تلقائيًا)'
        }),
        ('صور الفيديو', {
            'fields': ('video_preview', 'thumbnail', 'thumbnail_preview', 'cover_image', 'cover_preview'),
            'description': 'أضف صور للفيديو: صورة مصغرة (تظهر في القوائم) وصورة غلاف كبيرة (تظهر في صفحة الفيديو)'
        }),
        ('الأمان', {
            'fields': ('secret_code',),
            'description': 'هام جداً: كل فيديو يتطلب كود وصول خاص به. يجب إنشاء أكواد وصول خاصة بهذا الفيديو من صفحة أكواد الوصول. الأكواد تعمل مدى الحياة.',
            'classes': ('alert-danger',),
        }),
        ('معلومات إضافية', {
            'fields': ('uploaded_by', 'created_at', 'updated_at', 'view_count'),
            'classes': ('collapse',),
        }),
    )

    class Media:
        js = ('js/admin/video_form.js',)

    def video_preview(self, obj):
        """Show video preview or placeholder"""
        if obj.video_type == 'youtube' and obj.youtube_id:
            return format_html(
                '<a href="https://www.youtube.com/watch?v={}" target="_blank">'
                '<img src="https://img.youtube.com/vi/{}/0.jpg" width="200" />'
                '</a>',
                obj.youtube_id, obj.youtube_id
            )
        elif obj.video_file:
            return format_html('<div style="width:200px;height:120px;background:#000;color:#fff;text-align:center;line-height:120px;">فيديو</div>')
        return "-"
    video_preview.short_description = "معاينة الفيديو"

    def thumbnail_preview(self, obj):
        """Show video thumbnail preview"""
        if obj.thumbnail:
            return format_html('<img src="{}" width="100" />', obj.thumbnail.url)
        elif obj.video_type == 'youtube' and obj.youtube_id:
            return format_html(
                '<img src="https://img.youtube.com/vi/{}/0.jpg" width="100" />',
                obj.youtube_id
            )
        return "-"
    thumbnail_preview.short_description = "صورة مصغرة"

    def cover_preview(self, obj):
        """Show video cover image preview"""
        if obj.cover_image:
            return format_html('<img src="{}" width="200" />', obj.cover_image.url)
        elif obj.thumbnail:
            return format_html('<img src="{}" width="200" />', obj.thumbnail.url)
        elif obj.video_type == 'youtube' and obj.youtube_id:
            return format_html(
                '<img src="https://img.youtube.com/vi/{}/0.jpg" width="200" />',
                obj.youtube_id
            )
        return "-"
    cover_preview.short_description = "صورة الغلاف"

    def view_count(self, obj):
        """Count views for this video"""
        count = obj.views.count()
        return format_html('<span class="badge bg-success">{}</span>', count)
    view_count.short_description = "عدد المشاهدات"

    def save_model(self, request, obj, form, change):
        """Generate a secret code for new videos and set uploaded_by"""
        if not obj.uploaded_by:
            obj.uploaded_by = request.user
        if not change or not obj.secret_code:  # If new video or no secret code
            obj.generate_secret_code()
        super().save_model(request, obj, form, change)

@admin.register(VideoView, site=admin_site)
class VideoViewAdmin(admin.ModelAdmin):
    """Admin configuration for VideoView model"""
    list_display = ('video', 'user', 'viewed_at', 'ip_address')
    search_fields = ('video__title', 'user__username', 'ip_address')
    list_filter = ('viewed_at', 'video__lesson__course__grade', 'video__lesson__course')
    readonly_fields = ('video', 'user', 'viewed_at', 'ip_address', 'user_agent')
    date_hierarchy = 'viewed_at'

    def has_add_permission(self, request):
        """Disable adding video views manually"""
        return False

# Access Code Admin
@admin.register(AccessCode, site=admin_site)
class AccessCodeAdmin(admin.ModelAdmin):
    """Admin configuration for AccessCode model"""
    list_display = ('code', 'get_code_type_display', 'course', 'video', 'is_used', 'used_by', 'created_by', 'created_at', 'used_at')
    list_filter = ('code_type', 'course', 'video', 'is_used', 'created_at', 'used_at')
    search_fields = ('code', 'course__name', 'course__name_ar', 'video__title', 'video__title_ar', 'used_by__username', 'created_by__username')
    readonly_fields = ('code', 'created_by', 'created_at', 'used_by', 'used_at', 'is_used')

    def get_code_type_display(self, obj):
        """Display the code type in Arabic"""
        return dict(AccessCode.CODE_TYPES).get(obj.code_type, obj.code_type)
    get_code_type_display.short_description = "نوع الكود"

    def has_change_permission(self, request, obj=None):
        """Disable changing access codes"""
        return False

    def get_urls(self):
        """Add custom URL for generating codes"""
        urls = super().get_urls()
        custom_urls = [
            path(
                'generate-codes/',
                self.admin_site.admin_view(self.generate_codes_view),
                name='generate-access-codes',
            ),
        ]
        return custom_urls + urls

    def generate_codes_view(self, request):
        """View for generating multiple access codes"""
        if request.method == 'POST':
            course_id = request.POST.get('course')
            video_id = request.POST.get('video')
            count = int(request.POST.get('count', 100))
            code_type = request.POST.get('code_type', 'video')  # Default to 'video' if not specified

            try:
                if video_id:
                    # إنشاء أكواد لفيديو محدد
                    video = Video.objects.get(id=video_id)
                    course = video.lesson.course

                    # تحديد نوع الكود
                    if code_type == 'single':
                        code_type_name = 'كود فيديو واحد فقط'
                    elif code_type == 'course':
                        code_type_name = 'كود كورس'
                    else:
                        code_type_name = 'كود فيديو'

                    codes = AccessCode.generate_codes(count, request.user, video=video, course=course, code_type=code_type)
                    self.message_user(
                        request,
                        f'تم إنشاء {len(codes)} {code_type_name} بنجاح للفيديو "{video.title_ar}".',
                        messages.SUCCESS
                    )
                elif course_id:
                    # إنشاء أكواد للكورس
                    course = Course.objects.get(id=course_id)

                    # للكورس، نستخدم نوع الكود 'course' دائمًا
                    code_type = 'course'
                    code_type_name = 'كود كورس'

                    codes = AccessCode.generate_codes(count, request.user, course=course, code_type=code_type)
                    self.message_user(
                        request,
                        f'تم إنشاء {len(codes)} {code_type_name} بنجاح للكورس "{course.name_ar}".',
                        messages.SUCCESS
                    )
                else:
                    self.message_user(
                        request,
                        'يجب اختيار كورس أو فيديو لإنشاء الأكواد.',
                        messages.ERROR
                    )
            except Course.DoesNotExist:
                self.message_user(
                    request,
                    'الكورس غير موجود.',
                    messages.ERROR
                )
            except Video.DoesNotExist:
                self.message_user(
                    request,
                    'الفيديو غير موجود.',
                    messages.ERROR
                )
            except Exception as e:
                self.message_user(
                    request,
                    f'حدث خطأ أثناء إنشاء الأكواد: {str(e)}',
                    messages.ERROR
                )

        return HttpResponseRedirect("../")

    def changelist_view(self, request, extra_context=None):
        """Add form for generating codes to the changelist view"""
        extra_context = extra_context or {}

        # Get all courses for the dropdown
        courses = Course.objects.all().order_by('grade__order', 'order')

        # Get all videos for the dropdown
        videos = Video.objects.all().order_by('lesson__course__grade__order', 'lesson__course__order', 'lesson__order', 'order')

        extra_context.update({
            'courses': courses,
            'videos': videos,
            'title': 'أكواد الوصول',
        })

        return super().changelist_view(request, extra_context=extra_context)


# Payment Method Admin
@admin.register(PaymentMethod, site=admin_site)
class PaymentMethodAdmin(admin.ModelAdmin):
    """Admin configuration for PaymentMethod model"""
    list_display = ('name_ar', 'phone_number', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'name_ar', 'phone_number', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'name_ar', 'phone_number', 'description', 'icon', 'is_active')
        }),
        ('معلومات إضافية', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


# Payment Package Admin
@admin.register(PaymentPackage, site=admin_site)
class PaymentPackageAdmin(admin.ModelAdmin):
    """Admin configuration for PaymentPackage model"""
    list_display = ('name_ar', 'price', 'number_of_codes', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'name_ar', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'name_ar', 'description', 'price', 'number_of_codes', 'is_active')
        }),
        ('معلومات إضافية', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


# Notification Admin
@admin.register(Notification, site=admin_site)
class NotificationAdmin(admin.ModelAdmin):
    """Admin configuration for Notification model"""
    list_display = ('title', 'notification_type', 'all_users', 'specific_grade', 'created_by', 'created_at')
    list_filter = ('notification_type', 'all_users', 'is_read', 'created_at')
    search_fields = ('title', 'message', 'created_by__username')
    filter_horizontal = ('specific_users',)
    fieldsets = (
        (None, {
            'fields': ('title', 'message', 'notification_type', 'icon', 'url')
        }),
        ('الجمهور المستهدف', {
            'fields': ('all_users', 'specific_users', 'specific_grade'),
            'description': 'حدد من سيتلقى هذا الإشعار'
        }),
        ('معلومات إضافية', {
            'fields': ('is_read', 'created_by', 'created_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        """Set the created_by field to the current user"""
        if not change:  # Only set created_by for new notifications
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


# StudentVideoAccess Admin
@admin.register(StudentVideoAccess, site=admin_site)
class StudentVideoAccessAdmin(admin.ModelAdmin):
    """Admin for student video access records"""
    list_display = ('student', 'video', 'access_code', 'access_date', 'last_viewed', 'view_count')
    list_filter = ('access_date', 'last_viewed')
    search_fields = ('student__user__username', 'video__title', 'video__title_ar', 'access_code__code')
    readonly_fields = ('student', 'video', 'access_code', 'access_date', 'last_viewed', 'view_count')
    date_hierarchy = 'access_date'

    def has_add_permission(self, request):
        """Disable adding access records manually"""
        return False

    def has_delete_permission(self, request, obj=None):
        """Disable deleting access records"""
        return False