---
title: How was Uber hacked, and what can we learn from the incident?
url: https://blog.appsecco.com/how-was-uber-hacked-and-what-can-we-learn-from-the-incident-d421ea90449?source=rss----e2adb3957733---4
source: Appsecco - Medium
date: 2022-11-16
fetch_date: 2025-10-03T22:55:31.819720
---

# How was Uber hacked, and what can we learn from the incident?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd421ea90449&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.appsecco.com%2Fhow-was-uber-hacked-and-what-can-we-learn-from-the-incident-d421ea90449&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.appsecco.com%2Fhow-was-uber-hacked-and-what-can-we-learn-from-the-incident-d421ea90449&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Appsecco](https://blog.appsecco.com/?source=post_page---publication_nav-e2adb3957733-d421ea90449---------------------------------------)

·

Follow publication

[![Appsecco](https://miro.medium.com/v2/resize:fill:76:76/1*-ERVMgF2P005dtPsm5nIqw.jpeg)](https://blog.appsecco.com/?source=post_page---post_publication_sidebar-e2adb3957733-d421ea90449---------------------------------------)

Blog posts from the Security Testing Teams and DevSecOps Teams at Appsecco. Covering security around applications, Cloud environments like AWS, Azure, GCP, Kubernetes, Docker. Covering DevSecOps topics such as Secrets Management, Secure CI/CD Pipelines and more

Follow publication

# How was Uber hacked, and what can we learn from the incident?

[![Shiva Gupta](https://miro.medium.com/v2/resize:fill:64:64/1*YW2w7XIp0BXlfD-VgKzfWw.jpeg)](https://medium.com/%40admiralgaust?source=post_page---byline--d421ea90449---------------------------------------)

[Shiva Gupta](https://medium.com/%40admiralgaust?source=post_page---byline--d421ea90449---------------------------------------)

6 min read

·

Nov 9, 2022

--

Listen

Share

Unless you were off planet or on a remote uninhabited island mid Pacific with no Internet access, it would have been hard to miss the Uber hack which was disclosed in September. An obvious question that came to everyone’s mind is “what exactly went wrong with Uber?” and “What could they have done better to prevent this breach from happening?”. If you are also curious about this and searching for the answer to these questions, then this blog post gives you good insight into what went wrong and the aftermath of the attack.

In this blog post, we will break down the Uber security breach into “what” and “how”. Then we will try to address some measures which Uber could have taken to prevent this breach from happening ending with a summary of important lessons learnt from this incident.

This article has referred to multiple Internet sources to build a timeline of the execution of the breach and predominantly covers the technical aspects of what (potentially) happened.

On 15th September 2022, Uber made an official announcement acknowledging the security breach. Soon enough Twitter users started tweeting about this. Some users even started tweeting about this even before the official announcement was made from the company side. The hacker after getting access to Uber’s **AWS**, **Slack** and **SentinelOne** accounts started posting insider information and screenshots of evidence to announce the hack.

![]()

![]()

<https://twitter.com/ColtonSeal/status/1570596125924794368?t=yrxYHGRLy4BZ2dLB7-w_Fg&s=08>

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

On 19th September 2022, Uber completed their initial stage of investigation and released an official note emphasising on “What did happen” and their response to this security breach.

### **A brief summary of what happened**

The image below shows the life-cycle of the breach and all the events that possibly could have happened.

Press enter or click to view image in full size

![]()

[Lifecyle of events](https://twitter.com/sec_r0/status/1574459793519292416?t=hR7g33oy232YCZASNjJ_qg&s=19)

**Initial foothold**

The hacker was able to get an initial foothold using a set of credentials purchased from the dark web. Two of the Uber contractor employees VPN credentials were compromised after their personal devices were infected with a malware. The attacker then utilised these credentials and performed the MFA fatigue attack (aka MFA Prompt Spamming/MFA bombing). This is a simple technique in which attackers flood user’s authentication app with push notifications in the hope they will accept, enabling the attacker to gain entry to an account or device. Eventually, the contractor employee accepted the push request once, and the attacker successfully logged in.

![]()

<https://twitter.com/GroupIB_GIB/status/1570821203685937154?t=j9t-toPsBXeLm8LteYEm_g&s=08>

![]()

<https://twitter.com/Savitar0x01/status/1570679758740148226?t=0gKnwvLeiOTkPk1Rr4AkmQ&s=08>

Post Pandemic, it has become very normal for the organisations to allow users to work from home using VPN or similar technologies. One of the main challenges with work from home setup is to ensure that people are well trained and have good awareness about information security practices. Especially, when they are using their personal laptop to connect to the corporate network. According to Uber, the contractor employee password was compromised after their personal laptop was infected with the malware resulting in allowing the attacker to get initial access to the Uber internal environment.

**Lack of Security Awareness and Training**

Clearly, the contractor employee lacked general security awareness. The employee might have either ignored or neglected the information security training and sessions conducted withing the organisation, if any. Allowing use of personal devices and not ensuring sufficient security training for all employees seems like the first mistake which Uber did resulting into this breach.

It is very important for all the organisations to conduct proper security awareness sessions for all employees on a periodic basis to strengthen their security posture. That too should be conducted in a fun and interactive manner so that employees actively participate and learn from the training. Not just for compliance reasons wherein employees often tend to get bored and could not learn anything from it. After all, humans are the weakest link of an organisation's security and requires most attention, constant training and periodic reminders.

**Network Enumeration**

Once the hacker penetrated Uber’s internal network by using compromised VPN credentials, he/she scanned for internal resources and eventually found a network share to which they had at least read permissions. The hacker may have used common network discovery and enumeration tools like [Nmap](https://github.com/nmap/nmap), [sharesniffer](https://github.com/shirosaidev/sharesniffer), [SMB-Data-Discovery](https://github.com/gh0x0st/SMB-Data-Discovery), etc for enumerating the internal network and discovering the network shares. They then found a folder inside an accessible network share which contained a few windows PowerShell scripts. These PowerShell scripts that the attacker stumbled upon contained credentials of an admin user of Thycotic (a popular Privileged Access Management software). Windows PowerShell scripts are written in an English like language that can easily be read using simple text editors like notepad.

Pres...