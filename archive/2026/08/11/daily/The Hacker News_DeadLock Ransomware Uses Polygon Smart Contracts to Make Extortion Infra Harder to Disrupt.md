---
title: DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt
url: https://thehackernews.com/2026/08/deadlock-ransomware-uses-polygon-smart.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:49.420990
---

# DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt

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

# [DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt](https://thehackernews.com/2026/08/deadlock-ransomware-uses-polygon-smart.html)

**Ravie Lakshmanan**Aug 11, 2026Ransomware / Blockchain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHe7Kt8X_4eEC2ICocbCp-eg1Vs7xknMUYEnZzepw5j6mg7v7C7DmPvzf4S-Z4wGhofTJco3eW95xPm3x7nDEzdfF9dpJAEriyIAGsXqNcLT02br6Em30kPnD5vYp4CrHHAR8TvvNr6glr8mIeRwhPANZqTSG7w_tR1-8QUNgYWg4AXgVPrmob7CFzwLmA/s1700-e365/deadlock.jpg)

The ransomware group known as **DeadLock** has been observed using decentralized infrastructure to facilitate victim communications and data leak operations in a bid to improve operational resilience.

"Its recovery ecosystem combines the Session messaging network with blockchain-backed services that store and deliver resources used throughout the extortion process," the Microsoft Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/).

The tech giant said it observed the ransomware being deployed by multiple threat actors, including an affiliate for Lynx and INC ransomware.

DeadLock was first detected in July 2025, employing double extortion tactics to encrypt victim environments and apply pressure by threatening to publicly release exfiltrated data. As of this month, the group has [claimed 96 victims](https://ransomware.live/group/Deadlock), with most of them located in Italy, Spain, Poland, Türkiye, and the U.S.

In an analysis published earlier this January, Singapore-headquartered Group-IB [said](https://www.group-ib.com/blog/deadlock-ransomware-polygon-smart-contracts/) the group has managed to keep a lower profile than its peers owing to it not being associated with any known affiliate programs and for lacking a data leak site (DLS). According to Ransomware.Live, the first set of victims was not discovered until late May 2026.

Attacks mounted by the group are known to encrypt files with the ".dlock" extension, change file icons using a custom ".ico" file written to disk, and modify the victim's desktop wallpaper to display the message "Your infrastructure DeadLocked" and instruct them to open the ransom note.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The ransomware adopts a selective encryption model to exclude certain directories, file extensions, and file names from encryption. It employs a hybrid cryptographic design that combines Curve25519 elliptic-curve cryptography with the XChaCha20 stream cipher for file encryption.

The ransom note urges the victim to download a decentralized, end-to-end encrypted messaging application called Session to get in touch and make a Bitcoin or Monero payment after sharing a decrypted version of a locked file as proof. One version of the ransom note also claims to provide the compromised company with a "security report" that details the steps the attackers took to break into their network.

Furthermore, the note states that victims who make a payment will receive security recommendations to stop future attacks, along with assurances that they will not be targeted again in the future.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfBiMlLI9HhrrAMtKC1-ucVWhPTyHVHXTfwvHQeQEK5j195xKeK8yliNYb_MQyU02qZci0tLcLqJxCokJVuCFK6qV4nMqoFV20eDVLIekZu3w_AtU2NU6nTR-gPnVKt-bmRI8hNVXF315FViCPlzXnjnadf1WQ_g3j_gndaszpun0Rc6jliijfqa26FRdp/s1700-e365/ms.jpg) |
| HTML recovery chat infrastructure summary |

Another important feature is its implementation of a language- or country-based geofencing to avoid execution in environments associated with former Soviet and Commonwealth of Independent States (CIS)-linked countries as well as select Middle Eastern countries.

Separately, it includes a "resource-aware throttling mechanism" that ensures system responsiveness as the encryption process is underway and pauses it when memory usage exceeds 29% or CPU load exceeds 70%, while relying on AnyDesk for remote control of compromised hosts. For defense evasion and minimizing forensic evidence, it systematically erases logs and disables logging via Registry manipulation to prevent recording future events.

The Windows version of the locker uses a PowerShell script to stop services that are not allowlisted and ensure they are not executed automatically after reboot. The script is also responsible for deleting Volume Shadow Copies and erasing itself in an attempt to cover its tracks. As a final cleanup step post successful encryption, the malware creates a batch script to delete its own binary from disk and then remove itself.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdPNKBQqUmLF1D4vVPe80rtINtyEfv4DJRlLeqaLhs3Dg-jqW70KogLZ5fuuY-bC8CQ-5azeQSdH5vIhVgmAULO0bymMeBFssYq8XXXqLwYTvhh3dbsAxyKtx0RuRoeWsO2A4yDyXgjmeNmGjmSQi-72xjgXhXaAQbQbuiW_V11s7myA0mdhf0spyWUMJE/s1700-e365/note.jpg)

Perhaps the most unusual aspect of the ransomware is its use of an HTML note ("RECOVERY\_CHAT.<UID>.html") that's dropped in all drive root directories and all Desktop folders.

"Unlike the text note, the HTML note is a full interactive web application with a self-contained single-page application that implements end-to-end encrypted chat, a paginated data leak blog, and a file browser, all without requiring a traditional backend server," Microsoft said.

The purpose of the HTML file, as previously highlighted by Group-IB, is to facilitate direct communications between the DeadLock operator and the victim as an alternative to downloading the Session app. The HTML file sends and receives messages from a server that acts as a proxy, the details of which are retrieved and managed using a blockchain-based approach.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Specifically, this involves using JavaScript code within the HTML file that interacts with Polygon smart contracts for decentralized proxy server address rotation, turning them into a censorship- and takedown-resistant infrastructure that allows the operator to update the proxy URL without hav...