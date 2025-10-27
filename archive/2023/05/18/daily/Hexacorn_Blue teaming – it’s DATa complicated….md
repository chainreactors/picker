---
title: Blue teaming – it’s DATa complicated…
url: https://www.hexacorn.com/blog/2023/05/17/blue-teaming-its-data-complicated/
source: Hexacorn
date: 2023-05-18
fetch_date: 2025-10-04T11:39:15.133900
---

# Blue teaming – it’s DATa complicated…

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2023/05/12/da-lil-world-of-dll-exports-and-entry-points-part-6/)
[Next →](https://www.hexacorn.com/blog/2023/05/23/dexray-dfir-and-the-art-of-ambulance-chasing/)

# Blue teaming – it’s DATa complicated…

Posted on [2023-05-17](https://www.hexacorn.com/blog/2023/05/17/blue-teaming-its-data-complicated/ "10:57 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

A decade ago blue teaming was … easy (this is a really bad joke, I know!).

In fairness, we had less targets, less programming languages to deal with, less platforms, less architectures, consoles, less … of everything…

In 2023 the life of a SOC/CERT person is a nightmare.. In this [Twitter thread](https://twitter.com/Hexacorn/status/1658959899496202241?s=20) I tried to summarize the state of the affairs when it comes to data that comes our way… in many forms…

It comes in a binary form, it comes in a textual form, using a variety of data formats, data encodings, encryption schemes, protocol-driven encapsulations, languages of telemetry, languages of defense, languages of offense, hidden, manipulative and driving us both nuts and making us all loving it…

There are so many forms in which information arrives to us today:

* assembly: x86, x64, arm, sparc, ppc, IoC-specific
* bytecode: IL, python, java, autoit, nullsoft, inno
* actual executables: PE, ELF, COM, SYS, DRV, OCX, DLL
* archives/images: ZIP, TAR, GZ, RAR, 7z, Xz, Bzip2, KGB, ARJ, LHA, ISO, BIN, NRG, DMG, PKG, RPM, DEB, MSI, DLL, OVR, VMDK
* macros: VBA, OpenOffice BASIC
* c, cpp, C#, other .NET languages, vb, delphi, rust, go, nim
* scripts: bat, vbs, js, applescript, mof, idc, idl, rc, bash, powershell
* encrypted scripts: jse, vbe
* web scripts: php, perl, asp, jsp
* python (IDAPython), perl, ruby, winbatch, autoit
* exotic malware files: fas (AutoDesk/AutoCAD)
* autorun scripts: autoruns.inf
* Sigma
* SPL
* KQL
* AQL
* PowerQuery
* Linq
* SQL (including cache files)
* Yara (\*.yar, \*.yara)
* Detect It Easy
* Snort
* ClamAV
* Tanium Signals
* Synapse Storm
* Sublime Security email rules language
* R
* pseudo-code (IDA, Ghidra, etc.)
* config files: ini, yaml, linux config files (/etc/\*), program-specific config files (too many to list)
* event logs: evt, evtx
* URL shortcuts: url
* binary shortcuts: lnk files
* data formats: sql, csv, tsv, json, xml
* plug-ins: from total commander, nmap, burp, windbg, notepad++, xdbg, etc. to regripper, kape, plaso, etc.
* network dumps: pcap
* files using character encoding: ascii, utf7, utf8, utf16, utf32, ebcdic, KOI etc.
* files and streams using data encodings: base64, Ascii85, uuencode, etc.
* message encodings: mime
* memory dumps: raw, core, dmp (per process and full-physical)
* highlight files: uew, tmLanguage, bt
* registry files: .reg
* quarantined files
* EDR logs in many formats, offering different level of telemetry
* web logs (f.ex. both HTTP and HTTPS)
* mail logs
* mailbox files (ost, pst, mbox, msg, eml)
* (S)ftp logs
* aws CloudTrail logs
* aws GuardDuty logs
* command line syntax: lin, win, mac
* ‘randomly accessible (per company)’ feeds: f.ex. jamf
* proprietary and less-known log streams (msad, ossec, SaaS, FIM, etc.)
* browser extensions: xpi, crx
* microsoft / office files (rtf, doc\*, xls\*, ppt\*, pps\*, one, mdb, accdb)

This entry was posted in [Security Logs](https://www.hexacorn.com/blog/category/security-logs/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/05/17/blue-teaming-its-data-complicated/ "Permalink to Blue teaming – it’s DATa complicated…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")