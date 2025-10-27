---
title: Massive Git Config Breach Exposes 15,000 Credentials; 10,000 Private Repos Cloned
url: https://thehackernews.com/2024/11/massive-git-config-breach-exposes-15000.html
source: The Hacker News
date: 2024-11-02
fetch_date: 2025-10-06T19:20:40.130412
---

# Massive Git Config Breach Exposes 15,000 Credentials; 10,000 Private Repos Cloned

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

# [Massive Git Config Breach Exposes 15,000 Credentials; 10,000 Private Repos Cloned](https://thehackernews.com/2024/11/massive-git-config-breach-exposes-15000.html)

**Nov 01, 2024**Ravie LakshmananVulnerability / Cloud Security

[![Massive Git Config Breach](data:image/png;base64... "Massive Git Config Breach")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcVrsuFBB-v2r6qUMRYJyhiPaIgI8urfLOl8DJmI6vVqz_O5XtRPoVujk1WQIi3xYKQv8pj3gMY3rle9us-q_7IdqIUNawzbX5XZODGKOgkm4ZFl5alSXi8u6dVoDBYbAsmqWwfoCFJ-co61kSDweCOe3zj1oFLGtHVld3_Kad41YokTWmBmRzo6wG3uNM/s790-rw-e365/git.png)

Cybersecurity researchers have flagged a "massive" campaign that targets exposed Git configurations to siphon credentials, clone private repositories, and even extract cloud credentials from the source code.

The activity, codenamed **EMERALDWHALE**, is estimated to have collected over 10,000 private repositories and stored in an Amazon S3 storage bucket belonging to a prior victim. The bucket, consisting of no less than 15,000 stolen credentials, has since been taken down by Amazon.

"The stolen credentials belong to Cloud Service Providers (CSPs), Email providers, and other services," Sysdig [said](https://sysdig.com/blog/emeraldwhale/) in a report. "Phishing and spam seem to be the primary goal of stealing the credentials."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The multi-faceted criminal operation, while not sophisticated, has been found to leverage an arsenal of private tools to steal credentials as well as scrape Git config files, Laravel .env files, and raw web data. It has not been attributed to any known threat actor or group.

Targeting servers with exposed Git repository configuration files using broad IP address ranges, the toolset adopted by EMERALDWHALE allows for the discovery of relevant hosts and credential extraction and validation.

These stolen tokens are subsequently used to clone public and private repositories and grab more credentials embedded in the source code. The captured information is finally uploaded to the S3 bucket.

[![Massive Git Config Breach](data:image/png;base64... "Massive Git Config Breach")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPIIyERKeZow0ka_7e_qdtfjXhpxK0xLYOCMtaAks2WnRjXC7xLSPcNY3y9vZV_BBa7DtjedhS8hcYswgWhME6zwdyOsSN9wVCRLkFnhi4WZxm1QmEf_0YG1cvkcGGB3XtoITfjEOIIs7SVtLyletg-NGkTljiNMXwsRT8_BNEP0N98nWTs03X9_l1A9MO/s790-rw-e365/git.png)

Two prominent programs the threat actor uses to realize its goals are MZR V2 and Seyzo-v2, which are sold on underground marketplaces and are capable of accepting a list of IP addresses as inputs for scanning and exploitation of exposed Git repositories.

These lists are typically compiled using legitimate search engines like Google Dorks and Shodan and scanning utilities such as [MASSCAN](https://github.com/robertdavidgraham/masscan).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

What's more, Sysdig's analysis found that a list comprising more than 67,000 URLs with the path "/.git/config" exposed is being offered for sale via Telegram for $100, signaling that there exists a market for Git configuration files.

"EMERALDWHALE, in addition to targeting Git configuration files, also targeted exposed Laravel environment files," Sysdig researcher Miguel Hernández said. "The .env files contain a wealth of credentials, including cloud service providers and databases."

"The underground market for credentials is booming, especially for cloud services. This attack shows that secret management alone is not enough to secure an environment."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[Malware](https://thehackernews.com/search/label/Malware)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First M...