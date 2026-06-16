---
title: Chinese Hackers Abused Google Workspace Rules to Steal Research and Defense Emails
url: https://thehackernews.com/2026/06/chinese-hackers-abused-google-workspace.html
source: The Hacker News
date: 2026-06-15
fetch_date: 2026-06-16T07:17:03.142640
---

# Chinese Hackers Abused Google Workspace Rules to Steal Research and Defense Emails

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Chinese Hackers Abused Google Workspace Rules to Steal Research and Defense Emails](https://thehackernews.com/2026/06/chinese-hackers-abused-google-workspace.html)

**Swati Khandelwal**Jun 15, 2026Cyber Espionage / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjE7EMoBrh5-6_V336v7LMFfChDVp-Sux8RX-UY5zhONtACR6kiz2w_VQ9o7e8nuqaWCqbxrvzPgSrruvEXN0jw_zKnaeVl73yDnfqbVqTPDnjHDPJPuBLd9vhGCJIl1BuqSblleOG9zG9YgbriqE7oiCuTEBQRDadsFOgQdN9PjdOglDeI_y2ZV5-Ehbo/s1700-e365/google-china.jpg)

A China-linked espionage group hid inside North American medical, academic, and military research networks for more than a year, quietly stealing sensitive research and defense email.

The way in was a backdoor on their **REDCap** research servers that stole login credentials. The exfiltration was the unusual part: the attackers rewired the victims' own Google Workspace rules to copy any message matching their keywords to an inbox they controlled.

Google's Threat Intelligence Group (GTIG) laid out the campaign in a [report](https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research) published this week and attributes it with high confidence to a cluster it tracks as UNC6508.

The actor and its REDCap backdoor are not new names; Google [first surfaced both in February](https://thehackernews.com/2026/02/google-links-china-iran-russia-north.html), in a wider report on state-backed attacks against the defense sector. It did not name the victims, describing them only as multiple organizations across the US and Canada: clinical providers, academic centers, military health institutions, advocacy groups, and health regulators.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Google says it notified them and disrupted the group's infrastructure.

## How they got in

The entry point was [REDCap](https://www.project-redcap.org/) (Research Electronic Data Capture), a web platform that hospitals and universities use to build and manage study databases. UNC6508 compromised externally facing REDCap servers.

Google has not pinned down the initial access vector, named a specific CVE, or listed the affected versions, though it saw the group probing older, vulnerable ones.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglqcg8G8FFD1MT7qT3NoWswq3ciVr7Ah8YmpeFcflN4rTZ-uIQ_57r80-3b0o2fgp6gQFJjb_UoXwlO01I_mObxm8xgTJzOZJpx9En8Ydh3LihdhKq37wkgoNCDAdxUujwenoRXAvyWvMV0RebUQeAcL9QrcvIyxmn2t7n1f7j4D_y41YZ8gI7btZ2PqQ/s1700-e365/INFINITERED1.png)

Around three months after getting in, the group deployed custom malware GTIG calls **INFINITERED**, which trojanizes REDCap's own system files and does three things.

* First, it hijacks the upgrade process so each new REDCap version reinjects the code instead of clearing it.
* Second, it harvests usernames and passwords from the login page and stores them, encrypted, in local database tables.
* Third, it acts as a backdoor, taking commands through HTTP cookies and running on every page load.

The earliest known compromise dates to September 2023, with activity continuing through November 2025. Once on the server, UNC6508 ran internal reconnaissance and credential discovery, pulling database and service account credentials, then used those logins to move into the internal network and on to a domain administrator account.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR_ozU4SXXSrDzvJ7UTv16s_C2jdp1ECN5KGkN-QHt8-fa5Shn0LPn1w8qSao_Tm1KKzaguPDqoSdKQtqCzyUfa9bKN6SrGogJQ6LYjWR81ze31LG8lJaXzZDuCGszVD5uswVFtKxWSJ6mp3pFoSxAgwINaPR9R4jYfX48tmFvVgOdvZ2mEf6ibrQn03Y/s1700-e365/INFINITERED2.png)

Google does not spell out the exact path to that admin account. With admin rights, the group set up the exfiltration.

## How they stole the email

The exfiltration rode a feature that was already there. UNC6508 abused content compliance rules, a legitimate Google Workspace admin feature that scans mail for keywords and can copy or forward matching messages.

Similar features exist in other cloud mail suites. The group created a rule, misspelled "Patroit," that watched for nearly 150 keywords, search terms, and email addresses. When a message matched, Workspace silently BCC'd it to an attacker-controlled Gmail address, which Google has since disabled. No malware on the mail server, no separate exfiltration tool, no unusual network traffic. Just a built-in mail feature, turned to copy the organization's secrets to an inbox the attackers owned.

MITRE already catalogs [email-forwarding-rule abuse](https://attack.mitre.org/techniques/T1114/003/) as a known technique. What GTIG flags as new here is the use of domain content compliance rules to do it, a method it says it had not seen from a China-linked actor before.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The rule's keywords mapped to UNC6508's collection priorities: geo-strategic policy, military strategy and equipment, advanced technology including AI and uncrewed vehicles, offensive cyber programs, and medical research. One term stood out for its specificity, **chikungunya**, the mosquito-borne virus behind a 2025 outbreak in China's Guangdong province.

## What to do

Start with REDCap. Patch externally facing servers and remove old versions outright, not just alongside the current build. REDCap lets legacy versions run side-by-side, and that is what enables downgrade attacks, where an attacker forces software back to a known-vulnerable release.

Then check the mail side. Review Workspace, or equivalent, content compliance and mail-forwarding rules for anything that BCCs or reroutes mail to outside addresses. Check admin audit logs for when rules changed, not just what they say now. Pull GTIG's published indicators and hunt for INFINITERED. And put phishing-resistant MFA on administrator accounts, since the whole mail-...