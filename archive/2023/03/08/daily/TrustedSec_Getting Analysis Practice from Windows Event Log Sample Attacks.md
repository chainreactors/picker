---
title: Getting Analysis Practice from Windows Event Log Sample Attacks
url: https://www.trustedsec.com/blog/getting-analysis-practice-from-windows-event-log-sample-attacks/
source: TrustedSec
date: 2023-03-08
fetch_date: 2025-10-04T08:57:08.010011
---

# Getting Analysis Practice from Windows Event Log Sample Attacks

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Getting Analysis Practice from Windows Event Log Sample Attacks](https://trustedsec.com/blog/getting-analysis-practice-from-windows-event-log-sample-attacks)

March 07, 2023

# Getting Analysis Practice from Windows Event Log Sample Attacks

Written by
Thomas Millar

Incident Response
Incident Response & Forensics

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AnalysisPracticeWindowsEventLogSampleAttack_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695564084&s=d138784b130edda7f487b37371aab3e2)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#330c404651595650470e705b5650581601035c4647160103475b5a401601035241475a505f5616010355415c5e1601036741464047565760565016010215525e4308515c574a0e745647475a5d54160103725d525f4a405a4016010363415250475a505616010355415c5e160103645a5d575c44401601037645565d471601037f5c5416010360525e435f56160103724747525058401600721601035b47474340160072160175160175474146404756574056501d505c5e160175515f5c54160175545647475a5d541e525d525f4a405a401e43415250475a50561e55415c5e1e445a5d575c44401e5645565d471e5f5c541e40525e435f561e52474752505840 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fgetting-analysis-practice-from-windows-event-log-sample-attacks "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Getting%20Analysis%20Practice%20from%20Windows%20Event%20Log%20Sample%20Attacks%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fgetting-analysis-practice-from-windows-event-log-sample-attacks "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fgetting-analysis-practice-from-windows-event-log-sample-attacks&mini=true "Share on LinkedIn")

Throughout my career as an Incident Responder, one of the most invaluable skillsets I have had to draw on has been analysis of Windows event logs. These event logs are an invaluable source of information to forensic practitioners, as they are crucial in determining the cause of events during computer security incidents. Windows event logs hold a great amount of varying data for how the system is functioning, the occurrences for both legitimate users and their activities, and what happens when attackers enter the arena. With respect to log analysis, I maintain that the event logs are valuable not only for helping you find ‘badness’, but also for teaching you important fundamentals about Windows system internals.

To practice your detection and analysis skills to find such badness, it’s helpful to have a set of event log samples that represent actual attack data and explore different ways to apply your knowledge and analysis techniques. The scope of this article will involve attack samples for the Windows platform. These are event log files that reflect different types of attacks stored within the event data. Each of them can be browsed through by mostly anyone, and the end results are that you walk away knowing a bit more about attacks that you might not have encountered before, and now you have log data to explore and learn from.

To retrieve the log files, I will be using in this demonstration, you can find them on GitHub under the following link: <https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES>. After downloading them, browse around within the folder groupings to see what they offer. The event log samples are grouped by different MITRE ATT&CK attacker techniques and tactics such as ‘defense evasion’, ‘credential access’, ‘lateral movement’, and others.

Below, I have identified some records that trigger a ‘Malicious Named Pipe’ rule. You should see that these are rated as a critical severity, so we will focus in on them throughout this article. A snippet of some that looked appealing to me is shown immediately below using a Python tool that applies Sigma rules for identifying and classifying suspicious events.

![](https://www.trustedsec.com/wp-content/uploads/2023/03/Millar_1.png)

We can dive in a bit more using the native Windows Event Viewer. It may be beneficial to explore using other tools; however, for the purposes of this blog entry, we will primarily be using the Event Viewer. Additionally, the event log source we will focus on will be System Monitor (Sysmon) logs, which are not native to Windows; they are an add-on but also highly desired to IR, as they provide a higher level of event monitoring.

![](https://www.trustedsec.com/wp-content/uploads/2023/03/Millar_2.png)

After navigating to the prospective log file, we can open up the events that are filtered specifically for the attack concer...