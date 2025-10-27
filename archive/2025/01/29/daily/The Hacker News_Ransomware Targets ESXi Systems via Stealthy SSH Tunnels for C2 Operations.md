---
title: Ransomware Targets ESXi Systems via Stealthy SSH Tunnels for C2 Operations
url: https://thehackernews.com/2025/01/ransomware-targets-esxi-systems-via.html
source: The Hacker News
date: 2025-01-29
fetch_date: 2025-10-06T20:12:20.472000
---

# Ransomware Targets ESXi Systems via Stealthy SSH Tunnels for C2 Operations

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

# [Ransomware Targets ESXi Systems via Stealthy SSH Tunnels for C2 Operations](https://thehackernews.com/2025/01/ransomware-targets-esxi-systems-via.html)

**Jan 28, 2025**Ravie LakshmananRansomware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHbuAemk6xq6i6aXXyKpxryeYpHaI1oG4AgM9cUrnkRr6bgLZqOfcvJUMwMqpTSLa8nMUnOT7Wor1SCKvKGMZdvfjQK3ojmeGdN1jQCK4khO0JncIFOL1S4hdFJd28hKogupixw7zUQFiuxfnrCsIzJ4Dwxivuztj7fX-I2SO6yLfJAFDZu2OAyUggO16X/s790-rw-e365/ransomware.png)

Cybersecurity researchers have found that [ransomware attacks](https://thehackernews.com/2024/07/new-linux-variant-of-play-ransomware.html) targeting [ESXi systems](https://www.bitdefender.com/en-us/blog/businessinsights/akira-ransomware-a-shifting-force-in-the-raas-domain) are also leveraging the access to repurpose the appliances as a conduit to tunnel traffic to command-and-control (C2) infrastructure and stay under the radar.

"ESXi appliances, which are unmonitored, are increasingly exploited as a persistence mechanism and gateway to access corporate networks widely," Sygnia researchers Aaron (Zhongyuan) Hau and Ren Jie Yow [said](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/) in a report published last week.

"Threat actors use these platforms by adopting 'living-off-the-land' techniques and using native tools like SSH to establish a SOCKS tunnel between their C2 servers and the compromised environment."

In doing so, the idea is to blend into legitimate traffic and establish long-term persistence on the compromised network with little-to-no detection by security controls.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity company said in many of its incident response engagements, ESXi systems were compromised either by using admin credentials or leveraging a known security vulnerability to get around authentication protections. Subsequently, the threat actors have been found to set up a tunnel using SSH or other tools with equivalent functionality.

"Since ESXi appliances are resilient and rarely shutdown unexpectedly, this tunneling serves as a semi-persistent backdoor within the network," the researchers noted.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPvyS2Coqo7lyYt44HyapFgmlhgqQBzHmehutU5L43DLmCrNI7ffIF_LiiLHuZDTDMoNFImkRZwD5ouN8-LdJDZ42MQQy4vU2iSZe8hl4VCWlgFySpKEFEGDz0hXgmCI8zYcbBNLvxrWkdy_HpNLxI_5MvUZTz82Ufpx9UAMvEtkQ4pez1AroeEiEkKbt-/s790-rw-e365/malware.png)

Sygnia has also highlighted the challenges in monitoring ESXi logs, emphasizing the need for configuring log forwarding to capture all relevant events in one place for forensic investigations.

To detect attacks that involve the use of SSH tunneling on ESXi appliances, organizations have been recommended to review the below four log files -

* /var/log/shell.log (ESXi shell activity log)
* /var/log/hostd.log (Host agent log)
* /var/log/auth.log (authentication log)
* /var/log/vobd.log (VMware observer daemon log)

### Andariel Employs RID Hijacking

The development comes as the AhnLab Security Intelligence Center (ASEC) detailed an attack mounted by the North Korea-linked [Andariel](https://thehackernews.com/2024/10/andariel-hacker-group-shifts-focus-to.html) group that involves the use of a technique known as Relative Identifier ([RID](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers)) hijacking to covertly modify the Windows Registry to assign a guest or low privileged account administrative permissions during the next login.

The [persistence](https://pentestlab.blog/2020/02/12/persistence-rid-hijacking/) [method](https://www.ired.team/offensive-security/persistence/rid-hijacking) is sneaky in that it takes advantage of the fact that regular accounts are not subjected to the same level of surveillance as the administrator account, thereby allowing threat actors to perform malicious actions while remaining undetected.

However, in order to perform RID hijacking, the adversary must have already compromised a machine and gained administrative or SYSTEM privileges, as it requires changing the RID value of the standard account to that of the Administrator account (500).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEje14N39rJYO93kxrPmMSFsJsXMPSYhwKeCGgLu2Rpi1ufZ_6q_lsiWzkBtc1irXg87asPn399FBAsTmqEt4eBVW2JBsbkhx_gpbkl5TTdt0l7FsqFHIjj6NwKdyVIiy9x6B8fp8LuLy8Kcfqeqo0XRzIjzcgEHy62wTkEqHauwYfekbT_OW3ItxXTTGIyb/s790-rw-e365/rid-hijacking.png)

In the attack chain documented by ASEC, the threat actor is said to have created a new account and assigned it administrator privileges using this approach, after obtaining SYSTEM privileges themselves using privilege escalation tools such as PsExec and JuicyPotato.

"The threat actor then added the created account to the Remote Desktop Users group and Administrators group using the 'net localgroup' command," the company [said](https://asec.ahnlab.com/en/85942/). "When an account is added to the Remote Desktop Users group, the account can be accessed by using RDP."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Once the RID value has been changed, the Windows OS recognizes the account created by the threat actor as having the same privileges as the target account, enabling privilege escalation."

### New Technique for EDR Evasion

In related news, it has also been discovered that an approach based on hardware breakpoints could be leveraged to bypass Event Tracing for Windows ([ETW](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/event-tracing-for-windows)) detections, which provides a mechanism to log events raised by user-mode applications and kernel-mode drivers.

This entails using a native Windows function called [NtContinue](https://www.outflank.nl/blog/2024/10/15/introducing-early-cascade-injection-f...