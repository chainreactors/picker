---
title: Why Post-Quantum Cryptography Starts With Credentials
url: https://thehackernews.com/2026/06/why-post-quantum-cryptography-starts.html
source: The Hacker News
date: 2026-06-29
fetch_date: 2026-06-30T06:10:13.580806
---

# Why Post-Quantum Cryptography Starts With Credentials

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

# [Why Post-Quantum Cryptography Starts With Credentials](https://thehackernews.com/2026/06/why-post-quantum-cryptography-starts.html)

**The Hacker News**Jun 29, 2026Quantum Computing / Non-Human Identity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgufw7UrtG2RgRTMvdhUaNVywdIBuSIRFLngtWMIY_3fzq7gzTZnlL7KMi_kzPhfpdny4vP5Rd9QVLpkX9xR5Vpk0cVvDV8Xsy4wljRyA5TjKvojsoBsYJt7yhhk1VK46OegGewBgqi-c41Z5mX5Ivos1PMrgrrmgLZKUJ8hqb4xl8o85sB7jQJLvI3gj0/s1700-e365/keeper.jpg)

Today’s encrypted data, such as credentials, may no longer remain confidential in the future because the public-key cryptography protecting it will soon be broken by quantum computers. Although no machine today can break [elliptic curve cryptography](https://www.keepersecurity.com/blog/2023/06/07/what-is-elliptic-curve-cryptography/) or RSA, quantum hardware is advancing rapidly and will inevitably change how organizations protect their data. Ciphertext and credentials captured by attackers can now be stored and decrypted as soon as quantum computing catches up.

## How urgent is quantum-resistant cryptography?

The [Global Risk Institute’s 2025 Quantum Threat Timeline report](https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/) shows that surveyed security specialists believe a cryptographically relevant quantum computer is likely to be available within 15 years, with 51-70% indicating so. The threat dates back to 1994, when Peter Shor proved that a powerful quantum computer could efficiently factor large numbers and compute discrete logarithms. However, Shor’s algorithm applies to public-key cryptography, posing no meaningful threat to symmetric encryption like AES-256 or modern hashing. This distinction matters because public-key cryptography is what two systems use to establish trust and agree on the keys that protect their data. If a quantum computer can break that step, the attacker can unlock the protected data and credentials behind it.

What makes the quantum threat relevant today, rather than solely in the future, is a tactic known as Harvest Now, Decrypt Later, in which an attacker captures encrypted traffic today, stores it, then decrypts it when a quantum computer is available. With a capable quantum computer plausibly available within 15 years, any data intercepted and harvested today should be treated as data already exposed.

### Q-day deadlines

Even though it’s unclear exactly when a quantum computer will arrive, government agencies are setting deadlines around the milestone known as Q-day for when cryptography must change. NSA’s Commercial National Security Algorithm Suite 2.0 will require new national security systems to start supporting quantum-resistant algorithms starting January 1, 2027. While deadlines are staggered for various system categories throughout the early 2030s, the NSA hopes to make all national security systems quantum-resistant by 2035. NIST is moving on a parallel track with its draft IR 8547, which deprecates RSA-2048 and ECC P-256 after 2030 and disallows them entirely after 2035. These dates may seem far away, but a full enterprise transition could take 5 to 15 years, since the discovery phase alone can take 1 to 2 years in large enterprises.

## Why credentials carry major risk in a post-quantum future

Not all encrypted data within an organization carries the same risk when the cryptography protecting it eventually becomes obsolete. Most secrets, like session tokens, have a confidentiality lifetime measured in months; credentials may persist for years or as long as their associated systems remain in service. To attackers, that makes credentials worth harvesting now and holding onto until a quantum computer can decrypt them. What makes this a major security risk is scale, especially since most organizations have growing populations of Non-Human Identities (NHIs) like service accounts and API keys. These machine credentials tend to be long-lived because no human user is responsible for rotating them, and they likely have not been inventoried for cryptographic exposure, making them ideal targets for harvesting.

## How to start a credentials-first quantum migration

Since most of the risk is concentrated in credentials, the migration should begin with them as well. Organizations should take a credentials-first approach to quantum migration by doing the following.

### Inventory existing cryptography

The main reason migrations are such lengthy processes is that organizations cannot itemize their cryptographic dependencies. A credentials-first inventory begins with finding the systems that hold or broker secrets, including password managers, secrets managers and Privileged Access Management (PAM) platforms. This phase is likely to expose forgotten service accounts, hardcoded secrets or integrations that have been dormant for years.

### Prioritize risk over size

While organizations may want to start protecting their largest systems, it is smarter to prioritize confidentiality lifetime based on exposure, like how long a secret must remain private, combined with how reachable it is to an attacker. With this logic, a small, long-lived secret that brokers access to critical systems outweighs a vast but short-lived dataset. Prioritizing risk this way ensures the credentials most vulnerable to Harvest Now, Decrypt Later are secured first.

### Migrate to hybrid cryptography

Instead of replacing classical algorithms outright, organizations should adopt hybrid cryptography by combining a classical algorithm with a quantum-resistant one in the same key exchange. This keeps a connection protected against both today’s traditional attackers and future quantum attackers. Hybrid cryptography also prevents organizations from betting everything on a single, relatively new algorithm, since the classical component remains in place and nothing is removed to add quantum-resistant protection.

### Build for crypto-agility

Given that algorithms get d...