---
title: Russian CTRL Toolkit Delivered via Malicious LNK Files Hijacks RDP via FRP Tunnels
url: https://thehackernews.com/2026/03/russian-ctrl-toolkit-delivered-via.html
source: The Hacker News
date: 2026-03-30
fetch_date: 2026-03-31T04:37:37.253665
---

# Russian CTRL Toolkit Delivered via Malicious LNK Files Hijacks RDP via FRP Tunnels

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Russian CTRL Toolkit Delivered via Malicious LNK Files Hijacks RDP via FRP Tunnels](https://thehackernews.com/2026/03/russian-ctrl-toolkit-delivered-via.html)

**Ravie Lakshmanan**Mar 30, 2026Malware / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh05CEOtp0cIlsi1qDK4HRH2PPOFyvB5jca65pAQVsnCfBHZ-wRGt0s8VhvzO_l-4Q9H_xGKQsO_efVGzJ46ElLQNaq_FEp6wPUou4aqTvEKMPlEEGOTyEtISTj0VkC5QmO38HuxWehNDTUkdvCVCCp-GrIPWJyFt4dTLp1TIbqW8hAiVEJ-vxnoKUexR6-/s1700-e365/ctrl-ctrl.jpg)

Cybersecurity researchers have discovered a remote access toolkit of Russian-origin that's distributed via malicious Windows shortcut (LNK) files that are disguised as private key folders.

The **CTRL** toolkit, according to Censys, is custom-built using .NET and includes various executables" to facilitate credential phishing, keylogging, Remote Desktop Protocol (RDP) hijacking, and reverse tunneling via Fast Reverse Proxy (FRP).

"The executables provide encrypted payload loading, credential harvesting via a polished Windows Hello phishing UI, keylogging, RDP session hijacking, and reverse proxy tunneling through FRP," Censys security researcher Andrew Northern [said](https://censys.com/blog/under-ctrl-dissecting-a-previously-undocumented-russian-net-access-framework/).

The attack surface management platform said it recovered CTRL from an open directory at 146.19.213[.]155 in February 2026. Attack chains distributing the toolkit rely on a weaponized LNK file ("Private Key #kfxm7p9q\_yek.lnk") with a folder icon to trick users into double-clicking it.

This triggers a multi-stage process, with each stage decrypting or decompressing the next, until it leads to the deployment of the toolkit. The LNK file dropper is designed to launch a hidden PowerShell command, which then wipes existing persistence mechanisms from the victim's Windows Startup folder.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

It also decodes a Base64-encoded blob and runs it in memory. The stager, for its part, tests TCP connectivity to hui228[.]ru:7000 and downloads next-stage payloads from the server. Furthermore, it modifies firewall rules, sets up persistence using scheduled tasks, creates backdoor local users, and spawns a cmd.exe shell server on port 5267 that's accessible through the FRP tunnel.

One of the downloaded payloads, "ctrl.exe," functions as a .NET loader for launching an embedded payload, the CTRL Management Platform, which can serve either as a server or a client depending on the command-line arguments. Communication occurs over a Windows named pipe.

"The dual-mode design means the operator deploys ctrl.exe once on the victim (via the stager), then interacts with it by running ctrl.exe client through the FRP-tunneled RDP session," Censys said. "The named pipe architecture keeps all C2 command traffic local to the victim machine — nothing traverses the network except the RDP session itself."

The supported commands allow the malware to gather system information, launch a module designed for credential harvesting, and start a keylogger as a background service (if configured as a server) to capture all keystrokes to a file named "C:\Temp\keylog.txt" by installing a keyboard hook, and exfiltrate the results.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYj6OjS1oR64ByDgk4vLMP8990lF5dvAb0ZvA_oU33CsC_i_fqE95S2fyYpqrAUfzvHG67-1P8mc_fA-5DnSgCVLvwzFu5df_qvttbj7m2CbgaGR6lNW5DUxWRilmUxn5XY_nzsjh5lbM3W4Alzga-6H3gYlZyIKeIiQMh1C0EHCBwkmEGPcVoNU1vi7TN/s1700-e365/ctrl.jpg)

The credential harvesting component is launched as a Windows Presentation Foundation (WPF) application that mimics a real Windows PIN verification prompt to capture the system PIN. The module, besides blocking attempts to escape the phishing window via keyboard shortcuts like Alt+Tab, Alt+F4, or F4, validates the entered PIN against the real Windows credential prompt via UI automation by using the [SendKeys()](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.sendkeys) method.

"If the PIN is rejected, the victim is looped back with an error message," Northern explained. "The window remains open even if the PIN successfully validates against the actual Windows authentication system. The captured PIN is logged with the prefix [STEALUSER PIN CAPTURED] to the same keylog file used by the background keylogger."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-stories-xmcyber-d)

One of the commands built into the toolkit allows it to send toast notifications impersonating web browsers like Google Chrome, Microsoft Edge, Brave, Opera, Opera GX, Vivaldi, Yandex, and Iron to conduct additional credential theft or deliver other payloads. The two other payloads dropped as part of the attack are listed below -

* FRPWrapper.exe, which is a Go DLL that's [loaded in memory](https://github.com/schellingb/DLLFromMemory-net) to establish reverse tunnels for RDP and a raw TCP shell through the operator's FRP server.
* RDPWrapper.exe, which enables unlimited concurrent RDP sessions.

"The toolkit demonstrates deliberate operational security. None of the three hosted binaries contain hard-coded C2 addresses," Censys said. "All data exfiltration occurs through the FRP tunnel via RDP — the operator connects to the victim’s desktop and reads keylog data through the ctrl named pipe. This architecture leaves minimal network forensic artifacts compared to traditional C2 beacon patterns."

"The CTRL toolkit demonstrates a trend toward purpose-built, single-operator toolkits that prioritize operational security over feature breadth. By routing all interaction through FRP reverse tunnels to RDP sessions, the operator avoids the network-detectable beacon patterns that characterize commodity RATs."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQ...