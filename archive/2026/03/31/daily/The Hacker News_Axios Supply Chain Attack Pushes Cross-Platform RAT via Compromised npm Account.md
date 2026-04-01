---
title: Axios Supply Chain Attack Pushes Cross-Platform RAT via Compromised npm Account
url: https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html
source: The Hacker News
date: 2026-03-31
fetch_date: 2026-04-01T04:47:53.494107
---

# Axios Supply Chain Attack Pushes Cross-Platform RAT via Compromised npm Account

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

# [Axios Supply Chain Attack Pushes Cross-Platform RAT via Compromised npm Account](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html)

**Ravie Lakshmanan**Mar 31, 2026Open Source / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdY8iKA7o-K-4HkIjPMiBRWAn5vCvSNDu1sm09t10vWMzXO6cIblLHQyu1no-KBhq4W7EWS03zqvI4n_k9mYWCDsCVoiX4cwsV9T862WTq1yGb6VkX1ZGTa7MKZE43llbF9n2Py1mC2yhCIfRlXGkvya_NQ9lX7vZ32YW8pHZlw1dPZcI9eCrgysiWqSSR/s1700-e365/Axios-attack.jpg)

The popular HTTP client known as [Axios](https://www.npmjs.com/package/axios) has suffered a supply chain attack after two newly published versions of the npm package introduced a malicious dependency that delivers a trojan capable of targeting Windows, macOS, and Linux systems.

Versions 1.14.1 and 0.30.4 of Axios have been found to inject "[plain-crypto-js](https://www.npmjs.com/package/plain-crypto-js)" version 4.2.1 as a fake dependency.

According to StepSecurity, the two versions were [published](https://github.com/axios/axios/issues/10604) using the compromised npm credentials of the primary Axios maintainer ("jasonsaayman"), allowing the attackers to bypass the project's GitHub Actions CI/CD pipeline.

"Its sole purpose is to execute a postinstall script that acts as a cross-platform remote access trojan (RAT) dropper, targeting macOS, Windows, and Linux," security researcher Ashish Kurmi [said](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan). "The dropper contacts a live command and control server and delivers platform-specific second-stage payloads. After execution, the malware deletes itself and replaces its own package.json with a clean version to evade forensic detection."

Users who have Axios versions 1.14.1 or 0.30.4 installed are required to rotate their secrets and credentials with immediate effect, and downgrade to a safe version (1.14.0 or 0.30.3). The malicious versions, as well as "plain-crypto-js," are no longer available for download from npm.

With more than 83 million weekly downloads, Axios is one of the most widely used HTTP clients in the JavaScript ecosystem across frontend frameworks, backend services, and enterprise applications.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"This was not opportunistic," Kurmi added. "The malicious dependency was staged 18 hours in advance. Three separate payloads were pre-built for three operating systems. Both release branches were hit within 39 minutes. Every trace was designed to self-destruct."

The timeline of the attack is as follows -

* March 30, 2026, 05:57 UTC - A clean version of the package "plain-crypto-js@4.2.0" is published.
* March 30, 2026, 23:59 UTC - A new version ("plain-crypto-js@4.2.1") with the payload added is published.
* March 31, 2026, 00:21 UTC - A new version of Axios ("axios@1.14.1") that injects "plain-crypto-js@4.2.1" as a runtime dependency is published using the compromised "jasonsaayman" account.
* March 31, 2026, 01:00 UTC - A new version of Axios ("axios@0.30.4") that injects "plain-crypto-js@4.2.1" as a runtime dependency is published using the compromised "jasonsaayman" account.

According to StepSecurity, the threat actor behind the campaign is said to have compromised the npm account of "jasonsaayman" and changed its registered email address to a Proton Mail address under their control ("ifstap@proton.me"). The "plain-crypto-js" was published by an npm user named "nrwise" with the email address "nrwise@proton.me."

It's believed that the attacker obtained a long-lived classic npm access token for the account to take control and directly publish poisoned versions of Axios to the registry.

The embedded malware, for its part, is launched via an [obfuscated Node.js dropper](https://www.endorlabs.com/learn/npm-axios-compromise) ("setup.js") and is designed to branch into one of three attack paths based on the operating system -

* On macOS, it runs an AppleScript payload to fetch a trojan binary from an external server ("sfrclak.com:8000"), save it as "/Library/Caches/com.apple.act.mond," change its permissions to make it executable, and launch it in the background via /bin/zsh. The AppleScript file is deleted after execution to cover up the tracks.
* On Windows, it locates the PowerShell binary path, copies it to the "%PROGRAMDATA%\wt.exe" (disguising it as the Windows Terminal app), and writes a Visual Basic Script (VBScript) to the temp directory and executes it. The VBScript contacts the same server to fetch a PowerShell RAT script and execute it. The downloaded file is then deleted.
* On other platforms (e.g., Linux), the dropper runs a shell command via Node.js’s execSync to fetch a Python RAT script from the same server, save it to "/tmp/ld.py," and execute it in the background using the nohup command.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZYI1-U2x1NxniUyNqyOamnEjLToB2HSDCTN_Xm8buVSkf_sO0eQQl5xZmMaNty8X4oAM-drrAaEQvym9MT7Fnmr3aVYhaFrXNNAyIe-pQ53z697lxLBeDGnbLYjQhU3xbJ9VdpYz8iPu13c5Bd5gigvFcz5Z5BTXE50UrXuqQbVgbikRy8vH8CwSAW7Gn/s1700-e365/works.jpg)

"Each platform sends a distinct POST body to the same C2 URL — packages.npm.org/product0 (macOS), packages.npm.org/product1 (Windows), packages.npm.org/product2 (Linux)," StepSecurity said. "This allows the C2 server to serve a platform-appropriate payload in response to a single endpoint."

The downloaded second-stage binary for macOS is a C++ RAT that fingerprints the system and beacons to a remote server every 60 seconds to retrieve commands for subsequent execution. It supports capabilities to run additional payloads, execute shell commands, enumerate the file system, and terminate the RAT.

SafeDep's analysis of the Linux RAT has revealed that it supports the same commands as its macOS counterpart. The absence of a persistence mechani...