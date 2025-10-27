---
title: Preventing Insider Threats in Your Active Directory
url: https://thehackernews.com/2023/03/preventing-insider-threats-in-your.html
source: The Hacker News
date: 2023-03-23
fetch_date: 2025-10-04T10:27:04.164652
---

# Preventing Insider Threats in Your Active Directory

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

# [Preventing Insider Threats in Your Active Directory](https://thehackernews.com/2023/03/preventing-insider-threats-in-your.html)

**Mar 22, 2023**The Hacker NewsPassword Security / Active Directory

[![Active Directory](data:image/png;base64... "Active Directory")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUfxVsLvrrMk8euIngTXxazN_vPkx7U0-dVEBsz4yqtbyHZE0JqHGyZfxsp6SleGcfzN6Km-1ee1fM6bcwdw7gbuRSDrQeSvrJiqEhI4T6ZAb1EA4MhxelSNyMoWMKNUbRBef2sUAMuf1lMg7WnbA6rXeuDQKGp2RfLccsnkRcycDithxGimkOY2xa/s790-rw-e365/lock.png)

Active Directory (AD) is a powerful authentication and directory service used by organizations worldwide. With this ubiquity and power comes the potential for abuse. Insider threats offer some of the most potentials for destruction. Many internal users have over-provisioned access and visibility into the internal network.

Insiders' level of access and trust in a network leads to unique vulnerabilities. Network security often focuses on keeping a threat actor out, not on existing users' security and potential vulnerabilities. Staying on top of potential threats means protecting against inside and outside threats.

## Active Directory Vulnerabilities

From the outside, a properly configured AD domain offers a secure authentication and authorization solution. But with complex social engineering and phishing email attacks, an existing AD user can become compromised. Once inside, threat actors have many options to attack Active Directory.

### Insecure Devices

With "Bring Your Own Device" (BYOD) growing, there is increased device support and security complexity. If users connect a device that is already compromised or has inadequate security measures, attackers have a simple way to gain access to the internal network.

In the past, an attacker would have to sneak in to install a malicious device. Now, however, a user with a compromised device does the hard work for them. Moreover, many workers may also connect their smartphones or tablets to the network. This means that, instead of a single work-issued laptop, you may have two or three user devices that are not subject to the same security measures.

### Over-Provisioned Access

Adding complexity to internal security is the common issue of over-provisioned access. Organizations often tend to expand access instead of restricting it. A single act of convenience to solve a problem can have the unintended consequence of creating a potential attack vector, which is then often forgotten.

For those users that are also administrators, there is not always a highly secure "Administrative" account created to separate the different access levels. In this way, the convenience of allowing Administrative tasks via a standard user account opens the door to rampant abuse due to a compromised and highly privileged account.

### Weak Password Policies

Many organizations, especially larger ones, may have weaker password policies due to the various applications they support. Not all applications are the same, and some do not support the latest security standards. Examples of this include those that do not support LDAP signing or TLS over LDAP with LDAPS.

A weak password policy coupled with a lack of multi-factor authentication makes it easy to crack a retrieved hash through a technique such as Keberoasting via a privileged internal account. This is in stark contrast to a strong password policy and multi-factor authentication, which makes it much harder to gain access to a system or network by cracking a hash.

## Best Practices for Securing Active Directory

To secure Active Directory, there are many best practices to follow. Based on the previously outlined security themes, here are several:

* Restrict access to systems and networks to those with a legitimate business need.
* Ensure connected devices meet a minimum standard of security.
* Configure Active Directory securely with [LDAP signing](https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/enable-ldap-signing-in-windows-server) and [LDAPS requirements](https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/enable-ldap-over-ssl-3rd-certification-authority), regularly [rotate the KRBTGT password](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-forest-recovery-resetting-the-krbtgt-password) and use [group-managed service accounts (gMSA)](https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview) to rotate service account credentials.
* Enable multi-factor authentication and a strong password policy, augmented by solutions such as [Specops Password Policy](https://specopssoft.com/product/specops-password-policy/?utm_source=bleepingcomputer&utm_medium=referral&utm_campaign=na_2023_bleepingcomputer&utm_content=guest-post).
* Separate permissions from the [typical user account and assign them to special administrative accounts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts#separate-administrator-accounts-from-user-accounts).
* Ensure that users know the dangers of phishing emails and social engineering, such as clicking on attachments.

Training users to identify potential phishing emails and social engineering attacks is essential. Additionally, users should be discouraged from clicking on any attachments, and organizations should use systems that scan for malicious content. These measures can help to reduce the risk of a successful attack.

But, assume that AD has already been compromised. An organization can and should take an in-depth look into the permissions assigned to active and non-active or decommissioned users and systems. Are there ways to separate permissions from typical user accounts and assign them to special administrative accounts with a higher security level?

Enabling multi-factor authentication with a strong password policy is essential for creating some of the strongest protections available. As many social engi...