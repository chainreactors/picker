---
title: Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures
url: https://thehackernews.com/2026/07/ousaban-banking-trojan-targets-iberian.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:21.661250
---

# Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures

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

# [Ousaban Banking Trojan Targets Iberian Bank Users with Fake PDF Lures](https://thehackernews.com/2026/07/ousaban-banking-trojan-targets-iberian.html)

**Swati Khandelwal**Jul 01, 2026Endpoint Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3GnjevIMTqO1nAZ7LWeRKAz2NCKGTKCC2ldSx5dsd2SShjh4pWcmddVJse4MP4QLhA_DOP1K_RajPwe8YR7rc57CqPUO0i9RDYoZQA0yRAokZt1r2hyphenhyphenccOjcFh2SgUTnyUjj-M-y7WUUXVF0rpSrcxTrjb5nPOnpnIP5YvdxzUaLXkubSTXFaj0RzxEvH/s1700-e365/windows-trojan.jpg)

A Brazilian banking trojan called **Ousaban** is going after Windows users who bank in Spain and Portugal. [Fortinet's FortiGuard Labs](https://www.fortinet.com/blog/threat-research/analysis-of-ongoing-ousaban-attacks-targeting-the-iberian-peninsula) identified the campaign in May 2026.

It opens with a phishing PDF disguised as a corrupted file, checks that the visitor is really in Spain or Portugal, and hides its real payload inside an image.

The goal is the usual one: steal banking logins and take over accounts.

Ousaban sits quietly on a Windows PC and waits for the user to open a banking site. When a target bank loads, it can capture screenshots and keystrokes, tamper with the clipboard, show fake messages, and give the attacker remote control.

Together, those are the tools for hijacking a live banking session and taking over an account. Ousaban watches for more than two dozen banks across the two countries, among them Banco Santander, BBVA, CaixaBank, Bankinter, and Caixa Geral de Depósitos.

## How the attack works

It starts with a phishing PDF disguised as a corrupted file. The PDF shows a prompt telling the victim to press an "Atualizar" (Update) button, which opens a malicious webpage.

Hidden JavaScript in the PDF can open the same page on its own. The page poses as a tax-document and installer portal while screening visitors. Fortinet says an earlier version ran these checks in the browser: it looked at the visitor's IP address, language, and time zone, blocked anyone coming through a VPN, and filtered out automated security tools by checking details like screen size and installed fonts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The current version moves that screening to the operator's server, so the exact rules are hidden. Either way, visitors outside Spain or Portugal get a Spanish "access denied" notice instead of malware.

Clear the check, and the download starts. A script downloads an image that looks like a PDF icon but hides a ZIP file inside, a trick called steganography. The script unpacks Ousaban from that ZIP, runs it, then deletes the image, the ZIP, and itself to leave less behind. Once running, Ousaban adds a registry entry named Financeiro (Portuguese for "finance") so it starts up with Windows.

Ousaban's command server, the machine that controls it, is deliberately hard to find. It carries a Pastebin link that points to one server address, but Fortinet says that address is a decoy.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD7P5AJa9slw6tFG6anN4SxfIoYW32CE_MPCM0om39nleRscm8dgL5e9qAOAx-Jl2nOJ3mfn7upgIFKiSh_qXXkgHYuXAyBeWGJQaCThu0KmRiwFgV7WSa9BFQCrAQPeER4s6IFU1psIYDnRV6fy0dnqt4lAvoyyazXntE7HMdgTT25j8XduEURPAt4wD4/s1700-e365/pdf.png)

Hiding these details in web services is an old Ousaban habit: earlier campaigns stashed the [configuration in Google Docs](https://thehackernews.com/2024/02/banking-trojans-target-latin-america.html). This time, the real server moves every day. The malware reads the current date off a Google page, builds a web address from that date plus a fixed secret, and looks it up. Blocking yesterday's address does little good.

## A familiar Brazilian playbook

None of this is new. Ousaban, also tracked as Javali, is one of a group of Brazilian banking trojans that Kaspersky labeled years ago as the ["Tetrade,"](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/) alongside Grandoreiro, Guildma, and Melcoz.

These families started in Brazil and pushed into Spain and Portugal, borrowing code from each other as they went; Ousaban's string encryption is the same custom scheme used by another family, Casbaneiro.

Grandoreiro, the best known of the group, shows how durable the playbook is. It survived an [Interpol-coordinated takedown](https://www.interpol.int/en/News-and-Events/News/2024/Disrupting-a-Grandoreiro-malware-operation) in January 2024 and [was back within months](https://thehackernews.com/2024/05/grandoreiro-banking-trojan-resurfaces.html), and its loaders leaned on the same habit of hiding downloads behind PDF-looking lures and country checks.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

It is [still active against Iberian targets](https://thehackernews.com/2026/05/grandoreiro-malware-and-btmob-rat.html), with a campaign reported this year that kept hitting Portuguese banks. Fortinet links the same infrastructure to Ousaban activity in late 2025 that used other entry points, including "ClickFix," a scam that gets the victim to paste a malicious command themselves while thinking they are fixing an error.

## What to do

The first place to catch it is the lure. Treat any PDF or email that claims a file is corrupted and tells you to press "Update" as hostile. The same goes for prompts that tell users to paste a command to fix an "error." The PDF can even open the malicious page on its own.

Treat unexpected invoice, factura, or tax-document attachments as suspect, especially in Spain and Portugal.

Server-side screening means that an automated sandbox that just fetches the link may get only the Spani...