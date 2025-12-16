---
title: Phantom Stealer Spread by ISO Phishing Emails Hitting Russian Finance Sector
url: https://thehackernews.com/2025/12/phantom-stealer-spread-by-iso-phishing.html
source: The Hacker News
date: 2025-12-15
fetch_date: 2025-12-16T03:24:40.562377
---

# Phantom Stealer Spread by ISO Phishing Emails Hitting Russian Finance Sector

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Phantom Stealer Spread by ISO Phishing Emails Hitting Russian Finance Sector](https://thehackernews.com/2025/12/phantom-stealer-spread-by-iso-phishing.html)

**Dec 15, 2025**Ravie LakshmananMalware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglC802fHbjYDV11Y3NmxnCVUJfKSNEDRXAtOM722x09s0GmNQF11fP-r7betDJE1NOMAXe9DcIyEGYlWLMFf8S2B3pMRcLtLuGqqYovFNSGfnruQbydlAzRhpYQgKTZrYR68RcpYTJRjUEHTBDLDANrBWUx2zYhtcm28f7njmIuqHXI36W9omWtuD8AeFC/s790-rw-e365/email.jpg)

Cybersecurity researchers have disclosed details of an active phishing campaign that's targeting a wide range of sectors in Russia with phishing emails that deliver [Phantom Stealer](https://thehackernews.com/2025/09/noisy-bear-targets-kazakhstan-energy.html#cyber-attacks-reported-against-russia) via malicious ISO optical disc images.

The activity, codenamed Operation MoneyMount-ISO by Seqrite Labs, has primarily singled out finance and accounting entities, with those in the procurement, legal, payroll verticals emerging as secondary targets.

"This campaign employs a fake payment confirmation lure to deliver the Phantom information-stealing malware through a multi-stage attachment chain," the cybersecurity company [said](https://www.seqrite.com/blog/operation-moneymount-iso-deploying-phantom-stealer-via-iso-mounted-executables/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

The infection chain begins with a phishing email that masquerades as legitimate financial communications, urging recipients to confirm a recent bank transfer. Attached to the email is a ZIP archive that claims to contain additional details, but, instead, contains an ISO file that, when launched, mounts on the system as a virtual CD drive.

The ISO image ("Подтверждение банковского перевода.iso" or "Bank transfer confirmation.iso") serves as an executable that's designed to launch Phantom Stealer by means of an embedded DLL ("CreativeAI.dll").

Phantom Stealer is capable of extracting data from cryptocurrency wallet browser extensions installed in Chromium-based browsers and desktop wallet apps, as well as grab files, Discord authentication tokens, and browser-related passwords, cookies, and credit card details.

It also monitors clipboard content, logs keystrokes, and runs a series of checks to detect virtualized, sandboxed, or analysis environments, and if so, aborts its execution. Data exfiltration is achieved via a Telegram bot or to an attacker-controlled Discord webhook. On top of that, the stealer enables file transfer to an FTP server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBLb3eeGIbqDid9WQD04VDahWznMqMyShsmoXBapbaZn5ECGbgga2vjsynGGfO6Zf6G7AFatKhkKsV7elww5e4gZsxtMRIFBR8KTm9CyBSAnFNohv1iVY6OPcATbOJVZn14DxRPdjAhPjZ4wnUz2arCjaevAefQ2vzAIk_Dynj-E18JHcEAQzZSBBcFhdI/s790-rw-e365/phantom.jpg)

In recent months, Russian organizations, mainly human resources and payroll departments, have also been targeted by phishing emails that employ lures related to bonuses or internal financial policies to deploy a previously undocumented implant named DUPERUNNER that loads [AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html), an open-source command-and-control (C2) framework.

Dubbed [DupeHike](https://www.seqrite.com/blog/operation-dupehike-ung0902-targets-russian-employees-with-duperunner-and-adaptixc2/), the campaign has been attributed to a threat cluster named UNG0902.

"The ZIP has been used as a preliminary source of spear-phishing-based infection containing decoys with PDF and LNK extension, which downloads the implant DUPERUNNER, which finally executes the Adaptix C2 Beacon," Seqrite said.

The LNK file ("Документ\_1\_О\_размере\_годовой\_премии.pdf.lnk" or "Document\_1\_On\_the\_amount\_of\_the\_annual\_bonus.pdf.lnk"), in turn, proceeds to download DUPERUNNER from an external server using "powershell.exe." The primary responsibility of the implant is to retrieve and display a decoy PDF and launch AdaptixC2 by injecting it into a legitimate Windows process like "explorer.exe," "notepad.exe," and "msedge.exe."

Other phishing campaigns have taken aim at finance, legal, and aerospace sectors in Russia to distribute [Cobalt Strike](https://www.seqrite.com/blog/operation-frostbeacon-multi-cluster-cobalt-strike-campaign-targets-russia/) and malicious tools like Formbook, DarkWatchman, and PhantomRemote that are capable of data theft and hands-on keyboard control. The email servers of compromised Russian companies are used to send the spear-phishing messages.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

French cybersecurity company Intrinsec has attributed the intrusion set targeting the Russian aerospace industry to hacktivists aligned with Ukrainian interests. The activity, detected between June and September 2025, shares overlaps with [Hive0117](https://thehackernews.com/2025/05/darkwatchman-sheriff-malware-hit-russia.html), [Operation CargoTalon](https://thehackernews.com/2025/07/cyber-espionage-campaign-hits-russian.html), and [Rainbow Hyena](https://thehackernews.com/2025/07/weekly-recap-sharepoint-0-day-chrome.html#:~:text=Rainbow%20Hyena%20Goes%20After%20Russian%20Firms) (aka Fairy Trickster, Head Mare, and PhantomCore).

Some of these efforts have also been found to redirect users to phishing login pages hosted on the InterPlanetary File System ([IPFS](https://thehackernews.com/2022/11/several-cyber-attacks-observed.html)) and Vercel, designed to steal credentials associated with Microsoft Outlook and Bureau 1440, a Russian aerospace company.

"The campaigns observed between June and September 2025 [...] aimed at compromising entities actively cooperating with Russia's army amidst the current conflict with Ukraine, largely assessed by the Western sanctions imposed on them," Intrinsec [said](https://www.intrinsec.com/campaigns-targeting-the-aerospace-industry-in-russia/).

Found this article int...