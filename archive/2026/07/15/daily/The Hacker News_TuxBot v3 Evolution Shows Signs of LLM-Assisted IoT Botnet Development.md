---
title: TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development
url: https://thehackernews.com/2026/07/tuxbot-v3-evolution-shows-signs-of-llm.html
source: The Hacker News
date: 2026-07-15
fetch_date: 2026-07-16T04:58:59.200350
---

# TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development

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

# [TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development](https://thehackernews.com/2026/07/tuxbot-v3-evolution-shows-signs-of-llm.html)

**Ravie Lakshmanan**Jul 15, 2026IoT Security / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmKa1OIdUu8LgLPgZkc9qbOTzhARf1dEJa_fzyVt7vvSzidHy3Lrb-2R4hs2ryt9b4Aq3zOnJRtWVuQ8KHKUZ5x9Iv6Q0vGTVMPxNMLTdGaNsquyrL18QXk8TcMP2nEwFHE1snKt2aG6rEmyVMwRp7Fk4G_x_sXjk_4AmYWsH2JCvOe2Adut2PZbLVc4YI/s1700-e365/tuxbot.jpg)

Cybersecurity researchers have disclosed details of a previously unreported Internet-of-Things (IoT) botnet framework dubbed **TuxBot v3 Evolution** that shows signs of being developed with assistance from a large language model (LLM), albeit with not so successful results.

"While the AI complied with their request to generate botnet code, it included a safety disclaimer that the developer failed to remove before shipping," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/). "Although the LLM clearly aided in constructing the botnet, several functions in the analyzed samples failed to work correctly."

The cybersecurity company said a manual code review would have resolved these errors and that it's possible more polished iterations of the malware exist out there in the wild.

The botnet framework consists of multiple components: a C-based bot agent that cross-compiles for multiple architectures (e.g., ARM, MIPS, MIPSEL, MIPS64, x86\_64, PowerPC, and RISC-V), a Go-based command-and-control (C2) server with a DDoS-for-hire panel, a custom exploit virtual machine, Docker-based test infrastructure, and an automated build system.

The bot agent is designed to brute-force Telnet access on targeted devices with a set of 1,496 credential pairs, as well as incorporate exploit code targeting more than 30 IoT device families using known vulnerabilities. It communicates with the C2 server over an encrypted TCP channel, while resorting to a SHA512 domain generation algorithm (DGA), peer-to-peer (P2P) gossip protocol with Ed25519-signed commands, Internet Relay Chat (IRC), DNS TXT queries, and HTTP polling as a fallback mechanism.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The modular framework's lineage has been traced back to three different botnets, like [Mirai](https://thehackernews.com/2024/05/mirai-botnet-exploits-ivanti-connect.html), [AISURU](https://thehackernews.com/2026/03/doj-disrupts-3-million-device-iot.html), and Wuhan, in addition to partially porting some of its functions from the open-source [MHDDoS Python DDoS toolkit](https://github.com/MatrixTM/MHDDoS). At least one sample of the malware was [uploaded](https://www.virustotal.com/gui/file/71dfbb171eca4ef9d02ff630b56e5283bbef7b375d4dbe9e8c9531bef312fa8d) to the VirusTotal platform on January 20, 2026, indicating it has been around for over six months. Evidence suggests that work on the botnet commenced one year before that, when the author cloned the MHDDoS repository from GitHub.

"According to the framework's description, the TuxBot developer built what they called a professional-grade C2 framework platform with a multi-user admin panel, automated deployment, and modular attack capabilities," researchers Chris Navarrete, Asher Davila, and Doel Santos said.

The Go-based C2 server component uses three different TCP ports for incoming connections -

* TCP port 1999 (or 31337), which is used for handling encrypted command dispatch to connected bots
* TCP port 2222, which presents an interactive shell for operators over SSH
* TCP port 9999, which uses a JSON interface for programmatic access

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh977AeY5sxCPHTIaTVgIEcLRReomDexUUSjpBFCmpQD5zvCToXwO0dnOSd3LW93Ete7jQ_nlqRvrsp_Tg3zEPda3zJd2vJ9bDQR7dH_BeFiAdED2-P-8ZD0r7M3ueVSuipF_BA0pXgqNhQHML18b8lee4fnxgpdrX43biUdZMHEH362rrjNzlZnPY4rUw8/s1700-e365/cnc.png)

Once launched, the botnet follows a pre-defined initialization sequence to perform a series of actions -

* Loading the C2 address from a multi-tiered architecture with one primary channel and five alternate mechanisms
* Setting up anti-debugging and anti-VM protections that check for running analysis tools
* Hiding its process name
* Installing persistence
* Launching various sub-modules to mount DDoS attacks, terminate competing processes, establish C2 channels over IRC, HTTP, DNS, and P2P, run scanners for Telnet, SSH, HTTP, and Android Debug Bridge (ADB), spawn a SOCKS5 proxy, and execute a cryptocurrency mining placeholder

The dedicated HTTP scanner, in particular, can manage up to 128 concurrent connections at any given point in time, operating with the goal of discovering vulnerable web interfaces. Persistence, on the other hand, is accomplished by means of a systemd service, cron entries, and a watchdog keepalive process to ensure TuxBot remains operational on the compromised machine.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

"Multiple files contain raw LLM chain-of-thought reasoning left verbatim in comments," Unit42 said. "These comments are the LLM's internal reasoning as it worked through porting tasks. This reasoning is complete with self-interruptions, decisions, and references to 'the user' (meaning the developer who prompted the LLM)."

Although TuxBot v3 Evolution is a botnet under development, the core working functions, coupled with its reliance on AI, signal accelerated integration of features, at the same time enabling what looks to be single developer to come up with a multi-pronged toolset with multiple C2 channels, a cust...