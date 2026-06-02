---
title: China-Aligned Groups Ramp Up Attacks: Dragon Weave Hits Czech Republic & Taiwan
url: https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html
source: The Hacker News
date: 2026-06-01
fetch_date: 2026-06-02T06:33:16.262178
---

# China-Aligned Groups Ramp Up Attacks: Dragon Weave Hits Czech Republic & Taiwan

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [China-Aligned Groups Ramp Up Attacks: Dragon Weave Hits Czech Republic & Taiwan](https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html)

**Ravie Lakshmanan**Jun 01, 2026Endpoint Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUhiw46hdnhoY05E-0EyhOX5AxQrqJeNM0WDEWiYHAi5pPt4kIFPbvqGZhyAK4NxlAF7KJKxPfWlbGLbZUJJD9PgGmazvyhzaSgBXokM_6eYQfWXQ1HDv2heSDTnps4EGhjKqwCbuQOl0d9QN25tmn85xLujp-htCwLhhywI4A6BKJxkOOKb9FSu02AMjX/s1700-e365/china.jpg)

A new cyber espionage campaign codenamed **Operation Dragon Weave** has been observed targeting officials and citizens in the Czech Republic and Taiwan to deliver an [AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html) agent.

According to Seqrite Labs, targets of the campaign include government, research, academic, technology, and financial services sectors. The activity entails distributing spear-phishing emails containing ZIP attachments to trigger an infection chain that uses a Rust loader to drop the final payload for data exfiltration and remote control.

"When extracted, the archive contains multiple files that appear legitimate but are actually part of a structured infection chain designed to execute malicious payloads in the background," security researcher Priya Patel [said](https://www.seqrite.com/blog/operation-dragon-weave-uncovering-a-china-linked-campaign-targeting-czech-republic-and-taiwan-using-azure-cloud-c2/).

The attack chain uses two different pathways to launch the final-stage malware. One infection sequence begins when the recipient of the ZIP archive opens a malicious Windows Shortcut (LNK) file that masquerades as a PDF document. This leads to the execution of a PowerShell script that's responsible for extracting an executable ("RuntimeBroker\_update.exe") from an intermediate DAT file and running it.

In the second attack chain, the victim directly launches a binary from the same archive. The binary functions as a self-contained Rust-based dropper to launch "RuntimeBroker\_update.exe." Regardless of the path chosen, the executable loads a malicious DLL ("UnityPlayer.dll") via [DLL side-loading](https://attack.mitre.org/techniques/T1102/001/), resulting in the deployment of a Rust-based loader called RUSTCLOAK.

The loader then decrypts and runs the main payload, an AdaptixC2 agent codenamed AZUREVEIL owing to the use of Microsoft Azure Blob Storage for command-and-control (C2). The loader is designed to perform anti-analysis checks to proceed only if the malware determines that it's being run within a sandboxed environment.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"The malware just talks to Azure Blob Storage, the same service used by thousands of legitimate enterprises worldwide," Seqrite Labs said. "Instead of using a traditional pull-based C2 model, AZUREVEIL follows a dead drop approach. The attacker and the infected system never communicate directly. Instead, both sides use the same Azure storage container to exchange data."

AZUREVEIL supports 36 commands that allow it to perform a wide range of post-compromise actions on the host, including file operations, file uploads and downloads, shell command execution, process enumeration and termination, port forwarding, SOCKS proxy control, C2 server management, and in-memory execution of Beacon Object Files (BOFs).

These capabilities grant the attacker complete control over the compromised endpoint. Although the activity has been attributed to a known threat actor or group, it's assessed to be China-aligned.

The disclosure comes as Cato Networks [said](https://www.catonetworks.com/blog/cato-ctrl-suspected-china-linked-threat-actor-targets-global-manufacturer/) it detected and blocked an attempted intrusion against the Indian branch of an unnamed global manufacturing customer to deliver TencShell, a previously undocumented Go-based implant derived from the open-source [rshell](https://thehackernews.com/2022/08/chinese-hackers-backdoored-mimi-chat.html) C2 framework.

The attack is believed to be the work of China-nexus threat actors based on the historical use of rshell, Tencent-themed API impersonation, and infrastructure patterns. The initial access vector used in the intrusion is currently unknown.

"If successful, TencShell could have given the attacker remote command execution, in-memory payload execution, proxying, pivoting, system profiling, and a path to deploy additional tooling," researchers Idan Tarab, Dr. Guy Waizel, Zohar Buber, and Shani Kurtzberg said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXrHx_UGV-y1UISYxIwz9vFhggR56dzfc6jM7Q5pfSgnb7K025yIXL0EHIU8x77rEP9SM7qmQsBD-VBseLjdhZEaKySlge4wM6Q6J9kwahFOm3jYU2Wwcijbvj9MkEpDLORnaSOSy7NAasqd3YqTA4WdTbB2I9C8OloviE1FWt19CT9QoOvAkSbAWqIeYz/s1700-e365/TencShell.png)

In a report published last week, ESET [said](https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q4-2025-q1-2026/) China-aligned threat actors have remained "highly active" globally from October 2025 through March 2026. This includes an unreported cluster dubbed SteppeDriver that was first discovered in 2024 and has since targeted entities in France, Mongolia, and South America using tools like [ShadowPad](https://thehackernews.com/2025/02/chinese-linked-attackers-exploit-check.html), [COOLCLIENT](https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html), CurlyDoor, RudeGull, and MKTDownloader.

Also identified by the Slovakian cybersecurity vendor is a new toolkit linked to [UNC5221](https://thehackernews.com/2025/09/unc5221-uses-brickstorm-backdoor-to.html) dubbed PhiliKit that acts as a passive backdoor for executing shell commands, Python scripts, and Perl scripts. It's suspected that PhiliKit is deployed as part of the [SPAWN](https://thehackernews.com/2025/04/critical-ivanti-flaw-actively-exploited.html) ma...