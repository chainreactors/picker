---
title: MyloBot Botnet Spreading Rapidly Worldwide: Infecting Over 50,000 Devices Daily
url: https://thehackernews.com/2023/02/mylobot-botnet-spreading-rapidly.html
source: The Hacker News
date: 2023-02-22
fetch_date: 2025-10-04T07:48:08.856281
---

# MyloBot Botnet Spreading Rapidly Worldwide: Infecting Over 50,000 Devices Daily

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

# [MyloBot Botnet Spreading Rapidly Worldwide: Infecting Over 50,000 Devices Daily](https://thehackernews.com/2023/02/mylobot-botnet-spreading-rapidly.html)

**Feb 21, 2023**Ravie LakshmananEndpoint Security / Botnet

[![MyloBot Botnet](data:image/png;base64... "MyloBot Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPWD1mIOZN3qGcZI8dEvZZIQbf0d8deyWUOsKFOMoYH06j8_sUu6mdH_-RN8AqWbRXh7NSsc7KZKO5zinEkB1P-8y-sh3hLcvK6R3dINqrPvHdTILCcuMYXufvlpFk2Vb96Ar9K1wkM07u7wzOW1GM35SKyzmQkOA6UNqniZI0wmgxCRP151E4mAtq/s790-rw-e365/botnet.jpg)

A sophisticated botnet known as MyloBot has compromised thousands of systems, with most of them located in India, the U.S., Indonesia, and Iran.

That's according to new findings from BitSight, which [said](https://www.bitsight.com/blog/mylobot-investigating-proxy-botnet) it's "currently seeing more than 50,000 unique infected systems every day," down from a high of 250,000 unique hosts in 2020.

Furthermore, an analysis of MyloBot's infrastructure has found connections to a residential proxy service called BHProxies, indicating that the compromised machines are being used by the latter.

MyloBot, which emerged on the threat landscape in 2017, was [first documented](https://www.deepinstinct.com/blog/meet-mylobot-a-new-highly-sophisticated-never-seen-before-botnet-thats-out-in-the-wild) by Deep Instinct in 2018, calling out its anti-analysis techniques and its ability to function as a downloader.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"What makes MyloBot dangerous is its ability to download and execute any type of payload after it infects a host," Lumen's Black Lotus Labs [said](https://blog.lumen.com/mylobot-continues-global-infections/) in November 2018. "This means at any time it could download any other type of malware the attacker desires."

Last year, the malware was observed [sending extortion emails](https://thehackernews.com/2022/02/new-mylobot-malware-variant-sends.html) from hacked endpoints as part of a financially motivated campaign seeking over $2,700 in Bitcoin.

[![MyloBot Botnet](data:image/png;base64... "MyloBot Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4y9asHZIkgRqcs74eur21VSy0m_q48PTJ-7rThCZ78uWx_JmOL9ggPi9DYxvXhYfGtyTlCzDyjqez5ViBPMmemHvv7DEiqgMtPdx7m2TRhmvSjvGWwloqOnrLiwdbL9RTYdkUcTOqyIs_qnDCXjpi67vyfh8qtOiiAMUntbF2hEpH7eHptcbSvhb8/s790-rw-e365/malware.png)

MyloBot is known to employ a multi-stage sequence to unpack and launch the bot malware. Notably, it also sits idle for 14 days before attempting to contact the command-and-control (C2) server to sidestep detection.

The primary function of the botnet is to establish a connection to a hard-coded C2 domain embedded within the malware and await further instructions.

"When Mylobot receives an instruction from the C2, it transforms the infected computer into a proxy," BitSight said. "The infected machine will be able to handle many connections and relay traffic sent through the command-and-control server."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Subsequent iterations of the malware have leveraged a downloader that, in turn, contacts a C2 server, which responds with an encrypted message containing a link to retrieve the MyloBot payload.

[![MyloBot Botnet](data:image/png;base64... "MyloBot Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA2j4gjRUjrf1rtCNo7-VQtHfCByvdQFRlzZnBfdtR1fBgmM0sF2EoHHsQtdV9wkxg4gNvhodFCKoafVNQ1J0Vyj08dE580un2bXrll3qLEzC1CrIQ75LIPgrrqIel9-RriW5KDvef_cc4oco7n-5N1Q0IzP_z2pKrLEKJiLRaILXRg97dmi0NuC9X/s790-rw-e365/map.png)

The evidence that MyloBot could be a part of something bigger stems from a reverse DNS lookup of one of the IP addresses associated with the botnet's C2 infrastructure, which has revealed ties to a domain named "clients.bhproxies[.]com."

The Boston-based cybersecurity company said it began sinkholing MyloBot in November 2018 and that it continues to see the botnet evolve over time.

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

[botnet](https://thehackernews.com/search/label/botnet)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Cred...