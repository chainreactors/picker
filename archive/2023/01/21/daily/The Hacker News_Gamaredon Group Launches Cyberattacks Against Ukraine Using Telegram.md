---
title: Gamaredon Group Launches Cyberattacks Against Ukraine Using Telegram
url: https://thehackernews.com/2023/01/gamaredon-group-launches-cyberattacks.html
source: The Hacker News
date: 2023-01-21
fetch_date: 2025-10-04T04:32:07.206539
---

# Gamaredon Group Launches Cyberattacks Against Ukraine Using Telegram

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

# [Gamaredon Group Launches Cyberattacks Against Ukraine Using Telegram](https://thehackernews.com/2023/01/gamaredon-group-launches-cyberattacks.html)

**Jan 20, 2023**Ravie LakshmananCyber War / Cyber Attack

[![Cyberattacks Against Ukraine](data:image/png;base64... "Cyberattacks Against Ukraine")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigo210ObqgRzhoJott_rD-W6PlRZjR69UbRkcBHHEg2MfpRZcAVhc9mU1yVKjY2lbSSVuIJZyQJa0xjL78pqdWmJL6kdHlqm9wGDNLBE-OQWtM1rDQlkySi8U2M4lAgQ7ZyJlIrFB-JI_p31bBlqc473rf-jIOi-xZXbz_r9VRDOgVy5kx_XjLuvNc/s790-rw-e365/telegram.png)

The Russian state-sponsored cyber espionage group known as Gamaredon has continued its digital onslaught against Ukraine, with recent attacks leveraging the popular messaging app Telegram to strike military and law enforcement sectors in the country.

"The Gamaredon group's network infrastructure relies on multi-stage Telegram accounts for victim profiling and confirmation of geographic location, and then finally leads the victim to the next stage server for the final payload," the BlackBerry Research and Intelligence Team [said](https://blogs.blackberry.com/en/2023/01/gamaredon-abuses-telegram-to-target-ukrainian-organizations) in a report shared with The Hacker News. "This kind of technique to infect target systems is new."

[Gamaredon](https://blogs.blackberry.com/en/2022/11/gamaredon-leverages-microsoft-office-docs-to-target-ukraine-government), also known by names such as Actinium, Armageddon, Iron Tilden, Primitive Bear, Shuckworm, Trident Ursa, and Winterflounder, is known for its assaults aimed at Ukrainian entities since at least 2013.

Last month, Palo Alto Networks Unit 42 [disclosed](https://thehackernews.com/2022/12/russian-hackers-target-major-petroleum.html) the threat actor's unsuccessful attempts to break into an unnamed petroleum refining company within a NATO member state amid the Russo-Ukrainian war.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attack chains mounted by the threat actor have [employed](https://thehackernews.com/2022/09/russian-gamaredon-hackers-target.html) legitimate Microsoft Office documents originating from Ukrainian government organizations as lures in spear-phishing emails to deliver malware capable of harvesting sensitive information.

These documents, when opened, load a malicious template from a remote source (a technique called remote template injection), effectively getting around the need to enable macros in order to breach target systems and propagate the infection.

The latest findings from BlackBerry demonstrate an evolution in the group's tactics, wherein a hard-coded Telegram channel is used to fetch the IP address of the server hosting the malware. The IP addresses are periodically rotated to fly under the radar.

To that end, the remote template is designed to fetch a VBA script, which drops a VBScript file that then connects to the IP address specified in the Telegram channel to fetch the next-stage – a PowerShell script that, in turn, reaches out to a different IP address to obtain a PHP file.

This PHP file is tasked with contacting another Telegram channel to retrieve a third IP address that contains the final payload, which is an information-stealing malware that was previously [revealed](https://thehackernews.com/2022/09/russian-gamaredon-hackers-target.html) by Cisco Talos in September 2022.

It's also worth pointing out that the heavily obfuscated VBA script is only delivered if the target's IP address is located in Ukraine.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The threat group changes IP addresses dynamically, which makes it even harder to automate analysis through sandbox techniques once the sample has aged out," BlackBerry pointed out.

"The fact that the suspect IP addresses change only during Eastern European working hours strongly suggests that the threat actor works from one location, and with all probability belongs to an offensive cyber unit that deploys malicious operations against Ukraine."

The development comes as the Computer Emergency Response Team of Ukraine (CERT-UA) [attributed](https://cip.gov.ua/en/news/kiberataka-ne-zmogla-zupiniti-robotu-informaciinogo-agentstva-ukrinform) a [destructive malware attack](https://cip.gov.ua/ua/news/ukrinform-mogli-atakuvati-khakeri-z-ugrupuvannya-sandworm-pov-yazanogo-z-rosiiskim-gru-poperedni-dani-doslidzhennya-cert-ua) targeting the National News Agency of Ukraine to the Russia-linked [Sandworm](https://thehackernews.com/2022/11/microsoft-blames-russian-hackers-for.html) hacking group.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Gamaredon Hackers](https://thehackernews.com/search/label/Gamaredon%20Hackers)[Malware](https://thehackernews.com/search/label/Malware)[Telegram](https://thehackernews.com/search/label/Telegram)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-...