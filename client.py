import socket
import sys


host = '127.0.0.1'
port = 8080
buffer_size = 1024
text = "Hello, World!"
if len(sys.argv) > 1:
    text2 = str(sys.argv[1])
else:
    text2 = text
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
text2 = text2.encode('utf-8')
s.send(text2)
data = s.recv(buffer_size)
s.close()
print("received data:", data)