---
title: Multi-Stage Phishing Campaign Targets Russia with Amnesia RAT and Ransomware
url: https://thehackernews.com/2026/01/multi-stage-phishing-campaign-targets.html
source: The Hacker News
date: 2026-01-24
fetch_date: 2026-01-25T03:56:38.901199
---

# Multi-Stage Phishing Campaign Targets Russia with Amnesia RAT and Ransomware

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

# [Multi-Stage Phishing Campaign Targets Russia with Amnesia RAT and Ransomware](https://thehackernews.com/2026/01/multi-stage-phishing-campaign-targets.html)

**Ravie Lakshmanan**Jan 24, 2026Ransomware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipVK-eTPu0vfv8p-slHnoh8LJka5_l-zmd82fTCO2rB8yxGFPRArabSzbI5LWzMskPr6UWf79uQ9fiHvVzY7eDB0Kj0cQIFZQEVSYJv-2nhqZJeNdnlZTp_I3e3tDePl7El94WvXFz4U-alGCONeTaxYRGWUNxhY1L0Osoq2hgl3pUghnPGbc5YK-XVVLj/s1600-e365/github-chain.jpg)

A new multi-stage phishing campaign has been observed targeting users in Russia with ransomware and a remote access trojan called Amnesia RAT.

"The attack begins with social engineering lures delivered via business-themed documents crafted to appear routine and benign," Fortinet FortiGuard Labs researcher Cara Lin [said](https://www.fortinet.com/blog/threat-research/inside-a-multi-stage-windows-malware-campaign) in a technical breakdown published this week. "These documents and accompanying scripts serve as visual distractions, diverting victims to fake tasks or status messages while malicious activity runs silently in the background."

The campaign stands out for a couple of reasons. First, it uses multiple public cloud services to distribute different kinds of payloads. While GitHub is mainly used to distribute scripts, binary payloads are staged on Dropbox. This separation complicates takedown efforts, effectively improving resilience.

Another "defining characteristic" of the campaign, per Fortinet, is the operational abuse of [defendnot](https://thehackernews.com/2025/05/weekly-recap-zero-day-exploits-insider.html#:~:text=New%20%22defendnot%22%20Tool%20Can%20Disable%20Windows%20Defender) to disable Microsoft Defender. [Defendnot](https://binarydefense.com/resources/blog/defendnot-turning-windows-defender-against-itself) was [released](https://www.huntress.com/blog/defendnot-detecting-malicious-security-product-bypass-techniques) last year by a security researcher who goes by the online alias es3n1n as a way to trick the security program into believing another antivirus product has already installed on the Windows host.

The campaign leverages social engineering to distribute compressed archives, which contain multiple decoy documents and a malicious Windows shortcut (LNK) with Russian-language filenames. The LNK file uses a double extension ("Задание\_для\_бухгалтера\_02отдела.txt.lnk") to give the impression that it's a text file.

When executed, it runs a PowerShell command to retrieve the next-stage PowerShell script hosted on a GitHub repository ("github[.]com/Mafin111/MafinREP111"), which then serves as a first-stage loader to establish a foothold, readies the system to hide evidence of malicious activity, and hands off control flow to subsequent stages.

"The script first suppresses visible execution by programmatically hiding the PowerShell console window," Fortinet said. "This removes any immediate visual indicators that a script is running. It then generates a decoy text document in the user's local application data directory. Once written to disk, the decoy document is automatically opened."

Once the document is displayed to the victim to keep up the ruse, the script sends a message to the attacker using the [Telegram Bot API](https://core.telegram.org/bots/api), informing the operator that the first stage has been successfully executed. A deliberately-introduced 444 second delay later, the PowerShell script runs a Visual Basic Script ("SCRRC4ryuk.vbe") hosted at the same repository location.

This offers two crucial advantages in that it keeps the loader lightweight and allows the threat actors to update or replace the payload's functionality on the fly without having to introduce any changes to the attack chain itself.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The Visual Basic Script is highly obfuscated and acts as the controller that assembles the next-stage payload directly in memory, thereby avoiding leaving any artifacts on disk. The final-stage script checks if it's running with elevated privileges, and, if not, repeatedly displays a User Account Control ([UAC](https://thehackernews.com/2026/01/fake-booking-emails-redirect-hotel.html)) prompt to force the victim to grant it the necessary permissions. The script pauses for 3,000 milliseconds between attempts.

In the next phase, the malware initiates a series of actions to suppress visibility, neutralize endpoint protection mechanisms, conduct reconnaissance, inhibit recovery, and ultimately deploy the main payloads -

* Configure Microsoft Defender exclusions to prevent the program from scanning ProgramData, Program Files, Desktop, Downloads, and the system temporary directory
* Use PowerShell to turn off additional Defender protection components
* Deploy defendnot to register a fake antivirus product with the Windows Security Center interface and cause Microsoft Defender to disable itself to avoid potential conflicts
* Conduct environment reconnaissance and surveillance via screenshot capture by means of a dedicated .NET module downloaded from the GitHub repository that takes a screengrab every 30 seconds, save it as a PNG image, and exfiltrates the data using a Telegram bot
* Disable Windows administrative and diagnostic tools by tampering with the Registry-based policy controls
* Implement a file association hijacking mechanism such that opening files with certain predefined extensions causes a message to be displayed to the victim, instructing them to contact the threat actor via Telegram

One of the final payloads deployed after successfully disarming security controls and recovery mechanisms is Amnesia RAT ("svchost.scr"), which is retrieved from Dropbox and is capable of broad data theft and remote control. It's designed to pilfer information stored in web browsers, cryptocurrency wallets, Discord, Steam, and Telegram, along with system metadata, screenshots, webcam images, microphone audio, clipboard, and active window title.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS3LjzY-kPQNYkUOzIYRw2AJ3ULqoUvEXnzMoOu6i0LJcVhen0Htlrh88MnarHpuhzA_UGJ4ypzxjcGBIEEa9yhq5FkpYN-5mpVA5sLU2o7Zi68fnn0yDAphgcEpweh5MQNa7GNglUJZh_twv2AgvS0z5sv7f-U55iL_8WItFtYm-L9Ji0LmXzlWa4hwvZ/s1600-e365/telegram.pn...