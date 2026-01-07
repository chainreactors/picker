---
title: Bioformats v8.3.0 Untrusted Deserialization of Bio-Formats Memoizer Cache Files
url: https://seclists.org/fulldisclosure/2026/Jan/7
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:41.187851
---

# Bioformats v8.3.0 Untrusted Deserialization of Bio-Formats Memoizer Cache Files

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# Bioformats v8.3.0 Untrusted Deserialization of Bio-Formats Memoizer Cache Files

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Mon, 29 Dec 2025 22:59:51 -0500

---

```
Bio-Formats performs unsafe Java deserialization of attacker-controlled
memoization cache files (.bfmemo) during image processing. The
loci.formats.Memoizer class automatically loads and deserializes memo files
associated with images without validation, integrity checks, or trust
enforcement.
An attacker can exploit this behavior by supplying a crafted or corrupted
.bfmemo file—either fully attacker-controlled or derived from a legitimate
memo file—causing Bio-Formats to deserialize untrusted data. This can lead
to denial-of-service, logic manipulation, or remote code execution when
suitable gadget chains are present on the classpath.

*Impact:*
An attacker can:
* Trigger deserialization of untrusted data
* Cause repeated parsing failures (denial-of-service)
* Influence reader discovery and class loading
* Potentially achieve remote code execution when suitable gadget chains
exist
The vulnerability is reachable through standard image processing workflows
and does not require non-default configuration.

*Proof of Concept:*
Corrupting a Legitimate Memo File
This PoC demonstrates exploitation by modifying a legitimately generated
.bfmemo file, which closely mirrors a real-world attack scenario.

Step 1 – Generate a Valid Memo File
[Step 1/4] Creating valid TIFF image...
[+] Created valid.tif

[Step 2/4] Generating legitimate memo file...
[+] Memo created at: ./root/bioformats/.valid.tif.bfmemo
[+] Size: 34815 bytes

Step 2 – Corrupt the Existing Memo File
[Step 4/4] Corrupting memo file...
[+] Corrupted memo (appended 400 garbage bytes)
[+] Created symlink to memo file

Example Output
[*] Loading valid.tif with Memoizer...

java.lang.ClassNotFoundException: loci.formats.in.URLReader
at loci.formats.ClassList.parseLine(ClassList.java:196)
at loci.formats.ClassList.parseFile(ClassList.java:258)
at loci.formats.Memoizer.<init>(Memoizer.java:540)

java.lang.ClassNotFoundException: loci.formats.in.SlideBook6Reader
java.lang.ClassNotFoundException: loci.formats.in.ScreenReader
java.lang.ClassNotFoundException: loci.formats.in.ZarrReader
java.lang.ClassNotFoundException:
ch.epfl.biop.formats.in.ZeissQuickStartCZIReader
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **Bioformats v8.3.0 Untrusted Deserialization of Bio-Formats Memoizer Cache Files** *Ron E (Jan 05)*

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