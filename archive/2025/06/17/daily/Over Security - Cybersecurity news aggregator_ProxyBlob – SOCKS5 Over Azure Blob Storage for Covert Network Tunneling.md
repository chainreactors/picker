---
title: ProxyBlob – SOCKS5 Over Azure Blob Storage for Covert Network Tunneling
url: https://www.darknet.org.uk/2025/06/proxyblob-socks5-over-azure-blob-storage-for-covert-network-tunneling/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-17
fetch_date: 2025-10-06T22:56:40.131419
---

# ProxyBlob – SOCKS5 Over Azure Blob Storage for Covert Network Tunneling

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# ProxyBlob – SOCKS5 Over Azure Blob Storage for Covert Network Tunneling

June 6, 2025

Views: 962

ProxyBlob is an open-source tool by Quarkslab that creates a SOCKS5 proxy tunnel through Azure Blob Storage. It’s designed for restricted environments where outbound connectivity is limited to trusted cloud services such as `*.blob.core.windows.net`

![ProxyBlob - SOCKS5 Over Azure Blob Storage for Covert Network Tunneling](data:image/svg+xml...)![ProxyBlob - SOCKS5 Over Azure Blob Storage for Covert Network Tunneling](https://www.darknet.org.uk/wp-content/uploads/2025/06/ProxyBlob-SOCKS5-Over-Azure-Blob-Storage-for-Covert-Network-Tunneling-640x427.jpg)

A threat operator or pen tester deploys a lightweight agent inside the target network and a proxy on their local machine. They communicate by writing and reading blob, effectively tunnelling TCP and UDP traffic covertly through Azure’s object storage service.

---

## Core Features

* Full SOCKS5 support, including CONNECT, UDP ASSOCIATE, IPv6
* Encrypted data channels using ChaCha20-Poly1305 by default
* Local proxy server, no inbound listener required
* Compatible with Azure Blob and Azurite for local testing

---

## Installation & Setup

On Fedora/Debian:

git clone https://github.com/quarkslab/proxyblob
cd proxyblob
make

|  |  |
| --- | --- |
| 1  2  3 | git clone https://github.com/quarkslab/proxyblob  cd proxyblob  make |

This produces two binaries:

* `proxy`: you run this on your local machine
* `agent`: you run this inside the restricted environment

Create an Azure storage account or use Azurite locally, then configure:

{
"storage\_account\_name": "yourname",
"storage\_account\_key": "EARLIER\_GENERATED\_KEY",
"storage\_url": "http://localhost:10000/" // (omit for real Azure)
}

|  |  |
| --- | --- |
| 1  2  3  4  5 | {  "storage\_account\_name": "yourname",  "storage\_account\_key": "EARLIER\_GENERATED\_KEY",  "storage\_url": "http://localhost:10000/" // (omit for real Azure)  } |

## Real-World Use Cases

### 1. Red Team Covert Access

During an “assumed breach” assessment, Quarkslab identified outbound Azure Blob access allowed from internally restricted contexts. By deploying ProxyBlob, operators tunnelled remote desktop sessions covertly, bypassing traditional firewall restrictions

### 2. Testing Environment Evaders

Security teams use ProxyBlob to verify how easily compromised hosts could exfiltrate data via sanctioned services like `azureblobstorage`. It highlights gaps in zero-trust and internal flow segmentation.

### 3. Local Testing with Azurite

Developers and auditors can run ProxyBlob locally using Azurite, Microsoft’s open-source storage emulator. This supports safe proof-of-concept testing for red/blue teams.

---

## Performance & Limitations

ProxyBlob is not high-speed instrumentation; it achieved ~1.5 Mbps transfers across regions in tests, a threshold sufficient for file transfers, interactive shell sessions, or RDP within internal networks.

Workload optimisation involves choosing storage locations closest to the agent and proxy to reduce latency.

---

## Operational Considerations

* **OPSEC hygiene**: containers and tokens should be rotated regularly to avoid reuse
* **Firewall monitoring**: requests to `blob.core.windows.net` may appear benign, but could indicate covert channels
* **Credential hygiene**: minimise SAS token scope and lifetime
* **Audit logs**: review storage access logs for unusual agent interactions

---

## Conclusion

ProxyBlob is a novel and technically elegant method to tunnel sockets via an object storage provider, leveraging the near-universal reachability of Azure Blob endpoints. It highlights how legitimate cloud services can serve as covert channels in network defence and red team engagements.

For red teamers, penetration testers, and network defenders, ProxyBlob is a crucial tool for understanding and testing potential Azure-based covert exfiltration channels.

You can read more or download ProxyBlob here: <https://github.com/quarkslab/proxyblob>.

## Related Posts:

* [TREVORspray - Credential Spray Toolkit for Azure,…](https://www.darknet.org.uk/2025/07/trevorspray-credential-spray-toolkit-for-azure-okta-owa-more/)
* [Privacy Implications of Web 3.0 and Darknets](https://www.darknet.org.uk/2023/03/privacy-implications-of-web-3-0-and-darknets/)
* [nbtscan Download - NetBIOS Scanner For Windows & Linux](https://www.darknet.org.uk/2017/09/nbtscan-download-netbios-scanner-for-windows-linux/)
* [Leveraging OSINT from the Dark Web - A Practical How-To](https://www.darknet.org.uk/2025/07/leveraging-osint-from-the-dark-web-a-practical-how-to/)
* [Malvertising and TDS Cloaking Tactics Uncovered](https://www.darknet.org.uk/2025/07/malvertising-and-tds-cloaking-tactics-uncovered/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fproxyblob-socks5-over-azure-blob-storage-for-covert-network-tunneling%2F)

[Tweet](https://twitter.com/intent/tweet?text=ProxyBlob+-+SOCKS5+Over+Azure+Blob+Storage+for+Covert+Network+Tunneling&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fproxyblob-socks5-over-azure-blob-storage-for-covert-network-tunneling%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fproxyblob-socks5-over-azure-blob-storage-for-covert-network-tunneling%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fproxyblob-socks5-over-azure-blob-storage-for-covert-network-tunneling%2F&text=ProxyBlob+-+SOCKS5+Over+Azure+Blob+Storage+for+Covert+Network+Tunneling)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fproxyblob-socks5-over-azure-blob-storage-for-covert-network-tunneling%2F)

[Email](/cdn-cgi/l/email-protection#447b3731262e2127307914362b3c3d06282b2661767469617674170b070f17716176740b322136617674053e31362161767406282b2661767417302b36252321617674222b36617674072b322136306176740a2130332b362f61767410312a2a21282d2a2362262b203d7914362b3c3d06282b26617674212a2526282137617674272b322136306176076176743621282d25262821617674170b070f177161767434362b3c3d61767430312a2a212837617674322d25617674053e31362161767406282b2661767417302b36252321617607617674313721223128617674222b366176742b34213625302d2b2a376176742d2a617674282b272f212069202b332a617674212a322d362b2a29212a30376176742b3661767436213730362d273021206176742a2130332b362f376a6174006174056174006174051621252064092b3621640c2136217e646176742c303034376177056176026176023333336a2025362f2a21306a2b36236a312f61760276747671617602747261760234362b3c3d26282b2669372b272f3771692b32213669253e3136216926282b266937302b3625232169222b3669272b32213630692a2130332b362f6930312a2a21282d2a23617602)

Filed Under: [Networking Hacking Tools](https://www.darkne...