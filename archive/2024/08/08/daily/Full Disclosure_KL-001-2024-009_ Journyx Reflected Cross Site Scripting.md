---
title: KL-001-2024-009: Journyx Reflected Cross Site Scripting
url: https://seclists.org/fulldisclosure/2024/Aug/7
source: Full Disclosure
date: 2024-08-08
fetch_date: 2025-10-06T18:08:48.683655
---

# KL-001-2024-009: Journyx Reflected Cross Site Scripting

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

# KL-001-2024-009: Journyx Reflected Cross Site Scripting

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 7 Aug 2024 18:53:23 -0500

---

```
KL-001-2024-009: Journyx Reflected Cross Site Scripting

Title: Journyx Reflected Cross Site Scripting
Advisory ID: KL-001-2024-009
Publication Date: 2024.08.07
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2024-009.txt

1. Vulnerability Details

     Affected Vendor: Journyx
     Affected Product: Journyx (jtime)
     Affected Version: 11.5.4
     Platform: GNU/Linux
     CWE Classification: CWE-81: Improper Neutralization of Script in an Error
                         Message Web Page
     CVE ID: CVE-2024-6892

2. Vulnerability Description

     Attackers can craft a malicious link that once clicked
     will execute arbitrary JavaScript in the context of
     the Journyx web application.

3. Technical Description

     During the active directory login flow, if an error
     occurs, the user is redirected to a page containing
     an error message outlining the problem. The error
     message shown in the page response is derived from
     the "error_description" query parameter that appears
     in the URL. This parameter is not sanitized or validated
     prior to being reflected, allowing for an attacker to
     insert malicious HTML/JavaScript into the "error_description"
     parameter.

     This vulnerability can be exploited regardless of whether
     active directory authentication has been configured for the
     Journyx instance.

4. Mitigation and Remediation Recommendation

     The vendor reports that this issue was remediated in Journyx
     v13.0.0.

     For self-hosted instances of JournyX, additional security
     measures (such as input sanitization) can be added by monkey
     patching the PYC file responsible for handling request
     parameters (mycgi.pyc).

     1) Rename "mycgi.pyc" to an alternative name, e.g. mycgi_original.pyc.
          $ mv wt_tar/pi/pylib/wtlib/mycgi.py wt_tar/pi/pylib/wtlib/mycgi_original.py

     2) Create a file named "mycgi.py" in the same directory.
          $ touch wt_tar/pi/pylib/wtlib/mycgi.py

     3) Insert the following code into the newly created "mycgi.py"

          from mycgi_original import *
          from html import escape

          def patch():
              pdata = _parse()

              # force the value of "end_URL" to always be "wte"
              if pdata.get('end_URL'): pdata['end_URL'] = ['wte']

              # sanitize user-controlled error messages
              for parameter in ['error', 'error_description']:
                  if not pdata.get(parameter): continue
                  pdata[parameter] = [escape(value) for value in pdata[parameter]]

              return pdata

          _parse = parse
          parse  = patch

     Once these changes have been made, the JournyX native "mycgi.parse()"
     function will be overwritten with the "patch()" function located in the
     "mycgi.py" file. Relevant to this advisory, the patch provided above
     will replace special characters with their respective HTML entity
     representation for the "error" and "error_description" parameters. This
     list of parameters can be extended as needed.

     Additionally, if SSO is not required, requests to /jtcgi/r/adlogin/sso
     could be dropped without forwarding invoking FastCGI via a ModSecurity
     rule like the one below:

          SecRule REQUEST_URI "@contains adlogin/sso" "id:4,phase:2,deny,log,auditlog"

5. Credit

     This vulnerability was discovered by Jaggar Henry of KoreLogic, Inc.

6. Disclosure Timeline

     2024.01.31 - KoreLogic notifies Journyx support of the intention to
                  report vulnerabilities discovered in the licensed,
                  on-premises version of the product.
     2024.01.31 - Journyx acknowledges receipt.
     2024.02.02 - KoreLogic requests a meeting with Journyx support to share
                  vulnerability details.
     2024.02.07 - KoreLogic reports vulnerability details to Journyx.
     2024.02.09 - Journyx responds that this vulnerability has been remediated
                  in the cloud-hosted version of the product.
     2024.02.21 - KoreLogic offers to test the cloud version to confirm
                  the fix; no response.
     2024.07.01 - KoreLogic notifies Journyx of impending public disclosure.
     2024.07.09 - Journyx confirms version number of the remediation.
     2024.08.07 - KoreLogic public disclosure.

7. Proof of Concept

    The following URL contains the "error_description"
    parameter with a value of "%3Csvg%2fonload%3dprompt(%27KoreLogic%27)%3E":

http://redacted.com:8080/jtcgi/r/adlogin/sso?code=1337&state=foobar&id_token=zoinks&error_description=%3Csvg%2fonload%3dprompt(%27KoreLogic%27)%3E&error=error

    This value is automatically URL decoded to "<svg/onload=prompt('KoreLogic')>"
    and reflected into the page response:

        <div class="errorMessage">
```

            Unable to complete sign-on attempt. This is possibly a configuration error in the application registration
on the Identity Provider (IdP) side. The IdP server said:

```
            <p>error <b><svg onload="prompt('KoreLogic')"></svg></b></p>
        </div>

    Once this link is clicked or visited in a browser, the
    javascript function "prompt()" is executed, and a display
    box is presented, thereby validating the execution of
    arbitrary JavaScript.

The contents of this advisory are copyright(c) 2024
KoreLogic, Inc. and are licensed under a Creative Commons
Attribution Share-Alike 4.0 (United States) License:
http://creativecommons.org/licenses/by-sa/4.0/

KoreLogic, Inc. is a founder-owned and operated company with a
proven track record of providing security services to entities
ranging from Fortune 500 to small and mid-sized companies. We
are a highly skilled team of senior security consultants doing
by-hand security assessments for the most important networks in
the U.S. and around the world. We are also developers of various
tools and resources aimed at helping the security community.
https://www.korelogic.com/about-korelogic.html

Our public vulnerability disclosure policy is available at:
https://korelogic.com/KoreLogic-Public-Vulnerability-Disclosure-Policy
```

**Attachment:
[OpenPGP\_signature.asc](att-7/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **KL-001-2024-009: Journyx Reflected Cross Site Scripting** *KoreLogic Disclosures via Fulldisclosure (Aug 07)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [D...