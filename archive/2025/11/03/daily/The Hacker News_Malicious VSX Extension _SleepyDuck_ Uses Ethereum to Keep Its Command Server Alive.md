---
title: Malicious VSX Extension "SleepyDuck" Uses Ethereum to Keep Its Command Server Alive
url: https://thehackernews.com/2025/11/malicious-vsx-extension-sleepyduck-uses.html
source: The Hacker News
date: 2025-11-03
fetch_date: 2025-11-04T03:11:34.567977
---

# Malicious VSX Extension "SleepyDuck" Uses Ethereum to Keep Its Command Server Alive

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Malicious VSX Extension "SleepyDuck" Uses Ethereum to Keep Its Command Server Alive](https://thehackernews.com/2025/11/malicious-vsx-extension-sleepyduck-uses.html)

**Nov 03, 2025**Ravie LakshmananCryptocurrency / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsNAYBUN0RQ2z5BWnN5wrHTjB-XMx0nYPvJ5PMwCjxNk6CVExZCv401_jX_vaktwnLz8B3owRjupOCNIH7s2lbATDXkpMWwounrKb1OaiINgihVNcp_Mc17Wt7y2-LJBiEOk04hyphenhyphen6WlNKg76W5-f3fx2SDPtSSHQSO5gPu0E4V5RmzDEH0WcdpmAzXG0iB/s790-rw-e365/soladity.jpg)

Cybersecurity researchers have flagged a new malicious extension in the Open VSX registry that harbors a remote access trojan called **SleepyDuck**.

According to Secure Annex's John Tuckner, the extension in question, juan-bianco.solidity-vlang (version 0.0.7), was first published on October 31, 2025, as a completely benign library that was subsequently updated to version 0.0.8 on November 1 to include new malicious capabilities after reaching 14,000 downloads.

"The malware includes sandbox evasion techniques and utilizes an Ethereum contract to update its command and control address in case the original address is taken down," Tuckner [added](https://secureannex.com/blog/sleepyduck-malware/).

Campaigns [distributing](https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html) rogue extensions targeting Solidity developers have been repeatedly detected across both the Visual Studio Extension Marketplace and Open VSX. In July 2025, Kaspersky [disclosed](https://thehackernews.com/2025/07/weekly-recap-chrome-0-day-ivanti.html#:~:text=Open%20VSX%20Used%20to%20Distribute%20Malicious%20VS%20Code%20Extensions) that a Russian developer lost $500,000 in cryptocurrency assets after installing one such extension through Cursor.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

In the latest instance detected by the enterprise extension security firm, the malware is triggered when a new code editor window is opened or a .sol file is selected.

Specifically, it's configured to find the fastest Ethereum Remote Procedure Call (RPC) provider to connect to in order to obtain access to the blockchain, initialize contact with a remote server at "sleepyduck[.]xyz" (hence the name) via the contract address "[0xDAfb81732db454DA238e9cFC9A9Fe5fb8e34c465](https://etherscan.io/address/0xDAfb81732db454DA238e9cFC9A9Fe5fb8e34c465)," and kicks off a polling loop that checks for new commands to be executed on the host every 30 seconds.

It's also capable of gathering system information, such as hostname, username, MAC address, and timezone, and exfiltrating the details to the server. In the event the domain is seized or taken down, the malware has built-in fallback controls to reach out to a predefined list of Ethereum RPC addresses to extract the contract information that can hold the server details.

What's more, the extension is equipped to reach a new configuration from the contract address to set a new server, as well as execute an emergency command to all endpoints in the event that something unexpected occurs. The contract was created on October 31, 2025, with the [threat actor](https://etherscan.io/address/0x0edcfe26cf600fb56ae6aaf3f1d943c811314573) updating the server details from "localhost:8080" to "sleepyduck[.]xyz" over the course of four transactions.

It's not clear if the download counts were artificially inflated by the threat actors to boost the relevance of the extension in search results – a tactic often [adopted](https://thehackernews.com/2025/10/eclipse-foundation-revokes-leaked-open.html) to increase the popularity so as to trick unsuspecting developers into installing a malicious library.

The development comes as the company also disclosed details of another set of five extensions, this time published to the VS Code Extension Marketplace by a user named "developmentinc," including a Pokémon-themed library that downloads a batch script miner from an external server ("mock1[.]su:443") as soon as it's installed or enabled, and runs the miner using "cmd.exe."

The script file, besides relaunching itself with administrator privileges using PowerShell and configuring Microsoft Defender Antivirus exclusions by adding every drive letter from C: through Z:, downloads a Monero mining executable from "mock1[.]su" and runs it.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

The extensions uploaded by the threat actor, now no longer available for download, are listed below -

* developmentinc.cfx-lua-vs
* developmentinc.pokemon
* developmentinc.torizon-vs
* developmentinc.minecraftsnippets
* developmentinc.kombai-vs

Users are advised to exercise caution when it comes to downloading extensions, and make sure that they are from trusted publishers. Microsoft, for its part, announced back in June that it's instituting periodic marketplace-wide scans to protect users against malware. Every removed extension from the official marketplace can be viewed from the [RemovedPackages page](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md) on GitHub.

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

[...