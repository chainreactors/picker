---
title: New Cyberattack Targets Chinese-Speaking Businesses with Cobalt Strike Payloads
url: https://thehackernews.com/2024/08/new-cyberattack-targets-chinese.html
source: The Hacker News
date: 2024-08-31
fetch_date: 2025-10-06T18:12:57.149396
---

# New Cyberattack Targets Chinese-Speaking Businesses with Cobalt Strike Payloads

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

# [New Cyberattack Targets Chinese-Speaking Businesses with Cobalt Strike Payloads](https://thehackernews.com/2024/08/new-cyberattack-targets-chinese.html)

**Aug 30, 2024**Ravie LakshmananCyber Espionage / Threat Intelligence

[![Cobalt Strike Payloads](data:image/png;base64... "Cobalt Strike Payloads")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7PUbwqT9X9WjONn09hHtsNvtLKUEBE1HerAB7PtK0JuCClv6nm7l3CKrhaWe-LQDEj0zV7eU8DjutbIMs5U2uQWfLXYCl5Y0MBeoaVAg4ji7KNq6Z8pKLgdo6OxNDleZ0dTeUs020v68v0k-1N5_C1L5w2m5FIfko6BNyUeicHzwHgrWPK-EZjzyz7Jx3/s790-rw-e365/malware.png)

Chinese-speaking users are the target of a "highly organized and sophisticated attack" campaign that is likely leveraging phishing emails to infect Windows systems with Cobalt Strike payloads.

"The attackers managed to move laterally, establish persistence and remain undetected within the systems for more than two weeks," Securonix researchers Den Iuzvyk and Tim Peck [said](https://www.securonix.com/blog/from-cobalt-strike-to-mimikatz-slowtempest/) in a new report.

The covert campaign, codenamed **SLOW#TEMPEST** and not attributed to any known threat actor, commences with malicious ZIP files that, when unpacked, activates the infection chain, leading to the deployment of the post-exploitation toolkit on compromised systems.

Present with the ZIP archive is a Windows shortcut (LNK) file that disguises itself as a Microsoft Word file, "违规远程控制软件人员名单.docx.lnk," which roughly translates to "List of people who violated the remote control software regulations."

"Given the language used in the lure files, it's likely that specific Chinese related business or government sectors could be targeted as they would both employ individuals who follow 'remote control software regulations,'" the researchers pointed out.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The LNK file acts as a conduit to launch a legitimate Microsoft binary ("LicensingUI.exe") that employs [DLL side-loading](https://cloud.google.com/blog/topics/threat-intelligence/abusing-dll-misconfigurations) to execute a rogue DLL ("dui70.dll"). Both the files are part of the ZIP archive within a directory called "\其他信息\.\_\_MACOS\_\_\.\_MACOS\_\\_\_MACOSX\\_MACOS\_." The attack marks the first time DLL side-loading via LicensingUI.exe has been reported.

The DLL file is a Cobalt Strike implant that allows for persistent and stealthy access to the infected host, while establishing contact with a remote server ("123.207.74[.]22").

The remote access is said to have allowed the attackers to conduct a series of hands-on activities, including deploying additional payloads for reconnaissance and setting up proxied connections.

The infection chain is also notable for setting up a scheduled task to periodically execute a malicious executable called "lld.exe" that can run arbitrary shellcode directly in memory, thereby leaving minimal footprints on disk.

[![Cobalt Strike Payloads](data:image/png;base64... "Cobalt Strike Payloads")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-yQJZnOpOzQkxC07wMC21bLulW1xfjhEAIf5HhT0rNXOYYbmm21S1SY7n6HByYyDp8LiopGvpgOFHBbLpJ14ssG6Z6Rfc5kq1KHvKd2cfHRkFriLgXuq16ZEXdG3fFDEHMqCAjoppd8X9VHLVhkTqLB176cv0915G1CTsyx29LpAydNLuj5Hur69nauzt/s790-rw-e365/code.png)

"The attackers further enabled themselves to hide in the weeds in compromised systems by manually elevating the privileges of the built-in Guest user account," the researchers said.

"This account, typically disabled and minimally privileged, was transformed into a powerful access point by adding it to the critical administrative group and assigning it a new password. This backdoor allows them to maintain access to the system with minimal detection, as the Guest account is often not monitored as closely as other user accounts."

The unknown threat actor subsequently proceeded to move laterally across the network using Remote Desktop Protocol ([RDP](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/understanding-remote-desktop-protocol)) and credentials obtained via the Mimikatz password extraction tool, followed by setting up remote connections back to their command-and-control (C2) server from each of those machines.

The post-exploitation phase is further characterized by the execution of several enumeration commands and the use of the BloodHound tool for active directory (AD) reconnaissance, the results of which were then exfiltrated in the form of a ZIP archive.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The connections to China are reinforced by the fact that all of the C2 servers are hosted in China by Shenzhen Tencent Computer Systems Company Limited. On top of that, a majority of the artifacts connected with the campaign have originated from China.

"Although there was no solid evidence linking this attack to any known APT groups, it is likely orchestrated by a seasoned threat actor who had experience using advanced exploitation frameworks such as Cobalt Strike and a wide range of other post-exploitation tools," the researchers concluded.

"The campaign's complexity is evident in its methodical approach to initial compromise, persistence, privilege escalation and lateral movement across the network."

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
[**Share on Wh...