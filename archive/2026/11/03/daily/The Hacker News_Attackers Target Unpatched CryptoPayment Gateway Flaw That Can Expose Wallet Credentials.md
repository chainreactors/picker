---
title: Attackers Target Unpatched CryptoPayment Gateway Flaw That Can Expose Wallet Credentials
url: https://thehackernews.com/2026/11/attackers-target-unpatched.html
source: The Hacker News
date: 2026-11-03
fetch_date: 2026-11-04T08:19:21.705817
---

# Attackers Target Unpatched CryptoPayment Gateway Flaw That Can Expose Wallet Credentials

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Attackers Target Unpatched CryptoPayment Gateway Flaw That Can Expose Wallet Credentials](https://thehackernews.com/2026/11/attackers-target-unpatched.html)

**Ravie Lakshmanan**Nov 03, 2026Cryptocurrency / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1tflB6yfzJv3UijqJlfCikzOQx0NHz9AVTh13vDvWu-LfAfFfBDjGbKI79Cb3dd2Ca_ck2KNP46WwYKcuweVD9Wc1srFpRkBimsG-EQS567tR92Yyg1DKPWqhhZHc1sP71qHWQoUxndY2VzDlqVsd2gx2GPcMx7pjVG8ws13bfMKXDtqz5q7EiJ22Mmr_/s1700-nu-rw-lo-l85-e365/wp.jpg)

Threat actors are attempting to exploit an unpatched maximum-severity security vulnerability in the CryptoPayment Gateway WordPress plugin, according to [findings](https://x.com/DefusedCyber/status/2117325160608870613) from Defused Cyber.

The vulnerability in question is CVE-2026-81648, which carries a CVSS score of 10.0. Successful exploitation of the flaw could permit unauthenticated users to delete arbitrary files on the server and extract sensitive data, including stored wallet credentials.

"The CryptoPayment Gateway WordPress plugin from 1.2.1 to 1.2.2 does not apply an authorization check on one of its AJAX endpoints, allowing unauthenticated users to invoke administrative operations, including deleting arbitrary files on the server, overwriting the payment gateway configuration and recovering stored wallet credentials in cleartext," according to a [description of the flaw](https://nvd.nist.gov/vuln/detail/cve-2026-81648) on the NIST National Vulnerability Database (NVD).

The vulnerability affects versions 1.2.1 through 1.2.2, which is the latest version. There are no known fixes for the flaw, according to [WP Scan](https://wpscan.com/vulnerability/9b1490a0-1381-4d22-8086-f75aade4e898/). As of August 28, 2026, the plugin has been [closed on the WordPress Plugin Directory](https://wordpress.org/plugins/cryptopayment-gateway/) and is no longer available for download due to an unspecified "security issue."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Statistics show that the plugin has been collectively downloaded 1,845 times, including 20 downloads over the last seven days. It's unclear if it's actively installed on any WordPress sites.

"We are observing in-the-wild exploitation attempts against CVE-2026-81648, a critical (CVSS 10.0) flaw in the CryptoPayment Gateway for WordPress," Defused Cyber said in an X post. "The attacks we recorded came from infrastructure that markets themselves as 'Anonymous KYC-Free VPS Hosting.'"

In the absence of a fix, site owners are advised to remove the plugin, rotate wallet keys, and audit for any suspicious changes.

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security), [WordPress](https://thehackernews.com/search/label/WordPress)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them](https://thehackernews.com/2026/10/teamviewer-flaw-lets-remote-computers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html)

[![The Hacker News](data:image/svg+xml;base64...)

Binance Suffers Security Breach Affecting $6.3 Billion in Assets, Nearly $3 Billion Frozen](https://thehackernews.com/2026/10/binance-suffers-security-breach.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: Critical Firewall Flaws, Banking Trojans Rented, Weaponized PDF, Token Theft + 26 More Stories](https://thehackernews.com/2026/10/threatsday-critical-firewall-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html)

[![The Hacker News](data:image/svg+xml;base64...)

Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html)

[![The Hacker News](data:image/svg+xml;base64...)

China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html)

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Exploit PHP2Shell Flaws in Internet-Exposed Palo Alto Networks Man...