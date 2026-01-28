---
title: ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted Web Services
url: https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html
source: The Hacker News
date: 2026-01-27
fetch_date: 2026-01-28T03:35:27.439270
---

# ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted Web Services

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

# [ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted Web Services](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html)

**Ravie Lakshmanan**Jan 27, 2026Malware / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW6W_rux-XGbdn40S_idHK9NuIPQ9Apvc-2JZAvLaHngDYeb5gvSFLF0A4Fds4fpAZqOdeavVBdL0mpSYS3uuIZ7x_w4cdViWRc8e8SoHUkCcfrTxWCm-i8-g63Xn7wgF3IEs21EWyAYn3m719zUh66sCrVOjCaKNJrkoI6q_LwayxogECmwHCKjQS-HO6/s1700-e365/clickfix.jpg)

Cybersecurity researchers have disclosed details of a new campaign that combines [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)-style fake CAPTCHAs with a signed Microsoft Application Virtualization ([App-V](https://learn.microsoft.com/en-us/microsoft-desktop-optimization-pack/app-v/appv-for-windows)) script to distribute an information stealer called [Amatera](https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html).

"Instead of launching PowerShell directly, the attacker uses this script to control how execution begins and to avoid more common, easily recognized execution paths," Blackpoint researchers Jack Patrick and Sam Decker [said](https://blackpointcyber.com/blog/novel-fake-captcha-chain-delivering-amatera-stealer/) in a report published last week.

In doing so, the idea is to transform the App-V script into a living-off-the-land (LotL) binary that proxies the execution of PowerShell through a trusted Microsoft component to conceal the malicious activity.

The starting point of the attack is a fake CAPTCHA verification prompt that seeks to trick users into pasting and executing a malicious command on the Windows Run dialog. But here is where the attack diverges from traditional ClickFix attacks.

The supplied command, rather than invoking PowerShell directly, abuses "[SyncAppvPublishingServer.vbs](https://lolbas-project.github.io/lolbas/Scripts/Syncappvpublishingserver/)," a signed Visual Basic Script associated with App-V to retrieve and execute an in-memory loader from an external server using "wscript.exe."

It's worth noting that the misuse of "SyncAppvPublishingServer.vbs" is not new. In 2022, two different threat actors from China and North Korea, tracked as [DarkHotel](https://thehackernews.com/2022/03/south-korean-darkhotel-hackers-targeted.html) and [BlueNoroff](https://thehackernews.com/2022/12/bluenoroff-apt-hackers-using-new-ways.html), were observed leveraging the LOLBin exploit to stealthily execute a PowerShell script. But this is the first time it has been observed in ClickFix attacks.

"Adversaries may abuse SyncAppvPublishingServer.vbs to bypass PowerShell execution restrictions and evade defensive counter measures by 'living off the land,'" MITRE [notes](https://attack.mitre.org/techniques/T1216/002/) in its ATT&CK framework. "Proxying execution may function as a trusted/signed alternative to directly invoking 'powershell.exe.'"

The use of an App-V script is also significant as the virtualization solution is built only into Enterprise and Education editions of Windows 10 and Windows 11, along with modern Windows Server versions. It's not available for Windows Home or Pro installations.

In Windows operating systems where App-V is either absent or not enabled, the execution of the command fails outright. This also indicates that enterprise managed systems are likely the primary targets of the campaign.

The obfuscated loader runs checks to ensure that it's not run within sandboxed environments, and then proceeds to fetch configuration data from a public Google Calendar (ICS) file, essentially turning a trusted third-party service into a [dead drop resolver](https://attack.mitre.org/techniques/T1102/001/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

"By externalizing configuration in this way, the actor can rapidly rotate infrastructure or adjust delivery parameters without redeploying earlier stages of the chain, reducing operational friction and extending the lifespan of the initial infection vector," the researchers pointed out.

Parsing the calendar event file leads to the retrieval of additional loader stages, including a PowerShell script that functions as an intermediate loader to execute the next stage, another PowerShell script, directly in memory. This step, in turn, results in the retrieval of a PNG image from domains like "gcdnb.pbrd[.]co" and "iili[.]io" via WinINet APIs that conceals an encrypted and compressed PowerShell payload.

The resulting script is decrypted, GZip decompressed in memory, and run using Invoke-Expression, ultimately culminating in the execution of a shellcode loader that's designed to launch Amatera Stealer.

"What makes this campaign interesting isn't any single trick, but how carefully thought-out everything is when chained together," Blackpoint concluded. "Each stage reinforces the last, from requiring manual user interaction, to validating clipboard state, to pulling live configuration from a trusted third-party service."

"The result is an execution flow that only progresses when it unfolds (almost) exactly as the attacker expects, which makes both automated detonation and casual analysis significantly harder."

### The Evolution of ClickFix: JackFix, CrashFix, and GlitchFix

The disclosure comes as ClickFix has become one of the most widely used initial access methods in the last year, accounting for 47% of the attacks observed by Microsoft.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhP27LWF5aO5Os7An9WAdWRVGbHse0sLTS7W4eChxZepnbMjGz2uPfehyphenhyphenFqJE94XQ_btoInRt0xnkjnXpIV5G4T9Mmc9fqluwN4zjYWNfbVbPt1U0Gkn_KmHlr9PU5DhjodckVdBvQ5Yh81te56GeZhD5KOf8xwpklHdZyRtfdipxbNDmg68SCwzLVyYHkH/s1700-e365/facebook.jpg)

Recent ClickFix campaigns have [targeted](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2025-12-18-phishing-for-authentication-tokens.txt) social media content creators by claiming they are eligible for free verified badges, instructing them via videos to copy authentication tokens from their browser cookies into a fake form to complete the supposed verification process. The embedded video also informs the user to "not log out for at least 24 hours" to keep the authentication tokens valid.

The campaign, active...