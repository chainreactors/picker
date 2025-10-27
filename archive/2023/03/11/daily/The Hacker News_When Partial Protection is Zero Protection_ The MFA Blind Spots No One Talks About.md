---
title: When Partial Protection is Zero Protection: The MFA Blind Spots No One Talks About
url: https://thehackernews.com/2023/03/when-partial-protection-is-zero.html
source: The Hacker News
date: 2023-03-11
fetch_date: 2025-10-04T09:18:41.922895
---

# When Partial Protection is Zero Protection: The MFA Blind Spots No One Talks About

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

# [When Partial Protection is Zero Protection: The MFA Blind Spots No One Talks About](https://thehackernews.com/2023/03/when-partial-protection-is-zero.html)

**Mar 10, 2023**The Hacker NewsMulti-factor Authentication

[![Multi-factor Authentication](data:image/png;base64... "Multi-factor Authentication")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3b_fBAzsejHrSAUuwfwtZqr_KxhcbBT8UBO6YDROrBC8QwI2ehcWWXz3Szun0SyGnUdrthlQI64n_xbCIy5QZpNnpAh5DZKKgV0dweaWcrGYB74ioM3DwG1ZVCC_oI8I6zWcC-ZWAsyAVBZZgGjRxPknxpT4_0nIuukynSxsQ9AWyXIpprNimORnG/s790-rw-e365/mfa.png)

Multi-factor Authentication (MFA) has long ago become a standard security practice. With a wide consensus on its ability to fend off more than 99% percent of account takeover attacks, it's no wonder why security architects regard it as a must-have in their environments. However, what seems to be less known are the inherent coverage limitations of traditional MFA solutions. While compatible with RDP connection and local desktop logins, **they offer no protection to remote command line access tools like PsExec, Remote PowerShell and their likes.**

In practice, it means that workstations and servers remain as vulnerable to lateral movement, ransomware spread and other identity threats despite having a fully functioning MFA solution on. For the adversary it's just a matter of taking the command line path instead of the RDP to log in as if there was not protection installed at all. In this article we'll explore this blind spot, understand its root cause and implications, and view the different options security teams can overcome it to maintain their environments protected.

## The Core Purpose of MFA: Prevent Adversaries from Accessing your Resources with Compromised Credentials

MFA the most efficient security measure again account takeover. The reason that we have MFA in the first place to prevent adversaries from accessing our resources with compromised credentials. So even if an attacker would be able to take hold of our username and password – which is more than plausible scenario – it still won't be able to leverage them for malicious access on our behalf. So, it's the ultimate last line of defense against credential compromise, that aims to void this compromise form any gain.

## The Blind Spot: MFA is not Supported by Command Line Access Tools in the Active Directory Environment

While MFA can fully cover access to SaaS and web apps it's significantly more limited when it comes to the Active Directory managed environment. This is because the key authentication protocols that are used in this environment, NTLM and Kerberos, were written way before MFA existed and don't natively support it. What it means is that every authentication method that implements these protocols cannot be protected with MFA. That includes every CMD and PowerShell-based remote access tools, of which the most prominent ones are PsExec and Remote PowerShell. These are the default tools admin use to connect remotely to users' machines for troubleshooting and maintenance purposes, and hence are found in practically any AD environment.

## The Cyber Security Implications: Lateral Movement and Ransomware Attacks Encounter no Resistance.

This mainstream remote connection path is, by definition, unprotected from a compromised credentials scenario and as a result is used in most to all lateral movement and ransomware spread attacks. It doesn't matter that there is an MFA solution that guards the RDP connection and prevents them from being abused. For an attacker, moving from the patient-zero machine to other workstations in the environment with PsExec or Remote PowerShell is as easy as doing so with RDP. It's just a matter of using one door instead of the other.

Are you as protected as you should be? Maybe it's time for you to re-evaluate your MFA. As a follow-up, [**explore this eBook to learn**](https://www.silverfort.com/resources/ebook/re-evaluate-your-mfa-protection-ebook/utm_source%3DTHN%26utm_medium%3Darticle%26utm_campaign%3Dmfamarch) more about Silverfort's Unified Identity Protection approach to MFA and gain insight into how to assess your existing protections and relative risk exposure.

## The Harsh Truth: Partial MFA Protection is No Protection at all

So, if you've gone through the pain of installing MFA agents on all your critical servers and workstations, most chances are that you've achieved little in actually securing them from identity threats. This is one of the cases where you can't go halfway. It's either you're protected or you're not. When there's a hole in the bottom of the boat it makes little difference that all the rest of it is solid wood. And in the same manner, if attackers can move laterally in your environment by providing compromised credentials to command line access tools, it no longer matters that you have MFA protection for RDP and desktop login.

## The MFA Limitations in the On-Prem Environment Puts your Cloud Resources in Risk As well

Despite the shift to the cloud, more than 90% of organizations maintain a hybrid identity infrastructure with both AD managed workstations and servers, as well as SaaS apps and cloud workloads. So not only core on-prem resources like legacy applications and file shares are exposed to the use of compromised credentials due to the lack of MFA protection, but also the SaaS apps as well.

The common practice today is to sync passwords between all these resources, so the same username and password are used to access both an on-prem file server as well an organizational SaaS app. This means that any attack on-prem that includes the compromise and use of users' credentials can easily pivot to access SaaS resources directly from the attacked machines.

## The Paradigm Shift: From Traditional MFA to Unified Identity Protection

The gap that we've described stems from how traditional MFA is designed and implemented. The key limitation is that MFA solutions today plug into the authentication process of each individual resource, s...