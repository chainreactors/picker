---
title: New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs
url: https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html
source: The Hacker News
date: 2026-11-13
fetch_date: 2026-11-14T08:21:56.274756
---

# New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs](https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html)

**Swati Khandelwal**Nov 13, 2026Vulnerability / Hardware Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi28SrA-dW0l0kreAg1vMHHOgBRMM7lzxv5qg2FT2HzRxReJ96pxZP4Fjpm15fYWDDgWpbBI8iC119aE37t_kmQ4guoA70NUlJsdiA4hFvTg8fflx9fsKqUsGuoB-S9VS5pPd38EBVYRGmvKIT5EylE3IwEK8bBCp5CkLrdTwhbyUA2xWN_0iOynP33yE8/s1700-nu-rw-lo-l85-e365/amd-flaws.jpg)

Two attacks made public this week allow a malicious host to read data inside AMD SEV-SNP-protected virtual machines (VMs), which are built to keep the server's operator out.

One of them, **Mior**, can also modify a VM's memory and fake the signed report confirming which software it runs. Both need control of the server's hypervisor, and Mior also needs control of the server's BIOS. Researchers showed both in lab tests on AMD EPYC server processors.

AMD, which makes the processors, lists SEV firmware for Mior and microcode for **Skyfall**, both dated August 12. It plans to give server makers platform firmware in November for Skyfall and in December for Mior, and fixes for embedded chips later. Customers are told to get the BIOS update from their server maker.

SEV-SNP brings confidential computing to AMD EPYC server processors. It uses hardware-enforced memory encryption and access control to protect a VM, even from the host's hypervisor.

The ETH Zurich team behind Mior attacked SEV-SNP while it was starting up. During start-up, a security co-processor on the chip, the Platform Security Processor (PSP), fills in a table called the Reverse Map Table (RMP). The RMP records who owns each page of memory and what they may do with it.

The team redirected the PSP's writes to the memory of a graphics card it controlled, instead of to main memory. The team used a card because it believes the PSP reads the values back to check them, and the card could return them. Start-up then finished without errors, but part of the real RMP, including the entry that protects the table itself, stayed uninitialized.

That let the hypervisor rewrite the RMP's protections. The team then enabled debugging on a confidential VM that had it disabled and used the PSP's own debug commands to read and write the VM's memory. This worked in all 1,000 attempts across both test runs.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

SEV-SNP also measures a VM's software image when the VM starts, and the PSP signs attestation reports that include this measurement. In a second test, the team copied a harmless VM's measurement into a malicious VM, so the malicious VM's attestation reports described the harmless image instead.

The attack needs control of the hypervisor and the BIOS (also called UEFI), plus a PCIe device such as a graphics card, the [Mior paper](https://xca-attacks.github.io/mior/mior_ccs26.pdf) says. For the tests, the team modified the BIOS to leave the chip's memory-routing settings unlocked.

"We operate in AMD’s threat model defined for SEV-SNP. AMD explicitly distrusts the UEFI, thus an attacker can modify the UEFI," the researchers say.

Ordinary VMs already trust their host and its firmware, so Mior gives an attacker nothing new against them, the team says.

The team ran Mior on one EPYC 9135, a Zen 5 chip. It considers Zen 3 and Zen 4 chips potentially affected but did not test them because it had no setup that allowed it to change their BIOS.

The debugging and attestation tests both worked with ciphertext hiding turned on. That optional SEV-SNP feature stops the hypervisor from even reading encrypted VM memory.

Two earlier attacks by some of the same researchers, the [Fabricked attack](https://xca-attacks.github.io/fabricked/) and the [RMPocalypse attack](https://thehackernews.com/2025/10/rmpocalypse-single-8-byte-write.html), also corrupted the RMP as SEV-SNP started up. Mior is a separate flaw, unrelated to Fabricked and to the fix for it, the team says. It also worked on older firmware from before that fix.

Skyfall comes from a team at ETH Zurich and Google. It builds on [Transient Scheduler Attacks](https://thehackernews.com/2025/07/amd-warns-of-new-transient-scheduler.html) (TSA), a group of flaws in AMD processors that can leak data through instruction timing. TSA was first disclosed on July 8, 2025.

The team found that when a hypervisor intentionally causes a VM to fail to start, the processor has already cached part of the VM's saved state. That data is left behind without the usual cleanup, and the hypervisor can read it through TSA.

This way, the team recovered a VM's saved register values and a disk-encryption key from a test VM. For the key, it changed the VM's kernel to pause at the moment the key sat in registers. In a real attack, the team says, a hypervisor can instead use a technique called SEV-Step to step through the VM until the key reaches the registers.

Skyfall can also read VM memory, but only three fixed cache lines in a page it targets, at offsets 0x0c0, 0x380 and 0x3c0. The rest of the page stays out of reach.

The attack needs a malicious host or hypervisor, but no tampering with the hardware. The team tested it on an EPYC 7313, a Zen 3 chip, and on EPYC 9124 and 9334 chips, which are Zen 4. It did not show the leak on Zen 5 chips.

Beyond VMs, the Skyfall team read decrypted microcode updates on all three test chips. It also recovered register values stored in System Management Mode (SMM) memory, which even the operating system kernel normally cannot read. Both of these attacks need privileged software on the machine.

The program committee of the IEEE Symposium on Security and Privacy, which accepted the [Skyfall paper](https://skyfall-attack.github.io/assets/skyfall.pdf), said it overlooks what a realistic attack on VMs would need. That includes a processor core free of other activity, fa...