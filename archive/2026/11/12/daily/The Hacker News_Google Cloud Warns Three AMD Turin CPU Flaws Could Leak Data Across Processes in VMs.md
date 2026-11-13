---
title: Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes in VMs
url: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:45.388647
---

# Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes in VMs

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

# [Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes in VMs](https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html)

**Swati Khandelwal**Nov 12, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikEkIc_eg4_tE5XE6CQrLFl74Gk0QwxcqaGXBnDAlitVIbzreq8faf57QtAqFh8rEn7HgTJzvGUZl2yNBhWVKOKo9KqnJHfduQfoT_HqUTlKhE-FzshzDrpIskiMQ3_Lz2hImNMbt9VdCj0O725_WyZsDXDB91phFceXh6Y_qzHgv1nJPMNjv8a7AU52c/s1700-nu-rw-lo-l85-e365/amd.jpg)

Google Cloud VMs on AMD Turin chips need a guest OS patch and a stop-and-start to protect against three CPU side-channel flaws, Google said this week.

The company has already applied mitigations against attacks between VMs, and between VMs and the host. Inside a VM, the flaws may let an attacker with code on the same processor core infer data from other processes or the kernel.

The affected machine series are C4D, N4D, H4D, Z4D,, and G4, including bare-metal instances of C4D and Z4D. Turin is the code name for fifth-generation AMD EPYC processors.

All three flaws are Transient Scheduler Attacks (TSA). Two of them, TSA-SQ (CVE-2024-36350) and TSA-L1 (CVE-2024-36357), were first disclosed on July 8, 2025, for earlier EPYC processors.

AMD now says its Zen 5 processors, which include Turin, are "impacted differently from previously characterized AMD processors." The third flaw, CVE-2026-0004, is new. It may let an attacker who can run code on a system infer data in the processor's L1 data cache.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The Xen Project, which maintains the Xen hypervisor, calls the new flaw TSA-Fill. It also says an earlier statement has been corrected: "AMD had previously said that Zen5 CPUs were not vulnerable to TSA-SQ and TSA-L1."

Google rates the issue Medium. AMD classifies all three as local attacks with high attack complexity that require only low privileges, according to its [Zen 5 bulletin](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7073.html) and [CVE-2026-0004 advisory](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3055.html).

As of today, none of the three is in the KEV catalog of exploited flaws kept by the U.S. Cybersecurity and Infrastructure Security Agency. Neither company reports any exploitation in its bulletins.

### What Google Cloud Customers Need to Do

Google's [security bulletin](https://docs.cloud.google.com/support/bulletins#gcp-2026-081) gives these steps for each service:

* **VMs:** Install your OS vendor's fix when it ships. Starting this week, the company will update the CPU information that VMs report, so a patched guest kernel can turn on its mitigations. After that update reaches a VM, stop and start it. As the company puts it: "Rebooting the guest OS isn't enough."
* **Bare metal instances:** If you run your own OS or hypervisor on a C4D or Z4D bare metal instance, apply your vendor's fixes when they are available.
* **Hypervisors inside a VM:** The same CPU information update applies, so patched guest kernels can turn on their mitigations. Stop and start the VM once the update arrives.
* **GKE:** Updated node images for Turin-based bare metal instances will be made available, and upgrading nodes picks up the CPU information update. As of today, the bulletin does not yet list them as available.
* **Cloud Run:** No action is needed.

Customers on older Rome, Milan, and Genoa processors got the same stop-and-start instruction in an [earlier bulletin](https://docs.cloud.google.com/support/bulletins#gcp-2025-037) at the time of the [original disclosure](https://thehackernews.com/2025/07/amd-warns-of-new-transient-scheduler.html) on July 8, 2025.

The company lists nothing to do in the meantime for VMs whose OS vendor has not yet shipped a fix. It also does not say how to tell when the CPU information update has reached a VM.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

A [kernel commit](https://git.kernel.org/linus/cf27412f19c9cc5909b9107cd1b3f4ab7608e362) that mitigates TSA on Zen 5, including the new variant, is in the Linux kernel source tree. As of today, Debian has fixed CVE-2026-0004 in its Linux kernel only in its unstable branch. Its [security tracker](https://security-tracker.debian.org/tracker/CVE-2026-0004) still lists the kernels in bookworm, trixie, and forky as vulnerable.

For Turin servers on your own hardware, AMD says both platform firmware and OS updates are needed to mitigate the flaws fully. The mitigation may affect performance, and administrators should weigh the risk to their own workloads, according to its [technical guidance](https://www.amd.com/content/dam/amd/en/documents/resources/bulletin/technical-guidance-for-mitigating-transient-scheduler-attacks.pdf).

The Xen Project has published hypervisor patches in its [Xen advisory](https://xenbits.xen.org/xsa/advisory-525.html). It says microcode for all TSA flaws on Zen 5 has been in linux-firmware since September 23.

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

[Cloud security](https://thehackernew...