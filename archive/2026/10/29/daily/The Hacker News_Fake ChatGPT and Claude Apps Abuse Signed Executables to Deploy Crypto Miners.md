---
title: Fake ChatGPT and Claude Apps Abuse Signed Executables to Deploy Crypto Miners
url: https://thehackernews.com/2026/10/fake-chatgpt-and-claude-apps-abuse.html
source: The Hacker News
date: 2026-10-29
fetch_date: 2026-10-30T07:56:33.211974
---

# Fake ChatGPT and Claude Apps Abuse Signed Executables to Deploy Crypto Miners

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Fake ChatGPT and Claude Apps Abuse Signed Executables to Deploy Crypto Miners](https://thehackernews.com/2026/10/fake-chatgpt-and-claude-apps-abuse.html)

**Ravie Lakshmanan**Oct 29, 2026Cryptocurrency / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1ij0gwe-L1jDZxdoUPZ6hpSJnJgMHh2bG8bFF2y8y-dJA9nY0Fr2JOU2i4NaCetGqvTZOtvaRXbZONR6d8ajjMR6DNm_X7OwaVCiH7dPycEN9xGI0psNvPYbwDhpGmUQ4Qyhp5x9fqQ_sgzjcReslK-a-gRS3kFr5_JOns1kkuC6UheDHVb2yaV8EAhIF/s1700-nu-rw-lo-l85-e365/claude-hack.jpg)

Threat actors are delivering malicious loaders and cryptocurrency miners under the guise of artificial intelligence (AI) desktop applications for Anthropic Claude and OpenAI ChatGPT as part of a campaign dubbed **Yoba**.

The activity involves creating fake GitHub projects that claim to be desktop applications like GPT-5.6 Sol, GPT-6 Astra, and Claude Opus, only to deliver a malware family called YobaLoader.

"The malware is placed next to legitimate, signed executables from OpenAI and Anthropic so it can be loaded indirectly, a technique commonly known as DLL sideloading, which is often used to bypass security protections," Check Point Research [said](https://research.checkpoint.com/2026/tricks-from-the-past-deployed-via-signed-chatgpt-and-claude-binaries/) in an analysis.

To add to the project's credibility, the attackers set up GitHub.io pages to describe the capabilities of the software. Although the GitHub projects' popularity is not manipulated using techniques like [ghost networks](https://thehackernews.com/2025/10/3000-youtube-videos-exposed-as-malware.html), signs point to the use of SEO poisoning tactics to ensure that links to them are surfaced on top of search results on Google.

Some of the identified GitHub pages links are below -

* github[.]com/gpt-5-6/sol-free-desktop
* gpt-5-6.github[.]io
* github[.]com/gpt-5-6/gpt-5-6.github.io
* github[.]com/gpt-6-astra/gpt-6-astra.github.io
* gpt-6-astra[.]github[.]io
* github[.]com/opus-5-0/opus-5-0.github[.]io
* opus-5-0[.]github[.]io

"Each repository uses a different email address (edwardcarlsonmkym[@]outlook[.]com, daxschneiderdjuu[@]outlook[.]com, and rioprestonlfyx[@]outlook[.]com), and the uploader appears to operate in UTC+4, UTC-4, and UTC+3 respectively," Check Point said. "This inconsistency likely reflects a deliberate attempt to obscure the threat actor's true operational time zone."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Hosted within these repositories are ZIP archives that, among other files, contain two specific components -

* **Setup.exe**, a legitimate signed OpenAI Codex or Claude executable
* **winmm.dll**, a malicious DLL that's sideloaded by the executable

The DLL is a dropper codenamed YobaDropper, which implements checksum value checks by hashing the basename of its host executable and if it matches a hard-coded value "0xE6C2F326." In other words, the check requires it to be launched under "Setup.exe," and fails if the DLL is executed on its own inside a sandboxed environment.

Additional anti-analysis techniques and pre-checks include 200,000 iterations of "Sleep(5500)," which amounts to 12.73 days, and skipping machines whose keyboard layout corresponds to that of Russia, Belarus, Tajikistan, Armenia, Azerbaijan, Georgia, Kazakhstan, Kyrgyzstan, Turkmenistan, and Uzbekistan.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9RYLUrzFNOI-8R5aF-IYA_SUIgqOM5wSeOxZGS2cbdVH9SBlb6Lkx51Cdt-ByHGzNltCMN0ue2ncQ6MoVGlW93SlvQs8Op2ZY8E5LzhuTY4fCMhHhPfNch10mH2nJfERUbMQKGLL7VMp07x_Jlc055d9qLRZkzi7tgeeqHNR6GqzMczISO6DNDLIVeIcg/s1700-nu-rw-lo-l85-e365/chain.png)

Another language ID excluded from the infection process is [Tatar](https://kbdlayout.info/KBDTT102/). Notably missing from the list is Ukraine, which used to be historically included in such checks.

YobaDropper, for its part, triggers a DLL sideloading chain of its own comprising "wmpdmc.exe" and "ampdui.dll," [copying the former from its "system32" folder](https://learn.microsoft.com/en-us/windows/iot/iot-enterprise/optimize/removable-packages/microsoft-windows-media-streaming) and placing it in a new directory named "WMProcess" created under "ProgramData."

The dropper then extracts and decrypts an embedded payload, and drops it into the same folder as "wmpdui.dll." It also establishes persistence by means of a scheduled task that launches the legitimate executable to load the malicious payload.

The second DLL is YobaLoader. It implements the same anti-sandbox technique as YobaDropper, requiring the malware to be run only by "wmpdmc.exe" by checking the hash against a hard-coded value ("0x552751E3"). The loader is responsible for three main tasks -

* Downloads an image from a Telegram channel ("t[.]me/yoba\_fanclub").
* Uses the last 50 bytes as a seed to generate a domain based on three lists of dictionary words and an integer value in the range 0–999 using a domain generation algorithm (DGA). The end result is domain in the format "*adjective*-*noun*-*verb*-*digit*.dedyn[.]io."
* Queries Google's DNS-over-HTTPS (DoH) API to obtain a Base64-encoded command from a DNS TXT record by passing the constructed domain as input.
* Decrypts the response to obtain the link to fetch the next-stage payload ("files.catbox[.]moe/z5zpy9.dat").

"By relying on a DoH service and common file-hosting platforms, the actor aims to bypass passive DNS monitoring and some gateway-based security protections, making their command-and-control traffic harder to distinguish from regular user activity," Check Point said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The downloaded payload is then injected into "svchost.exe," resulting in the execution of an XMRig cryptocurrency miner.

Evidence indicates that the first GitHub repository was created around July 2026, although the malicious releases were not uploaded u...