---
title: New Go-based Backdoor GoGra Targets South Asian Media Organization
url: https://thehackernews.com/2024/08/new-go-based-backdoor-gogra-targets.html
source: The Hacker News
date: 2024-08-08
fetch_date: 2025-10-06T18:08:40.143445
---

# New Go-based Backdoor GoGra Targets South Asian Media Organization

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

# [New Go-based Backdoor GoGra Targets South Asian Media Organization](https://thehackernews.com/2024/08/new-go-based-backdoor-gogra-targets.html)

**Aug 07, 2024**Ravie LakshmananCloud Security / Cyber Espionage

[![Go-based Backdoor](data:image/png;base64... "Go-based Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuim1UlAUR-iKBziT1BUU4nm6SNgwZaOOcJ8j_auM91hpLEOFZpmHVkutctdKfi8S4jeeyz_7TiWlv0xO0kUGVPOqAxDcEU7ShIGzLEOJ2ufDveReH-bscdBjVpKZTWKxo6-I4cPH27IWmzFeTcIwRlgXe6WIDKql3mKKUFiA4-LgNkRtFIcCzq-9xQajs/s790-rw-e365/cyberattack.png)

An unnamed media organization in South Asia was targeted in November 20233 using a previously undocumented Go-based backdoor called GoGra.

"GoGra is written in Go and uses the Microsoft Graph API to interact with a command-and-control (C&C) server hosted on Microsoft mail services," Symantec, part of Broadcom, [said](https://symantec-enterprise-blogs.security.com/threat-intelligence/cloud-espionage-attacks) in a report shared with The Hacker News.

It's currently not clear how it's delivered to target environments. However, GoGra is specifically configured to read messages from an Outlook username "FNU LNU" whose subject line starts with the word "Input."

The message contents are then decrypted using the AES-256 algorithm in Cipher Block Chaining (CBC) mode using a key, following which it executes the commands via cmd.exe.

The results of the operation are then encrypted and sent to the same user with the subject "Output."

GoGra is said to be the work of a nation-state hacking group known as [Harvester](https://thehackernews.com/2024/05/hackers-increasingly-abusing-microsoft.html) owing to its similarities to a custom .NET implant named Graphon that also utilizes the Graph API for C&C purposes.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as threat actors are increasingly taking advantage of legitimate cloud services to stay low-key and avoid having to purchase dedicated infrastructure.

Some of the other new malware families that have employed the technique are listed below -

* A previously unseen data exfiltration tool deployed by [Firefly](https://thehackernews.com/2024/06/chinese-cyber-espionage-targets-telecom.html) in a cyber attack targeting a military organization in Southeast Asia. The harvested information is uploaded to Google Drive using a hard-coded refresh token.

* A new backdoor dubbed Grager that was deployed against three organizations in Taiwan, Hong Kong, and Vietnam in April 2024. It uses the Graph API to communicate with a C&C server hosted on Microsoft OneDrive. The activity has been tentatively linked to a suspected Chinese threat actor tracked as [UNC5330](https://thehackernews.com/2024/04/researchers-identify-multiple-china.html).

* A backdoor known as MoonTag that contains functionality for communicating with the Graph API and is attributed to a Chinese-speaking threat actor

* A backdoor called Onedrivetools that has been used against IT services companies in the U.S. and Europe. It uses the Graph API to interact with a C&C server hosted on OneDrive to execute received commands and save the output to OneDrive.

"Although leveraging cloud services for command and control is not a new technique, more and more attackers have started to use it recently," Symantec said, pointing to malware like [BLUELIGHT](https://thehackernews.com/2022/12/north-korea-hackers-using-new-dolphin.html), [Graphite](https://thehackernews.com/2022/01/hackers-exploited-mshtml-flaw-to-spy-on.html), [Graphican](https://thehackernews.com/2023/06/chinese-hacker-group-flea-targets.html), and [BirdyClient](https://thehackernews.com/2024/05/hackers-increasingly-abusing-microsoft.html).

"The number of actors now deploying threats that leverage cloud services suggests that espionage actors are clearly studying threats created by other groups and mimicking what they perceive to be successful techniques."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[Information security](https://thehackernews.com/search/label/Information%20security)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/...