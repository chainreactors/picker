---
title: Critical VMware vCenter Zero-Day Flaw Lets Network Attackers Bypass Authentication
url: https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html
source: The Hacker News
date: 2026-11-19
fetch_date: 2026-11-20T09:23:13.086866
---

# Critical VMware vCenter Zero-Day Flaw Lets Network Attackers Bypass Authentication

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Critical VMware vCenter Zero-Day Flaw Lets Network Attackers Bypass Authentication](https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html)

**Swati Khandelwal**Nov 19, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ5IDT81eb7KUE0LzwGJAzuAETft3pD5sOz2dJxnQin_-zR_hH8tDKFTsLNBNoe35KM4DhFJjP7K-0YwaMoVwz7xUhTiP2vKeNqmN3kenPgwflENu35qx-QlFj-rDFdyXx1HMz6ykegw6nlnPDXppYbotjoRj-ammlyUZ-Cr0JYLS5iyZXkJXkaIO5UAc/s1700-nu-rw-lo-l85-e365/vmware.jpg)

A critical flaw in **VMware vCenter** lets an attacker with network access bypass authentication and gain unauthorized access to the system, Broadcom, which owns VMware, said in an advisory published today.

Fixed versions are out for all supported branches, and the company lists no workaround. vCenter is the central console for managing an organization's ESX hosts and virtual machines.

The vulnerability is tracked as **CVE-2026-123890** and is rated 9.8 on the CVSS scoring system. "VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service," the advisory says.

In an FAQ published with the advisory, the company says the issue "qualifies under ITIL methodologies as an emergency change," and urges organizations to consult their security staff immediately on timing.

The flaw was exploited as a zero-day more than two months before the patch, Google's threat intelligence team said in a [technical analysis](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere) published November 20. A suspected China-nexus espionage actor tracked as Armory Castle used it in early September to gain administrator access to a vCenter server inside a network the group had already breached. Credit for reporting the bug goes to Google-owned Mandiant.

The bug is present in vCenter 8.0, 9.0, and 9.1, and in the vCenter builds that ship inside VMware Cloud Foundation, vSphere Foundation, and the Telco Cloud Platform and Telco Cloud Infrastructure products. That includes the older Cloud Foundation 5.x line. It is there whether or not Enhanced Linked Mode is in use.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Older versions are not cleared. The company no longer evaluates versions past end of support, and says vSphere 6.5 and 6.7 should be presumed affected. The same goes for vSphere 7.0, which left general support in October 2025, and whose customers can request a patch under an extended support contract.

None of the five flaws in the advisory lets code run on an ESX host from inside a virtual machine, and ESX itself is not affected, the [advisory FAQ](https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0009/README.md) says.

There is no fallback for systems that cannot be updated yet: asked whether a workaround exists, the FAQ answers "Not as listed by Broadcom," while noting that mitigations may still exist in an organization's own defenses.

The updates are cumulative and cannot be installed through vCenter Quick Patch. Virtual machines continue running while vCenter installs the update, though management access drops briefly, and some encryption operations against a Standard Key Provider become unavailable until vCenter is back online.

One warning applies to upgrades already in progress: installing vCenter 8.0 U3m or 9.0.2.0200 blocks a later upgrade to VMware Cloud Foundation 9.1.1, a conflict the FAQ calls a "Back-in-Time" issue. The options are to upgrade vCenter to 9.1.1 first and apply the security update there, or to wait briefly for VCF 9.1.2.

The bypass is the second critical authentication flaw in the VMware Directory Service this year. The [earlier vCenter flaws](https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html), patched on July 29, included CVE-2026-59309, another 9.8-rated bypass in the same component per the [July advisory](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017), alongside a directory-traversal bug, CVE-2026-59310.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Attacks on that traversal flaw began five days after its disclosure, German incident response firm QUIRSO assessed in August, linking them with moderate confidence to a suspected China-nexus actor.

The [August attacks](https://thehackernews.com/2026/08/suspected-china-nexus-actor-exploits.html) compromised an estimated 361 IP addresses in 47 countries and deployed Babuk-derived ransomware on ESXi hosts.

The advisory also fixes four lower-severity flaws, rated 6.7 to 8.1: a SQL injection (CVE-2026-123891) and a command injection (CVE-2026-123892) in SDDC Manager, a privilege escalation to root on the SDDC Manager appliance (CVE-2026-123893), and a SAML token signature bypass in VMware Tools for Windows (CVE-2026-123894), exploitable only where Guest Alias mapping is configured. Each needs an authenticated or already privileged actor, and the last one stays inside the guest virtual machine.

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
[**Sha...