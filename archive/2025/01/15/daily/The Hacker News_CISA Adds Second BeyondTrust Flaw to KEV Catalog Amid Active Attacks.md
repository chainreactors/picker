---
title: CISA Adds Second BeyondTrust Flaw to KEV Catalog Amid Active Attacks
url: https://thehackernews.com/2025/01/cisa-adds-new-beyondtrust-flaw-to-kev.html
source: The Hacker News
date: 2025-01-15
fetch_date: 2025-10-06T20:13:43.548235
---

# CISA Adds Second BeyondTrust Flaw to KEV Catalog Amid Active Attacks

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

# [CISA Adds Second BeyondTrust Flaw to KEV Catalog Amid Active Attacks](https://thehackernews.com/2025/01/cisa-adds-new-beyondtrust-flaw-to-kev.html)

**Jan 14, 2025**Ravie LakshmananVulnerability / Cybersecurity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigevA6xcgwq2RWsDUiDFhSFDkcBJagWoFXSfCyloGKHKxEGDfCwh8uBTIamDtjfjmS06E7oTCyC-h8jVKBf-5PKMw-5PiFm8bMr4IoJAjT2TJuteFTtMFwOBD5klUj1dIjT8wpOhDLeiUWflsW8XBMhxoIHM8j4FUWXMGIwKKwrxVpzNOOWDXntN_5Jj6d/s790-rw-e365/cisa.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a second security flaw impacting BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) products to the Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, citing evidence of active exploitation in the wild.

The vulnerability in question is [CVE-2024-12686](https://thehackernews.com/2024/12/cisa-adds-critical-flaw-in-beyondtrust.html) (CVSS score: 6.6), a medium-severity bug that could allow an attacker with existing administrative privileges to inject commands and run as a site user.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) contain an OS command injection vulnerability that can be exploited by an attacker with existing administrative privileges to upload a malicious file," CISA said.

"Successful exploitation of this vulnerability can allow a remote attacker to execute underlying operating system commands within the context of the site user."

The addition of CVE-2024-12686 to the KEV catalog comes nearly a month after it added another critical security flaw impacting the same product ([CVE-2024-12356](https://thehackernews.com/2024/12/cisa-adds-critical-flaw-in-beyondtrust.html), CVSS score: 9.8) that could also lead to the execution of arbitrary commands.

BeyondTrust said both vulnerabilities were discovered as part of its investigation into a cyber incident in early December 2024 that involved malicious actors leveraging a compromised Remote Support SaaS API key to breach some of the instances, and reset passwords for local application accounts.

Although the API key has since been revoked, the exact manner in which the key was compromised remains unknown as yet. It's suspected that the threat actors exploited the two flaws as zero-days to break into BeyondTrust systems.

Earlier this month, the U.S. Treasury Department [revealed](https://thehackernews.com/2025/01/cisa-no-wider-federal-impact-from.html) its network was breached using the compromised API key in what it said was a "major cybersecurity incident." The hack has been pinned on a Chinese state-sponsored group called [Silk Typhoon](https://thehackernews.com/2025/01/reddelta-deploys-plugx-malware-to.html) (aka Hafnium).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The threat actors are believed to have specifically targeted the Treasury's Office of Foreign Assets Control (OFAC), Office of Financial Research, and the Committee on Foreign Investment in the United States (CFIUS), according to multiple reports from [the Washington Post](https://www.washingtonpost.com/national-security/2025/01/01/treasury-hack-china/) and [CNN](https://edition.cnn.com/2025/01/10/politics/chinese-hackers-breach-committee-on-foreign-investment-in-the-us/).

Also added to the KEV catalog is a now-patched critical security vulnerability affecting Qlik Sense (CVE-2023-48365, CVSS score: 9.9) that allows an attacker to escalate privileges and execute HTTP requests on the backend server hosting the software.

It's worth noting that the security flaw has been actively exploited in the past by the [Cactus ransomware](https://thehackernews.com/2023/11/cactus-ransomware-exploits-qlik-sense.html) group. Federal agencies are required to apply the necessary patches by February 3, 2024, to secure their networks against active threats.

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

[API Breach](https://thehackernews.com/search/label/API%20Breach)[BeyondTrust](https://thehackernews.com/search/label/BeyondTrust)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Federal Security](https://thehackernews.com/search/label/Federal%20Security)[ransomware](https://thehackernews.com/search/label/ransomware)[Treasury Department](https://thehackernews.com/search/label/Treasury%20Department)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the ...