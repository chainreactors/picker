---
title: [SYSS-2026-071]: GDCM (Grassroots DICOM) - Format String	(CWE-134)
url: https://seclists.org/fulldisclosure/2026/Sep/87
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:56:57.981661
---

# [SYSS-2026-071]: GDCM (Grassroots DICOM) - Format String	(CWE-134)

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

[![Previous](/images/left-icon-16x16.png)](86)
[By Date](date.html#87)
[![Next](/images/right-icon-16x16.png)](88)

[![Previous](/images/left-icon-16x16.png)](86)
[By Thread](index.html#87)
[![Next](/images/right-icon-16x16.png)](88)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-071]: GDCM (Grassroots DICOM) - Format String (CWE-134)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 15:33:50 +0200

---

```
Advisory ID:               SYSS-2026-071
Product:                   GDCM (Grassroots DICOM)
Manufacturer:              GDCM Project
Affected Version(s):       3.3.0
Tested Version(s):         3.3.0
Vulnerability Type:        Format String (CWE-134)
Risk Level:                Medium
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

The gdcmFilenameGenerator component, used by the gdcmraw command-line tool
to generate output filenames for split fragments, is vulnerable to a
format string vulnerability. The user-supplied pattern string is used
directly as the format string argument to snprintf() without proper
validation of the format specifiers. Only the count of % characters is
checked (exactly one required), but the specifier that follows is not
validated.

An attacker can supply format specifiers such as "%n" to write to arbitrary
memory addresses, or "%s" to dereference small integers as pointers,
causing crashes. Positional parameters like "%5$x" can be used to leak
stack data into generated filenames, enabling information disclosure.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The vulnerable code is in the FilenameGenerator::Generate() function at
Source/Common/gdcmFilenameGenerator.cxx:94:

  int res = snprintf( internal, internal_len, Pattern.c_str(), i );

The Pattern string is set by the user via FilenameGenerator::SetPattern().
In the gdcmraw command-line tool, the pattern comes directly from the
- -p/--pattern command-line argument:

  // gdcmraw.cxx:150
  pattern = optarg;  // user-controlled!
  // gdcmraw.cxx:353
  fg.SetPattern( pattern.c_str() );

The validation in Generate() only counts % characters and requires
exactly one but does NOT validate what format specifier follows:

  const char *pattern = Pattern.c_str();
  int num_percent = 0;
  while( (pattern = strchr( pattern, '%')) )
    {
    ++pattern;
    ++num_percent;
    }
  if ( num_percent != 1 )
    {
    gdcmDebugMacro( "No more than one % in string formatting please" );
    return false;
    }

This means patterns like "%s", "%x", "%5$x", and "%n" all pass validation:

  - "%s"  : treats the loop index i as a char* pointer and attempts to
            dereference it, causing a segmentation fault (information
            disclosure if the dereferenced memory contains readable data)
  - "%x"  : reads the loop index value as hex and embeds it in the filename
  - "%5$x": positional parameter that skips past the provided argument
            to the 5th variadic argument on the stack, leaking arbitrary
            stack data into the generated filename (information disclosure)
  - "%n"  : interprets the loop index i as an int* and writes the number
            of bytes written so far to that address, enabling arbitrary
            memory writes and potential remote code execution

The loop index i is of type SizeType (unsigned long / size_t). When
interpreted as a pointer, small index values (0, 1, 2, ...) point to
invalid memory addresses, causing immediate segmentation faults. The
"%n" specifier is particularly dangerous as it enables write-what-where
attacks if the attacker can control the stack layout.

The exploitability of the vulnerable code with the different shown
options depends on on the used compiler settings, for example glibc's
FORTIFY_SOURCE.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

Using the format specifier "%s" in combination with a multi-fragment
DICOM file leads to a segmentation fault as the loop index gets interpreted
as char* pointer. When the loop counter is 1, snprintft() attempts to
read from address 0x1.

gdcmraw -i multifrag.dcm -o output_ --split-frags -p '%s'
```

[1] 13623 segmentation fault (core dumped) gdcmraw -i multifrag.dcm
-o output\_ --split-frags -p '%s'

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
[2] SySS Security Advisory SYSS-2026-071
```

<https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2026-071.txt>

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
latest version of this security advisory is available on the SySS website.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright:

Creative Commons - Attribution (by) - Version 4.0
URL: https://creativecommons.org/licenses/by/4.0/deed.en
```

**Attachment:
[OpenPGP\_signature.asc](att-87/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](86)
[By Date](date.html#87)
[![Next](/images/right-icon-16x16.png)](88)

[![Previous](/images/left-icon-16x16.png)](86)
[By Thread](index.html#87)
[![Next](/images/right-icon-16x16.png)](88)

### Current thread:

* **[SYSS-2026-071]: GDCM (Grassroots DICOM) - Format String (CWE-134)** *Matthias Deeg via Fulldisclosure (Sep 26)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

#...