---
title: Researchers Uncover Years-Long Cyber Espionage on Foreign Embassies in Belarus
url: https://thehackernews.com/2023/08/researchers-uncover-decade-long-cyber.html
source: The Hacker News
date: 2023-08-12
fetch_date: 2025-10-04T12:03:41.412496
---

# Researchers Uncover Years-Long Cyber Espionage on Foreign Embassies in Belarus

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

# [Researchers Uncover Years-Long Cyber Espionage on Foreign Embassies in Belarus](https://thehackernews.com/2023/08/researchers-uncover-decade-long-cyber.html)

**Aug 11, 2023**Ravie LakshmananCyber Espionage / Malware

[![Cyber Espionage Campaign](data:image/png;base64... "Cyber Espionage Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhotMoFS2JqMGDnGRDU7jMvbpG6vsA7jmIZ7ZMJX3XaodFfNAZirhJYqlldC-7L8sEz37b9CGAOSh8ewWl89q9ayC6xSiYmqoUGf69SqjCN4fBBZ-Q7Yu47z8lz_ALLDDlSPYCW0Xt9xQXSkdiDjAPMZDKnKnhPagoKZiKUu9coWXWYOFJXZJLVG3W3Tn6x/s790-rw-e365/hacking.jpg)

A hitherto undocumented threat actor operating for nearly a decade and codenamed **MoustachedBouncer** has been attributed to cyber espionage attacks aimed at foreign embassies in Belarus.

"Since 2020, MoustachedBouncer has most likely been able to perform adversary-in-the-middle (AitM) attacks at the ISP level, within Belarus, in order to compromise its targets," ESET security researcher Matthieu Faou [said](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/), describing the group as skilled and advanced.

The adversary, active since at least 2014, is assessed to be aligned with Belarusian interests, likely employing a lawful interception system such as [SORM](https://www.theverge.com/2016/7/6/12107092/belarus-surveillance-encryption-amnesty-international) to conduct its AitM attacks as well as deploy disparate tools called NightClub and Disco.

Both the Windows malware frameworks support additional spying plugins including a screenshotter, an audio recorder, and a file stealer. The oldest sample of NightClub dates back to November 19, 2014, when it was uploaded to VirusTotal from Ukraine.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Embassy staff from four different countries have been targeted since June 2017: two from Europe, one from South Asia, and one from Northeast Africa. One of the European diplomats was compromised twice in November 2020 and July 2022. The names of the countries were not revealed.

MoustachedBouncer is also believed to work closely with another advanced persistent threat (APT) actor known as [Winter Vivern](https://thehackernews.com/2023/03/winter-vivern-apt-targets-european.html) (aka TA473 or UAC-0114), which has a track record of striking government officials in Europe and the U.S.

The exact initial infection vector used to deliver NightClub is presently unknown. The distribution of Disco, on the other hand, is accomplished by means of an AitM attack.

"To compromise their targets, MoustachedBouncer operators tamper with their victims' internet access, probably at the ISP level, to make Windows believe it's behind a [captive portal](https://en.wikipedia.org/wiki/Captive_portal)," Faou said. "For IP ranges targeted by MoustachedBouncer, the network traffic is tampered at the ISP level, and the latter URL redirects to a seemingly legitimate, but fake, Windows Update URL."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk8PtszeiafwktPUZg7_afwIk1LesVk5GsY9TCk5ds9hqKrcx-moDxDxhnutxVqW-LXFH8phCrZcweq_jakf2IJGq1jqKklabboo8oyGnKAFPD7Y0ft-QSI9YKvkXJxI7fDZu0AlSQk_mflZDw21mNiIx2n5H2eebnIj6HpiXEjCkjiUjFg_PKltjfbcWI/s790-rw-e365/timeline.jpg)

"While the compromise of routers in order to conduct AitM on embassy networks cannot be fully discarded, the presence of lawful interception capabilities in Belarus suggests the traffic mangling is happening at the ISP level rather than on the targets' routers," Fou said.

Two Belarusian internet service providers (ISPs), viz Unitary Enterprise A1 and Beltelecom, are suspected to be involved in the campaign, per the Slovak cybersecurity company.

Victims who land on the bogus page are greeted with a message urging them to install critical security updates by clicking on a button. In doing so, a rogue Go-based "Windows Update" installer is downloaded to the machine that, when executed, sets up a scheduled task to run another downloader binary responsible for fetching additional plugins.

The add-ons expand on Disco's functionality by capturing screenshots every 15 seconds, executing PowerShell scripts, and setting up a reverse proxy.

A significant aspect of the plugins is the use of the Server Message Block ([SMB](https://en.wikipedia.org/wiki/Server_Message_Block)) protocol for data exfiltration to command-and-control servers that are inaccessible over the internet, making the threat actor's infrastructure highly resilient.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also used in the January 2020 attack aimed at diplomats of a Northeast African country in Belarus is a C# dropper referred to as SharpDisco, which facilitates the deployment of two plugins by means of a reverse shell in order to enumerate connected drives and exfiltrate files.

The NightClub framework also comprises a dropper that, in turn, launches an orchestrator component to harvest files of interest and transmit them over the Simple Mail Transfer Protocol ([SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)). Subsequent iterations of NightClub unearthed in 2017 and 2020 also incorporate a keylogger, audio recorder, screenshotter, and a DNS-tunneling backdoor.

"The DNS-tunneling backdoor (ParametersParserer.dll) uses a custom protocol to send and receive data from a malicious DNS server," Faou explained. "The plugin adds the data to exfiltrate as part of the subdomain name of the domain that is used in the DNS request."

The commands supported by the modular implant allow the threat actor to search for files matching a specific pattern, read, copy, and remove files, write to files, copy directories, and create arbitrary processes.

It's believed that NightClub is used in scenarios where traffic interception at the ISP level isn't possible because of anonymity-boosting mitigations such as the use of an end-to-e...