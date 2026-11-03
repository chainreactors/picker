---
title: Attackers Pose as IT Support on Microsoft Teams, Abuse AD CS to Steal Company Data
url: https://thehackernews.com/2026/11/attackers-pose-as-it-support-on.html
source: The Hacker News
date: 2026-11-02
fetch_date: 2026-11-03T08:51:45.272617
---

# Attackers Pose as IT Support on Microsoft Teams, Abuse AD CS to Steal Company Data

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Attackers Pose as IT Support on Microsoft Teams, Abuse AD CS to Steal Company Data](https://thehackernews.com/2026/11/attackers-pose-as-it-support-on.html)

**Swati Khandelwal**Nov 02, 2026Social Engineering / Active Directory

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLv88EM1ZSjaeI7bH9DVpg2mGdkwXWUuir0S_p9IfiWG49_TgRalFdK4oQ6e7UE_JYOnNH70Z6wcftnjhcYHRY-Xc0o8GYp9r1uNzxdC_1bnXZgvon74cXkWgKpHZtwJg3IKLsqGC2HS2tcMfQS8BZu7kfrW1vAaaIA316LRzgCOn8zeGZ1WvALgJmyM4/s1700-nu-rw-lo-l85-e365/ms-ad.jpg)

Attackers posing as IT support on Microsoft Teams talked employees into giving them remote control of their PCs. They then used insecure Active Directory Certificate Services (AD CS) settings to obtain login certificates for privileged accounts, including one for a domain controller.

Microsoft said in [a report](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/) that it investigated two such intrusions, one of which resulted in company data being copied to an external server.

The attackers exploited no flaw in Teams itself. They relied on social engineering and on AD CS that had been set up insecurely, and Microsoft did not tie the activity to any known group.

### How the Attacks Began

Both intrusions started the same way, Microsoft said. The attackers messaged and called employees on Teams while posing as the company's own IT or help desk, working from outside tenants with support-themed names so the contact looked familiar.

They talked each user into opening Quick Assist, a remote-help tool built into Windows, and reading the connection code back to them. That gave the attacker direct, hands-on control of the workstation.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidksUUoNFOF9jbb1QOmQ37tNavcwp1gx9wPFCK_P6ZzFcD0nwSVUWTAMGW9E5NFuhBGuO9o82iUzn97FXXDC7KeEI8E3XrW5mCkdmbtxezOkS8uxUNnQw20GmSSmZcvxbEImriuw65DWi9JdszJLRkA_EWXM7_zz0kCn3biLi7Sn6ZPFE4dKZps3XUz9Q/s1700-nu-rw-lo-l85-e365/entry.jpg)

From there, the attacker dropped an archive into the Downloads folder, unpacked it into a new folder named to resemble a Windows update, and ran its contents with a portable Python, Bun, or Java runtime. File names alone were a weak signal, because one copy was renamed while still carrying the real runtime's version details.

### What a Certificate Buys an Attacker

AD CS is the Windows role that issues the certificates users and computers present when they log in. A certificate from a poorly configured template lets whoever holds it sign in as the account it names.

Microsoft said such a certificate continues to work even after the account's password is reset or the first machine is wiped, so neither step ends the attacker's access.

### Case 1: Privileged Certificates, and a Gap in Containment

In the first intrusion, the attackers found a certificate template with a weakness known as ESC1. With that kind of template, the requester can name the account the certificate will represent, so a low-privileged user can request one that stands in for a privileged account.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The first wave of calls targeted three users and one workstation, producing certificates for three highly privileged accounts. Microsoft Defender's automatic attack disruption cut those identities off and dropped their active sessions. One privileged account, though, had been left out of the automatic response, so it stayed usable.

About 90 minutes later, a larger wave hit 16 users and a second workstation, producing certificates for 8 more privileged accounts. Microsoft said more than 1,000 later attempts to reach files over SMB or to log in were blocked.

Within seconds of obtaining a certificate, the attacker signed in to a domain controller and ran DCSync, a tool for copying password data from Active Directory. The operation had already begun when containment took hold, limiting how much could be replicated. Microsoft did not say how much credential data the attacker obtained.

The excluded account was the opening. The attacker kept using it, reached a file server, and ran a renamed copy of the file-copying tool Rclone to move data from a share to an outside SFTP server. Microsoft did not say how much data was taken.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7HJZkLf4BTF2d3snB9vZzofHRSe5XM9QsTdkt-OFfaQHsW-DjQc5CfdgUaBXmjpDdBE1N0nA5TKSEMUsOFCAITMiMt32CjQFSv4TSCagqz3auoXUob0D88Qz4cDHgfAu9YwrXSEsLj4LEpxi9wjPM2UAVYSX0mzR8c5TqSJJmrhZQ6hgwI8la1xBIh10/s1700-nu-rw-lo-l85-e365/11.jpg)

The case shows, in Microsoft's words, that "partial identity containment can reduce attack activity while still leaving a viable privileged route."

### Case 2: A Certificate for the Domain Controller

The second intrusion began the same way but took a different direction because that template weakness was not present. The attacker instead used a technique called PetitPotam to force a domain controller to authenticate to a machine the attacker controlled.

That NTLM login was relayed to the AD CS web enrollment page, an abuse known as ESC8, with no password needed. The attacker used the relayed login to request a certificate for the domain controller itself. With that certificate and Kerberos (PKINIT), the attacker obtained a ticket-granting ticket for the domain controller, turning a one-off relayed login into a lasting identity.

Here the response held. Defender raised ESC8 alerts, the customer isolated the workstation, and Microsoft said no further activity followed.

The difference between the two came down to containment. In the first, automatic disruption blocked most of the attack, but the one excluded account stayed open. In the second, isolating a single workstation stopped it.

### What Defenders Can Do

There is no patch, because nothing here was a ...