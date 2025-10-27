---
title: Malicious Pull Request Targets 6,000+ Developers via Vulnerable Ethcode VS Code Extension
url: https://thehackernews.com/2025/07/malicious-pull-request-infects-6000.html
source: The Hacker News
date: 2025-07-09
fetch_date: 2025-10-07T00:03:32.328546
---

# Malicious Pull Request Targets 6,000+ Developers via Vulnerable Ethcode VS Code Extension

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

# [Malicious Pull Request Targets 6,000+ Developers via Vulnerable Ethcode VS Code Extension](https://thehackernews.com/2025/07/malicious-pull-request-infects-6000.html)

**Jul 08, 2025**Ravie Lakshmanan

[![Vulnerable Ethcode VS Code Extension](data:image/png;base64... "Vulnerable Ethcode VS Code Extension")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJvbqFYqi0KOuviC3wF4Xkx80Kt68smB8BmDm47eRJ1w9ZN5_AWqG0xux_DVEEff2Nppc-Am-r8HFXXryo9Z4jp0Z1yYqI3a7NP1CdOzbs2Gm1DXBZWuGH4YC2LUQPxjvM0aF4ssx4RMWyBAvch14TdFRaPeBoUeZ5l0TYfsPMuHGxfw6xJGqDUUeHymTm/s790-rw-e365/ethcode.jpg)

Cybersecurity researchers have flagged a supply chain attack targeting a Microsoft Visual Studio Code (VS Code) extension called **Ethcode** that has been installed a little over 6,000 times.

The compromise, per [ReversingLabs](https://www.reversinglabs.com/blog/malicious-pull-request-infects-vscode-extension), occurred via a GitHub pull request that was opened by a user named Airez299 on June 17, 2025.

First released by 7finney in 2022, [Ethcode](https://marketplace.visualstudio.com/items?itemName=7finney.ethcode) is a VS Code extension that's used to deploy and execute solidity smart contracts in Ethereum Virtual Machine ([EVM](https://www.coinbase.com/en-in/learn/crypto-glossary/what-is-the-ethereum-virtual-machine))-based blockchains. An EVM is a decentralized computation engine that's designed to run smart contracts on the Ethereum network.

According to the supply chain security company, the GitHub project received its last non-malicious update on September 6, 2024. That changed last month when Airez299 [opened a pull request](https://github.com/7finney/ethcode/commit/a0e83c3e34e4d9bae02936008dd7fed6009d58a8) with the message "Modernize codebase with viem integration and testing framework."

The user claimed to have added a new testing framework with Mocha integration and contract testing features, as well as made a number of changes, including removing old configurations and updating the dependencies to the latest version.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While that may seem like a useful update for a project that lay dormant for over nine months, ReversingLabs said the unknown threat actor behind the attack managed to sneak in two lines of code as part of 43 commits and roughly 4,000 lines of changed code that compromised the entire extension.

This included the addition of an npm dependency in the form of "[keythereum-utils](https://www.npmjs.com/package/keythereum-utils)" in the project's "package.json" file and importing it in the TypeScript file linked to the VS Code extension ("src/extension.ts").

The JavaScript library, now taken down from the npm registry, has been found to be heavily obfuscated and contains code to download an unknown second-stage payload. The package has been [downloaded](https://npm-stat.com/charts.html?package=keythereum-utils) 495 times.

Multiple versions of "keythereum-utils" were uploaded to npm by users named 0xlab (version 1.2.1), 0xlabss (versions 1.2.2, 1.2.3, 1.2.4, 1.2.5, and 1.2.6), and 1xlab (version 1.2.7) between June 17 and 21, 2025. The npm accounts no longer exist.

"After deobfuscating the keythereum-utils code, it became easy to see what the script does: spawn a hidden PowerShell that downloads and runs a batch script from a public file-hosting service," security researcher Petar Kirhmajer said.

While the exact nature of the payload is not known, it's believed to be a piece of malware that's either capable of stealing cryptocurrency assets or poisoning the contracts that are being developed by users of the extension.

Following responsible disclosure to Microsoft, the extension was removed from the VS Code Extensions Marketplace. After the removal of the malicious dependency, the extension has since been reinstated.

"Ethcode package has been unpublished by Microsoft," 0mkara, a project maintainer for the tool, [said](https://github.com/7finney/ethcode/pull/324) in a pull request submitted on June 28. "They detected a malicious dependency in Ethcode. This PR removes potential malicious repository keythereum from the package."

Ethcode is the latest example of a broader and escalating trend of software supply chain attacks, where attackers weaponize public repositories like PyPI and npm to deliver malware directly into developer environments.

"The GitHub account Airez299 that initiated the Ethcode pull request was created on the same day as the PR request was opened," ReversingLabs said. "Accordingly, the Airez299 account does not have any previous history or activity associated with it. This strongly indicates that this is a throwaway account that was created solely for the purpose of infecting this repo — a goal in which they were successful."

According to data compiled by Sonatype, 16,279 pieces of open-source malware have been discovered in the second quarter of 2025, a 188% jump year-over-year. In comparison, [17,954 pieces of open-source malware](https://www.sonatype.com/blog/open-source-malware-index-q1-2025) were uncovered in Q1 2025.

Of these, more than 4,400 malicious packages were engineered to harvest and exfiltrate sensitive information, such as credentials, and API tokens.

"Malware targeting data corruption doubled in frequency, making up 3% of total malicious packages — more than 400 unique instances," Sonatype [said](https://www.sonatype.com/blog/open-source-malware-index-q2-2025). "These packages aim to damage files, inject malicious code, or otherwise sabotage applications and infrastructure."

The North Korea-linked Lazarus Group has been attributed to 107 malicious packages, which were collectively downloaded over 30,000 times. Another set of more than 90 npm packages has been associated with a Chinese threat cluster dubbed [Yeshen-Asia](https://www.getsafety.com/blog-posts/yeshen-asia-threat-campaign) that has been active since at least December 2024 to harvest system information and the list of running ...