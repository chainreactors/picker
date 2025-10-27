---
title: [local] Microsoft Windows - Storage QoS Filter Driver Checker
url: https://www.exploit-db.com/exploits/52399
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:13.075758
---

# [local] Microsoft Windows - Storage QoS Filter Driver Checker

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

# Microsoft Windows - Storage QoS Filter Driver Checker

#### EDB-ID:

###### 52399

#### CVE:

###### [2025-49730](https://nvd.nist.gov/vuln/detail/CVE-2025-49730)

---

**EDB Verified:**

#### Author:

###### [nu11secur1ty](/?author=10359)

#### Type:

###### [local](/?type=local)

---

#### Platform:

###### [Windows](/?platform=windows)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
# Titles:  Microsoft Windows - Storage QoS Filter Driver Checker
# Author: nu11secur1ty
# Date: 08/04/2025
# Vendor: Microsoft
# Software: https://www.microsoft.com/en-us/software-download/windows11
# Reference:
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49730

## Description
This PowerShell script checks if your Windows system is vulnerable to
**CVE-2025-49730**, a critical vulnerability in the `storqosflt.sys`
Storage QoS Filter Driver.

## Features

- Detects if the `storqosflt` driver is present.
- Retrieves the driver version and compares it against the known patched
version (`10.0.26100.1`).
- Verifies the driver's digital signature to ensure authenticity.
- Calculates the SHA-256 hash of the driver file for integrity verification.
- Retrieves recent system event logs related to `storqosflt` to identify
suspicious or unusual activity.

## Usage

1. Open PowerShell with Administrator privileges.
2. Run the script:

   ```powershell
   .\Check-StorQoS-CVE2025.ps1
   ```

3. Review the output:

   - **Red messages** indicate vulnerable or suspicious conditions (e.g.,
vulnerable driver version or invalid digital signature).
   - **Yellow messages** indicate warnings or missing data.
   - **Green messages** indicate good or safe status.

## Requirements

- Windows PowerShell (tested on Windows 10 and 11).
- Execution policy set to allow running local scripts (`Set-ExecutionPolicy
RemoteSigned` may be needed).
- Administrator privileges recommended for full access to driver info and
logs.

## Disclaimer

This script **does not** attempt to exploit the vulnerability. It only
checks system status to **prove** vulnerability presence or absence based
on driver version, signature, and logs.

## Contact

For questions or improvements, please open an issue or contact the author.

# Source:
[href](
https://github.com/nu11secur1ty/Windows11Exploits/tree/main/2025/CVE-2025-49730
)

# Buy me a coffee if you are not ashamed:
[href](https://www.paypal.com/donate/?hosted_button_id=ZPQZT5XMC5RFY)

# Source download
[href](
https://nu11secur1ty.github.io/DownGit/#/home?url=https://github.com/nu11secur1ty/Windows11Exploits/tree/main/2025/CVE-2025-49730
)

# Time spent:
01:35:00

--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
                          nu11secur1ty <http://nu11secur1ty.com/>

--

System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstorm.news/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
                          nu11secur1ty <http://nu11secur1ty.com/>
```

**Tags:**

**Advisory/Source:**
[Link](https://github.com/nu11secur1ty/Windows11Exploits/tree/main/2025/CVE-2025-49730)

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
and usually sensitive, informatio...