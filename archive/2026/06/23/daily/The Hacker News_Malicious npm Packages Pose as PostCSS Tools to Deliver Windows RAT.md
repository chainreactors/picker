---
title: Malicious npm Packages Pose as PostCSS Tools to Deliver Windows RAT
url: https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html
source: The Hacker News
date: 2026-06-23
fetch_date: 2026-06-24T06:06:31.612739
---

# Malicious npm Packages Pose as PostCSS Tools to Deliver Windows RAT

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Malicious npm Packages Pose as PostCSS Tools to Deliver Windows RAT](https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html)

**Ravie Lakshmanan**Jun 23, 2026Supply Chain Attack / Developer Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiENcFC1DFPXKuRCT_WmSwq-wpzC8IcZUdZzu5IHi597n77W8LFs9qSUdDPCuMK9QzkRZEBMbBh4p2xhnI1OXZu4akIgR5suIv_yRA7AtEkojDcyXaU5x0UiZKRDRvTn0n0wy9HIQnhJj9zUO0rpemNOFNZEmMl4NQsCj5aDEpDrqXUkivsOX1QoLRqeKZh/s1700-e365/npmm.jpg)

Cybersecurity researchers have discovered a set of malicious npm packages that are designed to deliver a Windows-based remote access trojan (RAT).

The list of identified packages, is below -

* aes-decode-runner-pro (145 downloads)
* postcss-minify-selector (256 downloads)
* postcss-minify-selector-parser (615 downloads)

All the packages were published over the past month by an npm user named "[abdrizak](https://www.npmjs.com/~abdrizak)" and continue to be available for download from npm as of writing.

"Aes-decode-runner-pro and postcss-minify-selector-parser both present themselves as layered AES/custom-codec packages and depend on the legitimate postcss-selector-parser," JFrog [said](https://research.jfrog.com/post/from-postcss-typosquat-to-windows-rat/) in an analysis. "Postcss-minify-selector presents itself as a PostCSS selector minifier and depends on postcss-minify-selector-parser."

As for "postcss-minify-selector-parser," the name is a reference to "[postcss-selector-parser](https://www.npmjs.com/package/postcss-selector-parser)," a widely used npm library with more than 127 million weekly downloads. Regardless of the package downloaded, the attack chain leads to the deployment of the same Windows malware.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The packages come embedded with a JavaScript dropper that writes a PowerShell script ("settings.ps1") to disk and executes it. The PowerShell script then acts as a downloader for a next-stage payload retrieved from an external server ("nvidiadriver[.]net") using the "curl.exe."

The retrieved payload is a ZIP archive, from which a Visual Basic Script ("update.vbs") file is extracted and run using "wscript.exe." Also bundled in the downloaded ZIP file is a Python runtime, a Python loader ("loader.py"), and a number of Python extension modules (\*.pyd) compiled using [Nuitka](https://nuitka.net/).

Visual Basic is responsible for setting up the Python environment on the compromised host and launching the "loader.py" script, which then triggers the core logic of the malware. The RAT is equipped to gather host information, siphon credentials from Google Chrome, collect data from Chrome extensions, run shell commands, and download/upload files to and from a command-and-control (C2) server ("95.216.92[.]207:8080").

These features are realized through a set of Python native extension modules -

* config.pyd, which contains constants, command IDs, C2 URL, registry key names
* api.pyd, which handles HTTP C2 packet exchange
* audiodriver.pyd, which handles the main RAT orchestration loop
* command.pyd, which profiles the host, runs virtual machine (VM) checks, file transfer, and shell execution
* auto.pyd, which performs Chrome credential and extension theft, bypassing app-bound encryption ([ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)) protections
* util.pyd, which acts as tar/gzip archive helpers

"This case shows how a small parser-like package can hide a multi-stage Windows payload while appearing related to legitimate build tooling with massive weekly usage," JFrog said. "For defenders, the important lesson is to treat lookalike build dependencies as potential delivery mechanisms, not just harmless naming noise."

The discovery coincides with three other campaigns targeting the npm and TypeScript ecosystem -

* A malicious package named "[apintergrationpost](https://safedep.io/malicious-apintergrationpost-npm-myra-rat/)" that delivers a full-featured Linux RAT dubbed MYRA, while claiming to be a Node.js integration client for authorized red team exercises. "It compiles a native C rootkit during install, establishes three independent persistence mechanisms, masquerades as a systemd service, supports fileless execution, and provides interactive shell access with live screen streaming," SafeDep said.
* A malicious package named "[@withgoogle/stitch-sdk](https://safedep.io/withgoogle-stitch-sdk-scope-squat-credential-harvester/)" that impersonates Google's Stitch AI design tool but comes with capabilities to steal developer credentials from eight sources (Claude Code, git config, ~/.git-credentials, SSH public keys, GitHub CLI, npm config, ~/.npmrc, and ~/.docker/config.json) and exfiltrates them to an attacker-controlled domain ("stitch-production[.]org/api/v1").
* A cluster of [five packages](https://safedep.io/procwire-npm-windows-dropper-campaign/) ("procwire," "routecraft," "endpointmap," "bytecraft," and "staticlayer") that delivers a dropper binary on Windows hosts from an external server and executes it during npm install. The "routecraft" package lists "procwire" as a dependency, while the latter lists "endpointmap" and "bytecraft" as dependencies. The last package, "staticlayer," is designed to run on the server side and deliver files to a client that presents the dropper's exact User-Agent.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Users who have installed any of the above packages are advised to remove them with immediate effect, remove any artifacts created by them, and rotate credentials from impacted developer machines.

The findings also coincide with a [supply chain attack](https://safedep.io/astro-config-blockchain-c2-supply-chain/) targeting the "[gonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)" knowledge graph tool to push a malicious payload that "be...