---
title: Wireshark Cheatsheet
url: https://www.blackhillsinfosec.com/wireshark-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:18.821310
---

# Wireshark Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/), [Wireshark](https://www.blackhillsinfosec.com/tag/wireshark/)

# [Wireshark Cheatsheet](https://www.blackhillsinfosec.com/wireshark-cheatsheet/)

Written by [Shad Brown](https://bsky.app/profile/winterknight.net) || Revised by [Bronwen Aker](https://www.blackhillsinfosec.com/team/bronwen-aker/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_3.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**Wireshark Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_Wireshark.pdf)

Find the tool here: <https://www.wireshark.org/>

---

Wireshark is an incredible tool used to read and analyze network traffic coming in and out of an endpoint. Additionally, it can load previously captured traffic to assist with troubleshooting network issues or analyze malicious traffic to help determine what a threat actor is doing on your network.

## Basics

The most basic filtering Wireshark provides is by protocol. Simply type the protocol name:

* `dns`
* `http`
* `arp`
* `icmp`
* `tls`
* And many more!

## Logical Operators

* Logical AND: `and` or `&&`
* Logical OR : `or` or `||`
* Logical NOT: `not` or `!`

## Comparison Operators

* Equal to: `eq` or `==`
* Not Equal to: `ne` or `!=`
* Greater than: `gt` or `>`
* Less than: `lt` or `<`
* Greater than or equal to: `ge` or `>=`
* Less than or equal to: `le` or `<=`

## Transport Layer Filters

These also work for UDP!

* Port filtering: `tcp.port == 443`
* Source port filtering: `tcp.srcport == 443`
* Destination port filtering: `tcp.dstport == 443`
* TCP session tracking: `tcp.stream == 0`

## IP Filters

* **Filter by IP (matches source or destination):**

```
ip.addr == 192.168.0.1
```

* **Filter by source IP:**

```
ip.src == 192.168.0.1
```

or

```
ip.src == 192.168.1.0/24
```

* **Filter to destination IP:**

```
ip.dst == 192.168.0.1
```

or

```
ip.dst == 192.168.1.0/24
```

* **Exclude an IP:**

```
ip.addr != 192.168.0.1
```

* **Filter to multiple IPs (any of them):**

```
ip.addr == 192.168.0.1
```

or

```
ip.addr == 10.0.0.1
```

* **Filter for traffic between two specific IPs (both directions):**

```
(ip.src == 192.168.0.1 and ip.dst == 10.0.0.1)
```

or

```
(ip.src == 10.0.0.1 and ip.dst == 192.168.0.1)
```

* **Filter by subnet:**

```
ip.addr == 192.168.1.0/24
```

* **IP range filtering:**

```
ip.addr >= 192.168.0.1 and ip.addr <= 192.168.0.100
```

## Useful GUI Features

Wireshark’s graphical interface has handy right-click options:

* **Apply as Filter:** Immediately applies the selected field as the display filter.
* **Prepare as Filter:** Constructs the filter expression in the text bar so you can edit it before running it.

Wireshark also makes it easy to track individual conversations:

* Right-click a packet, then select **Follow > TCP Stream or Follow > UDP Stream**. This opens a window showing the conversation chronologically and applies the appropriate stream filter.

## Useful Statistical Tools

Wireshark provides statistical summaries to help you analyze traffic:

* Statistics > IPv4 Statistics > Destinations and Ports
  + *Shows all IPs, transport protocols, and ports involved in communication. You can apply display filters here to narrow results.*
* Statistics > HTTP > Requests
  + *Displays web requests, including domains and endpoints browsed during the capture.*
* Statistics > Protocol Hierarchy
  + *Gives a tree breakdown of all protocols seen in the capture.*
* Statistics > IO Graphs
  + *Lets you visualize traffic volume over time with custom filters.*

## Other Useful Filters and Features

* Exclude local network noise:

```
not arp and not ssdp and not mdns
```

* Filter packets by length:

```
frame.len > 500
```

or

```
frame.len > 1000
```

* Find packets with TCP errors or analysis flags:

```
tcp.analysis.flags
```

* Filter by MAC address:

```
eth.addr == aa:bb:cc:dd:ee:f
```

* HTTP host filter:

```
http.host == “example.com”
```

* TLS SNI filter:

```
tls.handshake.extensions_server_name == “example.com”
```

* Exclude an...