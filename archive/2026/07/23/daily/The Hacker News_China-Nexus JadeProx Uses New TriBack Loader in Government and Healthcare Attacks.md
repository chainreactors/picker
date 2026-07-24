---
title: China-Nexus JadeProx Uses New TriBack Loader in Government and Healthcare Attacks
url: https://thehackernews.com/2026/07/china-nexus-jadeprox-uses-new-triback.html
source: The Hacker News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:41.722495
---

# China-Nexus JadeProx Uses New TriBack Loader in Government and Healthcare Attacks

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

# [China-Nexus JadeProx Uses New TriBack Loader in Government and Healthcare Attacks](https://thehackernews.com/2026/07/china-nexus-jadeprox-uses-new-triback.html)

**Swati Khandelwal**Jul 23, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-rvCSGHVd2nngnpcdcc8Eh-QFaxQrcyegoSIPhUeTpr5qrGHcHYIstDAj08yLDeYcNZkZ26Ta53fdYefY8NjW8MprrOL4lQ4VnDCMpBrsrSQccyUipoC3VvFtMNUxUpUzOYra58WqjRwn952-fvzZLpXtgeY8Ao660YY49FaqcTTjBrDN_DsFFnsftJ8/s1700-e365/malware-attack.jpg)

An exposed Alibaba Cloud server has revealed a China-nexus operation that Group-IB tracks as **JadeProx**. The cluster has targeted government, healthcare, and education organizations across Asia and Latin America with a previously undocumented Windows loader called TriBack Loader.

Group-IB found the server in mid-April 2026 in Alibaba Cloud's Singapore region; it was offline by the time the [report](https://www.group-ib.com/blog/jadeprox-china-nexus-triback-loader/) published on July 23, 2026.

Its bash history, phishing packages, post-exploitation tools, and webshell paths laid the operation out: active intrusions against a Vietnamese public hospital's medical imaging system and Malaysia's Ministry of Foreign Affairs, scanning and exploitation follow-up against Hong Kong education infrastructure, and a spear-phishing package addressed to the National Congress of Honduras.

The operators reached the hospital's imaging server through webshells planted on an exposed Java management interface.

## One Loader, Four Builds

TriBack Loader appears in four infection chains built around DLL sideloading. Most recovered builds pair a legitimate signed executable with a malicious DLL and an encrypted .dat or .log payload.

The DLL reverses the payload bytes, XORs them with a rolling key, and executes the shellcode through Win32 calls that EDR watches less closely than CreateThread.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The builds rotate that final call: InitOnceExecuteOnce and a TimerQueue callback in two variants, and EtwpCreateEtwThread, an undocumented thread-creation routine in ntdll, in a third. The signed host binary changed between variants too. The repeated API sequence suggests a custom loader builder, the researchers say.

Two variants delivered [AdaptixC2](https://github.com/Adaptix-Framework/AdaptixC2), an [open-source post-exploitation framework](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html). A Claude-themed variant used DonutLoader to run [Beagle](https://thehackernews.com/2026/05/weekly-recap-linux-rootkit-macos-crypto.html), a backdoor [Sophos](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor) was first to document. The fourth variant's payload is unknown; its encrypted companion file was never recovered.

One spear-phishing archive carried a fake beverage-company account statement as the decoy. Another campaign impersonated Anthropic's Claude software from claude-pro[.]com, registered on March 28, 2026, serving a malicious MSI installer that, past a UAC prompt, placed the sideloading chain in the Windows Startup folder for persistence. The Beagle backdoor it delivered reported to license[.]claude-pro[.]com.

Sophos, working from the fake site, its hosting infrastructure, and malware samples, found the same reused XOR key in builds going back to February but said a shared key was not enough to conclude one actor.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjferLfJSPNKvAJjwcARhdIZ22X2L7w6pk51_TYGayX2Sb6UJgyjj5BZ1rK5rvXM1BScYi483gulhGgh89EzmuOACVDFuiCBx_bdmlDKERt3AJ-oUrik5f3t-04T4pc_rg97E51REvfwOdidzgkqsllX4xT0xEqnxK7RSwGBo7ac3AbXIA3UE72jasdkyo/s1700-e365/attack-chain.jpg)

Group-IB, working from the exposed server's contents, groups those builds with the Asian intrusions. It still stops short of naming an established group: tooling moves freely in the China-nexus ecosystem, Group-IB notes, so a match on tools is not a match on operators.

The operators also ran Nuclei with critical-severity templates only against a list of 14,653 Hong Kong education-related URLs, surfacing 13 unique vulnerabilities. Those 14,653 URLs are a scan list, and the report does not say how many of the follow-ups succeeded.

The report names four CVEs the operators attempted against individual hosts, and The Hacker News confirmed all four against NVD on July 23, 2026: CVE-2018-11511 in ASUSTOR ADM, CVE-2021-24139 in the 10Web Photo Gallery WordPress plugin, [CVE-2021-31755](https://thehackernews.com/2021/08/hackers-exploiting-new-auth-bypass-bug.html) in Tenda AC11 routers, and CVE-2021-32305 in WebSVN. Each carries a CVSS base score of 9.8. The Tenda bug has been on [CISA's Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) since November 3, 2021, with a federal remediation deadline that expired two weeks later.

## Detection Starts With the Sideloading Chain

Sophos assessed that the fake Claude site was likely part of an active malvertising campaign. If so, the exposure runs well past the ministries and hospitals, out to users searching for a Claude download.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3-o9La7DYm6jz5qcavVBLvRXUoQLqwrMmrvB529PbUxdg7TJZS3BMjVi4D7vd6V9vlSf_OX48mmXQWPgah_SPITaGgg4AP9YxB2AH-63YeWU39N3DXadwc_2zjIpTwCt0iyTdPZIM-KzKhDf_JDPWDGu3IbYfi1ilQE8Ly29HiKYagSIur-il4k7MMNv8/s728-e100/sygnia-d-3.png)](https://thn.news/sygnia-webinar)

Detection works off the file layout, because the filenames and signed hosts change per build.

* Flag signed vendor binaries running from user-writable, temporary, or Startup directories, especially when an encrypted .dat or .log file sits in the same folder.
* Look for unexpected copies of hostfxr.dll, avk.dll, or MpClient.dll, plus nested \_CL\_###### folders and ~del.vbs.bat.
*...