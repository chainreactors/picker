---
title: Hackers Steal Over $1.6 Million in Crypto from General Bytes Bitcoin ATMs Using Zero-Day Flaw
url: https://thehackernews.com/2023/03/hackers-steal-over-16-million-in-crypto.html
source: The Hacker News
date: 2023-03-22
fetch_date: 2025-10-04T10:17:56.648539
---

# Hackers Steal Over $1.6 Million in Crypto from General Bytes Bitcoin ATMs Using Zero-Day Flaw

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

# [Hackers Steal Over $1.6 Million in Crypto from General Bytes Bitcoin ATMs Using Zero-Day Flaw](https://thehackernews.com/2023/03/hackers-steal-over-16-million-in-crypto.html)

**Mar 21, 2023**Ravie LakshmananCryptocurrency / Hacking

[![General Bytes Bitcoin ATM](data:image/png;base64... "General Bytes Bitcoin ATM")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVmPEIXvl4JK4K2CXrjYB6dP3aQoZPTsugEH32w9CULeaeqbEb26Bq52CX5wL4rEYcF9rR_ciJ3G0px_qAot3Kjb7DVFMJ-LUrT0AkYjvP7Yjmjb9GkiNPlOvl89owXx5D19rphx7d1I-xVLPNcJ53e24p9v_VnG22EJEXu-uhfX3YQ1HvfDNrU1ks/s790-rw-e365/BITCOIN.png)

Bitcoin ATM maker General Bytes disclosed that unidentified threat actors stole cryptocurrency from hot wallets by exploiting a zero-day security flaw in its software.

"The attacker was able to upload his own java application remotely via the master service interface used by terminals to upload videos and run it using 'batm' user privileges," the company [said](https://generalbytes.atlassian.net/wiki/spaces/ESD/pages/2885222430/Security%2BIncident%2BMarch%2B17-18th%2B2023) in an advisory published over the weekend.

"The attacker scanned the Digital Ocean cloud hosting IP address space and identified running CAS services on ports 7741, including the General Bytes Cloud service and other GB ATM operators running their servers on Digital Ocean," it further added.

The company said that the server to which the malicious Java application was uploaded was by default configured to start applications present in the deployment folder ("/batm/app/admin/standalone/deployments/").

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In doing so, the attack allowed the threat actor to access the database; read and decrypt API keys used to access funds in hot wallets and exchanges; send funds from the wallets; download usernames, password hashes, and turn off two-factor authentication (2FA); and even access terminal event logs.

General Bytes, [according to its website](https://www.generalbytes.com/en/about-us), has sold more than 15,137 terminals in 149 countries. It supports over 180 fiat currencies and has collectively performed nearly 22.6 million transactions worldwide.

The BATMs are designed to connect to a crypto application server ([CAS](https://generalbytes.atlassian.net/wiki/spaces/ESD/pages/2013921317/Welcome%2Bto%2BCAS)), which are either managed by the customer or by the company itself on the cloud via [infrastructure](https://generalbytes.atlassian.net/wiki/spaces/ESD/pages/1002537156/Create%2Ba%2BVPS%2Bon%2BDigital%2BOcean) provided by DigitalOcean.

It also warned that its own cloud service as well as other operators' standalone servers were infiltrated as a result of the incident, prompting the company to shutter the service.

In addition to urging customers to keep their crypto application servers (CASs) behind a firewall and a VPN, it's also recommending to rotate all users' passwords and API keys to exchanges and hot wallets.

"The CAS security fix is provided in two server patch releases, 20221118.48 and 20230120.44," General Bytes said in the advisory.

The company further emphasized that it had conducted multiple security audits since 2021 and that none of them flagged this vulnerability. It appears to have been unpatched since version 20210401.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

General Bytes did not disclose the exact amount of funds stolen by the hackers, but an analysis of the cryptocurrency wallets used in the attack reveals the receipt of [56.283 BTC](https://blockchair.com/bitcoin/address/bc1qfa8pryacrjuzp9287zc2ufz5n0hdthff0av440) ($1.5 million), [21.823 ETH](https://blockchair.com/ethereum/address/0xd5173d215551538cebe79c4e40a4c54fb751dd83) ($36,500), and [1,219.183 LTC](https://blockchair.com/litecoin/address/ltc1qvd5usunrpgsynyeey9n46xucy7emk62ycljl0t) ($96,500).

The ATM hack is the [second breach](https://thehackernews.com/2022/08/hackers-stole-crypto-from-bitcoin-atms.html) targeting General Bytes in less than a year, with another zero-day flaw in its ATM servers exploited to steal crypto from its customers in August 2022.

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

[Bitcoin ATM](https://thehackernews.com/search/label/Bitcoin%20ATM)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[hacking](https://thehackernews.com/search/label/hacking)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](...