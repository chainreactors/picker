---
title: Russian Ransomware Gangs Weaponize Open-Source AdaptixC2 for Advanced Attacks
url: https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html
source: The Hacker News
date: 2025-10-30
fetch_date: 2025-10-31T03:14:44.736446
---

# Russian Ransomware Gangs Weaponize Open-Source AdaptixC2 for Advanced Attacks

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

# [Russian Ransomware Gangs Weaponize Open-Source AdaptixC2 for Advanced Attacks](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)

**Oct 30, 2025**Ravie LakshmananMalware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHAemb8q0dPL4UJx7V6h0octnu9dSgvaV0KNS8ctKdDRlcrt51uM9BXud3jaJ7Gkc-NGMJfTfTmShpq9ehcNjW2nh-ncTHD37MRt9iY7ThMZKxp_ULdweMDi6iI0O8m_LkZV0N8Yegr1VWMxRUviU5h8jb3z0wlcxzru3Zu48O0AojPbgLvxLOQ8pEDBlS/s790-rw-e365/post-install.jpg)

The open-source command-and-control (C2) framework known as [AdaptixC2](https://github.com/Adaptix-Framework/AdaptixC2) is being used by a growing number of threat actors, some of whom are related to Russian ransomware gangs.

AdaptixC2 is an emerging [extensible post-exploitation and adversarial emulation framework](https://adaptix-framework.gitbook.io/adaptix-framework) designed for penetration testing. While the server component is written in Golang, the GUI Client is written in C++ QT for cross-platform compatibility.

It comes with a wide range of features, including fully encrypted communications, command execution, credential and screenshot managers, and a remote terminal, among others. An early iteration was [publicly released](https://t.me/AdaptixFramework/4) by a GitHub user named "[RalfHacker](https://github.com/RalfHacker)" ([@HackerRalf](https://x.com/hacker_ralf/status/1883592864153968697) on X) in August 2024, who describes themselves as a penetration tester, red team operator, and "MalDev" (short for malware developer).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In recent months, AdaptixC2 has been adopted by various hacking groups, including threat actors tied to the [Fog](https://thehackernews.com/2025/06/ransomware-gangs-exploit-unpatched.html) and [Akira](https://thehackernews.com/2025/08/sonicwall-investigating-potential-ssl.html) ransomware operations, as well as by an initial access broker that has leveraged [CountLoader](https://thehackernews.com/2025/09/countloader-broadens-russian-ransomware.html) in attacks that are designed to deliver various post-exploitation tools.

Palo Alto Networks Unit 42, which broke down the [technical aspects](https://unit42.paloaltonetworks.com/adaptixc2-post-exploitation-framework/) of the framework last month, characterized it as a modular and versatile framework that can be used to "comprehensively control impacted machines," and that it has been put to use as part of fake help desk support call scams via Microsoft Teams and through an artificial intelligence (AI)-generated PowerShell script.

While AdaptixC2 is offered as an ethical, open-source tool for red teaming activities, it's also clear that it has attracted the attention of cybercriminals.

Cybersecurity company Silent Push [said](https://www.silentpush.com/blog/adaptix-c2/) RalfHacker's GitHub bio about them being a "MalDev" triggered an investigation, allowing them to find several email addresses for GitHub accounts linked to the account's owner, in addition to a Telegram channel called [RalfHackerChannel](https://t.me/RalfHackerChannel), where they re-shared messages posted on a [dedicated channel](https://t.me/s/AdaptixFramework) for AdaptixC2. The RalfHackerChannel channel has more than 28,000 subscribers.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a message on the AdaptixFramework channel in August 2024, they mentioned their interest in starting a project about a "public C2, which is very trendy right now" and hoped "it will be like [Empire](https://unit42.paloaltonetworks.com/empire-c2-helps-train-machine-learning-framework/)," another popular post-exploitation and adversary emulation framework.

While it's currently not known if RalfHacker has any direct involvement in malicious activity tied to AdaptixC2 or CountLoader at this stage, Silent Push said their "ties to Russia's criminal underground, via the use of Telegram for marketing and the tool's subsequent uptick in utilization by Russian threat actors, all raise significant red flags."

The Hacker News has reached out to RalfHacker for comment, and we will update the story if we hear back.

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

[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ethical hacking](https://thehackernews.com/search/label/ethical%20hacking)[hacking tool](https://thehackernews.com/search/label/hacking%20tool)[Malware](https://thehackernews.com/search/label/Malware)[Open Source](https://thehackernews.com/search/label/Open%20Source)[ransomware](https://thehackernews.com/search/label/ransomware)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](data:image/svg+xml;base64... "⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens")

⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns...