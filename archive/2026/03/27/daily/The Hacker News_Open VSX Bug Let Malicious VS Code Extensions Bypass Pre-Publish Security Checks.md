---
title: Open VSX Bug Let Malicious VS Code Extensions Bypass Pre-Publish Security Checks
url: https://thehackernews.com/2026/03/open-vsx-bug-let-malicious-vs-code.html
source: The Hacker News
date: 2026-03-27
fetch_date: 2026-03-28T04:20:15.238922
---

# Open VSX Bug Let Malicious VS Code Extensions Bypass Pre-Publish Security Checks

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Open VSX Bug Let Malicious VS Code Extensions Bypass Pre-Publish Security Checks](https://thehackernews.com/2026/03/open-vsx-bug-let-malicious-vs-code.html)

**Ravie Lakshmanan**Mar 27, 2026Software Security / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxyuzdQgdhyphenhyphenfWqx9GyfXC7_Bop28GdU7Bvyj3ZEvEBm8HbchBOMZFiLIGHSVFM9OdfCaKJSyAZzY3F3soB37-VtKEcY_KShCnzB2D-t8DJ5mbSl4MlbMgCV8uSMf9LaTds8vn_rccuiUIzq0mC5lxYK7HstyftiOEqYGCJC8PP5sCF_UariwUHXuvqYXkt/s1700-e365/open-code.jpg)

Cybersecurity researchers have disclosed details of a now-patched bug impacting Open VSX's pre-publish scanning pipeline to cause the tool to allow a malicious Microsoft Visual Studio Code (VS Code) extension to pass the vetting process and go live in the registry.

"The pipeline had a single boolean return value that meant both 'no scanners are configured' and 'all scanners failed to run,'" Koi Security researcher Oran Simhony [said](https://www.koi.ai/blog/open-sesame-how-a-fail-open-bug-in-open-vsxs-new-scanner-let-malware-walk-right-in) in a report shared with The Hacker News. "The caller couldn't tell the difference. So when scanners failed under load, Open VSX treated it as 'nothing to scan for' and waved the extension right through."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Early last month, the Eclipse Foundation, which maintains Open VSX, [announced](https://thehackernews.com/2026/02/eclipse-foundation-mandates-pre-publish.html) plans to [enforce pre-publish security checks](https://github.com/eclipse-openvsx/openvsx/issues/1331) before VS Code extensions are published to the repository in an attempt to tackle the growing problem of malicious extensions.

With Open VSX also serving as the extension marketplace for Cursor, Windsurf, and other VS Code forks, the move was seen as a proactive approach to prevent rogue extensions from getting published in the first place. As part of pre-publish scanning, extensions that fail the process are quarantined for admin review.

The vulnerability discovered by Koi, codenamed **Open Sesame**, has to do with how this Java-based service reports the scan results. Specifically, it's rooted in the fact that it misinterprets scanner job failures as no scanners are configured, causing an extension to be marked as passes, and then immediately activated and made available for download from Open VSX.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMOFH9G9sMtwGREWmDJBASZfKSsFLrFQmEmBXHY7Rn2OAK3_cu11i99shqtgn8ad-ws0v1K5kaOz3V5xvEylToV1Uls_fx5pRtnBmXTR1JyAkAptjifaUjY9ttnqvS8n6C1jweoVZAf9BUzEjTeU3fnTpJRAGbCnJPI7JzFxE7lmsgQrIfwRBRD6iGsk0F/s1700-e365/koi.png)

At the same time, it can also refer to a scenario where the scanners exist, and the scanner jobs have failed and cannot be enqueued because the database connection pool is exhausted. Even more troublingly, a recovery service designed to retry failed scans suffered from the same problem, thereby allowing extensions to skip the entire scanning process under certain conditions.

An attacker can take advantage of this weakness to flood the publish endpoint with several malicious .VSIX extensions, causing the concurrent load to exhaust the database connection pool. This, in turn, leads to a scenario where scan jobs fail to enqueue.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-stories-xmcyber-d)

What's notable about the attack is that it does not require any special privileges. A malicious actor with a free publisher account could have reliably triggered this vulnerability to undermine the scanning process and get their extension published. The issue was [addressed](https://github.com/eclipse-openvsx/openvsx/commit/64720cc8d7a71de580c242b8d4a19c5c9771c889) in Open VSX [version 0.32.0](https://github.com/eclipse-openvsx/openvsx/releases/tag/v0.32.0) last month following responsible disclosure on February 8, 2026.

"Pre-publish scanning is an important layer, but it's one layer," Koi said. "The pipeline's design is sound, but a single boolean that couldn't distinguish between 'nothing to do' and 'something went wrong' turned the entire infrastructure into a gate that opened under pressure."

"This is a common anti-pattern: fail-open error handling hiding behind a code path designed for a legitimate 'nothing to do' case. If you're building similar pipelines, make failure states explicit. Never let 'no work needed' and 'work failed' share a return value."

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [Open Source](https://thehackernews.com/search/label/Open%20Source), [software security](https://thehackernews.com/search/label/software%20security), [Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security), [Visual Studio](https://thehackernews.com/search/label/Visual%20Studio), [Vulnerability](htt...