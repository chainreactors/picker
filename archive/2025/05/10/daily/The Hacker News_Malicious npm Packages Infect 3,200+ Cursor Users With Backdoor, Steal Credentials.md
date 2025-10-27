---
title: Malicious npm Packages Infect 3,200+ Cursor Users With Backdoor, Steal Credentials
url: https://thehackernews.com/2025/05/malicious-npm-packages-infect-3200.html
source: The Hacker News
date: 2025-05-10
fetch_date: 2025-10-06T22:31:43.515600
---

# Malicious npm Packages Infect 3,200+ Cursor Users With Backdoor, Steal Credentials

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Malicious npm Packages Infect 3,200+ Cursor Users With Backdoor, Steal Credentials](https://thehackernews.com/2025/05/malicious-npm-packages-infect-3200.html)

**May 09, 2025**Ravie LakshmananSupply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWmiupd-RsoTl5hFdOnLUSuz534IbJW4ngcGa-jLZHJMK2TPpRDMhgnIeI8ixc4FWh0UMGJRNc21ePgmDE6yKGxtrXFOS28j5DRKuwed9ScDfttmi39mKVSGq2IXmK_LnbhzN6Px13IYF1YlxZ6PHNKQ3l0JdM-PrnYHncv9hibabTBUnmQtLmbQjJ_WrE/s790-rw-e365/npm-code.jpg)

Cybersecurity researchers have flagged three malicious npm packages that are designed to target the Apple macOS version of Cursor, a popular artificial intelligence (AI)-powered source code editor.

"Disguised as developer tools offering 'the cheapest Cursor API,' these packages steal user credentials, fetch an encrypted payload from threat actor-controlled infrastructure, overwrite Cursor's main.js file, and disable auto-updates to maintain persistence," Socket researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-npm-packages-hijack-cursor-editor-on-macos).

The packages in question are listed below -

* [sw-cur](https://www.npmjs.com/package/sw-cur) (2,771 downloads)
* [sw-cur1](https://www.npmjs.com/package/sw-cur1) (307 downloads), and
* [aiide-cur](https://www.npmjs.com/package/aiide-cur) (163 downloads)

All three packages continue to be available for download from the npm registry. "Aiide-cur" was first published on February 14, 2025. It was uploaded by a user named "aiide." The npm library is described as a "command-line tool for configuring the macOS version of the Cursor editor."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The other two packages, per the software supply chain security firm, were published a day earlier by a threat actor under the alias "gtr2018." In total, the three packages have been downloaded over 3,200 times to date.

The libraries, once installed, are designed to harvest user-supplied Cursor credentials and fetch a next-stage payload from a remote server ("t.sw2031[.]com" or "api.aiide[.]xyz"), which is then used to replace a legitimate Cursor-specific code with malicious logic.

"Sw-cur" also takes the step of disabling Cursor's auto-update mechanism and terminating all Cursor processes. The npm packages then proceed to restart the application so that the patched code takes effect, granting the threat actor to execute arbitrary code within the context of the platform.

The findings point to an emerging trend where threat actors are using rogue npm packages as a way to introduce malicious modifications to other legitimate libraries or software already installed on developer systems.

This is significant not least because it adds a new layer of sophistication by allowing the malware to persist even after the nefarious libraries have been removed, requiring developers to perform a clean install of the altered software again.

"Patch‑based compromise is a new and a powerful addition to the threat actor arsenal targeting open-source supply chains: Instead (or in addition) of slipping malware into a package manager, attackers publish a seemingly harmless npm package that rewrites code already trusted on the victim's machine," Socket told The Hacker News.

"By operating inside a legitimate parent process -- an IDE or shared library -- the malicious logic inherits the application's trust, maintains persistence even after the offending package is removed, and automatically gains whatever privileges that software holds, from API tokens and signing keys to outbound network access."

"This campaign highlights a growing supply chain threat, with threat actors increasingly using [malicious patches](https://thehackernews.com/2025/04/malicious-npm-package-targets-atomic.html) to compromise trusted local software," Boychenko said.

The selling point here is that the attackers are attempting to exploit developers' interest in AI as well as those who are looking for cheaper usage fees for access to AI models.

"The threat actor's use of the tagline 'the cheapest Cursor API' likely targets this group, luring users with the promise of discounted access while quietly deploying a backdoor," the researcher added.

To counter such novel supply chain threats, defenders are required to flag packages that run postinstall scripts, modify files outside node\_modules, or initiate unexpected network calls, and combining those indicators with rigorous version pinning, real‑time dependency scanning, and file‑integrity monitoring on critical dependencies.

The disclosure comes as Socket uncovered two other npm packages – pumptoolforvolumeandcomment and debugdogs – to deliver an obfuscated payload that siphons cryptocurrency keys, wallet files, and trading data related to a cryptocurrency platform named BullX on and macOS systems. The captured data is exfiltrated to a Telegram bot.

While "pumptoolforvolumeandcomment" has been downloaded 625 times, "debugdogs" have received a total of 119 downloads since they were both published to npm in September 2024 by a user named "olumideyo."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Debugdogs simply invokes pumptoolforvolumeandcomment, making it a convenient secondary infection payload," security researcher Kush Pandya [said](https://socket.dev/blog/malicious-npm-packages-use-telegram-to-exfiltrate-bullx-credentials). "This 'wrapper' pattern doubles down on the main attack, making it easier to spread under multiple names without changing the core malicious code."

"This highly targeted attack can empty wallets and expose sensitive credentials and trading data in seconds."

### Npm Package "rand-user-agent" Compromised in Supply Chain Attack

The discovery also follows a [report](https://www.aikido.dev/blog/catching-a-rat-remote-access-trojian-rand-user-agent-supply-chain-compromise) from Aikido about a supply chain attack that has compromised a ...