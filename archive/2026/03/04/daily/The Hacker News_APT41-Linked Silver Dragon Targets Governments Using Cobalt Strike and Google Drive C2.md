---
title: APT41-Linked Silver Dragon Targets Governments Using Cobalt Strike and Google Drive C2
url: https://thehackernews.com/2026/03/apt41-linked-silver-dragon-targets.html
source: The Hacker News
date: 2026-03-04
fetch_date: 2026-03-05T04:07:47.832863
---

# APT41-Linked Silver Dragon Targets Governments Using Cobalt Strike and Google Drive C2

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

# [APT41-Linked Silver Dragon Targets Governments Using Cobalt Strike and Google Drive C2](https://thehackernews.com/2026/03/apt41-linked-silver-dragon-targets.html)

**Ravie Lakshmanan**Mar 04, 2026Malware / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGPaqQJe-7ak-qgx29_h6G7zUiJhGiBSHZEiydrRzZzuKVlVMBzrJNLFndAvmu15EzX2SXQ8NUHKyH9ZJDQRQMnXukmrUfdPor35gswSxUuTNGGXo7h8eOhDNBVAaCGEo_ohNYv2-8W-zpOuSSHYqCB5iURwesotjNTK9a3926UdkuqI2uz-zUBMzNP5cU/s1700-e365/dragon.jpg)

Cybersecurity researchers have disclosed details of an advanced persistent threat (APT) group dubbed **Silver Dragon** that has been linked to cyber attacks targeting entities in Europe and Southeast Asia since at least mid-2024.

"Silver Dragon gains its initial access by exploiting public-facing internet servers and by delivering phishing emails that contain malicious attachments," Check Point [said](https://research.checkpoint.com/2026/silver-dragon-targets-organizations-in-southeast-asia-and-europe/) in a technical report. "To maintain persistence, the group hijacks legitimate Windows services, which allows the malware processes to blend into normal system activity."

Silver Dragon is assessed to be operating within the [APT41 umbrella](https://thehackernews.com/2025/09/china-linked-apt41-hackers-target-us.html). APT41 is the cryptonym assigned to a prolific Chinese hacking group known for its targeting of healthcare, telecoms, high-tech, education, travel services, and media sectors for cyber espionage as early as 2012. It's also believed to engage in financially motivated activity potentially outside of state control.

Attacks mounted by Silver Dragon have been found to primarily single out government entities, with the adversary using Cobalt Strike beacons for persistence on compromised hosts. It's also known to employ techniques like DNS tunneling for command-and-control (C2) communication to bypass detection.

Check Point said it identified three different infection chains to deliver Cobalt Strike: [AppDomain hijacking](https://attack.mitre.org/techniques/T1574/014/), service DLL, and email-based phishing.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"The first two infection chains, AppDomain hijacking and Service DLL, show clear operational overlap," the cybersecurity company said. "They are both delivered via compressed archives, suggesting their use in post‑exploitation scenarios. In several cases, these chains were deployed following the compromise of publicly exposed vulnerable servers."

The two chains make use of a RAR archive containing a batch script, with the first chain using it to drop MonikerLoader, a .NET-based loader responsible for decrypting and executing a second-stage directly in memory. The second stage, for its part, mimics MonikerLoader's behavior, acting as a conduit for loading the final Cobalt Strike beacon payload.

On the other hand, the service DLL chain uses a batch script to deliver a shellcode DLL loader dubbed BamboLoader, which is registered as a Windows service. A heavily obfuscated C++ malware, it's used to decrypt and decompress shellcode staged on disk, and inject it into a legitimate Windows process, such as "taskhost.exe." The binary targeted for injection is configurable within BamboLoader.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPleTdpYzAN-hRx0ZQDAutOQ8NHCiTk-IGca5jGqaztyxqrArnvgmOhypgWJpvWbPPAbTOGyLe5yWXHEJXhKnCz83KXuRXrd_3yWt70Q-ZUemrenbKs42eM4n5OMsDEevSVM9LV3sfgrR9MIaHCq-u7UFwYWTcemgGEZUyuQfeDE15dcuLYqh41nXDfFWp/s1700-e365/cp.png)

The third infection chain involves a phishing campaign that has primarily targeted Uzbekistan with malicious Windows shortcuts (LNK) as attachments. The weaponized LNK file is designed to launch PowerShell code by means of "cmd.exe," leading to the extraction and execution of next-stage payloads. This includes four different files -

* Decoy document
* Legitimate executable vulnerable to DLL side-loading ("GameHook.exe")
* Malicious DLL aka BamboLoader ("graphics-hook-filter64.dll")
* Encrypted Cobalt Strike payload ("simhei.dat")

As part of this campaign, the decoy document is displayed to the victim, while, in the background, the rogue DLL is sideloaded via "GameHook.exe" to ultimately launch Cobalt Strike. The attacks are also characterized by the deployment of various post-exploitation tools -

* **SilverScreen**, a .NET screen-monitoring tool used to capture periodic screenshots of user activity, including precise cursor positioning.
* **SSHcmd**, a .NET command-line SSH utility that provides remote command execution and file transfer capabilities over SSH.
* **GearDoor**, a .NET backdoor that shares similarities with MonikerLoader and communicates with its C2 infrastructure via Google Drive.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

Once executed, the backdoor authenticates to the attacker-controlled Google Drive account and uploads a heartbeat file containing basic system information. Interestingly, the backdoor utilizes different file extensions to indicate the nature of the task to be performed on the infected host. The results of the task execution are captured and uploaded to Drive.

* **\*.png**, to send heartbeat files.
* **\*.pdf**, to receive and execute commands, list the contents of a directory, make a new directory, and remove all files within a specified directory. The results of the operation are sent to the server in the form of a \*.db file.
* **\*.cab**, to receive and execute commands to gather host information and a list of running processes, enumerate files and directories, run commands via "cmd.exe" or scheduled tasks, upload files to Google Drive, and terminate the implant. The execution status is uploaded as a .bak file.
* **\*.rar**, to receive and execute payloads. If the RAR file is named "wiatrace.b...