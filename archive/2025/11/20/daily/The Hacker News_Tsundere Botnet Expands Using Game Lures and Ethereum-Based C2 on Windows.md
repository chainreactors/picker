---
title: Tsundere Botnet Expands Using Game Lures and Ethereum-Based C2 on Windows
url: https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html
source: The Hacker News
date: 2025-11-20
fetch_date: 2025-11-21T03:14:22.443653
---

# Tsundere Botnet Expands Using Game Lures and Ethereum-Based C2 on Windows

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

# [Tsundere Botnet Expands Using Game Lures and Ethereum-Based C2 on Windows](https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html)

**Nov 20, 2025**Ravie LakshmananBotnet / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWCzFuJ27zRdLiXDJLbzAKsXq1B21v769VXyN0N9wjg3aQQPMHqsiaxXi3V6LM1xbQCB0ecsOjlEEORaSeRnnFVBjK3OtrxcTS_oSQiadmLSZNDow8eeIB5QVX8q19t6MyRR5XL2CRsTy7QD-GtWn82x_HH1gcas-9NW1vDfN3QlvcpUSqRa1gnMNBD2xJ/s790-rw-e365/botnet-malware-windows.jpg)

Cybersecurity researchers have warned of an actively expanding botnet dubbed **Tsundere** that's targeting Windows users.

Active since mid-2025, the threat is [designed](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/) to execute arbitrary JavaScript code retrieved from a command-and-control (C2) server, Kaspersky researcher Lisandro Ubiedo said in an analysis published today.

There are currently no details on how the botnet malware is propagated; however, in at least one case, the threat actors behind the operation are said to have leveraged a legitimate Remote Monitoring and Management (RMM) tool as a conduit to download an MSI installer file from a compromised site.

The names given to the malware artifacts – Valorant, r6x (Rainbow Six Siege X), and cs2 (Counter-Strike 2) – also suggest that the implant is likely being disseminated using lures for games. It's possible that users searching for pirated versions of these games are the target.

Regardless of the method used, the fake MSI installer is designed to install Node.js and launch a loader script that's responsible for decrypting and executing the main botnet-related payload. It also prepares the environment by downloading three legitimate libraries, namely, ws, ethers, and pm2, using an "npm install" command.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"The pm2 package is installed to ensure the Tsundere bot remains active and used to launch the bot," Ubiedo explained. "Additionally, pm2 helps achieve persistence on the system by writing to the registry and configuring itself to restart the process upon login."

Kaspersky's analysis of the C2 panel has revealed that the malware is also propagated in the form of a PowerShell script, which performs a similar sequence of actions by deploying Node.js on the compromised host and downloading ws and ethers as dependencies.

While the PowerShell infector doesn't make use of pm2, it carries out the same actions observed in the MSI installer by creating a registry key value that ensures the bot is executed on each login by spawning a new instance of itself.

The Tsundere botnet makes [use of the Ethereum blockchain](https://thehackernews.com/2025/10/hackers-abuse-blockchain-smart.html) to [fetch details](https://thehackernews.com/2025/11/malicious-vsx-extension-sleepyduck-uses.html) of the WebSocket C2 server (e.g., ws://193.24.123[.]68:3011 or ws://185.28.119[.]179:1234), creating a resilient mechanism that allows the attackers to [rotate the infrastructure](https://etherscan.io/tx/0x834769584d0305b7517aea4f17d3382e68e86b535c190bba51d56981c83a4705) simply by employing a [smart contract](https://etherscan.io/address/0xa1b40044EBc2794f207D45143Bd82a1B86156c6b). The contract was created on September 23, 2024, and has had 26 transactions to date.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfP4WfTWwwnAS92uX37llxzn0vGgMoK4uC8PvpPVkjHqhXw_alJ-_EJXlHMUIIB6LrGO1apBbYYKhScGy_KuuwtOS3qvYu-4mEQeDpUywV1ShoseYiyGE-wuc_-pUWossWkdr_FGYk71Oq4Pp22zB_Ggt3IinhVaiJ845d_vaa_aayurjzcVtCp9NP7ZEP/s790-rw-e365/tsundere-node9.png)

Once the C2 address is retrieved, it checks to ensure it is a valid WebSocket URL, and then proceeds to establish a WebSocket connection with the specific address and receive JavaScript code sent by the server. Kaspersky said it did not observe any follow-up commands from the server during the observation period.

"The ability to evaluate code makes the Tsundere bot relatively simple, but it also provides flexibility and dynamism, allowing the botnet administrators to adapt it to a wide range of actions," Kaspersky said.

The botnet operations are facilitated by a control panel that allows logged-in users to build new artifacts using MSI or PowerShell, manage administrative functions, view the number of bots at any given point of time, turn their bots into a proxy for routing malicious traffic, and even browse and purchase botnets via a dedicated marketplace.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Exactly who is behind Tsundere is not known, but the presence of the Russian language in the source code for logging purposes alludes to a threat actor who is Russian-speaking. The activity is assessed to share functional overlaps with a malicious npm campaign [documented](https://thehackernews.com/2024/11/malware-campaign-uses-ethereum-smart.html) by Checkmarx, Phylum, and Socket in November 2024.

What's more, the same server has been identified as hosting the C2 panel associated with an information stealer known as 123 Stealer, which is available on a subscription basis for $120 per month. It was first advertised by a threat actor named "koneko" on a dark web forum on June 17, 2025, per [Outpost24's KrakenLabs Team](https://x.com/KrakenLabs_Team/status/1940756956156666349).

Another clue that points to its Russian origins is that the customers are forbidden from using the stealer to target Russia and the Commonwealth of Independent States (CIS) countries. "Violation of this rule will result in the immediate blocking of your account without explanation," Koneko said in the post at the time.

"Infections can occur through MSI and PowerShell files, which provide flexibility in terms of disguising installers, using phishing as a point of entry, or integrating with other attack mechanisms, making it an even more formidable threat," Kaspersky said....