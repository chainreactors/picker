---
title: Researchers Uncover Vulnerabilities in Solarman and Deye Solar Systems
url: https://thehackernews.com/2024/08/researchers-uncover-vulnerabilities-in.html
source: The Hacker News
date: 2024-08-13
fetch_date: 2025-10-06T18:08:59.529000
---

# Researchers Uncover Vulnerabilities in Solarman and Deye Solar Systems

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

# [Researchers Uncover Vulnerabilities in Solarman and Deye Solar Systems](https://thehackernews.com/2024/08/researchers-uncover-vulnerabilities-in.html)

**Aug 12, 2024**Ravie LakshmananCritical Infrastructure / Vulnerability

[![Solarman and Deye Solar Systems](data:image/png;base64... "Solarman and Deye Solar Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtwis5FB4jU1PMRQWQdbKm7jQVTPWvNr8sfV6w2jNxRXfmvmttxc83YcUn_m71DuqXSUvtVRzPYN4rc74t9SD3EPeNyCSKtR0cCdmdm02K7zuyCvUDDQh4eoyE0Ovp-Lx2Ty7fxUj3CsQWOJTdpK6b1IFyDfUyKRoxSv6heN3z_xt3Rpo-kFojwXeeNMvI/s790-rw-e365/solar.png)

Cybersecurity researchers have identified a number of security shortcomings in photovoltaic system management platforms operated by Chinese companies Solarman and Deye that could enable malicious actors to cause disruption and power blackouts.

"If exploited, these vulnerabilities could allow an attacker to control inverter settings that could take parts of the grid down, potentially causing blackouts," Bitdefender researchers [said](https://www.bitdefender.com/blog/labs/60-hurts-per-second-how-we-got-access-to-enough-solar-power-to-run-the-united-states/) in an analysis published last week.

The vulnerabilities have been addressed by Solarman and Deye as of July 2024, following responsible disclosure on May 22, 2024.

The Romanian cybersecurity vendor, which analyzed the two PV monitoring and management platforms, said they suffer from a number of issues that, among others, could result in account takeover and information disclosure.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A brief description of the issues is listed below -

* Full Account Takeover via Authorization Token Manipulation Using the /oauth2-s/oauth/token API endpoint
* Deye Cloud Token Reuse
* Information Leak through /group-s/acc/orgs API Endpoint

* Hard-coded Account with Unrestricted Device Access (account: "SmartConfigurator@solarmanpv.com" / password: 123456)
* Information Leak through /user-s/acc/orgs API Endpoint
* Potential Unauthorized Authorization Token Generation

[![Solarman and Deye Solar Systems](data:image/png;base64... "Solarman and Deye Solar Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSBzhzeY31qeRK95ZjauQ0OZXbcoblRL7gISFfpfBsjXcVWG1CeFw2QsutslKafgUoaeEkCjcT_RALzZmMf_AHnB6wgmpftCRrbhmM2cNLtA-3yWI-z1Qu5QxyhVMw9YAJ7xKSERERQw01WkNCApOiPZlXUn5A1KBY0HXCz4os4jj9UjEG5seM6rMbvjSy/s790-rw-e365/solar.png)

Successful exploitation of the aforementioned vulnerabilities could allow attackers to gain control over any Solarman account, reuse JSON Web Tokens (JWTs) from Deye Cloud to gain unauthorized access to Solarman accounts, and gather private information about all registered organizations.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

They could also obtain information about any Deye device, access confidential registered user data, and even generate authentication tokens for any user on the platform, severely compromising on its confidentiality and integrity.

"Attackers can take over accounts and control solar inverters, disrupting power generation and potentially causing voltage fluctuations," the researchers said.

"Sensitive information about users and organizations can be leaked, leading to privacy violations, information harvesting, targeted phishing attacks or other malicious activities. By accessing and modifying settings on solar inverters, attackers can cause widespread disruptions in power distribution, impacting grid stability and potentially leading to blackouts."

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

[critical infrastructure](https://thehackernews.com/search/label/critical%20infrastructure)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[iot security](https://thehackernews.com/search/label/iot%20security)[power grid](https://thehackernews.com/search/label/power%20grid)[technology](https://thehackernews.com/search/label/technology)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity...