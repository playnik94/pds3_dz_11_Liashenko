import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    words = len(data.split(bytes(' , ',encoding='UTF-8')))
    print(" The are " + str(words) + " Words.")
    conn.send(data.upper())
conn.close()