---
title: PyTorch Lightning and Intercom-client Hit in Supply Chain Attacks to Steal Credentials
url: https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html
source: The Hacker News
date: 2026-04-30
fetch_date: 2026-05-01T05:40:14.136293
---

# PyTorch Lightning and Intercom-client Hit in Supply Chain Attacks to Steal Credentials

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [PyTorch Lightning and Intercom-client Hit in Supply Chain Attacks to Steal Credentials](https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html)

**Ravie Lakshmanan**Apr 30, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7hiQfVCFzoPBzfr5xqJ06qMjzv-zw_qiUcDTgyEM8RbEVk3PDztg9U5Vlkgvz6j7nX8ODtXwnTCC2wB78lupEmRjcxJTz74GJGSslsMQM-e5b8vG0W2gLFnbEzYAPKw05ZelkaNfy50VyLJeb-3EhwiGKfIP9qHNRpNG4MnFUnTBBOJ95vRJb-RbcFVxX/s1700-e365/python.png)

In yet another software supply chain attack, threat actors have managed to compromise the popular Python package [Lightning](https://pypi.org/project/lightning/) to push two malicious versions to conduct credential theft.

According to [Aikido Security](https://www.aikido.dev/blog/pytorch-lightning-pypi-compromise-mini-shai-hulud), [OX Security](https://www.ox.security/blog/lightning-python-package-shai-hulud-supply-chain-attack/), [Socket](https://socket.dev/blog/lightning-pypi-package-compromised), and [StepSecurity](https://www.stepsecurity.io/blog/lightning-obfuscated-javascript-credential-stealer-bundled-in-pypi-wheel), the two malicious versions are versions 2.6.2 and 2.6.3, both of which were published on April 30, 2026. The campaign is assessed to be an extension of the [Mini Shai-Hulud supply chain incident](https://socket.dev/supply-chain-attacks/mini-shai-hulud) that targeted [SAP-related npm packages](https://thehackernews.com/2026/04/sap-npm-packages-compromised-by-mini.html) on Wednesday.

As of writing, the project has been quarantined by the administrators of the Python Package Index (PyPI) repository. PyTorch Lightning is an [open-source Python framework](https://github.com/Lightning-AI/pytorch-lightning) that provides a high-level interface for PyTorch. The open-source project has more than 31,100 stars on GitHub.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

"The malicious package includes a hidden \_runtime directory containing a downloader and an obfuscated JavaScript payload," Socket said. "The execution chain runs automatically when the lightning module is imported, requiring no additional user action after installation and import."

The attack chain paves the way for a Python script ("start.py"), which downloads and executes the Bun JavaScript runtime, and then uses it to run an 11MB obfuscated malicious payload ("router\_runtime.js") with an aimto conduct comprehensive credential theft.

From among the harvested credentials, the GitHub tokens are validated against the "api.github[.]com/user" endpoint before being used to inject a worm-like payload to up to 50 branches retrieved from every repository the token can write to.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicg-RRSQfbmXs_SU3PubaP7p6-vxK7VWnk1Zdnh24QJqW6E_VGy031cZLVi_FVxUaFbllUQ_nfPaRMu0EvJITiJkPvuDn_5VEqu4rnf34Vb5_2GMOsgFVtJS8Tr6ywPjRQOGuVevgkBQJNCheRagkxN6nO3VAwoV79gWAVqS2Sdk6_Q9y5et5UdGgHrElG/s1700-e365/oxaws.png)

"The operation is an upsert: it creates files that do not yet exist and silently overwrites files that do," Socket added. "No pre-check for existing content is performed. Every poisoned commit is authored using a hardcoded identity designed to impersonate Anthropic's Claude Code."

Separately, the malware implements an npm-based propagation vector that modifies the developer's local npm packages with a postinstall hook in the "package.json" file to invoke the malicious payload, increases the patch version number, and repacks the .tgz tarballs. Should the unsuspecting developer publish the tampered packages from their local environment, they are made available on npm, from where the malware ends up on downstream user systems.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGF1UnYtnSR1hwh3xiP_m-WgFgfEIJCg1Ga3JwkEG0rkrEURtRc-baEynn39iU9LKlItYfIYERz43SCmJuFCuS914BXOSD7U-4R7FsA3RHhN41u4Mm4KHIcS10yBywtWGLqEf_N598mqyz0pfhDcevOJPCmujS7qAKEBj0PPqbyW75IBW0E61TwvMzsjTm/s1700-e365/note.png)

The maintainers of the project have [acknowledged](https://github.com/Lightning-AI/pytorch-lightning/issues/21691) that "we are aware of the issue and are actively investigating." It's currently not clear how the incident occurred, but indications are that the project's GitHub account has been compromised.

In a [separate advisory](https://github.com/Lightning-AI/pytorch-lightning/security/advisories/GHSA-w37p-236h-pfx3), Lightning revealed an investigation is still underway to determine the exact root cause of the compromise and that the "affected versions have introduced functionality consistent with a credential harvesting mechanism."

In the interim, it's advised to block Lightning versions 2.6.2 and 2.6.3 and remove them from developer systems, if already installed. It's also essential to downgrade to the last known clean version, 2.6.1, and rotate credentials exposed in affected environments.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The supply chain attack is the latest addition to a long list of compromises carried out by a threat actor known as TeamPCP, which has now launched an onion website on the dark web after its account was [suspended from X](https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html) for violating the platform's rules.

It also called [LAPSUS$](https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html), a "good partner of ours and has been involved heavily throughout this entire operation." The group also made it a point to emphasize that it has "never used VECT encryption tools and we own CipherForce, our own private locker," following a [report from Check Point Research](https://thehackernews.com/2026/04/vect-20-ransomware-irreversibly.html) about vulnerabilities discovered in the ransomware's encryption process.

### Intercom npm Package Compromised as Part of Mini Shai-Hulud

In a related development, it has emerged that version 7.0.4 of [intercom-client](https://github.com/intercom/intercom-node) has been compromised as part of the Mini Shai-Hulud campaign, following a similar modus operandi as that of the [SAP packages](https://thehackernews.com/2...