---
title: Ghost Campaign Uses 7 npm Packages to Steal Crypto Wallets and Credentials
url: https://thehackernews.com/2026/03/ghost-campaign-uses-7-npm-packages-to.html
source: The Hacker News
date: 2026-03-24
fetch_date: 2026-03-25T04:18:09.231477
---

# Ghost Campaign Uses 7 npm Packages to Steal Crypto Wallets and Credentials

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

# [Ghost Campaign Uses 7 npm Packages to Steal Crypto Wallets and Credentials](https://thehackernews.com/2026/03/ghost-campaign-uses-7-npm-packages-to.html)

**Ravie Lakshmanan**Mar 24, 2026Cryptocurrency / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlh6CuYJhvsInqih03x9cvHFvmbF-F8DFJF_Y9VQMslT9g5yp_jhDewDUjcvUlAMzyKbfOHz0eMdFqHdIGwbtOY0MOHDGr_lA1TraO34SwYiKrieNnOQsAo5DbKhpJCp2X60_0epyBiBDs-KRgFjhR0QEPMmTRBCvJCiiQaJg7MaRCLf3EHcrIdluUrmJ-/s1700-e365/1000062391.jpg)

Cybersecurity researchers have uncovered a new set of malicious npm packages that are designed to steal cryptocurrency wallets and sensitive data.

The activity is being tracked by ReversingLabs as the **Ghost** campaign. The list of identified packages, all published by a user named mikilanjillo, is below -

* react-performance-suite
* react-state-optimizer-core
* react-fast-utilsa
* ai-fast-auto-trader
* pkgnewfefame1
* carbon-mac-copy-cloner
* coinbase-desktop-sdk

"The packages themselves are phishing for sudo password with which the last stage is executed, and are trying to hide their real functionality and avoid detection in a sophisticated way: displaying fake npm install logs," Lucija Valentić, software threat researcher at ReversingLabs, [said](https://www.reversinglabs.com/blog/npm-fake-install-logs-rat) in a report shared with The Hacker News.

The identified Node.js libraries, besides falsely claiming to download additional packages, insert random delays to give the impression that the installation process is underway. At one point during this step, the user is alerted that the installation is running into an error due to missing write permissions to "/usr/local/lib/node\_modules," which is the default location for globally installed Node.js packages on Linux and macOS systems.

It also instructs the victim to enter their root or administrator password to continue with the installation. Should they enter the password, the malware then silently retrieves the next-stage downloader, which then reaches out to a Telegram channel to fetch the URL for the final payload and the key required to decrypt it.

The attack culminates with the deployment of a remote access trojan that's capable of harvesting data, targeting cryptocurrency wallets, and awaiting further instructions from an external server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

ReversingLabs said the activity shares overlaps with an activity cluster documented by JFrog under the name [GhostClaw](https://thehackernews.com/2026/03/malicious-npm-package-posing-as.html) earlier this month, although it's currently not known if it's the work of the same threat actor or an entirely new campaign.

### GhostClaw Uses GitHub Repositories and AI Workflows to Deliver macOS Stealer

Jamf Threat Labs, in an analysis published last week, said the GhostClaw campaign uses GitHub repositories and artificial intelligence (AI)-assisted development workflows to deliver credential-stealing payloads on macOS.

"These repositories impersonate legitimate tools, including trading bots, SDKs and developer utilities, and are designed to appear credible at a glance," security researcher Thijs Xhaflaire [said](https://www.jamf.com/blog/ghostclaw-ghostloader-malware-github-repositories-ai-workflows/). "Several of the identified repositories have accumulated significant engagement, in some cases exceeding hundreds of stars, further reinforcing their perceived legitimacy."

In this campaign, the repositories are initially populated with benign or partially functional code and left unchanged for an extended period of time to build trust among users before introducing malicious components. Specifically, the repositories feature a README file that guides developers to execute a shell script as part of the installation step.

A variant of these repositories feature a SKILL.md file, primarily targeting Al-oriented workflows under the guise of installing external skills through AI agents like OpenClaw. Regardless of the method used, the shell script initiates a multi-stage infection process that ends with the deployment of a stealer. The entire sequence of actions is as follows -

* It identifies the host architecture and macOS version, checks if Node.js is already present, and installs a compatible version if required. The installation takes place in a user-controlled directory to avoid raising any red flags.
* It invokes "node scripts/setup.js" and "node scripts/postinstall.js," causing the execution to transition to JavaScript payloads, enabling it steal system credentials, deliver the GhostLoader malware by contacting a command-and-control (C2) server, and remove traces of malicious activity by clearing the Terminal.

The script also comes with an environment variable named "GHOST\_PASSWORD\_ONLY," which, when set to zero, presents a full interactive installation flow, complete with progress indicators and user prompts. If it's set to 1, the script launches a simplified execution path focused primarily on credential collection without any extra user interface elements.

Interestingly, in at least some cases, the "postinstall.js" script displays a benign success message, stating the installation was successful and that users can configure the library in their projects by running the "npx react-state-optimizer" command.

According to a [report](https://panther.com/blog/phantom-menace-the-ghost-loader-infostealer-campaign) from cloud security company Panther last month, "react-state-optimizer" is one of several other npm packages published by "mikilanjillo," indicating that the two clusters of activity are one and the same -

* react-query-core-utils
* react-state-optimizer
* react-fast-utils
* react-performance-suite
* ai-fast-auto-trader
* carbon-mac-copy-cloner
* carbon-mac-copys-cloner
* pkgnewfefame
* darkslash

[![Cybersecurity](data:image/png;base64...)](https://theh...