---
title: New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing
url: https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html
source: The Hacker News
date: 2026-09-14
fetch_date: 2026-09-15T07:03:15.332542
---

# New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing](https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html)

**Swati Khandelwal**Sep 14, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4IfzHWVZbbX-Jlw_WME4viVgnupLfVdkxzfZ0skzjQpB5I32f-nua5-Gt6UJGJ9-cwTyrHqaCxBFndtNkIFx_Tj9sf3LnxfrqlecJ0zh0N83i5YRdukZRTpTiUP-kVrkpF4gMJZN-tONZy7jjk2gqdq87ELsUHDlyjQDFCIX6Rioz3ljHItZ2IeLDqb-w/s1700-nu-rw-lo-l85-e365/DDRop.gif)

Researchers have disclosed a new hardware attack, called **DDRop**, that breaks the memory protection in Intel and AMD confidential computing by silently dropping writes to a server's memory, so the processor keeps reading old encrypted data as if it were current.

The attack requires an attacker who already controls the server's software and can briefly access the machine to insert a small circuit board, called an **interposer**, between the processor and a memory module.

The interposer costs under $200 to build. DDRop works against Intel TDX, Intel Scalable SGX, and AMD SEV-SNP, the hardware that cloud services use to keep customer data private while it is in use, even from the cloud provider.

Confidential computing keeps a server's memory encrypted, so that even someone with physical access to the machine sees only scrambled data. To cover the large amount of memory that a cloud server uses, though, these designs omit a guarantee called freshness. The processor can confirm that memory is encrypted, but not that it holds the latest written value, and that old encrypted data still decrypts correctly.

DDRop turns that gap into an attack. When the interposer drops a write, the earlier value stays in memory, and the processor reads it back as though the update had happened. The encryption engine detects nothing wrong.

DDRop is the first active interposer attack to work on the DDR5 memory in today's cloud servers, the researchers say, and the first to break the integrity of an up-to-date Intel TDX system rather than only read data from it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Earlier DDR5 interposer attacks, such as [TEE.fail](https://thehackernews.com/2025/10/new-teefail-side-channel-attack.html), were passive. They listened to the memory bus and had to slow it down to work with second-hand lab equipment. Active attacks that changed what the memory saw, such as [Battering RAM](https://thehackernews.com/2025/10/50-battering-ram-attack-breaks-intel.html), worked only on older DDR4, and DDR5's redesigned command format blocks the address-swapping trick they used. DDRop gets around that by dropping writes instead.

The interposer is a small board of switches that sits on the memory bus and runs at full DDR5 speed. To drop a write, it forces an error on the command bus and then cuts the wire the memory module uses to report that error, so the module quietly discards the command and the processor is never told.

[DDRop](https://ddropattack.eu/) is the work of researchers at KU Leuven, ETH Zurich, Durham University, and Google, and is due to be presented at the ACM CCS 2026 conference in November. The team says it is releasing the interposer's board designs, controller firmware, and attack code [on GitHub](https://github.com/ddropattack/ddrop), alongside [their research paper](https://ddropattack.eu/ddrop.pdf).

### Breaking Intel TDX

On Intel TDX, the researchers turned write-dropping into full control of a protected virtual machine. TDX keeps each virtual machine's page tables encrypted and under the control of trusted firmware.

When that firmware writes empty entries to set up a new page table, DDRop drops those writes, so the table instead keeps attacker-chosen data left in that memory beforehand. That lets an attacker's own virtual machine map its memory onto any physical address and read or change protected memory.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3-y-6t8lWqMpRHEzm1bvDJnuUgNvZIpWRT7Ic1YeMFuCYy-gHihg75WrDnDKEnu229FzYhIhfHvtTJk10FPvMD_gFLX1HyTkYh3mKXMI6jlWkDz6M1bI3B3GuTjYthyTpYCCetwQsW7MtEWVEiMLFq4aRvDDFK9Dxoa1wZYhJ3i7bPAza9a_VSbGsB5HX/s1700-nu-rw-lo-l85-e365/intel.jpg)

With that access, the researchers read a victim virtual machine's private memory and switched a victim machine into debug mode, which let them copy its memory in plaintext and then restore the original data so the victim showed no sign of tampering.

They also overwrote the launch measurement that a virtual machine uses to prove to a remote customer that it started in a known, trusted state. With that changed, a virtual machine the attacker controls could pass that check as if it were a trusted one.

Two of these results, reading a victim's memory and toggling debug mode, were shown only under TDX's default mode, called logical integrity. TDX's optional, stronger mode, called cryptographic integrity, would block them, the researchers say, because both involve changing data that belongs to another virtual machine.

Forging a machine's own attestation, they argue, would still work under the stronger mode, because that write happens inside the attacker's own virtual machine and under its own key, so the hardware still marks the data as valid. Cryptographic integrity does not add a freshness check either, so it cannot tell that old contents were reused. Their test system did not support the mode, so they could not confirm this.

On AMD SEV-SNP, the result is narrower. Dropping writes during AMD's page-relocation feature let the researchers copy the contents of one victim page into another, but the debug-mode and attestation-forgery attacks are specific to Intel TDX.

All three technologies encrypt memory without the freshness check DDRop exploits, so all three are affected. Intel's older Client SGX, used in some desktop and laptop chips, is not, because it uses a hardware inte...