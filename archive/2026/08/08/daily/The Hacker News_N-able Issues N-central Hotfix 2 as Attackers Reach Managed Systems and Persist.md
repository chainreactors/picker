---
title: N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist
url: https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html
source: The Hacker News
date: 2026-08-08
fetch_date: 2026-08-09T03:29:33.728693
---

# N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist

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

![cybersecurity](data:image/svg+xml;base64...)

# [N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist](https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html)

**Ravie Lakshmanan**Aug 08, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsaNpVaG83aDE1lJwcNllVSeS-ebafbbt4FgaKHH1_4dt1i4qvCtw-dYVrE_MiWf2GZ5vyGPhyphenhyphenCieChBz2IChMJew0I1Ze2HEYJpB-j3rB2VnfNrzbFpPDD7VFkWCkYBn2CJRLpOBIKNaeKPXlVPHpz7-1Wx9go7IfyUKSVNliDO644rNsoMmAk5a3Qf_W/s1700-e365/nc.jpg)

N-able has [released](https://www.n-able.com/blog/n-central-security-update-august-6-2026) a fresh round of hotfixes for N‑central as part of its investigation into ongoing exploitation of a recently disclosed security flaw in the Remote Monitoring and Management (RMM) product.

"We are proactively expanding protections in response to ongoing monitoring of threat actors as they evolve their attack techniques," the company said.

"This is not a duplicate of our previous communication. [Hotfix 2](https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/) is required, even if you already applied the earlier hotfix. Hotfix 2 supersedes Hotfix 1 with additional hardening measures to further protect you and your customers."

The disclosure comes as N-able acknowledged that it detected unusual activity within a customer's environment on July 31, 2026, leading to the discovery of unknown threat actors exploiting a then-zero-day flaw in the N‑central server (CVE-2026-18577, CVSS score: 8.2). It impacts all versions prior to 2026.3.1.7.

It's worth noting that CVE-2026-18577 relates to an incomplete fix for CVE-2026-18556 (CVSS score: 8.2). Both vulnerabilities, which allow authentication bypass and account takeover in susceptible versions, have been [flagged](https://thehackernews.com/2026/08/cisa-adds-exploited-n-able-n-central.html) as [actively exploited](https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html) by the U.S. Cybersecurity and Infrastructure Security Agency (CISA).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

In the attacks observed by N-able, the vulnerability allowed the attackers to obtain administrative access remotely and then leverage the Take Control feature to connect to systems within the N‑central managed environment. Upon gaining access to those devices, the threat actors registered a new service for a Cloudflare Tunnel, enabling persistence even after access to the N‑central server was revoked.

N-able has confirmed that a limited number of customers have been affected by the exploitation activity. Customers running an on-premise version are advised to update their instances to 026.3.1.10 immediately. The company has also shared an expanded set of IP addresses as indicators of compromise (IoCs) -

* 173.249.252[.]176
* 173.249.252[.]200
* 185.156.46[.]150
* 23.234.94[.]43
* 37.153.90[.]88
* 37.19.210[.]32
* 68.235.46[.]214
* 68.235.46[.]235
* 87.249.138[.]34
* 92.118.112[.]181

In addition, N-able has released a [custom service template](https://developer.n-able.com/n-central/recipes/cve-2026-18577-detection) that offers an automated way to check for known IoCs against Windows device endpoints in N‑central.

"A clean result should not be interpreted as a guarantee that your environment has not been impacted," it said. "Our investigation is ongoing and additional indicators may be identified over time. We strongly recommend this be used as one layer of your assessment, alongside a thorough review of your environment, logs, and account activity."

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

[account takeover](https://thehackernews.com/search/label/account%20takeover), [Authentication](https://thehackernews.com/search/label/Authentication), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Incident response](https://thehackernews.com/search/label/Incident%20response), [network security](https://thehackernews.com/search/label/network%20security), [Remote Access](https://thehackernews.com/search/label/Remote%20Access), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](data:image/svg+xml;base64... "New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit")

New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](https://thehackernews.com/2026/07/new-bit2watt-attack-could-let-cloud.html)

[![Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](data:image/svg+xml;base64... "Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs")

Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html)

[![Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC](data:image/svg+xml;base64... "Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC")

Critical SharePoint RCE CVE-2026-50522 Under Active ...