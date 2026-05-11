---
title: You Don’t Need a 0-Day for RCE: A Real-World Kill Chain
url: https://infosecwriteups.com/you-dont-need-a-0-day-for-rce-a-real-world-kill-chain-e7ec690ba9a4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-10
fetch_date: 2026-05-11T05:54:57.290926
---

# You Don’t Need a 0-Day for RCE: A Real-World Kill Chain

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyou-dont-need-a-0-day-for-rce-a-real-world-kill-chain-e7ec690ba9a4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyou-dont-need-a-0-day-for-rce-a-real-world-kill-chain-e7ec690ba9a4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e7ec690ba9a4---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e7ec690ba9a4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# You Don’t Need a 0-Day for RCE: A Real-World Kill Chain

[![Nebty](https://miro.medium.com/v2/resize:fill:64:64/1*ke-UIygZxq4_g18M0bH4GA.png)](https://medium.com/%40nebty?source=post_page---byline--e7ec690ba9a4---------------------------------------)

[Nebty](https://medium.com/%40nebty?source=post_page---byline--e7ec690ba9a4---------------------------------------)

9 min read

·

10 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3De7ec690ba9a4&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyou-dont-need-a-0-day-for-rce-a-real-world-kill-chain-e7ec690ba9a4&source=---header_actions--e7ec690ba9a4---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

## **Introduction**

There is a pervasive myth in cybersecurity that achieving **Remote Code Execution (RCE)** on an enterprise target requires a sophisticated 0-day exploit or months of reverse engineering. In reality, some of the most devastating breaches happen through a simple chain of **logical misconfigurations**. There’s a unique kind of thrill when you bypass an enterprise-grade Web Application Firewall (WAF) without actually sending a single malicious payload through it.

Recently, while performing a security assessment on a heavily defended certification portal (let’s call it *“CertGuard”*), I stumbled upon a classic architectural blind spot. What started as a frustrating encounter with Cloudflare evolved into a scenario where I entirely bypassed the perimeter and achieved a complete server takeover. **No zero-days. No complex memory corruption. Just basic OSINT, a broken assumption, and a naked backend.**

In this article, I want to walk you through the attack chain: utilizing **OSINT to unmask the Origin IP**, building a robust validation pipeline to **bypass the WAF**, and finally, exploiting an **Unrestricted File Upload** on the naked backend to achieve **Remote Code Execution (RCE)**.

*Disclaimer: The vulnerabilities discussed in this article were discovered during an authorized penetration test. To respect client confidentiality and adhere to non-disclosure agreements, all identifying details, company names, URLs, and sensitive data have been completely redacted or altered. This write-up is shared purely for educational purposes.*

Press enter or click to view image in full size

![]()

The high-level kill chain: From unmasking the Origin IP to achieving Remote Code Execution.

## **The Recon: A WAF in the Way**

After mapping out the application, I hit a familiar brick wall: `Server: cloudflare`. My standard scanning payloads were getting instantly dropped, rate-limiting was aggressive, and the WAF was doing its job perfectly.

But any pentester knows that a WAF is only as strong as the perimeter it protects. If the backend server (the Origin) is directly accessible from the public internet, the WAF is nothing more than a suggestion. I needed to unmask that Origin IP.

Finding an Origin IP is an art form. Here are my go-to techniques using OSINT search engines:

**1. Historical SSL Certificates (The “Forgetful Admin” Vector)**

Before moving behind a WAF, servers often host their own SSL certificates. Search engines archive this data.

* **Censys Query:** `host.services.cert.names: "certguard-target.com"`

*(****Pro-Tip:*** *Companies often expose non-standard ports like 3306 or 8080 on the same IP or subnet. You can combine queries:* `host.services.cert.names:"certguard-target.com" and host.services.port:{"22", "3306", "3389", "8080", "27017"}`*)*

**2. Unique Identifiers (The Fingerprinting Vector)**

If the SSL trick doesn’t work, search for unique elements from the website’s source code indexed on raw IPs.

**Google Analytics IDs:** Grab the ID (e.g., `UA-12345678-1`) from the source.

* **Censys Query:** `host.services.endpoints.http.body: "UA-12345678-1"`

**Favicon Hashes:** Calculate the MurmurHash3 of the site’s favicon.

* **Censys Query***:* `host.services.endpoints.http.favicons.hash_md5: "hash"`

**Copyright Strings:**

* **Censys Query***:* `web.endpoints.http.body:"\u00A9 copyright CertGuard 2024"`

**3. HTML Titles & Open Ports**

Sometimes, the backend IP answers HTTP requests directly with the same title as the main site.

* **Censys Query:** `web.endpoints.http.html_title: "CertGuard Secure Portal"`

### Leveling Up: Automating the Hunt & Further Reading

Clicking through the Censys or Shodan web interfaces is fine for a single target, but if you are doing at-scale bug bounty recon, you need automation.

You can use the official [Censys Command Line Interface (cencli)](https://github.com/Censys/cencli) to run these queries directly from your terminal. *(Note: Running advanced CLI queries requires a paid/premium tier. Censys also recently updated their authentication mechanisms, so the official GitHub repo is the best place to learn the setup).* For practical usage examples on how to automate your searches, check out this excellent guide: [Automate your Recon with Censys: How Pro Hackers Use It](https://pallabjyoti218.medium.com/automate-your-recon-with-censys-how-pro-hacker-use-censys-871aeabd517e).

If you want to dive deeper into advanced dorking and recon chains, here are a few highly recommended resources from the community:

* [**Intigriti’s Complete Guide to finding more vulnerabilities with Shodan and Censys**](https://www.intigriti.com/researchers/blog/hacking-tools/complete-guide-to-finding-more-vulnerabilities-with-shodan-and-censys) — A masterclass on building better search queries.
* [**From Recon via Censys and DNSDumpster to getting a P1**](/from-recon-via-censys-and-dnsdumpster-to-getting-p1-by-login-using-weak-password-password-504e617956ce) — A great write-up demonstrating how combining different OSINT tools leads directly to critical impact.
* [**Shodan for Bug Bounty and why you shouldn’t use these 53 Dorks**](https://medium.com/%40BrownBearSec/shodan-for-bug-bounty-and-why...