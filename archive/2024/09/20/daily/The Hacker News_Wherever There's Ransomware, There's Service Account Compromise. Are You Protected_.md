---
title: Wherever There's Ransomware, There's Service Account Compromise. Are You Protected?
url: https://thehackernews.com/2024/09/wherever-theres-ransomware-theres.html
source: The Hacker News
date: 2024-09-20
fetch_date: 2025-10-06T18:31:11.728133
---

# Wherever There's Ransomware, There's Service Account Compromise. Are You Protected?

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

# [Wherever There's Ransomware, There's Service Account Compromise. Are You Protected?](https://thehackernews.com/2024/09/wherever-theres-ransomware-theres.html)

**Sep 19, 2024**The Hacker NewsNetwork Security / Active Directory

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnEW90pkil285v8c8sQ5HUgxr87_gf0wc-PTQnLeFDeA3MT1A9qjswqQDbeJVDcxCceRR6iWCi49nzWX1Gxy_-Sy1qnISnINr2faz-mVHVtN6rogpuC77jN0uU6OIkt6DMayxDt9U0jC4FXX-iTv_21ODuPgWZzpiZ-aFtyKmNMRinHp9dz3PoeLnB1M4/s790-rw-e365/ransomware.png)

Until just a couple of years ago, only a handful of IAM pros knew what service accounts are. In the last years, these silent Non-Human-Identities (NHI) accounts have become [one of the most targeted and compromised attack surfaces](https://www.silverfort.com/blog/shining-the-spotlight-on-the-rising-risks-of-non-human-identities/?utm_campaign=securing-service-accounts&utm_source=thn&utm_medium=article&utm_term=sept-24&utm_content=nhi-blog). Assessments report that compromised service accounts play a key role in lateral movement in over 70% of ransomware attacks. However, there's an alarming disproportion between service accounts' compromise exposure and potential impact, and the available security measures to mitigate this risk.

In this article, we explore what makes service accounts such a lucrative target, why they are beyond the scope of most security control, and how the new approach of unified identity security can [prevent service accounts from compromise and abuse](https://www.silverfort.com/blog/securing-service-accounts-with-silverfort/?utm_campaign=securing-service-accounts&utm_source=thn&utm_medium=article&utm_term=sept-24&utm_content=best-pracs).

## Active Directory Service accounts 101: Non-human identities used for M2M

In an [Active Directory (AD) environment](https://www.silverfort.com/blog/how-to-find-service-accounts-in-active-directory/?utm_campaign=securing-service-accounts&utm_source=thn&utm_medium=article&utm_term=sept-24&utm_content=ad-blog), service accounts are user accounts that are not associated with human beings but are used for machine-to-machine communication. They're created by admins either to automate repetitive tasks, or during the process of installing on-prem software. For example, if you have an EDR in your environment, there's a service account that is responsible for fetching updates to the EDR agent on your endpoint and servers. Apart from being an NHI, service accounts are not different than any other user account in AD.

## Why do attackers go after service accounts?

Ransomware actors rely on compromised AD accounts – preferably privileged ones – for lateral movement. A ransomware actor would conduct such lateral movement until obtaining a foothold that's strong enough to encrypt multiple machines in a single click. Typically, they would achieve that by accessing a Domain Controller or another server that's used for software distribution and abusing the network share to execute the ransomware payload on as many machines as possible.

While any user account would suit this purpose, service accounts are best fitted due to the following reasons:

### High access privileges

Most service accounts are created to access other machines. That inevitably implies that they have the required access privileges to log-in and execute code on these machines. This is exactly what threat actors are after, as compromising these accounts would render them the ability to access and execute their malicious payload.

### Low visibility

Some service accounts, especially those that are associated with an installed on-prem software, are known to the IT and IAM staff. However, many are created ad-hoc by IT and identity personnel with no documentation. This makes the task of maintaining a [monitored inventory of service accounts close to impossible](https://www.silverfort.com/blog/finding-service-accounts-on-servers/?utm_campaign=securing-service-accounts&utm_source=thn&utm_medium=article&utm_term=sept-24&utm_content=finding-blog). This plays well in attackers' hands as compromising and abusing an unmonitored account has a far greater chance of going undetected by the attack's victim.

### Lack of security controls

The common security measures that are used for the prevention of account compromise are MFA and PAM. MFA can't be applied to service accounts because they are not human and don't own a phone, hardware token, or any other additional factor that can be used to verify their identity beyond their username and passwords. PAM solutions also struggle with the protection of service accounts. Password rotation, which is the main security control PAM solutions use, can't be applied to service accounts due to the concern of failing their authentication and breaking the critical processes they manage. This leaves service accounts practically unprotected.

> Want to learn more about protecting your service accounts? Explore our eBook, *[Overcoming the Security Blind Spots of Service Accounts](https://www.silverfort.com/resources/ebook/overcoming-the-security-blind-spots-of-service-accounts/?utm_campaign=securing-service-accounts&utm_source=thn&utm_medium=article&utm_term=sept-24&utm_content=blindspot-ebook)*, for further insights into the challenges of protecting service accounts and get guidance on how to combat these issues.

## Reality bytes: Every company is a potential victim regardless of vertical and size

It was once said that ransomware is the great democratizer that doesn't discriminate between victims based on any characteristic. This is truer than ever in regard to service accounts. In the past years, [we've investigated incidents](https://www.silverfort.com/blog/3-cyberattacks-in-which-compromised-service-accounts-played-a-key-role/?utm_campaign=securing-service-accounts&utm_source=thn&utm_medium=article&utm_term=sept-24&utm_content=3-cyberattack-blog) in companies from 200 to 200K employees in finance, manufacturing, retail, telecom, and many others. In 8 out of 1...