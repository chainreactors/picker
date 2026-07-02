---
title: AI-Generated Browser Ransomware Abuses Chromium API on Windows and Android
url: https://thehackernews.com/2026/07/ai-generated-browser-ransomware-abuses.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:22.376734
---

# AI-Generated Browser Ransomware Abuses Chromium API on Windows and Android

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

# [AI-Generated Browser Ransomware Abuses Chromium API on Windows, Linux, macOS, Android](https://thehackernews.com/2026/07/ai-generated-browser-ransomware-abuses.html)

**Ravie Lakshmanan**Jul 01, 2026Browser Security / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4BJdHYquuxXoz8n0LhMEmm9KPcWcMC57w4LnqbMNCPXMAFdS95ys3zE6F5jZOvSKwsVWp6t3z8pVImRJ3Nvxgkr4QiPI5O06zJywlL5uuBIU2G0ZtPucYq80Z_G-PnVzjYfChzbnpLxGyD2PpbH8VdLWjIuNLt0RoAe5Q8mVulX2s_4Ueg7XR0pxZVwKn/s1700-e365/chrome-ransomware.jpg)

Cybersecurity researchers have [flagged](https://research.checkpoint.com/2026/browser-only-ransomware-from-llm-hallucinations-to-a-practical-attack-technique/) a new malware artifact generated using DeepSeek that constructed a novel attack path combining "unrealistic browser-malware concepts with a real browser capability" to turn it into a working ransomware technique that runs entirely inside the browser on both Windows and Android devices.

"This is the first documented case where a frontier AI model independently bridged the gap between a theoretical browser-only ransomware risk and a practical, working attack chain – surfacing a novel attack path that defenders had previously dismissed as unfeasible due to browser sandboxing limits," Check Point said in a statement shared with The Hacker News.

"The expertise needed to discover a new attack path is no longer the bottleneck, and defenders need to account for that shift now — before threat actors operationalize it at scale."

The identified sample is a Python Flask application named "[deepseek\_python\_20260125\_da0631.py](https://www.virustotal.com/gui/file/07c39f79ab92fb21557b82283472dce1c112f577d796111fb752c3c6d84c86b5)" that was uploaded to VirusTotal on January 25, 2026, with the Google-owned malware scanning service describing it as a "fully functional information stealer and ransomware toolkit." It has been named **InfernoGrabber** v9.0 by the malware author.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The application is designed to operate as a malicious web server that lures victims with a fake Discord avatar AI upscaler, while stealthily running a wide array of harmful actions, including stealing Discord tokens, harvesting credit card numbers and cryptocurrency seed phrases, logging keystrokes, and capturing unauthorized webcam and microphone feeds.

"The code includes specific routines for browser exploitation (targeting CVEs like CVE-2023-4863), data exfiltration via a hard-coded Discord webhook, a ransomware 'WinLocker' screen demanding Bitcoin, and an administrative dashboard for the attacker to manage stolen data," according to VirusTotal.

The findings come as artificial intelligence and large language models (LLMs) are redefining the cyber threat landscape, enabling threat actors to abuse the technology to develop malware and exploits. The use of DeepSeek is noteworthy as it signals that the Chinese company's models have lower refusal rates for malicious cyber requests when compared to its Western counterparts from Anthropic, Google, or OpenAI.

Other factors that may have facilitated the use of DeepSeek is its free access via the web interface, availability in regions where other frontier models do not operate, and its ability to generate a working malicious application from a "single broad prompt" as opposed to models from Anthropic or OpenAI.

"DeepSeek models can turn high‑level malicious ideas into concrete, complete attacks with less expertise than competing platforms," Check Point Research said.

The Israeli cybersecurity company said it unearthed the Python artifact as part of its analysis of about 3,000 files attributed to DeepSeek over the past year. Of these, 1,383 samples have been classified as malicious or dangerous. The Python malware is an instance of what's called In-Browser Ransomware that implements a browser-native technique not encountered in real-world campaigns in the past. The exact prompt that was used to produce the sample is unknown.

The attack technique entails using a phishing decoy to trick a user into granting file system access to a web page, which then enumerates local files in the selected folder, reads and exfiltrates their contents, encrypts and overwrites them, and finally displays an extortion note to the victim. What makes this more unusual is that all of this can be accomplished without installing a native payload, exploiting a browser vulnerability, or requiring root access.

It's worth mentioning here that the approach is limited to web browsers that expose the picker-based [File System Access API](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access). This includes Google Chrome and other Chromium-based browsers across Windows, macOS, ChromeOS, Linux, and Android. There is no evidence that the browser-native ransomware pattern has been abused in the wild.

"Our testing confirmed the attack works across Windows, macOS, Linux, Android, and Microsoft Edge on Windows," Pedro Drimel Neto, malware analysis team leader at Check Point Research, told The Hacker News. "The only significant exception is that on iOS, we could not reproduce the attack there. Since the File System Access API is implemented in Chromium-based browsers across these platforms, the attack surface is wider than initially thought, affecting the vast majority of desktop and Android users."

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

Another troubling aspect of AI-assisted development is that it not only lowers the barrier for bad actors to generate offensive code, but also the fact that they do not even need to k...