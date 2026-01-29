---
title: Fake Python Spellchecker Packages on PyPI Delivered Hidden Remote Access Trojan
url: https://thehackernews.com/2026/01/fake-python-spellchecker-packages-on.html
source: The Hacker News
date: 2026-01-28
fetch_date: 2026-01-29T04:06:00.545349
---

# Fake Python Spellchecker Packages on PyPI Delivered Hidden Remote Access Trojan

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

# [Fake Python Spellchecker Packages on PyPI Delivered Hidden Remote Access Trojan](https://thehackernews.com/2026/01/fake-python-spellchecker-packages-on.html)

**Ravie Lakshmanan**Jan 28, 2026Supply Chain Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDmO6wqQYQf9Jzy85AeKQArxw_sFT_Qyd30NJ2Fxfs6FN6MgxQDuyTmUnlyThYj_4a4BN0bsejx2owRMl6_rLwiCpgh_WGWVH80OezW3ToFf2Aedn9a-023kI71i4NwG7HQ5tZ2So97M4N4jkTXKqRnlty7V10DsQeQ6UIPC7jIRrCNzSd6p1KfKKx_9m_/s1700-e365/python.jpg)

Cybersecurity researchers have discovered two malicious packages in the Python Package Index (PyPI) repository that masquerade as spellcheckers but contain functionality to deliver a remote access trojan (RAT).

The packages, named **spellcheckerpy** and **spellcheckpy**, are no longer available on PyPI, but not before they were collectively downloaded a little over 1,000 times.

"Hidden inside the Basque language dictionary file was a base64-encoded payload that downloads a full-featured Python RAT," Aikido researcher Charlie Eriksen [said](https://www.aikido.dev/blog/malicious-pypi-packages-spellcheckpy-and-spellcheckerpy-deliver-python-rat). "The attacker published three 'dormant' versions first, payload present, trigger absent, then flipped the switch with spellcheckpy v1.2.0, adding an obfuscated execution trigger that fires the moment you import SpellChecker."

Unlike other packages that conceal the malicious functionality within "\_\_init\_\_.py" scripts, the threat actor behind the campaign has been found to add the payload inside a file named "resources/eu.json.gz" that contains Basque word frequencies from the legitimate pyspellchecker package.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

While the package appears harmless at first glance, the malicious behavior is triggered when the archive file is extracted using the test\_file() function with the parameters: test\_file("eu", "utf-8", "spellchecker"), causing it to retrieve a Base64-encoded downloader hidden in the dictionary under a key called "spellchecker."

Interestingly, the first three versions of the package only fetched and decoded the payload, but never executed it. However, that changed with the release of spellcheckpy version 1.2.0, published on January 21, 2026, when it gained the ability to run the payload as well.

The first stage is a downloader that's designed to retrieve a Python-based RAT from an external domain ("updatenet[.]work"). It's capable of fingerprinting the compromised host, parsing incoming commands, and executing them. The domain, registered in late October 2025, is associated with 172.86.73[.]139, an IP address managed by RouterHosting LLC (aka Cloudzy), a hosting provider that has a [history](https://www.halcyon.ai/blog/update-cloudzy-command-and-control-provider-report) of offering its services to nation-state groups.

This is not the first time fake Python spell-checking tools have been detected in PyPI. In November 2025, HelixGuard [said](https://thehackernews.com/2025/11/legacy-python-bootstrap-scripts-create.html) it discovered a malicious package named "spellcheckers" that featured the ability to retrieve and execute a RAT payload. It's suspected that these two sets of attacks are the work of the same threat actor.

The development coincides with the discovery of several malicious npm packages to facilitate data theft and target cryptocurrency wallets -

* flockiali (1.2.3-1.2.6), opresc (1.0.0), prndn (1.0.0), oprnm (1.0.0), and operni, which [contain](https://www.aikido.dev/blog/npm-supply-chain-phishing-campaigns) a single JavaScript file that, when loaded, serves a fake Microsoft-branded login screen as part of a [targeted spear-phishing campaign](https://thehackernews.com/2025/12/27-malicious-npm-packages-used-as.html) hitting employees at specific industrial and energy companies located in France, Germany, Spain, the U.A.E, and the U.S. with malicious links

* ansi-universal-ui (1.3.5, 1.3.6, 1.3.7, 1.4.0, 1.4.1), which masquerades as a UI component library but deploys a Python-based stealer dubbed [G\_Wagon](https://www.aikido.dev/blog/npm-malware-g-wagon-python-stealer-crypto-wallets) that exfiltrates web browser credentials, cryptocurrency wallets, cloud credentials, and Discord tokens to an Appwrite storage bucket

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The disclosure also comes as Aikido highlighted the threat associated with [slopsquatting](https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html), wherein artificial intelligence (AI)-powered agents can hallucinate non-existent packages that could then be claimed by a threat actor to push malicious code to downstream users.

In one case highlighted by the supply chain security company, it has been found that a fictitious npm package named "react-codeshift" is referenced by 237 GitHub repositories since it was made up by a large language model in mid-October 2025, with some of them even instructing AI agents to install it.

"How did it spread to 237 repos? Agent skill files. Copy-pasted, forked, translated into Japanese, never once verified," Eriksen [said](https://www.aikido.dev/blog/agent-skills-spreading-hallucinated-npx-commands). "Skills are the new code. They don't look like it. They're Markdown and YAML and friendly instructions. But they're executable. AI agents follow them without asking, 'Does this package actually exist?'"

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[a...