---
title: Cyber Espionage Group Earth Kitsune Deploys WhiskerSpy Backdoor in Latest Attacks
url: https://thehackernews.com/2023/02/north-korean-cyber-espionage-group.html
source: The Hacker News
date: 2023-02-21
fetch_date: 2025-10-04T07:39:24.873193
---

# Cyber Espionage Group Earth Kitsune Deploys WhiskerSpy Backdoor in Latest Attacks

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

# [Cyber Espionage Group Earth Kitsune Deploys WhiskerSpy Backdoor in Latest Attacks](https://thehackernews.com/2023/02/north-korean-cyber-espionage-group.html)

**Feb 20, 2023**Ravie LakshmananCyber Threat / Cyber Espionage

[![Cyber Espionage](data:image/png;base64... "Cyber Espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgP8EmA64mqJbZdYVLq9nxSVXCI9M2XhAj4c0B8zNMGYUIYYXBrNKIDiJi3DUhZHti-JW1iuWq_hgH_KGkQT_pkqueXKc0WcPMVbLXmAIPg9BotGqpr9xFx0yMyAUyMDgNz_Ar4heB34OmTE4ThPz9VHq3QCC9EcZyyW_oQTKK5EvsbRCGK_sU_s3kC/s790-rw-e365/trend.png)

The cyber espionage threat actor tracked as **Earth Kitsune** has been observed deploying a new backdoor called **WhiskerSpy** as part of a social engineering campaign.

Earth Kitsune, active since at least 2019, is [known](https://thehackernews.com/2020/10/browser-exploit-backdoor.html) to primarily target individuals interested in North Korea with self-developed malware such as dneSpy and agfSpy. Previously documented intrusions have entailed the use of watering holes that leverage browser exploits in Google Chrome and Internet Explorer to activate the infection chain.

The differentiating factor in the latest attacks is a shift toward social engineering to trick users into visiting compromised websites related to North Korea, according to a new report from Trend Micro released last week.

The cybersecurity company said the website of an unnamed pro-North Korean organization was hacked and modified to distribute the WhiskerSpy implant. The compromise was discovered at the end of last year.

"When a targeted visitor tries to watch videos on the website, a malicious script injected by the attacker displays a message prompt notifying the victims with a video codec error to entice them to download and install a trojanized codec installer," researchers Joseph C Chen and Jaromir Horejsi [said](https://www.trendmicro.com/en_us/research/23/b/earth-kitsune-delivers-new-whiskerspy-backdoor.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The booby-trapped script is said to have been injected into the website's video pages, with the installer ("Codec-AVC1.msi") subsequently employed to load WhiskerSpy.

But the attack also exhibits some clever tricks in an attempt to sidestep detection. This involves delivering the malicious script only to those visitors whose IP addresses match specific criteria -

* An IP address subnet located in Shenyang, China
* A specific IP address located in Nagoya, Japan, and
* An IP address subnet located in Brazil

Trend Micro noted that the targeted IP addresses in Brazil belong to a commercial VPN service and that the threat actor may have "used this VPN service to test the deployment of their watering hole attacks."

Persistence is achieved by either [abusing](https://www.bitdefender.com/blog/labs/side-loading-onedrive-for-profit-cryptojacking-campaign-detected-in-the-wild/) a Dynamic Library Link (DLL) hijacking vulnerability in OneDrive or via a malicious Google Chrome extension that employs [native messaging APIs](https://developer.chrome.com/docs/apps/nativeMessaging/) to execute the payload every time the web browser is launched.

[![Cyber Espionage](data:image/png;base64... "Cyber Espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhq5-DjM4brKdcgDtL1bWCs-XXDrT-V7ZNC0XIh6iHmfIaHSB_XY77EQZjr458uJAWQKpAju4Of7qyS-iS9v67JGf2Gz0zDfayH6jDkMZmeu9PM28eUagpJRr3DWJmzoObGO2sIBdqjW7Oi_UqKaBxPQgc52my8MCv6x3fx7EF2bnDzshfFjjKXnAkw/s790-rw-e365/loader.png)

The WhiskerSpy backdoor, like other malware of its kind, comes with capabilities to delete, enumerate, download and upload files, take screenshots, inject shellcode, load arbitrary executables.

"Earth Kitsune are proficient with their technical abilities and are continuously evolving their tools, tactics, and procedures," the researchers said.

### Earth Yako Strikes Academic and Research Sectors in Japan

Earth Kitsune is not the only threat actor to go after Japanese targets, for the cybersecurity company also detailed another intrusion set codenamed **Earth Yako** striking research organizations and think tanks in the country.

The activity, observed as recently as January 2023, is a continuation of a previously known campaign referred to as [Operation RestyLink](https://insight-jp.nttsecurity.com/post/102hojk/operation-restylink-apt-campaign-targeting-japanese-companies). A subset of the attacks also targeted entities located in Taiwan.

"The intrusion set introduced new tools and malware within a short period of time, frequently changing and expanding its attack targets," Trend Micro [said](https://www.trendmicro.com/en_us/research/23/b/invitation-to-secret-event-uncovering-earth-yako-campaigns.html), pointing out Earth Yako's modus operandi of "actively changing their targets and methods."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The starting point is a spear-phishing email that masquerades as invitations to public events. The messages contain a malicious URL that points to a payload, which, in turn, is responsible for downloading the malware onto the system.

The attacks are also characterized by a trove of custom tools comprising droppers (PULink), loaders (Dulload, MirrorKey), stagers (ShellBox), and backdoors (PlugBox, TransBox).

PlugBox, ShellBox, and TransBox, as the names imply, take advantage of Dropbox APIs to retrieve next-stage malware from a remote server hard-coded in a GitHub repository, receive commands, and harvest and exfiltrate data.

The exact origins of Earth Yako remain unknown, but Trend Micro said it identified partial technical overlaps between the group and other threat actors like Darkhotel, APT10 (aka Stone Panda), and APT29 (aka Cozy Bear or Nobelium).

"One of the characteristics of the recent targeted attacks is that they shifted to targeting the individuals considered to have relatively weak security measures compared to companies and other organiza...