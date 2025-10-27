---
title: Raspberry Robin Worm Strikes Again, Targeting Telecom and Government Systems
url: https://thehackernews.com/2022/12/raspberry-robin-worm-strikes-again.html
source: The Hacker News
date: 2022-12-22
fetch_date: 2025-10-04T02:15:33.332363
---

# Raspberry Robin Worm Strikes Again, Targeting Telecom and Government Systems

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

# [Raspberry Robin Worm Strikes Again, Targeting Telecom and Government Systems](https://thehackernews.com/2022/12/raspberry-robin-worm-strikes-again.html)

**Dec 21, 2022**Ravie Lakshmanan

[![Raspberry Robin Worm](data:image/png;base64... "Raspberry Robin Worm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRVJjBvQfK0PWR6FkMazheqwCCdCIlq-tK7upDED-CRn9b1eEEhPKRXRryNxMyWezRfLvtonBTb0mPHOWmfvpQmrwg_44GqOP654oLwPChHyrWl3SoZkNBjYQgST4eKImuuSzHTWFfobrSJjWANNY03q6YHVXx1ZIgMrsKkOCfyarz03X3lUb77bME/s790-rw-e365/Raspberry-Robin-Malware.jpg)

The **Raspberry Robin** worm has been used in attacks against telecommunications and government office systems across Latin America, Australia, and Europe since at least September 2022.

"The main payload itself is packed with more than 10 layers for obfuscation and is capable of delivering a fake payload once it detects sandboxing and security analytics tools," Trend Micro researcher Christopher So [said](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html) in a technical analysis published Tuesday.

A majority of the infections have been detected in Argentina, followed by Australia, Mexico, Croatia, Italy, Brazil, France, India, and Colombia.

Raspberry Robin, attributed to an activity cluster tracked by Microsoft as [DEV-0856](https://thehackernews.com/2022/10/raspberry-robin-operators-selling.html), is being increasingly [leveraged by multiple threat actors](https://thehackernews.com/2022/12/new-truebot-malware-variant-leveraging.html) as an initial access mechanism to deliver payloads such as [LockBit](https://thehackernews.com/2022/11/amadey-bot-spotted-deploying-lockbit-30.html) and [Clop](https://thehackernews.com/2021/06/clop-gang-members-laundered-500-million.html) ransomware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware is known for relying on infected USB drives as a distribution vector to download a rogue MSI installer file that deploys the main payload responsible for facilitating post-exploitation.

Further analysis of Raspberry Robin reveals the use of heavy obfuscation to prevent analysis, with the malware "composed of two payloads embedded in a payload loader packed six times."

The payload loader, for its part, is orchestrated to load the decoy payload, an adware dubbed BrowserAssistant, to throw off detection efforts.

[![Raspberry Robin](data:image/png;base64... "Raspberry Robin")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiU-t5DztcNbK07sZAyny35sjN5BhljqepY-OoQJwvqN1yvv6BSJ-FBPIAGzhoYL0AjtLVrwj7K0jGDgLZ-WfVkTIXBeRF2_rlHWk3KGy5RsYOU_9BCgR0qKFr7pYh-BNqDxmbctXNpc69AS62gkJFBVQ6RwPToRFOMQ_7CFrQhVo_stzFm7sCfdZic/s790-rw-e365/trendmicro.png)

Should no sandboxing and analysis be observed, the legitimate payload is installed and proceeds to connect to a hard-coded .onion address using a custom TOR client embedded within it to await further commands.

The TOR client process masquerades as legitimate Windows processes like dllhost.exe, regsvr32.exe, and rundll32.exe, once again underscoring the considerable efforts made by the threat actor to fly under the radar.

What's more, the malware's real routine is run in [Session 0](https://techcommunity.microsoft.com/t5/ask-the-performance-team/application-compatibility-session-0-isolation/ba-p/372361), a [specialized Windows session](https://techcommunity.microsoft.com/t5/ask-the-performance-team/sessions-desktops-and-windows-stations/ba-p/372473) reserved for services and other non-interactive user applications to mitigate security risks such as [shatter attacks](https://en.wikipedia.org/wiki/Shatter_attack).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Trend Micro said it found similarities in a privilege escalation and an anti-debugging technique used by Raspberry Robin and LockBit ransomware, hinting at a potential connection between the two criminal actors.

"The group behind Raspberry Robin is the maker of some of the tools LockBit is also using," the company theorized, adding it alternatively "availed of the services of the affiliate responsible for the techniques used by LockBit."

That having said, the intrusions appear to be a reconnaissance operation, as no data is returned from the TOR domain, suggesting that the group behind the malware is "testing the waters to see how far its deployments can spread."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)[Raspberry Robin](https://thehackernews.com/search/label/Raspberry%20Robin)[Trend Micro](https://thehackernews.com/search/label/Trend%20Micro)[worm](https://thehackernews.com/search/label/worm)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CV...