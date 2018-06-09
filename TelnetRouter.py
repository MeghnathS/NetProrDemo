import getpass
import telnetlib

HOST = input("")
user = input("")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"hostname ROUTER1\n")
tn.write(b"int loopback 0\n")
tn.write(b"ip address 192.168.10.1 255.255.255.0\n")
tn.write(b"no shut\n")
tn.write(b"int loopback 1\n")
tn.write(b"ip address 192.168.20.1 255.255.255.0\n")
tn.write(b"no shut\n")
tn.write(b"end\n")
tn.write(b"copy run star\n")
tn.write(b"\n")
tn.write(b"\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))
