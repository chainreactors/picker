---
title: Employees Searching Payroll Portals on Google Tricked Into Sending Paychecks to Hackers
url: https://thehackernews.com/2025/05/employees-searching-payroll-portals-on.html
source: The Hacker News
date: 2025-05-28
fetch_date: 2025-10-06T22:31:23.630395
---

# Employees Searching Payroll Portals on Google Tricked Into Sending Paychecks to Hackers

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

# [Employees Searching Payroll Portals on Google Tricked Into Sending Paychecks to Hackers](https://thehackernews.com/2025/05/employees-searching-payroll-portals-on.html)

**May 27, 2025**Ravie LakshmananMalware / Mobile Security

[![Payroll Portals on Google](data:image/png;base64... "Payroll Portals on Google")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAA4c9t3UoyrhYNZes6PD7HQodaHqBMHEw3xCTE9RJwmxL37DbTGfqnZmVN7GwZPKv7tKL966OHAXcg7_RcQ_4YYzI0fz4msBUUaArVfH9eMtJHdxtDkXlQUjfgXDp2J45GFJhBs_vvuEOFIynULPBf1pcR33fUNdlHHBsnqZSufGKmfAyxME9WsMXUtMD/s790-rw-e365/google.jpg)

Threat hunters have exposed a novel campaign that makes use of search engine optimization (SEO) poisoning techniques to target employee mobile devices and facilitate payroll fraud.

The activity, first detected by ReliaQuest in May 2025 targeting an unnamed customer in the manufacturing sector, is characterized by the use of fake login pages to access the employee payroll portal and redirect paychecks into accounts under the threat actor's control.

"The attacker's infrastructure used compromised home office routers and mobile networks to mask their traffic, dodging detection and slipping past traditional security measures," the cybersecurity company [said](https://reliaquest.com/blog/threat-spotlight-payroll-fraud-attackers-stealing-paychecks-seo-poisoning/) in an analysis published last week.

"The adversary specifically targeted employee mobile devices with a fake website impersonating the organization's login page. Armed with stolen credentials, the adversary gained access to the organization's payroll portal, changed direct deposit information, and redirected employees' paychecks into their own accounts."

While the attacks have not been attributed to a specific hacking group, ReliaQuest said it's part of a broader, ongoing campaign owing to two similar incidents it investigated in late 2024.

It all starts when an employee searches for their company's payroll portal on search engines like Google, with deceptive lookalike websites surfacing to the top of the results using sponsored links. Those who end up clicking on the bogus links are led to a WordPress site that redirects to a phishing page mimicking a Microsoft login portal when visited from a mobile device.

The credentials entered on the fake landing page are subsequently exfiltrated to an attacker-controlled website, while also establishing a two-way WebSocket connection in order to alert the threat actor of stolen passwords using a push notifications API powered by [Pusher](https://pusher.com).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This gives attackers an opportunity to reuse the credentials as soon as possible before they are changed and gain unauthorized access to the payroll system.

On top of that, the targeting of employee mobile devices offers twofold advantages in that they lack enterprise-grade security measures typically available in desktop computers and they connect outside of the corporate network, effectively reducing visibility and hampering investigation efforts.

"By targeting unprotected mobile devices that lack security solutions and logging, this tactic not only evades detection but also disrupts efforts to analyze the phishing website," ReliaQuest said. "This prevents security teams from scanning the site and adding it to indicators of compromise (IOC) threat feeds, further complicating mitigation efforts."

In a further attempt to sidestep detection, the malicious login attempts have been found to originate from residential IP addresses associated with home office routers, including those from brands like ASUS and Pakedge.

This indicates that the threat actors are exploiting weaknesses like security flaws, default credentials, or other misconfigurations often plaguing such network devices to launch brute-force attacks. Compromised routers are then infected with malware that enlists them into [proxy botnets](https://thehackernews.com/2025/05/breaking-7000-device-proxy-botnet-using.html), which are eventually rented out to cybercriminals.

"When attackers use proxy networks, especially ones tied to residential or mobile IP addresses, they become much harder for organizations to detect and investigate," ReliaQuest said. "Unlike VPNs, which are often flagged because their IP addresses have been abused before, residential or mobile IP addresses let attackers fly under the radar and avoid being classified as malicious."

"What's more, proxy networks allow attackers to make their traffic look like it originates from the same geographical location as the target organization, bypassing security measures designed to flag logins from unusual or suspicious locations."

The disclosure comes as Hunt.io [detailed](https://hunt.io/blog/phishing-kit-targets-outlook-credentials) a phishing campaign that employs a fake Adobe Shared File service web page to steal Microsoft Outlook login credentials under the pretext of allowing access to files purportedly shared by a contact. The pages, per the company, are developed using the [W3LL phishing kit](https://thehackernews.com/2025/01/new-sneaky-2fa-phishing-kit-targets.html).

It also coincides with the discovery of a new phishing kit codenamed CoGUI that's being used to actively target Japanese organizations by impersonating well-known consumer and finance brands such as Amazon, PayPay, MyJCB, Apple, Orico, and Rakuten. As many as 580 million emails have been sent between January and April 2025 as part of campaigns using the kit.

"CoGUI is a sophisticated kit that employs advanced evasion techniques, including geofencing, headers fencing, and fingerprinting to avoid detection from automated browsing systems and sandboxes," enterprise security firm Proofpoint [said](https://www.proofpoint.com/us/blog/threat-insight/cogui-phish-kit-targets-japan-millions-messages) in an analysis released this month. "The objective of the campaigns is to steal usernames, passwords, and payment ...