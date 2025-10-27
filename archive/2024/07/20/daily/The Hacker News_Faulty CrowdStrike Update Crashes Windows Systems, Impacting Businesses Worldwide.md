---
title: Faulty CrowdStrike Update Crashes Windows Systems, Impacting Businesses Worldwide
url: https://thehackernews.com/2024/07/faulty-crowdstrike-update-crashes.html
source: The Hacker News
date: 2024-07-20
fetch_date: 2025-10-06T17:45:08.757711
---

# Faulty CrowdStrike Update Crashes Windows Systems, Impacting Businesses Worldwide

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

# [Faulty CrowdStrike Update Crashes Windows Systems, Impacting Businesses Worldwide](https://thehackernews.com/2024/07/faulty-crowdstrike-update-crashes.html)

**Jul 19, 2024**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCd0OiieEqhsfgCpLqSMJi9i34PfDTR8wJst_UcoafjD29g6QFHJT4Ea579Y_ZYNo1nYXZyez4aLC_DQDs_hvpA517u4RA1NxvaW7taf-P-9eK_rA3PrvloNkcUKwX_UVvQxGk-BNEreJfhOpM59b8G06nKrsrh4XFY2xb25wH02l_RZ5hrbBxTxZqaO-a/s790-rw-e365/blue-screen-of-death.png)

Businesses across the world have been hit by widespread disruptions to their Windows workstations stemming from a faulty update pushed out by cybersecurity company CrowdStrike.

"CrowdStrike is actively working with customers impacted by a defect found in a single content update for Windows hosts," the company's CEO George Kurtz [said](https://www.crowdstrike.com/blog/statement-on-windows-sensor-update/) in a [statement](https://x.com/George_Kurtz/status/1814235001745027317). "Mac and Linux hosts are not impacted. This is not a security incident or cyber attack."

The company, which [acknowledged](https://www.reddit.com/r/crowdstrike/comments/1e6vmkf/bsod_error_in_latest_crowdstrike_update/) "reports of [[Blue Screens of Death](https://en.wikipedia.org/wiki/Blue_screen_of_death)] on Windows hosts," further said it has identified the issue and a fix has been deployed for its Falcon Sensor product, urging customers to refer to the support portal for the latest updates.

For systems that have been already impacted by the problem, the mitigation instructions are listed below -

* Boot Windows in Safe Mode or Windows Recovery Environment
* Navigate to the C:\Windows\System32\drivers\CrowdStrike directory
* Find the file named "C-00000291\*.sys" and delete it
* Restart the computer or server normally

It's worth noting that the outage has also impacted Google Cloud Compute Engine, causing Windows virtual machines using CrowdStrike's csagent.sys to crash and go into an unexpected reboot state.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"After having automatically received a defective patch from CrowdStrike, Windows VMs crash and will not be able to reboot," it [said](https://status.cloud.google.com/incidents/DK3LfKowzJPpZq4Q9YqP). "Windows VMs that are currently up and running should no longer be impacted."

Microsoft Azure has also [posted](https://azure.status.microsoft/en-us/status) a [similar update](https://techcommunity.microsoft.com/t5/azure-compute-blog/recovery-options-for-azure-virtual-machines-vm-affected-by/ba-p/4196798), stating it "received reports of successful recovery from some customers attempting multiple Virtual Machine restart operations on affected Virtual Machines" and that "several reboots (as many as 15 have been reported) may be required."

Amazon Web Services (AWS), for its part, [said](https://health.aws.amazon.com/health/status) it has taken steps to mitigate the issue for as many Windows instances, Windows Workspaces, and Appstream Applications as possible, recommending customers still affected by the issue to "take action to restore connectivity."

Security researcher Kevin Beaumont [said](https://x.com/GossiTheDog/status/1814217357058842914) "I have obtained the CrowdStrike driver they pushed via auto update. I don't know how it happened, but the file isn't a validly formatted driver and causes Windows to crash every time."

"CrowdStrike is the top tier EDR product, and is on everything from point-of-sale to ATMs etc. – this will be the biggest 'cyber' incident worldwide ever in terms of impact, most likely."

Airlines, financial institutions, food and retail chains, hospitals, hotels, news organizations, railway networks, and telecom firms are [among](https://www.bbc.com/news/live/cnk4jdwp49et) the [many](https://www.theguardian.com/business/live/2024/jul/19/retail-sales-great-britain-slump-12-government-borrowing-june-figure-lowest-2019-horizon-business-live) [businesses](https://www.nytimes.com/live/2024/07/19/business/global-tech-outage) affected. Shares of CrowdStrike have tanked 15% in U.S. premarket trading.

The Texas-based firm, which serves over 530 companies in the Fortune 1,000, develops endpoint detection and response ([EDR](https://www.microsoft.com/en-us/security/business/security-101/what-is-edr-endpoint-detection-response)) software that are given [entrenched, privileged access](https://www.optiv.com/insights/source-zero/blog/endpoint-detection-and-response-how-hackers-have-evolved) to the operating system's kernel to flag and block security threats. However, this access also gives them wide-ranging powers to disrupt the very systems they are trying to secure.

"The current event appears – even in July – that it will be one of the most significant cyber issues of 2024," Omer Grossman, Chief Information Officer (CIO) at CyberArk, said in a statement shared with The Hacker News. "The damage to business processes at the global level is dramatic. The glitch is due to a software update of CrowdStrike's EDR product."

"This is a product that runs with high privileges that protects endpoints. A malfunction in this can, as we are seeing in the current incident, cause the operating system to crash."

The recovery is expected to take days as the problem needs to be solved manually, endpoint by endpoint, by starting them in Safe Mode and removing the buggy driver, Grossman pointed out, adding the root cause behind the malfunction will be of the "utmost interest."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Jake Moore, global security advisor at Slovakian cybersecurity company ESET, told The Hacker News that the incident serves to highlight the need for implementing multiple "fail safes" in place and diversifying IT infrastructure.

"Upgrades and maintenance to systems and networks can unintentionally include small errors, which can have wide-reaching consequences as experienced today by C...