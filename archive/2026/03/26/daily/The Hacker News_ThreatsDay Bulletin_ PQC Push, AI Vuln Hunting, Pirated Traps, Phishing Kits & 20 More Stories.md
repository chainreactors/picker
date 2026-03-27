---
title: ThreatsDay Bulletin: PQC Push, AI Vuln Hunting, Pirated Traps, Phishing Kits & 20 More Stories
url: https://thehackernews.com/2026/03/threatsday-bulletin-pqc-push-ai-vuln.html
source: The Hacker News
date: 2026-03-26
fetch_date: 2026-03-27T04:33:40.635788
---

# ThreatsDay Bulletin: PQC Push, AI Vuln Hunting, Pirated Traps, Phishing Kits & 20 More Stories

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [ThreatsDay Bulletin: PQC Push, AI Vuln Hunting, Pirated Traps, Phishing Kits & 20 More Stories](https://thehackernews.com/2026/03/threatsday-bulletin-pqc-push-ai-vuln.html)

**Ravie Lakshmanan**Mar 26, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOuz5FhCwEEsebWV1fHdF2VE-lnNBee6FrzMYsTdEODBsw07F76vTo3-UJKUz7QENWIUU_J7IdNj2vlhZbbdL5Chz6Vt6SyEbIwH-vw3J76SlUT02eZwbGHG5egcJNFeaKBd3sdLrp7egajwLniaeBMwZdXAMv3la2Ywzxin4gLiZK6lHbdPSzUDFCuWHF/s1700-e365/tday-main.jpg)

Some weeks in security feel loud. This one feels sneaky. Less big dramatic fireworks, more of that slow creeping sense that too many people are getting way too comfortable abusing things they probably shouldn’t even be touching.

There’s a little bit of everything in this one, too. Weird delivery tricks, old problems coming back in slightly worse forms, shady infrastructure doing shady infrastructure things, and the usual reminder that if criminals find a workflow annoying, they’ll just make a new one by Friday. Efficient little parasites. You almost have to respect the commitment.

A few of these updates have that nasty “yeah, that tracks” energy. Stuff that sounds niche right up until you picture it landing in a real environment with real users clicking real nonsense because they’re busy and tired and just trying to get through the day. Then it stops being abstract pretty fast.

So yeah, this week’s ThreatsDay Bulletin is a solid scroll-before-you-log-off kind of read. Nothing here needs a full panic spiral, but some of it definitely deserves a raised eyebrow and maybe a muttered: “Oh come on.” Let’s get into it.

1. PQC migration fast-tracked

   [Google Announces Accelerated Timeline for its PQC Migration](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)

   Google has unveiled a 2029 timeline to secure the quantum era with post-quantum cryptography (PQC) migration, urging other engineering teams to follow suit. "This new timeline reflects migration needs for the PQC era in light of progress on quantum computing hardware development, quantum error correction, and quantum factoring resource estimates," the tech giant [said](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/). "Quantum computers will pose a significant threat to current cryptographic standards, and specifically to encryption and digital signatures. The threat to encryption is relevant today with store-now-decrypt-later attacks, while digital signatures are a future threat that require the transition to PQC prior to a Cryptographically Relevant Quantum Computer (CRQC). That's why we've adjusted our threat model to prioritize PQC migration for authentication services." As part of the effort, the company said Android 17 is integrating PQC digital signature protection using the Module-Lattice-Based Digital Signature Algorithm ([ML-DSA](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)). This [includes](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) upgrading the Android Verified Boot (AVB) with support for ML-DSA to ensure that the software loaded during the boot sequence remains highly resistant to unauthorized tampering. The second PQC upgrade concerns the transition of Remote Attestation to a fully PQC-compliant architecture and updating Android Keystore to natively support ML-DSA.
2. AI finds hidden vulns

   [GitHub Brings AI-Powered Detections to GitHub Code Security](https://github.blog/security/application-security/github-expands-application-security-coverage-with-ai-powered-detections/)

   GitHub said it's introducing AI-powered security detections in GitHub Code Security to expand application security coverage across more languages and frameworks. "These detections complement CodeQL by surfacing potential vulnerabilities in areas that are difficult to support with traditional static analysis alone," GitHub [said](https://github.blog/security/application-security/github-expands-application-security-coverage-with-ai-powered-detections/). "This hybrid detection model helps surface vulnerabilities – and suggested fixes – directly to developers within the pull request workflow." The Microsoft subsidiary said the move is designed to uncover security issues "in areas that are difficult to support with traditional static analysis alone." The new hybrid model is expected to enter public preview in early Q2 2026.
3. Pirated apps spread backdoors

   [Sandworm Leverages Pirated Software Ploys to Drop Backdoors](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html)

   The Russian threat actor known as Sandworm (aka APT-C-13) has been attributed with moderate confidence to an attack campaign that leverages pirated versions of legitimate software like Microsoft Office ("Microsoft.Office.2025x64.v2025.iso") as lures to deliver different backdoors tracked as Tambur, [Sumbur, Kalambur](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html), and DemiMur to high-value targets. It's assessed that these attacks use Telegram as a distribution vector, using social engineering tactics to target Ukrainian users seeking software cracks. Tambur is designed to spawn SSH reverse tunnels to issue malicious commands, while Kalambur revolves around intranet penetration, remote desktop (RDP) takeover, and persistent communication. Sumbur is a successor to Kalambur with improved obfuscation techniques. DemiMur is mainly used to tamper with the trust chain and evade detection. "Attackers use this module to force the import of a forged DemiMurCA.crt root certificate into the operating system's trusted root certificate authority store," the 360 Advanced Threat Research Institute [said](https://mp.weixin.qq.com/s/QWe2m4qdp45u1cuA5rgLwQ). "When subsequent scripts are executed, Windows automatically verifies the validi...