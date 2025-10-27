---
title: Vietnamese Human Rights Group Targeted in Multi-Year Cyberattack by APT32
url: https://thehackernews.com/2024/08/vietnamese-human-rights-group-targeted.html
source: The Hacker News
date: 2024-08-30
fetch_date: 2025-10-06T18:09:17.929463
---

# Vietnamese Human Rights Group Targeted in Multi-Year Cyberattack by APT32

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

# [Vietnamese Human Rights Group Targeted in Multi-Year Cyberattack by APT32](https://thehackernews.com/2024/08/vietnamese-human-rights-group-targeted.html)

**Aug 29, 2024**Ravie LakshmananCyber Espionage / Malware

[![Multi-Year Cyberattack](data:image/png;base64... "Multi-Year Cyberattack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1TK5Fhs03GTUwEItgP_qrkAVv5gukRmUE7mkvYQBgUmbq9NGziq9Vju0BHcU1e-7zWOYenRfXo4EXgyXP_Qsuo_nKMaTOTvf_CvzPyZof-vv3ShHMYTudzkGTNh-1fow3LMYI2Ed1ULo1F6I2bQcOU1SUl7CY3HMyUlunODkNulMMcgv3A3X0V1BEjiRR/s790-rw-e365/code.png)

A non-profit supporting Vietnamese human rights has been the target of a multi-year campaign designed to deliver a variety of malware on compromised hosts.

Cybersecurity company Huntress attributed the activity to a threat cluster tracked as APT32, a Vietnamese-aligned hacking crew that's also known as APT-C-00, Canvas Cyclone (formerly Bismuth), Cobalt Kitty, and OceanLotus. The intrusion is believed to have been ongoing for at least four years.

"This intrusion has a number of overlaps with known techniques used by the threat actor APT32/OceanLotus, and a known target demographic which aligns with APT32/OceanLotus targets," security researchers Jai Minton and Craig Sweeney [said](https://www.huntress.com/blog/advanced-persistent-threat-targeting-vietnamese-human-rights-defenders).

[OceanLotus](https://thehackernews.com/2020/12/facebook-tracks-apt32-oceanlotus.html), active since at least 2012, has a [history](https://www.cybereason.com/blog/operation-cobalt-kitty-apt) of targeting company and government networks in East-Asian countries, particularly Vietnam, the Philippines, Laos, and Cambodia with the end goal of cyber espionage and intellectual property theft.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Attack chains [typically](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/) make use of [spear-phishing lures](https://blogs.blackberry.com/en/2019/04/report-oceanlotus-apt-group-leveraging-steganography) as the initial penetration vector to deliver backdoors capable of running arbitrary shellcode and collecting sensitive information. That said, the group has also been observed [orchestrating](https://www.welivesecurity.com/2018/11/20/oceanlotus-new-watering-hole-attack-southeast-asia/) watering hole campaigns as early as 2018 to infect site visitors with a reconnaissance payload or harvest their credentials.

The latest set of attacks pieced together by Huntress spanned four hosts, each of which was compromised to add various scheduled tasks and Windows Registry keys that are responsible for launching Cobalt Strike Beacons, a backdoor that enables the theft of Google Chrome cookies for all user profiles on the system, and loaders responsible for launching embedded DLL payloads.

The development comes as South Korean users are the target of an [ongoing campaign](https://asec.ahnlab.com/ko/82628/) that likely leverages spear-phishing and vulnerable Microsoft Exchange servers to deliver reverse shells, backdoors, and VNC malware to gain control of infected machines and steal credentials stored in web browsers.

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

[APT group](https://thehackernews.com/search/label/APT%20group)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data theft](https://thehackernews.com/search/label/data%20theft)[hacking](https://thehackernews.com/search/label/hacking)[Malware](https://thehackernews.com/search/label/Malware)

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

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in ...