---
title: Cybercriminals Use Go Resty and Node Fetch in 13 Million Password Spraying Attempts
url: https://thehackernews.com/2025/02/cybercriminals-use-axios-and-node-fetch.html
source: The Hacker News
date: 2025-02-06
fetch_date: 2025-10-06T20:39:55.051951
---

# Cybercriminals Use Go Resty and Node Fetch in 13 Million Password Spraying Attempts

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

# [Cybercriminals Use Go Resty and Node Fetch in 13 Million Password Spraying Attempts](https://thehackernews.com/2025/02/cybercriminals-use-axios-and-node-fetch.html)

**Feb 05, 2025**Ravie LakshmananCybersecurity / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYcB32bkzUF1AUr0lZ-QhdBoLLvnT73Shfa_xeGfbzGcBDUBqpyPKsM8S2JQTYp2QPGEz9VYJtSjJQyPoaq62xn45twN9602Yhyphenhyphen2oaCfmumyoGw_m7b9zmIzDVJ4rtwEIe7veBBkkObIMddQ2IOKjt81JpF3aCJmPHikqQqDQwGUOk2Z3KPxOrkKRfKHDg/s790-rw-e365/pssword.png)

Cybercriminals are increasingly leveraging legitimate HTTP client tools to facilitate account takeover (ATO) attacks on Microsoft 365 environments.

Enterprise security company Proofpoint said it observed campaigns using HTTP clients Axios and Node Fetch to send HTTP requests and receive HTTP responses from web servers with the goal of conducting ATO attacks.

"Originally sourced from public repositories like GitHub, these tools are increasingly used in attacks like Adversary-in-the-Middle (AitM) and brute force techniques, leading to numerous account takeover (ATO) incidents," security researcher Anna Akselevich [said](https://www.proofpoint.com/us/blog/threat-insight/http-client-tools-exploitation-account-takeover-attacks).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The use of HTTP client tools for brute-force attacks has been a long-observed trend since at least February 2018, with successive iterations employing variants of OkHttp clients to target Microsoft 365 environments at least until early 2024.

But by March 2024, Proofpoint said it began to observe a wide range of HTTP clients gaining traction, with the attacks scaling a new high such that 78% of Microsoft 365 tenants were targeted at least once by an ATO attempt by the second half of last year.

"In May 2024, these attacks peaked, leveraging millions of hijacked residential IPs to target cloud accounts," Akselevich said.

The volume and diversity of these attack attempts is evidenced by the emergence of HTTP clients such as Axios, Go Resty, Node Fetch, and Python Requests, with those combining precision targeting with AitM techniques achieving a higher compromise rate.

Axios, per Proofpoint, is designed for Node.js and browsers and can be paired with AitM platforms like Evilginx to enable theft of credentials and multi-factor authentication (MFA) codes.

The threat actors have also been observed setting up new mailbox rules to conceal evidence of malicious activities, stealing sensitive data, and even registering a new OAuth application with excessive permission scopes to establish persistent remote access to the compromised environment.

The Axios campaign is said to have primarily singled out high-value targets like executives, financial officers, account managers, and operational staff across transportation, construction, finance, IT, and healthcare verticals.

Over 51% of the targeted organizations have been assessed to be successfully impacted between June and November 2024, compromising 43% of targeted user accounts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The cybersecurity company said it also detected a large-scale password spraying campaign using Node Fetch and Go Resty clients, recording no less than 13 million login attempts since June 9, 2024, averaging over 66,000 malicious attempts per day. The success rate, however, remained low, affecting only 2% of targeted entities.

More than 178,000 targeted user accounts across 3,000 organizations have been identified to date, a majority of which belong to the education sector, particularly student user accounts that are likely to be less protected and can be weaponized for other campaigns or sold to different threat actors.

"Threat actors' tools for ATO attacks have greatly evolved, with various HTTP client tools used for exploiting APIs and making HTTP requests," Akselevich said. "These tools offer distinct advantages, making attacks more efficient."

"Given this trend, attackers are likely to continue switching between HTTP client tools, adapting strategies to leverage new technologies and evade detection, reflecting a broader pattern of constant evolution to enhance their effectiveness and minimize exposure."

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

[account takeover](https://thehackernews.com/search/label/account%20takeover)[Brute force](https://thehackernews.com/search/label/Brute%20force)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Microsoft 365](https://thehackernews.com/search/label/Microsoft%20365)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chao...