---
title: New Windows Task Scheduler Bugs Let Attackers Bypass UAC and Tamper with Logs
url: https://thehackernews.com/2025/04/experts-uncover-four-new-privilege.html
source: The Hacker News
date: 2025-04-17
fetch_date: 2025-10-06T22:09:24.089520
---

# New Windows Task Scheduler Bugs Let Attackers Bypass UAC and Tamper with Logs

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

# [New Windows Task Scheduler Bugs Let Attackers Bypass UAC and Tamper with Logs](https://thehackernews.com/2025/04/experts-uncover-four-new-privilege.html)

**Apr 16, 2025**Ravie LakshmananEndpoint Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8AUniRDkx_hmhlRLXM90BvM7qjdCTYaSdXMMyLOhx933X44BxGL5q0dxAt_dN05OgR45gasinWyg_7BqamqQU_UmGNF8gzj7CvxW77b8yxxnIUjbcZe7HfBLE2nlMWonF4RsG7l-Az7mOjjycJBHp-cLJi8Axm6NWF2UzLIrG_h7GG_EugerUE-TSfEJY/s790-rw-e365/1000101087.jpg)

Cybersecurity researchers have detailed four different vulnerabilities in a core component of the Windows [task scheduling service](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) that could be exploited by local attackers to achieve privilege escalation and erase logs to cover up evidence of malicious activities.

The issues have been uncovered in a binary named "[schtasks.exe](https://learn.microsoft.com/en-us/windows/win32/taskschd/schtasks)," which enables an administrator to create, delete, query, change, run, and end scheduled tasks on a local or remote computer.

"A [User Account Control] bypass vulnerability has been found in Microsoft Windows, enabling attackers to bypass the User Account Control prompt, allowing them to execute high-privilege (SYSTEM) commands without user approval," Cymulate security researcher Ruben Enkaoua [said](https://cymulate.com/blog/task-scheduler-new-vulnerabilities-for-schtasks-exe/) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"By exploiting this weakness, attackers can elevate their privileges and run malicious payloads with Administrators' rights, leading to unauthorized access, data theft, or further system compromise."

The problem, the cybersecurity company said, occurs when an attacker creates a scheduled task [using Batch Logon](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-logontype-simpletype) (i.e., a password) as opposed to an Interactive Token, causing the task scheduler service to grant the running process the maximum allowed rights.

However, for this attack to work, it hinges on the threat actor acquiring the password through some other means, such as cracking an NTLMv2 hash after authenticating against an SMB server or exploiting flaws such as [CVE-2023-21726](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21726).

A net result of this issue is that a low-privileged user can leverage the schtasks.exe binary and impersonate a member of groups such as Administrators, Backup Operators, and Performance Log Users with a known password to obtain the maximum allowed privileges.

The registration of a scheduled task using a Batch Logon authentication method with an XML file can also pave the way for two defense evasion techniques that make it possible to overwrite [Task Event Log](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4698), effectively erasing audit trails of prior activity, as well as overflow Security Logs.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Specifically, this involves registering a task with an [author](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-author-registrationinfotype-element) with the name, say, where the letter A is repeated 3,500 times, in the XML file, causing the entire XML task log description to be overwritten. This behavior could then be extended further to overwrite the whole "C:\Windows\System32\winevt\logs\[Security.evtx](https://attack.mitre.org/techniques/T1070/001/)" database.

"The Task Scheduler is a very interesting component. Accessible by anyone willing to create a task, initiated by a SYSTEM running service, juggling between the privileges, the process integrities and user impersonations," Enkaoua said.

"The first reported vulnerability is not only a UAC Bypass. It is far more than that: it is essentially a way to impersonate any user with its password from CLI and to obtain the maximum granted privileges on the task execution session, with the /ru and /rp flags."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[Task Scheduler](https://thehackernews.com/search/label/Task%20Scheduler)[UAC Bypass](https://thehackernews.com/search/label/UAC%20Bypass)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern...