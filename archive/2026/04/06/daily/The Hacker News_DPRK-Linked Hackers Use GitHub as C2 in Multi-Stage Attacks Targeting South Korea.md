---
title: DPRK-Linked Hackers Use GitHub as C2 in Multi-Stage Attacks Targeting South Korea
url: https://thehackernews.com/2026/04/dprk-linked-hackers-use-github-as-c2-in.html
source: The Hacker News
date: 2026-04-06
fetch_date: 2026-04-07T04:30:41.780882
---

# DPRK-Linked Hackers Use GitHub as C2 in Multi-Stage Attacks Targeting South Korea

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [DPRK-Linked Hackers Use GitHub as C2 in Multi-Stage Attacks Targeting South Korea](https://thehackernews.com/2026/04/dprk-linked-hackers-use-github-as-c2-in.html)

**Ravie Lakshmanan**Apr 06, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh23Q23hk6n_d_f9evdsf7JVcn5OswTUqwd0B8EvWdftPQXN4K1V6nHICk_MvzLf4jUfCCHpUmaZIzECekbKf3PQ2w2gRlY-AphdBRZgyJHq7XQsyIS_vp6iT_fVLoDQ1TFA4DBLT32Q1sTY_WHjGRtzaYMOqMNThcg8JodZ-Aozj2OO21DQLj2agEojjdp/s1700-e365/github.jpg)

Threat actors likely associated with the Democratic People's Republic of Korea (DPRK) have been observed using GitHub as command-and-control (C2) infrastructure in multi-stage attacks targeting organizations in South Korea.

The attack chain, per [Fortinet FortiGuard Labs](https://www.fortinet.com/blog/threat-research/dprk-related-campaigns-with-lnk-and-github-c2), involves obfuscated Windows shortcut (LNK) files acting as the starting point to drop a decoy PDF document and a PowerShell script that sets the stage for the next phase of the attack. It's assessed that these LNK files are distributed via phishing emails.

As soon as the payloads are downloaded, the victim is displayed the PDF document, while the malicious PowerShell script runs silently in the background. The PowerShell script performs checks to resist analysis by scanning for running processes related to virtual machines, debuggers, and forensic tools. If any of those processes are detected, the script immediately terminates.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Otherwise, it extracts a Visual Basic Script (VBScript) and sets up persistence using a scheduled task that launches the PowerShell payload every 30 minutes in a hidden window to sidestep detection. This ensures that the PowerShell script is executed automatically after every system reboot.

The PowerShell script then profiles the compromised host, saves the result to a log file, and exfiltrates it to a GitHub repository created under the account "motoralis" using a hard-coded access token. Some of the GitHub accounts created as part of the campaign include "God0808RAMA," "Pigresy80," "entire73," "pandora0009," and "brandonleeodd93-blip."

The script then parses a specific file in the same GitHub repository to fetch additional modules or instructions, thus allowing the operator to weaponize the trust associated with a platform like GitHub to blend in and maintain persistent control over the infected host.

Fortinet said that earlier iterations of the campaign relied on LNK files to spread malware families like Xeno RAT. It's worth noting that the use of GitHub C2 to distribute Xeno RAT and its variant MoonPeak was documented by [ENKI](https://thehackernews.com/2025/07/north-korean-hackers-target-web3-with.html#kimsuky-s-use-of-clickfix-continues) and [Trellix](https://thehackernews.com/2025/08/north-korea-uses-github-in-diplomat.html) last year. These attacks were attributed to a North Korean state-sponsored group known as Kimsuky.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfY4RcwrXff9_9NLfQ2x9xSnE9mDyH4twfumUEbBaJGKgF8GaiwAiHllBJ6Dx2AjliQHxDlhJpr09SHuyernQhimTbRBv7t337-1CIssYzCQhGm7kczxnKdu7FGksqP4KswNDAzzFT9Xl-EVqZUbkXPIkb0emdHYR5HVnulYTgofqzI3eGylrjclzkfbPa/s1700-e365/git.png)

"Instead of depending on complex custom malware, the threat actor uses native Windows tools for deployment, evasion, and persistence," security researcher Cara Lin said. "By minimizing the use of dropped PE files and leveraging LolBins, the attacker can target a broad audience with a low detection rate."

The disclosure comes as AhnLab [detailed](https://asec.ahnlab.com/en/93151/) a similar LNK-based infection chain from Kimsuky that ultimately results in the deployment of a Python-based backdoor.

The LNK files, as before, execute a PowerShell script and create a hidden folder in the "C:\windirr" path to stage the payloads, including a decoy PDF and another LNK file that mimics a Hangul Word Processor (HWP) document. Also deployed are intermediate payloads to set up persistence and launch a PowerShell script, which then uses Dropbox as a C2 channel to fetch a batch script.

The batch file then downloads two separate ZIP file fragments from a remote server ("quickcon[.]store") and combines them together to create a single archive and extracts from it an XML task scheduler and a Python backdoor. The task scheduler is used to launch the implant.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The Python-based malware supports the ability to download additional payloads and execute commands issued from the C2 server. The instructions allow it to run shell scripts, list directories, upload/download/delete files, and run BAT, VBScript, and EXE files.

The findings also coincide with [ScarCruft](https://thehackernews.com/2026/02/scarcruft-uses-zoho-workdrive-and-usb.html)'s shift from traditional LNK-based attack chains to an HWP OLE-based dropper to deliver [RokRAT](https://thehackernews.com/2024/10/north-korean-scarcruft-exploits-windows.html), a remote access trojan exclusively used by the North Korean hacking group, per S2W. Specifically, the malware is embedded as an OLE object within an HWP document and executed via DLL side-loading.

"Unlike previous attack chains that progressed from LNK-dropped BAT scripts to shellcode, this case confirms the use of newly developed dropper and downloader malware to deliver shellcode and the ROKRAT payload," the South Korean security company [said](https://s2w.inc/en/resource/detail/1011).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/)...