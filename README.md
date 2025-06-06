# منصة التعليم

منصة تعليمية متكاملة تتيح للطلاب مشاهدة الفيديوهات التعليمية وتقييم المعلمين.

## المميزات

- نظام تسجيل دخول وتسجيل مستخدمين جديد
- دعم تسجيل الدخول باستخدام حساب Google
- عرض الفيديوهات التعليمية بطريقة آمنة
- نظام أكواد الوصول للفيديوهات
- لوحة تحكم للمشرفين لإدارة المحتوى
- نظام تقييم المعلمين
- وضع مظلم (Dark Mode)
- تصميم متجاوب يعمل على جميع الأجهزة

## متطلبات التشغيل

- Python 3.8+
- Django 5.2
- قاعدة بيانات (SQLite للتطوير، PostgreSQL للإنتاج)

## التثبيت

1. قم بتنزيل المشروع أو استنساخه:

```bash
git clone https://github.com/yourusername/teaching-platform.git
cd teaching-platform
```

2. قم بإنشاء بيئة افتراضية وتفعيلها:

```bash
python -m venv venv
source venv/bin/activate  # على Linux/Mac
venv\Scripts\activate  # على Windows
```

3. قم بتثبيت المتطلبات:

```bash
pip install -r requirements.txt
```

4. قم بإجراء عمليات الترحيل لقاعدة البيانات:

```bash
python manage.py migrate
```

5. قم بإنشاء مستخدم مشرف:

```bash
python manage.py createsuperuser
```

6. قم بتشغيل الخادم المحلي:

```bash
python manage.py runserver
```

## الإعداد للإنتاج

1. قم بتعديل ملف `teacher_platform/settings.py`:
   - قم بتغيير `DEBUG = False`
   - قم بتعيين `ALLOWED_HOSTS` بنطاق موقعك
   - قم بتعيين مفتاح سري آمن لـ `SECRET_KEY`

2. قم بجمع الملفات الثابتة:

```bash
python manage.py collectstatic
```

3. قم بإعداد قاعدة بيانات PostgreSQL بدلاً من SQLite

4. قم بإعداد خادم WSGI مثل Gunicorn:

```bash
pip install gunicorn
gunicorn teacher_platform.wsgi:application
```

5. قم بإعداد خادم Nginx كواجهة أمامية

## المساهمة

نرحب بمساهماتكم! يرجى اتباع الخطوات التالية:

1. قم بعمل Fork للمشروع
2. قم بإنشاء فرع جديد (`git checkout -b feature/amazing-feature`)
3. قم بإجراء التغييرات وحفظها (`git commit -m 'Add some amazing feature'`)
4. قم برفع التغييرات (`git push origin feature/amazing-feature`)
5. قم بفتح طلب سحب (Pull Request)

## الترخيص

هذا المشروع مرخص تحت رخصة MIT - انظر ملف LICENSE للتفاصيل.

## الاتصال

عمار محمود - Telegram: @d_f_l
#   a m m a r  
 #   m m  
 