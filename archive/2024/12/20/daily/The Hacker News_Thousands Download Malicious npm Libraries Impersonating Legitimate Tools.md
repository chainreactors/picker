---
title: Thousands Download Malicious npm Libraries Impersonating Legitimate Tools
url: https://thehackernews.com/2024/12/thousands-download-malicious-npm.html
source: The Hacker News
date: 2024-12-20
fetch_date: 2025-10-06T19:58:30.689033
---

# Thousands Download Malicious npm Libraries Impersonating Legitimate Tools

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

# [Thousands Download Malicious npm Libraries Impersonating Legitimate Tools](https://thehackernews.com/2024/12/thousands-download-malicious-npm.html)

**Dec 19, 2024**Ravie LakshmananSupply Chain / Software Security

[![Malicious npm Libraries](data:image/png;base64... "Malicious npm Libraries")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjl_AszE3pXQcN5IuqH8Hb3rt_tQkJgjVr7F3SnMmDIm7I0Sn2OEZh9rFLyg0_OGCIo4ooNLuCImn8FxXgx9lcREIaH3INHQQ4bRUcvredJNa15yMzMTQedhKSz8osRSEsd55atYTfmsuKJeKbFUwFq0sLQeW7hKkIQ8er_F18gRvHFYZDu_z4cpqZAsJ1V/s790-rw-e365/npm.png)

Threat actors have been observed uploading malicious typosquats of legitimate npm packages such as typescript-eslint and @types/node that have racked up thousands of downloads on the package registry.

The counterfeit versions, named [@typescript\_eslinter/eslint](https://npm-stat.com/charts.html?package=@typescript_eslinter/eslint) and [types-node](https://npm-stat.com/charts.html?package=types-node), are engineered to download a trojan and retrieve second-stage payloads, respectively.

"While typosquatting attacks are hardly new, the effort spent by nefarious actors on these two libraries to pass them off as legitimate is noteworthy," Sonatype's Ax Sharma [said](https://www.sonatype.com/blog/counterfeit-eslint-and-node-types-libraries-downloaded-thousands-of-times-abuse-pastebin) in an analysis published Wednesday.

"Furthermore, the high download counts for packages like "types-node" are signs that point to both some developers possibly falling for these typosquats, and threat actors artificially inflating these counts to boost the trustworthiness of their malicious components."

The npm listing for @typescript\_eslinter/eslint, Sonatype's analysis revealed, points to a phony GitHub repository that was set up by an account named "[typescript-eslinter](https://github.com/typescript-eslinter)," which was created on November 29, 2024. Present within this package is a file named "[prettier.bat](https://github.com/typescript-eslinter/eslint/tree/main/tools)."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Another package linked to the same npm/GitHub account is named @typescript\_eslinter/prettier. It impersonates a [well-known code formatter tool](https://blog.logrocket.com/linting-typescript-eslint-prettier/) of the same name, but, in reality, is configured to install the fake @typescript\_eslinter/eslint library.

The malicious library contains code to drop "prettier.bat" into a temporary directory and add it to the Windows Startup folder so that it's automatically run every time the machine is rebooted.

"Far from being a 'batch' file though, the "prettier.bat" file is actually a Windows executable (.exe) that has previously been flagged as a trojan and dropper on [VirusTotal](https://www.virustotal.com/gui/file/ab3e8378aa31584160898d97d1ecfead2a63cd977efacec98df375fefdda3016)," Sharma said.

On the other hand, the second package, types-node, incorporates instructions to reach out to a Pastebin URL and fetch scripts that are responsible for running a malicious executable that's deceptively named "[npm.exe](https://www.virustotal.com/gui/file/7f9bd9406bac62b0bce01d4aff4068aa1b5b7396b0c7c34d76057b2e27cfb555)."

"The case highlights a pressing need for improved supply chain security measures and greater vigilance in monitoring third-party software registry developers," Sharma said.

The development comes as ReversingLabs identified several malicious extensions that were initially detected in the Visual Studio Code (VSCode) Marketplace in October 2024, a month after which one additional package emerged in the npm registry. The package [attracted](https://npm-stat.com/charts.html?package=etherscancontracthandler) a total of 399 downloads.

The list of rogue VSCode extensions, now removed from the store, is below -

* EVM.Blockchain-Toolkit
* VoiceMod.VoiceMod
* ZoomVideoCommunications.Zoom
* ZoomINC.Zoom-Workplace
* Ethereum.SoliditySupport
* ZoomWorkspace.Zoom
* ethereumorg.Solidity-Language-for-Ethereum
* VitalikButerin.Solidity-Ethereum
* SolidityFoundation.Solidity-Ethereum
* EthereumFoundation.Solidity-Language-for-Ethereum
* SOLIDITY.Solidity-Language
* GavinWood.SolidityLang
* EthereumFoundation.Solidity-for-Ethereum-Language

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The campaign started with targeting of the crypto community, but by the end of October, extensions published were mostly impersonating the Zoom application," ReversingLabs researcher Lucija Valentić [said](https://www.reversinglabs.com/blog/a-new-playground-malicious-campaigns-proliferate-from-vscode-to-npm). "And each malicious extension published was more sophisticated than the last."

All the extensions as well as the npm package have been found to include obfuscated JavaScript code, acting as a downloader for a second-stage payload from a remote server. The exact nature of the payload is currently not known.

The findings once again emphasize the need for exercising caution when it comes to downloading tools and libraries from open-source systems and avoid introducing malicious code as a dependency in a larger project.

"The possibility of installing plugins and extending functionality of IDEs makes them very attractive targets for malicious actors," Valentić said. "VSCode extensions are often overlooked as a security risk when installing in an IDE, but the compromise of an IDE can be a landing point for further compromise of the development cycle in the enterprise."

### Update

Cybersecurity company Hunt.io, in a follow-up report published on January 21, 2025, said it discovered a new VSCode extension impersonating Zoom ("zoom-communications.Zoom") that's designed to access and steal cookies stored in Google Chrome's SQLite database.

"This incident underscores an ongoing threat where malicious actors exploit trusted infrastructure, like Microsoft's CDN, to distribute malware through seemingly...