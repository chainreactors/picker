---
title: Critical Flaws in Traccar GPS System Expose Users to Remote Attacks
url: https://thehackernews.com/2024/08/critical-flaws-in-traccar-gps-system.html
source: The Hacker News
date: 2024-08-27
fetch_date: 2025-10-06T18:08:43.611826
---

# Critical Flaws in Traccar GPS System Expose Users to Remote Attacks

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

# [Critical Flaws in Traccar GPS System Expose Users to Remote Attacks](https://thehackernews.com/2024/08/critical-flaws-in-traccar-gps-system.html)

**Aug 26, 2024**Ravie LakshmananSoftware Security / Vulnerability

[![Traccar GPS System](data:image/png;base64... "Traccar GPS System")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsEAueQ83P-n8Tb9-uc6BdnNm1XMf_BNle-Wwl-btR74oHrOPZ7m-WmhcLE3kuBPtsZyBIlNwk6xYyDdu5ZQXuM4PEAB7s9APUiqSqHByjestjSPfM4VtiNp-agkgVCLMmp7nffQTPNS00KtRsAIVtRrWovaKq97IwiwMZ7tj6RqSQ7Smr2O6nrVXJghNq/s790-rw-e365/gps.png)

Two security vulnerabilities have been disclosed in the open-source [Traccar](https://github.com/traccar/traccar) GPS tracking system that could be potentially exploited by unauthenticated attackers to achieve remote code execution under certain circumstances.

Both the vulnerabilities are path traversal flaws and could be weaponized if guest registration is enabled, which is the default configuration for Traccar 5, Horizon3.ai researcher Naveen Sunkavally said.

A brief description of the shortcomings is as follows -

* **[CVE-2024-24809](https://github.com/traccar/traccar/security/advisories/GHSA-vhrw-72f6-gwp5)** (CVSS score: 8.5) - Path Traversal: 'dir/../../filename' and unrestricted upload of file with dangerous type
* **[CVE-2024-31214](https://github.com/traccar/traccar/security/advisories/GHSA-3gxq-f2qj-c8v9)** (CVSS score: 9.7) - Unrestricted file upload vulnerability in device image upload could lead to remote code execution

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The net result of CVE-2024-31214 and CVE-2024-24809 is that an attacker can place files with arbitrary content anywhere on the file system," Sunkavally [said](https://www.horizon3.ai/attack-research/disclosures/traccar-5-remote-code-execution-vulnerabilities/). "However an attacker only has partial control over the filename."

The issues have to do with how the program handles device image file uploads, effectively allowing an attacker to overwrite certain files on the file system and trigger code execution. This includes files matching the below naming format -

* device.ext, where the attacker can control ext, but there MUST be an extension
* blah", where the attacker can control blah but the filename must end with a double quote
* blah1";blah2=blah3, where the attacker can control blah1, blah2, and blah3, but the double quote semicolon sequence and equals symbol MUST be present

[![Traccar GPS System](data:image/png;base64... "Traccar GPS System")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkNGcpvAbROux3pBDoMUfqDGB2PJdbtwxYpgJQ93fYF1XlEkHmvsGTLwpJw5ZeoFqlUx5tQwUBLjqyZrS9cVtkpMwK5a_DabBshtxUKnWdS-Zl0snB8PpcZ4vRD6Rr8dEnOX5s3CXPe5wYrfV8ObcVgwCH7iOlvYaDvTIiJxpzC-Es_Nkllbjd7iOD4HfW/s790-rw-e365/code.png)

In a hypothetical proof-of-concept (PoC) devised by Horizon3.ai, an adversary can exploit the path traversal in the Content-Type header to upload a crontab file and obtain a reverse shell on the attacker host.

This attack method, however, does not work on Debian/Ubuntu-based Linux systems due to file naming restrictions that bar crontab files from having periods or double quotes.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

An alternative mechanism entails taking advantage of Traccar being installed as a root-level user to drop a kernel module or [configuring an udev rule](https://thehackernews.com/2024/08/new-linux-malware-sedexp-hides-credit.html) to run an arbitrary command every time a hardware event is raised.

On susceptible Windows instances, remote code execution could also be achieved by placing a shortcut (LNK) file named "device.lnk" in the C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp folder, which gets subsequently executed when any victim user logs into the Traccar host.

Traccar versions 5.1 to 5.12 are vulnerable to CVE-2024-31214 and CVE-2024-2809. The issues have been addressed with the release of Traccar 6 in April 2024 which turns off self-registration by default, thereby reducing the attack surface.

"If the registration setting is true, readOnly is false, and deviceReadonly is false, then an unauthenticated attacker can exploit these vulnerabilities," Sunkavally said. "These are the default settings for Traccar 5."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GPS Tracking](https://thehackernews.com/search/label/GPS%20Tracking)[Linux security](https://thehackernews.com/search/label/Linux%20security)[Path Traversal](https://thehackernews.com/search/label/Path%20Traversal)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert...