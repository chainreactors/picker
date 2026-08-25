---
title: WordlistLoader Delivers Amatera via ClickFix, SynkLoader Phishes Windows Passwords
url: https://thehackernews.com/2026/08/wordlistloader-delivers-amatera-via.html
source: The Hacker News
date: 2026-08-24
fetch_date: 2026-08-25T03:00:40.994999
---

# WordlistLoader Delivers Amatera via ClickFix, SynkLoader Phishes Windows Passwords

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [WordlistLoader Delivers Amatera via ClickFix, SynkLoader Phishes Windows Passwords](https://thehackernews.com/2026/08/wordlistloader-delivers-amatera-via.html)

**Ravie Lakshmanan**Aug 24, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNZ5JtaLAZIvAO7R42dqB1NBKwtOlFHZIl0yqtfPhyphenhyphenHMJB9MMg8oLLb8p6n9mF67PgHSytYigaqeAoGejuVd42lDlCT42T6vqCgfl6IE-8LnMQjyiCj8MVMdg5ZKznn2cZ18T9zubhLJ-JUZLSWeqEVGQbke44f83WHpoMuaVM9J6G0FA-9RG8_wb8lUTt/s1700-e365/windows-signin.jpg)

Cybersecurity researchers have flagged two new malware families called  **WordlistLoader** and **SynkLoader** that's used to deliver next-stage payloads and likely sell access to ransomware groups.

According to findings from Gen Digital, WordlistLoader is being used to deliver Amatera Stealer (aka ACR Stealer or AcridRain Stealer) via [ClearFake](https://thehackernews.com/2025/03/clearfake-infects-9300-sites-uses-fake.html) campaigns, which employ the ClickFix (aka FakeCaptcha) technique to dupe victims into running malicious commands under the pretext of completing CAPTCHA verification checks.

"Once the visitor clicks on the 'I'm not a robot' checkbox, they're walked through the well-known ClickFix flow, where a malicious command is copied into their clipboard and the victim is instructed to paste it into the Windows Run dialog and execute it, leading to the download of WordlistLoader that ultimately results in the execution of Amatera," security researcher Vojtěch Krejsa [said](https://www.gendigital.com/blog/insights/research/wordlistloader-delivering-amatera-via-clearfake-campaigns).

The ClickFix prompts are displayed on real websites that have been compromised with malicious JavaScript that's injected in the form of a Base64-encoded blob. The blob, for its part, fetches another JavaScript from a smart contract stored on the blockchain, an approach known as EtherHiding, and dynamically executes the retrieved code. Some of the compromised websites serving ClickFix prompts are below -

* abogadosrosarinos[.]com
* aptisweb[.]com
* avene-hebergement[.]com
* https-xhamster[.]com
* www.caesarjaco.co[.]id
* skybap[.]shop

In recent months, ClearFake campaigns have been revamped to use "cdn.jsdelivr[.]net" to host the threat actor's malicious JavaScript, highlighting the abuse of a legitimate Content Delivery Network (CDN) to stage rogue payloads.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"Although the CDN is meant for hosting JavaScript, the threat actors are actually using it to host their malicious PowerShell script," Expel [noted](https://expel.com/blog/clearfake-new-lotl-techniques/) earlier this January. "While jsDelivr appears to be taking down the actor's malicious repositories fairly quickly, the first stage's use of EtherHiding allows them to easily swap out burned URLs for fresh working ones."

The ClickFix command uses "conhost" to launch a hidden "cmd.exe" process, then map a remote WebDAV share using pushd, and finally launch the loader via "rundll32.exe." It's worth noting this WebDAV-based approach [overlaps](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/) with a similar campaign recently highlighted by Microsoft.

In this campaign, a ClickFix prompt instructs the target to run a command that launches "cmd.exe," which subsequently invokes "rundll32.exe" to load a DLL from a remote WebDAV share accessed over HTTPS. Three different versions of the command have been recorded -

* Direct rundll32 invocation
* pushd-Mounted WebDAV Share followed by rundll32.exe invocation
* Headless and obfuscated pushd execution followed by rundll32.exe invocation (which matches the WordlistLoader infection chain)

"In the more advanced variant, threat actors further enhance stealth by launching commands through conhost.exe –headless, suppressing visible console windows, and employing environment variable obfuscation with delayed variable expansion to conceal critical execution components such as pushd, rundll32, and the remote host name," Microsoft said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgt_3wv-0k_CdtHlmcPCP6oBbYv2TofOSesaMiOVnKJR-XK1v3v5dKieHavEi3CtBsGvov0dE3DyH3s_FUGaZrJh101HuzI-u8IkmGQDczD67hAgWWjm9p3aDwqSM9pM04M7smfEUOqt9GOFRoVNFrKMzYEoKn5Q52m7lw8S620cYVKBrYL9mkbaIGzv-nB/s1700-e365/gen.jpg)

"Combined with minimized or headless execution, these techniques reduce user visibility, complicate static analysis and detection, and enable the infection chain to execute with minimal indication to the victim."

The primary difference is that the Python-based loaders observed by Microsoft between late April 2026 and mid-June 2026 in connection with the ACR Stealer intrusion chain have been replaced by WordlistLoader. ACR Stealer has also been propagated via ClickFix prompts that trigger a command spawning MSHTA to retrieve and execute remote HTA content from a threat actor-controlled domain.

This leads to the execution of a VBScript loader that decodes and runs PowerShell designed to fetch a JPEG image from an image-hosting service and extract it from the stealer payload in memory to minimize on-disk artifacts and complicate detection and analysis.

"The primary purpose of WordlistLoader, an intermediate stage in the Amatera infection chain, is to reconstruct a shellcode that serves as the entry point for subsequent stages," Gen Digital said. At the same time, it employs a hardware-breakpoint-based method to bypass Event Tracing for Windows (ETW) and avoid leaving traces of malicious activity.

WordlistLoader gets its name from the fact that the shellcode is stored in encoded form as a sequence of plain English words, with each word representing one byte. Gen said it also identified a variant that replaces the wordlist with an array of 16-byte UUID-encoded chunks.

The shellcode ulti...