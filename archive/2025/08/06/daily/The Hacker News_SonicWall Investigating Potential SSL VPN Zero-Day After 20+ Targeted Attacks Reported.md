---
title: SonicWall Investigating Potential SSL VPN Zero-Day After 20+ Targeted Attacks Reported
url: https://thehackernews.com/2025/08/sonicwall-investigating-potential-ssl.html
source: The Hacker News
date: 2025-08-06
fetch_date: 2025-10-07T00:49:54.666754
---

# SonicWall Investigating Potential SSL VPN Zero-Day After 20+ Targeted Attacks Reported

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

# [SonicWall Investigating Potential SSL VPN Zero-Day After 20+ Targeted Attacks Reported](https://thehackernews.com/2025/08/sonicwall-investigating-potential-ssl.html)

**Aug 05, 2025**Ravie LakshmananZero-Day / Network Security

[![SonicWall SSL VPN Zero-Day](data:image/png;base64... "SonicWall SSL VPN Zero-Day")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPdVjhWPgKWUoYvWQ6R5WXi3t3dfVBkEM1DVg2y0k9Vj48_JSc0dBUh6RmFidVrDQoIWxIlOKIA-q0lCFtVxxe4n4-25jZKeqlEcD_eG0F7dzPyX_tQfGUfHKl6oGpmXLgWPaPJ31_FvWkUi2usxk2ZtE-LMd_MAzc5BVyGrjCdWMNGjn5Q_d4acmWBkzC/s790-rw-e365/sonicwall-zero-day.jpg)

SonicWall said it's actively investigating reports to determine if there is a new zero-day vulnerability following reports of a spike in Akira ransomware actors in late July 2025.

"Over the past 72 hours, there has been a notable increase in both internally and externally reported cyber incidents involving Gen 7 SonicWall firewalls where SSLVPN is enabled," the network security vendor [said](https://www.sonicwall.com/support/notices/gen-7-sonicwall-firewalls-sslvpn-recent-threat-activity/250804095336430) in a statement Monday.

"We are actively investigating these incidents to determine whether they are connected to a previously disclosed vulnerability or if a new vulnerability may be responsible."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While SonicWall is digging deeper, organizations using Gen 7 SonicWall firewalls are advised to follow the steps below until further notice -

* Disable SSL VPN services where practical
* Limit SSL VPN connectivity to trusted IP addresses
* Activate services such as Botnet Protection and Geo-IP Filtering
* Enforce multi-factor authentication
* Remove inactive or unused local user accounts on the firewall, particularly those with SSL VPN access
* Encourage regular password updates across all user accounts

"VPNs are a requirement for many organizations for their employees to access the corporate network, so expecting every customer to disable the service is not viable, but it is the only current way to halt the malicious activity against these devices," Satnam Narang, senior staff research engineer at Tenable, said.

"While the list of additional security actions organizations can take are valuable in lieu of disabling the VPN, it is highly advised that organizations initiate incident response to determine their exposure."

The development comes shortly after Arctic Wolf [revealed](https://thehackernews.com/2025/08/akira-ransomware-exploits-sonicwall.html) it had identified a surge in Akira ransomware activity targeting SonicWall SSL VPN devices for initial access since late last month.

Huntress, in a follow-up analysis published Monday, also said it has observed threat actors pivoting directly to domain controllers merely a few hours after the initial breach.

Attack chains commence with the breach of the SonicWall appliance, followed by the attackers taking a "well-worn" post-exploitation path to conduct enumeration, detection evasion, lateral movement, and credential theft.

The incidents also involve the bad actors methodically disabling Microsoft Defender Antivirus and deleting volume shadow copies prior to deploying Akira ransomware.

Huntress said it detected around 20 different attacks tied to the latest attack wave starting on July 25, 2025, with variations observed in the tradecraft used to pull them off, including in the use of tools for reconnaissance and persistence, such as AnyDesk, ScreenConnect, or SSH.

In a statement shared with The Hacker News, the company said all the identified incidents were related to [Akira ransomware](https://www.acronis.com/en-gb/tru/posts/msps-a-top-target-for-akira-and-lynx-ransomware/), although there were instances where the attackers did not succeed in their efforts.

"Some may have not been successful in fully encrypting the targets, but they gained access and would have most likely tried to encrypt the environment if they had been given the chance," Huntress said. "We know that these actors were Akira related because they operated similarly to what we've seen from them in the past, or there were readme files, or executables directly linking them."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

There is evidence to suggest that the activity may be limited to TZ and NSa-series SonicWall firewalls with SSL VPN enabled, and that the suspected flaw exists in firmware versions 7.2.0-7015 and earlier.

"The speed and success of these attacks, even against environments with MFA enabled, strongly suggest a zero-day vulnerability is being exploited in the wild," the cybersecurity company [said](https://www.huntress.com/blog/exploitation-of-sonicwall-vpn). "This is a critical, ongoing threat."

### Update

In a report published August 5, 2025, GuidePoint Security disclosed that the Akira ransomware actors have leveraged two Windows drivers, rwdrv.sys, a legitimate driver for a Windows performance tuning utility called [ThrottleStop](https://www.techpowerup.com/download/techpowerup-throttlestop/), and hlpdrv.sys, as part of a Bring Your Own Vulnerable Driver (BYOVD) exploitation chain to disarm antivirus (AV) solutions.

"We have observed Akira affiliates registering [rwdrv.sys] as a service and we assess that this driver is used to gain kernel-level access to the impacted device," Jason Baker [said](https://www.guidepointsecurity.com/blog/gritrep-akira-sonicwall/).

"The second driver, hlpdrv.sys, is similarly registered as a service. When executed, it modifies the DisableAntiSpyware settings of Windows Defender within \REGISTRY\MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware. The malware accomplishes this via execution of regedit.exe."

GuidePoint also theorized that the legitimate rwdrv.sys driver may have been utilized by the attackers to facilitate the execution of hlpdrv.sys. However, the exact mechanism used to pull this off rema...