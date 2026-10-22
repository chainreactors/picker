---
title: Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases
url: https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:42.664517
---

# Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html)

**Swati Khandelwal**Oct 21, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEig4Pkd5r0GeWGSaCoHaEsZVVoh5Y6xBkFvMTGYKvD5oONYnczQGAUqpjD6eCiA6sxiiel6Zs0kPiBEWOZJ21URkE59iJm-LDUFPYwPEf8o8d8lnyiMOR53H7IeXGKn3tTG9pusA-HKwYo0n04WQ1m8kg8dxIWEtxFGMDiBzrV-zzqAH2R2OVT2E1ViX_U/s1700-nu-rw-lo-l85-e365/git-rce.jpg)

GitLab released fixes on October 21 for a flaw that lets an attacker run code on a self-managed server without logging in, and it affects every version of the software going back to 7.0, released in 2014.

The fix matters even for administrators who patched nine days earlier: the October 12 update covered only versions 19.2 and later, and the new fixed versions sit one patch above it, so an instance updated then is in range again.

The flaw, tracked as [CVE-2026-110264](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/), is rated 10.0 on the CVSS scale, the maximum. GitLab says that, under certain conditions, it could allow an unauthenticated user to run arbitrary code on the server due to an integer overflow during the compilation of a specially crafted regular expression. GitLab has not said what those conditions are.

The company reports no sign the flaw has been used in attacks, and it is not listed in the U.S. CISA catalog of known exploited vulnerabilities as of October 22.

Only self-managed installations need to act. GitLab.com already runs the fixed version, and GitLab Dedicated tenants on the internal releases 19.3.5-internal0 and 19.4.2-internal0 or later already have the fix. GitLab fixed the flaw in seven versions at once.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

The table below pairs each release branch with the version that fixes it.

| If you run | Upgrade to |
| --- | --- |
| 19.5 before 19.5.1 | 19.5.1 |
| 19.4 before 19.4.3 | 19.4.3 |
| 19.3 before 19.3.6 | 19.3.6 |
| 19.2 before 19.2.9 | 19.2.9 |
| 19.1 before 19.1.9 | 19.1.9 |
| 19.0 before 19.0.10 | 19.0.10 |
| 7.0 through 18.11, before 18.11.13 | 18.11.13 |

Four of those versions are older than GitLab normally patches. The company's policy covers the current release and the previous two monthly releases, which, as of today, are 19.5, 19.4, and 19.3.

GitLab said it backported this fix to 18.11.13, 19.0.10, 19.1.9, and 19.2.9 on top of its standard releases, a step it reserves for severe issues.

The reason the flaw reaches so far back is the part of GitLab that failed. The regular-expression compiler is Ruby's built-in engine, called Onigmo, which GitLab ships inside its own packages and patches in its own builds. A weakness in that engine is present wherever GitLab has shipped it, which is every release since 7.0.

GitLab also published two detection rules to help self-managed administrators look for exploitation attempts, named "Onigmo native worker crash" and "Org mode render error burst." They are part of the company's open-source [TLDR framework](https://docs.gitlab.com/security/detecting_security_incidents/), which writes each detection in the Sigma format against GitLab's own application logs.

GitLab has not said what preconditions an attacker needs to reach the compiler, so administrators cannot yet rule themselves out by configuration; the fix is the only certain protection, and GitLab's advisory offers no interim workaround.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

This is the fourth code-execution flaw in GitLab's regular-expression engine that the same researcher, who uses the handle joaxcar, has reported in a month, and the first to reach versions before 19.2.

On [October 12](https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html), GitLab fixed CVE-2026-97229, also an unauthenticated 10.0 overflow in the regex compiler, in versions 19.2.8, 19.3.5, and 19.4.2. On [September 23](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-1-released/), it fixed two more, CVE-2026-93577 and CVE-2026-89078, both rated 9.9 but requiring a logged-in account. The three earlier flaws stopped at version 19.2; this one does not.

The October 21 release fixes 11 security issues in all, one critical and the rest high, medium, or low.

Two of the others concern authentication. CVE-2026-15723, rated high at 8.2, could allow a logged-in user to take over another account, but only when an administrator has enabled both SAML and LDAP auto-linking.

A cache-poisoning flaw in GitLab's OAuth and OpenID Connect endpoints, CVE-2026-112212, rated high at 7.5, could allow an attacker to redirect certain sign-in flows to a server they control in setups that use a shared cache.

The upgrade carries a cost worth planning for. The 19.4.3 and 19.3.6 releases include database changes that run during the upgrade, and on a single-node server that means downtime while they finish. GitLab says multi-node setups can apply the patch without downtime using its zero-downtime procedure.

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
[![Facebook Messenger](data:image/png;ba...