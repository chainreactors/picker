---
title: GhostRedirector Hacks 65 Windows Servers Using Rungan Backdoor and Gamshen IIS Module
url: https://thehackernews.com/2025/09/ghostredirector-hacks-65-windows.html
source: The Hacker News
date: 2025-09-05
fetch_date: 2025-10-02T19:42:39.476312
---

# GhostRedirector Hacks 65 Windows Servers Using Rungan Backdoor and Gamshen IIS Module

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

# [GhostRedirector Hacks 65 Windows Servers Using Rungan Backdoor and Gamshen IIS Module](https://thehackernews.com/2025/09/ghostredirector-hacks-65-windows.html)

**Sep 04, 2025**Ravie LakshmananData Breach / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJ9IxdheAfdLi4r8N_NZGNOTpgrIWFuvh0Gh-_rLJEl-1XhzvEtJ2kvybXam97uORiVJCETWwLeu8LiDvvEOvyJ3ifKElUuDcCEhEZMsH1vsIULD7OFKUPFwun2c2k7qMDPwRFiLPO4NtH3y1ivu6neuIITw1a67PnQHxgAn1yRnEdZsUSK1wVTPJ5b0a7/s790-rw-e365/cyberattack.jpg)

Cybersecurity researchers have lifted the lid on a previously undocumented threat cluster dubbed **GhostRedirector** that has managed to compromise at least 65 Windows servers primarily located in Brazil, Thailand, and Vietnam.

The attacks, per Slovak cybersecurity company ESET, led to the deployment of a passive C++ backdoor called Rungan and a native Internet Information Services (IIS) module codenamed Gamshen. The threat actor is believed to be active since at least August 2024.

"While Rungan has the capability of executing commands on a compromised server, the purpose of Gamshen is to provide SEO fraud as-a-service, i.e., to manipulate search engine results, boosting the page ranking of a configured target website," ESET researcher Fernando Tavella [said](https://www.welivesecurity.com/en/eset-research/ghostredirector-poisons-windows-servers-backdoors-side-potatoes/) in a report shared with The Hacker News.

"Even though Gamshen only modifies the response when the request comes from Googlebot – i.e., it does not serve malicious content or otherwise affect regular visitors of the websites – participation in the SEO fraud scheme can hurt the compromised host website's reputation by associating it with shady SEO techniques and the boosted websites."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the other targets of the hacking group include Peru, the U.S., Canada, Finland, India, the Netherlands, the Philippines, and Singapore. The activity is also said to be indiscriminate, with entities in the education, healthcare, insurance, transportation, technology, and retail sectors singled out.

Initial access to target networks is accomplished by exploiting a vulnerability, likely an SQL injection flaw, after which PowerShell is used to deliver additional tools hosted on a staging server ("868id[.]com").

"This conjecture is supported by our observation that most unauthorized PowerShell executions originated from the binary sqlserver.exe, which holds a stored procedure [xp\_cmdshell](https://thehackernews.com/2023/09/threat-actors-targeting-microsoft-sql.html) that can be used to execute commands on a machine," ESET said.

Rungan is designed to await incoming requests from a URL matching a predefined pattern (i.e., "https://+:80/v1.0/8888/sys.html"), and then proceeds to parse and execute the commands embedded in them. It supports four different commands -

* mkuser, to create a user on the server with the username and password provided
* listfolder, to collect information from a provided path (unfinished)
* addurl, to register new URLs that the backdoor can listen on
* cmd, to run a command on the server using pipes and the [CreateProcessA](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) API

Written in C/C++, Gamshen is an example of an [IIS malware](https://www.splunk.com/en_us/blog/security/sharepoint-exploits-and-the-hidden-threat-of-iis-module-persistence.html) family called "[Group 13](https://thehackernews.com/2021/08/several-malware-families-targeting-iis.html)," which can act both as a backdoor and conduct SEO fraud. It functions similar to IISerpent, another IIS-specific malware that was documented by ESET back in August 2021.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7067xKwlfuUPZAkhUBQVgDvudAw9AMVK-mN9R-M3-Py08lNBGhChmYbA_0SzYjkDQmrgdp0ee6zDHof1rEW4z-QTCVscchGPzmLYAI_9AkW6Q84wZUe0Njn8tNaZMqMPRysnwCWANnnm7bmv2gKW3zzQOCron-apUqkyJAnT6tAz0Aj-ijdhUfzASybyr/s790-rw-e365/web-malware.jpg)

[IISerpent](https://www.welivesecurity.com/2021/08/11/iiserpent-malware-driven-seo-fraud-service/), configured as a malicious extension for Microsoft's web server software, allows it to intercept all HTTP requests made to the websites hosted by the compromised server, specifically those originating from search engine crawlers, and change the server's HTTP responses with the goal of redirecting the search engines to a scam website of the attacker's choosing.

That IIS extensions can covertly open persistent backdoors into servers was acknowledged by Microsoft back way back in July 2022, [stating](https://www.microsoft.com/en-us/security/blog/2022/07/26/malicious-iis-extensions-quietly-open-persistent-backdoors-into-servers/) they are also "harder to detect since they mostly reside in the same directories as legitimate modules used by target applications, and they follow the same code structure as clean modules."

"GhostRedirector attempts to manipulate the Google search ranking of a specific, third-party website by using manipulative, shady SEO techniques such as creating artificial backlinks from the legitimate, compromised website to the target website," Tavella said.

It's currently not known where these backlinks redirect unsuspecting users to, but it's believed that the SEO fraud scheme is being used to promote various gambling websites.

Also dropped alongside Rungan and Gamshen are various other tools -

* GoToHTTP to establish a remote connection that's accessible from a web browser
* BadPotato or EfsPotato for creating a privileged user in the Administrators group
* Zunput to collect information about websites hosted on the IIS server and drop ASP, PHP, and JavaScript web shells

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's assessed with medium confidence that GhostRedirector is a China-align...