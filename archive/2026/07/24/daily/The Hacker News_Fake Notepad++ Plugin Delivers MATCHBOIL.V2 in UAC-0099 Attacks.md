---
title: Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks
url: https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html
source: The Hacker News
date: 2026-07-24
fetch_date: 2026-07-25T05:00:49.764026
---

# Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html)

**Ravie Lakshmanan**Jul 24, 2026Cyber Espionage / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCA0-yh9EAnhFa2V3NzQVw2m-sLgbCNVQ8GVMBX4Y6vUNwPXE-vHzdJLFKXVi3rdGXhx5RawHTwox7cd9ph20u5qn_H8TJUOKG8nITccTkzqfiyBKStdCgcrJOgAeGf9Mkzr1g8iCB0HrpuonkIQQTx15L2P53RPX9GeMYVIuvl51jJ2hn1jn0PcQARQaj/s1700-e365/notepad-malware-code.jpg)

The Computer Emergency Response Team of Ukraine (CERT-UA) has [warned](https://cert.gov.ua/article/6318634) of a new campaign that involves the use of a malicious program that's dressed up as a Notepad++ plugin to compromise Windows systems.

The activity has been attributed by the agency to a threat cluster it tracks as **[UAC-0099](https://thehackernews.com/2023/12/uac-0099-using-winrar-exploit-to-target.html)**, a [Russia-aligned group](https://www.eset.com/us/about/newsroom/research/eset-research-investigates-russian-aligned-gamaredon-group-2025/) that has previously observed weaponizing security flaws in WinRAR software to deliver a malware strain called LONEPAGE. Other cyber attacks mounted by the adversary have [employed](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html) phishing emails as an initial access method to deploy MATCHBOIL, MATCHWOK, and DRAGSTARE. It's known to be active since at least mid-2022.

The latest set of attacks begins, observed earlier this summer, with a phishing email containing an image attachment, which, when clicked, opens a URL that's concealed using a link shortener from where the request is sent to a file-sharing service like EasySend[.]co to retrieve a ZIP archive.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The ZIP file contains a Visual Basic Script (VBScript) that masquerades as a PDF document. Attempting to launch it will cause a decoy PDF to be downloaded and displayed to the victim as a distraction mechanism, while it silently downloads a second archive named "Evernote.zip." The archive includes multiple components -

* A complete copy of the legitimate editor Notepad++ version 8.8.3
* A malicious DLL plugin ("NppExport.dll")
* A password-protected archive ("updater.rar")
* Legitimate WinRAR executable ("winrar.exe")

The primary goal of the VBScript is to extract the contents of the archive and launch Notepad++, which, in turn, loads "NppExport.dll." Codenamed LUNCHPOKE, the DLL is designed to unpack the RAR archive, which contains "RemoteLibUpdater.exe" and "InitTest.dll," to a specific directory, set up persistence by means of a scheduled task to run "RemoteLibUpdater.exe" every three minutes.

The "RemoteLibUpdater.exe" binary is BURNYBEAR, which serves as a loader for "InitTest.dll," a modified version of [MATCHBOIL](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html), a C#-based loader capable of delivering secondary payloads. The new version has been codenamed MATCHBOIL.V2.

"At the same time, if 'RemoteLibUpdater.exe' is launched incorrectly, namely without specifying arguments, BURNYBEAR instead activates logic designed to exhaust computer resources (RAM and processor)," CERT-UA said.

CERT-UA is recommending that organizations update their WinRAR, 7-Zip, and Notepad++ software to the latest versions to prevent threat actors from exploiting any known vulnerabilities to facilitate follow-on attacks.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5ULiK2c7eL5isjO3O6NWXaCFL4sc8Znxd0LnivmJIcRXay0i8YzapqwH6odHGGrL0H0dj6lPuDzhDGBkwUR6XE2RIoMk2ukPzOIDfUBn84oI10M5Sx4sZsmmIx29NcAA0SsUfDNAuVHDP2lFoz7bKw48wk2onJH9-4udbqS8Giuyvh36pWFAMmmrA1Wyj/s1700-e365/notepad.png)

The disclosure comes as the U.S. government [highlighted](https://thehackernews.com/2026/07/russian-espionage-group-exploited.html) a phishing campaign orchestrated by the Russia-linked threat actor called [Laundry Bear](https://thehackernews.com/2026/01/pluggyape-malware-uses-signal-and.html) (aka CL-STA-1114, TA488, UNK\_PitStop, and Void Blizzard) targeting Zimbra mail servers belonging to Western government and commercial organizations since at least July 2025.

The campaign employs a novel "half-click" exploit that abuses CVE-2025-66376 to deliver malicious JavaScript dubbed ZimReaper capable of harvesting email communications and other sensitive data.

"Unlike traditional phishing campaigns that persuade a user into taking an action, such as clicking a link or opening a file, Laundry Bear's latest campaign leverages a view-based exploit that only requires a user to view a malicious email within a vulnerable version of the webmail service," the U.S. government said.

"The covert and persistent nature of this activity, along with the absence of any known financial extortion, almost certainly indicates this group's involvement in espionage activities with Russian government backing. Additionally, extensive Ukrainian targeting, prior to use against U.S. and other NATO allies, outlines an increasing trend within Russian cyber threat groups to target Ukrainian users first-both as a priority target and as a test bench for malicious cyber techniques before broader global deployment."

The disclosure also follows a [report](https://www.proofpoint.com/us/blog/threat-insight/ta458-roundpress-exploits) from Proofpoint about Russian threat actor's continued webmail targeting using half-click cross-site scripting (XSS) exploits to siphon valuable data as part of a campaign referred to as [Operation RoundPress](https://thehackernews.com/2025/05/russia-linked-apt28-exploited-mdaemon.html). The email security company is tracking the activity as TA458.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNP...