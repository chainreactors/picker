---
title: Over 1 Million Domains at Risk of 'Sitting Ducks' Domain Hijacking Technique
url: https://thehackernews.com/2024/08/over-1-million-domains-at-risk-of.html
source: The Hacker News
date: 2024-08-02
fetch_date: 2025-10-06T18:07:22.541382
---

# Over 1 Million Domains at Risk of 'Sitting Ducks' Domain Hijacking Technique

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

# [Over 1 Million Domains at Risk of 'Sitting Ducks' Domain Hijacking Technique](https://thehackernews.com/2024/08/over-1-million-domains-at-risk-of.html)

**Aug 01, 2024**Ravie LakshmananVulnerability / Threat Intelligence

[![Domain Hijacking Technique](data:image/png;base64... "Domain Hijacking Technique")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMhhnkpBltf8eiRERnidnvbignuAJNzXkC1wxLIk0-ti6m-IP__y27HsfTleGPzIQVbB8R_Rgs3neAcEBVp-7FC3CtJnx58VsF84XQCdJExUi-ooRJO3SQRseKse6oueKjv5eKifXFCr_lQySQiQmyD4Bwx69IXwMvu8HtnUht3c6gUEB3RVrRpQfmxqVl/s790-rw-e365/domain.png)

Over a million domains are susceptible to takeover by malicious actors by means of what has been called a **Sitting Ducks** attack.

The powerful attack vector, which exploits weaknesses in the domain name system (DNS), is being exploited by over a dozen Russian-nexus cybercriminal actors to stealthily hijack domains, a joint analysis published by [Infoblox](https://blogs.infoblox.com/threat-intelligence/who-knew-domain-hijacking-is-so-easy/) and [Eclypsium](https://eclypsium.com/blog/ducks-now-sitting-dns-internet-infrastructure-insecurity/) has revealed.

"In a Sitting Ducks attack, the actor hijacks a currently registered domain at an authoritative DNS service or web hosting provider without accessing the true owner's account at either the [DNS provider](https://www.cloudflare.com/learning/dns/dns-server-types/) or registrar," the researchers said.

"Sitting Ducks is easier to perform, more likely to succeed, and harder to detect than other well-publicized domain hijacking attack vectors, such as [dangling CNAMEs](https://thehackernews.com/2024/02/8000-subdomains-of-trusted-brands.html)."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Once a domain has been taken over by the threat actor, it could be used for all kinds of nefarious activities, including serving malware and conducting spams, while abusing the trust associated with the legitimate owner.

Details of the "pernicious" attack technique were [first](https://thehackerblog.com/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/) [documented](https://thehackerblog.com/the-orphaned-internet-taking-over-120k-domains-via-a-dns-vulnerability-in-aws-google-cloud-rackspace-and-digital-ocean/) by The Hacker Blog in 2016, although it remains largely unknown and unresolved to date. More than 35,000 domains are estimated to have been hijacked since 2018.

"It is a mystery to us," Dr. Renee Burton, vice president of threat intelligence at Infoblox, told The Hacker News. "We frequently receive questions from prospective clients, for example, about dangling CNAME attacks which are also a hijack of forgotten records, but we have never received a question about a Sitting Ducks hijack."

At issue is the incorrect configuration at the domain registrar and the inadequate ownership verification at the authoritative DNS provider, coupled with the fact that the nameserver is unable to respond authoritatively for a domain it's listed to serve (i.e., [lame delegation](https://www.cloudns.net/blog/dns-delegation/)).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqmoIJSOmp9mx2Igt8-uX9deJmmTsdekpKzUI60TPfHMBPcLLOriWxAoSrjHznaI3tWHMLqZa6oYvf7WNxWUTz_uzW55TRlhu_eE2Nty7dZ0HD_j0Ytr7C6nsblF5_9dWWN7UbpGiwb3VKJ0WHbjpnnMSmfMVZthAcZRKWo5Ze-R3RGIhIcMgC_JzLF7QZ/s1700/spot-image-sitting-duck-fig-2.jpg)

It also requires that the authoritative DNS provider is exploitable, permitting the attacker to claim ownership of the domain at the delegated authoritative DNS provider while not having access to the valid owner's account at the domain registrar.

In such a scenario, should the authoritative DNS service for the domain expire, the threat actor could create an account with the provider and claim ownership of the domain, ultimately impersonating the brand behind the domain to distribute malware.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"There are many variations [of Sitting Ducks], including when a domain has been registered, delegated, but not configured at the provider," Burton said.

​​The Sitting Ducks attack has been weaponized by different threat actors over the years, with the stolen domains used to fuel multiple traffic distribution systems (TDSes) such as [404 TDS](https://thehackernews.com/2023/02/hackers-targeting-us-and-german-firms.html) (aka Vacant Viper) and [VexTrio Viper](https://thehackernews.com/2024/01/vextrio-uber-of-cybercrime-brokering.html). It has also been leveraged to [propagate](https://krebsonsecurity.com/2019/01/bomb-threat-sextortion-spammers-abused-weakness-at-godaddy-com/) bomb threat hoaxes and sextortion scams, an activity cluster tracked as Spammy Bear.

"Organizations should check the domains they own to see if any are lame and they should use DNS providers that have protection against Sitting Ducks," Burton said.

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

[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DNS Vulnerability](https://...