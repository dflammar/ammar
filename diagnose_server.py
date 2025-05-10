import os
import sys
import socket
import subprocess
import platform
import time

def print_header(message):
    print("\n" + "=" * 50)
    print(f" {message} ".center(50))
    print("=" * 50)

def check_port(port):
    """Check if a port is in use"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result == 0

def main():
    print_header("Django Server Diagnostic Tool")
    
    # System information
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {sys.version}")
    print(f"Current Directory: {os.getcwd()}")
    
    # Check Python installation
    print_header("Checking Python Installation")
    try:
        python_path = sys.executable
        print(f"Python Path: {python_path}")
        
        # Check if manage.py exists
        if os.path.exists("manage.py"):
            print("✓ manage.py found")
        else:
            print("✗ manage.py not found in current directory")
            
        # Check Django installation
        try:
            import django
            print(f"✓ Django installed (version {django.get_version()})")
        except ImportError:
            print("✗ Django not installed")
            print("Installing Django...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "django==5.2"])
            
        # Check other dependencies
        dependencies = ["django-admin-interface", "django-allauth", "pillow", "pyjwt", "cryptography"]
        for dep in dependencies:
            try:
                __import__(dep.replace("-", "_"))
                print(f"✓ {dep} installed")
            except ImportError:
                print(f"✗ {dep} not installed")
                print(f"Installing {dep}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
    
        # Check port availability
        print_header("Checking Port Availability")
        ports_to_check = [8000, 8080, 8888, 9000]
        available_ports = []
        
        for port in ports_to_check:
            if check_port(port):
                print(f"Port {port} is in use")
            else:
                print(f"Port {port} is available")
                available_ports.append(port)
        
        if not available_ports:
            print("No tested ports are available. Try manually specifying a different port.")
            return
            
        # Try to run the server on an available port
        print_header("Starting Django Server")
        chosen_port = available_ports[0]
        print(f"Attempting to start server on port {chosen_port}")
        
        # Create a settings file to ensure DEBUG is True
        with open("debug_settings.py", "w") as f:
            f.write("DEBUG = True\n")
            f.write("ALLOWED_HOSTS = ['*']\n")
        
        # Try to run the server with --noreload to see errors
        cmd = [sys.executable, "manage.py", "runserver", f"0.0.0.0:{chosen_port}", "--noreload", "--settings=debug_settings"]
        print(f"Running command: {' '.join(cmd)}")
        
        # Run the server in a subprocess
        server_process = subprocess.Popen(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait a bit for the server to start
        time.sleep(5)
        
        # Check if the server is running
        if check_port(chosen_port):
            print(f"✓ Server started successfully on port {chosen_port}")
            print(f"Access the server at: http://127.0.0.1:{chosen_port}/")
            print("\nPress Ctrl+C to stop the server")
            
            # Keep the server running and display output
            try:
                while True:
                    output = server_process.stdout.readline()
                    if output:
                        print(output.strip())
                    error = server_process.stderr.readline()
                    if error:
                        print(f"ERROR: {error.strip()}")
                    
                    # Check if process is still running
                    if server_process.poll() is not None:
                        print("Server process has stopped")
                        break
                        
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("Stopping server...")
                server_process.terminate()
        else:
            print("✗ Server failed to start")
            stdout, stderr = server_process.communicate()
            print("\nServer output:")
            print(stdout)
            print("\nServer errors:")
            print(stderr)
            
    except Exception as e:
        print(f"Error during diagnostics: {str(e)}")
        
    print_header("Diagnostic Complete")
    print("If the server still doesn't work, try the following:")
    print("1. Check your firewall settings")
    print("2. Try running as administrator")
    print("3. Check for any error messages in the output above")
    print("4. Make sure no other Django server is running")
    
if __name__ == "__main__":
    main()
