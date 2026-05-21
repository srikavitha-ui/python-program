import socket
s=socket.socket()
s.settimeout(5)
status=s.connect_ex(("127.0.0.1",3307))
if status==0:
 print("[+] port 80 is open")
else:
 print("[-] port 80 is closed")
 print(f"error code:{status}")
if status==10061:
 print("f reason:connection refused")
elif status==10060:
 print("reason:connetion is timeout")
elif status==10035:
 print("reasdon:opewrtion would block")
else:
 print("reason unknown")
