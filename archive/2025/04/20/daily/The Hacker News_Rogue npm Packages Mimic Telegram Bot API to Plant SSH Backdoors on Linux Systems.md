---
title: Rogue npm Packages Mimic Telegram Bot API to Plant SSH Backdoors on Linux Systems
url: https://thehackernews.com/2025/04/rogue-npm-packages-mimic-telegram-bot.html
source: The Hacker News
date: 2025-04-20
fetch_date: 2025-10-06T22:04:54.455513
---

# Rogue npm Packages Mimic Telegram Bot API to Plant SSH Backdoors on Linux Systems

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

# [Rogue npm Packages Mimic Telegram Bot API to Plant SSH Backdoors on Linux Systems](https://thehackernews.com/2025/04/rogue-npm-packages-mimic-telegram-bot.html)

**Apr 19, 2025**Ravie LakshmananLinux / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTYaPrg3QcUDzJQw_6M2cQ8mylAmeTI7yDB2gTcrkFTeuN-nmzQGrSavv6DL8aU7gs55EFPkfLJM_rYvi1lm8wCbOK3OKftPnP9DR_HJbvbzvnvevxMUQRwOX0xd6qSZ0Is0f-eWZJFTknWvr4IoD2Qu4sZxmlmtn8nTW9yOOHbiFgeNyzc8cv5Wb9Z1X2/s790-rw-e365/linux.jpg)

Cybersecurity researchers have uncovered three malicious packages in the npm registry that masquerade as a popular Telegram bot library but harbor SSH backdoors and data exfiltration capabilities.

The packages in question are listed below -

* [node-telegram-utils](https://npm-stat.com/charts.html?package=node-telegram-utils) (132 downloads)
* [node-telegram-bots-api](https://npm-stat.com/charts.html?package=node-telegram-bots-api) (82 downloads)
* [node-telegram-util](https://npm-stat.com/charts.html?package=node-telegram-util) (73 downloads)

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to supply chain security firm Socket, the packages are designed to mimic [node-telegram-bot-api](https://www.npmjs.com/package/node-telegram-bot-api), a popular Node.js Telegram Bot API with over 100,000 weekly downloads. The three libraries are still available for download.

"While that number may sound modest, it only takes a single compromised environment to pave the way for wide-scale infiltration or unauthorized data access," security researcher Kush Pandya [said](https://socket.dev/blog/npm-malware-targets-telegram-bot-developers).

"Supply chain security incidents repeatedly show that even a handful of installs can have catastrophic repercussions, especially when attackers gain direct access to developer systems or production servers."

The rogue packages not only replicate the description of the legitimate library, but also leverage a technique called [starjacking](https://thehackernews.com/2022/11/w4sp-stealer-constantly-targeting.html) in a bid to elevate the authenticity and trick unsuspecting developers into downloading them.

Starjacking refers to an approach where an open-source package is made to be more popular than it is by linking the GitHub repository associated with the legitimate library. This typically takes advantage of the non-existing validation of the relation between the package and the GitHub repository.

[![SSH Backdoors on Linux Systems](data:image/png;base64... "SSH Backdoors on Linux Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE1h2efG4A4gi-XQFVoa5_-vaSEHHxVBpvvVEOeiFSqstqBaNASdgIwD8ofeKnlo1DrCCLkUC-lkZ8n9KSvfq-HOQyaV6_WWdils6NG6JWlLkUOPzicvZzppX00oiR8Yr9CuTZkeDmuk9Tom8V6vRHI_vRoOVc0cr5jW7VTnDhVs_xXueiU0E3gzynHUg4/s790-rw-e365/node.jpg)

Socket's analysis found that the packages are designed to explicitly work on Linux systems, adding two SSH keys to the "~/.ssh/authorized\_keys" file, thus granting the attackers persistent remote access to the host.

The script is designed to collect the system username and the external IP address by contacting "ipinfo[.]io/ip." It also beacons out to an external server ("solana.validator[.]blog") to confirm the infection.

What makes the packages sneaky is that removing them does not completely eliminate the threat, as the inserted SSH keys grant unfettered remote access to the threat actors for subsequent code execution and data exfiltration.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Socket detailed another malicious package named [@naderabdi/merchant-advcash](https://npm-stat.com/charts.html?package=@naderabdi/merchant-advcash) that's engineered to launch a reverse shell to a remote server while disguising as a Volet (formerly Advcash) integration.

"The package @naderabdi/merchant-advcash contains hardcoded logic that opens a reverse shell to a remote server upon invocation of a payment success handler," the company [said](https://socket.dev/blog/npm-package-advcash-integration-triggers-reverse-shell). "It is disguised as a utility for merchants to receive, validate, and manage cryptocurrency or fiat payments."

"Unlike many malicious packages that execute code during installation or import, this payload is delayed until runtime, specifically, after a successful transaction. This approach may help evade detection, as the malicious code only runs under specific runtime conditions."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[node.js](https://thehackernews.com/search/label/node.js)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Reverse Shell](https://thehackernews.com/search/label/Reverse%20Shell)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[SSH](https://thehackernews.com/search/label/SSH)[Telegram](https://thehacke...