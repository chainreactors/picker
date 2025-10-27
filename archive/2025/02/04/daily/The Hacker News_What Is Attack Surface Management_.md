---
title: What Is Attack Surface Management?
url: https://thehackernews.com/2025/02/what-is-attack-surface-management.html
source: The Hacker News
date: 2025-02-04
fetch_date: 2025-10-06T20:49:05.426840
---

# What Is Attack Surface Management?

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

# [What Is Attack Surface Management?](https://thehackernews.com/2025/02/what-is-attack-surface-management.html)

**Feb 03, 2025**The Hacker NewsAttack Surface Management

[![Attack Surface Management](data:image/png;base64... "Attack Surface Management")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9GPTnlkZEmINbXHKjh1DEDdkAtbkPkC6Fx3-BZMdGUPPUFuC91JZUeFhjUnrK3NI2fLV5rP1bz9gYSRnKcRsCy0oVyRXzhyRY1Tx3UY8l9IqKPLQp6ebwiR9U339BORXmRBGzj-oSVvxndeWZnDYDEiAk8utNGn1JyuaGUBHrkTAzCEeLWkJrFuUIjUoV/s790-rw-e365/intruder.png)

Attack surfaces are growing faster than security teams can keep up – to stay ahead, you need to know what's exposed and where attackers are most likely to strike.

With cloud adoption dramatically increasing the ease of exposing new systems and services to the internet, prioritizing threats and managing your attack surface from an attacker's perspective has never been more important.

In this guide, we look at why attack surfaces are growing and how to monitor and manage them properly with [tools like Intruder](https://www.intruder.io/attack-surface-management?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=eu%7Csearch%7C03_feb). Let's dive in.

## What is your attack surface?

First, it's important to understand what we mean when we talk about an attack surface. An attack surface is the sum of your digital assets that are 'reachable' by an attacker – whether they are secure or vulnerable, known or unknown, in active use or not.

You can also have both internal and external attack surfaces - imagine for example a malicious email attachment landing in a colleague's inbox, vs a new FTP server being put online.

Your external attack surface changes continuously over time, and includes digital assets that are on-premises, in the cloud, in subsidiary networks, and in third-party environments. In short, your attack surface is anything that a hacker can attack.

## What is attack surface management?

Attack surface management (ASM) is the process of discovering these assets and services and reducing or minimizing their exposure to prevent hackers exploiting them.

Exposure can mean two things: current vulnerabilities, such as missing patches or misconfigurations that reduce the security of the services or assets. But it can also mean exposure to future vulnerabilities or determined attacks.

Take for example an admin interface like cPanel, or a firewall administration page – these may be secure against all known current attacks today, but a vulnerability could easily be discovered in the software tomorrow – in which case it would immediately become a significant risk. So while traditional vulnerability management processes would say "wait until a vulnerability is detected and then remediate it", attack surface management would say "get that firewall admin panel off the internet before it becomes a problem!".

That's not to mention that having a firewall admin panel exposed to the internet opens it up to other attacks, regardless of a vulnerability being discovered. For example, if an attacker discovers some admin credentials elsewhere, they could potentially reuse those credentials against this admin interface, and this is often how attackers expand their access across networks. Equally, they may just try a sustained "low and slow" password guessing exercise which goes under the radar but eventually yields results.

To highlight this point in particular, ransomware gangs were [reported in 2024](https://www.bleepingcomputer.com/news/security/vmware-confirms-critical-vcenter-flaw-now-exploited-in-attacks/) targeting VMware vSphere environments exposed to the internet. By exploiting a vulnerability in these servers, they were able to gain access and encrypt virtual hard disks of critical infrastructure to demand huge ransoms. It was reported there are over two thousand vSphere environments still exposed.

So for multiple reasons, reducing your attack surface today makes you harder to attack tomorrow.

## The need for attack surface management

### **The challenges of asset management**

So, if a significant part of attack surface management is reducing exposure to possible future vulnerabilities by removing unnecessary services and assets from the internet, the first step is to know what you have.

Often considered the poor relation of vulnerability management, asset management has traditionally been a labor intensive, time-consuming task for IT teams. Even when they had control of the hardware assets within their organization and network perimeter, it was still fraught with problems. If just one asset was missed from the asset inventory, it could evade the entire vulnerability management process and, depending on the sensitivity of the asset, could have far reaching implications for the business. This was the case in the [Deloitte breach](https://krebsonsecurity.com/2017/09/source-deloitte-breach-affected-all-company-email-admin-accounts/) in 2016, where an overlooked administrator account was exploited, exposing sensitive client data.

When companies expand through mergers and acquisitions too, they often take over systems they're not even aware of – take the example of telco TalkTalk which was [breached in 2015](https://www.trendmicro.com/vinfo/pl/security/news/cyber-attacks/talktalk-breach-up-to-4-million-unencrypted-records-stolen) and up to 4 million unencrypted records were stolen from a system they didn't even know existed.

### **The shift to cloud**

Today, it's even more complicated. Businesses are migrating to cloud platforms like Google Cloud, Microsoft Azure, and AWS, which allow development teams to move and scale quickly when needed. But this puts a lot of the responsibility for security directly into the hands of the development teams – shifting away from traditional, centralized IT teams with change control processes.

While this is great for speed of development, it creates a visibility gap, and so cyber security teams need ways to keep up with the pace.

### **A modern solution**
...