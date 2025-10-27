---
title: Horns&Hooves Campaign Delivers RATs via Fake Emails and JavaScript Payloads
url: https://thehackernews.com/2024/12/horns-campaign-delivers-rats-via-fake.html
source: The Hacker News
date: 2024-12-04
fetch_date: 2025-10-06T19:42:05.732357
---

# Horns&Hooves Campaign Delivers RATs via Fake Emails and JavaScript Payloads

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

# [Horns&Hooves Campaign Delivers RATs via Fake Emails and JavaScript Payloads](https://thehackernews.com/2024/12/horns-campaign-delivers-rats-via-fake.html)

**Dec 03, 2024**Ravie LakshmananMalware / Phishing Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijwTYvrTy-wRJMNdlnDR8sjf5GsmLg7XgmDl5qe7WqwwBHQoLzHN0yviyqbjw2N64Ks-mLNgwi6YMifcE_l8Y5puNqcNT2X7Y_pPfurBrb3I4VBA5JZbAXdU9p_2Wi6xCYNEfupc0JbmL8stSwNNNoTNdLiQmexJW7tZrhkWide3AoJu1Moy2oZJmSHIXg/s790-rw-e365/malware.png)

A newly discovered malware campaign has been found to target private users, retailers, and service businesses mainly located in Russia to deliver [NetSupport RAT](https://thehackernews.com/2023/11/netsupport-rat-infections-on-rise.html) and BurnsRAT.

The campaign, dubbed **Horns&Hooves** by Kaspersky, has hit more than 1,000 victims since it began around March 2023. The end goal of these attacks is to leverage the access afforded by these trojans to install stealer malware such as [Rhadamanthys](https://thehackernews.com/2024/10/ai-powered-rhadamanthys-stealer-targets.html) and [Meduza](https://thehackernews.com/2023/07/evasive-meduza-stealer-targets-19.html).

"Recent months have seen a surge in mailings with lookalike email attachments in the form of a ZIP archive containing JScript scripts," security researcher Artem Ushkov [said](https://securelist.com/horns-n-hooves-campaign-delivering-netsupport-rat/114740/) in a Monday analysis. "The script files [are] disguised as requests and bids from potential customers or partners."

The threat actors behind the operations have demonstrated their active development of the JavaScript payload, making significant changes during the course of the campaign.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In some instances, the ZIP archive has been found to contain other documents related to the organization or individual being impersonated so as to increase the likelihood of success of the phishing attack and dupe recipients into opening the malware-laced file.

One of the earliest samples identified as part of the campaign is an HTML Application (HTA) file that, when run, downloads a decoy PNG image from a remote server using the curl utility for Windows, while also stealthily retrieving and running another script ("bat\_install.bat") from a different server using the [BITSAdmin](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin-transfer) command-line tool.

The newly downloaded script then proceeds to fetch using BITSAdmin several other files, including the NetSupport RAT malware, which establishes contact with a command-and-control (C2) server set up by the attackers.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRXtHOwutmoaptsEifa1HEnUV4tBl21DZPbNNfmbzTXwQYKchO91ZY6BpyDM0H5ulWIQYnNXjCCrZ9Y3mgST7ll_iXcuhqhT-qMcNQmVv7VYEWAoZD2kPMfXhb4rWSOZdyYGDIpJlPUYsFZ3HbMy7zZwjwwdXZ4DUtxp1Z1jR7OX4JkkHxVL79GFw6AldY/s790-rw-e365/emails.png)

A subsequent iteration of the campaign observed in mid-May 2023 involved the intermediate JavaScript mimicking legitimate JavaScript libraries like Next.js to activate the NetSupport RAT infection chain.

Kaspersky said it also found another variant of the JavaScript file that dropped an NSIS installer that's then responsible for deploying BurnsRAT on the compromised host.

"Although the backdoor supports commands for remotely downloading and running files, as well as various methods of executing commands via the Windows command line, the main task of this component is to start the Remote Manipulator System ([RMS](https://www.fortiguard.com/appcontrol/46612)) as a service and send the RMS session ID to the attackers' server," Ushkov explained.

"RMS is an application that allows users to interact with remote systems over a network. It provides the ability to manage the desktop, execute commands, transfer files and exchange data between devices located in different geographic locations."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a sign that the threat actors continued to tweak their modus operandi, two other attack sequences spotted in late May and June 2023 came with a completely reworked BAT file for installing NetSupport RAT and incorporated the malware directly within the JavaScript code, respectively.

There are indications that the campaign is the work of a threat actor known as [TA569](https://thehackernews.com/2023/11/clearfake-campaign-expands-to-deliver.html) (aka Gold Prelude, Mustard Tempest, and Purple Vallhund), which is known for operating the [SocGholish](https://thehackernews.com/2024/07/socgholish-malware-exploits-boinc.html) (aka FakeUpdates) malware. This connection stems from overlaps in the NetSupport RAT license and configuration files used in respective activities.

It's worth mentioning that TA569 has also been known to [act as an initial access broker](https://thehackernews.com/2021/06/ransomware-attackers-partnering-with.html) for follow-on ransomware attacks such as WastedLocker.

"Depending on whose hands this access falls into, the consequences for victim companies can range from data theft to encryption and damage to systems," Ushkov said. "We also observed attempts to install stealers on some infected machines."

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
[**Share on...