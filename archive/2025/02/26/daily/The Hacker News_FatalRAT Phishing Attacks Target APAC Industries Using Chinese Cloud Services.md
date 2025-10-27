---
title: FatalRAT Phishing Attacks Target APAC Industries Using Chinese Cloud Services
url: https://thehackernews.com/2025/02/fatalrat-phishing-attacks-target-apac.html
source: The Hacker News
date: 2025-02-26
fetch_date: 2025-10-06T20:50:22.509746
---

# FatalRAT Phishing Attacks Target APAC Industries Using Chinese Cloud Services

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

# [FatalRAT Phishing Attacks Target APAC Industries Using Chinese Cloud Services](https://thehackernews.com/2025/02/fatalrat-phishing-attacks-target-apac.html)

**Feb 25, 2025**Ravie LakshmananCybercrime / Malware

[![Chinese Cloud Services](data:image/png;base64... "Chinese Cloud Services")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijEPgWIgmZOPhRpJpO17A9tuCmDGJqHlvkpjT828S-axryaRv-1xzma5pPWZrWuPNVhmS4-omFv-BOR7jEuTOs0NbY8HLs3DQshrEkUONBepfSz3hp0arv1D8SfBCoZbEjz0Zo-pcpHYYC2_e6euubSGXkIAQ6wUjbr5h62py9ATt5Jlhk0_YdCJD1jQlN/s790-rw-e365/malware.png)

Various industrial organizations in the Asia-Pacific (APAC) region have been targeted as part of phishing attacks designed to deliver a known malware called FatalRAT.

"The threat was orchestrated by attackers using legitimate Chinese cloud content delivery network (CDN) myqcloud and the Youdao Cloud Notes service as part of their attack infrastructure," Kaspersky ICS CERT [said](https://ics-cert.kaspersky.com/publications/reports/2025/02/24/fatalrat-attacks-in-apac-backdoor-delivered-via-an-overly-long-infection-chain-to-chinese-speaking-targets/) in a Monday report.

"The attackers employed a sophisticated multi-stage payload delivery framework to ensure evasion of detection."

The activity has singled out government agencies and industrial organizations, particularly manufacturing, construction, information technology, telecommunications, healthcare, power and energy, and large-scale logistics and transportation, in Taiwan, Malaysia, China, Japan, Thailand, South Korea, Singapore, the Philippines, Vietnam, and Hong Kong.

The lure attachments used in the email messages suggest that the phishing campaign, dubbed Operation SalmonSlalom, is designed to go after Chinese-speaking individuals.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth noting that [FatalRAT](https://levelblue.com/blogs/labs-research/new-sophisticated-rat-in-town-fatalrat-analysis) campaigns have [previously leveraged](https://thehackernews.com/2023/02/hackers-using-google-ads-to-spread.html) bogus Google Ads as a distribution vector. In September 2023, Proofpoint [documented](https://thehackernews.com/2023/09/sophisticated-phishing-campaign_20.html) another email phishing campaign that propagated various malware families such as FatalRAT, Gh0st RAT, Purple Fox, and ValleyRAT.

An interesting aspect of both intrusion sets is that they have primarily targeted Chinese-language speakers and Japanese organizations. Some of these activities have been attributed to a threat actor tracked as [Silver Fox APT](https://thehackernews.com/2025/02/fake-google-chrome-sites-distribute.html).

The starting point of the latest attack chain is a phishing email containing a ZIP archive with a Chinese-language filename, which, when launched, launches the first-stage loader that, in turn, makes a request to Youdao Cloud Notes in order to retrieve a DLL file and a FatalRAT configurator.

For its part, the configurator module downloads the contents of another note from note.youdao[.]com so as to access the configuration information. It's also engineered to open a decoy file in an effort to avoid raising suspicion.

The DLL, on the other hand, is a second-stage loader that's responsible for downloading and installing the FatalRAT payload from a server ("myqcloud[.]com") specified in the configuration, while displaying a fake error message about a problem running the application.

An important hallmark of the campaign includes the use of DLL side-loading techniques to advance the multi-stage infection sequence and load the FatalRAT malware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMcSZbK4W10tFS06P56_Hv4bl_1i425dnuaS0HbXFhJBzMws2FcUaCz40GKSz0dVBOK19pMCg6PhV5r06gsW86p9FSOkkmLd23rShYHNOlXA8fwTHdlntOVOiOGebKST_b_QV068L09Bj5QAb4cKOAMvFVF5edh4k9oZZatsLoWSDy07yGsFIYqsrqhTD/s790-rw-e365/malware.png)

"The threat actor uses a black and white method where the actor leverages the functionality of legitimate binaries to make the chain of events look like normal activity," Kaspersky said. "The attackers also used a DLL side-loading technique to hide the persistence of the malware in legitimate process memory."

"FatalRAT performs 17 checks for an indicator that the malware executes in a virtual machine or sandbox environment. If any of the checks fail, the malware stops executing."

It also terminates all instances of the rundll32.exe process, and gathers information about the system and the various security solutions installed in it, before awaiting further instructions from a command-and-control (C2) server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

FatalRAT is a feature-packed trojan that's equipped to log keystrokes, corrupt Master Boot Record (MBR), turn on/off screen, search and delete user data in browsers like Google Chrome and Internet Explorer, download additional software like AnyDesk and UltraViewer, perform file operations, and start/stop a proxy, and terminate arbitrary processes.

It's currently not known who is behind the attacks using FatalRAT, although the tactical and instrumentation overlaps with other campaigns suggest that "they all reflect different series of attacks that are somehow related." Kaspersky has assessed with medium confidence that a Chinese-speaking threat actor is behind it.

"FatalRAT's functionality gives an attacker almost unlimited possibilities for developing an attack: spreading over a network, installing remote administration tools, manipulating devices, stealing, and deleting confidential information," the researchers said.

"The consistent use of services and interfaces in Chinese at various stages of the attack, as well as other indirect evidence, indicates that a Chinese-speaking actor may be involved."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWF...