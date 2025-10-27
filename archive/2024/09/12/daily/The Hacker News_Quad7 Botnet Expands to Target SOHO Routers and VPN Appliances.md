---
title: Quad7 Botnet Expands to Target SOHO Routers and VPN Appliances
url: https://thehackernews.com/2024/09/quad7-botnet-expands-to-target-soho.html
source: The Hacker News
date: 2024-09-12
fetch_date: 2025-10-06T18:40:10.605656
---

# Quad7 Botnet Expands to Target SOHO Routers and VPN Appliances

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

# [Quad7 Botnet Expands to Target SOHO Routers and VPN Appliances](https://thehackernews.com/2024/09/quad7-botnet-expands-to-target-soho.html)

**Sep 11, 2024**Ravie LakshmananNetwork Security / Hacking

[![Quad7 Botnet](data:image/png;base64... "Quad7 Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjbVjDR8WnH7XFwM-jwvPCvWth_3dWl4w9W-xukLInEDS9SobL5Cf54WW2KjF5RATcJ3rQ5x8J2ova-kjLL0n_YxxvrP5rIq-jSPvyIxOFUU-KIMcwNUqW7gTuuxfqRg_KFl3ym3eCmFEEOWmCBe1zItNB-zEA2aRxP0w0jj1qeCC9NksJ7go5h1vDQZqJ/s790-rw-e365/router.png)

The operators of the mysterious Quad7 botnet are actively evolving by compromising several brands of SOHO routers and VPN appliances by leveraging a combination of both known and unknown security flaws.

Targets include devices from TP-LINK, Zyxel, Asus, Axentra, D-Link, and NETGEAR, according to a new report by French cybersecurity company Sekoia.

"The Quad7 botnet operators appear to be evolving their toolset, introducing a new backdoor and exploring new protocols, with the aim of enhancing stealth and evading the tracking capabilities of their operational relay boxes (ORBs)," researchers Felix Aimé, Pierre-Antoine D., and Charles M. [said](https://blog.sekoia.io/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets/).

Quad7, also called 7777, was [first publicly documented](https://gi7w0rm.medium.com/the-curious-case-of-the-7777-botnet-86e3464c3ffd) by independent researcher Gi7w0rm in October 2023, highlighting the activity cluster's pattern of ensnaring TP-Link routers and Dahua digital video recorders (DVRs) into a botnet.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The botnet, which gets its name from the fact it opens TCP port 7777 on compromised devices, has been observed brute-forcing Microsoft 3665 and Azure instances.

"The botnet also appears to infect other systems like MVPower, Zyxel NAS, and GitLab, although at a very low volume," VulnCheck's Jacob Baines [noted](https://vulncheck.com/blog/ip-intel-7777-botnet) earlier this January. "The botnet doesn't just start a service on port 7777. It also spins up a SOCKS5 server on port 11228."

Subsequent [analyses](https://thehackernews.com/2024/08/unpatched-avtech-ip-camera-flaw.html) by Sekoia and Team Cymru over the past few months have found that not only the botnet has compromised TP-Link routers in Bulgaria, Russia, the U.S., and Ukraine, but has since also expanded to target ASUS routers that have TCP ports 63256 and 63260 opened.

[![Quad7 Botnet](data:image/png;base64... "Quad7 Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpBFZhUapUf5BWMwvaZoqChm20fZzOWCsmdLEjS_N87YnSNtKzHEqFmu2cD5Q6QSIGGXREd5m9gI1mgitxjeS_VI_Drq42qVosFDVBXbxcZEa71NHEB26Xnu1_FW1zQl-pa5_zmdH40AQhH7nhJSgjfn_mdX6pZFhfZdbyGIt_X0NaXfp18l1p5CwogNus/s790-rw-e365/chart2.png)

The latest findings show that the botnet is comprised of three additional clusters -

* xlogin (aka 7777 botnet) - A botnet composed of compromised TP-Link routers which have both TCP ports 7777 and 11288 opened
* alogin (aka 63256 botnet) - A botnet composed of compromised ASUS routers which have both TCP ports 63256 and 63260 opened
* rlogin - A botnet composed of compromised Ruckus Wireless devices which have TCP port 63210 opened
* axlogin - A botnet capable of targeting Axentra NAS devices (not detected in the wild as yet)
* zylogin - A botnet composed of compromised Zyxel VPN appliances that have TCP port 3256 opened

Sekoia told The Hacker News that the countries with the most number of infections are Bulgaria (1,093), the U.S. (733), and Ukraine (697).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a further sign of tactical evolution, the threat actors now utilize a new backdoor dubbed UPDTAE that establishes an HTTP-based reverse shell to establish remote control on the infected devices and execute commands sent from a command-and-control (C2) server.

It's currently not clear what the exact purpose of the botnet is or who is behind it, but the company said the activity is likely the work of a Chinese state-sponsored threat actor.

"Regarding the 7777 [botnet], we only saw brute-force attempts against Microsoft 365 accounts," Aimé told the publication. "For the other botnets, we still don't know how they are used."

"However, after exchanges with other researchers and new findings, we are almost certain that the operators are more likely CN state-sponsored rather than simple cybercriminals doing [business email compromise]."

"We are seeing the threat actor attempting to be more stealthy by using new malwares on the compromised edge devices. The main aim behind that move is to prevent tracking of the affiliated botnets."

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

[botnet](https://thehackernews.com/search/label/botnet)[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Malware](https://thehackernews.com/search/label/Malware)[...