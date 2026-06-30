---
title: Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer
url: https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html
source: The Hacker News
date: 2026-06-29
fetch_date: 2026-06-30T06:10:14.255861
---

# Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer

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

# [Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer](https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html)

**Ravie Lakshmanan**Jun 29, 2026Supply Chain Attack / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBjmO4haWCgXfALMAtSHKJXRWIlLfYqulkKflfK-3BSYON-8A4MjUNoZRxOyaLGc-4Bsj1eIfGDhdpJuKZrJORz4HZHx5iM7lj0-VlehqqZ6kaq5_ZWP08MviAchtNF1XORD_Fps-IWderGKNM18TT-Jgh_0LRFULqdMeOfv_FKDd8oWmHmv-iR1-_7XZP/s1700-e365/gogo.jpg)

Cybersecurity researchers have uncovered two hijacked npm packages and a cluster of Go packages that are designed to deploy a Python-based information stealer on compromised Windows, Linux, and macOS hosts.

"This attack avoids the most common npm execution paths through lifecycle scripts, perhaps in an attempt to remain 'compatible' with [npm v12's security hardenings](https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html)," JFrog [said](https://research.jfrog.com/post/hijacked-npm-vscode-tasks-blockchain/) in a technical analysis.

"The package hides execution inside a VS Code task, configured to run automatically when the project folder is opened in VS Code. From there, the malware retrieves encrypted JavaScript from blockchain transaction data, connects to attacker-controlled infrastructure, launches a socket.io backdoor, and eventually deploys a Python infostealer.

The names of the identified npm packages are listed below -

* html-to-gutenberg
* fetch-page-assets (which lists html-to-gutenberg as a dependency)

The two packages were uploaded to npm on May 25, 2026, and are no longer available for download from the registry. The starting point of the attack is a hidden Microsoft Visual Studio Code (VS Code) task named "eslint-check" that's configured with the "runOn: 'folderOpen'" option to trigger the execution of arbitrary code when the folder is opened as a workspace folder in an IDE like VS Code or Cursor.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"They do not recursively execute every nested .vscode/tasks.json; in this case, the trigger fires when the malicious package directory itself is opened as the workspace and marked as trusted, or that the developer explicitly allowed automatic tasks," JFrog said. "The command also disguises the payload as a font file - public/fonts/fa-solid-400.woff2, even though the file just contains JavaScript code."

It's worth noting that the [abuse of a VS Code auto-run task](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html), coupled with the [disguise of JavaScript malware](https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html) as font files, has been attributed to North Korea. The OpenSourceMalware team, which is tracking the activity under the moniker Fake Font, has described it as a variant of [Contagious Interview](https://dti.domaintools.com/securitysnacks/dprk-contagious-interview-developer-workflow-compromise), a long-running campaign targeting software developers and technical personnel through fraudulent job interview processes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgd6MExRbjbh93JrXI991seXurjb3kMrMNfQ1Xa7vqS8mgQyQPF_oXFelcK02N4abo9shDJ4WBQYcG7sSYZNmIsrYtLYjOirnDBY50vfm_t3xOo8gxH6FEZJkc2kfiGcjYpLzSnHdyKW0aJ0GGs4oG-Tu20t4WgLemQ6PnvCPjTcfTYzp4M_p8bE9ic-Q-E/s1700-e365/go.png)

"This 'Fake Font' campaign delivers a multi-stage loader that ultimately deploys the InvisibleFerret Python backdoor, designed to steal cryptocurrency wallets, browser credentials, and establish persistent access," security researcher Paul McCarty [noted](https://opensourcemalware.com/blog/dprk-contagious-interview-campaign-fake-font-uses-malicious-vs-code-fonts) back in January. "This is the third sub-campaign of the Contagious Interview' campaign that has been ongoing since 2023."

The bogus font file uses blockchain infrastructure as a dead drop resolver, relying on TronGrid and Aptos as a fallback mechanism to fetch a next-stage JavaScript payload in a manner that's resilient to takedown efforts. The JavaScript stage repeats the same dead drop retrieval pattern to configure a command-and-control (C2) server that enables file uploads and Python malware delivery.

This includes setting up a Socket.io backdoor that grants the operator remote control over the infected host through features like shell execution, clipboard harvesting, file system operations, file upload, process management, and arbitrary JavaScript execution.

In parallel, the infection chain launches a Python loader component that's responsible for retrieving the Python infostealer from the C2 server and installing the necessary dependencies. The artifact is a wide-ranging credential, browser, wallet, and developer artifact stealer that can siphon data stored in Chromium-based and Mozilla Firefox browsers, password managers, authenticators, and cryptocurrency wallets.

It's also equipped to harvest developer-oriented information like Git credentials, GitHub CLI hosts.yml, GitHub Desktop logs, VS Code, and global storage, as well as data from Windows Credential Manager, Linux Secret Service, KDE Wallet, macOS Keychain, and cloud storage metadata for Dropbox, Google Drive, Microsoft OneDrive, Apple iCloud, Box, Mega, and pCloud.

In the final stage, the collected data is packaged into compressed ZIP archives and uploaded to the C2 server, and to a Telegram bot if a bot token is provided by the attacker during runtime.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The campaign has also targeted the Go ecosystem, with Nextron Systems [discovering](https://x.com/nextronresearch/status/2069802303817679083) a set of 16 Go packages containing the same malware. The list is as follows -

* github.com/lambda-platform/lambda
* github.com/reauheau/goaubio
* github.com/glacialspring/go-winsparkle...