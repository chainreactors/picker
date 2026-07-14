---
title: Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365
url: https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
source: The Hacker News
date: 2026-07-13
fetch_date: 2026-07-14T04:48:21.671280
---

# Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365](https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html)

**Swati Khandelwal**Jul 13, 2026Identity Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVh0XoiKxyvhXW_SN-Ynau8iPG3vd2ltt4cDr4L_cGUhc5oBmsogZt5A_l2qbTdPG8Ciu73I0mHhRBDRJ2uWasrA_vqnkdvpbQcdh0ipe-d_cz2HTFJWOCBNxplCO0RuppogFhl1OONqWWXOLQWhH_Bt89c160ZzHtkrnDJN6PsnYWNV1W510diYait_g/s1700-e365/phishing-server-ms.jpg)

An attacker running a live Microsoft 365 phishing operation left a Python web server listening on a public port with directory listing switched on. The command that did it: `python3 -m http.server 8080`, was still sitting in the readable `.bash_history`.

From that one lapse, French security firm [Lexfo](https://blog.lexfo.fr/opendir-to-phishing-operator.html) lifted the operator's entire toolkit and pivoted through it to two more phishing operators, three campaigns in all. Each ran a custom fork of the open-source [Evilginx proxy](https://thehackernews.com/2026/01/researchers-uncover-service-providers.html), cloned from public GitHub.

The largest of the three had been running for more than a year, its victims overwhelmingly corporate mailboxes.

The three got past MFA in two mechanically different ways, one by [proxying the live login](https://thehackernews.com/2026/03/starkiller-phishing-suite-uses-aitm.html), one by abusing a legitimate Microsoft sign-in flow. The two need different defenses, which is the part that matters most if you run Microsoft 365.

Directory listing on a working attack server is close to a full confession. The listing exposed phishing configs, credential-harvesting logs, RMM installers, combolists, backup archives, and the operator's own Telegram session files.

Behind it ran an Evilginx adversary-in-the-middle proxy and a [SimpleHelp](https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html) remote console on the same host, at 185.163.204[.]7 in Budapest, cataloged in late April 2026 during a routine internet scan.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The bash history and a set of public repos pointed straight at the operator: an Egyptian actor the firm tracks as **codemado**, active in VoIP and hacking forums since 2018, now running a Microsoft 365 AiTM platform on picis[.]net and monetizing access through a bulk mailer he wrote called **MaDoO Blaster**.

His campaign went live on April 20 and kept running past the day the directory was found on April 30, with fresh subdomains and a renewed wildcard certificate turning up weeks later. His own bot logged captures against two corporate M365 accounts, one French, one North American.

The repeated captures of the same accounts from different IPs are consistent, the firm says, with the operator refreshing stolen tokens as they aged out.

## Where the kits came from

codemado did not build the framework he runs. He cloned it, and his bash history shows him comparing kits side by side. The server held four Evilginx variants pulled from two other GitHub developers, and both turned out to be active operators in their own right.

The first, **red-queen**, comes from a Nigerian operator the report calls mail-argenta, and it shows how much polish gets bolted onto a public framework. His fork renames the `crossorigin` and `integrity` HTML attributes to defeat Subresource Integrity checks and adds a URL-rewriting engine to `http_proxy.go` to dodge path-based detection. It pre-fills the victim's email address to cut abandonment.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgd1tA6hYRlMS1ChDPxn1-I3yqyBVQDKgeulgu2dQ2C5V29HvJf6L_5027a6FjMnGkZzgRVRMAz23SELE7gCljBibxPaIhNnX7qws6-HsKPisnZ8XLhxVxOjTq8i9uo0s-mhvOz0N2sn0uQwO9OdfYV4uknBXDdLX0xXomMsDTrMLu789hG6WwWUZQDt1o/s1700-e365/directory.jpg)

It also sets a one-year TTL, 31,536,000 seconds, on the captured Microsoft session cookies. The report says an [intercepted login can then outlast a password reset](https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html) and, without a CAE-capable Conditional Access policy, stay usable for months.

A pre-compiled `evilginx2.exe` is committed to the repo, so a buyer never has to build anything. One captured M365 cookie sitting in the repo carried an expiration date of June 30, 2027.

**mail-argenta** got caught the way his own victims do. The firm found his email and a password in infostealer logs, the kind of harvested-credential data his phishing panels exist to produce. That leaked password matched the one hardcoded as the MySQL password in his Kraken panel and reused across his accounts.

## The quiet one

The third fork, **black-queen**, logged far more captures than the other two, and it never touches a password. Its author, whom the researchers could not identify past the handle **saroula01**, built it around Microsoft's OAuth device code flow, a legitimate sign-in path meant for input-constrained devices.

The attack generates a real device code, wraps it in an Authenticator-themed lure page, and tells the target to enter it at the genuine `microsoft.com/devicelogin`. The victim signs in on a real Microsoft page and clears MFA themselves. saroula01's backend polls the token endpoint and takes the token the moment they do.

Calling this "MFA bypass" misses how it works: nothing gets bypassed. The lure page is Authenticator-themed and attacker-built, but the device code and the Microsoft page where the victim finishes are genuine, so the MFA prompt the victim satisfies is real.

A passkey or FIDO2 key does not help either, because the victim clears it on genuine Microsoft infrastructure while authorizing the attacker's session; the origin binding that stops Evilginx passes cleanly when the origin really is Microsoft.

Microsoft [documented the technique in Febru...