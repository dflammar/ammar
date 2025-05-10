import subprocess
import sys
import os

def run_command(command):
    """Run a command and print its output"""
    print(f"Running: {command}")
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    
    if stdout:
        print(stdout)
    if stderr:
        print(f"Error: {stderr}")
    
    return process.returncode

def main():
    # Install required packages
    packages = [
        "django==5.2",
        "django-admin-interface",
        "django-allauth",
        "pillow",
        "pyjwt",
        "cryptography",
        "requests"
    ]
    
    print("Installing required packages...")
    for package in packages:
        run_command(f"{sys.executable} -m pip install {package}")
    
    # Run the Django server
    print("\nStarting Django server...")
    os.environ['PYTHONUNBUFFERED'] = '1'  # Show output immediately
    
    # Use subprocess.run to keep the process running
    subprocess.run([sys.executable, "manage.py", "runserver", "8080"])

if __name__ == "__main__":
    main()
