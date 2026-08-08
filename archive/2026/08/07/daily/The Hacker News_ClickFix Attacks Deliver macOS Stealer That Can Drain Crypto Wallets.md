---
title: ClickFix Attacks Deliver macOS Stealer That Can Drain Crypto Wallets
url: https://thehackernews.com/2026/08/clickfix-attacks-deliver-macos-stealer.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:00.564934
---

# ClickFix Attacks Deliver macOS Stealer That Can Drain Crypto Wallets

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

# [ClickFix Attacks Deliver macOS Stealer That Can Drain Crypto Wallets](https://thehackernews.com/2026/08/clickfix-attacks-deliver-macos-stealer.html)

**Ravie Lakshmanan**Aug 07, 2026Malware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKQGTQ6AquoAvAeMWXXITPacYsdChgFUpg7MLwKkfb2AylEuwQTk9av5GqMSdgtsB_tr_6QC70DrJkEo02t-Wo67z1gumix6FKKlOPSWo4fLEUHCibBoTrf1zCdmn72ESzo5CzCKKEgyETZ0FeVD_3QLfCNit7vIwlMA7MmwGYg2JGbeYOBrjSHmOnfpWl/s1700-e365/macos.jpg)

[ClickFix-style attacks](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) are being used to deliver a Go-based malware capable of stealing cryptocurrency assets, as well as browser-stored passwords, Apple iCloud Keychain data, and cached credentials.

The macOS-focused infection chain is designed to deliver a shell script that profiles the host and then fetches a macOS malware payload that's compatible with the computer's CPU architecture.

"While the malware payload is capable of stealing passwords, its most interesting function is its capability to slowly deplete cryptocurrency accounts, siphoning their contents into accounts under the threat actor's control," Huntress security researcher Andrew Brandt [said](https://www.huntress.com/blog/mac-crypto-draining-malware).

The attack chain begins with pasting a ClickFix command into the Terminal app, triggering the execution of a Bash profiler/loader that collects extensive system details and then retrieves a Mach-O payload that matches the victim's processor architecture. The payload is a Go-based stealer that can capture browser passwords, Apple Keychain data, and cached credentials and transmit them to a remote server operated by the threat actor.

Like other macOS stealers, the malware attempts to escalate privileges by prompting the victim to enter their system credentials via a fake prompt under the guise of an "unexpected system error" and restoring damaged system files.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

What's notable about the malware is that it also packs in a "DRAIN" routine that checks if a cryptocurrency wallet holds funds, and if so, redirects a chunk or all of it to an attacker-controlled wallet. There exist multiple versions of the same function based on the cryptocurrency being targeted. This includes Bitcoin, Litecoin, Dogecoin, Monero, Ethereum, and Ripple's XRP.

"While this may not be a brand new feature, it's the first time we have seen malware capable of emptying a cryptocurrency wallet that could be used to remove any less than the entire wallet's value," Huntress said. "The malware contained separate functions to determine just how much 1% of the wallet's contents is worth, depending on which cryptocurrency the malware targets."

The server staging the malicious payloads and the command-and-control (C2) server all link back to infrastructure belonging to [Aeza Group](https://thehackernews.com/2025/07/us-sanctions-russian-bulletproof.html), a Russian bulletproof hosting provider that has been sanctioned by the U.S., the U.K., and Australia for facilitating bad actors.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVSRfBpsMCn4hZCk6089FFaZHX1qwvDHjuAzLaiIFbpP04CEhJprvlwAbRuRgn3Zlx3HlAenH9pGg6a4Kbf_TZVT7yBH9ilRfvzALXwZdXbr6QewjZYy0KzEXtzR1Pq9sm_OMOqA8jmpD-TMybBCuBrx_QWjwJxXTkqmXRiqMByi0JAwtHDru_UM6xZ6d8/s1700-e365/drain.png)

The disclosure comes as a number of ClickFix attacks have been reported in recent weeks -

* A macOS ClickFix campaign distributing [MacSync and Atomic Stealer](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/) malware that uses a cluster of look-alike domains and implements a server-side browser-fingerprinting and hardware validation gate to conditionally serve the lures only to those visitors whose environment appears consistent with a genuine macOS browser, while blocking crawlers, sandboxes, and some automated analysis tools.
* A ClickFix variant that abuses [Program Compatibility Assistant](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-08-05-New-Clickfix-Variant.txt) ("pcalua.exe"), a legitimate Windows binary, as a launcher to bypass parent-process heuristics. "The victim is tricked (via a ClickFix lure) into pasting a crafted command that spawns PowerShell, uses WMI to create cmd.exe, mounts a remote WebDAV share, and loads a malicious DLL through rundll32.exe," Palo Alto Networks Unit 42 said. "The WebDAV share is exposed over HTTPS via CDN-fronted infrastructure at a per-victim tokenized URL (UUIDv4 path) used to deliver malicious DLL. Once loaded, the DLL is leveraged to deploy infostealer capabilities on the compromised host."
* A ClickFix campaign that uses [on-the-fly WebAssembly (wasm) module instantiation](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-07-16-ClickFix-campaign-using-wasm-and-steganography.txt) and steganography through SVG images to evade network-level detection. The activity uses legitimate-but-compromised websites to run injected malicious JavaScript that builds a wasm module that exports URLs from which the SVG files are downloaded to construct the ClickFix URL. "This final ClickFix URL is then dropped onto the DOM with a script tag to display the fake verification page," Unit 42 said. "The fake verification page presents a checkbox. When the checkbox is clicked, the page presents instructions to paste content into a Run window."

The findings also coincide with the discovery of two other stealer campaigns, one which delivers Lumma Stealer via files [disguised](https://www.bitdefender.com/en-us/blog/hotforsecurity/the-odyssey-piracy-lumma-stealer) as 1080p WEBRip and Blu-ray releases of The Odyssey, a newly released movie adaptation of Homer's ancient Greek epic poem of the same name, and another which uses [cracked software and pirated game lures](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-07-30-Remus-Info-Stealer-Uses-Blockchain-Anchored-C2.txt) hosted on fake websites via SEO poisoning to drop [Remus](https://flashpoint.io/blog/remus-stealer-a-new-not-so-new-infostealer/), a 64-bit...