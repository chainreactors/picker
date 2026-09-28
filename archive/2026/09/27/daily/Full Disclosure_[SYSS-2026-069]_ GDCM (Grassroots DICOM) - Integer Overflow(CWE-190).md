---
title: [SYSS-2026-069]: GDCM (Grassroots DICOM) - Integer Overflow	(CWE-190)
url: https://seclists.org/fulldisclosure/2026/Sep/85
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:58.492789
---

# [SYSS-2026-069]: GDCM (Grassroots DICOM) - Integer Overflow	(CWE-190)

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

[![Previous](/images/left-icon-16x16.png)](84)
[By Date](date.html#85)
[![Next](/images/right-icon-16x16.png)](86)

[![Previous](/images/left-icon-16x16.png)](84)
[By Thread](index.html#85)
[![Next](/images/right-icon-16x16.png)](86)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-069]: GDCM (Grassroots DICOM) - Integer Overflow (CWE-190)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 15:33:39 +0200

---

```
Advisory ID:               SYSS-2026-069
Product:                   GDCM (Grassroots DICOM)
Manufacturer:              GDCM Project
Affected Version(s):       3.3.0
Tested Version(s):         3.3.0
Vulnerability Type:        Integer Overflow (CWE-190)
Risk Level:                High
Solution Status:           Open
Manufacturer Notification: 2026-07-24
Public Disclosure:         2026-09-23
CVE Reference:             Not yet assigned
Author of Advisory:        Matthias Deeg, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

GDCM (Grassroots DICOM) is an open-source C++ library for reading, writing,
and processing DICOM (Digital Imaging and Communications in Medicine)
medical imaging files (see [1]).

The JPEG2000 image codec in GDCM, used for decoding JPEG2000-compressed
DICOM pixel data, is vulnerable to an integer overflow that leads to a
heap buffer overflow. The buffer size for decoded pixel data is computed
using 32-bit unsigned integer arithmetic based on image dimensions
(rows * columns) from the DICOM header. When the product exceeds 2^32,
the result silently wraps around, causing an undersized buffer allocation.
The subsequent pixel data write loop then overflows the heap buffer.
A malicious DICOM file with crafted image dimensions can trigger this
vulnerability, potentially leading to remote code execution in the
context of the user processing the file.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The vulnerable code is in the JPEG2000Codec::DecodeCommon function at
Source/MediaStorageAndFileFormat/gdcmJPEG2000Codec.cxx:1037-1038:

  unsigned long len = Dimensions[0]*Dimensions[1] *
                      (PF.GetBitsAllocated() / 8) * image->numcomps;
  char *raw = new char[len];

The variables Dimensions[0] and Dimensions[1] are both 'unsigned int'
(32-bit) values inherited from the ImageCodec base class, populated from
the DICOM header's Rows and Columns elements (VR=US, maximum value
65535). The multiplication chain
Dimensions[0]*Dimensions[1]*(PF.GetBitsAllocated()/8)*image->numcomps
is executed entirely in 32-bit unsigned integer arithmetic, because all
operands are 32-bit types. The result is only widened to 'unsigned long'
on assignment to 'len', after the overflow has already occurred.

When the product exceeds 2^32, it wraps around modulo 2^32.

Following the allocation, the decoded pixel data is written to the 'raw'
buffer in a loop:

  for (int i = 0; i < wr * hr; i++) {
      int v = image->comps[compno].data[i / wr * w + i % wr];
      *data8 = (uint8_t)v;
      data8 += image->numcomps;
  }

This loop writes wr*hr pixels, each advancing the pointer by numcomps,
to the 'raw' buffer. Since the buffer is far smaller than needed due to
the integer overflow, this write operation causes a heap buffer overflow.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

A PoC was developed that reproduces the vulnerable calculation and
buffer allocation pattern from gdcmJPEG2000Codec.cxx, simulating the
pixel data write loop that overflows the undersized buffer.

PoC source code:

#include <cstdint>
#include <cstdio>
#include <cstring>

typedef unsigned int uint32;
typedef unsigned long ulong;

static void vulnerable_jpeg2000_decode(uint32 dim_x, uint32 dim_y,
                                       int bits_allocated, int numcomps)
{
    // Vulnerable calculation (gdcmJPEG2000Codec.cxx:1037)
    unsigned long len = dim_x * dim_y *
                        (bits_allocated / 8) * numcomps;

    // Vulnerable allocation (gdcmJPEG2000Codec.cxx:1038)
    char *raw = new char[len];

    unsigned long actual_bytes = (unsigned long long)dim_x * dim_y *
                                 (bits_allocated / 8) * numcomps;

    // Vulnerable pixel write loop (gdcmJPEG2000Codec.cxx:1084-1092)
    for (unsigned long i = 0; i < actual_bytes; i++) {
        raw[i] = (char)(i & 0xFF);
    }

    delete[] raw;
}

int main()
{
    // Test Case 1: 16-bit grayscale, 65536 x 65536
    // Product overflows to 0, buffer allocated as 0 bytes
    vulnerable_jpeg2000_decode(65536, 65536, 16, 1);
    return 0;
}

To build and run the PoC:

g++ -fsanitize=address -fno-omit-frame-pointer -g \
  pocs/poc_jpeg2000_integer_overflow.cpp -o poc

Running the PoC triggers the heap buffer overflow, detected by ASan:

  $ ./poc
  ==ERROR: AddressSanitizer: heap-buffer-overflow on address
  0x7b2dac5e0010 at pc 0x557e499c4371 bp 0x7ffdf03c63a0 sp 0x7ffdf03c6390
  WRITE of size 1 at 0x7b2dac5e0010 thread T0
      #0 0x557e499c4370 in vulnerable_jpeg2000_decode
          poc_jpeg2000_integer_overflow.cpp:106
      #1 0x557e499c442d in main
          poc_jpeg2000_integer_overflow.cpp:131
  0x7b2dac5e0010 is located 0 bytes inside of 1-byte region
  [0x7b2dac5e0010,0x7b2dac5e0011) allocated by thread T0 here:
      #0 0x7f0dadd2d431 in operator new[](unsigned long)
      #1 0x557e499c420e in vulnerable_jpeg2000_decode
          poc_jpeg2000_integer_overflow.cpp:79

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

SySS GmbH is not aware of a security update for the described issue.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2026-07-24: Vulnerability reported to manufacturer
2026-07-31: Vulnerability reported to manufacturer again
2026-09-23: Public release of security advisory

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] GDCM project website
    https://gdcm.sourceforge.net/
[2] SySS Security Advisory SYSS-2026-069
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-069.txt>

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
[OpenPGP\_signature.asc](att-85/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing li...