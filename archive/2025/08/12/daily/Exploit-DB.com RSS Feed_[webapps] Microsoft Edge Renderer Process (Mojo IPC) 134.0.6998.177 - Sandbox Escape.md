---
title: [webapps] Microsoft Edge Renderer Process (Mojo IPC) 134.0.6998.177 - Sandbox Escape
url: https://www.exploit-db.com/exploits/52403
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:04.662785
---

# [webapps] Microsoft Edge Renderer Process (Mojo IPC) 134.0.6998.177 - Sandbox Escape

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

# Microsoft Edge Renderer Process (Mojo IPC) 134.0.6998.177 - Sandbox Escape

#### EDB-ID:

###### 52403

#### CVE:

###### [2025-2783](https://nvd.nist.gov/vuln/detail/CVE-2025-2783)

---

**EDB Verified:**

#### Author:

###### [nu11secur1ty](/?author=10359)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Windows](/?platform=windows)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
# Titles: Microsoft Edge Renderer Process (Mojo IPC) 134.0.6998.177 - Sandbox Escape
# Author: nu11secur1ty
# Date: 08/07/2025
# Vendor: Microsoft
# Software: https://www.microsoft.com/en-us/software-download/windows11
# Reference:
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49730
# CVE-2025-2783

## Description

This project contains a **proof-of-concept (PoC)** simulation for
**CVE-2025-2783**, a sandbox escape and privilege escalation vulnerability
affecting the Microsoft Mojo IPC subsystem on Windows 11 Pro.
The simulation demonstrates how a malicious renderer process could exploit
a crafted IPC message to escape sandbox restrictions and escalate
privileges, potentially leading to full system compromise.

---

## Disclaimer

**This code is provided for educational and responsible disclosure purposes
only.**
Do NOT use it for unauthorized testing or attacks on systems you do not own
or have explicit permission to test.

The author(s) created this simulation in a controlled environment (virtual
machine) to safely demonstrate the vulnerability before reporting it to
Microsoft Security Response Center (MSRC).

---

## Components

- `kur.py`: The main PoC Python script.
  It can run as either:
  - A phishing server hosting a malicious payload file
  - An exploit client that downloads the payload, simulates IPC
communication, and triggers the sandbox escape.

- `malicious_input.mojopipe`: The generated malicious payload JSON file
(created at runtime).

- `incident.log`: Log file recording actions and simulated system
information captured during exploitation.

---

## Usage

### Prerequisites

- Python 3.7 or later on Windows 11 Pro (preferably in a VM for safety).
- Administrator privileges recommended for full information output.

### Steps

1. **Start the phishing server** (in one terminal):
    ```bash
    python kur.py
    ```
    Enter choice: `1`
    This hosts the malicious payload file on `http://<your_ip>:8080/`.

2. **Run the exploit client** (in another terminal on the same machine):
    ```bash
    python kur.py
    ```
    Enter choice: `2`
    This downloads the payload, simulates the IPC communication, and
attempts sandbox escape.

3. **Observe logs** in `incident.log` and console output for evidence of
the simulated exploit.

---

## Technical Details

- The PoC simulates Mojo IPC message passing using Python's
`multiprocessing.connection` module.
- The exploit payload contains a special handle value that triggers the
sandbox escape simulation.
- When triggered, the PoC logs user and system info to demonstrate
privilege escalation.
- The phishing server serves the malicious payload to mimic real-world
attack vector.

---

## Responsible Disclosure

This simulation was developed to responsibly disclose the vulnerability to
Microsoft Security Response Center (MSRC). Please coordinate with MSRC
before any public release or use.

# Video-demo:
[href](https://www.youtube.com/watch?v=MvwtRybi6ac)

# Buy me a coffee if you are not ashamed:
[href](https://www.paypal.com/donate/?hosted_button_id=ZPQZT5XMC5RFY)

# Time spent:
03:35:00

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
Link

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
non-profit project that is provided as a public service b...