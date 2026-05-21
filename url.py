import socket
targeturl="instagram.com"
targetip=socket.gethostbyname(targeturl)
print(f"[+] the ip address of {targeturl}is {targetip}")
