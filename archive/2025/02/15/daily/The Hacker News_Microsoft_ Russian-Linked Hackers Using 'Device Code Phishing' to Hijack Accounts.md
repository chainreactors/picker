---
title: Microsoft: Russian-Linked Hackers Using 'Device Code Phishing' to Hijack Accounts
url: https://thehackernews.com/2025/02/microsoft-russian-linked-hackers-using.html
source: The Hacker News
date: 2025-02-15
fetch_date: 2025-10-06T20:57:45.133503
---

# Microsoft: Russian-Linked Hackers Using 'Device Code Phishing' to Hijack Accounts

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

# [Microsoft: Russian-Linked Hackers Using 'Device Code Phishing' to Hijack Accounts](https://thehackernews.com/2025/02/microsoft-russian-linked-hackers-using.html)

**Feb 14, 2025**Ravie LakshmananEnterprise Security / Cyber Attack

[![device-code-phishing](data:image/png;base64... "device-code-phishing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2L91xTiJXih_PuvIGt46ZDmkAXHqiAmC05E8OwYyn3WWUBNWEQjg4KZhFG40fUaVUQQvyVCXjuzYN8a97ahllL5zPz_anZG_zz-O6Lvh3hwOn2lNoVZ16CRDXBAC4yK3dNtLdUtf86fjL-seoBTzLU8sU-KF_wOiOUqvoIpP_zVMy_mha8fXNmKogyu3J/s790-rw-e365/device-code-phishing.png)

Microsoft is calling attention to an emerging threat cluster it calls **Storm-2372** that has been attributed to a new set of cyber attacks aimed at a variety of sectors since August 2024.

The attacks have targeted government, non-governmental organizations (NGOs), information technology (IT) services and technology, defense, telecommunications, health, higher education, and energy/oil and gas sectors in Europe, North America, Africa, and the Middle East.

The threat actor, assessed with medium confidence to be aligned with Russian interests, victimology, and tradecraft, has been observed targeting users via messaging apps like WhatsApp, Signal, and Microsoft Teams by falsely claiming to be a prominent person relevant to the target in an attempt to build trust.

"The attacks use a specific phishing technique called 'device code phishing' that tricks users to log into productivity apps while Storm-2372 actors capture the information from the log in (tokens) that they can use to then access compromised accounts," the Microsoft Threat Intelligence [said](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/) in a new report.

The goal is to leverage the authentication codes obtained via the technique to access target accounts, and abuse that access to get hold of sensitive data and enable persistent access to the victim environment as long as the tokens remain valid.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The tech giant said the attack involves sending phishing emails that masquerade as Microsoft Teams meeting invitations that, when clicked, urge the message recipients to authenticate using a threat actor-generated device code, thereby allowing the adversary to hijack the authenticated session using the valid access token.

[![device-code-phishing](data:image/png;base64... "device-code-phishing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCGUyOQ1um686a68jDpdSocmLDvbJ0eNHrL0MzUJFMzQ5ysUh4hc9oJNguEZaV39SP4xRulY5M6N17dNDQ9Mn_mELlOVqxdBOB-ifkjk8b5JVOEnRc8cUXEZOKstQGMWVRsEFA4AwYedxPfgGyKFi45phm0FL_6sFYzAsJYzfmRknl7jyEe4HZGMJTITl2/s790-rw-e365/scam-msgs.png)

"During the attack, the threat actor generates a legitimate device code request and tricks the target into entering it into a legitimate sign-in page," Microsoft explained. "This grants the actor access and enables them to capture the authentication—access and refresh—tokens that are generated, then use those tokens to access the target's accounts and data."

The phished authentication tokens can then be used to gain access to other services that the user already has permissions to, such as email or cloud storage, without the need for a password.

Microsoft said the valid session is used to move laterally within the network by sending similar phishing intra-organizational messages to other users from the compromised account. Furthermore, the Microsoft Graph service is used to search through messages of the breached account.

"The threat actor was using keyword searching to view messages containing words such as username, password, admin, teamviewer, anydesk, credentials, secret, ministry, and gov," Redmond said, adding the emails matching these filter criteria were then exfiltrated to the threat actor.

To mitigate the risk posed by such attacks, organizations are recommended to [block device code flow](https://learn.microsoft.com/en-in/entra/identity/conditional-access/policy-block-authentication-flows) wherever possible, enable phishing-resistant multi-factor authentication (MFA), and follow the principle of least privilege.

### Update

In an update shared on February 14, 2025, Microsoft said it "observed Storm-2372 shifting to using the specific client ID for Microsoft Authentication Broker in the device code sign-in flow."

Using the client ID, it added, enables the attackers to receive a refresh token that can be used to request another token for the device registration service, and then register an actor-controlled device within Entra ID. The connected device is then used to harvest emails.

"With the same refresh token and the new device identity, Storm-2372 is able to obtain a Primary Refresh Token (PRT) and access an organization's resources," Microsoft said. "The actor has also been observed to use proxies that are regionally appropriate for the targets, likely in an attempt to further conceal the suspicious sign in activity."

Cybersecurity firm Volexity said it has observed at least three different Russian threat actors conducting spear-phishing campaigns using the device code approach to compromise Microsoft 365 accounts since mid-January 2025.

Some of the emails have been identified as sent from accounts impersonating individuals from the United States Department of State, Ukrainian Ministry of Defence, European Union Parliament, and other prominent research institutions.

One of the clusters behind the activity is suspected to be [APT29](https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html), which is also known as BlueBravo, Cloaked Ursa, CozyLarch, Cozy Bear, Midnight Blizzard (formerly Nobelium), and The Dukes. The other two groups have been assigned the monikers UTA0304 and UTA0307.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhizyd4sBiiV7hXHI6iGqyT_ytauk5c4BeD4G9VaeMRfc31...