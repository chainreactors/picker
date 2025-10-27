---
title: New SOHO Router Botnet AVrecon Spreads to 70,000 Devices Across 20 Countries
url: https://thehackernews.com/2023/07/new-soho-router-botnet-avrecon-spreads.html
source: The Hacker News
date: 2023-07-15
fetch_date: 2025-10-04T11:55:45.364743
---

# New SOHO Router Botnet AVrecon Spreads to 70,000 Devices Across 20 Countries

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

# [New SOHO Router Botnet AVrecon Spreads to 70,000 Devices Across 20 Countries](https://thehackernews.com/2023/07/new-soho-router-botnet-avrecon-spreads.html)

**Jul 14, 2023**Ravie LakshmananNetwork Security / Malware

[![SOHO Router Botnet](data:image/png;base64... "SOHO Router Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIAt0dtx2_JDXDxAduKTtD9YItkgONoDf-qpj5eRyhdSKugD2FG_50vShdBECG01t0QzsEZm7QFjXyCHNZseCpPTsWki4SE7Mmq9iH9CksV_3LMudZD6mPzJF2C0C2HzKKXgYmBWrgGQ3rBq5P-NXHiyY5oIaA9AvAjJCHHuTxTqgrWtXLO2WeD8kjfJyi/s790-rw-e365/black.jpg)

A new malware strain has been found covertly targeting small office/home office (SOHO) routers for more than two years, infiltrating over 70,000 devices and creating a botnet with 40,000 nodes spanning 20 countries.

Lumen Black Lotus Labs has dubbed the malware **AVrecon**, making it the third such strain to focus on SOHO routers after [ZuoRAT](https://thehackernews.com/2022/06/zuorat-malware-hijacking-home-office.html) and [HiatusRAT](https://thehackernews.com/2023/03/new-hiatusrat-malware-targets-business.html) over the past year.

"This makes AVrecon one of the largest SOHO router-targeting botnets ever seen," the company [said](https://blog.lumen.com/routers-from-the-underground-exposing-avrecon/). "The purpose of the campaign appears to be the creation of a covert network to quietly enable a range of criminal activities from password spraying to digital advertising fraud."

A majority of the infections are located in the U.K. and the U.S., followed by Argentina, Nigeria, Brazil, Italy, Bangladesh, Vietnam, India, Russia, and South Africa, among others.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

AVrecon was [first highlighted](https://twitter.com/sethkinghi/status/1397814848549900288) by Kaspersky senior security researcher Ye (Seth) Jin in May 2021, indicating that the malware has managed to avoid detection until now.

In the attack chain detailed by Lumen, a successful infection is followed by enumerating the victim's SOHO router and exfiltrating that information back to an embedded command-and-control (C2) server.

It also checks if other instances of malware are already running on the host by searching for existing processes on port 48102 and opening a listener on that port. A process bound to that port is terminated.

[![SOHO Router Botnet](data:image/png;base64... "SOHO Router Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtjsLa3X2ubfwxz2aMlQC0mB4tq9-WgHf1NnPwciiiHvNGSkTc5YQcnh6Y2D-7ze2FhTmCZCWusck4AUoNjxEZX2XTWlNvgHOl41rl18gxbjT86CUuYF5eB0Z0PMQ4Y6bP1-PA9s4QJd8HRkH5jbSyVPmc2D0ncZ_QRKHR5QTniXrUWedYYk0mpEHP_gwO/s790-rw-e365/bots.jpg)

The next stage involves the compromised system establishing contact with a separate server, called the secondary C2 server, to await further commands. Lumen said it identified 15 such unique servers that have been active since at least October 2021.

It's worth noting that tiered C2 infrastructure is prevalent among notorious botnets like [Emotet](https://www.welivesecurity.com/2023/07/06/whats-up-with-emotet/) and [QakBot](https://thehackernews.com/2023/06/evasive-qbot-malware-leverages-short.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

AVrecon is written in the C programming language, making it easy to port the malware for different architectures. What's more, a crucial reason why such attacks work is because they leverage infrastructure living on the edge that typically lacks support for security solutions.

Evidence gathered so far points to the botnet being used for clicking on various Facebook and Google ads, and to interact with Microsoft Outlook. This likely indicates a two-pronged effort to conduct advertising fraud and data exfiltration.

"The manner of attack seems to focus predominantly on stealing bandwidth – without impacting end-users – in order to create a [residential proxy service](https://thehackernews.com/2023/06/cybercriminals-hijacking-vulnerable-ssh.html) to help launder malicious activity and avoid attracting the same level of attention from Tor-hidden services or commercially available VPN services," the researchers said.

### AVRecon Linked to Malware Proxy Service SocksEscort

New findings have revealed that AVrecon is the "malware engine" behind a service called SocksEscort, which rents hacked residential and small business devices to cybercriminals looking to obscure their true location online, KrebsOnSecurity [reported](https://krebsonsecurity.com/2023/07/who-and-what-is-behind-the-malware-proxy-service-socksescort/) on July 25, 2023, linking it to a Moldovan national named Adrian Crismaru.

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

[Emotet](https://thehackernews.com/search/label/Emotet)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Router hacking](https://thehackernews.com/search/label/Router%20hacking)[router security](https://thehackernews.com/search/label/router%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds ...