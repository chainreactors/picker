---
title: Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer
url: https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:00.409872
---

# Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer

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

![cybersecurity](data:image/svg+xml;base64...)

# [Nearly 800 Malicious npm Packages Deliver Cross-Platform RAT and Infostealer](https://thehackernews.com/2026/08/nearly-800-malicious-npm-packages.html)

**Ravie Lakshmanan**Aug 07, 2026Malware / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIEXaa59LRblZ0rcBVbKDdH4w9Rszk27anNt20Onx7Li8D7FXbf3Ipod53uo3N2aa6Hj1QLJaNFDIBlrcgM3YZg0UJCsjI3maDKkFEdOeyhzis15St3QDg6WCXcYlbDRlw2WvgiOH-BL_v8I21QoSTE9kmJzzKqQwstqn11JWkAL1_9W41ZF04T-9ImaiL/s1700-e365/npms.jpg)

A cluster of nearly 800 malicious packages has been published to the npm registry as part of a new campaign designed to deliver cross-platform malware targeting Windows, Mac, and Linux systems.

"These packages appear to use AI slop squatted, or randomly generated typo-squatting package names, but all of them deliver a powerful RAT and infostealer payload," OpenSourceMalware researcher Paul McCarty [said](https://opensourcemalware.com/blog/russian-ai-slopsquatting-npm-campaign).

Unlike other npm-oriented software supply chain attacks that make use of lifecycle hooks like preinstall or postinstall to trigger the execution of malicious code, the newly identified packages come with a README that instructs developers to load them with require(), a built-in function to import modules, local files, and third-party packages.

The attack leads to the execution of a downloader named **[WEL1DROPPER](https://opensourcemalware.com/?search=%23wel1dropper)**, which, when executed, identifies the host operating system and processor architecture and fetches a compatible payload from one of the three Cloudflare Workers hosts. The three Cloudflare Workers domains are listed below -

* oob-worker.cf103-070.workers[.]dev
* oob-worker.cf102-baf.workers[.]dev
* oob-worker.cf99-9b3.workers[.]dev

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

If the HTTPS-based downloads fail, the malware switches to a platform-specific domain and uses DNS TXT records to obtain the next-stage from the domain "wel1[.]ru." The payload domain for each operating system and CPU architecture is as follows -

* Linux x64 - sdk.dl.wel1[.]ru
* Linux ARM64 - ext.dl.wel1[.]ru
* macOS - pkg.dl.wel1[.]ru
* Windows - net.dl.wel1[.]ru

"The package first requests a TXT record from c.<domain>," McCarty explained. "It parses the response as the number of payload chunks, accepting a value between 1 and 2,000. It then requests numbered TXT records. The returned strings are joined together and Base64-decoded into a binary buffer."

In the final stage, the payload is written to a temporary folder and executed either using "/bin/sh" on Linux and macOS, or "cmd.exe" on Windows.

Sonatype, which is also [tracking](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages) the campaign under the moniker Flooding Dropper, said the final stage is launched as a detached process, with the Windows version taking steps to patch Event Tracing for Windows (ETW) and Antimalware Scan Interface (AMSI) to interfere with monitoring, check for sandboxes and virtual environments, establish persistence through a Registry Run key and a scheduled task, and download an encrypted payload ("/pkg/update\_win.exe") and run it.

The macOS infection chain is similar, performing an identical set of actions to look for debuggers and analysis artifacts before retrieving a compatible payload ("/pkg/beacon\_mac.bin") from a remote server. If this fails, it employs the aforementioned DNS TXT delivery, sets up persistence using a LaunchAgent, and then starts the executable in a detached process.

The Linux sample, on the other hand, is an [UPX-packed](https://www.iblue.team/malware-analysis/identifying-upx-packed-elf-decompressing-fixing-and-analysing-linux-malware) ELF binary that's configured to download auxiliary payloads from a Cloudflare Worker URL ("oob-worker[.]cf99-9b3.workers[.]dev"), ultimately leading to the deployment of [Sliver](https://thehackernews.com/2022/08/cybercrime-groups-increasingly-adopting.html), an open-source command-and-control (C2) framework.

The packages have also been found to contain a file called "lib/telemetry.js" that implements a plausible-looking telemetry SDK but also contains the same downloader logic.

"The package entry point does not import this file, and it contains no additional hard-coded infrastructure," OpenSourceMalware said. "The oversized telemetry implementation appears intended to add noise and make the malicious behavior look like native profiling or analytics functionality during a quick review."

The presence of domains like "tcsbank[.]ru" and "cloudpayments[.]ru" in the macOS payload indicates that the campaign could be targeting Russian financial institutions and mobile payments.

It's also suspected to be an evolution of a [dependency confusion](https://thehackernews.com/2021/02/dependency-confusion-supply-chain.html) campaign codenamed [Moika](https://opensourcemalware.com/?search=%23moika) that was observed earlier this April and saw over 250 packages published to the npm registry to steal environment information and deliver an operating system-specific second-stage payload.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The development comes as Palo Alto Networks Unit 42 documented multiple campaigns targeting npm and the Python Package Index (PyPI) repository -

* A set of [10 npm packages](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-08-06-Obfuscated-JavaScript-Crypto-Stealer.txt) that download an obfuscated cryptocurrency stealer and a remote access trojan from an external server. "After installation, the packages export a 'getPlugin' function that constructs the URL from which the payload is downloaded as an obfuscated IIFE (Immediately Invoked Function Expression) JavaScript code embedded in a JSON object," Unit 42 said. "The payload implements a crypto stealer and Remote-Access Trojan (RAT) that allows the attacker to execute arbitrary commands on the infected host."
* A set of [malicious packages across npm and PyPI](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-07-21-Malicious-npm-PyPI-Supply-Chain-packages.txt) representing multiple di...