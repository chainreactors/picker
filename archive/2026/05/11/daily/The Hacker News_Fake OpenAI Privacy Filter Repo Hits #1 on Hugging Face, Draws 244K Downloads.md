---
title: Fake OpenAI Privacy Filter Repo Hits #1 on Hugging Face, Draws 244K Downloads
url: https://thehackernews.com/2026/05/fake-openai-privacy-filter-repo-hits-1.html
source: The Hacker News
date: 2026-05-11
fetch_date: 2026-05-12T05:39:07.392117
---

# Fake OpenAI Privacy Filter Repo Hits #1 on Hugging Face, Draws 244K Downloads

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Fake OpenAI Privacy Filter Repo Hits #1 on Hugging Face, Draws 244K Downloads](https://thehackernews.com/2026/05/fake-openai-privacy-filter-repo-hits-1.html)

**Ravie Lakshmanan**May 11, 2026Supply Chain Attack / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPtLFShq_XoM9Nzsl5kmSsF2UGsm6VhRoLNodcqRCdq45zqy4ekFVtamokNzEFifQknD502Wc0uFTBUdvLsBsYn4QAeVHSWLmhF2ROBMXutev8T6JjCGrrarzLhkSTUHLBq-nEWrF0WTb2epkX_3Ba5a6Gv_21R7PPQ_zCjhk7OU702Y10tJkcJiYG52D4/s1700-e365/hugging-face-malware.jpg)

A malicious Hugging Face repository managed to take a spot in the platform's trending list by impersonating OpenAI's Privacy Filter open-weight model to deliver a Rust-based information stealer to Windows users.

The project, named [Open-OSS/privacy-filter](https://huggingface.co/Open-OSS/privacy-filter), masqueraded as its legitimate counterpart released by OpenAI late last month ([openai/privacy-filter](https://huggingface.co/openai/privacy-filter)), including copying the entire description verbatim to trick unsuspecting users into downloading it. Access to the malicious model has since been disabled by Hugging Face.

Privacy Filter was [unveiled](https://openai.com/index/introducing-openai-privacy-filter/) in April 2026 by the artificial intelligence (AI) company as a way to detect and redact personally identifiable information (PII) in unstructured text with an aim to incorporate strong privacy and security protections into applications.

"The repository had typosquatted OpenAI's legitimate Privacy Filter release, copied its model card nearly verbatim, and shipped a loader.py file that fetches and executes infostealer malware on Windows machines," the HiddenLayer Research Team [said](https://www.hiddenlayer.com/research/malware-found-in-trending-hugging-face-repository-open-oss-privacy-filter) in a report published last week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The malicious project instructs users to clone the repository and run a batch script ("start.bat") for Windows or a Python script ("loader.py") for Linux or macOS systems to configure all necessary dependencies and start the model.

Once launched, the Python script triggers malicious code responsible for disabling SSL verification, decoding a Base64-encoded URL hosted on JSON Keeper, and using it to extract a command that's passed to PowerShell for subsequent execution.The use of JSON Keeper, a public JSON paste service, as a dead drop resolver allows the attackers to switch payloads on the fly without the need for modifying the repository.

The PowerShell command is used to download a batch script from a remote server ("api.eth-fastscan[.]org") and launch it using "cmd.exe."The batch script functions as a second-stage downloader that prepares the environment by elevating its privileges by means of a User Account Control (UAC) prompt, configuring Microsoft Defender Antivirus exclusions, downloading the next-stage binary from the same domain, and setting up a scheduled task that launches a PowerShell script to run the executable.

Once the scheduled task is launched, the malware waits for two seconds before deleting itself. The final stage is an information stealer that's designed to take screenshots and harvest data from Discord, cryptocurrency wallets and extensions, system metadata, files such as FileZilla configurations and wallet seed phrases, and web browsers based on the Chromium and Gecko rendering engines.

"Despite using a scheduled task, this stage establishes no persistence: the task is destroyed before any reboot. It is being used as a one-shot SYSTEM-context launcher," HiddenLayer explained.

The stealer also runs checks to detect debuggers and sandboxes, ascertains it's not running in a virtual machine, and tries to disable Windows Antimalware Scan Interface (AMSI) and Event Tracing for Windows (ETW) to evade behavioural detection. The stolen data is exfiltrated in JSON format to the "recargapopular[.]com" domain.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgktNa8Ejw3vrSO1h0djyf_XA0lvv4E8h8nwiAHUInGfIzHh4kqc718j_KrIU4XCvIVeNiRFRSmRMfgli7R_Mz2CpXHXbNYA4NzVGLiHQiujW-jHF-Ww3eLK-KF9yvarLcXkMvxrwwHYP2DJHOveaDkCD0OQ6xsTcXWn8d1Z6i7GTN9gWpYD1o5_aZ0Luxg/s1700-e365/lure.png)

Prior to it being disabled, the model is said to have reached the #1 trending position on Hugging Face with approximately 244,000 downloads and 667 likes within 18 hours. It's suspected that these numbers were artificially inflated to give the repository an illusion of trust and get users to download it.

Further analysis of the activity has unearthed six more repositories that feature a similar Python loader to deploy the stealer -

* anthfu/Bonsai-8B-gguf
* anthfu/Qwen3.6-35B-A3B-APEX-GGUF
* anthfu/DeepSeek-V4-Pro
* anthfu/Qwopus-GLM-18B-Merged-GGUF
* anthfu/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF
* anthfu/supergemma4-26b-uncensored-gguf-v2

HiddenLayer said it also observed the "api[.]eth-fastscan[.]org" domain being used to serve a different Windows executable ("[o0q2l47f.exe](https://www.virustotal.com/gui/file/c1b59cc25bdc1fe3f3ce8eda06d002dda7cb02dea8c29877b68d04cd089363c7/detection)") that beacons out to "welovechinatown[.]info," a command-and-control (C2) server previously put to use in a campaign in which a malicious npm package named trevlo was leveraged to deliver ValleyRAT (aka Winos 4.0).

The Node.js library was downloaded more than 2,300 times after it was published by a user named "titaniumg" on April 4, 2026, although it's not clear if the download count was artificially boosted using automated processes. It's no longer available on npm.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"The package's postinstall hook silently executes an obfuscated JavaScript loader that spawns a base64-encoded PowerShell command, which in turn fetches and exe...