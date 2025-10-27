---
title: OpenAI Bans ChatGPT Accounts Used by Russian, Iranian, and Chinese Hacker Groups
url: https://thehackernews.com/2025/06/openai-bans-chatgpt-accounts-used-by.html
source: The Hacker News
date: 2025-06-10
fetch_date: 2025-10-06T22:57:40.871813
---

# OpenAI Bans ChatGPT Accounts Used by Russian, Iranian, and Chinese Hacker Groups

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [OpenAI Bans ChatGPT Accounts Used by Russian, Iranian, and Chinese Hacker Groups](https://thehackernews.com/2025/06/openai-bans-chatgpt-accounts-used-by.html)

**Jun 09, 2025**Ravie LakshmananArtificial Intelligence / Social Media

[![OpenAI Bans ChatGPT Accounts](data:image/png;base64... "OpenAI Bans ChatGPT Accounts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-dkxPd5jkfcoCpl2fFVt-MNLzbvxjx554pgkuHA89FexnGWeSUy3CfM7fdp9d2GanqhAkdp9s9FWVzGtNs4nk0xk5LaOwRFG1CbbHmfUAAp3trGdPXEgoUkENIfJE1yPIpLAOpqlFLqYKLP0f_g46PNKJa7VnXHauvfeo_yI_d333yqCk0f31DI0w1if7/s790-rw-e365/hacker-ai-coding.gif)

OpenAI has [revealed](https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-june-2025/) that it banned a set of ChatGPT accounts that were likely operated by Russian-speaking threat actors and two Chinese nation-state hacking groups to assist with malware development, social media automation, and research about U.S. satellite communications technologies, among other things.

"The [Russian-speaking] actor used our models to assist with developing and refining Windows malware, debugging code across multiple languages, and setting up their command-and-control infrastructure," OpenAI said in its threat intelligence report. "The actor demonstrated knowledge of Windows internals and exhibited some operational security behaviors."

The Go-based malware campaign has been codenamed ScopeCreep by the artificial intelligence (AI) company. There is no evidence that the activity was widespread in nature.

The threat actor, per OpenAI, used temporary email accounts to sign up for ChatGPT, using each of the created accounts to have one conversation to make a single incremental improvement to their malicious software. They subsequently abandoned the account and moved on to the next.

This practice of using a network of accounts to fine-tune their code highlights the adversary's focus on operational security (OPSEC), OpenAI added.

The attackers then distributed the AI-assisted malware through a publicly available code repository that impersonated a legitimate video game crosshair overlay tool called [Crosshair X](https://centerpointgaming.com). Users who ended up downloading the trojanized version of the software had their systems infected by a malware loader that would then proceed to retrieve additional payloads from an external server and execute them.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"From there, the malware was designed to initiate a multi-stage process to escalate privileges, establish stealthy persistence, notify the threat actor, and exfiltrate sensitive data while evading detection," OpenAI said.

"The malware is designed to escalate privileges by relaunching with ShellExecuteW and attempts to evade detection by using PowerShell to programmatically exclude itself from Windows Defender, suppressing console windows, and inserting timing delays."

Among other tactics incorporated by ScopeCreep include the use of Base64-encoding to obfuscate payloads, DLL side-loading techniques, and SOCKS5 proxies to conceal their source IP addresses.

The end goal of the malware is to harvest credentials, tokens, and cookies stored in web browsers, and exfiltrate them to the attacker. It's also capable of sending alerts to a Telegram channel operated by the threat actors when new victims are compromised.

OpenAI noted that the threat actor asked its models to debug a Go code snippet related to an HTTPS request, as well as sought help with integrating Telegram API and using PowerShell commands via Go to modify Windows Defender settings, specifically when it comes to adding antivirus exclusions.

The second group of ChatGPT accounts disabled by OpenAI are said to be associated with two hacking groups attributed to China: [APT5](https://thehackernews.com/2022/12/hackers-actively-exploiting-citrix-adc.html) (aka Bronze Fleetwood, Keyhole Panda, Manganese, and UNC2630) and [APT15](https://thehackernews.com/2025/04/spynote-badbazaar-moonshine-malware.html) (aka Flea, Nylon Typhoon, Playful Taurus, Royal APT, and Vixen Panda)

While one subset engaged with the AI chatbot on matters related to open-source research into various entities of interest and technical topics, as well as to modify scripts or troubleshooting system configurations.

"Another subset of the threat actors appeared to be attempting to engage in development of support activities including Linux system administration, software development, and infrastructure setup," OpenAI said. "For these activities, the threat actors used our models to troubleshoot configurations, modify software, and perform research on implementation details."

This consisted of asking for assistance building software packages for offline deployment and advice pertaining to configured firewalls and name servers. The threat actors engaged in both web and Android app development activities.

In addition, the China-linked clusters weaponized ChatGPT to work on a brute-force script that can break into FTP servers, research about using large-language models (LLMs) to automate penetration testing, and develop code to manage a fleet of Android devices to programmatically post or like content on social media platforms like Facebook, Instagram, TikTok, and X.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Some of the other observed malicious activity clusters that harnessed ChatGPT in nefarious ways are listed below -

* A network, consistent with the [North Korea IT worker scheme](https://thehackernews.com/2025/02/openai-bans-accounts-misusing-chatgpt.html), that used OpenAI's models to drive deceptive employment campaigns by developing materials that could likely advance their fraudulent attempts to apply for IT, software engineering, and other remote jobs around the world
* **Sneer Review**, a likely China-origin activity that used OpenAI's models to bulk generate social media posts in English, Chinese, and ...