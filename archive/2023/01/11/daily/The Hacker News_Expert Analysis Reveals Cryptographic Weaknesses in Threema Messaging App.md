---
title: Expert Analysis Reveals Cryptographic Weaknesses in Threema Messaging App
url: https://thehackernews.com/2023/01/expert-analysis-reveals-cryptographic.html
source: The Hacker News
date: 2023-01-11
fetch_date: 2025-10-04T03:34:56.232845
---

# Expert Analysis Reveals Cryptographic Weaknesses in Threema Messaging App

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Expert Analysis Reveals Cryptographic Weaknesses in Threema Messaging App](https://thehackernews.com/2023/01/expert-analysis-reveals-cryptographic.html)

**Jan 10, 2023**Ravie LakshmananPrivacy / Encryption

[![Threema Messaging App](data:image/png;base64... "Threema Messaging App")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpaE_D5nfmlvXEHXDjvdPSmY2PacrnU08gK7a-BRzKtrb_7jwUeJgxCO2szrK0AObUq6et7nk_nvMB-RarmpXHoipNxH2C_rxDfzzZ-tA6INCN1bmAtF8ufShWIf0RkKqaiWvgDLPZ6EMtxMXbztGlRH-lsenG13wDb79Y-zr4IWxQXGzEBgCiatoH/s790-rw-e365/hacking.png)

A comprehensive analysis of the cryptographic protocols used in the Swiss encrypted messaging application Threema has revealed a number of loopholes that could be exploited to break authentication protections and even recover users' private keys.

The seven attacks span three different threat models, [according](https://breakingthe3ma.app/) to ETH Zurich researchers Kenneth G. Paterson, Matteo Scarlata, and Kien Tuong Truong, who reported the issues to Threema on October 3, 2022. The weaknesses have since been addressed as part of [updates](https://threema.ch/en/versionhistory) released by the company on November 29, 2022.

Threema is an encrypted messaging app that's used by more than 11 million users as of October 2022. "Security and privacy are deeply ingrained in Threema's DNA," the company [claims](https://threema.ch/en/about) on its website.

Officially used by the Swiss Government and the Swiss Army, it's also advertised as a secure alternative alongside other services such as Signal, Meta-owned WhatsApp, and Telegram.

While Threema has been subjected to [third-party code audits](https://threema.ch/en/faq/code_audit/) at least twice – once in 2019 and a second time in 2020 – the latest findings show that they weren't thorough enough to uncover the problems present in the "cryptographic core of the application."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Ideally, any application using novel cryptographic protocols should come with its own formal security analyses (in the form of security proofs) in order to provide strong security assurances," the researchers said.

In a nutshell, the attacks could pave the way for a wide range of exploitation scenarios, namely allowing an attacker to impersonate a client, reorder the sequence of messages exchanged between two parties, clone the account of a victim user, and even leverage the backup mechanism to recover the user's private key.

The latter two attack pathways, which require direct access to a victim's device, could have severe consequences, as it enables the adversary to stealthily access the users' future messages without their knowledge.

Also uncovered is a case of [replay](https://en.wikipedia.org/wiki/Replay_attack) and reflection attack related to its Android app that occurs when users reinstall the app or change devices, granting a bad actor with access to Threema servers to replay old messages. A [similar replay attack](https://www.computer.org/csdl/proceedings-article/euros%26p/2018/422801a415/12OmNzFv4aX) was identified in January 2018.

Last but not least, an adversary could also stage what's called a Kompromat attack wherein a malicious server tricks a client "into unwittingly encrypting a message of the server's choosing that can be delivered to a different user."

It's worth noting that this attack was previously reported to Threema by University of Erlangen-Nuremberg researcher Jonathan Krebs, prompting the company to [ship fixes](https://threema.ch/en/versionhistory) in December 2021 (version 4.62 for Android and version 4.6.14 for iOS).

"Using modern, secure libraries for cryptographic primitives does not, on its own, lead to a secure protocol design," the researchers said. "Libraries such as [NaCl](https://nacl.cr.yp.to/) or [libsignal](https://en.wikipedia.org/wiki/Signal_Protocol) can be misused while building more complex protocols and developers must be wary not to be lulled into a false sense of security."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"While the mantra 'don't roll your own crypto' is now widely known, it should be extended to 'don't roll your own cryptographic protocol' (assuming one already exists that meets the developer's requirements)," they added. "In the case of Threema, the bespoke C2S protocol could be replaced by [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)."

When reached for comment, Threema told The Hacker News that it has released a new communication protocol called **[Ibex](https://threema.ch/en/blog/posts/ibex)** that renders "some of the issues obsolete," adding it "acted instantly to implement fixes for all findings within weeks."

"While some of the findings [...] may be interesting from a theoretical standpoint, none of them ever had any considerable real-world impact," the company further [noted](https://threema.ch/en/blog/posts/news-alleged-weaknesses-statement). "Most assume extensive and unrealistic prerequisites that would have far greater consequences than the respective finding itself."

It also pointed out that some of the attacks bank on having physical access to an unlocked mobile device over an extended time period, at which point the "entire device must be considered compromised."

The study arrives almost six months after ETH Zurich researchers [detailed](https://thehackernews.com/2022/06/researchers-uncover-ways-to-break.html) critical shortcomings in the MEGA cloud storage service that could be weaponized to crack the private keys and fully compromise the privacy of the uploaded files.

Then in September 2022, another group of researchers [disclosed](https://nebuchadnezzar-megolm.github.io/) a host of [security flaws](https://arstechnica.com/information-technology/2022/09/matrix-patches-vulnerabilities-that-completely-subvert-e2ee-guarantees/) in the [Matrix](https://matrix.org/docs/guides/introduction) decentralized, real-time co...