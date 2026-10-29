---
title: Critical 16-Year-Old UEFI Flaw Can Run Code Before Secure Boot on Network-Booting Servers
url: https://thehackernews.com/2026/10/critical-16-year-old-uefi-flaw-can-run.html
source: The Hacker News
date: 2026-10-28
fetch_date: 2026-10-29T07:52:55.414793
---

# Critical 16-Year-Old UEFI Flaw Can Run Code Before Secure Boot on Network-Booting Servers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Critical 16-Year-Old UEFI Flaw Can Run Code Before Secure Boot on Network-Booting Servers](https://thehackernews.com/2026/10/critical-16-year-old-uefi-flaw-can-run.html)

**Swati Khandelwal**Oct 28, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoVVx2e6mg8LPbhDYmtubHewVD_9BI7UcctCMSwwG-h4SuOyZJOvIyTre_g9Ggo6sLw6Bjrse_1FsqKKThyiIvc5CbuYqq4caYCtUciHGg33wReFQgOjJuTX5FrnSS3OZTd_yjXt03l_kxwIX-NshU9A8wpANSdQwOWkDKzy31QdXkCD6UP21dOpfbjhg/s1700-nu-rw-lo-l85-e365/server-bios.jpg)

A critical 16-year-old flaw in **EDK II**, the open-source code that most hardware makers use to build UEFI firmware, can allow an attacker to run code on a machine before its operating system loads, but only while the machine is booting over the network.

UEFI firmware is the software that runs first when a computer is switched on, before the operating system. An attacker who can reach the machine with a crafted network message during such a network boot can hang the boot, or, with work tailored to the exact firmware build, run their own code before Secure Boot and other startup defenses load.

An attacker needs no password and no existing access to the machine, but does need to reach it over the network during the short window when it is booting this way.

Red Hat and SUSE, which both ship the affected code, rated the flaw as one an attacker exploits from an adjacent network position rather than across the open internet.

TianoCore, the project behind EDK II, [published an advisory](https://github.com/tianocore/edk2/security/advisories/GHSA-99cj-7hg9-mp4m) on October 22 and rated the flaw, [tracked as CVE-2026-97631](https://www.cve.org/CVERecord?id=CVE-2026-97631), 9.5 out of 10. A code fix exists, but no stable release of EDK II contains it yet, and the advisory still lists no patched version, so most users have nothing to install today.

### What the Flaw Lets an Attacker Do

The flaw is a buffer overflow in EDK II's network-boot code, known as PXE. During a PXE boot, a machine loads its startup image from the network instead of from a local disk.

As part of this, the PXE driver listens for ICMP error messages and the small status messages that network devices send back, and copies each one into a fixed 504-byte area of memory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The size checks in that copy are wrong in both the IPv4 and IPv6 versions of the code, so a message longer than 504 bytes spills past the area and overwrites nearby memory with data the attacker chose.

To set this off, an attacker only has to send one crafted error message to the machine's address while it is in the middle of a network boot. No password or existing access to the machine is needed.

The simple result is a crash: the boot hangs, and the machine fails to start. Getting code to run is much harder and far less reliable. The advisory says that an attacker who knows the exact firmware build can plant a "counterfeit event" that causes the firmware to run the attacker's own code, so an exploit has to be built for a specific build.

When code runs, it executes within the firmware, before Secure Boot and other boot-time checks have verified anything. That timing is what makes the flaw serious.

Code planted this way runs only once and does not survive a reboot by itself. That single run is still enough to install other code that does start on every boot.

### Who Is Affected

The bug sits in EDK II up to and including [edk2-stable202608](https://github.com/tianocore/edk2/releases), the newest stable version, dated August 21. EDK II is the reference code that nearly every UEFI firmware vendor builds on, including the independent BIOS makers AMI, Insyde, and Phoenix, as well as Microsoft's hardened fork, Project Mu.

The flawed copy loop has been in the code since a commit added in [November 2010](https://github.com/tianocore/edk2/commit/a3bcde70e6dc69000f85cc5deee98101d2ae200a), The Hacker News found by tracing the project's history.

PXE network boot is turned on by default in EDK II's standard build. The flaw does not affect home or office users who boot only from a local disk. It applies to organizations whose machines boot over a network, primarily servers and data center equipment.

How many shipping products carry the vulnerable code is not known. Intel told Ars Technica that none of its "commercial products currently under security support" are known to be affected, and that it "does not include the affected EDK2 functionality in its reference code," though an OEM board vendor or system maker could add it.

Arm said the flaw "is not directly applicable to Arm's product portfolio." Both companies' own firmware draws on EDK II.

Linux distributions also ship the code. Red Hat [lists its edk2 package](https://access.redhat.com/security/cve/CVE-2026-97631) in Red Hat Enterprise Linux 8, 9, and 10 as affected and not yet fixed, and [SUSE](https://www.suse.com/security/cve/CVE-2026-97631/) and [Debian](https://security-tracker.debian.org/tracker/CVE-2026-97631) mark their equivalent packages the same way.

AMD, Phoenix Technologies, AMI, Microsoft, and Amazon did not answer the tech news site's questions before publication, and TianoCore did not respond either, so the status of their products remains unclear.

### Is There a Fix?

A fix has been [merged into the EDK II source code](https://github.com/tianocore/edk2/pull/13302). It rewrites the faulty copy so an oversized message is cut off at 504 bytes instead of spilling over, and it reached the main development branch on October 15.

No stable release of EDK II includes that fix yet. The Hacker News checked the project's release tags on October 28 and found the newest, edk2-stable202608, predates it, and the advisory still lists the patched version as "Not patched currently." Microsoft's Project Mu has already pulled the fix into its release branches, and ...