---
title: Brazil Hit by Banking Trojan Spread via WhatsApp Worm and RelayNFC NFC Relay Fraud
url: https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html
source: The Hacker News
date: 2025-12-03
fetch_date: 2025-12-04T03:19:40.546757
---

# Brazil Hit by Banking Trojan Spread via WhatsApp Worm and RelayNFC NFC Relay Fraud

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

# [Brazil Hit by Banking Trojan Spread via WhatsApp Worm and RelayNFC NFC Relay Fraud](https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html)

**Dec 03, 2025**Ravie LakshmananBanking Security / Malware

[![Banking Trojan Spread via WhatsApp](data:image/png;base64... "Banking Trojan Spread via WhatsApp")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaXJGSuca7TOkhpzQSqTtJJWkuBbFzjkm6UDnl04TARRIVqKOvnJmtLCysj9BEt7zm7QmU8RZMFjwiGnVOQUKIxvVle841t-4dv7YGs8Rx4qo9cvYQApnnJnAhmG419Xy-d0_nI8URsb8IQpXQpfBFD5nlOiADT0Mp0ZW0Ze-rxNvgCuQIAGTgNZovCBTN/s790-rw-e365/brazil-malware.jpg)

The threat actor known as **[Water Saci](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html)** is actively evolving its tactics, switching to a sophisticated, highly layered infection chain that uses HTML Application (HTA) files and PDFs to propagate via WhatsApp a worm that deploys a banking trojan in attacks targeting users in Brazil.

The latest wave is characterized by the attackers shifting from PowerShell to a Python-based variant that spreads the malware in a worm-like manner over WhatsApp Web.

"Their new multi-format attack chain and possible use of artificial intelligence (AI) to convert propagation scripts from PowerShell to Python exemplifies a layered approach that has enabled Water Saci to bypass conventional security controls, exploit user trust across multiple channels, and ramp up their infection rates," Trend Micro researchers Jeffrey Francis Bonaobra, Sarah Pearl Camiling, Joe Soares, Byron Gelera, Ian Kenefick, and Emmanuel Panopio [said](https://www.trendmicro.com/en_us/research/25/l/water-saci.html).

In these attacks, users receive messages from trusted contacts on WhatsApp, urging them to interact with malicious PDF or HTA attachments and activate the infection chain and ultimately drop a banking trojan that can harvest sensitive data. The PDF lure instructs victims to update Adobe Reader by clicking on an embedded link.

Users who receive HTA files are deceived into executing a Visual Basic Script immediately upon opening, which then runs PowerShell commands to fetch next-stage payloads from a remote server, an MSI installer for the trojan and a Python script that's responsible for spreading the malware via WhatsApp Web.

"This newly observed variant allows for broader browser compatibility, object-oriented code structure, enhanced error handling, and faster automation of malware delivery through WhatsApp Web," Trend Micro said. "Together, these changes make propagation faster, more resilient to failure, and easier to maintain or extend."

The MSI installer, for its part, serves as a conduit for delivering the banking trojan using an AutoIt script. The script also runs checks to ensure that only one instance of the trojan is running at any given point of time. It accomplishes this by verifying the presence of a marker file named "executed.dat." If it does not exist, the script creates the file and notifies an attacker-controlled server ("manoelimoveiscaioba[.]com").

Other AutoIt artifacts uncovered by Trend Micro have also been found to verify whether the Windows system language is set to Portuguese (Brazil), proceeding further to scan the infected system for banking-related activity only if this criteria is met. This includes checking for folders related to major Brazilian banking applications, security, and anti-fraud modules, such as Bradesco, Warsaw, Topaz OFD, Sicoob, and Itaú.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

It's worth noting Latin America (LATAM)-focused banking trojans like [Casbaneiro](https://thehackernews.com/2023/07/casbaneiro-banking-malware-goes-under.html) (aka Metamorfo and Ponteiro) have [incorporated similar features](https://thehackernews.com/2025/06/malicious-browser-extensions-infect-722.html) as far back as 2019. Furthermore, the script analyzes the user's Google Chrome browsing history to search visits to banking websites, specifically a hard-coded list comprising Santander, Banco do Brasil, Caixa Econômica Federal, Sicredi, and Bradesco.

The script then proceeds to another critical reconnaissance step that involves checking for installed antivirus and security software, as well as harvesting detailed system metadata. The main functionality of the malware is to monitor open windows and extract their window titles to compare them against a list of banks, payment platforms, exchanges, and cryptocurrency wallets.

If any of these windows contain keywords related to targeted entities, the script looks for a TDA file dropped by the installer and decrypts and injects it into a hollowed "svchost.exe" process, following which the loader searches for an additional DMP file containing the banking trojan.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbmy6fEHz-iFF5MMQSQFHzF0ue1mAtXMx6Irq4N96z2AQW_jcG1KzUli3rw1ET_19InO353l0i4nerGhGu8rjxnEWgzkCKcNU5eAwPy3ZYe4PgNifhGbq2Yjam2GRIwuzrSZSs55SEP4xStpA_wPmd5VgAiwaczW0yc3S_cswOKdR4o_dLCo3Bv850Dws3/s2600/phish.jpg)

"If a TDA file is present, the AutoIt script decrypts and loads it as an intermediate PE loader (Stage 2) into memory," Trend Micro explained. "However, if only a DMP file is found (no TDA present), the AutoIt script bypasses the intermediate loader entirely and loads the banking trojan directly into the AutoIt process memory, skipping the process hollowing step and running as a simpler two-stage infection."

Persistence is achieved by constantly keeping tabs on the newly spawned "svchost.exe" process. Should the process be terminated, the malware starts afresh and waits to re-inject the payload the next time the victim opens a browser window for a financial service that's targeted by Water Saci.

The attacks stand out for a major tactical shift. The banking trojan deployed is not Maverick, but rather a malware that exhibits structural and behavioral continuity with Casbaneiro. This assessment is based on the AutoIt-based delivery and loader m...