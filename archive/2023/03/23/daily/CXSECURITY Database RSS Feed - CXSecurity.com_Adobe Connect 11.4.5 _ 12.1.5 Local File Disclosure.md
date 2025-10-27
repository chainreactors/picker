---
title: Adobe Connect 11.4.5 / 12.1.5 Local File Disclosure
url: https://cxsecurity.com/issue/WLB-2023030050
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-23
fetch_date: 2025-10-04T10:20:29.912035
---

# Adobe Connect 11.4.5 / 12.1.5 Local File Disclosure

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
|  |  | |  | | --- | | **Adobe Connect 11.4.5 / 12.1.5 Local File Disclosure** **2023.03.22**  Credit:  **[h4shur](https://cxsecurity.com/author/h4shur/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2023-22232](https://cxsecurity.com/cveshow/CVE-2023-22232/ "Click to see CVE-2023-22232")**  CWE: **[CWE-284](https://cxsecurity.com/cwe/CWE-284 "CWE-284")** | |

# Title: adobe connect - Local File Disclosure / Download [security feature
bypass vulnerability]
# Author: h4shur
# date:2021.01.16-2023.02.17
# CVE: CVE-2023-22232
# Vendor Homepage: https://www.adobe.com
# Software Link: https://www.adobe.com/products/adobeconnect.html
# Version: 11.4.5 and earlier, 12.1.5 and earlier
# User interaction: None
# Tested on: Windows 10 & Google Chrome, kali linux & firefox
### Summary:
Adobe Connect versions 11.4.5 (and earlier), 12.1.5 (and earlier) are
affected by an Improper Access Control vulnerability that could result in a
Security feature bypass. An attacker could leverage this vulnerability to
impact the integrity of a minor feature.
Exploitation of this issue does not require user interaction.
### Description :
There are many web applications in the world, each of which has
vulnerabilities due to developer errors, and this is a problem for all of
them, and even the best of them, like the "adobe connect" program, have
vulnerabilities that occur every month. They are found and fixed by the
team.
\* What is LFD bug?
LFD bug stands for Local File Disclosure / Download, which generally allows
the attacker to read and download files within the server, so it can be
considered a very dangerous bug in the web world and programmers must be
aware of it. Be careful and maintain security against this bug
\* Intruder access level with LFD bug
The level of access using this bug can be even increased to the level of
access to the website database in such a way that the hacker reads
sensitive files inside the server that contain database entry information
and enters the database and by extracting the information The admin will
have a high level of access
\* Identify vulnerable sites
To search for LFD bugs, you should check the site inputs. If there is no
problem with receiving ./ characters, you can do the test to read the files
inside the server if they are vulnerable. Enter it and see if it is read or
not, or you can use files inside the server such as / etc / passwd / .. and
step by step using ../ to return to the previous path to find the passwd
file
\* And this time the "lfd" in "adobe connect" bug:
To download and exploit files, you must type the file path in the
"download-url" variable and the file name and extension in the "name"
variable.
You can download the file by writing the file path and file name and
extension.
When you have written the file path, file name and extension in the site
address variables, a download page from Adobe Connect will open for you,
with "Save to My Computer
file name]" written in the download box and a file download link at the
bottom of the download box, so you can download the file.
\* There are values inside the url that do not allow a file other than this
file to be downloaded.
\* Values: sco\_id and tickets
But if these values are cleared, you will see that reloading is possible
without any obstacles
At another address, you can download multiple files as a zip file.
We put the address of the files in front of the variable "ffn" and if we
want to add the file, we add the variable "ffn" again and put the address
of the file in front of it. The "download\_type" variable is also used to
specify the zip extension.
### POC :
https://target.com/[folder]/download?download-url=[URL]&name=[file.type]
https://target.com/[folder]/download?output=output&download\_type=[Suffix]&ffn=[URL]&baseContentUrl=[base
file folder]
### References:
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22232
https://nvd.nist.gov/vuln/detail/CVE-2023-22232
https://helpx.adobe.com/security/products/connect/apsb23-05.html

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030050)

[Tweet](https://twitter.com/share)

Vote for this issue:
 5
 0

100%

0%

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