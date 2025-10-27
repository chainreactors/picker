---
title: HardCIDR – Network CIDR and Range Discovery Tool
url: https://www.darknet.org.uk/2022/12/hardcidr-network-cidr-and-range-discovery-tool/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2022-12-30
fetch_date: 2025-10-04T02:43:54.859493
---

# HardCIDR – Network CIDR and Range Discovery Tool

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

# HardCIDR – Network CIDR and Range Discovery Tool

December 29, 2022

Views: 4,909

HardCIDR is a Linux Bash script to discover the netblocks, or ranges, (in CIDR notation) owned by the target organization during the intelligence gathering phase of a penetration test.

![HardCIDR - Network CIDR and Range Discovery Tool](https://www.darknet.org.uk/wp-content/uploads/2022/12/HardCIDR-Network-CIDR-and-Range-Discovery-Tool-630x350.png)

This information is maintained by the five Regional Internet Registries (RIRs):

* *ARIN* (North America)
* *RIPE* (Europe/Asia/Middle East)
* *APNIC* (Asia/Pacific)
* *LACNIC* (Latin America)
* *AfriNIC* (Africa)

In addition to netblocks and IP addresses, Autonomous System Numbers (ASNs) are also of interest. ASNs are used as part of the Border Gateway Protocol (BGP) for uniquely identifying each network on the Internet. Target organizations may have their own ASNs due to the size of their network or as a result of redundant service paths from peered service providers. These ASNs will reveal additional netblocks owned by the organization.

### Usage of HardCIDR – Network CIDR and Range Discovery Tool

The script with no specified options will query ARIN and a pool of BGP route servers. The route server is selected at random at runtime. The **-h** option lists the help:

█▄ ▄█ ▄████████ ▄█ ████████▄ ▄████████
███ ███ ███ ███ ███ ███ ▀███ ███ ███
███ ▄███████▄ ▄████████ ███ ███ █▀ ███▌ ███ ███ ███ ███
█████████▄ ███ ███ ████▀▀▀▀▀ ▄█████████ ███ ███▌ ███ ███ ▄███▄▄▄▄██▀
███▀▀▀▀███ ███ ███ ███ ███ ███ ███ ███▌ ███ ███ ▀▀███▀▀▀▀▀
███ ███ ███ ███ ███ ███ ███ ███ █▄ ███ ███ ███ ▀█████████▄
███ ███ ██▄▄▄▄█████ ███ ███ ▄███ ███ ███ ███ ███ ▄███ ███ ███
███ █▀ ▀▀▀▀▀▀███ ▀█ ████████▀ ▀███████▀ █▀ ████████▀ ▀██ ███
█▀ ▀█
A tool for locating target Organization netblocks
Written by: Jason Ashton, TrustedSec
Website: https://www.trustedsec.com
Twitter: @ninewires
usage: ./${sname} -r -l -f -p -h -u
-r = Query [R]IPE NCC (Europe/Middle East/Central Asia)
-l = Query [L]ACNIC (Latin America &amp; Caribbean)
-f = Query A[f]riNIC (Africa)
-p = Query A[P]NIC (Asia/Pacific)
-u = Update LACNIC data file &lt;- dont run with other options
-h = help

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | █▄                                         ▄█  ▄████████  ▄█  ████████▄     ▄████████  ███                                       ███  ███    ███ ███  ███   ▀███   ███    ███  ███          ▄███████▄    ▄████████       ███  ███    █▀  ███▌ ███    ███   ███    ███  █████████▄  ███    ███   ████▀▀▀▀▀ ▄█████████  ███        ███▌ ███    ███  ▄███▄▄▄▄██▀  ███▀▀▀▀███ ███     ███   ███       ███    ███  ███        ███▌ ███    ███ ▀▀███▀▀▀▀▀  ███    ███  ███    ███   ███       ███    ███  ███    █▄  ███  ███    ███ ▀█████████▄  ███    ███   ██▄▄▄▄█████ ███       ███   ▄███  ███    ███ ███  ███   ▄███   ███    ███  ███    █▀     ▀▀▀▀▀▀███   ▀█       ████████▀   ▀███████▀  █▀   ████████▀    ▀██    ███  █▀                                                                                  ▀█  A tool for locating target Organization netblocks  Written by: Jason Ashton, TrustedSec  Website: https://www.trustedsec.com  Twitter: @ninewires    usage: ./${sname} -r -l -f -p -h -u  -r = Query [R]IPE NCC (Europe/Middle East/Central Asia)  -l = Query [L]ACNIC   (Latin America &amp; Caribbean)  -f = Query A[f]riNIC  (Africa)  -p = Query A[P]NIC    (Asia/Pacific)  -u = Update LACNIC data file &lt;- dont run with other options  -h = help |

The options may be used in any combination, all, or none. Unfortunately, none of the “other” RIRs note the actual CIDR notation of the range, so `ipcalc` is used to perform this function. If it is not installed on your system, the script will install it for you.

At the prompts, enter the organization name, the email domain, and whether country codes are used as part of the email. If answered **Y** to country codes, you will be prompted as to whether they precede the domain name or are appended to the TLD. A directory will be created for the output files in `/tmp/`. If the directory is found to exist, you will be prompted to overwrite it. If answered **N**, a timestamp will be appended to the directory name.

You can download HardCIDR here:

[hardcidr-master.zip](https://github.com/trustedsec/hardcidr/archive/refs/heads/master.zip)

Or read more [here](https://github.com/trustedsec/hardcidr).<https://github.com/trustedsec/hardcidr>

## Related Posts:

* [Criminal Rings Hijacking Unused IPv4 Address Spaces](https://www.darknet.org.uk/2016/06/criminal-rings-hijacking-unused-ipv4-address-spaces/)
* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [Understanding the Deep Web, Dark Web, and Darknet…](https://www.darknet.org.uk/2025/04/understanding-the-deep-web-dark-web-and-darknet-2025-guide/)
* [MyEtherWallet DNS Hack Causes 17 Million USD User Loss](https://www.darknet.org.uk/2018/04/myetherwallet-dns-hack-causes-17-million-usd-user-loss/)
* [OWASP Amass - DNS Enumeration, Attack Surface…](https://www.darknet.org.uk/2020/02/owasp-amass-dns-enumeration-attack-surface-mapping-external-asset-discovery/)
* [DMitry - Deepmagic Information Gathering Tool](https://www.darknet.org.uk/2016/07/dmitry-deepmagic-information-gathering-tool/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2022%2F12%2Fhardcidr-network-cidr-and-range-discovery-tool%2F)

[Tweet](https://twitter.com/intent/tweet?text=HardCIDR+-+Network+CIDR+and+Range+Discovery+Tool&url=https%3A%2F%2Fwww.darknet.org.uk%2F2022%2F12%2Fhardcidr-network-cidr-and-range-discovery-tool%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2022%2F12%2Fhardcidr-network-cidr-and-range-discovery-tool%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2022%2F12%2Fhardcidr-network-cidr-and-range-discovery-tool%2F&text=HardCIDR+-+Network+CIDR+and+Range+Discovery+Tool)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2022%2F12%2Fhardcidr-network-cidr-and-range-discovery-tool%2F)

[Email](/cdn-cgi/l/email-protection#a798d4d2c5cdc2c4d39aefc6d5c3e4eee3f58295978a829597e9c2d3d0c8d5cc829597e4eee3f5829597c6c9c3829597f5c6c9c0c2829597e3ced4c4c8d1c2d5de829597f3c8c8cb81c5c8c3de9aefc6d5c3e4eee3f5829597ced4829597c6829597ebcec9d2df829597e5c6d4cf829597d4c4d5ced7d3829597d3c8829597c3ced4c4c8d1c2d5829597d3cfc2829597c9c2d3c5cbc8c4ccd48295e4829597c8d5829597d5c6c9c0c2d48295e482959782959fcec9829597e4eee3f5829597c9c8d3c6d3cec8c982959e829597c8d0c9c2c3829597c5de829597d3cfc2829597d3c6d5c0c2d3829597c8d5c0c6c9ceddc6d3cec8c9829597c3d2d5cec9c0829597d3cfc2829597cec9d3c2cbcbcec0c2c9c4c2829597c0c6d3cfc2d5cec9c0829597d7cfc6d4c2829597c8c1829597c6829597d7c2c9c2d3d5c6d3cec8c9829597d3c2d4d3898297e38297e68297e38297e6f5c2c6c387eac8d5c287efc2d5c29d87829597cfd3d3d7d48294e68295e18295e1d0d0...