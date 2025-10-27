---
title: [remote] Microsoft Edge (Chromium-based) 135.0.7049.114/.115 - Information Disclosure
url: https://www.exploit-db.com/exploits/52389
source: Exploit-DB.com RSS Feed
date: 2025-08-04
fetch_date: 2025-10-07T00:15:15.000874
---

# [remote] Microsoft Edge (Chromium-based) 135.0.7049.114/.115 - Information Disclosure

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

# Microsoft Edge (Chromium-based) 135.0.7049.114/.115 - Information Disclosure

#### EDB-ID:

###### 52389

#### CVE:

###### [2025-49741](https://nvd.nist.gov/vuln/detail/CVE-2025-49741)

---

**EDB Verified:**

#### Author:

###### [nu11secur1ty](/?author=10359)

#### Type:

###### [remote](/?type=remote)

---

#### Platform:

###### [Windows](/?platform=windows)

#### Date:

###### 2025-08-03

---

**Vulnerable App:**

```
# Titles: Microsoft Edge (Chromium-based) 135.0.7049.114/.115 - Information Disclosure
# Date: 08/02/2025
# Vendor: Microsoft
# Software: https://www.microsoft.com/bg-bg/edge/download?form=MA13FJ
# Reference:
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49741

## Description

# CVE-2025-49741 Exploit Server
**Author:** nu11secur1ty (2025)

## Overview
This Python script simulates an exploit targeting a Microsoft Edge
(Chromium-based) information disclosure vulnerability identified as
**CVE-2025-49741**.

It runs two HTTP servers concurrently:

- **Malicious Server (port 8080):** Serves a crafted page that collects
victim headers and simulates an internal request to the exfiltration
endpoint.
- **Exfiltration Endpoint (port 1337):** Receives simulated internal
requests and logs headers for demonstration purposes.

## Components

### MaliciousRequestHandler
- Handles HTTP GET requests on port 8080.
- Logs the victim's IP address, User-Agent, and all request headers.
- Sends a crafted HTTP GET request to the exfiltration server on port 1337
with spoofed headers to simulate internal communication.
- Responds with an HTML page indicating that the victim's information is
being sent.

### ExfilEndpoint
- Handles HTTP GET requests on port 1337.
- Logs all headers received, simulating data exfiltration.
- Responds with a success message.

## Features
- Automatically detects the local IP address to bind the servers.
- Graceful shutdown on Ctrl+C (SIGINT), ensuring both servers close cleanly.
- Uses `ThreadingTCPServer` for responsive handling of multiple connections.
- Clear console logging for monitoring victim connections and exfiltration
simulation.

## Requirements
- Python 3.6+
- `requests` library (`pip install requests`)

## Usage
1. Run the script:
   ```bash
   python CVE-2025-49741.py
   ```
2. The script will print the URLs where both servers are running (e.g.,
`http://192.168.x.x:8080` and `http://192.168.x.x:1337`).
3. Press Ctrl+C to stop both servers gracefully.

## Notes
- This tool is for educational and research purposes only.
- Do NOT use against systems you do not own or have explicit permission to
test.
- The exploit logic is simulated and does NOT perform real exploitation but
mimics the vulnerability for demonstration.

## Disclaimer
Use responsibly. The author is not responsible for any misuse of this
software.

---
**nu11secur1ty 2025**

# Video:
[href](https://www.youtube.com/watch?v=cWClT0Hvqac)

# Source:
[href](
https://github.com/nu11secur1ty/CVE-mitre/tree/main/2025/CVE-2025-49741)

# Buy me a coffee if you are not ashamed:
[href](https://www.paypal.com/donate/?hosted_button_id=ZPQZT5XMC5RFY)

# Source download
[href](
https://nu11secur1ty.github.io/DownGit/#/home?url=https://github.com/nu11secur1ty/CVE-mitre/tree/main/2025/CVE-2025-49741
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
[Link](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49741)

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
devel...