---
title: Experts Uncover 70,000 Hijacked Domains in Widespread 'Sitting Ducks' Attack Scheme
url: https://thehackernews.com/2024/11/experts-uncover-70000-hijacked-domains.html
source: The Hacker News
date: 2024-11-15
fetch_date: 2025-10-06T19:21:59.914335
---

# Experts Uncover 70,000 Hijacked Domains in Widespread 'Sitting Ducks' Attack Scheme

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

# [Experts Uncover 70,000 Hijacked Domains in Widespread 'Sitting Ducks' Attack Scheme](https://thehackernews.com/2024/11/experts-uncover-70000-hijacked-domains.html)

**Nov 14, 2024**Ravie LakshmananOnline Fraud / Network Security

[![Hijacked Domains](data:image/png;base64... "Hijacked Domains")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDbPXgNRdZ4xewgzZZxQUAbPsD06k3JNmhkxzl6JP4TLDMzazd0Pd0K-Z9HSzw1sa7j7NGQLtRnLcITnyGXngIlPO9y3JJNf59q0P-rjBmByfDXcC6tsAvQzgIzyTvzp4r7d1QmKMLZCOzry14teu0g3oR18ZYRBRWlERyr7bVG_iPomEW8sjUc0glTeDh/s790-rw-e365/domain.png)

Multiple threat actors have been found taking advantage of an attack technique called [Sitting Ducks](https://thehackernews.com/2024/08/over-1-million-domains-at-risk-of.html) to hijack legitimate domains for using them in phishing attacks and investment fraud schemes for years.

The [findings](https://blogs.infoblox.com/threat-intelligence/dns-predators-hijack-domains-to-supply-their-attack-infrastructure) come from Infoblox, which said it identified nearly 800,000 vulnerable registered domains over the past three months, of which approximately 9% (70,000) have been subsequently hijacked.

"Cybercriminals have used this vector since 2018 to hijack tens of thousands of domain names," the cybersecurity company said in a deep-dive report shared with The Hacker News. "Victim domains include well-known brands, non-profits, and government entities."

The little-known attack vector, although [originally documented](https://thehackerblog.com/floating-domains-taking-over-20k-digitalocean-domains-via-a-lax-domain-import-system/) by security researcher Matthew Bryant way back in 2016, didn't attract a lot of attention until the scale of the hijacks was disclosed earlier this August.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"I believe there is more awareness [since then]," Dr. Renee Burton, vice president of threat intelligence at Infoblox, told The Hacker News. "While we haven't seen the number of hijackings go down, we have seen customers very interested in the topic and grateful for awareness around their own potential risks.

The Sitting Ducks attack, at its core, allows a malicious actor to seize control of a domain by leveraging misconfigurations in its domain name system ([DNS](https://en.wikipedia.org/wiki/Domain_Name_System)) settings. This includes scenarios where the DNS points to the wrong authoritative name server.

However, there are certain prerequisites in order to pull this off: A registered domain delegates authoritative DNS services to a different provider than the domain registrar, the [delegation is lame](https://www.akamai.com/glossary/what-are-lame-delegations), and the attacker can "claim" the domain at the DNS provider and set up DNS records without access to the valid owner's account at the domain registrar.

[![Hijacked Domains](data:image/png;base64... "Hijacked Domains")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp8LxQD_a9ThJyNIewOcw8JIwzAm6kkhCvD07REDu1EGJeTy2Opq25CLpjQXoTUrG-WV3royTQzm8DrT6SAzC4Pig5uy9rflGpuW8TxsEt3RHYCL2Lrd9oOKYwttI49HwF3-K0ovBK7EQJVdybY3Iw9tHljzjYoiBWatoHwt1zQhhyphenhyphenf1lhCh-qzAC2lWXk/s790-rw-e365/attack.png)

Sitting Ducks is both easy to perform and stealthy, in part driven by the positive reputation that many of the hijacked domains have. Some of the domains that have fallen prey to the attacks include an entertainment company, an IPTV service provider, a law firm, an orthopedic and cosmetic supplier, a Thai online apparel store, and a tire sales firm.

The threat actors who hijack such domains take advantage of the brand reposition and the fact that they are unlikely to be flagged by security tools as malicious to accomplish their strategic goals.

"It is hard to detect because if the domain has been hijacked, then it is not lame," Burton explained. "Without any other sign, like a phishing page or a piece of malware, the only signal is a change of IP addresses."

"The number of domains is so vast that attempts to use IP changes to indicate malicious activity would lead to a lot of false positives. We 'back in' to tracking the threat actors that are hijacking domains by first understanding how they individually operate and then tracking that behavior."

An important aspect that's common to the Sitting Ducks attacks is rotational hijacking, where one domain is repeatedly taken over by different threat actors over time.

[![Hijacked Domains](data:image/png;base64... "Hijacked Domains")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfhVkQ299l3CuqTwrqq-FDpraNo_uW3-9MsvbCpLbByDofJ7W3hDa8_P-vCOXAiml152T2PjoMGgWkBWUlMB-nh36YtA5DLXOuRgrgmEZM6O0U3Duh98tz_t3SC-QySLQX32EhKEwkBx6vQo67IOPrvWrtI2GP5aZL92PY2zmdOy-GCAzvOB0e61JIzfKG/s1010/sitting-such.png)

"Threat actors often use exploitable service providers that offer free accounts like DNS Made Easy as lending libraries, typically hijacking domains for 30 to 60 days; however, we've also seen other cases where actors hold the domain for a long period of time," Infoblox noted.

"After the short-term, free account expires, the domain is 'lost' by the first threat actor and then either parked or claimed by another threat actor."

Some of the prominent DNS threat actors that have been found "feasting on" Sitting Ducks attacks are listed below -

* Vacant Viper, which has used it to operate the 404 TDS, alongside running malicious spam operations, delivering porn, establishing command-and-control (C2), and dropping malware such as DarkGate and AsyncRAT (Ongoing since December 2019)
* Horrid Hawk, which has used it to conduct investment fraud schemes by distributing the hijacked domains via short-lived Facebook ads (Ongoing since at least February 2023)
* Hasty Hawk, which has used it to conduct widespread phishing campaigns that primarily mimic DHL shipping pages and fake donation sites that mimic supportukrainenow[.]org and claim to support Ukraine (Ongoing since at least March 2022)
* [VexTrio V...