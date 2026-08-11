---
title: Solidity Pro VS Code Extensions Steal Crypto Wallets, API Keys, and Credentials
url: https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html
source: The Hacker News
date: 2026-08-10
fetch_date: 2026-08-11T03:31:51.789864
---

# Solidity Pro VS Code Extensions Steal Crypto Wallets, API Keys, and Credentials

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

![cybersecurity](data:image/svg+xml;base64...)

# [Solidity Pro VS Code Extensions Steal Crypto Wallets, API Keys, and Credentials](https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html)

**Ravie Lakshmanan**Aug 10, 2026Malware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR5_Dx4heVYIxaujo8ybl0OFdVuLzMFe0qdEdr6-q_QTdhSVlgHdrP6MeooXamFpRNfHjoAqTquvk3CkkCKUw1TQDkQJCrZY1RTC9iYK_bsTLNvpj0BZfFKFcnlt1RAlBvfcsWeSuLAn6Gwh9lur7v9-HlH-6ZpSmw7npsn9TSZAEpwFSFE54_xcFPcuDi/s1700-e365/pro.jpg)

Cybersecurity researchers have flagged a malicious Microsoft Visual Studio Code (VS Code) extension named Solidity Pro ("solidity-pro") that has been observed delivering a browser wallet and credential stealer.

The names of the extensions are below -

* helper-beeps.solidity-pro
* web3devtoolsx.solidity-pro

Although neither of the extensions is now available on Open VSX, the GitHub repository for "[web3devtoolsx/solidity-pro](https://github.com/web3devtoolsx/solidity-pro)" continues to remain accessible as of writing.

According to [Yeeth Security](https://yeethsecurity.com/blog/2026-08-06-Solidity-Pro-WhiteCobra-C2-to-Telegram), early iterations of the extensions – from 1.0.0 through v2.4.x – were found to beacon to Cloudflare Workers endpoints to retrieve an encrypted Python payload and execute it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Subsequent versions starting with v3.0.0, on the other hand, have shifted to a full-blown information stealer that can collect browser profiles, crypto wallets, source-control tokens, API keys, SSH keys, and Telegram bot tokens. The captured data is then exfiltrated via a Telegram bot upload.

The list of data harvested by the stealer is as follows -

* GitHub ghp\_ and github\_pat\_ tokens
* GitLab glpat- tokens
* AWS keys and session tokens
* Cloudflare cfat\_ tokens
* OpenAI sk-, sk-proj-, and sk-ant- keys
* Telegram bot tokens
* Mnemonic and seed phrases
* MetaMask, Phantom, Rabby, Coinbase, Trust, Keplr wallet vaults
* Bitcoin WIF / xprv
* SSH private keys (PRIVATE KEY)
* URL credentials and 1Password MFA tokens

The malware family is also equipped to bypass marketplace review, static scanning, and casual sandboxing through heavy obfuscation, intermediate clean versions to build trust, and randomized delayed activation that causes the malicious code to run several hours or days after installation.

"By the time the malicious branch runs, the user has already decided the extension is useful, and automated scanners that only observe the package for minutes have moved on," Yeeth Security said. "The obfuscation is not decorative; it splits strings across IIFE tables, reassembles them at runtime, and switches method names between releases so signature-based detection must track a moving target."

The cybersecurity company said the activity shares the same high-level playbook as [WhiteCobra](https://yeethsecurity.com/blog/2025-09-03-WhiteCobra), another threat cluster that was [detected in September 2025](https://thehackernews.com/2025/09/weekly-recap-bootkit-malware-ai-powered.html#:~:text=Code%2C%20Cursor%2C%20and%20Windsurf%20Users%20Targeted%20by%20WhiteCobra) as distributing Lumma Stealer through malicious VS Code extensions.

This is not the first time threat actors have [published](https://thehackernews.com/2025/01/russian-speaking-attackers-target.html) bogus Solidity extensions across [open-source ecosystems](https://thehackernews.com/2025/11/malicious-vsx-extension-sleepyduck-uses.html). In June 2026, Yeeth Security flagged another extension named "[ethdevtools.solidity-language-support](https://yeethsecurity.com/blog/2026-06-21-ethdevtools-Clipboard-Crypto-Stealer)" that impersonated a Solidity language-support tool for Ethereum developers, but harbored a delayed-activation clipboard stealer to scrape BIP-39 seed phrases, Ethereum private keys, and wallet addresses.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"When a recognized crypto address is on the clipboard, it replaces the pasted value with an attacker-controlled address," it added. "The swap happens through vscode.env.clipboard.writeText, a first-party API call that requires no child\_process, no network access, and no file writes. Static scanners that only look for dangerous Node imports will not see it."

The findings also coincide with the discovery of a number of rogue VS Code extensions and npm packages -

* An npm package called "[ascii-fetcher](https://yeethsecurity.com/blog/2026-07-02-The-jsononifier-npm-Dropper)," which embeds the malicious code in a dependency named "@jaymara/jsononifier" to decode an embedded command (in the observed case, "calc.exe") and run it via "child\_process.exec" with "windowsHide"
* [A set of 10 VS Code extensions](https://yeethsecurity.com/blog/2026-07-02-The-Windows-Installer-Dropper-Family) that deliver a wide range of Windows-based BAT, JavaScript, and HTA droppers, with two of them bundling an npm dependency that uses a postinstall hook to fetch and execute a remote payload
* A VS Code extension named "[DigitalBarberTrim.html-entity-codec](https://yeethsecurity.com/blog/2026-07-02-DigitalBarberTrim-Multi-IDE-VSIX-Installer)" that drops a remote VSIX file in select versions after enumerating known VS Code forks like Cursor, Windsurf, Codium, and Positron, while serving a "nearly empty stub" in others to fly under the radar.
* A VS Code extension named "[Zlmiles.zlmiles-liquid](https://yeethsecurity.com/blog/2026-06-18-The-Replit-MSI-and-State-Diagram-Campaign)" (now removed from the [VS Marketplace](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md)) that makes use of a suspected builder kit to drop an MSI installer hosted on a Replit domain.

Users who have installed the extensions are advised to remove them, inspect dependency graphs, block known command-and-control (C2) domains, and alert on use of cscript, mshta, cmd, curl, and powershell commands.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) ...