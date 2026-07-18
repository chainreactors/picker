---
title: Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT
url: https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html
source: The Hacker News
date: 2026-07-17
fetch_date: 2026-07-18T04:46:39.531931
---

# Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT

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

# [Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT](https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html)

**Ravie Lakshmanan**Jul 17, 2026Software Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA07xA1INXGKM7Z2LQ6zk2IFE_Hb_aDQNHmSfPtJkZY5Gzo2U2_cyflorBsU76hbXK8SwKXR5AmkK5dAAd9uw0wRh6gYaC-5ZPjT6kEdvE7rO-5G0TxXm8a-eytoygZOMuSG-aOnYkC_zTVbnxSq7zxaIFYyLcegbQ59WVztRO-y3MHmce7XuDz2SdVsKA/s1700-e365/vite-npm.jpg)

Cybersecurity researchers have discovered a cluster of seven malicious npm packages targeting the Vite frontend tooling ecosystem as part of a software supply chain attack.

The malicious package campaign, codenamed **[ViteVenom](https://checkmarx.com/zero-post/sequel-to-chainveil-npm-malware-targets-vite-ecosystem/)** by Checkmarx, marks an expansion of **[ChainVeil](https://checkmarx.com/zero-post/chainveil-a-malicious-npm-supply-chain-attack-by-successkey/)**, which was observed using an "unprecedented" four-tier blockchain-based command-and-control (C2) infrastructure spanning Tron, Aptos, and Binance Smart Chain to deliver a remote access trojan (RAT) capable reverse shell, credential harvesting, file exfiltration, and persistent backdoor injection.

"This tactic makes disabling or destroying the C2 infrastructure extremely difficult," Checkmarx researcher Pavan Gudimalla said in an analysis published last month. The activity has been attributed to a threat actor named SuccessKey, with evidence of malicious activity detected as far back as February 27, 2026, when cryptocurrency wallets linked to ViteVenom were activated.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

While the typosquats published to npm in connection with ChainVeil masqueraded as libraries for Tailwind, Sass, ORM, and rate-limiting tools, the latest iteration specifically focuses on developers building applications using the Vite JavaScript and frontend build tool.

The list of identified packages, published between June 29 and July 3, 2026, is below -

* @uw010010/vite-tree (1070 Downloads)
* @vite-tab/tab (289 Downloads)
* @vite-ln/build-ts (252 Downloads)
* @vite-mcp/vite-type (239 Downloads)
* @vite-pro/vite-ui (200 Downloads)
* @vitets/vite-ts (194 Downloads)
* @vite-ts/vite-ui (176 Downloads)

Another crucial difference between the two clusters is that, unlike ChainVeil's unscoped typosquats (e.g., "rate-limit-flexible"), ViteVenom makes use of scoped package names in an attempt to impersonate the "@vitejs/\*" namespace and lend it a veneer of legitimacy.

The main aspect that unites the two campaigns is the use of shared tier-2 infrastructure, which is used to deliver the RAT. Specifically, this involves the same Tron wallet and Aptos account addresses, which point to the same Binance Smart Chain (BSC) transaction leading to the malware.

Like in the case of ChainVeil, the malicious code doesn't execute at install time but at import time, which has the consequence of limiting endpoint security detections. It acts as a loader by reaching out to the blockchain infrastructure to obtain the next-stage -

* Query the Tron blockchain for the latest transaction from the attacker's wallet.
* Decode and reverse the transaction data field to obtain a BSC transaction hash.
* Query the BSC transaction to extract the encrypted payload from its input field.
* Decrypt the payload using a hard-coded key.

"The attacker stores payload pointers as transaction data on public blockchains rather than on domain names that can be seized, making the infrastructure nearly impossible to take down," Gudimalla explained.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

If the Tron-based payload retrieval method fails, the malware uses Aptos as a backup. The payload, for its part, queries the blockchain to retrieve the C2 configuration and a next-stage loader responsible for launching the RAT. In tandem, there exists a fallback mechanism that fetches the RAT directly from the C2 server over HTTP, completely bypassing the blockchain.

Users who have installed the packages are advised to remove them immediately, audit dependencies, rotate all credentials, and look for unauthorized modifications to .bashrc, .zshrc, and .profile files.

"The surface-level differences - different package names, different maintainer accounts, different Tier-1 wallets, different malicious file paths - are consistent with how a single operator would compartmentalize multiple distribution tracks to limit exposure," Checkmarx said.

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

[Backdoor](https://thehackernews.com/search/label/Backdoor), [Command and Control](https://thehackernews.com/search/label/Command%20and%20Control), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [Developer Security](https...