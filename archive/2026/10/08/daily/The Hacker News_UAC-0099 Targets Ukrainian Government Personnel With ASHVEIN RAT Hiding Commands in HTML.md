---
title: UAC-0099 Targets Ukrainian Government Personnel With ASHVEIN RAT Hiding Commands in HTML
url: https://thehackernews.com/2026/10/uac-0099-targets-ukrainian-government.html
source: The Hacker News
date: 2026-10-08
fetch_date: 2026-10-09T08:12:12.199514
---

# UAC-0099 Targets Ukrainian Government Personnel With ASHVEIN RAT Hiding Commands in HTML

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [UAC-0099 Targets Ukrainian Government Personnel With ASHVEIN RAT Hiding Commands in HTML](https://thehackernews.com/2026/10/uac-0099-targets-ukrainian-government.html)

**Ravie Lakshmanan**Oct 08, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZWPW7zD0DZUCKyeRcD-sBZtZ28n4PPaJDPjiskf9ghOI7b3aYbYCEbNvITxaYjCkejq8Vfuc0xeZtJ7p2R4j4dEqGXwfb1JLqQVHrgE4uxdSCq-JJgAeLA0WZbz5Fi98LQbxr3ncRXodrBd83xaX2UpXtDb-Q55ryWBPeXGAQlDBykN_BYecleld5rxJM/s1700-nu-rw-lo-l85-e365/uk.jpg)

The Russia-aligned threat actor known as **[UAC-0099](https://thehackernews.com/2023/12/uac-0099-using-winrar-exploit-to-target.html)** has been attributed to a previously undocumented .NET infostealer and remote access trojan (RAT) codenamed **ASHVEIN**.

According to TrendAI, the malware has been put to use in attacks targeting Ukrainian government personnel. The cybersecurity company is tracking the cluster under the name **Earth Sirrush** (previously SHADOW-EARTH-065).

ASHVEIN, which its developers internally refer to as "TelemetryBrowser," brings together credential theft, surveillance, and remote-control capabilities. Its functionality includes credential theft from Chrome and Firefox, GDI-based screenshot capture, file enumeration and retrieval, PowerShell remote shell execution, system fingerprinting, and encrypted command-and-control (C2) communications.

"ASHVEIN also hides tasking inside invisible HTML elements," TrendAI [said](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/earth-sirrush-russia-aligned-intrusion-set-4-years-evolving-espionage-tooling). "Some variants use a GitHub-based dead drop resolver as a fallback mechanism, while delivery methods include DLL sideloading, VHD containers, and dedicated .NET droppers."

UAC-0099 was first documented by the Computer Emergency Response Team of Ukraine (CERT-UA) in June 2023. It has a history of targeting Ukrainian government, defense, border guard, and logistics entities since at least mid-2022, emerging in the wake of Russia's full-scale invasion of Ukraine.

ESET, in its APT Activity Report [published](https://thehackernews.com/2025/11/trojanized-eset-installers-drop.html) in November 2025, said the cyber espionage crew can serve as an initial access broker for [Sandworm](https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html), a Russian advanced persistent threat (APT) group best known for its destructive attacks against Ukraine.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

In the intervening time period, the threat actor has steadily expanded its malware arsenal, while shifting from PowerShell- and Go-based tools to compiled C# and .NET Reactor-protected binaries concealed within steganographic image files.

Some of the malware families deployed by the threat actor over the years are listed below -

* 2022 – 2024: [LONEPAGE](https://thehackernews.com/2023/12/uac-0099-using-winrar-exploit-to-target.html) (PowerShell-based loader), [THUMBCHOP](https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html) (C#-based browser stealer), [CLOGFLAG](https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html) (keylogger), SEAGLOW, and OVERJAM (Go-based backdoors for interactive access and reverse-proxy, respectively)
* 2024 – 2025: [MATCHBOIL](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html) (C#-based loader), [MATCHWOK](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html) (C#-based backdoor), and [DRAGSTARE](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html) aka [NordDragonScan](https://thehackernews.com/2025/07/researchers-uncover-batavia-windows.html) (C#-based information stealer)
* October 2025: ASHVEIN aka TelemetryBrowser
* February – April 2026: [BadPaw aka CINDERBLOT](https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html) (.NET-based loader) and [MeowMeow](https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html) (backdoor)
* April – July 2026: [LUNCHPOKE](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html) (.NET DLL that masquerades as a Notepad++ plugin), [BURNYBEAR](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html) (.NET-based loader), and [MATCHBOIL.V2](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html) (updated version of MATCHBOIL)

"Five builds were compiled between October 8 and October 23, 2025, across three distinct packing variants," TrendAI said. "ASHVEIN overlaps functionally with DRAGSTARE in credential theft, screenshots, file collection, and WMI fingerprinting, but key differences separate them."

"DRAGSTARE was compiled by the NordDragon developer account, targets both Chrome and Firefox, and includes anti-VM checks and subnet scanning. ASHVEIN, compiled by the dev account, uses a different packing approach. The functional overlap, combined with separate build environments, indicates parallel tool development under different developer accounts for the same operational requirement."

UAC-0099 makes use of multiple delivery methods for ASHVEIN, including DLL sideloading (aka FORGECLAMP), VHD containers, and purpose-built .NET droppers. One such .NET executable is AnswerFromPolice, which embeds a Microsoft Word document that purports to be a response from the National Police of Ukraine.

AnswerFromPolice displays the decoy document impersonating the National Police of Ukraine while deploying the malware in the background. "This combination of institutional impersonation and credible decoy content is designed to increase the likelihood that recipients will open and trust the file," TrendAI said.

Another malware family that has undergone extensive evolution over the past year is MATCHBOIL. ESET's research indicates that the C# downloader has been under act...