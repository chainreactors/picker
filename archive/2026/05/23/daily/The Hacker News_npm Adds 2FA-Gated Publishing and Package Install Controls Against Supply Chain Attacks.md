---
title: npm Adds 2FA-Gated Publishing and Package Install Controls Against Supply Chain Attacks
url: https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html
source: The Hacker News
date: 2026-05-23
fetch_date: 2026-05-24T06:01:18.088037
---

# npm Adds 2FA-Gated Publishing and Package Install Controls Against Supply Chain Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [npm Adds 2FA-Gated Publishing and Package Install Controls Against Supply Chain Attacks](https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html)

**Ravie Lakshmanan**May 23, 2026Software Supply Chain / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4rnMZgOYbsYr65UN9AZ3oFzcAwqXSYqgRfjUGpeaQeyP-0OAaqJ9aceXPAiujRKwyGQMa_4ShcSvtOWPb9T3qpqF2LATAw2U4iA7IkU9ok0alDbzN_WYJeaZ1SrF0-vyRrEHGedMEcCeP2otYYqplHmqEBda1R_MePbWgEpt-b-GB_RhxJLDC1pJFV0S0/s1700-e365/npm-security.png)

GitHub has rolled out new controls for npm to improve the security of the software supply chain, giving maintainers the ability to explicitly approve a release prior to the packages becoming publicly available for installation.

Called staged publishing, the feature is now generally available on npm. It mandates that a human maintainer pass a two-factor authentication (2FA) challenge to approve a package before it is pushed to the npmjs[.]com.

"Instead of a direct publish that immediately makes a package version available to consumers, the prebuilt tarball is uploaded to a stage queue where a maintainer must explicitly approve it before it becomes installable," GitHub [said](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/).

The Microsoft-owned subsidiary said the change ensures "proof of presence" for every publish, including those that come from non-interactive CI/CD workflows and trusted publishing with OpenID Connect (OIDC) authentication.

Before using [staged publishing](https://docs.npmjs.com/staged-publishing), package maintainers have to meet the following criteria -

* Have publish access to the package
* Package already exists on the npm registry, meaning a brand new package cannot be staged
* 2FA is enabled for the account

Developers can use the command "npm stage publish" from the root directory of the package to submit it to a staging area. To use this command, it's essential to update to npm CLI 11.15.0 or newer. For optimal protection, GitHub is recommending that staged publishing be paired with [trusted publishing](https://docs.npmjs.com/trusted-publishers) using OIDC.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

A second update focused on npm relates to the introduction of three new install source flags alongside the existing -allow-git flag -

* --allow-file: Controls installs from local file paths and local tarballs
* --allow-remote: Controls installs from remote URLs, including https tarballs
* --allow-directory: Controls installs from local directories

The flags allow developers to "apply the same explicit-allowlist approach to every non-registry install source," GitHub said.

The development comes amid a [massive surge](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html) in software supply chain attacks targeting open-source ecosystems over the past few months, with one cybercriminal group known as [TeamPCP](https://thehackernews.com/2026/05/github-internal-repositories-breached.html) engaging in poisoning popular packages at an unprecedented scale through a self-perpetuating cycle of compromises.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [GitHub](https://thehackernews.com/search/label/GitHub), [NPM](https://thehackernews.com/search/label/NPM), [Open Source](https://thehackernews.com/search/label/Open%20Source), [Package Security](https://thehackernews.com/search/label/Package%20Security), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain), [Two-Factor Authentication](https://thehackernews.com/search/label/Two-Factor%20Authentication)

⚡ Top Stories This Week

[![Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](data:image/svg+xml;base64... "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak")

Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vulnerability.html)

[![Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](data:image/svg+xml;base64... "Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence")

Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)

[![On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email](data:image/svg+xml;base64... "On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email")

On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email](https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html)

[![Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access](data:image/svg+xml;base64... "Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access")

Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to G...