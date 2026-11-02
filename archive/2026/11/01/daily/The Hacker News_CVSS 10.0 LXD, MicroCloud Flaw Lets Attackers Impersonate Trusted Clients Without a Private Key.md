---
title: CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key
url: https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html
source: The Hacker News
date: 2026-11-01
fetch_date: 2026-11-02T08:33:34.490560
---

# CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key

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

# [CVSS 10.0 LXD, MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key](https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html)

**Swati Khandelwal**Nov 01, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4Vibbj3miGalyf0avn_Z2WlLhFh5cC5ImXGFlOL0cisgxikHCcLzHjOVM3qO5B47V3uw62rWH6m6fP1svsH3TCG6i9sS19BIXn1CsDjKK3gnG6VQxkFwghemdeBlV4_AM5Ah-_TJ3T_5Gv-D5Pygrm-B5yzQnDqvIXmI2FyAeuzk57_l6esdhNrTMBj0/s1700-nu-rw-lo-l85-e365/linux-vm.jpg)

A critical flaw in Canonical's LXD and MicroCloud let an attacker log in as a trusted client without holding that client's private key. To do it, the attacker had to reach their HTTPS API over the network and have the trusted client's public certificate.

Once in, the attacker would act as that client, with access to the cluster and its virtual machines. If the impersonated account is privileged, the attacker could gain "root access to the host machine," Canonical said.

The flaw, tracked as [CVE-2026-112816](https://ubuntu.com/security/CVE-2026-112816), carries a maximum CVSS score of 10.0, and Canonical has [released fixed versions](https://discourse.ubuntu.com/t/security-advisory-critical-vulnerability-found-in-canonical-lxd-and-microcloud/90557) of both products.

### How the Flaw Works

LXD and MicroCloud let remote clients access their APIs over mutual TLS, a setup in which the client presents a certificate to prove who it is. A client is trusted when its certificate is in the server's trust store, the list of identities the server will accept.

The flaw was in how the server checked that certificate. It compared every certificate the client sent against the trust store, but a TLS connection only proves the client owns the private key for the first certificate in the chain, the leaf. The rest of the chain is whatever the client chose to attach.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

So an attacker could take a trusted client's public certificate, which is not secret, attach it to the chain behind their own, and the server would accept them as that client.

### Who Is Affected

Using the flaw takes two things: network access to the HTTPS API, and the public certificate of a client the server already trusts.

A standalone LXD server does not expose that API by default. It listens only on a local socket unless an administrator turns on the network API with the core.https\_address setting.

MicroCloud, which ties several machines running LXD into one cluster, has a specific weak point. Canonical said an attacker who can capture a member's public certificate as it joins the cluster can then log in as that member.

The CVE record lists LXD 4.0.14, 5.0.10, 5.21.8 and 6.9 as affected, each before the fixed release that follows. Canonical lists these fixed snap versions:

| Product | Snap channel | Fixed version |
| --- | --- | --- |
| LXD | 6/stable | 6.10.1 |
| LXD | 5.21/stable | 5.21.9 |
| LXD | 5.0/stable | 5.0.11 |
| LXD | 4.0/stable | 4.0.15 |
| MicroCloud | 3/stable | 3.4.1 |
| MicroCloud | 2/stable | 2.1.5 |

The bug did not start at Canonical. The Incus project, which began as a community fork of LXD, [reported it](https://github.com/lxc/incus/security/advisories/GHSA-xg75-xf37-cph9), and Canonical confirmed it affected LXD as well. Incus fixed the same flaw in version 7.6.0.

Ubuntu's own archive packages of LXD are listed as not affected or not shipped, so the fixed releases are the snaps.

There is no public sign the flaw has been used in an attack. The CVE record carries a U.S. CISA assessment, dated October 30, that the flaw is not known to have been exploited; it is not on CISA's Known Exploited Vulnerabilities list, and no working exploit has been published.

### What to Do

Update LXD and MicroCloud to the fixed versions. On a snap install, run sudo snap refresh lxd and sudo snap refresh microcloud.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Canonical said the fixed LXD point releases were still rolling out from the candidate channel to stable at the time of its advisory, so check the version you actually have after the refresh rather than assume the fix arrived.

Canonical's advisory gives no temporary workaround for LXD. Because the attack requires network access to the API, limiting who can reach it reduces risk until you update. The Incus project, reporting the same flaw, said there is no configuration fix and that the only step is to restrict network access to the listener.

Incus users should move to [7.6.0](https://discuss.linuxcontainers.org/t/incus-7-6-has-been-released/27462), which fixed this flaw along with 17 other security issues.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [linux](https://thehackernews.com/search/label/linux), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hija...