---
title: North Korean Hackers Publish 26 npm Packages Hiding Pastebin C2 for Cross-Platform RAT
url: https://thehackernews.com/2026/03/north-korean-hackers-publish-26-npm.html
source: The Hacker News
date: 2026-03-02
fetch_date: 2026-03-03T04:13:45.475292
---

# North Korean Hackers Publish 26 npm Packages Hiding Pastebin C2 for Cross-Platform RAT

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

# [North Korean Hackers Publish 26 npm Packages Hiding Pastebin C2 for Cross-Platform RAT](https://thehackernews.com/2026/03/north-korean-hackers-publish-26-npm.html)

**Ravie Lakshmanan**Mar 02, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB4nJ8ODWGAqDEjQl4cCSKOtIJoGood2beXae5mc7MKzZbAYl1Ij2AX0L3CNCuUc4R4TL-DOR6bIHU6yzHfoFir_gl6jbUf_0w69pGg3tsXI92smKf02pmQPqkbyBs-eOUp0SqdGSrBH68os3R2lkTDGvGpi3R3-EThgOy_ATJKTXVqr0_ug-otA6FkeAo/s1700-e365/npm.jpg)

Cybersecurity researchers have disclosed a new iteration of the ongoing [Contagious Interview](https://thehackernews.com/2026/02/fake-nextjs-repos-target-developers.html) campaign, where the North Korean threat actors have published a set of 26 malicious packages to the npm registry.

The packages masquerade as developer tools, but contain functionality to extract the actual command-and-control (C2) by using seemingly harmless Pastebin content as a dead drop resolver and ultimately drop a developer-targeted credential stealer and remote access trojan. The C2 infrastructure is hosted on Vercel across 31 deployments.

The [campaign](https://kmsec.uk/blog/dprk-text-steganography/), tracked by Socket and kmsec.uk's Kieran Miyamoto is being tracked under the moniker **StegaBin**. It's attributed to a North Korean threat activity cluster known as Famous Chollima.

"The loader extracts C2 URLs steganographically encoded within three Pastebin pastes, innocuous computer science essays in which characters at evenly-spaced positions have been replaced to spell out hidden infrastructure addresses," Socket researchers Philipp Burckhardt and Peter van der Zee [said](https://socket.dev/blog/stegabin-26-malicious-npm-packages-use-pastebin-steganography).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The list of the malicious npm packages is as follows -

* argonist@0.41.0
* bcryptance@6.5.2
* bee-quarl@2.1.2
* bubble-core@6.26.2
* corstoken@2.14.7
* daytonjs@1.11.20
* ether-lint@5.9.4
* expressjs-lint@5.3.2
* fastify-lint@5.8.0
* formmiderable@3.5.7
* hapi-lint@19.1.2
* iosysredis@5.13.2
* jslint-config@10.22.2
* jsnwebapptoken@8.40.2
* kafkajs-lint@2.21.3
* loadash-lint@4.17.24
* mqttoken@5.40.2
* prism-lint@7.4.2
* promanage@6.0.21
* sequelization@6.40.2
* typoriem@0.4.17
* undicy-lint@7.23.1
* uuindex@13.1.0
* vitetest-lint@4.1.21
* windowston@3.19.2
* zoddle@4.4.2

All identified packages come with an install script ("install.js") that's automatically executed during package installation, which, in turn, runs the malicious payload located in "vendor/scrypt-js/version.js." Another common aspect that unites the 26 packages is that they explicitly declare the legitimate package they are typosquatting as a dependency, likely in an attempt to make them appear credible.

The payload serves as a text steganography decoder by contacting a Pastebin URL and extracting its contents to retrieve the actual C2 Vercel URLs. While the pastes seemingly contain a benign essay about computer science, the decoder is designed to look at specific characters in certain positions in the text and string them together to create a list of C2 domains.

"The decoder strips zero-width Unicode characters, reads a 5-digit length marker from the beginning, calculates evenly-spaced character positions throughout the text, and extracts the characters at those positions," Socket said. "The extracted characters are then split on a ||| separator (with an ===END=== termination marker) to produce an array of C2 domain names."

The malware then reaches out to the decoded domain to fetch platform-specific payloads for Windows, macOS, and Linux, a tactic widely observed in the Contagious Interview campaign. One such domain, "ext-checkdin.vercel[.]app" has been found to serve a shell script, which then contacts the same URL to retrieve a RAT component.

The Trojan connects to 103.106.67[.]63:1244 to await further instructions that allow it to change the current directory and execute shell commands, through which a comprehensive intelligence collection suite is deployed. It contains nine modules to facilitate Microsoft Visual Studio Code (VS Code) persistence, keylogging and clipboard theft, browser credential harvesting, TruffleHog secret scanning, and Git repository and SSH key exfiltration -

* **vs**, which uses a malicious tasks.json file to contact a Vercel domain every time a project is opened in VS Code by taking advantage of the [runOn: "folderOpen" trigge](https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html)r. The module specifically scans the victim's VS Code config directory across all three platforms and writes the malicious tasks.json directly into it.
* **clip**, which acts as a keylogger, mouse tracker, and clipboard stealer with support for active window tracking and conducts periodic exfiltration every 10 minutes.
* **bro**, which is a Python payload to steal browser credential stores.
* **j**, which is a Node.js module used for browser and cryptocurrency theft by targeting Google Chrome, Brave, Firefox, Opera, and Microsoft Edge, and extensions like MetaMask, Phantom, Coinbase Wallet, Binance, Trust, Exodus, and Keplr, among others. On macOS, it also targets the iCloud Keychain.
* **z**, which enumerates the file system and steals files matching certain predefined patterns.
* **n**, which acts as a RAT to grant the attacker the ability to remotely control the infected host in real-time via a persistent WebSocket connection to 103.106.67[.]63:1247 and exfiltrate data of interest over FTP.
* **truffle**, which downloads the legitimate [TruffleHog secrets scanner](https://github.com/trufflesecurity/trufflehog) from the official GitHub page to discover and exfiltrate developer secrets.
* **git**, which collects files from .ssh directories, extracts Git credentials, and scans repositories.
* **sched**, which is the same as "vendor/...