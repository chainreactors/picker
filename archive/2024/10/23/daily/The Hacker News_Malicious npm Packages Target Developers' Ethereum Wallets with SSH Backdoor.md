---
title: Malicious npm Packages Target Developers' Ethereum Wallets with SSH Backdoor
url: https://thehackernews.com/2024/10/malicious-npm-packages-target.html
source: The Hacker News
date: 2024-10-23
fetch_date: 2025-10-06T18:56:25.971407
---

# Malicious npm Packages Target Developers' Ethereum Wallets with SSH Backdoor

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

# [Malicious npm Packages Target Developers' Ethereum Wallets with SSH Backdoor](https://thehackernews.com/2024/10/malicious-npm-packages-target.html)

**Oct 22, 2024**Ravie LakshmananVulnerability / Supply Chain

[![Ethereum Wallets with SSH Backdoor](data:image/png;base64... "Ethereum Wallets with SSH Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8NplkVO0QQMjwfqR7YOVpn1E-Y2EtfXc1Kn4UA7_CVidYJSYXvSGRpgLydR_u-XcbkPSEZFY__4nmfhDowsqt7eWJS3BhO_NzbpmfLM6sAylve_1sqcT2YKyxkEDYORvFx8QIBGsFJlA5KIqobW5cdhFSJBuzXiT4dm53eJDIh07LLuajfL6fuNPISQa3/s790-rw-e365/ether.png)

Cybersecurity researchers have discovered a number of suspicious packages published to the npm registry that are designed to harvest Ethereum private keys and gain remote access to the machine via the secure shell (SSH) protocol.

The packages attempt to "gain SSH access to the victim's machine by writing the attacker's SSH public key in the root user's authorized\_keys file," software supply chain security company Phylum [said](https://blog.phylum.io/trojanized-ethers-forks-on-npm-attempting-to-steal-ethereum-private-keys/) in an analysis published last week.

The list of packages identified as part of the campaign, which aim to impersonate the legitimate [ethers package](https://www.npmjs.com/package/ethers), are as follows -

* [ethers-mew](https://npm-stat.com/charts.html?package=ethers-mew) (62 downloads)
* [ethers-web3](https://npm-stat.com/charts.html?package=ethers-web3) (110 downloads)
* [ethers-6](https://npm-stat.com/charts.html?package=ethers-6) (56 downloads)
* [ethers-eth](https://npm-stat.com/charts.html?package=ethers-eth) (58 downloads)
* [ethers-aaa](https://npm-stat.com/charts.html?package=ethers-aaa) (781 downloads)
* [ethers-audit](https://npm-stat.com/charts.html?package=ethers-audit) (69 downloads)
* [ethers-test](https://npm-stat.com/charts.html?package=ethers-test) (336 downloads)

Some of these packages, most of which have been published by accounts named "crstianokavic" and "timyorks," are believed to have been released for testing purposes, as most of them carry minimal changes across them. The latest and the most complete package in the list is ethers-mew.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is not the first time rogue packages with similar functionality have been discovered in the npm registry. In August 2023, Phylum [detailed](https://blog.phylum.io/typosquat-of-popular-ethereum-package-steals-private-keys/) a package named ethereum-cryptographyy, a typosquat of a popular cryptocurrency library that exfiltrated the users' private keys to a server in China by introducing a malicious dependency.

[![Ethereum Wallets with SSH Backdoor](data:image/png;base64... "Ethereum Wallets with SSH Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3UqrZAruAi0VjeOyOQmdI5WSLbk9dT0hMZ7njDF5y5uRhWMUU1Jceru-jl7SEmwObnjel7ixFK0P_jv6PwwJP_IfCqDIfVb_vnIfOvj62NYZmgy1KttD5uud5GrlF8uIYNjanlJ-eoMHWbfyWrcEPCyWUs-sKN7TeqbLlMvhmk0iLFEStuJfSbTn_uZYK/s790-rw-e365/ether.png)

The latest attack campaign embraces a slightly different approach in that the malicious code is embedded directly into the packages, allowing threat actors to siphon the Ethereum private keys to the domain "ether-sign[.]com" under their control.

What makes this attack a lot more sneaky is the fact that it requires the developer to actually use the package in their code – such as creating a new Wallet instance using the imported package – unlike typically observed cases where simply installing the package is enough to trigger the execution of the malware.

In addition, the ethers-mew package comes with capabilities to modify the "/root/.ssh/authorized\_keys" file to add an attacker-owned SSH key and grant them persistent remote access to the compromised host.

"All of these packages, along with the authors' accounts, were only up for a very short period of time, apparently removed and deleted by the authors themselves," Phylum said.

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

[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Ethereum](https://thehackernews.com/search/label/Ethereum)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[SSH](https://thehackernews.com/search/label/SSH)[Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;b...