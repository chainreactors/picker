---
title: Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors
url: https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html
source: The Hacker News
date: 2026-09-11
fetch_date: 2026-09-12T06:50:13.201094
---

# Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors](https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html)

**Swati Khandelwal**Sep 11, 2026Vulnerability / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX61WXln9MMGAzqzflpRDt_LZGfB7ZJ_u1fsQhr5FRnml48-E-V-uxtCIF-GERZlt-eBhw3MDT7_6jFgwEDF1ppC7YZlB_CZn-q4_nKD9S3fQTI3kDQFe2Izsq6_NoGnCRtRZckr8Irg9kOJ8Fwghl3qHqwg1zWoN6ff-VsmlCaojw2Divb6L00F34lJk/s1700-nu-rw-lo-l85-e365/jfrog-art.jpg)

Attackers have chained two flaws in **JFrog Artifactory**, the repository that software build pipelines pull from, to take administrator control of self-hosted servers and plant backdoors, cloud security company Wiz said in a report.

Wiz saw the attacks between August 15 and September 8. JFrog had fixed both flaws before then, so only servers that had not been updated were open to them.

Neither flaw gives administrator control on its own.

* **CVE-2026-42018** makes Artifactory hand an internal anonymous-user token to a caller who has not logged in, even when anonymous access is turned off.
* **CVE-2026-42016** then allows that low-privilege token to be swapped for one with administrator scope, because Artifactory checks a token's signature and who issued it, but not what the token is allowed to do.

[Every case Wiz saw](https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201) followed a similar pattern. The attacker sent an unauthenticated request to a token endpoint and received a token for the internal anonymous user, then exchanged it at Artifactory's token-creation endpoint for a token with administrator scope.

That second token keeps the anonymous username. Administrator actions taken with it show up in the logs as **token:anonymous** rather than under a named account.

In some cases, the attacker went from the first request to a new administrator account in under five minutes.

The chain reaches a narrower set of builds than either flaw alone. A server has to be affected by both, so closing either one breaks it. In JFrog's published ranges, CVE-2026-42016 ends at 7.133.11, leaving the 7.146 and 7.161 branches outside that range.

JFrog shipped the CVE-2026-42018 fix on the 7.146 branch on April 28 and on the 7.133 branch on August 12, three days before the attacks Wiz saw began.

What the attackers did with administrator authority varied. Wiz said no single actor carried out every step it saw.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Across the compromised servers, attackers created administrator accounts and left them in place. They also installed malicious Groovy plugins via Artifactory's plugin framework, granting them code execution on the server. Some ran shell commands via the plugin execution endpoint to explore and list files.

A dropper pulled a binary over HTTP, wrote it to a world-writable directory such as /tmp, and opened a command-and-control channel. Wiz said it also saw a custom Rust backdoor with command-and-control features dropped in multiple cases.

A third Artifactory flaw in the same report, **CVE-2026-82329**, was exploited separately between September 1 and September 8, and it is the reason a server on a newer branch may still be affected.

It is a critical authentication bypass, rated 9.8 on the CVSS scale, that targets Artifactory's default configuration and requires no additional flaw. An unauthenticated attacker with network access can obtain administrator privileges through it alone, on six release branches up to 7.161.

The Hacker News [reported on September 1](https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html) that attackers had begun creating administrator tokens for themselves through that flaw days after JFrog disclosed it. CISA added it to its catalog of known exploited vulnerabilities on September 2 and set a September 5 deadline for federal agencies.

Fastly, a content delivery network, [said in an analysis](https://www.fastly.com/blog/cve-2026-82329-jfrog-artifactory-authentication-bypass-exploitation-activity) that a public exploit appeared on September 1 and scanning followed. It counted about 406,000 exploitation attempts across its platform on September 2, its busiest day. Those are attempts seen in traffic, not compromises.

On servers taken through that flaw, Wiz saw attackers read the system configuration and, in several cases, take the cluster join key, the shared secret Artifactory nodes use to register with one another.

### What to Install

Upgrade self-hosted Artifactory to the fixed build for your release branch, listed in [JFrog's security advisories](https://docs.jfrog.com/releases/docs/jfrog-security-advisories). JFrog says cloud instances need no action.

| CVE | What it does | Affected | Fixed in |
| --- | --- | --- | --- |
| CVE-2026-42018 | Returns an internal anonymous-user token to a caller who has not logged in | Below 7.111.20, and below 7.117.27, 7.125.19, 7.133.28, and 7.146.8 on those branches | 7.111.20, 7.117.27, 7.125.19, 7.133.28, 7.146.8 |
| CVE-2026-42016 | Lets a low-privilege token be exchanged for an administrator-scope token | Before 7.133.11 | 7.133.11 |
| CVE-2026-82329 | Gives an unauthenticated attacker administrator privileges on its own | Below 7.111.21, and below 7.117.28, 7.125.20, 7.133.29, 7.146.38, and 7.161.20 on those branches | 7.111.21, 7.117.28, 7.125.20, 7.133.29, 7.146.38, 7.161.20 |

JFrog lists one fixed version for CVE-2026-42016, 7.133.11, and no separate fix for each branch. Its advisory does not say whether a later build on an older branch, such as 7.117.28, also closes it. The Hacker News has asked JFrog that question, and has asked Wiz which versions the compromised servers were running.

For CVE-2026-82329, JFrog publishes a workaround for anyone who cannot upgrade quickly: generate a random value and add it as an ex...