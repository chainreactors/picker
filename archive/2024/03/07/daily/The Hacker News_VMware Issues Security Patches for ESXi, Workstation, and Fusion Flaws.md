---
title: VMware Issues Security Patches for ESXi, Workstation, and Fusion Flaws
url: https://thehackernews.com/2024/03/vmware-issues-security-patches-for-esxi.html
source: The Hacker News
date: 2024-03-07
fetch_date: 2025-10-06T17:11:44.585006
---

# VMware Issues Security Patches for ESXi, Workstation, and Fusion Flaws

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [VMware Issues Security Patches for ESXi, Workstation, and Fusion Flaws](https://thehackernews.com/2024/03/vmware-issues-security-patches-for-esxi.html)

**Mar 06, 2024**Ravie LakshmananSoftware Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhvc4vGa2IyZoEewlN5F2HLawFs-FiMfHbW4QfyADIIlt1iZUhIxuVnmgW6OYvwtnA8RRwFKws709zm8x4QGA3Gjc61Xg_tf94C7Z17P13EC8cbOs76bcIf9a5b7SMFV8G7sd8QGfCevWnV_Q9Kg2-lbEV_iKtrOBXnxT2bvyaoQSZsfA8u0fYqJ3e/s728-rw-e30/vmware.jpg)

VMware has released patches to address four security flaws impacting ESXi, Workstation, and Fusion, including two critical flaws that could lead to code execution.

Tracked as **CVE-2024-22252 and CVE-2024-22253**, the vulnerabilities have been described as use-after-free bugs in the XHCI USB controller. They carry a CVSS score of 9.3 for Workstation and Fusion, and 8.4 for ESXi systems.

"A malicious actor with local administrative privileges on a virtual machine may exploit this issue to execute code as the virtual machine's VMX process running on the host," the company [said](https://www.vmware.com/security/advisories/VMSA-2024-0006.html) in a new advisory.

"On ESXi, the exploitation is contained within the VMX sandbox whereas, on Workstation and Fusion, this may lead to code execution on the machine where Workstation or Fusion is installed."

Multiple security researchers associated with the Ant Group Light-Year Security Lab and QiAnXin have been credited with independently discovering and reporting CVE-2024-22252. Security researchers VictorV and Wei have been acknowledged for reporting CVE-2024-22253.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Also patched by the Broadcom-owned virtualization services provider are two other shortcomings -

* **CVE-2024-22254** (CVSS score: 7.9) - An out-of-bounds write vulnerability in ESXi that a malicious actor with privileges within the VMX process could exploit to trigger a sandbox escape.
* **CVE-2024-22255** (CVSS score: 7.1) - An information disclosure vulnerability in the UHCI USB controller that an attacker with administrative access to a virtual machine may exploit to leak memory from the vmx process.

The issues have been addressed in the following versions, including those that have reached end-of-life (EoL) due to the severity of these issues -

* ESXi 6.5 - [6.5U3v](https://docs.vmware.com/en/VMware-vSphere/6.5/rn/esxi650-202403001.html)
* ESXi 6.7 - [6.7U3u](https://docs.vmware.com/en/VMware-vSphere/6.7/rn/esxi670-202403001.html)
* ESXi 7.0 - [ESXi70U3p-23307199](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-70u3p-release-notes/index.html)
* ESXi 8.0 - [ESXi80U2sb-23305545](https://docs.vmware.com/en/VMware-vSphere/8.0/rn/vsphere-esxi-80u2b-release-notes/index.html) and [ESXi80U1d-23299997](https://docs.vmware.com/en/VMware-vSphere/8.0/rn/vsphere-esxi-80u1d-release-notes/index.html)
* VMware Cloud Foundation (VCF) 3.x
* Workstation 17.x - 17.5.1
* Fusion 13.x (macOS) - 13.5.1

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As a temporary workaround until a patch can be deployed, customers have been asked to remove all USB controllers from the virtual machine.

"In addition, virtual/emulated USB devices, such as VMware virtual USB stick or dongle, will not be available for use by the virtual machine," the company [said](https://kb.vmware.com/s/article/96682). "In contrast, the default keyboard/mouse as input devices are not affected as they are, by default, not connected through USB protocol but have a driver that does software device emulation in the guest OS."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[security update](https://thehackernews.com/search/label/security%20update)[vmware](https://thehackernews.com/search/label/vmware)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJack...