---
title: Cybercriminals Use Webflow to Deceive Users into Sharing Sensitive Login Credentials
url: https://thehackernews.com/2024/10/cybercriminals-use-webflow-to-deceive.html
source: The Hacker News
date: 2024-10-29
fetch_date: 2025-10-06T18:56:19.225515
---

# Cybercriminals Use Webflow to Deceive Users into Sharing Sensitive Login Credentials

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

# [Cybercriminals Use Webflow to Deceive Users into Sharing Sensitive Login Credentials](https://thehackernews.com/2024/10/cybercriminals-use-webflow-to-deceive.html)

**Oct 28, 2024**Ravie LakshmananPhishing / Cyber Attack

[![Cybercriminals](data:image/png;base64... "Cybercriminals")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5Lvp1ivVYd619h4Jd9xo2GKFvNKdXpLrnFnh1LPkNtUGnxDZD6L5Yt44Oei4yufWAgHVPVNIaZYekeerjsJolF52MMs9elv98ys9nA7E4CYJSXemnC-85Q5CTR9B6Rrh6cBF84ua-81KhX_zGBVLh1q5cbo6n9j6jpkjXA5iU_lxO10KygLzqSSvZokWW/s790-rw-e365/phishing.png)

Cybersecurity researchers have warned of a spike in phishing pages created using a website builder tool called Webflow, as threat actors continue to abuse legitimate services like [Cloudflare](https://thehackernews.com/2024/05/new-tricks-in-phishing-playbook.html) and [Microsoft Sway](https://thehackernews.com/2024/08/new-qr-code-phishing-campaign-exploits.html) to their advantage.

"The campaigns target sensitive information from different crypto wallets, including Coinbase, MetaMask, Phantom, Trezor, and Bitbuy, as well as login credentials for multiple company webmail platforms, as well as Microsoft 365 login credentials," Netskope Threat Labs researcher Jan Michael Alcantara [said](https://www.netskope.com/blog/attackers-target-crypto-wallets-using-codeless-webflow-phishing-pages) in an analysis.

The cybersecurity company said it tracked a 10-fold increase in traffic to phishing pages crafted using Webflow between April and September 2024, with the attacks targeting more than 120 organizations across the world. A majority of those targeted are located in North America and Asia spanning financial services, banking, and technology sectors.

The attackers have been observed using Webflow to create standalone phishing pages, as well as to redirect unsuspecting users to other phishing pages under their control.

"The former provides attackers stealth and ease because there are no phishing lines of code to write and detect, while the latter gives flexibility to the attacker to perform more complex actions as required," Michael Alcantara said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

What makes Webflow a lot more appealing than Cloudflare R2 or Microsoft Sway is that it allows users to create custom subdomains at no additional cost, as opposed to auto-generated random alphanumeric subdomains that are prone to raise suspicion -

* Cloudflare R2 - https://pub-<32\_alphanumeric\_string>.r2.dev/webpage.htm
* Microsoft Sway - https://sway.cloud.microsoft/{16\_alphanumeric\_string}?ref={sharing\_option}

In an attempt to increase the likelihood of success of the attack, the phishing pages are designed to mimic the login pages of their legitimate counterparts in order to deceive users into providing their credentials, which are then exfiltrated to a different server in some instances.

Netskope said it also identified Webflow crypto scam websites that use a screenshot of a legitimate wallet homepage as their own landing pages and redirect the visitor to the actual scam site upon clicking anywhere on the bogus site.

[![Cybercriminals](data:image/png;base64... "Cybercriminals")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimO-kzmrZbckX001o8edYJmRO6dGHzQX23FImTFKMa8S4eM78xli2EQXR0QIJrTL5XUQapdPeBbyk7VNKAWSXYC9ZNpwKiBDW1UxKZ1HrJa1ovsd35GUKwjqnrkFkDOuoA0fClvbsaRQRZ5FoQObxRYNBBp9Gsz1bWFSeGPCrLvOfLI5ygLix3xhyn1JyB/s790-rw-e365/longin.png)

The end goal of the crypto-phishing campaign is to steal the victim's seed phrases, allowing the attackers to hijack control of the cryptocurrency wallets and drain funds.

In the attacks identified by the cybersecurity firm, users who end up providing the recovery phrase are displayed an error message stating their account has been suspended due to "unauthorized activity and identification failure." The message also prompts the user to contact their support team by initiating an online chat on tawk.to.

It's worth noting that chat services such as LiveChat, Tawk.to, and Smartsupp have been misused as part of a cryptocurrency scam campaign dubbed [CryptoCore](https://thehackernews.com/2024/10/pypi-repository-found-hosting-fake.html) by Avast.

"Users should always access important pages, such as their banking portal or webmail, by typing the URL directly into the web browser instead of using search engines or clicking any other links," Michael Alcantara said.

The development comes as cybercriminals are advertising novel anti-bot services on the dark web that claim to bypass Google's [Safe Browsing warnings](https://safebrowsing.google.com) on the Chrome web browser.

"Anti-bot services, like Otus Anti-Bot, Remove Red, and Limitless Anti-Bot, have become a cornerstone of complex phishing operations," SlashNext [said](https://slashnext.com/blog/anti-bot-service-bypass-google-red-page/) in a recent report. "These services aim to prevent security crawlers from identifying phishing pages and blocklisting them."

"By filtering out cybersecurity bots and disguising phishing pages from scanners, these tools extend the lifespan of malicious sites, helping criminals evade detection longer."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Ongoing malspam and malvertising campaigns have also been [discovered](https://x.com/GenThreatLabs/status/1840762181668741130) propagating an actively-evolving malware called [WARMCOOKIE](https://thehackernews.com/2024/06/new-phishing-campaign-deploys.html) (aka [BadSpace](https://thehackernews.com/2024/06/hackers-exploit-legitimate-websites-to.html)), which then acts as a conduit for malware such as CSharp-Streamer-RAT and Cobalt Strike.

"WarmCookie offers a variety of useful functionality for adversaries including payload deployment, file manipulation, command execution, screenshot collection and persistence, making it attractive to use on systems once initial access has been gained to facilitate longer-term, ...