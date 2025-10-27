---
title: Siemens Energy Omnivise T3000 8.2 SP3 Privilege Escalation / File Download
url: https://cxsecurity.com/issue/WLB-2024110021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-15
fetch_date: 2025-10-06T19:17:01.122232
---

# Siemens Energy Omnivise T3000 8.2 SP3 Privilege Escalation / File Download

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
|  |  | |  | | --- | | **Siemens Energy Omnivise T3000 8.2 SP3 Privilege Escalation / File Download** **2024.11.14**  Credit:  **[Andreas Kolbeck](https://cxsecurity.com/author/Andreas%2BKolbeck/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-38879](https://cxsecurity.com/cveshow/CVE-2024-38879/ "Click to see CVE-2024-38879")** | **[CVE-2024-38876](https://cxsecurity.com/cveshow/CVE-2024-38876/ "Click to see CVE-2024-38876")** | **[CVE-2024-38877](https://cxsecurity.com/cveshow/CVE-2024-38877/ "Click to see CVE-2024-38877")** | **[CVE-2024-38878](https://cxsecurity.com/cveshow/CVE-2024-38878/ "Click to see CVE-2024-38878")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

SEC Consult Vulnerability Lab Security Advisory < 20241112-0 >
=======================================================================
title: Multiple vulnerabilities
product: Siemens Energy Omnivise T3000
vulnerable version: >=8.2 SP3
fixed version: see solution section
CVE number: CVE-2024-38876, CVE-2024-38877, CVE-2024-38878, CVE-2024-38879
impact: High
homepage: https://www.siemens-energy.com/global/en/home/products-services/product/omnivise-t3000.html
found: 2024-06-02
by: Steffen Robertz (Office Vienna)
Andreas Kolbeck (Office Munich)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Located in 90 countries, Siemens Energy operates across the whole energy landscape.
From conventional to renewable power, from grid technology to storage to electrifying
complex industrial processes.
Our mission is to support companies and countries with what they need to reduce
greenhouse gas emissions and make energy reliable, affordable, and more sustainable.
Let’s energize society."
Source: https://www.siemens-energy.com/global/en/home/company/about.html
Business recommendation:
------------------------
Siemens has released their security advisory SSA-857368, see the following URL
for further details:
https://cert-portal.siemens.com/productcert/html/ssa-857368.html#mitigations-section
Follow the mitigation instructions communicated in Omnivise T3000 Technical News 2024-089
and SE Controls Security Announcement 2024-01.
SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.
Vulnerability overview/description:
-----------------------------------
1) Local Privilege Escalation via Writable Service Binary (CVE-2024-38876)
Insecurely configured services or the insecure configuration of their authorizations
lead to privilege escalation vulnerabilities in the Windows operating system. It is
possible for a low-privileged user to modify a service in such a way that it executes
arbitrary code instead of starting the actual service. The service path is writable by
the "Authenticated Users" group.
Precondition for exploitation: requires authenticated local access to the Terminal Server
of the T3000 system.
2) Cleartext Storage of Passwords in Config and Log Files (CVE-2024-38877)
Multiple files containing cleartext passwords were discovered. These can be used
to jump from host to host and thus compromise the whole security architecture of
the T3000 system.
Precondition for exploitation: requires administrative local access to any server of the
T3000 system.
3) File System Access via RemoteDiagnosticView Website (CVE-2024-38878)
The RemoteDiagnosticView application is a web application hosted on the application
server. One parameter accepts a full path, which can be abused to download arbitrary
files.
Precondition for exploitation: requires administrative remote access to the Application
server of the T3000 system.
4) IP Whitelist Bypass (CVE-2024-38879)
The application server is hosting the T3000 web application on port 8080. However,
only the Terminal Server is whitelisted. This whitelisting can be circumvented by
exploiting the additionally exposed Tomcat AJP service on port 8009.
Precondition for exploitation: requires unauthenticated remote access to the Application
server of the T3000 system
Proof of concept:
-----------------
1) Local Privilege Escalation via Writable Service Binary (CVE-2024-38876)
The following path hosts a file that is used by the "DSGW Service" of the T3000 system:
"E:\dsgw\gw\bin\dsgwservice.exe"
The path is writable by the "Authenticated Users" group.
2) Cleartext Storage of Passwords in Config and Log Files (CVE-2024-38877)
Multiple files containing cleartext passwords were discovered.
Terminal Server:
\* C:\Program Files\SPPA-T3000\snmpv3trap\Config.properties (only readable by Admin)
\* E:\DSGW\GW\config\_PDC.properties (Passwords are Base64 encoded)
\* C:\Program Files\SPPA-T3000\Logs\AppInstallLogs\PostInstallConfigList.xml (Readable by every user)
Application Server:
\* D:\SPPA-T3000\\_framework\\_jre\installvariables.properties (contains passwords of tomcat and MySQL service
\* D:\SPPA-T3000\Orion\install\\_uninstall\installvariables.properties (contains password for MySQL service and installation)
All Servers:
All servers are being deployed via Puppet. However, the cache file is never
cleared and contains the initial passwords of all systems of the T3000 system:
"C:\Program Data\PuppetLabs\puppet\cache\client\_data\catalog\<uid.json>"
---------------------------------------
[...]
"parameters": {
"foreman\_pass": "[redacted]",
"foreman\_url": "[redacted]",
"foreman\_user": "puppet\_provider",
"is\_sec": "true",
"mpssvc\_pass": "[redacted]"
}
[...]
"parameters": {
"crsphost": "XXX.XXX.XXX.XXX",
"crsppswd": "",
"crsprepo": "AVPatterns",
"crspservice": "SFTP",
"crspuser": "siem\_t3000\_west",
"primary\_ts": true
}
[...]
"parameters": {
[...]
"snmpv3\_authpass": "[redacted]",
"snmpv3\_privpass": "[redacted]",
"snmpv3\_user": "snmpuser",
"snmpv3\_hash": "SHA",
"snmpv3\_encrypt": "AES"
}
[...]
"parameters": {
[...]
"cyg\_server\_passwd": "[redacted]",
[...]
"f...