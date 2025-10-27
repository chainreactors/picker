---
title: High-Severity Flaw Reported in Critical System Used by Oil and Gas Companies
url: https://thehackernews.com/2022/11/high-severity-flaw-reported-in-critical.html
source: The Hacker News
date: 2022-11-11
fetch_date: 2025-10-03T22:26:27.187608
---

# High-Severity Flaw Reported in Critical System Used by Oil and Gas Companies

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

# [High-Severity Flaw Reported in Critical System Used by Oil and Gas Companies](https://thehackernews.com/2022/11/high-severity-flaw-reported-in-critical.html)

**Nov 10, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiY8QKJVg6JY5KaI1X5f9DndXxpUqAcerX3w2Jv3B8m6YV4xyBx2-pmrcyFc6f6CBooa4j8yuwiZm25g118mQjKnLr3JPeauMxNrskRwCw3r9iCzziMf8FyZpk5a4RtYxj4lxfdeWogFKWAMgdtR9WLin01pwsuIFsyX7h-2tciAvHwmQNfBVC1rcoK/s790-rw-e365/oil-gas.jpg)

Cybersecurity researchers have disclosed details of a new vulnerability in a system used across oil and gas organizations that could be exploited by an attacker to inject and execute arbitrary code.

The high-severity issue, tracked as [CVE-2022-0902](https://claroty.com/team82/disclosure-dashboard/cve-2022-0902) (CVSS score: 8.1), is a path-traversal vulnerability in ABB Totalflow [flow computers and remote controllers](https://new.abb.com/products/measurement-products#Products=category0/flow_computers__remote_controllers%7Clevel/0%7Cpage/1).

"Attackers can exploit this flaw to gain root access on an ABB flow computer, read and write files, and remotely execute code," industrial security company Claroty [said](https://claroty.com/team82/research/an-oil-and-gas-weak-spot-flow-computers) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

ABB, a Swedish-Swiss industrial automation firm, has since released [firmware updates](https://global.abb/group/en/technology/cyber-security/alerts-and-notifications) as of July 14, 2022, following responsible disclosure.

Flow computers are special-purpose electronic instruments used by petrochemical manufacturers to interpret data from flow meters and calculate and record the volume of substances such as natural gas, crude oils, and other hydrocarbon fluids at a specific point in time.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicwZeVvlKHQdOcbaR0Z3mZCdRWuX1ab24nFJ_Fbdlg3F7P-Ckv7undW9h4-FWAT_dwONNekPddEISQtBY7IeVXfRihCerhhE7Z4LpVTGAyMtp4EhUCO8LVZUw_LW8ibk3YC6_ATCfySzMHkfcaQpMqnON4Zq4904-whpkI3AdrWPeUIh9uCsCn9iZ9/s790-rw-e365/flaw.jpg)

These electronic measurements are critical not only when it comes to process safety, but are also used as inputs when bulk liquid or gas products change hands between parties, making it imperative that the flow readings are accurately captured.

In a nutshell, the vulnerability identified by Claroty is a path traversal flaw that exists in ABB's implementation of its proprietary Totalflow TCP protocol, which is utilized to remotely configure the computers.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The issue, specifically, concerns a feature that allows for importing and exporting the configuration files, enabling an attacker to leverage an authentication bypass issue to get past the security passcode barrier and upload arbitrary files.

By taking advantage of the shortcoming, a remote malicious actor could seize control of the devices and hamper their ability to properly record oil and gas flow rates.

"A successful exploit of this issue could impede a company's ability to bill customers, forcing a disruption of services, similar to the [consequences](https://thehackernews.com/2022/05/us-proposes-1-million-fine-on-colonial.html) suffered by Colonial Pipeline following its 2021 ransomware attack," Claroty researcher Vera Mens said.

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

[path traversal attack](https://thehackernews.com/search/label/path%20traversal%20attack)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Atta...