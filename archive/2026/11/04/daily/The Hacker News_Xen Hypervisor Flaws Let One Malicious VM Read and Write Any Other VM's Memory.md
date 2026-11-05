---
title: Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory
url: https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:12.922914
---

# Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory](https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html)

**Swati Khandelwal**Nov 04, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAVPXiuTBfhBnpwaZHMfSDWymKJrXbS88kOEO1Xuh5t11qAnwSKeFTHGQy6ZG9Sr2N-wRYrJg58x3lKFbybvU9p1a85lxaCHfBa61vO1DfjEhUi5Yzf6bQS1eN7Mu-s_sUwkE-JGc-UznJ1p0qfmwMDusXFzWawXKXMt6jj-vENxyQG12uAUDUe0p0gtg/s1700-nu-rw-lo-l85-e365/xen.jpg)

Two flaws in the Xen hypervisor allow a malicious guest virtual machine (VM) to read and write the memory of other VMs on the same host, including dom0.

Dom0 is the VM that, by default, has full permissions and manages the others. Patches are out, and there is no known mitigation, the Xen Project said in an [advisory](https://xenbits.xen.org/xsa/advisory-523.html) on November 3.

All Xen versions from 4.6 onward are vulnerable, while 4.5 and earlier are not. The flaws are tracked as **CVE-2026-102703** and **CVE-2026-102704**, under Xen advisory XSA-523.

The Xen Project credited AI company **Anthropic** with finding the flaws using its Claude model. Stephan Lipp of Ada Logics then validated the finding, and the CodeAnt AI Security Research Team later independently reported the same issue.

The flaws are in grant copy, the operation Xen uses to copy data between VMs. Each VM tells Xen which of its memory pages other VMs may use, and Xen checks those permissions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

To save time on a batch of copies within the same memory page, Xen reuses checks it has already made. In some cases, it did not check again when it should have. That mistake is what lets a malicious guest read and write memory it does not own.

XCP-ng, an open-source virtualization platform built around Xen, said in its [update notes](https://xcp-ng.org/blog/2026/11/03/november-2026-security-and-maintenance-updates-1-for-xcp-ng-8-3-lts/) that "a single compromised guest can break out of its isolation and take over the whole host."

Xen's advisory does not mention any attacks that exploit the flaws or specify what access within the VM an attacker needs.

Qubes OS is a security-focused desktop operating system that keeps software in separate Xen-based compartments called qubes. A [bulletin](https://www.qubes-os.org/news/2026/11/03/qsb-121/) said that every supported release and configuration is affected. Its fix is for Qubes 4.3, the [only release it still supports](https://doc.qubes-os.org/en/latest/user/downloading-installing-upgrading/supported-releases.html).

Because every Xen version from 4.6 on is vulnerable, other products built on those versions are affected until their makers add the XSA-523 patches. As of November 4, Debian's [security tracker](https://security-tracker.debian.org/tracker/CVE-2026-102703) listed the xen package in its bookworm, trixie, and forky releases as vulnerable, and in sid as fixed.

### Fixes and Restarts by Platform

These are the fixes published so far:

* **Xen source:** the advisory has patches for xen-unstable to Xen 4.19.x, and for Xen 4.18.x to 4.17.x.
* **Xen 4.6 to 4.16:** the advisory has no patch for these versions. Xen 4.16's [security support ended](https://github.com/xen-project/xen/blob/stable-4.16/SUPPORT.md) on December 2, 2024.
* **XCP-ng 8.3:** xen-4.17.7-4.2.xcpng8.3, released November 3. Hosts must be rebooted. Vates, which backs XCP-ng, [rates the impact as Critical](https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-055/).
* **Qubes OS 4.3:** Xen packages 4.19.6-3 in dom0. Dom0 must be restarted, and Anti Evil Maid users must reseal their secret passphrase because the new Xen binaries change PCR18 and PCR19.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Qubes told users on November 3 to keep [installing updates](https://doc.qubes-os.org/en/latest/user/how-to-guides/how-to-update.html) as normal. The fixed packages were then in its security-testing repository, due to move to the stable one over the next two weeks after community testing.

XSA-523 is separate from [XSA-500](https://xenbits.xenproject.org/xsa/advisory-500.txt), an earlier grant copy flaw that Xen disclosed on July 28, and it has its own patches.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [linux](https://thehackernews.com/search/label/linux), [Virtualization Security](https://thehackernews.com/search/label/Virtualization%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organization...