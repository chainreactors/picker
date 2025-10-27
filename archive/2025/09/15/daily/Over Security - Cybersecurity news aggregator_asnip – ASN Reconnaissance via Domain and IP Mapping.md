---
title: asnip – ASN Reconnaissance via Domain and IP Mapping
url: https://www.darknet.org.uk/2025/09/asnip-asn-reconnaissance-via-domain-and-ip-mapping/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-15
fetch_date: 2025-10-02T20:10:14.010685
---

# asnip – ASN Reconnaissance via Domain and IP Mapping

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

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# asnip – ASN Reconnaissance via Domain and IP Mapping

September 8, 2025

Views: 455

In red team operations, one of the earliest and most valuable tasks is to expand the external attack surface. Autonomous System Numbers (ASNs) provide insight into which IP ranges belong to an organisation. **asnip** is a lightweight Go tool that automates this process: given a target domain or IP, it identifies the ASN, retrieves the related Classless Inter-Domain Routing (CIDR) blocks, and enumerates them into IP addresses.

![asnip - ASN Reconnaissance via Domain and IP Mapping](https://www.darknet.org.uk/wp-content/uploads/2025/09/asnip-ASN-Reconnaissance-via-Domain-and-IP-Mapping-640x427.jpg)

Unlike more heavyweight recon frameworks, asnip focuses purely on ASN → CIDR → IP mapping. This makes it fast, simple, and practical for reconnaissance phases where operators need to quickly turn a single known host into a broader network footprint.

## Features

* **Domain/IP to ASN mapping:** Automatically resolves domains or IPs to their owning ASN.
* **CIDR retrieval:** Queries an external API (HackerTarget) to fetch associated CIDR ranges.
* **IP enumeration:** Converts CIDR blocks into a list of individual IP addresses.
* **Console output:** Optional printing of results alongside file output.
* **Written in Go:** Small, portable binary suitable for integration into recon workflows.

## Installation

Install directly with Go:

`go install github.com/harleo/asnip@latest`

Requires a Go environment to be present on the host.

## Usage

`Usage:
 -t string
 Domain or IP address (Required)
 -p string
 Print results to console`

## Example

`$ asnip -t google.com -p`

`[?] ASN: "15169" ORG: "GOOGLE, US"
8.8.4.0/24
... snip ...
[.] Writing 616 CIDRs to file...
[.] Converting to IPs...
8.8.8.1
... snip ...
[.] Writing 14725936 IPs to file...
[!] Done.`

## Attack Scenario

A red team begins reconnaissance on a financial services company. With only the primary domain name in scope, they run:

`asnip -t targetbank.com -p`

The tool resolves the organization’s ASN and extracts dozens of associated CIDR ranges. Converting these to IPs reveals not just the main web servers, but forgotten legacy mail infrastructure still tied to the company. This expanded list becomes the foundation for further vulnerability scanning and exploitation attempts.

## Red Team Relevance

asnip’s simplicity is its strength. It strips ASN reconnaissance down to the essentials: map domains and IPs to ASNs, get the ranges, and convert them to targets. For operators, this reduces time spent manually querying routing databases and ensures coverage of entire network blocks that might otherwise be missed.

Defenders can also benefit by running asnip on their own domains to confirm whether shadow IP ranges or forgotten allocations are still tied to their organisation.

## Conclusion

*asnip* is a focused, Go-based tool for ASN reconnaissance. Automating ASN lookups and CIDR expansion enables red teams to move quickly from a single seed host to a comprehensive list of potential targets. For attackers, it means faster surface discovery. For defenders, it highlights the value of monitoring ASN allocations as part of external asset management.

You can read more or download asnip here: <https://github.com/harleo/asnip>

## Related Posts:

* [Argus - Ultimate Reconnaissance Toolkit for…](https://www.darknet.org.uk/2025/07/argus-ultimate-reconnaissance-toolkit-for-offensive-recon-operations/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [ChromeAlone - Chromium Browser C2 Implant for Red…](https://www.darknet.org.uk/2025/08/chromealone-chromium-browser-c2-implant-for-red-team-operations/)
* [PsMapExec - PowerShell Command Mapping for Lateral Movement](https://www.darknet.org.uk/2025/07/psmapexec-powershell-command-mapping-for-lateral-movement/)
* [TREVORspray - Credential Spray Toolkit for Azure,…](https://www.darknet.org.uk/2025/07/trevorspray-credential-spray-toolkit-for-azure-okta-owa-more/)
* [Recon-ng - Web Reconnaissance Framework](https://www.darknet.org.uk/2016/04/recon-ng-web-reconnaissance-framework/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fasnip-asn-reconnaissance-via-domain-and-ip-mapping%2F)

[Tweet](https://twitter.com/intent/tweet?text=asnip+-+ASN+Reconnaissance+via+Domain+and+IP+Mapping&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fasnip-asn-reconnaissance-via-domain-and-ip-mapping%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fasnip-asn-reconnaissance-via-domain-and-ip-mapping%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fasnip-asn-reconnaissance-via-domain-and-ip-mapping%2F&text=asnip+-+ASN+Reconnaissance+via+Domain+and+IP+Mapping)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fasnip-asn-reconnaissance-via-domain-and-ip-mapping%2F)

[Email](/cdn-cgi/l/email-protection#b18ec2c4d3dbd4d2c58cd0c2dfd8c19483819c948381f0e2ff948381e3d4d2dedfdfd0d8c2c2d0dfd2d4948381c7d8d0948381f5dedcd0d8df948381d0dfd5948381f8e1948381fcd0c1c1d8dfd697d3ded5c88cd0c2dfd8c1948381dcd0c1c2948381d5dedcd0d8dfc2948381d0dfd5948381f8e1c2948381c5de948381c5d9d4d8c3948381f0c4c5dedfdedcdec4c2948381e2c8c2c5d4dc948381ffc4dcd3d4c3c2948381948389f0e2ffc29483889483f2948381c3d4c5c3d8d4c7d4c2948381f2f8f5e3c29483f2948381d0dfd5948381d2dedfc7d4c3c5c2948381c5d9d4dc948381d8dfc5de948381f8e1c2948381d7dec3948381c3d4d2dedfdfd0d8c2c2d0dfd2d49f9481f59481f09481f59481f0e3d4d0d591fcdec3d491f9d4c3d48b91948381d9c5c5c1c29482f09483f79483f7c6c6c69fd5d0c3dadfd4c59fdec3d69fc4da9483f7838183849483f781889483f7d0c2dfd8c19cd0c2df9cc3d4d2dedfdfd0d8c2c2d0dfd2d49cc7d8d09cd5dedcd0d8df9cd0dfd59cd8c19cdcd0c1c1d8dfd69483f7)

Filed Under: [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) Tagged With: [info gathering](https://www.darknet.org.uk/tag/info-gathering/), [information gathering](https://www.darknet.org.uk/tag/information-gathering/), [network recon](https://www.darknet.org.uk/tag/network-recon/), [red team](https://www.darknet.org.uk/tag/red-team/)

## Reader Interactions

### Leave a Reply [Cancel reply](/2025/09/asnip-asn-reconnaissance-via-domain-and-ip-mapping/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Δ

## Primary Sidebar

### Search Darknet

Search the site ...

* [Email](https://www.darknet.org.uk/contact-darknet/)
* [Facebook](https://www.facebook.com/darknet.org.uk/)
* [LinkedIn](https://www.linkedin.com/company/25076296/)
* [RSS](https://www.darknet.org.uk/feed/)
* [Twitter](https://x.com/THEdarknet)

**[Advertise on Darknet](https://www.darknet.org.uk/contact-darknet/advertise/)**

### Latest Posts

[![Inside Dark Web Exploit Markets in 2025 Pricing, Access & Active Selle...