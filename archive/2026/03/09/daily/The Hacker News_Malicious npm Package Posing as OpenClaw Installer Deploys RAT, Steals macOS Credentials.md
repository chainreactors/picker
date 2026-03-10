---
title: Malicious npm Package Posing as OpenClaw Installer Deploys RAT, Steals macOS Credentials
url: https://thehackernews.com/2026/03/malicious-npm-package-posing-as.html
source: The Hacker News
date: 2026-03-09
fetch_date: 2026-03-10T04:04:05.029238
---

# Malicious npm Package Posing as OpenClaw Installer Deploys RAT, Steals macOS Credentials

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

# [Malicious npm Package Posing as OpenClaw Installer Deploys RAT, Steals macOS Credentials](https://thehackernews.com/2026/03/malicious-npm-package-posing-as.html)

**Ravie Lakshmanan**Mar 09, 2026Malware / Developer Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNWahQ89p408qBpZO2cmP-m44fNG_BRHT34hjfmDGn2WhALZRls9d94ap8uK0ZYXj1JjAgxdDogTHv_1PHloweK3RtglJheCsgulTB0-KrYOgUFI3Gvp4FJiPaV33FVa8I5bl-v92O1IephSEiV_FMU010of5pnmgMQ0ZmBuvY4yC0Bl0ndth42P924uxR/s1700-e365/openclaw.jpg)

Cybersecurity researchers have discovered a malicious npm package that masquerades as an [OpenClaw](https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html) installer to deploy a remote access trojan (RAT) and steal sensitive data from compromised hosts.

The package, named "[@openclaw-ai/openclawai](https://www.npmjs.com/package/%40openclaw-ai/openclawai)," was uploaded to the registry by a user named "openclaw-ai" on March 3, 2026. It has been downloaded 178 times to date. The library is still available for download as of writing.

JFrog, which discovered the package, said it's designed to steal system credentials, browser data, crypto wallets, SSH keys, Apple Keychain databases, and iMessage history, as well as install a persistent RAT with remote access capabilities, SOCKS5 proxy, and live browser session cloning.

"The attack is notable for its broad data collection, its use of social engineering to harvest the victim's system password, and the sophistication of its persistence and C2 [command-and-control] infrastructure," security researcher Meitar Palas [said](https://research.jfrog.com/post/ghostclaw-unmasked/). "Internally, the malware identifies itself as GhostLoader."

The malicious logic is triggered by means of a postinstall hook, which [re-installs the package globally](https://docs.npmjs.com/downloading-and-installing-packages-globally) using the command: "npm i -g @openclaw-ai/openclawai." Once the installation is complete, the OpenClaw binary points to "scripts/setup.js" by means of the "bin" property in the "package.json" file.

It's worth noting that the "[bin](https://docs.npmjs.com/cli/v11/configuring-npm/package-json#bin)" field is used to define executable files that should be added to the user's PATH during package installation. This, in turn, turns the package into a globally accessible command-line tool.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The file "setup.js" serves as the first-stage dropper that, upon running, displays a convincing fake command-line interface with animated progress bars to give the impression that OpenClaw is being installed on the host. After the purported installation step is complete, the script shows a bogus iCloud Keychain authorization prompt, asking users to enter their system password.

Simultaneously, the script retrieves an encrypted second-stage JavaScript payload from the C2 server ("trackpipe[.]dev"), which is then decoded, written to a temporary file, and spawned as a detached child process to continue running in the background. The temp file is deleted after 60 seconds to cover up traces of the activity.

"If the Safari directory is inaccessible (no Full Disk Access), the script displays an AppleScript dialog urging the user to grant FDA to Terminal, complete with step-by-step instructions and a button that opens System Preferences directly," JFrog explained. "This enables the second-stage payload to steal Apple Notes, iMessage, Safari history, and Mail data."

The JavaScript second-stage, featuring about 11,700 lines, is a full-fledged information stealer and RAT framework that's capable of persistence, data collection, browser decryption, C2 communication, a SOCKS5 proxy, and live browser cloning. It's also equipped to steal a wide range of data -

* macOS Keychain, including both the local login.keychain-db and all iCloud Keychain databases
* Credentials, cookies, credit cards, and autofill data from all Chromium-based browsers, such as Google Chrome, Microsoft Edge, Brave, Vivaldi, Opera, Yandex, and Comet
* Data from desktop wallet applications and browser extensions
* Cryptocurrency wallet seed phrases
* SSH keys
* Developer and cloud credentials for AWS, Microsoft Azure, Google Cloud, Kubernetes, Docker, and GitHub
* Artificial intelligence (AI) agent configurations, and
* Data protected by the FDA, including Apple Notes, iMessage history, Safari browsing history, Mail account configurations, and Apple account information

In the final stage, the collected data is compressed into a tar.gz archive and exfiltrated through multiple channels, including directly to the C2 server, Telegram Bot API, and GoFile.io.

What's more, the malware enters a persistent daemon mode that allows it to monitor clipboard content every three seconds and transmit any data that matches one of the nine pre-defined patterns corresponding to private keys, [WIF key](https://learnmeabitcoin.com/technical/keys/private-key/wif/), SOL private key, RSA private key, BTC address, Ethereum address, AWS key, OpenAI key, and Strike key.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

Other features include keeping tabs on running processes, scanning incoming iMessage chats in real-time, and executing commands sent from the C2 server to run arbitrary shell command, open a URL on the victim's default browser, download additional payloads, upload files, start/stop a SOCKS5 proxy, list available browsers, clone a browser profile and launch it in headless mode, stop the browser clone, self-destruct, and update itself.

The browser cloning function is particularly dangerous as it launches a headless Chromium instance with the existing browser profile that contains cookies, login, and history data. This gives the attacker a fully authenticated browser session without the need for accessing credentials.

"The @openclaw...