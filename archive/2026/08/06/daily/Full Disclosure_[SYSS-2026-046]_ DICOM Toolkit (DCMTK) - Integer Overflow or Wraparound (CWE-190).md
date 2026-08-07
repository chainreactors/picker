---
title: [SYSS-2026-046]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)
url: https://seclists.org/fulldisclosure/2026/Aug/24
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:29:56.275186
---

# [SYSS-2026-046]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)

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

# [SYSS-2026-046]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 31 Jul 2026 09:57:54 +0200

---

```
Advisory ID:               SYSS-2026-046
Product:                   DCMTK (DICOM ToolKit)
Manufacturer:              OFFIS e.V. / DCMTK Community
Affected Version(s):       3.7.0
Tested Version(s):         3.7.0
Vulnerability Type:        Integer Overflow or Wraparound (CWE-190)
Risk Level:                High
Solution Status:           Fixed
Manufacturer Notification: 2026-07-02
Solution Date:             2026-07-03
Public Disclosure:         2026-07-31
CVE Reference:             Not yet assigned
Author of Advisory:        Matthias Deeg, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

DCMTK (DICOM ToolKit) is an open-source collection of libraries and
applications implementing large parts of the DICOM (Digital Imaging
and Communications in Medicine) standard (see [1]).

DCMTK's DICOMDIR icon image loading is vulnerable to an integer overflow
in the PGM image size calculation. An attacker who can supply a
malicious PGM file referenced as an external icon can cause a heap
out-of-bounds read in the icon scaler, leading to a process crash or
potential information disclosure.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The function DicomDirInterface::getIconFromFile() in libsrc/dcddirif.cc
(line 4489) computes the PGM image buffer size by multiplying the width
and height parsed from the PGM file header:

  unsigned int pgmWidth, pgmHeight = 0;
  // ... values parsed from PGM file via sscanf()
  const unsigned long pgmSize = pgmWidth * pgmHeight;
  Uint8 *pgmData = new Uint8[pgmSize];

Both pgmWidth and pgmHeight are unsigned int. Their product is computed
as unsigned int, and only then assigned to unsigned long.

On any platform where unsigned int is 32 bits, a crafted PGM file with the
dimensions 4294967295 * 4294967295 produces pgmSize = 1 after overflow
(4294967295 * 4294967295 = 0x100000001, truncated to 32 bits = 1).

The allocation "new Uint8[1]" succeeds, and fread() reads exactly 1 byte
from the PGM file.

The icon scaler is invoked at line 4505 of dcddirif.cc:

  result = ImagePlugin->scaleData(pgmData, pgmWidth, pgmHeight,
                                  pixel, width, height);

The scaler implementation (DicomDirImageImplementation::scaleData in
dcmjpeg/libsrc/ddpiimpl.cc, line 60) casts the dimensions from
unsigned int to Uint16 without validation:

  DiScaleTemplate<Uint8> scale(1,
      OFstatic_cast(Uint16, srcWidth),   // 4294967295 -> 65535
      OFstatic_cast(Uint16, srcHeight),  // 4294967295 -> 65535
      OFstatic_cast(Uint16, dstWidth),
      OFstatic_cast(Uint16, dstHeight),
      1);
  scale.scaleData(OFstatic_cast(const Uint8 **, &srcData),
                  &dstData, 1 /* interpolate */);

The DiScaleTemplate constructor (dcmimgle/include/dcmtk/dcmimgle/discalet.h,
line 148) stores the truncated dimensions:

  DiScaleTemplate(const int planes,
                  const Uint16 src_cols,   // resolution of source image
                  const Uint16 src_rows,
                  const Uint16 dest_cols,
                  const Uint16 dest_rows,
                  const Uint32 frames,
                  const int bits = 0)

The scaleData() method (line 187) then iterates over the source image
using the truncated dimensions (65535 * 65535), reading from the 1-byte
heap allocation through the interpolatePixel() method, causing a heap
out-of-bounds read.

The root cause is the unchecked cast from unsigned int to Uint16 in the
scaler (ddpiimpl.cc:60), which silently truncates dimensions without any
bounds validation.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The integer overflow can be demonstrated using a specially crafted PGM
file. The following shell script exemplarily creates such a file named
demo.pgm:

cat > create_pgm.sh << 'EOF'
#!/bin/bash
printf 'P5\n4294967295 4294967295\n255\n' > demo.pgm
printf '\x00' >> demo.pgm
EOF

If this PGM file is processed by a vulnerable DCMTK component like
dcmmkdir, a heap out-of-bounds read is triggered, causing a segmentation
fault in this proof-of-concept example. The DICOM file PAT001 does not
contain pixel data and thus forces a fallback to the default icon.

dcmmkdir +X --default-icon demo.pgm PAT001
E: no pixel data found in DICOM dataset
W: cannot create monochrome icon from image file, using default
```

[1] 27078 segmentation fault (core dumped) dcmmkdir +X
--default-icon exploit.pgm PAT001

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

This security issue was fixed with the commit
534e146b672ccd13d1a2b134ef623840e775396a (see [4]).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2026-07-02: Vulnerability reported to manufacturer
2026-07-02: Manufacturer acknowledges receipt of security advisories
2026-07-03: Security fix published by manufacturer (see [4])
2026-07-31: Public release of security advisory

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] DCMTK project website
    https://dcmtk.org/en/
[2] SySS Security Advisory SYSS-2026-046
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-046.txt>

```
[3] SySS GmbH, SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy
[4] DCMTK security fix
```

<https://github.com/DCMTK/dcmtk/commit/534e146b672ccd13d1a2b134ef623840e775396a>

```
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
[![Next](/images/right-icon-16x16.png)](...