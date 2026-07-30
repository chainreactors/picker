---
title: Three Critical VMware Flaws Allow Auth Bypass, Code Execution, and VM Escape
url: https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:42.637983
---

# Three Critical VMware Flaws Allow Auth Bypass, Code Execution, and VM Escape

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Three Critical VMware Flaws Allow Auth Bypass, Code Execution, and VM Escape](https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html)

**Ravie Lakshmanan**Jul 29, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLKz0u1mJIVvPAxiFFqsvkMVXxyXqS_paYhbtTRFLoIWyl5Q_FwIrJjruxEYH0LAdzJm38P48m_T_24ycKfjPs2bg6FUoy2IWVUxH7SpNtiSJuExOy3dDEAWprGwkvhY5005OPyFUzl2qJzAztAckgZNLVzqlp34s9HtQ3wrvq6lDCcXgYwfOXKF08wtdp/s1700-e365/vmware.jpg)

Broadcom has [released](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) security updates to address multiple security flaws impacting VMware ESX, vCenter, Workstation, and Fusion, three of which have been designated as critical in severity.

The first of the three critical-rated flaws is **CVE-2026-59309** (CVSS score: 9.8), which has been described as an authentication bypass in VMware vCenter.

"A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system," Broadcom said.

The second critical flaw is a directory-traversal vulnerability in vCenter (**CVE-2026-59310**, CVSS score: 9.8) that a malicious actor with network access can exploit to execute arbitrary code. Both vulnerabilities have been addressed in the versions below -

* VMware Cloud Foundation, VMware vSphere Foundation versions 9.1.x.x (Fixed in 9.1.0.0300)
* VMware Cloud Foundation, VMware vSphere Foundation versions 9.0.x.x (Fixed in 9.0.2.0100)
* VMware vCenter version 8.0 (Fixed in 8.0 U3k)
* VMware Cloud Foundation versions 5.x (Async patch to 8.0 U3k)

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3-o9La7DYm6jz5qcavVBLvRXUoQLqwrMmrvB529PbUxdg7TJZS3BMjVi4D7vd6V9vlSf_OX48mmXQWPgah_SPITaGgg4AP9YxB2AH-63YeWU39N3DXadwc_2zjIpTwCt0iyTdPZIM-KzKhDf_JDPWDGu3IbYfi1ilQE8Ly29HiKYagSIur-il4k7MMNv8/s728-e100/sygnia-d-3.png)](https://thn.news/sygnia-webinar)

Also patched by Broadcom are three other flaws -

* **CVE-2026-47876** (CVSS score: 9.3) - An out-of-bounds write vulnerability in the VMXNET3 virtual network adapter of VMware ESX that a malicious actor with local administrative privileges on a virtual machine can exploit to execute code on the host. (Fixed in VMware Cloud Foundation and VMware vSphere Foundation versions ESXi-9.1.0.0200-25557999 and ESXi-9.0.2.0100-25595025, and VMware ESX ESXi80U3k-25595708)
* **CVE-2026-41703** (CVSS score: 7.6) - An out-of-bounds read vulnerability in VMware ESX that a malicious actor with VM deployment privileges could trigger, potentially leading to information disclosure or a denial-of-service (DoS) condition. On VMware Workstation and Fusion, the impact is limited to information disclosure. (Fixed in VMware Cloud Foundation and VMware vSphere Foundation versions ESXi-9.1.0.0-25370933 and ESXi-9.0.2.0100-25595025, VMware ESX ESXi80U3i-25205845, VMware Workstation 26H1, VMware Fusion 26H1, and VMware Cloud Foundation 5.2.3)
* **CVE-2026-41709** (CVSS score: 2.7) - An insufficient logging vulnerability in VMware ESX that a malicious administrator can exploit to perform certain operations without them being logged. (Fixed in VMware Cloud Foundation and VMware vSphere Foundation versions ESXi-9.1.0.0-25370933 and ESXi-9.0.2.0100-25595025, and VMware ESX ESXi80U3j-25429389)

Broadcom noted that it has found no evidence to suggest any of these issues have been exploited in the wild. The technology giant also characterized CVE-2026-47876 as a virtual machine escape.

"An attacker who already holds local administrative privileges inside a virtual machine that uses the VMXNET3 virtual network adapter may execute code on the ESX host," it [said](https://github.com/vmware/vcf-security-and-compliance-guidelines/tree/main/security-advisories/vmsa-2026-0006).

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

[Authentication Security](https://thehackernews.com/search/label/Authentication%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [denial of service](https://thehackernews.com/search/label/denial%20of%20service), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Virtualization Security](https://thehackernews.com/search/label/Virtualization%20Security), [VMware](https://thehackernews.com/search/label/VMware), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](data:image/svg+xml;base64... "New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit")

New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](https://thehackernews.com/2026/07/new-bit2watt-attack-could-let-cloud.html)

[![Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](data:image/svg+xml;base64... "Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host...