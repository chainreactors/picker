---
title: Okta Warns of Credential Stuffing Attacks Targeting Customer Identity Cloud
url: https://thehackernews.com/2024/05/okta-warns-of-credential-stuffing.html
source: The Hacker News
date: 2024-05-31
fetch_date: 2025-10-06T16:54:13.289965
---

# Okta Warns of Credential Stuffing Attacks Targeting Customer Identity Cloud

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

# [Okta Warns of Credential Stuffing Attacks Targeting Customer Identity Cloud](https://thehackernews.com/2024/05/okta-warns-of-credential-stuffing.html)

**May 30, 2024**Ravie LakshmananCredential Stuffing / Incident Response

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0Ia-e4pdjriPDDBZ0bQAVmmExV_gXJusAEN8HZpx_fbejDYDWpY2VrQv_N-KD0A9upeL0Zb0-qKDpih-PzQv-1KJO0MTO2izMq4rkvHe1jpKomXJ3CugZU_umrObBs1fTb_ExtFH7XeUhpYNCwO62WyTNXfChev6vg0rUA0wFYQ-ZUOxObhggUzn4CJBu/s790-rw-e365/okta.png)

Okta is warning that a [cross-origin authentication](https://auth0.com/docs/authenticate/login/cross-origin-authentication) feature in Customer Identity Cloud (CIC) is susceptible to credential stuffing attacks orchestrated by threat actors.

"We observed that the endpoints used to support the cross-origin authentication feature being attacked via credential stuffing for a number of our customers," the Identity and access management (IAM) services provider [said](https://sec.okta.com/articles/2024/05/detecting-cross-origin-authentication-credential-stuffing-attacks).

The suspicious activity commenced on April 15, 2024, with the company noting that it "proactively" informed customers that had the feature enabled. It did not disclose how many customers were impacted by the attacks.

Credential stuffing is a [type of cyber attack](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/) in which adversaries attempt to sign in to online services using an already available list of usernames and passwords obtained either from previous data breaches, or from phishing and malware campaigns.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As recommended actions, users are being asked to review tenant logs for any signs of unexpected [login events](https://auth0.com/docs/deploy-monitor/logs/log-event-type-codes) – failed cross-origin authentication (fcoa), success cross-origin authentication (scoa), and breached password (pwd\_leak) – rotate credentials, and restrict or disable cross-origin authentication for tenants.

Tenants are likely to have been targeted in a credential stuffing attack regardless of whether cross-origin authentication is used or not if scoa or fcoa events are present in event logs and if there is an increase in the failure-to-success events.

Other mitigations include enabling breached password detection or Credential Guard, prohibiting users from choosing weak passwords, and enrolling them in passwordless, phishing resistant authentication using new standards such as [passkeys](https://thehackernews.com/2024/05/google-announces-passkeys-adopted-by.html).

The development arrives a month after the company [alerted](https://thehackernews.com/2024/04/okta-warns-of-unprecedented-surge-in.html) of an uptick in the "frequency and scale" of credential stuffing attacks aimed at online services that's facilitated using residential proxy services.

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

[Breached Password](https://thehackernews.com/search/label/Breached%20Password)[Credential stuffing](https://thehackernews.com/search/label/Credential%20stuffing)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Incident response](https://thehackernews.com/search/label/Incident%20response)[Okta](https://thehackernews.com/search/label/Okta)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](https://thehackernews.com/2025/10/scanning-activity-on-palo-alto-networks.html)

[![...