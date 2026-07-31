---
title: ThreatsDay: AI-Powered Hacking, 370 Chrome Flaws, SonicWall Attacks, DNS Hijacking + 22 More Stories
url: https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html
source: The Hacker News
date: 2026-07-30
fetch_date: 2026-07-31T05:31:17.092217
---

# ThreatsDay: AI-Powered Hacking, 370 Chrome Flaws, SonicWall Attacks, DNS Hijacking + 22 More Stories

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

# [ThreatsDay: AI-Powered Hacking, 370 Chrome Flaws, SonicWall Attacks, DNS Hijacking + 22 More Stories](https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html)

**Ravie Lakshmanan**Jul 30, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNfPEjoHY1NDIrmCVPaZ_dmWbOk0MZwMlh6Odxpqfchn-5rOvsj4PhaBZs4LJvoj5iXhgbBTZzKCNYOPbblXU6kSnVNxEfQER6bNIuhROsSBTrhS6P_mPySTbAS5CvbYgu7lOANl0C6YuLR92om_sS_-9skmNqYT4BDmy_07cTMVj75vUUES70gPicrgGW/s1700-e365/threatsday.jpg)

A lot of security still comes down to trusting the wrong screen.

This week, that screen might be a login page, an install guide, a recruiter call, or a familiar service behaving slightly wrong. Behind it: reused credentials, exposed systems, quiet loaders, abused trust, and exploit paths that should have been harder.

Some defenses improved. The loose parts still got found first. Anyway, here's the mess.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. Phishing delivers XWorm

   [Xplogs22 Targets Russia with XWorm](https://www.f6.ru/blog/xplogs22/)

   A cybercrime group known as xplogs22 has been  [observed](https://www.f6.ru/blog/xplogs22/)  targeting Russia and other CIS countries with phishing emails that deliver Xworm. The group, per F6, is believed to have been active since November 2023. Prior attacks mounted by the threat actors leveraged Formbook and Snake Keylogger, before switching to XWorm around July 2025. In recent months, Russian customers of the banking sector have also been targeted by an Android trojan called  [LunaSpy](https://www.f6.ru/blog/lunaspy-android-research/)  as part of social engineering attacks. LunaSpy can capture camera streams, record audio and the screen, and collect sensitive data. The malware is disguised as an antivirus application to evade detection.
2. Custom ransomware targets Russia

   [Toy Ghouls Come Back with GenieLocker Ransomware](https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/)

   The financially motivated extortion group known as [Toy Ghouls](https://thehackernews.com/2026/03/bearlyfy-hits-70-russian-firms-with.html) (aka Bearlyfy and Labubu) has targeted organizations in the Russian Federation, primarily in the manufacturing, financial services, retail, and technology sectors, with a custom ransomware family called GenieLocker since March 2026. According to Kaspersky, the group previously relied on third-party encryptors like RedAlert, LockBit, and Babuk. "GenieLocker, apparently a custom design, upgrades their toolkit and reduces their reliance on third-party software," Kaspersky [said](https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/). In at least one case, initial access to the target environment was obtained via an OpenVPN connection originating from an external partner's network, with the attackers likely exploiting the trusted relationship to breach the target, conduct reconnaissance, deliver additional tools for credential harvesting, and perform lateral movement via RDP and SSH to reach other Windows and Linux hosts. "During the impact phase, the attackers encrypted files on the compromised Windows machines with the PE version of the GenieLocker ransomware," Kaspersky said. "On the compromised Linux and ESXi servers, they stopped active virtual machines and encrypted their disks using the ELF version of GenieLocker." Details of the activity were [first highlighted](https://thehackernews.com/2026/03/bearlyfy-hits-70-russian-firms-with.html) by F6 in March 2026.
3. Crypto-stealing payloads deployed

   [CastleLoader Delivers Needle Stealer](https://arcticwolf.com/resources/blog/castleloader-new-campaigns-new-tooling-and-the-needlestealer-connection/)

   The malware loader known as [CastleLoader](https://thehackernews.com/2025/12/four-threat-clusters-using-castleloader.html), which has been previously used to deliver [CastleStealer](https://thehackernews.com/2026/06/new-oxloader-loader-uses-malicious.html) and a Python-based [remote access trojan](https://www.levelblue.com/blogs/spiderlabs-blog/clickfix-is-now-hiring-from-job-platform-impersonation-to-python-based-rat-delivery) (RAT) via ClickFix-style lures, has now been used to distribute two payloads tied to the [Needle Stealer](https://thehackernews.com/2026/05/threatsday-bulletin-edge-plaintext.html#fake-ai-app-malware-wave) framework: a Rust-based desktop wallet spoofer, and a Golang-based malicious browser extension installer. Arctic Wolf [said](https://arcticwolf.com/resources/blog/castleloader-new-campaigns-new-tooling-and-the-needlestealer-connection/) it also identified a new shellcode loader variant spreading via digitally signed installers. The campaign has been codenamed Noidret. The introduction of these new tools is seen as an attempt to focus on cryptocurrency-specific targeting and establish browser-level persistence.
4. Fileless WebDAV execution

   [ClickFix Continues to Evolve](https://www.cyberproof.com/blog/clickfix-keeps-evolving-rundll32-ordinal-execution-over-webdav/)

   Speaking of ClickFix, CyberProof said it tracked a ClickFix variant that involves tricking victims into pasting a single command into the Windows Run dialog, which then communicates with a WebDAV endpoint and uses rundll32.exe to load a remote, non-DLL payload and call its first export by ordinal without having to leave any artifacts on disk. "The payload (gc.key, j.pm, or goog.ct) is a file served from the attacker WebDAV share and is not a standard DLL by extension," CyberProof [said](https://www.cyberproof.com/blog/clickfix-keeps-evolving-rundll32-ordinal-execution-over-webdav/). "It is invoked by rundll32.exe through ordinal #1, which runs its primary routine while keeping the export name off the command line."
5. Fake Claude guide spreads malware

   [Fake Claude Install Guide Leads to MacSync Stealer](https://www.hu...