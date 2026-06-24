---
title: FortiBleed: What Security Teams Need to Know (and Why This Story Is Bigger Than Fortinet)
url: https://securityuncorked.com/2026/06/fortibleed-what-security-teams-need-to-know-and-why-this-story-is-bigger-than-fortinet/
source: Security Uncorked
date: 2026-06-23
fetch_date: 2026-06-24T06:05:01.111456
---

# FortiBleed: What Security Teams Need to Know (and Why This Story Is Bigger Than Fortinet)

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)* ···

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)* ···

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

[![Security Uncorked](https://securityuncorked.com/wordpress/wp-content/uploads/2022/05/SU-blog-logonew.jpg)](https://securityuncorked.com/)

* 0

  + No videos yet!

    Click on "Watch later" to put videos here

* [Home](http://securityuncorked.com/)* [About JJ](https://securityuncorked.com/jennifer-minella/)* [Books](https://securityuncorked.com/books/)* [Topics](https://securityuncorked.com/topics/)
        + [Wireless](https://securityuncorked.com/category/wireless/)+ [Zero Trust, NAC, and 802.1X](https://securityuncorked.com/category/zero-trust-nac/)+ [Network Niblets](https://securityuncorked.com/category/network-niblets/)+ [Events](https://securityuncorked.com/category/events/)+ [Random-izations](https://securityuncorked.com/category/random-izations/)
                  - [J! True Stories](https://securityuncorked.com/category/j-true-stories/)- [Industry Insider](https://securityuncorked.com/category/industry-insider/)+ [White Papers & Guides](https://securityuncorked.com/category/white-papers-guides/)* [My Schedule](https://securityuncorked.com/schedule/)* [Contact](https://securityuncorked.com/contact/)

![Image showing attacker pivot from firewall to inside the network](https://securityuncorked.com/wordpress/wp-content/uploads/2026/06/FortiBleed-image-thumbnail-pivot-1500x350.png)

[Next
Chrome is Silently Installing 4GB AI Model on Your Device without Consent. Here’s how to find it and remove it.](https://securityuncorked.com/2026/05/how-to-stop-chrome-from-silently-installing-ai-model-on-your-device/)

[Industry Insider](https://securityuncorked.com/category/industry-insider/), [Zero Trust and NAC](https://securityuncorked.com/category/zero-trust-nac/)

# FortiBleed: What Security Teams Need to Know (and Why This Story Is Bigger Than Fortinet)

1 day ago

11 min read

[Add comment](https://securityuncorked.com/2026/06/fortibleed-what-security-teams-need-to-know-and-why-this-story-is-bigger-than-fortinet/#respond)

Most stories miss the most critical part of FortiBleed - the firewall wasn't the destination and it wasn't a breach. Attackers are targeting inside the network, capturing creds, exfiltrating data; hitting AD/LDAP, HTTP, FTP, SNMP, Telnet, SNMP, Kerberos, NTLM and more. Your whole infrastructure may be at risk.

Over the past several days, I’ve spent a lot of time digging through [FortiBleed](https://arstechnica.com/security/2026/06/massive-breach-spills-credentials-for-thousands-of-sensitive-networks/) research, public datasets, researcher findings, and incident analyses. The more I read, the more I realized something:

**Most of the headlines are focusing on the wrong thing.**

The common narrative is that FortiBleed is a Fortinet password leak.

That’s true—but it’s also woefully incomplete.

What makes FortiBleed remarkable is that it provides a rare look inside a modern credential-harvesting operation. Thanks to an exposed attacker server discovered by researchers, we aren’t just seeing the results of an attack. We’re seeing much of the attacker’s infrastructure, tooling, workflows, automation, and post-compromise activity. Down to a rarely seen view of their own [Hashtopolis](https://docs.hashtopolis.org/) implementation for industrial-scale password cracking.

In cybersecurity, we don’t often get that opportunity.

| **Here’s the 90-second TL:DR for this post** |
| --- |
| Most of the coverage is completely missing the three most critical details including mitigation.   1 — It was not a breach; a researcher stumbled on the attacker’s exposed infrastructure and got access to their full operation. This is covered in most articles, the next three points aren’t.  2 — It was not just a combination of leaked databases, the attackers built a semi-automated CREDENTIAL THEFT PLATFORM. They targeted FortiGates, Sophos firewalls, and MSSQL all in bulk.  3 — The goal wasn’t to get into firewalls, it was to pivot INSIDE the network, which they did successfully. They got Active Directory credentials, full GPO templates. Kerberos tokens and NTLM hashes (which they cracked), unencrypted management traffic including HTTP, SNMP, FTP, Telnet, plus SMTP and other mail protocols.  4 — Many FortiGates are still vulnerable after the 2025 firmware update b/c the users HAVE TO LOG IN for the SYSTEM TO RE-GENERATE THE NEW HASH. |

[![](https://securityuncorked.com/wordpress/wp-content/uploads/2026/06/FortiBleed-image-generated-1024x576.png)](https://securityuncorked.com/wordpress/wp-content/uploads/2026/06/FortiBleed-image-generated.png)

## FortiBleed Isn’t Just a Fortinet Story

One of the first misconceptions worth clearing up is that FortiGate devices were the only targets.

Based on publicly available research, we know the operators were also targeting:

* Sophos User Portal instances
* Microsoft SQL Server deployments
* Active Directory environments
* VPN infrastructure
* **Internal enterprise services**

I bolded that last item because THIS IS THE PART MOST PEOPLE ARE MISSING!

> The attackers were accessing INTERNAL networks and scraping combos of cleartext and encrypted credentials — HTTP, FTP, mail protocols SMTP/POP3/IMAP, LDAP, SNMP, Telnet and Kerberos and NTLM hashes.

Fortinet appears to have been the largest target set, but the operation itself was focused on credentials.

The firewall was the starting point—not the objective. But, more on that later!

## What Researchers Found

The operation came to light because the attackers accidentally exposed their own infrastructure. Cue the snickers.

Researchers (as far as I know, this was found by [Volodymyr (Bob) Daichenko](https://www.linkedin.com/in/vdyachenko/recent-activity/all/) based in Ukraine) discovered an open directory containing:

* Credential dat...