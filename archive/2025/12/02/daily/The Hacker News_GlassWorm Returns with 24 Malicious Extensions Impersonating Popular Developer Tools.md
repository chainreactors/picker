---
title: GlassWorm Returns with 24 Malicious Extensions Impersonating Popular Developer Tools
url: https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html
source: The Hacker News
date: 2025-12-02
fetch_date: 2025-12-03T03:17:10.358488
---

# GlassWorm Returns with 24 Malicious Extensions Impersonating Popular Developer Tools

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [GlassWorm Returns with 24 Malicious Extensions Impersonating Popular Developer Tools](https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html)

**Dec 02, 2025**Ravie LakshmananMalware / Blockchain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2togvMtptRUBClEk7aVrpK5mEsCqxdPbcfpQ0aczPMOBE-apKuQvTp-wxJpmSI5n7rh1z6jBb0CeMnt1APf5X_yfVrRIJ_Ix0fc1KBJ5HI7LHhZhTLsAsukNnM6KZaWakvD3X5cxIZgagaIKVltnozAVWGDBz48ARBwUwj9ODV7KRa9j4ZaOWdzHmF69U/s790-rw-e365/hacked.jpg)

The supply chain campaign known as [GlassWorm](https://secureannex.com/blog/glassworm-continued/) has once again reared its head, infiltrating both Microsoft Visual Studio Marketplace and Open VSX with 24 extensions impersonating popular developer tools and frameworks like Flutter, React, Tailwind, Vim, and Vue.

GlassWorm was [first documented](https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html) in October 2025, detailing its use of the Solana blockchain for command-and-control (C2) and harvest npm, Open VSX, GitHub, and Git credentials, drain cryptocurrency assets from dozens of wallets, and turn developer machines into attacker-controlled nodes for other criminal activities.

The most crucial aspect of the campaign is the abuse of the stolen credentials to compromise additional packages and extensions, thereby spreading the malware like a worm. Despite [continued efforts](https://thehackernews.com/2025/10/eclipse-foundation-revokes-leaked-open.html) of Microsoft and Open VSX, the malware [resurfaced](https://thehackernews.com/2025/11/glassworm-malware-discovered-in-three.html) a second time last month, and the attackers were [observed](https://thehackernews.com/2025/11/weekly-recap-lazarus-hits-web3-intelamd.html#:~:text=12%20Malicious%20VS%20Code%20Extensions%20Flagged) targeting GitHub repositories.

The latest wave of the GlassWorm campaign, spotted by Secure Annex's John Tuckner, involves a total of 24 extensions spanning both repositories. The list of identified extensions is below -

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

VS Code Marketplace:

* iconkieftwo.icon-theme-materiall
* prisma-inc.prisma-studio-assistance ([removed](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md) as of December 1, 2025)
* prettier-vsc.vsce-prettier
* flutcode.flutter-extension
* csvmech.csvrainbow
* codevsce.codelddb-vscode
* saoudrizvsce.claude-devsce
* clangdcode.clangd-vsce
* cweijamysq.sync-settings-vscode
* bphpburnsus.iconesvscode
* klustfix.kluster-code-verify
* vims-vsce.vscode-vim
* yamlcode.yaml-vscode-extension
* solblanco.svetle-vsce
* vsceue.volar-vscode
* redmat.vscode-quarkus-pro
* msjsdreact.react-native-vsce

Open VSX:

* bphpburn.icons-vscode
* tailwind-nuxt.tailwindcss-for-react
* flutcode.flutter-extension
* yamlcode.yaml-vscode-extension
* saoudrizvsce.claude-dev
* saoudrizvsce.claude-devsce
* vitalik.solidity

The attackers have been found to artificially inflate the download counts to make the extensions appear trustworthy and cause them to prominently appear in search results, often in close proximity to the actual projects they impersonate to deceive developers into installing them.

"Once the extension has been approved initially, the attacker seems to easily be able to update code with a new malicious version and easily evade filters," Tuckner said. "Many code extensions begin with an 'activate' context, and the malicious code is slipped in right after the activation occurs."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-insights-d)

The new iteration, while still relying on the invisible Unicode trick, is characterized by the use of Rust-based implants that are packaged inside the extensions. In an [analysis](https://www.nextron-systems.com/2025/11/28/malicious-vs-code-extension-impersonating-material-icon-theme-found-in-marketplace/) of the "icon-theme-materiall" extension, Nextron Systems said it comes with [two Rust implants](https://www.nextron-systems.com/2025/11/29/analysis-of-the-rust-implants-found-in-the-malicious-vs-code-extension/) that are capable of targeting Windows and macOS systems -

* A Windows DLL named os.node
* A macOS dynamic library named darwin.node

As observed in the previous GlassWorm infections, the implants are designed to fetch details of the C2 server from a Solana blockchain wallet address and use it to download the next-stage payload, an encrypted JavaScript file. As a backup, they can parse a Google Calendar event to fetch the C2 address.

"Rarely does an attacker publish 20+ malicious extensions across both of the most popular marketplaces in a week," Tuckner said in a statement. "Many developers could easily be fooled by these extensions and are just one click away from compromise."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Blockchain](https://thehackernews.com/search/label/Blockchain)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Open VSX](https://thehackernews.com/search/label/Open%20VS...