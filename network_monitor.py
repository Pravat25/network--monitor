import os
import platform

def ping_host(host):
    param = "-n 1" if platform.system().lower()=="windows" else "-c 1"
    command = f"ping {param} {host}"

    response = os.system(command)

    if response == 0:
        return "UP"
    else:
        return "DOWN"


hosts = []

print("Enter hosts to monitor (type 'done' when finished)")

while True:
    host = input("Host: ")
    if host.lower() == "done":
        break
    hosts.append(host)

print("\n===== Network Monitoring Report =====\n")

for host in hosts:
    status = ping_host(host)
    print(f"{host} : {status}")
