---
title: [SYSS-2024-085]: Broadcom CA Client Automation - Improper Privilege Management (CWE-269)
url: https://seclists.org/fulldisclosure/2024/Dec/16
source: Full Disclosure
date: 2024-12-20
fetch_date: 2025-10-06T19:42:38.682869
---

# [SYSS-2024-085]: Broadcom CA Client Automation - Improper Privilege Management (CWE-269)

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2024-085]: Broadcom CA Client Automation - Improper Privilege Management (CWE-269)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 17 Dec 2024 12:26:41 +0100

---

```
Advisory ID:               SYSS-2024-085
Product:                   CA Client Automation (CA DSM)
Manufacturer:              Broadcom
Affected Version(s):       14.5.0.15
Tested Version(s):         14.5.0.15
Vulnerability Type:        Improper Privilege Management (CWE-269)
Risk Level:                High
Solution Status:           Fixed
Manufacturer Notification: 2024-10-18
Solution Date:             2024-12-17
Public Disclosure:         2024-12-17
CVE Reference:             CVE-2024-38499
Authors of Advisory:       Matthias Deeg (SySS GmbH)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

The software product CA Client Automation is a client management
solution with many features including desktop and server management
(DSM) functionality.

The manufacturer describes the product as follows:

"CA Client Automation delivers a complete view into your entire IT asset
base and employs full automation and remote client management
capabilities for managing the end user computing environmentâ€”whether
physical or virtual. No matter how complex your IT environment, it
streamlines the daily operational tasks that bog down your IT
organization, helping you run more efficiently and cost-effectively than
ever before."

Due to improper privilege management, low-privileged Windows users or
malware running in their context are able to extract cryptographic keys
that are used to encrypt locally stored configuration data, which is
also accessible and can contain sensitive information, for example
service account credentials.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The desktop and server management solution Broadcom CA DSM stores some
configuration data of its agent component locally on managed systems in
encrypted form. The encrypted configuration data may include sensitive
data like user credentials of service accounts.

On a managed client system, low-privileged Windows users are able to
extract the used cryptographic key material that is used for encrypting
specific configuration data by exploiting a design security issue using
the Common Application Framework (CAF) command line tool.

It was also analyzed how specific configuration data containing Windows
account passwords is encrypted.

With access to the used cryptographic encryption method, the corresponding
cryptographic key material, and the encrypted configuration data, an
attacker is thus able to gain access to locally stored sensitive data
in cleartext.

Depending on the locally stored secrets, recovered user credentials
could be used for privilege escalation attacks and for gaining
unauthorized access to other systems within the corporate network.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

Matthias Deeg developed a proof-of-concept software tool for extracting
used cryptographic key material ("global" or "local" key) via the CAF
process.

The following output exemplarily demonstrates extracting the used
"global" cryptographic key, which is saved in the output file
"key_global.bin":

D:\>CA_DSM_keydumper.exe global "C:\Program Files (x86)\CA\DSM\Bin\CAF.exe"
```

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
 / \_\_\_\_\_ \_\_\_\_\_ \_\_\_\_\_
 \
 / / \_\_\_| / \_\_\_/ \_\_\_|
 \
 | \ `--. \_ \_\ `--.\ `--.
 |
 | `--. \ | | |`--. \`--. \
 |
 | /\\_\_/ / |\_| /\\_\_/ /\\_\_/ /
 |
 \ \\_\_\_\_/ \\_\_, \\_\_\_\_/\\_\_\_\_/ ... dumps crypto keys!
 /
 \ \_\_/ |
 /
 / |\_\_\_/
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/

```
              / _________________/
        (__) /_/
        (oo)
  /------\/
 / |____||
*  ||   ||
   ^^   ^^
SySS CA DSM Crypto Key Dumper v1.0 by Matthias Deeg - SySS GmbH (c) 2024

[+] Start caf.exe process
CA DSM r14 Common Application Framework 14.5.0.153
```

Copyright (c) 2020 Broadcom. All Rights Reserved.The term "Broadcom"
refers to Broadcom Inc.and/or its subsidiaries.

```
[+] The Caf process was patched successfully.
[+] The crypto key was written to the file 'key_global.bin'

Furthermore, a Python software tool named "CA DSM Decryptor" was
developed, which can be used to recover encrypted configuration data as
cleartext.

The following output illustrates a successful decryption of encrypted
password information contained within the configuration file
%PROGRAMFILES(X86)\CA\DSM\Agent\CCNF\reptempl.xml:

$ python ca-dsm-decryptor.py key_global.bin NB56fBY5W18TcGu840UH+w
SySS CA DSM Decryptor by Matthias Deeg (c) 2024 SySS GmbH
- -----
[*] Decrypted data:
syss

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

The manufacturer provided a security update that fixes the described
security vulnerability.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2024-10-18: Vulnerability reported to manufacturer
2024-10-18: Manufacturer acknowledges receipt of security advisory
2024-10-18: Manufacturer asks for proof-of-concept code
2024-10-18: Provided proof-of-concept code to manufacturer
2024-11-07: Conference call to answer open questions
2024-11-20: Received information from manufacturer about release of
            security fix and CVSS score
2024-12-04: Received further information from manufacturer
2024-12-17: Release of security update
2024-12-17: Public release of security advisory

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] Product website for Broadcom CA Client Automation (DSM CA)
```

<https://www.broadcom.com/products/software/service-management/client-automation>

```
[2] SySS Security Advisory SYSS-2024-085
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-085.txt>

```
[3] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy/
[4] Broadcom security advisory (only with customer sign-in)
```

<https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25284>

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Matthias Deeg of SySS GmbH.

E-Mail: matthias.deeg (at) syss.de
```

Public Key:
<https://www.syss.de/fileadmin/dokumente/Materialien/PGPKeys/Matthias_Deeg.asc>

```
Key fingerprint = D1F0 A035 F06C E675 CDB9 0514 D9A4 BF6A 34AD 4DAB

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclaimer:

The information provided in this security advisory is provided "as is"
and without warranty of any kind. Details of this security advisory may
be updated in order to provide as accurate information as possible. The
latest version of this security advisory is available on the SySS Web
site.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright:

Creative Commons - Attributio...