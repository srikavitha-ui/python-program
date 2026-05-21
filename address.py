import socket
try:
    target_url=input("Enter websitename:")
    target_ip=socket.gethostbyname(target_url)
    print(f"[+]the ip address of{target_url} is {target_ip}")
except socket.gaierror:print("[-] invaild website or dns lookup faild")
