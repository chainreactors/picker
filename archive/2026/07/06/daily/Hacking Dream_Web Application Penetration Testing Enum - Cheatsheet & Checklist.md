---
title: Web Application Penetration Testing Enum - Cheatsheet & Checklist
url: https://www.hackingdream.net/2026/07/web-application-penetration-testing-enum-cheatsheet-checklist.html
source: Hacking Dream
date: 2026-07-06
fetch_date: 2026-07-07T06:03:22.645851
---

# Web Application Penetration Testing Enum - Cheatsheet & Checklist

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Web Application Penetration Testing Enum - Cheatsheet & Checklist

[July 06, 2026](https://www.hackingdream.net/2026/07/web-application-penetration-testing-enum-cheatsheet-checklist.html "permanent link")

Web Application Penetration Testing: Step-by-Step Guide

# Web Application Penetration Testing: Step-by-Step Guide

*Updated on July 6, 2026*

### Table of Contents

* [Prerequisites](#prerequisites)
* [Base tooling](#base-tooling)
* [Attack Surface Overview](#attack-surface-overview)
* [Phase 1: Passive Reconnaissance](#phase-1-passive-reconnaissance)
* [Phase 2: Active Enumeration and DNS Resolution](#phase-2-active-enumeration-and-dns-resolution)
* [Phase 3: Port, Service and TLS Discovery](#phase-3-port-service-and-tls-discovery)
* [Phase 4: Technology Fingerprinting](#phase-4-technology-fingerprinting)
* [Phase 5: Content Discovery and Directory Enumeration](#phase-5-content-discovery-and-directory-enumeration)
* [Phase 6: Authentication Surface Enumeration](#phase-6-authentication-surface-enumeration)
* [Phase 7: CMS-Specific Enumeration](#phase-7-cms-specific-enumeration)
* [Phase 8: Vulnerability Identification](#phase-8-vulnerability-identification)
* [Phase 9: Recon Automation Frameworks](#phase-9-recon-automation-frameworks)
* [Phase 10: Burp Suite Workflow](#phase-10-burp-suite-workflow)
* [Phase 11: Exploitation Techniques](#phase-11-exploitation-techniques)
* [Full Validation Checklist](#full-validation-checklist)
* [Conclusion](#conclusion)

**Welcome to the ultimate guide on Web Application Penetration Testing. This penetration testing methodology will walk you through every critical step of modern security testing.**

Now, if there's one thing I've learned after running web assessments for years, it's this - engagements are won or lost in enumeration, but they get finished in exploitation. Everybody wants to jump straight to the shell. The people who consistently deliver, though, map the target obsessively first, then punch through the weak point they found. You can't attack what you haven't discovered, and you can't demonstrate impact without following through.

So this is the full playbook I actually work on real web engagements. We start completely passive - not a single packet to the target - and escalate through active scanning, content discovery, fingerprinting, and vulnerability identification, then finish with the exploitation techniques that turn a finding into proof. This is deliberately the order you follow in the field. If you want the broader mindset behind why this matters, I wrote it up in [how to become a hacker from scratch](https://www.hackingdream.net/2019/05/how-to-be-hacker-platforms-to-learn-hacking-from-scratch.html), and the core lesson holds: enumerate more, always.

By the end you'll have a repeatable flow covering subdomain discovery, origin IP hunting behind a WAF, TLS and email record checks, live host validation, directory brute forcing, CMS enumeration, automated vulnerability identification, and the payloads to validate file upload, SQL injection, and CORS findings. Incorporating principles from the [OWASP methodology](https://owasp.org/) ensures comprehensive coverage of these attack vectors.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZHaBwO2vZKNY3eAFFhSbXwDrdSspOc9Z7UmsKUPzyB3hkf4S6KhB7ogbBrabSD7M-gYrrm2i8MQHrbyijoqFsC_J4pDz2TOMBEs8tpLRKY1LOrDJRyWnBe5sljxoalyD1oDDPzzY3xba3BcF7lXZAUtws1bBGXcjcE3u7Q2rpPieeJpGhJ0ghgReSnetZ/w640-h358/Web%20Application%20Penetration%20Testing%20Enum%20Cheatsheet%20checklist.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZHaBwO2vZKNY3eAFFhSbXwDrdSspOc9Z7UmsKUPzyB3hkf4S6KhB7ogbBrabSD7M-gYrrm2i8MQHrbyijoqFsC_J4pDz2TOMBEs8tpLRKY1LOrDJRyWnBe5sljxoalyD1oDDPzzY3xba3BcF7lXZAUtws1bBGXcjcE3u7Q2rpPieeJpGhJ0ghgReSnetZ/s1024/Web%20Application%20Penetration%20Testing%20Enum%20Cheatsheet%20checklist.png)

Note: Before pentesting any system, have proper authorization from concerned authorities and follow ethical guidelines. Everything here assumes explicit written permission to test the target in scope. The exploitation sections are for demonstrating impact during authorized assessments and building your report, not for use anywhere you don't own or aren't contracted to test.

## Prerequisites

Here's the baseline setup before we dig in.

* **Access Level:** None required for external recon. Some authenticated enumeration and exploitation steps need valid application credentials (a low-privilege user account is enough).
* **Target Environment:** A web application in scope. Examples use `10.10.10.10` for hosts and `domain.local` / `domain.com` for domains.
* **Platform:** Kali or any Linux box with Go, Python3, and Docker installed.

Most of the modern recon stack is Go-based, so sort your Go environment first.

## Base tooling

```
# Base tooling
apt update && apt install -y golang-go python3 python3-pip git nmap masscan whatweb nikto dirb dirsearch sqlmap sslscan wafw00f hydra zaproxy -y
# WPScan (Ruby)
gem install wpscan
# testssl.sh - deep TLS auditing
git clone https://github.com/drwetter/testssl.sh.git
# ProjectDiscovery core - the workhorses of modern recon
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
# URL harvesting and crawling
go install -v github.com/lc/gau/v2/cmd/gau@latest
go install -v github.com/tomnomnom/waybackurls@latest
go install -v github.com/hakluke/hakrawler@latest
# Content discovery
cargo install feroxbuster        # or: apt install feroxbuster
go install -v github.com/ffuf/ffuf/v2@latest
# OWASP Amass for deep asset mapping
go install -v github.com/owasp-amass/amass/v4/...@master
```

## Attack Surface Overview

Before commands, understand what you're mapping. A modern web target isn't one server - it's a sprawl. You're hunting for:

* Root domain plus every subdomain (prod, dev, staging, admin panels, forgotten hosts)
* The real origin IP hiding behind Cloudflare, Akamai, or a load balancer
* Every open port, because web servers show up far beyond 80 and 443
* The technology stack - framework, language, CMS, WAF, reve...