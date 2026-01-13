---
title: n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens
url: https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html
source: The Hacker News
date: 2026-01-12
fetch_date: 2026-01-13T03:31:35.558788
---

# n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)

**Jan 12, 2026**Ravie LakshmananVulnerability / Workflow Automation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgN2wvrCTGv4Grbd3bv9DT4hUFuTCDt4Wlec_AQ5mYNiWEp2Kze4dSC56p123i08vZnmWNVBd9EZpcVnBdcN-VGShQYmQdDrgaZ6YshND2_s_ZB4S6Aml_tBIURWmvGI9ixZnXKiQMa62wQydWFKhMWVw6Z8S3nT3KlNPA0uJPFQBUPldUirfSu5UmRKJbY/s790-rw-e365/n8n-supply-chain.jpg)

Threat actors have been observed uploading a set of eight packages on the npm registry that masqueraded as integrations targeting the [n8n](https://thehackernews.com/2026/01/critical-n8n-vulnerability-cvss-100.html) workflow automation platform to steal developers' OAuth credentials.

One such package, named "n8n-nodes-hfgjf-irtuinvcm-lasdqewriit," mimics a Google Ads integration, and prompts users to link their advertising account in a seemingly legitimate form and then siphon it to servers under the attackers' control.

"The attack represents a new escalation in supply chain threats," Endor Labs [said](https://www.endorlabs.com/learn/n8mare-on-auth-street-supply-chain-attack-targets-n8n-ecosystem) in a report published last week. "Unlike traditional npm malware, which often targets developer credentials, this campaign exploited workflow automation platforms that act as centralized credential vaults – holding OAuth tokens, API keys, and sensitive credentials for dozens of integrated services like Google Ads, Stripe, and Salesforce in a single location."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The complete list of identified packages, which have since been removed, is as follows -

* n8n-nodes-hfgjf-irtuinvcm-lasdqewriit (4,241 downloads, author: kakashi-hatake)
* n8n-nodes-ggdv-hdfvcnnje-uyrokvbkl (1,657 downloads, author: kakashi-hatake)
* n8n-nodes-vbmkajdsa-uehfitvv-ueqjhhhksdlkkmz (1,493 downloads, author: kakashi-hatake)
* n8n-nodes-performance-metrics (752 downloads, author: hezi109)
* n8n-nodes-gasdhgfuy-rejerw-ytjsadx (8,385 downloads, author: zabuza-momochi)
* n8n-nodes-danev (5,525 downloads, author: dan\_even\_segler)
* n8n-nodes-rooyai-model (1,731 downloads, author: haggags)
* n8n-nodes-zalo-vietts (4,241 downloads, authors: vietts\_code and diendh)

The users "zabuza-momochi," "dan\_even\_segler," and "diendh" have also been linked to other libraries that are still available for download as of writing -

* [n8n-nodes-gg-udhasudsh-hgjkhg-official](https://secure.software/npm/packages/n8n-nodes-gg-udhasudsh-hgjkhg-official) (2,863 downloads)
* [n8n-nodes-danev-test-project](https://secure.software/npm/packages/n8n-nodes-danev-test-project) (1,259 downloads)
* [@diendh/n8n-nodes-tiktok-v2](https://secure.software/npm/packages/%40diendh/n8n-nodes-tiktok-v2) (218 downloads)
* [n8n-nodes-zl-vietts](https://secure.software/npm/packages/n8n-nodes-zl-vietts) (6,357 downloads)

It's not clear if they harbor similar malicious functionality. However, an assessment of the first three packages on ReversingLabs Spectra Assure has uncovered no security issues. In the case of "n8n-nodes-zl-vietts," the analysis has flagged the library as containing a component with malware history.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtilRbQ8ZrVxXhAnWfnWfVI9WuXfAlGbML7HEvW4TjciTzkJRuN_QUIrMT6fafXLYLUsqDjKHzxc_dIkVAoofARoOCWnaPZtzHF-cPcXyKb1d8CAlt5bbuq8GFQ1dczyAXIdsvLbinS-vNtdzJp8oTnZdHdtwIfEmFsC0-xDiqLA5UKvvymQo50Ysq3H6M/s790-rw-e365/ads.png)

Interestingly, an updated version of the package "n8n-nodes-gg-udhasudsh-hgjkhg-official" was published to npm just three hours ago, suggesting that the campaign is possibly ongoing.

The malicious package, once installed as a [community node](https://docs.n8n.io/integrations/community-nodes/usage/), behaves like any other n8n integration, displaying configuration screens and saving the Google Ads account OAuth tokens in encrypted format to the n8n credential store. When the workflow is executed, it runs code to decrypt the stored tokens using n8n's master key and exfiltrates them to a remote server.

The development marks the first time a supply chain threat has explicitly targeted the n8n ecosystem, with bad actors weaponizing the trust in community integrations to achieve their goals.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The findings highlight the security issues that come with integrating untrusted workflows, which can expand the attack surface. Developers are recommended to audit packages before installing them, scrutinize package metadata for any anomalies, and use official n8n integrations.

N8n has also [warned](https://docs.n8n.io/integrations/community-nodes/risks/) about the security risk arising from the use of community nodes from npm, which it said can execute malicious actions on the machine that the service runs on. On self-hosted n8n instances, it's advised to disable community nodes by setting N8N\_COMMUNITY\_PACKAGES\_ENABLED to false.

"Community nodes run with the same level of access as n8n itself. They can read environment variables, access the file system, make outbound network requests, and, most critically, receive decrypted API keys and OAuth tokens during workflow execution," researchers Kiran Raj and Henrik Plate said. "There is no sandboxing or isolation between node code and the n8n runtime."

"Because of this, a single malicious npm package is enough to gain deep visibility into workflows, steal credentials, and communicate externally without raising immediate suspicion. For attackers, the npm supply chain offers a quiet and highly effective entry point into n8n environments."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [L...