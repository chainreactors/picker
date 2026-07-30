---
title: Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js
url: https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:45.639827
---

# Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js

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

# [Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js](https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html)

**Ravie Lakshmanan**Jul 29, 2026Malware / Developer Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbnnos_l5g9tfmBH7efqHHPJs-C6Ti9zjG9iifZXs0QLLoUn7L1BwkunpqbD55rRvqSiJx0R_DTAl12TBnL9MN0DkDtzhwnm8Xgbsbu8LZuKyRDnVtq3cbeMlEmNJEmZgXy3BeOILj2kM24GojxXfDJDr93XsEiORhP9q1sYo814jzq4UsQCS0RRZmhp5k/s1700-e365/npm-hack.jpg)

Beta release versions of two npm packages in the @joyfill namespace have been compromised to deliver a remote access trojan (RAT) associated with the **[DEV#POPPER](https://thehackernews.com/2026/04/285-million-drift-hack-traced-to-six.html#social-engineering-behind-contagious-interview-and-it-worker-fraud)** malware family.

The list of affected packages is as follows -

* @joyfill/layouts@0.1.2-2773.beta.0
* @joyfill/components@4.0.0-rc24-2773-beta.4

The two packages "contain an import-time JavaScript implant that resolves encrypted code through Tron, Aptos, and BNB Smart Chain transactions," Socket [said](https://socket.dev/blog/joyfill-npm-beta-releases-compromised) in an analysis.

Unlike other malicious packages that are triggered via an npm lifecycle hook, the implant delivered as part of the JavaScript libraries runs when Node.js loads the CommonJS package entry point.

It's worth noting that the use of a multi-blockchain resolver structure comprising Tron, Aptos, and BNB Smart Chain (BSC) has been linked to a threat cluster tracked as [PolinRider](https://thehackernews.com/2026/07/north-korean-hackers-publish-108.html), which is assessed to be related to [Contagious Interview](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Earlier this month, Checkmarx and OpenSourceMalware [highlighted](https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html) a set of malicious npm packages collectively referred to as ViteVenom targeting the Vite frontend tooling ecosystem using the same tiered blockchain-based command-and-control (C2) infrastructure to deliver a RAT with reverse shell, credential harvesting, file exfiltration, and persistent backdoor injection capabilities.

The implant consists of two parallel sequences of actions -

* An in-process branch that leads to a recovered 77 KB JavaScript payload with similarities to the DEV#POPPER malware family
* A secondary branch that launches a detached Node.js process, requests a separate boot payload from 23.27.13[.]43, decrypts the response, and evaluates it

Once the package is loaded, it initiates a blockchain-based dispatch that obtains a BSC transaction hash from the latest outbound transaction of a hard-coded Tron address. If this step fails, it queries an Aptos account as a fallback to fetch the BSC transaction and, from it, decrypt and extract the JavaScript code and execute it.

Both the in-process and detached branches use a distinct set of wallet addresses, accounts, and transactions for Tron, Aptos, and BSC. The use of blockchain also means that it offers operational resilience and makes it possible to switch payloads without having to publish a new version of the packages.

The first in-process payload is a JavaScript loader that employs the blockchain resolution method to retrieve a second-stage malware named "clientCode." The detached process, on the other hand, queries the aforementioned IP address to obtain and execute JavaScript code.

"This is a redundant delivery branch, not a harmless fallback," Socket explained. "It is detached from the importing Node.js process and can continue after a build, test, or CLI command exits."

The final "clientCode" payload is heavily obfuscated and functions as a Node.js RAT with the following features, while avoiding execution on development, CI, or sandboxed machines with the hostnames github-runner, buildbot, buildkitsandbox, and microsoft-standard-WSL2 -

* Upload files to the configured upload host
* Retrieve additional JavaScript
* Collect basic host details
* Send status check-in messages
* Read clipboard data through PowerShell on Windows, pbpaste on macOS, and xclip or xsel on Linux

Two payloads have been associated with the detached process: the "clientCode" RAT and a Python infostealer that can harvest a wide range of data from compromised hosts. It's assessed to be an iteration of the OmniStealer malware, details of which were [first highlighted](https://thehackernews.com/2026/04/285-million-drift-hack-traced-to-six.html#social-engineering-behind-contagious-interview-and-it-worker-fraud) by eSentire earlier this April.

The data collected by the malware is below -

* Environment and host information
* Windows Credential Manager and Linux Secret Service data
* Chromium and Firefox browser data
* Browser extension storage for wallets and password managers
* Git credentials
* GitHub CLI configuration
* GitHub Desktop logs
* Microsoft Visual Studio Code storage

Socket told The Hacker News that both ViteVenom and the latest collection of npm packages are connected to the same ongoing operation by North Korean threat actors, rather than representing separate campaigns.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyoBGaLXGZpkSo8tDirSz-9LmmoOs31tQTlvJWBMLiWJKqMFFaiMmNLV3l-p8zXaFm1VmGG/s728-e100/sygnia-d-2.png)](https://thn.news/sygnia-webinar)

According to the application security company, both malicious versions are said to have been published by the same npm identity using Node.js 18.20.0 and npm 10.5.0, with the code present at bundle time. That said, it's currently not clear if this source code injection was achieved following a compromise of a developer workstation, source repository...