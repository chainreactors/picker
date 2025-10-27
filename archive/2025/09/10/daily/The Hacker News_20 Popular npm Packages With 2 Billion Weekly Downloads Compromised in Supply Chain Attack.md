---
title: 20 Popular npm Packages With 2 Billion Weekly Downloads Compromised in Supply Chain Attack
url: https://thehackernews.com/2025/09/20-popular-npm-packages-with-2-billion.html
source: The Hacker News
date: 2025-09-10
fetch_date: 2025-10-02T19:56:16.650516
---

# 20 Popular npm Packages With 2 Billion Weekly Downloads Compromised in Supply Chain Attack

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

# [20 Popular npm Packages With 2 Billion Weekly Downloads Compromised in Supply Chain Attack](https://thehackernews.com/2025/09/20-popular-npm-packages-with-2-billion.html)

**Sep 09, 2025**Ravie LakshmananCryptocurrency / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtemm9XFX7C2s0emclL3-7RrQ5wLlQ2ltlzDI0sOVKMC8NirJxT9C9yMnNO0DrcwB6yDwsArFXsKik-k9b1FvWeelLcN3rwubVJnllQwDUwoEH4WkTuUOiU5wgLCBrSaHhvvx9MNaH0dFr8tt9oqnDfSFY_26Cy6r-Nhwnrr00QiUifziWejCo5vd5jyQ/s790-rw-e365/1000015719.jpg)

Multiple npm packages have been compromised as part of a software supply chain attack after a maintainer's account was compromised in a phishing attack.

The attack targeted Josh Junon (aka [Qix](https://www.npmjs.com/~qix)), who received an email message that mimicked npm ("support@npmjs[.]help"), urging them to update their update their two-factor authentication (2FA) credentials before September 10, 2025, by clicking on embedded link.

The phishing page is said to have prompted the co-maintainer to enter their username, password, and two-factor authentication (2FA) token, only for it to be stolen likely by means of an adversary-in-the-middle ([AitM](https://thehackernews.com/2024/11/phishing-as-service-rockstar-2fa.html)) attack and used to publish the rogue version to the npm registry.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The following 20 packages, which collectively attract over 2 billion weekly downloads, have been confirmed as affected as part of the incident -

* ansi-regex@6.2.1
* ansi-styles@6.2.2
* backslash@0.2.1
* chalk@5.6.1
* chalk-template@1.1.1
* color-convert@3.1.1
* color-name@2.0.1
* color-string@2.1.1
* debug@4.4.2
* error-ex@1.3.3
* has-ansi@6.0.1
* is-arrayish@0.3.3
* proto-tinker-wc@1.8.7
* supports-hyperlinks@4.1.1
* simple-swizzle@0.2.3
* slice-ansi@7.1.1
* strip-ansi@7.1.1
* supports-color@10.2.1
* supports-hyperlinks@4.1.1
* wrap-ansi@9.0.1

"Sorry everyone, I should have paid more attention," Junon [said](https://bsky.app/profile/bad-at-computer.bsky.social/post/3lydioq5swk2y) in a post on Bluesky. "Not like me; have had a stressful week. Will work to get this cleaned up."

An analysis of the obfuscated malware injected into the source code reveals that it's designed to intercept cryptocurrency transaction requests and swap the destination wallet address with an attacker-controlled wallet that closely matches it by computing the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE_fkk2Zjopp-wCb_wixER0DZtfKQCtNihGDrW-3sxNHtvCwxNGtQDQbz1aDH9VMPEDvG9NH1LqeEx8xDHanKCjknW4i9V4vDfdNggrN5yi6C2w_5pzIffbE2cBlczdA1L8gsvLaiVUdVOUfO3fLlm5QGDO46jTgLlkdOQdZZgg5iQfIYWrJrddhcAJK0/s790-rw-e365/1000015635.jpg)

According to Aikido Security's Charlie Eriksen, the payload [acts](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised) as a browser-based interceptor that hijacks network traffic and application APIs to steal cryptocurrency assets by rewriting requests and responses. It's currently not known who is behind the attack.

"The payload begins by checking typeof window !== 'undefined' to confirm it is running in a browser," Socket [said](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack). "It then hooks into window.fetch, XMLHttpRequest, and window.ethereum.request, along with other wallet provider APIs."

"This means the malware targets end users with connected wallets who visit a site that includes the compromised code. Developers are not inherently the target, but if they open an affected site in a browser and connect a wallet, they too become victims."

Package ecosystems like npm and the Python Package Index (PyPI) remain recurring targets due to their popularity and broad reach within the developer community, with attackers abusing the trust associated with these platforms to push malicious payloads.

Beyond publishing malicious packages directly, attackers have also employed techniques such as typosquatting or even exploiting AI-hallucinated dependencies – called [slopsquatting](https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html) – to trick developers into installing malware. The incident once indicates the need for exercising vigilance and hardening CI/CD pipelines and locking down dependencies.

According to ReversingLabs' 2025 [Software Supply Chain Security Report](https://www.reversinglabs.com/thank-you/sscs-report-thank-you), 14 of the 23 crypto-related malicious campaigns in 2024 targeted npm, with the remainder linked to PyPI.

"What we are seeing unfold with the npm packages chalk and debug is an unfortunately common instance today in the software supply chain," Ilkka Turunen, Field CTO at Sonatype, told The Hacker News.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The malicious payload was focused on crypto theft, but this takeover follows a classic attack that is now established – by taking over popular open source packages, adversaries can steal secrets, leave behind backdoors and infiltrate organizations."

"It was not a random choice to target the developer of these packages. Package takeovers are now a standard tactic for advanced persistent threat groups like Lazarus, because they know they can reach a large amount of the world's developer population by infiltrating a single under-resourced project."

### Supply Chain Attack Broadens

According to [Socket](https://socket.dev/blog/duckdb-npm-account-compromised-in-continuing-supply-chain-attack) and [Sonatype](https://www.sonatype.com/blog/npm-chalk-and-debug-packages-hit-in-software-supply-chain-attack), the npm supply chain attack that compromised Qix has also managed to claim another high-profile maintainer, duckdb\_admin, to distribute the same wallet-drainer malware. The list of affected packages is be...