---
title: W4SP Stealer Constantly Targeting Python Developers in Ongoing Supply Chain Attack
url: https://thehackernews.com/2022/11/w4sp-stealer-constantly-targeting.html
source: The Hacker News
date: 2022-11-19
fetch_date: 2025-10-03T23:15:28.464034
---

# W4SP Stealer Constantly Targeting Python Developers in Ongoing Supply Chain Attack

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

# [W4SP Stealer Constantly Targeting Python Developers in Ongoing Supply Chain Attack](https://thehackernews.com/2022/11/w4sp-stealer-constantly-targeting.html)

**Nov 18, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQg8jczwSQpLksxTlRbjSKEJ8ZT6YMkuXsWgmg8BUR5znMELLXN13pDqAns0vYVZvk2XzY8ApFUTXCbSOmQN7YDm_9d_R6y1RdlEECzAXlncxS4BJUKWMlGw2vEnQbABsC3cA_elFR3ExNfVlxPzfBWvKvmVIa5bwxH9YghxAElNEKtjaRyZSiyNFo/s790-rw-e365/pypi.png)

An ongoing supply chain attack has been leveraging malicious Python packages to distribute malware called W4SP Stealer, with over hundreds of victims ensnared to date.

"The threat actor is still active and is releasing more malicious packages," Checkmarx researcher Jossef Harush [said](https://medium.com/checkmarx-security/wasp-attack-on-python-polymorphic-malware-shipping-wasp-stealer-infecting-hundreds-of-victims-10e92439d192) in a technical write-up, calling the adversary **WASP**. "The attack seems related to cybercrime as the attacker claims that these tools are undetectable to increase sales."

The findings from Checkmarx build on recent reports from [Phylum](https://thehackernews.com/2022/11/researchers-uncover-29-malicious-pypi.html) and [Check Point](https://thehackernews.com/2022/11/researchers-uncover-pypi-package-hiding.html), which flagged 30 different modules published on the Python Package Index (PyPI) that were designed to propagate malicious code under the guise of benign-looking packages.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack is just the latest threat to target the software supply chain. What makes it notable is the use of steganography to extract a [polymorphic malware](https://en.wikipedia.org/wiki/Polymorphic_code) payload hidden within an image file hosted on Imgur.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAacEZHEsABDLKTCV5BdYy3DHu_y6uR45UopRpOelQy6WKYPY5E8XIkuyQAXL32txqt76p5uELeTK9jlHOCbM_eKepgqFyytnHdehAATwFM9MvE3ozjIsbnrln_8-zTSmBjkjHEftyPJZh2YgBqEbyjx1gyA5uA6jjAeUalHOnbxRzqJzoUxEKKr2l/s790-rw-e365/code.png)

The installation of the package ultimately makes way for W4SP Stealer (aka WASP Stealer), an information stealer engineered to exfiltrate Discord accounts, passwords, crypto wallets, and other files of interest to a [Discord Webhook](https://discord.com/developers/docs/resources/webhook).

Checkmarx's analysis further tracked down the attacker's Discord server, which is managed by a lone user named "Alpha.#0001," and the various fake profiles created on GitHub to lure unwitting developers into downloading the malware.

Furthermore, the Alpha.#0001 operator has been observed advertising the "fully undetectable" malware for $20 on the Discord channel, not to mention releasing a steady stream of new packages under different names as soon as they are taken down from PyPI.

As recently as November 15, the threat actor was seen adopting a new username on PyPI ("halt") to upload typosquatting libraries that leveraged [StarJacking](https://checkmarx.com/blog/starjacking-making-your-new-open-source-package-popular-in-a-snap/) – a technique wherein a package is published with an URL pointing to an already popular source code repository.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The level of manipulation used by software supply chain attackers is increasing as attackers get increasingly more clever," Harush noted. "This is the first time [I've] seen polymorphic malware used in software supply chain attacks."

"The simple and lethal technique of fooling using by creating fake GitHub accounts and sharing poisoned snippets has proven to trick hundreds of users into this campaign."

The development also comes as U.S. cybersecurity and intelligence agencies published new guidance outlining the recommended practices customers can take to secure the software supply chain.

"Customer teams specify to and rely on vendors for providing key artifacts (e.g. SBOM) and mechanisms to verify the software product, its security properties, and attest to the SDLC security processes and procedures," the guidance [reads](https://www.cisa.gov/uscert/ncas/current-activity/2022/11/17/cisa-nsa-and-odni-release-guidance-customers-securing-software).

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

[Checkmarx](https://thehackernews.com/search/label/Checkmarx)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin ...