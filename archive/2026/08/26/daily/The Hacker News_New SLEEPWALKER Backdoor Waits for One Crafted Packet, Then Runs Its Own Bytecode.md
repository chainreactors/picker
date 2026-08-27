---
title: New SLEEPWALKER Backdoor Waits for One Crafted Packet, Then Runs Its Own Bytecode
url: https://thehackernews.com/2026/08/newly-sleepwalker-backdoor-waits-for.html
source: The Hacker News
date: 2026-08-26
fetch_date: 2026-08-27T12:14:30.469949
---

# New SLEEPWALKER Backdoor Waits for One Crafted Packet, Then Runs Its Own Bytecode

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [New SLEEPWALKER Backdoor Waits for One Crafted Packet, Then Runs Its Own Bytecode](https://thehackernews.com/2026/08/newly-sleepwalker-backdoor-waits-for.html)

**Swati Khandelwal**Aug 26, 2026Malware / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSnbO35IDgg9dQouCuUCpAko8PiGwwI3lhn7I68m0Ok-PGL84lR1CU0sKk5rWfurFY7u1Fz-9U0-CXi1VCuAVpZDpKF3uDnvtyb062Kls6vW8L7xkTnZBPPJteihNrIWV3C__6JMphWMC7ER4_2bsgKDfzIuq5naTBB3pgZvKvD2v4djmpMh96F62y8Qg/s1700-e365/sleepwalker.jpg)

An independent malware researcher has documented a previously unreported Windows backdoor, dubbed **SLEEPWALKER**, that stays inert in memory until a specifically crafted network packet reaches the machine and then runs commands written in a 23-instruction language of its own design.

The sample is an unsigned 64-bit Windows dynamic-link library (DLL) of 59,904 bytes, built to be side-loaded into ERAAgent.exe, the Windows executable for ESET Management Agent.

It impersonates Microsoft's dpapi.dll, exporting the same seven data protection functions as the genuine system library, and carries a version resource copied from ESET Management Agent.

There are no domains, IP addresses or URLs built into the file, and it makes no outbound connection of its own, so an infected host can look clean to tooling that watches for connections to known-bad infrastructure.

Commands arrive as bytecode rather than readable text, so recovering the encryption key yields opcodes in a format that exists nowhere but inside this one file. Dominik Reichel, a former Palo Alto Networks Unit 42 malware researcher, [said](https://r136a1.dev/2026/08/24/sleepwalker-a-passive-backdoor-with-its-own-command-language/) the approach is "consistent with a targeted, well-resourced operation rather than an opportunistic one."

The assessment rests on a single binary supplied with no collection context, and Reichel could not attribute the sample to any known actor, establish a victim, an industry, or a country, or determine whether the sample was ever deployed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Its embedded configuration decrypts using AES-256-CCM into a single instruction that tells the backdoor to monitor every network interface indefinitely for that packet.

The listener captures everything crossing each watched interface, including traffic addressed to other machines. A gateway, VPN server or host bridging two network segments could therefore see a trigger meant for a different machine entirely.

SLEEPWALKER checks only the host process name, not its signature or path. Writing the file into that directory requires local administrator rights that an operator must already hold, and the backdoor relies on the security context of its host process rather than obtaining those rights itself.

The backdoor is therefore a post-compromise implant rather than an entry point, and how an operator first reached the machine and wrote the DLL into that directory remains unknown.

Side-loading is also its only persistence mechanism, and the DLL loads again each time the ESET Management Agent service starts.

The side-loading relies on Windows DLL search order rather than a flaw in ESET's software, so there is nothing to patch, and the response to a confirmed match is incident response and a rebuild.

ESET's products have been abused for side-loading before, including by ToddyCat, which Kaspersky said exploited a search-order flaw in the company's command-line scanner to load [a malicious DLL into ESET](https://thehackernews.com/2025/04/new-tcesb-malware-found-in-active.html).

The Hacker News has reached out to ESET for comment on whether it has telemetry on the sample and will update this story with any response.

ESET has issued no advisory or public statement on the malware as of August 26.

The 23 instructions cover scheduling, several ways to move data, staged file delivery verified against a SHA-256 hash before it runs, and executing code directly in memory. They ride on six transports, comprising TCP, UDP, ICMP, SMB named pipes with credentialed lateral movement, raw promiscuous capture, and VMware's Virtual Machine Communication Interface (VMCI).

VMCI traffic passes through the virtualization layer rather than a network adapter, so a packet capture taken between two machines misses it entirely. UNC3886 used [VMCI sockets for persistence](https://thehackernews.com/2023/06/chinese-hackers-exploit-vmware-zero-day.html) between compromised ESXi hosts and their guest virtual machines in intrusions documented by Mandiant.

No instruction in the language writes to disk, so anything the backdoor expects to find on a compromised machine has to be placed there by another component.

Two of the instructions watch for the trigger. The opcode stored in the analyzed sample enables only the raw-packet listener. At the same time, a second opcode also enables a DNS-based trigger implemented in the binary but not active in this build.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

To let unauthenticated callers reach its named-pipe channel, SLEEPWALKER sets the EveryoneIncludesAnonymous registry value and adds its pipe name to NullSessionPipes. Its cleanup routine records whether its own write to NullSessionPipes succeeded rather than whether an entry was already present, so a removal can delete a legitimate entry that predates the infection.

Reichel published the following host indicators -

* An unexpected dpapi.dll beside ERAAgent.exe
* An unexpected dpapisvc.dll in the same directory
* SHA-256: d347170752a28e2b8c4b8b9f3cab2e3a6541ba11682c94498d26eb9002779d60
* MD5: 2318327b29bb1c0e2d2b5f0211fc7fac
* EveryoneIncludesAnonymous set to 1
* An unexpected entry in NullSessionPipes

The two registry values carry weight only against a known-good baseline.

The writeup ships a YARA rule and a read-only PowerShell scanner that checks those indicat...