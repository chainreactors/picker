---
title: BugBounty — Mastering the Basics (along with Resources)[Part-3]
url: https://infosecwriteups.com/bugbounty-mastering-the-basics-along-with-resources-part-3-1619f6854e20?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-06
fetch_date: 2025-10-06T20:07:58.847245
---

# BugBounty — Mastering the Basics (along with Resources)[Part-3]

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1619f6854e20&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbugbounty-mastering-the-basics-along-with-resources-part-3-1619f6854e20&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbugbounty-mastering-the-basics-along-with-resources-part-3-1619f6854e20&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40iabhipathak)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1619f6854e20---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1619f6854e20---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# BugBounty — Mastering the Basics (along with Resources)[Part-3]

[![Abhinav Pathak](https://miro.medium.com/v2/resize:fill:64:64/1*3-R6aIY4guWblT05QuUN-A.jpeg)](https://medium.com/%40iabhipathak?source=post_page---byline--1619f6854e20---------------------------------------)

[Abhinav Pathak](https://medium.com/%40iabhipathak?source=post_page---byline--1619f6854e20---------------------------------------)

54 min read

·

Nov 9, 2024

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Bug Bounty Hunting is a career that is known for the heavy use of security tools. These tools help to find vulnerabilities in software, web, and mobile applications and are an integral part of bounty hunting. Below is a list of security tools which should be leveraged by bug bounty hunters.

### Bug Bounty Tools & Scripts: Your Arsenal for Successful Hunting

![]()

Tools you should definitely know about:

* **BurpSuite**: Burp Suite is a software security application used for penetration testing of web applications.

[## Burp Suite - Application Security Testing Software

### Get Burp Suite. The class-leading vulnerability scanning, penetration testing, and web app security platform. Try for…

portswigger.net](https://portswigger.net/burp?source=post_page-----1619f6854e20---------------------------------------)

* **ZAP:** OWASP ZAP is an open-source web application security scanner.

[## The ZAP Homepage

### Welcome to ZAP!

www.zaproxy.org](https://www.zaproxy.org/?source=post_page-----1619f6854e20---------------------------------------)

* **Caido**: A lightweight web security auditing toolkit.

[## Caido - A lightweight web security auditing toolkit

### Built from the ground up in Rust, Caido aims to help security professionals and enthusiasts audit web applications with…

caido.io](https://caido.io/?source=post_page-----1619f6854e20---------------------------------------)

Below is an **awesome list** to know more about the Bug Bounty Tools.

[## GitHub - vavkamil/awesome-bugbounty-tools: A curated list of various bug bounty tools

### A curated list of various bug bounty tools. Contribute to vavkamil/awesome-bugbounty-tools development by creating an…

github.com](https://github.com/vavkamil/awesome-bugbounty-tools?source=post_page-----1619f6854e20---------------------------------------)

### Recon

### Subdomain Enumeration

* **Sublist3r**

[## GitHub - aboul3la/Sublist3r: Fast subdomains enumeration tool for penetration testers

### Fast subdomains enumeration tool for penetration testers - aboul3la/Sublist3r

github.com](https://github.com/aboul3la/Sublist3r?source=post_page-----1619f6854e20---------------------------------------)

Fast subdomains enumeration tool for penetration testers

* **Amass**

[## GitHub - owasp-amass/amass: In-depth attack surface mapping and asset discovery

### In-depth attack surface mapping and asset discovery - owasp-amass/amass

github.com](https://github.com/owasp-amass/amass?source=post_page-----1619f6854e20---------------------------------------)

In-depth Attack Surface Mapping and Asset Discovery

* **Massdns**

[## GitHub - blechschmidt/massdns: A high-performance DNS stub resolver for bulk lookups and…

### A high-performance DNS stub resolver for bulk lookups and reconnaissance (subdomain enumeration) - blechschmidt/massdns

github.com](https://github.com/blechschmidt/massdns?source=post_page-----1619f6854e20---------------------------------------)

A high-performance DNS stub resolver for bulk lookups and reconnaissance (subdomain enumeration)

* **Findomain**

[## GitHub - Findomain/Findomain: The fastest and complete solution for domain recognition. Supports…

### The fastest and complete solution for domain recognition. Supports screenshoting, port scan, HTTP check, data import…

github.com](https://github.com/Findomain/Findomain?source=post_page-----1619f6854e20---------------------------------------)

The fastest and cross-platform subdomain enumerator, do not waste your time.

* **Sudomy**

[## GitHub - screetsec/Sudomy: Sudomy is a subdomain enumeration tool to collect subdomains and…

### Sudomy is a subdomain enumeration tool to collect subdomains and analyzing domains performing automated reconnaissance…

github.com](https://github.com/Screetsec/Sudomy?source=post_page-----1619f6854e20---------------------------------------)

Sudomy is a subdomain enumeration tool to collect subdomains and analyzing domains performing automated reconnaissance (recon) for bug hunting / pentesting.

* **Chaos client**

[## GitHub - projectdiscovery/chaos-client: Go client to communicate with Chaos DB API.

### Go client to communicate with Chaos DB API. . Contribute to projectdiscovery/chaos-client development by creating an…

github.com](https://github.com/projectdiscovery/chaos-client?source=post_page-----1619f6854e20---------------------------------------)

Go client to communicate with Chaos DNS API.

* **Domained**

[## GitHub - TypeError/domained: Multi Tool Subdomain Enumeration

### Multi Tool Subdomain Enumeration. Contribute to TypeError/domained development by creating an account on GitHub.

github.com](https://github.com/TypeError/domained?source=post_page-----1619f6854e20---------------------------------------)

Multi Tool Subdomain Enumeration

* **Bugcrowd levelup subdomain enumeration**

[## GitHub - appsecco/bugcrowd-levelup-subdomain-enumeration: This repository contains all the material…

### This repository contains all the material from the talk "Esoteric sub-domain enumeration techniques" given at Bugcrowd…

github.com](https://github.com/appsecco/bugcrowd-levelup-subdomain-enumeration?source=post_page-----1619f6854e20---------------------------------------)

This repository contains all the material from the talk “Esoteric sub-domain enumeration techniques” given at Bugcrowd LevelUp 2017 virtual conference

* **Shuffled...