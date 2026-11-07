---
title: Experts Demonstrate Barracuda Email Security Gateway Chain Enabling Root Access Without Login
url: https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html
source: The Hacker News
date: 2026-11-06
fetch_date: 2026-11-07T08:02:14.338989
---

# Experts Demonstrate Barracuda Email Security Gateway Chain Enabling Root Access Without Login

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

# [Experts Demonstrate Barracuda Email Security Gateway Chain Enabling Root Access Without Login](https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html)

**Swati Khandelwal**Nov 06, 2026Vulnerability / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh59LXthjD6N50867w2v7T4JyVUCOlVAmz1MJcZHKBFFaSnKDabB0FmdedrbvWRkp9XONe9Pz2RV1MQ-9QpJ8d85XE3w54EmMLKgaf1ygKD2e0y2X9mA7VsfyyB-8l1KFi-F5Gj9Q2vdsusmAl2khvXHNyOzWB_l7bj6NkOHkUgDYW-vENOowt0L8qM4kM/s1700-nu-rw-lo-l85-e365/bar.jpg)

Two [flaws in Barracuda's Email Security Gateway](https://thehackernews.com/2026/11/barracuda-flaws-could-be-chained-to.html), an email-filtering appliance, can be chained to run commands on it as root, its highest level of access, with no login required.

The company released patches on Monday, and the security firm watchTowr detailed the attack chain on Thursday.

One flaw, **CVE-2026-116606**, is an authorization bypass. An unauthenticated attacker can use it to restore a crafted configuration backup and change the appliance's global settings.

The other, **CVE-2026-111560**, is a command injection. It runs commands as root but normally needs an administrator account, and on the Email Security Gateway the bypass gives an attacker that access. Chained, the two let an attacker reach root with no login.

### Affected Products and Fixes

The authorization bypass affects only the Email Security Gateway. The command injection reaches five other products, but on those it still needs an administrator account.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Mandiant, which assigned the two CVE records, rates the bypass 9.3 out of 10 and the command injection 8.6. Barracuda has released a patch for each affected product and lists the fixed firmware in its [security advisory](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection). The Email Security Gateway is fixed in version 9.4.0.030 and later.

### What to Do

The advisory sets out three steps:

* Apply the patch for each affected product, or upgrade to the fixed firmware listed above.
* If you cannot patch at once, limit the appliance's administration interface to trusted internal networks.
* If you have turned automatic patching off, switch it back on.

### How the Chain Works

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkbSqww_wRfY8jGc2zBfAXVNnw4GFAbnKM6ZOo6rIO9bAGND_J4BIodTOqDuvGNfTW7XG7_zTJrm_iqkmieD4Ts5zaVnQ0Saq_li5l4m4LQZit3rRI5Y36uw8mn_pp2xN5msNeO0X-7MfOZ8S-JLeg04bh8wS0n7b_lO6JDMcG7KooJejISN7R4NoSJRo/s1700-nu-rw-lo-l85-e365/barracuda.gif)

In its [technical analysis](https://labs.watchtowr.com/barracuda-networks-is-your-new-best-friend-barracuda-email-security-gateway-pre-auth-remote-root-rce-cve-2026-116606-cve-2026-111560/), watchTowr traced the chain through the appliance's code. A failed password change returns the attacker a low-privilege role instead of stopping the request, which leaves a backup-restore function open to someone who has not logged in.

That function accepts an uploaded backup, and the restored data includes a timezone value that the appliance later runs as a shell command with root privileges. Barracuda guards backups with a checksum, but the secret used to compute it is built into the code, allowing an attacker to forge a valid checksum. The firm showed the attack by writing a file to the appliance as root.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

As of this week, neither flaw appears in CISA's Known Exploited Vulnerabilities (KEV catalog), and no public report ties either to an attack. watchTowr also released a [detection tool](https://github.com/watchtowrlabs/watchTowr-vs-Barracuda-RCE-CVE-2026-116606-CVE-2026-111560) that checks whether an appliance is vulnerable, but has not published an exploit.

The Email Security Gateway was hit in [the 2023 attacks](https://thehackernews.com/2023/08/urgent-fbi-warning-barracuda-email.html) by a group tracked as UNC4841, which exploited a different flaw, CVE-2023-2868, as a zero-day. That case is unrelated to the two flaws patched this week, and nothing ties the new pair to any attacker.

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

[email security](https://thehackernews.com/search/label/email%20security), [network security](https://thehackernews.com/search/label/network%20security), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

TeamViewer ...