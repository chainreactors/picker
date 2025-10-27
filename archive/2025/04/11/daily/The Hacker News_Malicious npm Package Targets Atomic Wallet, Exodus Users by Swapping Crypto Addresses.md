---
title: Malicious npm Package Targets Atomic Wallet, Exodus Users by Swapping Crypto Addresses
url: https://thehackernews.com/2025/04/malicious-npm-package-targets-atomic.html
source: The Hacker News
date: 2025-04-11
fetch_date: 2025-10-06T22:07:12.724692
---

# Malicious npm Package Targets Atomic Wallet, Exodus Users by Swapping Crypto Addresses

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

# [Malicious npm Package Targets Atomic Wallet, Exodus Users by Swapping Crypto Addresses](https://thehackernews.com/2025/04/malicious-npm-package-targets-atomic.html)

**Apr 10, 2025**Ravie LakshmananMalware / Cryptocurrency

[![Swapping Crypto Addresses](data:image/png;base64... "Swapping Crypto Addresses")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkxm4irZn4wn2uLapl5_8-FQRyo8pl_K6U10po2Msz-9C0PezDr9peoGXocCDx_54W4oK7Uj1vHicxtVpY6dNbe9A8uAKCwD2_PQ6vDyJaZOG2XBtEqy-ne1hEyxkah_k2wE6ExSxFPm4HXK8FlFAmV2Ql1yKydy-Cn_5PAiI6ip-SSBMezh5UGRluISvM/s790-rw-e365/npm.jpg)

Threat actors are [continuing](https://thehackernews.com/2025/03/malicious-npm-package-modifies-local.html) to upload malicious packages to the npm registry so as to tamper with already-installed local versions of legitimate libraries and execute malicious code in what's seen as a sneakier attempt to stage a software supply chain attack.

The newly discovered package, named [pdf-to-office](https://www.npmjs.com/package/pdf-to-office), masquerades as a utility for converting PDF files to Microsoft Word documents. But, in reality, it harbors features to inject malicious code into cryptocurrency wallet software associated with Atomic Wallet and Exodus.

"Effectively, a victim who tried to send crypto funds to another crypto wallet would have the intended wallet destination address swapped out for one belonging to the malicious actor," ReversingLabs researcher Lucija Valentić [said](https://www.reversinglabs.com/blog/atomic-and-exodus-crypto-wallets-targeted-in-malicious-npm-campaign) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The npm package in question was [first published](https://secure.software/npm/packages/pdf-to-office/versions) on March 24, 2025, and has received three updates since then but not before the previous versions were likely removed by the authors themselves. The latest version, 1.1.2, was uploaded on April 8 and remains available for download. The package has been downloaded [334 times](https://npm-stat.com/charts.html?package=pdf-to-office) to date.

The disclosure comes merely weeks after the software supply chain security firm uncovered two npm packages named [ethers-provider2 and ethers-providerz](https://thehackernews.com/2025/03/malicious-npm-package-modifies-local.html) that were engineered to infect locally installed packages and establish a reverse shell to connect to the threat actor's server over SSH.

What makes this approach an attractive option for threat actors is that it allows the malware to persist on developer systems even after the malicious package is removed.

An analysis of pdf-to-office has revealed that the malicious code embedded within the package checks for the presence of the "atomic/resources/app.asar" archive inside the "AppData/Local/Programs" folder to ascertain that Atomic Wallet is installed on the Windows computer, and if so, introduce the [clipper functionality](https://thehackernews.com/2024/09/binance-warns-of-rising-clipper-malware.html).

"If the archive was present, the malicious code would overwrite one of its files with a new trojanized version that had the same functionality as the legitimate file, but switched the outgoing crypto address where funds would be sent with the address of a Base64-encoded Web3 wallet belonging to the threat actor," Valentić said.

[![Swapping Crypto Addresses](data:image/png;base64... "Swapping Crypto Addresses")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4hyphenhyphenrYLRBYnXOeT5-Gif9IpidvxMgrqUb-2nwaDfhwc42SpB_bm3wg7Uqjhal5WMdrXj3wA51LHOccdoVD1a_R72agxwv6puk4AUDXlHP4NrINVxWIzY0d0TTMI7-4_8Q4jBrGygq2yugVHoK616a8B_Myynp5ZCmk9M9luLMQiXhZCMl4tNWcKCTfh_Lm/s790-rw-e365/crypto-malware.png)

In a similar vein, the payload is also designed to trojanize the file "src/app/ui/index.js" associated with the Exodus wallet.

But in an interesting twist, the attacks are aimed at two specific versions each of both Atomic Wallet (2.91.5 and 2.90.6) and Exodus (25.13.3 and 25.9.2) so as to ensure that the correct JavaScript files are overwritten.

"If, by chance, the package pdf-to-office was removed from the computer, the Web3 wallets' software would remain compromised and continue to channel crypto funds to the attackers' wallet," Valentić said. "The only way to completely remove the malicious trojanized files from the Web3 wallets' software would be to remove them completely from the computer, and re-install them."

The disclosure comes as ExtensionTotal detailed 10 malicious Visual Studio Code extensions that stealthily download a PowerShell script that disables Windows security, establishes persistence through scheduled tasks, and installs an XMRig cryptominer.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The extensions were collectively installed over a million times before they were taken down. The names of the extensions are below -

* Prettier — Code for VSCode (by prettier)
* Discord Rich Presence for VS Code (by Mark H)
* Rojo — Roblox Studio Sync (by evaera)
* Solidity Compiler (by VSCode Developer)
* Claude AI (by Mark H)
* Golang Compiler (by Mark H)
* ChatGPT Agent for VSCode (by Mark H)
* HTML Obfuscator (by Mark H)
* Python Obfuscator for VSCode (by Mark H)
* Rust Compiler for VSCode (by Mark H)

"The attackers created a sophisticated multi-stage attack, even installing the legitimate extensions they impersonated to avoid raising suspicion while mining cryptocurrency in the background," ExtensionTotal [said](https://blog.extensiontotal.com/mining-in-plain-sight-the-vs-code-extension-cryptojacking-campaign-19ca12904b59).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclu...