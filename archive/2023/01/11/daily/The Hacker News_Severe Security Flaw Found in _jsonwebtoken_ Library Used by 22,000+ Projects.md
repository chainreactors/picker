---
title: Severe Security Flaw Found in "jsonwebtoken" Library Used by 22,000+ Projects
url: https://thehackernews.com/2023/01/critical-security-flaw-found-in.html
source: The Hacker News
date: 2023-01-11
fetch_date: 2025-10-04T03:34:59.480965
---

# Severe Security Flaw Found in "jsonwebtoken" Library Used by 22,000+ Projects

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Severe Security Flaw Found in "jsonwebtoken" Library Used by 22,000+ Projects](https://thehackernews.com/2023/01/critical-security-flaw-found-in.html)

**Jan 10, 2023**Ravie LakshmananSoftware Security / Supply Chain

[![high-severity security flaw](data:image/png;base64... "high-severity security flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5LcBYzGpiZdVnYmwrcLsf152DDY3nLQTYRETW_R3U1IN_ZezhDUut1IiqziXbz51S6_bCjrJ1hjD0_lAags912yJnU_T1jxDMT3JjJTYOCC152EMfQrjofIeDn8BhmO6SZtQjI9scL0Xae4186kSTga71gVL5y0hqdvGYfhdFG_Z9TDErs2bnxn8Z/s790-rw-e365/json.png)

> ### **UPDATE: CVE-2022-23529 Retracted Following Review**
>
> Auth0 and Unit 42 said they are formally retracting CVE-2022-23529 (CVSS score: 7.6) based on the fact that several prerequisites are essential for exploitation. The cybersecurity company said "important security checks" have been added to fix the problem.
>
> "The security issue remains a concern only when the jsonwebtoken library is used in an insecure way," the maintainers [said](https://github.com/auth0/node-jsonwebtoken/security/advisories/GHSA-27h2-hvpr-p74q) in an advisory. "In such a scenario, if all the prerequisites are met, the issue may be exploitable; however, the source of this risk is the calling code and not the library itself."

A high-severity security flaw has been disclosed in the open source jsonwebtoken (JWT) library that, if successfully exploited, could lead to remote code execution on a target server.

"By exploiting this [vulnerability](https://github.com/advisories/GHSA-27h2-hvpr-p74q), attackers could achieve remote code execution (RCE) on a server verifying a maliciously crafted JSON web token (JWT) request," Palo Alto Networks Unit 42 researcher Artur Oleyarsh [said](https://unit42.paloaltonetworks.com/jsonwebtoken-vulnerability-cve-2022-23529/) in a Monday report.

Tracked as [**CVE-2022-23529**](https://nvd.nist.gov/vuln/detail/CVE-2022-23529) (CVSS score: 7.6), the issue impacts all versions of the library, including and below 8.5.1, and has been addressed in [version 9.0.0](https://github.com/auth0/node-jsonwebtoken/releases/tag/v9.0.0) shipped on December 21, 2022. The flaw was reported by the cybersecurity company on July 13, 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

jsonwebtoken, which is [developed and maintained](https://jwt.io/introduction) by Okta's Auth0, is a JavaScript module that allows users to decode, verify, and generate JSON web tokens as a means of securely transmitting information between two parties for authorization and authentication. It has over [10 million weekly downloads](https://www.npmjs.com/package/jsonwebtoken) on the npm software registry and is used by more than 22,000 projects.

Therefore, the ability to run malicious code on a server could break confidentiality and integrity guarantees, potentially enabling a bad actor to overwrite arbitrary files on the host and perform any action of their choosing using a poisoned secret key.

[![high-severity security flaw](data:image/png;base64... "high-severity security flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGJMHm-180A73nnsr6sA5Zpd-WNjAgupUM8NT_GiKiGC52UhlokOF188ziYTYiayjBeEZFqLMSiEpJTuKKBbMWOOIpv1tB6XMkhbNXSouNadDbqd1Ur8Y_0Xy_rmoWZaQxvCkkv5by2-DqOTdjd7qaQFTjj-ohg_ZJnsp1xC5LiB5wxhBpLcnM_CZz/s790-rw-e365/poc.png)

"With that being said, in order to exploit the vulnerability described in this post and control the [secretOrPublicKey value](https://github.com/auth0/node-jsonwebtoken#jwtverifytoken-secretorpublickey-options-callback), an attacker will need to exploit a flaw within the secret management process," Oleyarsh explained.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As open source software increasingly emerges as a lucrative initial access pathway for threat actors to stage supply chain attacks, it's crucial that vulnerabilities in such tools are proactively identified, mitigated, and patched by downstream users.

Making matters worse is the fact that cybercriminals have become much faster at exploiting newly revealed flaws, drastically shrinking the time between a patch release and exploit availability. According to Microsoft, it only takes [14 days on average](https://thehackernews.com/2022/11/microsoft-warns-of-uptick-in-hackers.html) for an exploit to be detected in the wild after public disclosure of a bug.

To combat this problem of vulnerability discovery, Google, last month, announced the release of [OSV-Scanner](https://thehackernews.com/2022/12/google-launches-largest-distributed.html), an open source utility that aims to identify all transitive dependencies of a project and highlight relevant shortcomings impacting it.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[JSON](https://thehackernews.com/search/label/JSON)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWind...