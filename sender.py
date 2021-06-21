import socket
s=socket.(socket.AF_INET,socket.SOCK_DGRAM)
recv_addr=(("127.0.0.1,9999"))
user_data= input("Enter your message:-")
new_data= user_data.encode(ascii)
s.sento(user_data, rec_addr)
print("your message has been sent")