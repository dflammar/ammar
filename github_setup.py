import os
import sys
import subprocess
import webbrowser
import time

def print_header(text):
    print("\n" + "=" * 60)
    print(f" {text} ".center(60, "="))
    print("=" * 60)

def run_command(command):
    print(f"تنفيذ الأمر: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, 
                               capture_output=True)
        print(result.stdout)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"خطأ: {e}")
        print(f"المخرجات: {e.stdout}")
        print(f"رسالة الخطأ: {e.stderr}")
        return False, e.stderr

def check_git_installed():
    print("التحقق من تثبيت Git...")
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        if "git version" in result.stdout:
            print(f"✓ Git مثبت: {result.stdout.strip()}")
            return True
        else:
            print("✗ Git غير مثبت بشكل صحيح")
            return False
    except FileNotFoundError:
        print("✗ Git غير مثبت")
        print("يرجى تثبيت Git من: https://git-scm.com/downloads")
        webbrowser.open("https://git-scm.com/downloads")
        return False

def setup_git_repo():
    print_header("إعداد مستودع Git")
    
    # التحقق من وجود مستودع Git
    if os.path.exists(".git"):
        print("✓ مستودع Git موجود بالفعل")
    else:
        print("تهيئة مستودع Git جديد...")
        success, _ = run_command("git init")
        if not success:
            print("✗ فشل في تهيئة مستودع Git")
            return False
    
    # إنشاء ملف .gitignore
    if not os.path.exists(".gitignore"):
        print("إنشاء ملف .gitignore...")
        with open(".gitignore", "w") as f:
            f.write("""# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media

# Virtual Environment
venv/
ENV/
env/
myenv/
.env
.venv
env.bak/
venv.bak/
fresh_env/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS specific
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
""")
        print("✓ تم إنشاء ملف .gitignore")
    else:
        print("✓ ملف .gitignore موجود بالفعل")
    
    return True

def prepare_for_github():
    print_header("تجهيز المشروع لـ GitHub")
    
    # إضافة الملفات إلى Git
    print("إضافة الملفات إلى Git...")
    success, _ = run_command("git add .")
    if not success:
        print("✗ فشل في إضافة الملفات")
        return False
    
    # إنشاء commit
    print("إنشاء commit...")
    success, _ = run_command('git commit -m "Initial commit - منصة التعليم"')
    if not success:
        print("محاولة تكوين Git...")
        run_command('git config --global user.email "user@example.com"')
        run_command('git config --global user.name "User Name"')
        print("إعادة محاولة إنشاء commit...")
        success, _ = run_command('git commit -m "Initial commit - منصة التعليم"')
        if not success:
            print("✗ فشل في إنشاء commit")
            return False
    
    print("✓ تم تجهيز المشروع بنجاح")
    return True

def create_github_repo():
    print_header("إنشاء مستودع على GitHub")
    print("""
لإنشاء مستودع على GitHub، اتبع الخطوات التالية:

1. قم بزيارة https://github.com/new
2. أدخل اسم المستودع (مثلاً: teaching-platform)
3. أضف وصفًا للمشروع (مثلاً: منصة تعليمية للطلاب والمعلمين)
4. اختر ما إذا كنت تريد أن يكون المستودع عامًا أو خاصًا
5. انقر على "Create repository"
6. بعد إنشاء المستودع، ستظهر لك تعليمات لرفع المشروع

هل تريد فتح صفحة إنشاء مستودع GitHub الآن؟ (نعم/لا): """)
    
    choice = input().strip().lower()
    if choice in ["نعم", "y", "yes"]:
        webbrowser.open("https://github.com/new")
        print("تم فتح صفحة إنشاء مستودع GitHub")
        
        print("\nبعد إنشاء المستودع، أدخل رابط المستودع (مثال: https://github.com/username/repo-name):")
        repo_url = input().strip()
        
        if repo_url:
            print(f"إضافة remote للمستودع: {repo_url}")
            success, _ = run_command(f'git remote add origin {repo_url}')
            if not success:
                print("✗ فشل في إضافة remote")
                return False
            
            print("رفع المشروع إلى GitHub...")
            success, _ = run_command('git push -u origin master')
            if not success:
                # محاولة استخدام main بدلاً من master
                success, _ = run_command('git push -u origin main')
                if not success:
                    print("✗ فشل في رفع المشروع")
                    print("يمكنك محاولة رفع المشروع يدويًا باستخدام الأوامر التالية:")
                    print(f"git remote add origin {repo_url}")
                    print("git push -u origin master")
                    return False
            
            print(f"✓ تم رفع المشروع بنجاح إلى {repo_url}")
            print(f"يمكنك الآن الوصول إلى مشروعك من خلال: {repo_url}")
            
            # فتح صفحة GitHub Pages
            print("\nلتفعيل GitHub Pages واستضافة موقعك:")
            print(f"1. انتقل إلى: {repo_url}/settings/pages")
            print("2. اختر الفرع (Branch) الذي تريد استخدامه (عادةً main أو master)")
            print("3. اختر المجلد (عادةً /(root))")
            print("4. انقر على Save")
            
            print("\nهل تريد فتح صفحة إعدادات GitHub Pages الآن؟ (نعم/لا): ")
            choice = input().strip().lower()
            if choice in ["نعم", "y", "yes"]:
                webbrowser.open(f"{repo_url}/settings/pages")
                print("تم فتح صفحة إعدادات GitHub Pages")
            
            return True
        else:
            print("لم يتم إدخال رابط المستودع")
            return False
    else:
        print("تم إلغاء إنشاء مستودع GitHub")
        return False

def main():
    print_header("إعداد مشروع منصة التعليم على GitHub")
    
    # التحقق من تثبيت Git
    if not check_git_installed():
        print("يرجى تثبيت Git أولاً ثم إعادة تشغيل هذا البرنامج")
        return
    
    # إعداد مستودع Git
    if not setup_git_repo():
        print("فشل في إعداد مستودع Git")
        return
    
    # تجهيز المشروع لـ GitHub
    if not prepare_for_github():
        print("فشل في تجهيز المشروع لـ GitHub")
        return
    
    # إنشاء مستودع على GitHub
    if not create_github_repo():
        print("فشل في إنشاء مستودع GitHub")
        return
    
    print_header("تم الانتهاء")
    print("تم إعداد مشروعك على GitHub بنجاح!")
    print("يمكنك الآن الوصول إلى مشروعك من خلال الرابط الذي أدخلته")

if __name__ == "__main__":
    main()
