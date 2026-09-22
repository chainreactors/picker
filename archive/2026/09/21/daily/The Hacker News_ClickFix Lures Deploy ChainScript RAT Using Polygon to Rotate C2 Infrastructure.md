---
title: ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure
url: https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html
source: The Hacker News
date: 2026-09-21
fetch_date: 2026-09-22T07:05:19.990284
---

# ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [ClickFix Lures Deploy ChainScript RAT Using Polygon to Rotate C2 Infrastructure](https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html)

**Ravie Lakshmanan**Sep 21, 2026Malware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-cgmwQRZh142Z19A3s7K7tpaXtsyy6Imy9cYGM7nFP1DAZoSK9gDw8T0dGXlkFWOGDFShJWMNjC7jbwoSvLokr1pX27u2B1SABpBL-aWtaXj2hYYrqVwTE7LpEDn_iIbRYCro8sH2hzAEsjHLGkpFqTjEKlFHi2o2pgacFJQvYkPDCKVEhkJgW8OWhpZA/s1700-nu-rw-lo-l85-e365/poly.jpg)

Threat actors are leveraging [ClickFix-like lures](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html) to deliver a previously undocumented remote access trojan (RAT) called **ChainScript**.

"ChainScript has appeared under multiple build names, including ComponentTask33, UpdateDigital, HostShared, and OrchidViolet66, while presenting itself as Spotify, Zoom Workplace, and Microsoft Teams software," Blackpoint Adversary Pursuit Group (APG) researchers Sam Decker, Andi Ursry, and Nevan Beal [said](https://blackpointcyber.com/blog/chainscript-tracing-a-nodejs-rat-across-the-blockchain/).

Like many malware families observed in recent months, ChainScript employs an [EtherHiding](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html)-style command-and-control (C2) discovery technique that makes use of a Polygon smart contract to locate its active WebSocket infrastructure.

ChainScript is a full-featured RAT that provides extensive remote access to the operator, including interactive CMD and PowerShell, file operations, screenshot capture, payload deployment, cryptocurrency wallet enumeration (both desktop apps and browser extensions), and remote JavaScript execution.

The starting point of the attack chain is a ClickFix lure that leads to the download and execution of a malicious Windows installer using "msiexec.exe." The installer ("ComponentTask33-4d14e6ac.msi"), disguised as Spotify, deploys the Node.js runtime and launches the ChainScript JavaScript agent through hidden PowerShell and VBScript stages.

The PowerShell script drops various components, namely, the runtime, agent source, configuration, and other auxiliary binaries, across different Microsoft-looking paths in the "%LOCALAPPDATA%" folder. The VBScript serves as the main launcher for ChainScript.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The running agent then establishes user level persistence through a scheduled task with a Registry Run key fallback. Upon execution, ChainScript connects to the C2 server over WebSockets and retrieves additional tasking, giving the threat actor direct control over the compromised system. The supported commands also allow it to self-update and remove persistence.

The findings illustrate how threat actors are increasingly adopting a flexible decentralized infrastructure as a way to resist takedown efforts and ensure uninterrupted operations.

"ChainScript reflects an emerging pattern of malware using development frameworks and blockchain-based C2 discovery to enable infrastructure rotation and complicate traditional indicator-based detection," Blackpoint said. "By separating backend discovery from the malware itself and using the Polygon contract as an external resolver, the operator can redirect infected hosts to new infrastructure while retaining the same implant and reconnect workflow."

### ClickFix, a Way for Mac and Windows Users to Infect Themselves

The disclosure comes as threat actors [compromised](https://www.reddit.com/r/cybersecurity/comments/1w8gu91/reddit_infostealer_adverts/) HBO Max's official Reddit account ("u/hbomax") and abused it to push malicious ads that launched ClickFix attacks to infect Windows and macOS devices with information-stealing malware. The activity has been codenamed PasteSwitch by [Hudson Rock](https://www.hudsonrock.com/blog/hbo-max-ads-on-a-compromised-reddit-account-exposed-a-massive-pasteswitch-clickfix-operation) and [ADAMnetworks](https://adamnet.works/blog/hbo-max-ads-exposed-the-pasteswitch-clickfix-operation/). It's not known how the account was breached, and how many people clicked on these fake ads and how many were compromised as a result.

On macOS, PasteSwitch has been found to deliver MacSync, Atomic macOS Stealer (AMOS), and fake cryptocurrency wallet applications designed to steal recovery phrases. The Windows branch, on the other hand, distributes Amatera Stealer and cryptocurrency clippers like AnimateClipper and ZigClipper. In all, the verified Reddit account served 108 malicious ads over a 48-hour period in mid-September 2026.

According to data shared by Seqrite Labs, MacSync infections have concentrated in the U.S., followed by the U.K., Germany, Japan, Canada, France, Singapore, Australia, India, and the Netherlands. "MacSync campaigns primarily target regions with widespread macOS enterprise use, tech and software development sectors, and active cryptocurrency or Web3 communities," researcher Chandra Kant Bauri [said](https://www.seqrite.com/blog/macsync-the-evasive-macos-stealer-exploiting-clickfix-lures/).

"The threat actors utilized highly polished assets to establish trust before delivering the malicious payload," Hudson Rock said. "By hijacking a verified corporate account, they bypassed the initial skepticism many users apply to internet advertisements."

The findings dovetail with another ClickFix campaign that employs a fake Codex download experience surfaced via search results to lead users to bogus Google Sites pages and trick macOS users into pasting a malicious command into Terminal, resulting in the execution of Atomic Stealer. Visitors using non-Mac devices are served a harmless decoy page.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

"The copied Terminal command first retrieves a shell-script loader: the first stage," Cato Networks [said](htt...