import socket

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result == 0

ports_to_check = [8000, 8080, 9000, 7000]

print("Checking if ports are in use:")
for port in ports_to_check:
    if check_port(port):
        print(f"Port {port} is in use")
    else:
        print(f"Port {port} is available")

print("\nTrying to start a simple server on port 8000:")
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8000))
    server.listen(5)
    print("Successfully started server on port 8000")
    server.close()
except Exception as e:
    print(f"Failed to start server on port 8000: {e}")
