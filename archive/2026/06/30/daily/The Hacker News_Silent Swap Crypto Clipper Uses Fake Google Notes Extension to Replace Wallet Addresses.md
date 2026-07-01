---
title: Silent Swap Crypto Clipper Uses Fake Google Notes Extension to Replace Wallet Addresses
url: https://thehackernews.com/2026/06/silent-swap-crypto-clipper-uses-fake.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:40.458381
---

# Silent Swap Crypto Clipper Uses Fake Google Notes Extension to Replace Wallet Addresses

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

# [Silent Swap Crypto Clipper Uses Fake Google Notes Extension to Replace Wallet Addresses](https://thehackernews.com/2026/06/silent-swap-crypto-clipper-uses-fake.html)

**Ravie Lakshmanan**Jun 30, 2026Browser Security / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfz8WYO9wONzogh2V8g9VorZ8Ab_nAUZMD7rOM9xrVUhg3cbKGA5zc73PGQiAkbsNgY-qbm2AFAUjBdeMcpemGmDNWrvnpyjzKiqU8iJHMetkW68d20V_U-96mHOaHF6fff7VKBREN2v6fz1R_ahyIklq-Fd7ILYKxXck5ahL1BoFWC_CDQFrQZqQqg3hm/s1700-e365/chrome-wallet.jpg)

Cybersecurity researchers have flagged an active browser extension campaign that is designed to steal cryptocurrency by stealthily replacing wallet addresses when unsuspecting users initiate a transaction.

The [cryptocurrency clipper](https://thehackernews.com/2026/06/crypto-clipper-campaign-abuses-fake.html) activity has been codenamed **Silent Swap** by McAfee Labs.

"The campaign is delivered through unsigned installers – observed in both .NET and Golang variants – that deploy a malicious Chromium extension masquerading as a benign 'Google Notes' utility," the cybersecurity company [said](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/crypto-clipper-wallet-swapping-browser-extension-malware/) in a technical report shared with The Hacker News.

The unsigned .NET installer, named BaseZipInstaller, is designed to retrieve a ZIP archive, which serves as a foundation for the malicious browser extension by scanning the system for Chromium-based browsers. For each detected profile in those browsers, it forcibly terminates the browser process and injects the extension by modifying the [Secure Preferences and Preferences](https://thehackernews.com/2023/08/new-version-of-rilide-data-theft.html) files.

The end goal of the extension is to act as a clipper that's capable of intercepting and manipulating wallet addresses copied into the system clipboard with the goal of rerouting the funds to an attacker-controlled wallet. To realize its goals, the bogus Google Notes extension requests users to grant it permissions to access the clipboard, all URLs, and the browsing history.

Because most transactions on the blockchain are irreversible, an address swap can result in permanent financial loss. McAfee Labs said the activity overlaps with a prior [CountLoader campaign](https://thehackernews.com/2026/06/weedhack-attacks-minecraft-users.html#countloader-delivers-crypto-clipper) that delivered a crypto clipper, with evidence pointing to the same threat actor behind both clusters.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

What makes Silent Swap stand apart is the use of a technique called [EtherHiding](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html) that uses the blockchain as a [dead drop resolver](https://attack.mitre.org/techniques/T1102/001/) to retrieve the active command-and-control (C2) server details. This allows the attacker to trivially update a smart contract value to point to the new domain instead of having to redeploy the malware itself.

The second aspect revolves around the covert installation of the browser extension on Chromium-based browsers like Google Chrome, Microsoft Edge, Brave, and Vivaldi by modifying protected browser settings files. The attack, however, hinges on enabling the developer mode for newer versions of the browsers, something that a threat actor can accomplish through social engineering tactics.

"Normally, these browsers store security verification data (hash/HMAC values) alongside sensitive settings to detect unauthorized changes," McAfee said. "The malware recalculates and updates these security values after tampering with the files, tricking the browser into believing the malicious extension was installed legitimately."

"This allows the extension to bypass the normal extension web store installation process and load silently without user approval."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnt6PBoFu3sStdR9v0KVAHUwUbrb_itMErQwvp8Cu3b_Uel3_veVSIDoyqHHIe7N6NXqH6t1VfLOZNGaIt4hbS2T4igD__NdcMxGoP_ftUFZkp_7g_SP9caciBDXXnDwhl_r9FOE2cUv0MpadiB0yubFcflQu9q_dqJcJIGXZvHy7YOJwYz2t4zFwLNMYD/s1700-e365/cover.jpg)

The campaign's persistence and evasion posture has been characterized as deliberate and layered, with the primary focus being on maintaining low visibility to the end user and high resilience against takedown and static analysis. Persistence is established by registering the extension by altering the browser's Secure Preferences file so that it's loaded on subsequent browser launches without the need for a separate mechanism.

In addition, the malware attempts to enable developer mode programmatically in Brave and Opera, and the installer is self-deleted after execution, effectively removing an indicator of initial compromise. Another evasion technique is the use of dynamic wallet substitution, which is responsible for fetching a replacement address corresponding to a victim's original address.

"It sends the intercepted wallet address to the attacker backend and uses the response to dynamically substitute the original address," McAfee said. "If the backend request fails, the function falls back to a predefined hard-coded wallet address, ensuring uninterrupted malicious activity."

For every wallet address matching patterns associated with Bitcoin (BTC), Ethereum, Bitcoin Cash, Ripple, and Dash, it's mapped to a unique attacker-controlled address on the server-side. In contrast, all submitted Solana addresses resolve to a single attacker address. As of writing, the Solana address has been found to have a balance of $1,902.45.

"Each submitted address is mapped to a unique attacker-controlled address. Re-submitting the same original returns the same replacement, indicating a deterministic one-to-one mapping maintained server-side.

Telemetry data suggests that infections are globally distributed, with a higher co...