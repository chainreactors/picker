---
title: Aeternum C2 Botnet Stores Encrypted Commands on Polygon Blockchain to Evade Takedown
url: https://thehackernews.com/2026/02/aeternum-c2-botnet-stores-encrypted.html
source: The Hacker News
date: 2026-02-26
fetch_date: 2026-02-27T04:08:48.987964
---

# Aeternum C2 Botnet Stores Encrypted Commands on Polygon Blockchain to Evade Takedown

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Aeternum C2 Botnet Stores Encrypted Commands on Polygon Blockchain to Evade Takedown](https://thehackernews.com/2026/02/aeternum-c2-botnet-stores-encrypted.html)

**Ravie Lakshmanan**Feb 26, 2026Malware / Blockchain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQlH8RQUmcg8IWqV76NL0o4uRe86gJ6kxLV3DRYppBAVrfFR_gMPQBFn6GIl2jd9ZgzsuwRGAGTVUbaWCj795-XZ8I3eSBDLz6Q_0w4Alef6GNA3NtpK4po_WVC6p9o4aNVHqgCAEb3a7CqL_x7oBGWQ7N4z0IMyzOX3aZoI_TUZenfdAm0LZojDIkumG0/s1700-e365/botnet.jpg)

Cybersecurity researchers have disclosed details of a new botnet loader called **Aeternum C2** that uses a blockchain-based command-and-control (C2) infrastructure to make it resilient to takedown efforts.

"Instead of relying on traditional servers or domains for command-and-control, Aeternum stores its instructions on the public Polygon blockchain," Qrator Labs [said](https://qrator.net/blog/details/Exploring-Aeternum-C2/) in a report shared with The Hacker News.

"This network is widely used by decentralized applications, including Polymarket, the world's largest prediction market. This approach makes Aeternum's C2 infrastructure effectively permanent and resistant to traditional takedown methods."

This is not the first time botnets have been found relying on blockchain for C2. In 2021, Google said it took steps to disrupt a botnet known as [Glupteba](https://thehackernews.com/2024/02/glupteba-botnet-evades-detection-with.html) that uses the Bitcoin blockchain as a backup C2 mechanism to fetch the actual C2 server address.

Details of Aeternum C2 first emerged in December 2025, when Outpost24's KrakenLabs [revealed](https://x.com/KrakenLabs_Team/status/1998330973461622894) that a threat actor by the name of LenAI was advertising the malware on underground forums for $200 that grants customers access to a panel and a configured build. For $4,000, customers were allegedly promised the entire C++ codebase along with updates.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

A native C++ loader available in both x32 and x64 builds, the malware works by writing commands to be issued to the infected host to smart contracts on the Polygon blockchain. The bots then read those commands by querying public remote procedure call (RPC) endpoints.

All of this is managed via the web-based panel, from where customers can select a smart contract, choose a command type, specify a payload URL and update it. The command, which can target all endpoints or a specific one, is written into the blockchain as a transaction, after which it becomes available to every compromised device that's polling the network.

"Once a command is confirmed, it cannot be altered or removed by anyone other than the wallet holder," Qrator Labs said. "The operator can manage multiple smart contracts simultaneously, each one potentially serving a different payload or function, such as a clipper, a stealer, a RAT, or a miner."

According to a [two-part research](https://ctrlaltintel.com/threat%20research/Aeternum-Part-1/) published by [Ctrl Alt Intel](https://ctrlaltintel.com/threat%20research/Aeternum-Part-2/) earlier this month, the C2 panel is implemented as a Next.js web application that allows operators to deploy smart contracts to the Polygon blockchain. The smart contracts contain a function that, when called by the malware via the Polygon RPC, causes it to return the encrypted command that's subsequently decoded and run on the victim machines.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQh_BU2qZgAMPAaHWPZvrCPcPyObbJCdv76tTa_B3jlKu1Bj73xL4DEniUgRMYs5EFkAL01Cx2nN1OoEUPWg2rhLfw8RsJcJ5tmCMhM6y4QwFxLIR3J2zdKeqYrIVKDPIiE6E30I16nZlUnsMXmawGneCbyo3IrxfNrbTuppvw0lScE9pTgAwQUWKy5-40/s1700-e365/botnet.jpg)

Besides using the blockchain to turn it into a takedown-resistant botnet, the malware packs in various anti-analysis features to extend the lifespan of infections. This includes checks to detect virtualized environments, in addition to equipping customers with the ability to scan their builds via [Kleenscan](https://kleenscan.com/index) to ensure that they are not flagged by antivirus vendors.

"The operational costs are negligible: $1 worth of MATIC, the native token of the Polygon network, is enough for 100 to 150 command transactions," the Czechian cybersecurity vendor said. "The operator doesn't need to rent servers, register domains, or maintain any infrastructure beyond a crypto wallet and a local copy of the panel."

The threat actor has since [attempted to sell the entire toolkit](https://x.com/KrakenLabs_Team/status/2024872751266148544) for an asking price of $10,000, claiming a lack of time for support and their involvement in another project. "I will sell the entire project to one person with permission for resale and commercial use, with all 'rights,'" LenAI said. "I will also give useful tips/notes on development that I did not have time to implement."

It's worth noting that LenAI is also behind a second crimeware solution called [ErrTraffic](https://thehackernews.com/2026/01/threatsday-bulletin-ghostad-drain-macos.html#fake-glitch-scam-toolkit-exposed) that enables threat actors to automate ClickFix attacks by generating fake glitches on compromised websites to induce a false sense of urgency and deceive users into following malicious instructions.

The disclosure comes as Infrawatch published details of an underground service that deploys dedicated laptop hardware into American homes to co-opt the devices into a residential proxy network named DSLRoot that redirects malicious traffic through them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The hardware is designed to run a Delphi-based program called DSLPylon that's equipped with capabilities to enumerate supported modems on the network, as well as remotely control the residential networking equ...