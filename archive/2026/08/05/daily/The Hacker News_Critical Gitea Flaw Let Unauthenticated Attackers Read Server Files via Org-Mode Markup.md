---
title: Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup
url: https://thehackernews.com/2026/08/critical-gitea-flaw-let-unauthenticated.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:52.414415
---

# Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup

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

![cybersecurity](data:image/svg+xml;base64...)

# [Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup](https://thehackernews.com/2026/08/critical-gitea-flaw-let-unauthenticated.html)

**Swati Khandelwal**Aug 05, 2026Vulnerability / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwgShwk2piIWpgBCF7ikGum0q7QycFbG91NuOiXNj4iRw_Uya_1R53Mx53EcLELS4lEusFjCYxTZuD0vf1VbGdXJ6rM9zq2OuNMsP20bbATKOaMUYbu9vWRbAJUQX436hP4vWvwc-jy1sWdoIIph0Uf93XMVImu-OIKnOMBUOYptMtoK9nAsP4yo48AtM/s1700-e365/gitea-lfi.jpg)

An unauthenticated attacker can read any file the service account can access on **Gitea**, the self-hosted Git platform, in versions 1.22.1 through 1.27.0. No login, no repository write access. A public repository and crafted Org-mode markup are enough. The flaw is fixed in Gitea 1.27.1.

The file-read flaw is tracked as `CVE-2026-59774`, rated Critical with a CVSS score of 9.8, and received its formal advisory on August 2. Gitea 1.27.1 also patches `CVE-2026-60004`, a separate remote code execution bug covered in a [prior THN report](https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html).

Gitea said Cloud instances would be upgraded automatically during the release maintenance window. Self-hosted administrators should move to 1.27.1 immediately.

The file-read bug is not direct one-request remote code execution. Gitea says it can become command execution if an attacker reads `app.ini`, extracts `INTERNAL_TOKEN`, injects a Git hook through the internal logger, and triggers that hook during an anonymous clone.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

That chain is described in [Gitea's advisory](https://github.com/go-gitea/gitea/security/advisories/GHSA-6v53-hr58-556r); The Hacker News found no independently published exploit demonstrating it.

Upgrading is necessary but may not be sufficient after suspected exposure. If logs show the markup endpoint was reached on an affected build, treat credentials readable by the Gitea service account as exposed and rotate the internal token, OAuth material, JWT signing material, and database credentials before considering the instance clean.

## No badge required

The file-read path runs through Gitea's markup rendering endpoint, `POST /{owner}/{repo}/markup`. The route allows optional sign-in, resolves the repository, and checks reader access. An anonymous request clears that check against any public repository with its code unit enabled. That precondition limits the unauthenticated exposure: an instance with no public repositories has no anonymous attack path through this endpoint.

The break is in Gitea's Org-mode renderer. Gitea 1.27.0 initialized `go-org` with `org.New()` and did not replace the library's default `ReadFile` callback. In `go-org` 1.9.1, that callback is `ioutil.ReadFile`. Org-mode's `#+INCLUDE` directive accepts absolute paths and passes them to the callback. An attacker submits Org-mode markup, selects `Mode: file`, and receives files the service account can read.

The fix landed in PR #38642 and was backported in PR #38645. Gitea now overrides `ReadFile` so an Org-mode include path is returned as plain rendered content instead of being resolved from the server filesystem. The patch added a regression test for include-path rendering.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

CVE-2026-59774 was found by [XBOW Security](https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html), an autonomous offensive security system, and triaged by **[Guido Leo](https://x.com/NightRang3r/status/2084639306711171101)**. Shai Rod, known online as NightRang3r, independently reported the same issue.

## What administrators should check

Gitea did not publish formal detection guidance in the advisory. Review anonymous `POST` requests to `/{owner}/{repo}/markup`, especially requests selecting Org-mode rendering or submitting absolute filesystem paths. If the advisory's escalation path was attempted, check repository hook directories for unexpected executable files.

Gitea's advisory reports no exploitation in the wild, and as of August 5, 2026, CVE-2026-59774 had not appeared on CISA's Known Exploited Vulnerabilities catalog. The file-read primitive was publicly previewed before its formal advisory, according to a prior THN report. The token-to-hook command-execution chain remains single-sourced to Gitea's advisory.

The flaw follows a dense stretch of Gitea security work. In June, Gitea patched a critical reverse-proxy authentication bypass in Docker images, [`CVE-2026-20896`](https://thehackernews.com/2026/07/threat-actors-probe-gitea-docker-flaw.html), that threat actors were observed probing 13 days after disclosure. In May, a container-registry access-control flaw, [`CVE-2026-27771`](https://thehackernews.com/2026/05/gitea-vulnerability-exposes-private.html), was estimated to affect more than 30,000 deployments across over 30 countries.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Data Exposure](https://thehackernews.com/search/label/Data%20Exposure), [Developer Security](https://thehackernews.com/search/label/Developer%20Security), [DevOps Security](https://thehackernews.com/search/label/DevOps%20Security), [Git Security](https://thehackernews.com/search/label/Git%20Security), [Open Source Security](h...