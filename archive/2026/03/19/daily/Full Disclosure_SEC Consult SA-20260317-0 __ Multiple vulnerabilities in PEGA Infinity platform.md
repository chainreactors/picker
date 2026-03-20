---
title: SEC Consult SA-20260317-0 :: Multiple vulnerabilities in PEGA Infinity platform
url: https://seclists.org/fulldisclosure/2026/Mar/8
source: Full Disclosure
date: 2026-03-19
fetch_date: 2026-03-20T04:09:30.257262
---

# SEC Consult SA-20260317-0 :: Multiple vulnerabilities in PEGA Infinity platform

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260317-0 :: Multiple vulnerabilities in PEGA Infinity platform

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 17 Mar 2026 12:05:21 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260317-0 >
=======================================================================
              title: Multiple vulnerabilities
            product: PEGA Infinity platform
 vulnerable version: CVE-2025-62181: Pega Platform versions 7.1.0 through Infinity 25.1.0
                     CVE-2025-9559: Pega Platform versions 8.7.5 to Infinity 24.2.2
      fixed version: CVE-2025-62181: 24.1.4, 24.2.4, and 25.1.1 patch
                     CVE-2025-9559:  24.2.3
         CVE number: CVE-2025-62181, CVE-2025-9559
             impact: medium
           homepage:https://www.pega.com/
              found: 2024-12-12
                 by: Eric Kahlert
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"We are Pega- The enterprise transformation company.™
Our enterprise AI decisioning and workflow automation platform delivers business
transforming value. Together, we partner with the world’s largest organizations
to Build for Change®."

Source:https://www.pega.com/about

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Weak Brute-Force protection for login page (CVE-2025-62181)
The application's login form implements a weak login brute-force protection
mechanism, which is only effective against multiple login attempts using
different passwords. Attacks using the same password on different users and
username enumeration are therefore not prevented.

An attacker can perform the following attacks:
- Username Enumeration: An attacker can test a large list of potential usernames
  against the login mechanism and distinguish between valid and invalid usernames
  based on the server's response time.
- Password Spraying: In a password spraying attack, the same password is tested
  against many different usernames, potentially granting unauthorized access to user
  accounts in the worst-case scenario. To exploit this vulnerability, an attacker
  could, for example, create a script that uses the most common passwords and a list
  of known valid usernames to attempt authentication.

2) Insecure Direct Object Reference (IDOR) (CVE-2025-9559)
An Insecure Direct Object Reference (IDOR) occurs when an application grants direct
access to objects based on user input without performing sufficient authorization
checks. As a result, attackers can bypass authorization and directly access system
resources, such as files. In this case the IDOR vulnerability can be used to read
image files from other users without setting the option to share the images with
others.

Proof of concept:
-----------------
1) Weak Brute-Force protection for login page (CVE-2025-62181)
This is an invalid login request:
POST /XXX/app/default/CHhSc-bWE3BYCBUOUq46CjlmQt_t3VKg*/!STANDARD HTTP/1.1
Host: [...]
Cookie: Pega-RULES=[...]; JSESSIONID=[...]; ROUTEID=[...]
[...]

pzAuth=guest&UserIdentifier=PentestBenutzer_1&Password=invalid_password&pyActivity%3DCode-Security.Login=&lockScreenID=&lockScreenPassword=&newPassword=&confirmNewPassword=

The server response for a valid username shows a significantly higher response
time compared to responses with invalid usernames. An attacker can use a large
list of potential usernames in a script to enumerate valid usernames, as illustrated
in the following example, see figure <responseTimeTable.png>

In less than a minute, 8,000 invalid authentication attempts were made from the same
IP address using different usernames and the same password.

Password Spraying:
After enumerating valid usernames, an attacker can execute a password spraying attack by
using the same request method as for username enumeration. A script is used to test the
same password across many different usernames without triggering the brute-force protection.
During this attack, 8,000 invalid authentication attempts were again made from the same
IP address in under a minute, using different usernames and the same password.
The attacker would repeat this attack with a list of valid usernames and common passwords
until a successful login is found.

As shown in the following example, the attack was successful with the username PentestBenutzer_1.
See figure <passwordSpray.png>

2) Insecure Direct Object Reference (IDOR) (CVE-2025-9559)
In order to verify this vulnerability, e.g. a test user "user_1" is logged in:
POST /XXX/app/default/CHhSc-bWE3BYCBUOUq46CjlmQt_t3VKg*/!STANDARD HTTP/1.1
Host: [...]
Cookie: p_unknown=true%7Bapp%7D; Pega-RULES[...]; JSESSIONID=[...]; ROUTEID=[...]
[...]

pzAuth=guest&UserIdentifier=user_1&Password=[...]&pyActivity%3DCode-Security.Login=&lockScreenID=&lockScreenPassword=&newPassword=&confirmNewPassword=

The user receives the following Pega-RULES session cookie:

HTTP/1.1 303 See Other
Date: Thu, 12 Dec 2024 13:36:53 GMT
[...]
SET-COOKIE: Pega-RULES=%09%7Bpd%7DAAAABr3F5Rfo8PLlkIsDNLwSbSZ0HFLGwnS6[...]; Path=[...]; Secure; HttpOnly; SameSite=Lax;
X-Content-Type-Options: nosniff
Connection: close

Another user "user_2" uploads an image, which is a two step process:
POST
/XXX/app/XXX/bJXRcBOqwaiAstqd8LVSHIEMFNxpnKrvbr_zZRJ5OsQ*/!DCSPA_UserPortal?pyActivity=ReloadSection&pzTransactionId=b1f46a71d9635ab261358a8a4a9cbfdb&pzFromFrame=pyWorkPage&pzPrimaryPageName=pyWorkPage&pzKeepPageMessages=false&strPHarnessClass=XXX&strPHarnessPurpose=Review&UITemplatingStatus=Y&StreamName=pzBrowseDocument&BaseReference=pyAttachmentPage&StreamClass=Rule-HTML-Section&bClientValidation=true&FormError=NONE&pyCustomError=pyCaseErrorSection&PreActivity=pzUploadFileToADocument&HeaderButtonSectionName=-1&PagesToRemove=&pzHarnessID=HIDAA6704B0D23A3D2ABE9B1450BC6F31C4&inStandardsMode=true&AJAXTrackID=1&PreDataTransform=
 HTTP/1.1
Host: [...]
Cookie: Pega-Perf=itkn=5; Pega-RULES[...]; JSESSIONID=p_MM8f2VfKMT5sKhvtIc5_tNIt_foyBkqcpUIVW0.[...]; ROUTEID=[...]
Content-Length: 32973
[...]
------WebKitFormBoundaryTll7wmP4P42lbosV
Content-Disposition: form-data; name="$PpyAttachmentPage$ppxAttachName"; filename="cat.png"
Content-Type: image/png

PNG
[...]

The upload is finalized with a second HTTP POST request:
POST
/XXX/app/XXX/bJXRcBOqwaiAstqd8LVSHIEMFNxpnKrvbr_zZRJ5OsQ*/!DCSPA_UserPortal?pzTransactionId=b1f46a71d9635ab261358a8a4a9cbfdb&pzFromFrame=pyWorkPage&pzPrimaryPageName=pyWorkPage&AJAXTrackID=1
 HTTP/1.1
Host: [...]
Cookie: Pega-Perf=itkn=7&start; Pega-RULES=[...]; JSESSIONID=p_MM8f2VfKMT5sKhvtIc5_tNIt_foyBkqcpUIVW0.[...];
ROUTEID=[...]
Content-Length: 2655
[...]

pyActivity=SubmitModalFlowAction&E...