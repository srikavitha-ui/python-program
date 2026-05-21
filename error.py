import socket
 
s = socket.socket()
 
s.settimeout(1)
 
status = s.connect_ex(("127.0.0.1", 3307))
 
if status == 0:
	print("[+] Port 80 is OPEN")
else:
	print(f"[-] Port 80 is CLOSED | Error Code: {status}")
 
