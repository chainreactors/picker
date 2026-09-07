---
title: Four REVSTEALER-Linked Modules Disable Windows Update and Defender to Run a Crypto Miner
url: https://thehackernews.com/2026/09/four-revstealer-linked-modules-disable.html
source: The Hacker News
date: 2026-09-06
fetch_date: 2026-09-07T06:49:32.832562
---

# Four REVSTEALER-Linked Modules Disable Windows Update and Defender to Run a Crypto Miner

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Four REVSTEALER-Linked Modules Disable Windows Update and Defender to Run a Crypto Miner](https://thehackernews.com/2026/09/four-revstealer-linked-modules-disable.html)

**Swati Khandelwal**Sep 06, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpRcdfXd6kYnqLLWSFdzGKICUzSr90MsV2f3PXtw8VDVcT-xOP2w4HwnVzrRI4bdJqhboQMFIm9BZ393b89IOqgYx-VVmb_B8-XJCsZ9SAIymdlBpEf5ARizHvn32t8Mr9stzV6nMVcn3utUYI1xSRxhaC29QZjS-C3haNSRPfQI_eBYzXCrwn5rl18Nw/s1700-nu-rw-lo-l85-e365/rev.jpg)

Elastic Security Labs has documented four previously unreported programs associated with REVSTEALER, an emerging Windows information stealer, that remain on an infected machine after the stealer deletes itself.

One of them switches off Windows Update and Microsoft Defender before running a cryptocurrency miner.

The company named the four programs **ProManager**, **WinUpdate**, **SoftManager**, and **LockAppHost** and [published the findings on September 2](https://www.elastic.co/security-labs/threat-command/revstealer-credential-harvesting-infostealer), along with a [technical white paper](https://assets.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt9cd59668ba5a104d/6a97978bd04dac6f166ca8ce/REVSTEALER_-_White_paper.pdf). REVSTEALER has been sold as a commercial infostealer since at least February 2026, when the earliest sample was first detected on VirusTotal.

The core stealer exfiltrates browser passwords and cookies, cryptocurrency wallets, gaming accounts, messaging data, and files, then reports "complete" to its server, deletes itself, and leaves no persistence. The four newly documented programs work differently. Each installs itself into the user's profile and stays there.

Elastic recovered the four programs from the same investigation as REVSTEALER and found that they share its build tradecraft, including the same packer, runtime function resolution, and the use of Polygon smart contracts for backup configuration.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The core stealer can also download and run additional executables at the command line. Elastic did not report seeing any of the four delivered onto a live REVSTEALER host, so the connection rests on shared code and investigative context rather than an observed hand-off.

The company describes the components as an "activity set" and notes they are separate executables, not plug-ins loaded into the stealer itself.

What each program does, in Elastic's account:

|  |  |  |
| --- | --- | --- |
| **ProManager** | Steals wallet files and browser wallet extensions, displays attacker-controlled content over a wallet application's window, and logs passwords typed or pasted into fields it identifies as password or passphrase inputs | Registry Run key |
| **WinUpdate** | Watches the clipboard, replaces copied cryptocurrency addresses with the attacker's, and collects text that looks like a wallet recovery phrase | Scheduled task, with a Registry Run key as fallback |
| **SoftManager** | Turns the machine into a reverse proxy that routes the attacker's network traffic through the victim's connection | Logon script, scheduled task, or Registry Run key |
| **LockAppHost** | Runs a cryptocurrency miner with administrator rights after disabling Windows Update and excluding folders from Microsoft Defender | Registry Run key or a service |

LockAppHost is the most disruptive of the four. To gain administrator rights, it abuses the Windows CMSTP tool, falling back to a standard elevation prompt if that fails.

Once elevated, it adds Microsoft Defender exclusions for common folders and file types, disables 5 Windows Update services, disables 11 scheduled update tasks and 2 malware removal tasks, and then hides a miner within legitimate Windows processes. The changes it makes to weaken the machine's defenses remain after the miner is found.

ProManager targets users of desktop cryptocurrency wallets. Because most of those wallets are built with the Electron framework, ProManager reads the wallet window's saved position and opens attacker-supplied content sized and positioned to overlay the real wallet, without touching the wallet program itself.

A separate part of the module records what the user types into password and passphrase fields, including values pasted from the clipboard.

Before the modules ever arrive, REVSTEALER casts a wide net. It collects browser passwords and cookies; files from more than 50 cryptocurrency wallets and a large set of wallet browser extensions; session data from Telegram and other messaging clients; VPN and FTP configuration; the Windows Credential Manager; password managers; and selected documents.

For some gaming platforms, it goes further. It decrypts the stored Roblox session cookie, allowing an attacker to take over the account without the password.

To obtain credentials that Chrome protects with App-Bound Encryption, REVSTEALER launches the browser in a debugger and reads the decryption key from memory. This is not a new technique, nor is it unique to REVSTEALER.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuepMJ7PSLJNd3b-kqeQZd7rhzg3e-LZjI25YJu5fHlPhN_B85kvQyRPfdEZT0Y35cTiag1WXavTzpoMMR_UQGg-h6bLtcpl0SeNOm_xpG0F5W149hCGQcNDJqt-fBM7gV20JYJkA57Y3C6m3tnjEHr0fj4mt6ffj2bkZxbN9l6QRafF0ytvettXUsrwI/s1700-nu-rw-lo-l85-e365/chrome-app.jpg)

Elastic said it was likely adapted from the public ElevationKatz project and was also used by another stealer, [VoidStealer, in March 2026](https://thehackernews.com/2026/03/weekly-recap-cicd-backdoor-fbi-buys.html). Gen Digital, which analyzed VoidStealer, described it as the first infostealer seen using the technique in the wild.

REVSTEALER reaches victims mainly through game-cheat lures. Elastic identified at least 17 YouTube channels, many [of which were hijacked from their original owners](https://thehackernews.com/2025/10/3000...