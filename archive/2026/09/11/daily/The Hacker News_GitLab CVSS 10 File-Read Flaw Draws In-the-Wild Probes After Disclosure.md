---
title: GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure
url: https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html
source: The Hacker News
date: 2026-09-11
fetch_date: 2026-09-12T06:50:12.423679
---

# GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure

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

# [GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html)

**Ravie Lakshmanan**Sep 11, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioFH6aWhF9NgRW1O3yFExc7paTA9akN5-3IUQF8mvEiSTaFJjKvm6YQzFX6MP2uimYplHe1MJXz6eZtPtnxaLy25jJBhU6KuhsWFpIlnqhbn6OI6QTcfp6Olp1-VDUEF4KEYFF7hQDBdmgtxibsg9MkvbcOJIlR8Of2Flyw2m9zYfXC6gUm-TV8XA6vU43/s1700-nu-rw-lo-l85-e365/gitlab-wild.jpg)

GitLab has [released patches](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) to address multiple flaws, including a maximum-severity security vulnerability that has witnessed in-the-wild probes within hours of public disclosure.

The vulnerability in question is **CVE-2026-85706** (CVSS score: 10.0), a path traversal issue in the repository commits API that could allow an unauthenticated user to read arbitrary files from the GitLab server under certain conditions.

The problem, per GitLab, stems from "improper path confinement and missing authentication enforcement in the repository commits API."

The issue impacts the following versions of GitLab Community Edition (CE) and Enterprise Edition (EE) -

* All versions from 18.7 before 19.1.8,
* All versions from 19.2 before 19.2.6, and
* All versions from 19.3 before 19.3.2

According to preemptive exposure management firm watchTowr, the vulnerability is [already witnessing](https://www.linkedin.com/posts/watchtowr_watchtowr-intel-is-already-observing-in-the-wild-activity-7504127032608415744-8JqE/) active in-the-wild probes since 06:00 UTC on September 11, 2026. The issue, it said, allows an external attacker to read log files and GitLab-specific configuration files to obtain credentials, secrets, and sensitive information.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"This is the second instance of a critical severity GitLab vulnerability in recent weeks, following the previous GraphQL code injection ([CVE-2026-19478](https://thehackernews.com/2026/08/gitlab-cve-2026-19478-comes-under.html)) that was almost immediately actively exploited," Jake Knott, head of threat intelligence at watchTowr, said in a statement shared with The Hacker News. "Exploitation requires just one requirement, at least one public project must exist."

"The appeal to attackers of GitLab is obvious, as unauthorized access allows an attacker to gain access to source code, CI/CD secrets, credentials, and the ability to inject code into build pipelines, gaining access or poisoning anything downstream of it, which as we've seen throughout this year has been a favorite of attackers."

Also patched by GitLab in versions 19.3.2, 19.2.6, and 19.1.8 is a critical insecure deserialization bug in GitLab EE (CVE-2026-87719, CVSS score: 9.9) that could result in information disclosure.

The vulnerability could allow an authenticated user with Duo Chat access to obtain Advanced Search instance configurations and sensitive credentials using a specially crafted GraphQL subscription argument to bypass serialization and perform server object lookup," GitLab said.

Organizations running self-managed GitLab instances that are exposed to the internet must apply the patches as soon as possible, or limit public access, if not required.

"Based on the history, the transition of this vulnerability to indiscriminate mass exploitation is likely not far away, and defenders have limited time to act," Knott said. "Where possible, organizations should also review log files for HTTP POST requests to '/api/v4/projects/{id}/repository/commits/' URIs containing 'file.Path' parameters to identify potential exploitation attempts."

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Gitlab](https://thehackernews.com/search/label/Gitlab), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity](https://thehackernews.com/2026/09/attackers-exploit-critical-langflow-and.html)

[![The Hacker News](data:image/svg+xml;base64...)

Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests](https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More](https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html)

[![The Hacker News](data:image/svg+xml;base64...)

N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw](https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html)

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication](https://thehackernews.com/20...