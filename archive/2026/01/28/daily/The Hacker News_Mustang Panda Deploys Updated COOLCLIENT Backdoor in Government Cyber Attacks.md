---
title: Mustang Panda Deploys Updated COOLCLIENT Backdoor in Government Cyber Attacks
url: https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html
source: The Hacker News
date: 2026-01-28
fetch_date: 2026-01-29T04:06:00.049306
---

# Mustang Panda Deploys Updated COOLCLIENT Backdoor in Government Cyber Attacks

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

# [Mustang Panda Deploys Updated COOLCLIENT Backdoor in Government Cyber Attacks](https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html)

**Ravie Lakshmanan**Jan 28, 2026Cyber Espionage / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbfyqOKlboKyz0aepCrCjmgfx7hVJKbZ5zcv_iQC6sUvz4vyarawc69b_BxxUdQYhl62-gOoWmlEDQywKqX4zRtKo7X_G_eZTCignSldlMeGxb6ZxhYRJTFn2L0f_FcdJS2FrlLq32HpdE1N_XqD639QIYNC9xGZymr8PNBLW_mU7uB6Oa4f759T_4t-0E/s1700-e365/cyber.jpg)

Threat actors with ties to China have been observed using an updated version of a backdoor called COOLCLIENT in cyber espionage attacks in 2025 to facilitate comprehensive data theft from infected endpoints.

The activity has been attributed to **[Mustang Panda](https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html)** (aka Earth Preta, Fireant, HoneyMyte, Polaris, and Twill Typhoon) with the intrusions primarily directed against government entities located across campaigns across Myanmar, Mongolia, Malaysia, and Russia.

Kaspersky, which disclosed details of the updated malware, said it's deployed as a secondary backdoor along with [PlugX](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html) and [LuminousMoth](https://thehackernews.com/2021/07/chinas-cyberspies-targeting-southeast.html) infections.

"COOLCLIENT was typically delivered alongside encrypted loader files containing encrypted configuration data, shellcode, and in-memory next-stage DLL modules," the Russian cybersecurity company [said](https://securelist.com/honeymyte-updates-coolclient-uses-browser-stealers-and-scripts/118664/). "These modules relied on DLL side-loading as their primary execution method, which required a legitimate signed executable to load a malicious DLL."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Between 2021 and 2025, Mustang Panda is said to have leveraged signed binaries from various software products, including Bitdefender ("qutppy.exe"), VLC Media Player ("vlc.exe" renamed as "googleupdate.exe"), Ulead PhotoImpact ("olreg.exe"), and Sangfor ("sang.exe") for this purpose.

Campaigns observed in 2024 and 2025 have been found to abuse legitimate software developed by Sangfor, with one such wave targeting Pakistan and Myanmar using it to deliver a COOLCLIENT variant that drops and executes a previously unseen rootkit.

COOLCLIENT was [first documented](https://www.sophos.com/en-us/blog/family-tree-dll-sideloading-cases-may-be-related) by Sophos in November 2022 in a report detailing the widespread use of DLL side-loading by China-based APT groups. A subsequent analysis from Trend Micro officially [attributed](https://thehackernews.com/2023/03/researchers-uncover-chinese-nation.html) the backdoor to Mustang Panda and highlighted its ability to read/delete files, as well as monitor the clipboard and active windows.

The malware has also been put to use in attacks targeting multiple telecom operators in a single Asian country in a long-running espionage campaign that may have commenced in 2021, Broadcom's Symantec and Carbon Black Threat Hunter Team [revealed](https://thehackernews.com/2024/06/chinese-cyber-espionage-targets-telecom.html) in June 2024.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidMAFT6elOg9LlbeJwwZZMAk-XEZVVtJr5EfkRtAvkBxhDHFmv0em0-yGdA_3amiXSF28HXJH5zYmlZlcsNCmBJKTg0ztlD-kxPFyww-w3xPdhXxJNx_qhmvZqCWlEB4LuDs1OAAdrKFeNMifeHv2XRhb_Mp26YW7eqLMvoxWWmCClaS-zoZy1Tj23gRjk/s1700-e365/vlc.png)

COOLCLIENT is designed for collecting system and user information, such as keystrokes, clipboard contents, files, and HTTP proxy credentials from the host's HTTP traffic packets based on instructions sent from a command-and-control (C2) server over TCP. It can also set up a reverse tunnel or proxy, and receive and execute additional plugins in memory.

Some of the supported plugins are listed below -

* ServiceMgrS.dll, a service management plugin to oversee all services on the victim host
* FileMgrS.dll, a file management plugin to enumerate, create, move, read, compress, search, or delete files and folders
* RemoteShellS.dll, a remote shell plugin that spawns a "cmd.exe" process to allow the operator to issue commands and capture the resulting output

Mustang Panda has also been observed deploying three different stealer programs in order to extract saved login credentials from Google Chrome, Microsoft Edge, and other Chromium-based browsers. In at least one case, the adversary ran a cURL command to exfiltrate the Mozilla Firefox browser cookie file ("cookies.sqlite") to Google Drive.

These stealers, detected in attacks against the government sector in Myanmar, Malaysia, and Thailand, are suspected to be used as part of broader post-exploitation efforts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

Furthermore, the attacks are characterized by the use of a known malware called [TONESHELL](https://thehackernews.com/2022/11/chinese-mustang-panda-hackers-actively.html) (aka TOnePipeShell), which has been employed with varying levels of capabilities to establish persistence and drop additional payloads like [QReverse](https://hitcon.org/2024/CMT/agenda/5e788b7a-f9e1-4f0c-b772-f7fe9b0140ec/), a remote access trojan with remote shell, file management, screenshot capture, and information gathering features, and a USB worm codenamed [TONEDISK](https://thehackernews.com/2025/09/mustang-panda-deploys-snakedisk-usb.html).

Kaspersky's analysis of the browser credential stealer has also uncovered code-level similarities with a cookie stealer used by LuminousMoth, suggesting some level of tool sharing between the two clusters. On top of that, Mustang Panda has been identified as using batch and PowerShell scripts to gather system information, conduct document theft activities, and steal browser login data.

"With capabilities such as keylogging, clipboard monitoring, proxy credential theft, document exfiltration, browser credential harvesting, and large-scale file theft, HoneyMyte's campaigns appear to go far beyond traditional espionage goals like document theft and persistence," the company said.

"These tools indicate a shift toward the active surveillance of user activity that includes capturing ...