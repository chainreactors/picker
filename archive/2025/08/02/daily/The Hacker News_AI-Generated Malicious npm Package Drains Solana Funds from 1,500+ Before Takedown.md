---
title: AI-Generated Malicious npm Package Drains Solana Funds from 1,500+ Before Takedown
url: https://thehackernews.com/2025/08/ai-generated-malicious-npm-package.html
source: The Hacker News
date: 2025-08-02
fetch_date: 2025-10-07T00:52:22.394578
---

# AI-Generated Malicious npm Package Drains Solana Funds from 1,500+ Before Takedown

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

# [AI-Generated Malicious npm Package Drains Solana Funds from 1,500+ Before Takedown](https://thehackernews.com/2025/08/ai-generated-malicious-npm-package.html)

**Aug 01, 2025**Ravie LakshmananMalware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKTBrsZjpi5rp4-0Vr15rSWfPez24p7MktzJnzb-ES3wWuxinrTP00pS6GhlhTzYii6VkOo2T3oQecWCyTPXBksGJVtXKoujySt7by-IbUtFM5OrnZep3fIc6mW8uP-xtunCGkKfjg8L5r6gkwuJHcmUuJ7uX_boz78Wd6gws9MlDzlm7uI1FkZQwW7jJS/s790-rw-e365/npm-malware.jpg)

Cybersecurity researchers have flagged a malicious npm package that was generated using artificial intelligence (AI) and concealed a cryptocurrency wallet drainer.

The package, @kodane/patch-manager, claims to offer "advanced license validation and registry optimization utilities for high-performance Node.js applications." It was uploaded to npm by a user named "Kodane" on July 28, 2025. The package is no longer available for download from the registry, but not before it attracted over 1,500 downloads.

Software supply chain security company Safety, which [discovered](https://getsafety.com/blog-posts/threat-actor-uses-ai-to-create-a-better-crypto-wallet-drainer) the library, said the malicious features are advertised directly in the source code, calling it an "enhanced stealth wallet drainer."

Specifically, the behavior is triggered as part of a postinstall script that drops its payload within hidden directories across Windows, Linux, and macOS systems, and then proceeds to connect to a command-and-control (C2) server at "sweeper-monitor-production.up.railway[.]app."

"The script generates a unique machine ID code for the compromised host and shares that with the C2 server," Paul McCarty, head of research at Safety, said, noting that the C2 server lists two compromised machines.

In the npm ecosystem, postinstall scripts are often overlooked attack vectors—they run automatically after a package is installed, meaning users can be compromised without ever executing the package manually. This creates a dangerous blind spot, especially in CI/CD environments where dependencies are updated routinely without direct human review.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware is designed to scan the system for the presence of a wallet file, and if found, it proceeds to drain all funds from the wallet to a hard-coded wallet address on the Solana blockchain.

While this is not the first time [cryptocurrency drainers](https://thehackernews.com/2025/06/malicious-pypi-npm-and-ruby-packages.html) have been [identified](https://thehackernews.com/2025/06/malicious-pypi-package-masquerades-as.html) in open-source repositories, what makes @kodane/patch-manager stand out are clues that suggest the use of Anthropic's Claude AI chatbot to generate it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhI1PmXDbzvyf6sxmVffyhaAyI3jxSBRyNgSgP2_m7vJdx36g_U3iC6eo9zBR_IkLAIXyebwBouTq5AKx_THMYebZVEBnkzQ_8JyNVS7XVpBiPNLYWJvv-SOURhombIxlbQaLQsWmqb73FY5BThGlC3MiuTJDNfFa_mF_Z0HG0lQtlRKteBhigFy_bG2V2/s790-rw-e365/solana.png)

This includes the presence of emojis, extensive JavaScript console logging messages, well-written and descriptive comments, the README.md markdown file written in a style that's consistent with Claude-generated markdown files, and Claude's pattern of calling code changes as "Enhanced."

The discovery of the npm package highlights "how threat actors are leveraging AI to create more convincing and dangerous malware," McCarty said.

The incident also underlines growing concerns in software supply chain security, where AI-generated packages may bypass conventional defenses by appearing clean or even helpful. This raises the stakes for package maintainers and security teams, who now need to monitor not just known malware, but increasingly polished, AI-assisted threats that exploit trusted ecosystems like npm.

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

[Anthropic](https://thehackernews.com/search/label/Anthropic)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[Claude](https://thehackernews.com/search/label/Claude)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[Solana](https://thehackernews.com/search/label/Solana)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterpr...