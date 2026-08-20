---
title: SilkParasite Espionage Campaign Targets Central Asian Governments with Five New RATs
url: https://thehackernews.com/2026/08/silkparasite-espionage-campaign-targets.html
source: The Hacker News
date: 2026-08-19
fetch_date: 2026-08-20T02:56:56.261891
---

# SilkParasite Espionage Campaign Targets Central Asian Governments with Five New RATs

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

# [SilkParasite Espionage Campaign Targets Central Asian Governments with Five New RATs](https://thehackernews.com/2026/08/silkparasite-espionage-campaign-targets.html)

**Ravie Lakshmanan**Aug 19, 2026 Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgukQx26zt-EE2Q-I5EPzGDeXiUneL1NzNma73qc5r03gJ5Xj6kiTigXadbXa1XWqg7Y-UHq5YzEu7bPxN4BXjVUbId9eaPwWddiP_oB7Zz2fBV0bxr2S2wh9oVEFI-IEe4jMgA1REmrbKFSE33oztVDuz0p2TQhKA_0koqZ3qYcWH_d5Ec4lExxdMzWw5I/s1700-e365/malware-code.jpg)

A previously unreported cyber espionage operation dubbed **SilkParasite** has been observed targeting government bodies in Central Asia.

The intrusion set makes use of seven remote access tool (RAT) families, five of which have never been previously documented: DriveSilkRAT, CookiETagRAT, NomadRAT, GoginRAT, and NodeEdgeRAT. SilkParasite, first discovered in late 2025, is assessed to be a China-nexus threat cluster with medium confidence.

"What makes SilkParasite interesting is the traces of AI-assisted development running through otherwise expert code, which is a different thing from AI-generated malware," Bitdefender Labs [said](https://businessinsights.bitdefender.com/silkparasite-tracking-china-nexus-apt-across-central-asia) in a technical report shared with The Hacker News.

Unlike other operations that rely on AI-generated malware, SilkParasite's arsenal exhibits all hallmarks typically associated with professional espionage tooling that's developed by a team of human operators while AI is likely used to streamline the process.

The Romanian cybersecurity vendor said the clearest sign of the technology use comes from a phishing lure that's indubitably AI-generated. It's also the only place the adversary seems to have been sloppy, which has raised the possibility that it may have been a deliberate choice to confuse attribution efforts.

SilkParasite is the third prominent threat actor to strike Central Asia in recent years, after [UAC-0063](https://thehackernews.com/2025/01/uac-0063-expands-cyber-attacks-to.html) and [FamousSparrow](https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html). One notable aspect that ties the operation to China is the use of a backdoor dubbed [BLOODALCHEMY](https://thehackernews.com/2024/05/japanese-experts-warn-of-bloodalchemy.html), which is an updated version of Deed RAT, itself a successor to [ShadowPad](https://thehackernews.com/2021/08/shadowpad-malware-is-becoming-favorite.html). ShadowPad, for its part, is an evolution of PlugX. Both ShadowPad and PlugX are widely put to use by Chinese hacking groups.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

First documented by Elastic Security Labs in October 2023, BLOODALCHEMY was observed as part of attacks mounted by REF5961 targeting government organizations in Southern and Southeast Asia. The C-based backdoor is said to be part of a broader toolset that's launched by means of a DLL loader that's sideloaded using a legitimate binary.

The malware supports basic commands to gather host information, overwrite the malware binary, the loader, or the main trusted binary that's vulnerable to DLL sideloading, and terminate and uninstall itself.

Another indicator that points to China-nexus is the use of an updated version of [SpiceRAT](https://thehackernews.com/2024/06/chinese-hackers-deploy-spicerat-and.html), which is equipped to download and run executable binaries and arbitrary commands. It's attributed to another Chinese-speaking threat actor codenamed SneakyChef.

Attack chains begin with password-protected RAR archives bearing malicious Microsoft Office documents that are likely delivered via spear-phishing emails. The password to open the archive is supplied in the email body. Opening the document launches a macro responsible for trigger a DLL sideloading sequence to drop the first-stage payload.

"The lures were regionally tailored," Bitdefender said. "Recovered documents were crafted to look relevant to government

entities in Uzbekistan, Turkmenistan, Kyrgyzstan, Tajikistan, and Kazakhstan, several impersonating specific ministries. A further document, recovered from a public malware-sharing platform, was addressed to a Georgian government entity."

Perhaps more significantly, the macro checks if Kaspersky's antivirus software is installed and running on the machine before execution. This is indicative of attempts to bypass detection given the prevalence of the security program in the region.

Almost every single tool deployed over the course of the attack implements a plugin-oriented architecture that allows the operators to expand its capabilities at will, while selectively serving payloads that can better adapt to the victim environment and keeping the detection footprint small.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGNB_RB_AmARMTgpdrN7Ks-W0tZjy46nGZ_OJaA0CNv6S1Bl9760_ccnlZeEyBp_JwdpLUrqvSOftnJpZWV_5VgPPrEifX1w-6_ObHjhwpanYeK-a046wdAgN83akSX3elBrl5Qu-nDlfV5FE9Pp6m3gEQ3gRgeDrr7ljvjXqACvQ16N2NTxMSOA32TLk8/s1700-e365/rats.jpg)

What's more, the modular system offers another crucial advantage in that it enables the threat actors to upgrade the components' capabilities without having to replace the underlying foundations. The seven implants span four different programming languages -- .NET, C++, Go, and JavaScript -- and use DLL sideloading as the main delivery vector.

The approach involves bringing their own copy of a legitimately signed program, as opposed to leveraging an already installed binary, and placing the rogue DLL under a name the executable looks for, causing the malicious code to be run. A brief description of each of the malware family is as follows -

* **DriveSilkRAT** (.NET/C++), which uses Google Drive as command-and-control (C2) to poll a specific folder for tasking, run it through an in-memory .NET plugin system, and upload the resu...