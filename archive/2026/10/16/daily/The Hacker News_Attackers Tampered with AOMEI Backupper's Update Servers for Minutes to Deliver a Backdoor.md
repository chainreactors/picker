---
title: Attackers Tampered with AOMEI Backupper's Update Servers for Minutes to Deliver a Backdoor
url: https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html
source: The Hacker News
date: 2026-10-16
fetch_date: 2026-10-17T06:39:13.618352
---

# Attackers Tampered with AOMEI Backupper's Update Servers for Minutes to Deliver a Backdoor

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Attackers Tampered with AOMEI Backupper's Update Servers for Minutes to Deliver a Backdoor](https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html)

**Swati Khandelwal**Oct 16, 2026Supply Chain Attack / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhuPumyjeBRpQZo5_3mvqZ2_kXuPiOK02cH-ARofYrny0mQ2-rv55w7yBxMTBe3ymCW7c77quZ4xlkdDG9FcEhBYFr7GWmbyPE_1K1xqU0mvT-h51Z8hLg-LnWl32MeOy-aumsGO9-j8VSOSOfVUDB2k1vWOpEdyGEWV9ipF4kf3HVP1Au2ClbkYtAJrc/s1700-nu-rw-lo-l85-e365/backup-hacked.jpg)

Attackers repeatedly changed the files that AOMEI Backupper fetches from the vendor's own update servers, in windows of five to ten minutes at a time between May and July 2026, so that any copy of the Windows backup program that checked for an update during one of those windows would download and run a backdoor.

[Google Threat Intelligence Group, Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering), and [ManageEngine's Threat Analysis Lab](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html), which disclosed the campaign this week, say AOMEI has reported fixing its servers, but that fix does not remove the backdoor from machines that were already hit.

AOMEI Backupper is Windows backup and disk-cloning software made by AOMEI Technology, a vendor registered in Hong Kong. Like the company's remote-desktop tool AnyViewer, it runs background services that regularly check AOMEI's servers over HTTPS for software updates and promotional pop-ups.

Two files drive that check. One, down\_html.ini, names the update package to download and the checksum the program uses to verify it. The other, Notifycfg.ini, tells the pop-up service what to display and what to run.

The program does not cryptographically verify either file, and the checksum that is supposed to prove the download is genuine sits inside the same unsigned file that names it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

Nothing in the software was exploited. There was no vulnerability, and no user action was needed beyond having the program installed and running, according to ManageEngine's lab. The attacker only had to change two text files on the server for a few minutes.

A copy of Backupper that checked in during a window pulled the attacker's package into its own folder, and the notification file then made it run. It ran with the privileges of the AOMEI process that launched it.

On the machines the lab examined, that was enough to install software across the whole system, though it said the elevation depended on how the AOMEI service was running.

### Three Windows, Eleven Countries

GTIG and Mandiant confirmed three tampering windows, and said more probably happened that they did not see:

* May 28, 2026: a 10-minute window, 05:40 to 05:50 UTC
* July 16, 2026: a 6-minute window, 08:33 to 08:39 UTC
* July 20, 2026: a 5-minute window, 10:35 to 10:40 UTC

Only copies that checked for an update during a window were affected. A copy that checked before or after got clean, genuine files, which is what makes the attack hard to catch. GTIG described the targeting as opportunistic, hitting whatever system happened to poll during those minutes.

From its own telemetry, GTIG identified affected organizations in IT services, telecommunications and higher education across 11 countries: Australia, Brazil, India, Pakistan, Portugal, Singapore, South Africa, Spain, Switzerland, Türkiye and the United States. It gave no total and said the real number is likely higher.

GTIG named AnyViewer, AOMEI's remote-desktop tool, as using the same update flow, but the detections it describes involve Backupper. Neither report lists which Backupper versions are affected, and the lab examined version 8.3.0.

GTIG tracks the group behind the campaign as UNC7017 and names no country or known actor. It said this is the first supply chain compromise it has encountered built on Windows this short, "effectively evading traditional point-in-time triage and automated file scanning."

### What Landed on the Machine

On a machine that pulled the package, a downloader that GTIG calls CROSSROAD unpacked a bundle into a local Radmin folder, created a scheduled task set to run every three hours, and then deleted itself from disk.

The bundle included a genuine, signed copy of Radmin, a commercial remote-administration tool. ManageEngine's lab found it staged but never switched on, with no listener, no configuration, and no new account. The remote control came instead from a separate implant that reached out to the attacker.

The scheduled task runs the signed Radmin program, which loads an attacker-built DLL placed beside it, which in turn loads the SHINYROAD implant. The implant gives a remote shell and can fetch and run new code on command. It talks to a single hard-coded address with no backup, so blocking that one address cuts off the attacker's control.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj58Ya_nWI2eG16TGbDum201rk0BU654-Iz7S7zYdJdB2w-aIJIc5eas6GDHzYfjnrv-5tLZm5YdyvLU6kNe5bSPOEYAbF2j56zrDg0uL1n6X2anZa3O2zBpYi85zH7ADPW0cQ8_jiZYUb5JnT0Mj1eJLASxlXB11JHnu3ACebotwG3oAVjnM3ic3qf0w/s1700-nu-rw-lo-l85-e365/backup.png)

CROSSROAD runs only in some places. It checks the machine's location and stops if it is in China, and ManageEngine added that it also stops if it finds particular security agents on the host. On machines that passed those checks, GTIG later saw a second tool pushed down on top of SHINYROAD, the open-source [Adaptix C2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html) framework, disguised as Nitro PDF software.

### A July 20 Change That Needed No Code to Run

The July 20 window included a second trick that did not require running any program. GTIG...