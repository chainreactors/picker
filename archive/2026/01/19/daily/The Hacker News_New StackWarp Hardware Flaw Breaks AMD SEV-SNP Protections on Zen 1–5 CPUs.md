---
title: New StackWarp Hardware Flaw Breaks AMD SEV-SNP Protections on Zen 1–5 CPUs
url: https://thehackernews.com/2026/01/new-stackwarp-hardware-flaw-breaks-amd.html
source: The Hacker News
date: 2026-01-19
fetch_date: 2026-01-20T03:35:29.196876
---

# New StackWarp Hardware Flaw Breaks AMD SEV-SNP Protections on Zen 1–5 CPUs

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

# [New StackWarp Hardware Flaw Breaks AMD SEV-SNP Protections on Zen 1–5 CPUs](https://thehackernews.com/2026/01/new-stackwarp-hardware-flaw-breaks-amd.html)

**Ravie Lakshmanan**Jan 19, 2026Hardware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjvBKIwExgNlDEHvCub_5W4y4uhPhsKYtGX8oPC_DrwzV5Wl5i_QPN2oEgBoSHBAAbsurdEryR3O56kclGi5uN38Y50ftQUAPzj1Y-r0bAS3rQ_lqRm88M4umTl1e4bAiCAGArNy2v70l31w5IArnzj8rUqxCAL2Xd3C8j2POKMP8tr6iAhsynSMNPAZH6/s900-e365/stack.jpg)

A team of academics from the CISPA Helmholtz Center for Information Security in Germany has disclosed the details of a new hardware vulnerability affecting AMD processors.

The security flaw, codenamed **StackWarp**, can allow bad actors with privileged control over a host server to run malicious code within confidential virtual machines (CVMs), undermining the integrity guarantees provided by AMD Secure Encrypted Virtualization with Secure Nested Paging ([SEV-SNP](https://thehackernews.com/2025/10/rmpocalypse-single-8-byte-write.html)). It impacts AMD Zen 1 through Zen 5 processors.

"In the context of SEV-SNP, this flaw allows malicious VM [virtual machine] hosts to manipulate the guest VM's [stack pointer](https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29#Hardware_stack)," researchers Ruiyi Zhang, Tristan Hornetz, Daniel Weber, Fabian Thomas, and Michael Schwarz [said](https://stackwarpattack.com/). "This enables hijacking of both control and data flow, allowing an attacker to achieve remote code execution and privilege escalation inside a confidential VM."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

AMD, which is tracking the vulnerability as [CVE-2025-29943](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3027.html) (CVSS v4 score: 4.6), characterized it as a medium-severity, improper access control bug that could allow an admin-privileged attacker to alter the configuration of the CPU pipeline, causing the stack pointer to be corrupted inside an SEV-SNP guest.

The issue affects the following product lines -

* AMD EPYC 7003 Series Processors
* AMD EPYC 8004 Series Processors
* AMD EPYC 9004 Series Processors
* AMD EPYC 9005 Series Processors
* AMD EPYC Embedded 7003 Series Processors
* AMD EPYC Embedded 8004 Series Processors
* AMD EPYC Embedded 9004 Series Processors
* AMD EPYC Embedded 9005 Series Processors

While SEV is designed to encrypt the memory of protected VMs and is intended to isolate them from the underlying hypervisor, the new findings from CISPA show that the safeguard can be bypassed without reading the VM's plaintext memory by instead targeting a microarchitectural optimization called stack engine, responsible for accelerated stack operations.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDf44A5TcQy2eeckm9WvvIa7EyUvuOWzpMFb4PxccmYnmJP1jxvOJVGCYYZoHCcxXgIyhlwwJyAY8VkJZ0t0mVOuAEa75IxLyb7SvBBJKk7vF8Fv27Lk2_WnJem3fcNzrQudd1ZKFZLCzyLBdzmLcViOh23vKAsr24KHBxVieMBVTeMIu_T6KF90WjOvj5/s900-e365/StackWarp.jpg)

"The vulnerability can be exploited via a previously undocumented control bit on the hypervisor side," Zhang said in a statement shared with The Hacker News. "An attacker running a hyperthread in parallel with the target VM can use this to manipulate the position of the stack pointer inside the protected VM."

This, in turn, enables redirection of program flow or manipulation of sensitive data. The StackWarp attack can be used to expose secrets from SEV-secured environments and compromise VMs hosted on AMD-powered cloud environments. Specifically, it can be exploited to recover an RSA-2048 private key from a single faulty signature, effectively getting around OpenSSH password authentication and sudo's password prompt, and attain kernel-mode code execution in a VM.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The chipmaker released microcode updates for the vulnerability in July and October 2025, with AGESA patches for EPYC Embedded 8004 and 9004 Series Processors scheduled for release in April 2026.

The development builds upon a prior study from CISPA that detailed [CacheWarp](https://thehackernews.com/2023/11/cachewarp-attack-new-vulnerability-in.html) (CVE-2023-20592, CVSS v3 score:m 6.5), a software fault attack on AMD SEV-SNP, which permits attackers to hijack control flow, break into encrypted VMs, and perform privilege escalation inside the VM. It's worth noting that both are hardware architectural attacks.

"For operators of SEV-SNP hosts, there are concrete steps to take: First, check whether hyperthreading is enabled on the affected systems. If it is, plan a temporary disablement for CVMs that have particularly high integrity requirements," Zhang said. "At the same time, any available microcode and firmware updates from the hardware vendors should be installed. StackWarp is another example of how subtle microarchitectural effects can undermine system-level security guarantees."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[AMD](https://thehackernews.com/search/label/AMD)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Confidential Computing](https://thehackernews.com/search/label/Confidential%20Computing)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hardware security](https://thehackernews.com/search/label/hardware%20security)[Secure Encrypted Virtualization](https://thehackernews.com/search/label/Secure%20Encryp...