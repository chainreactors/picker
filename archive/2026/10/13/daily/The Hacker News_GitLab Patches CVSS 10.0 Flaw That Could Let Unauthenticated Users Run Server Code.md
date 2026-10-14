---
title: GitLab Patches CVSS 10.0 Flaw That Could Let Unauthenticated Users Run Server Code
url: https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:25.533512
---

# GitLab Patches CVSS 10.0 Flaw That Could Let Unauthenticated Users Run Server Code

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [GitLab Patches CVSS 10.0 Flaw That Could Let Unauthenticated Users Run Server Code](https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html)

**Ravie Lakshmanan**Oct 13, 2026Vulnerability / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOWNiMkzMghhERT5BPyrVI9JdCWExRLtDNHIHPjmT_WnGhLHyWhahW3xPurPPQJUn7Yz0_g9Nk0zWinEKh4J71g9viLtNVx2fM2anNzhA514PAgZBxobRfeP1jSsovLI6iVi9HIUXxv_dLvK8DrKy5vZktoxrxyd0riB83XCR2dlne7lEgTqdXW1Rwhekz/s1700-nu-rw-lo-l85-e365/gitlab-exploit.jpg)

GitLab has released patches for a maximum-severity security flaw impacting its Community Edition (CE) and Enterprise Edition (EE) software that could result in arbitrary code execution.

"GitLab has remediated an issue that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation," the company [said](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) in a Monday advisory.

The flaw, tracked as **CVE-2026-97229**, has been described as an integer overflow issue. It carries a CVSS score of 10.0. It affects the following versions -

* All versions from 19.2 before 19.2.8
* All versions from 19.3 before 19.3.5, and
* All versions from 19.4 before 19.4.2

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

Patches for the flaw are available in versions 19.4.2, 19.3.5, and 19.2.8. Also addressed are three high-severity bugs -

* **CVE-2026-92883** (CVSS score: 8.7) - A cross-site scripting vulnerability that could allow an authenticated user to execute arbitrary JavaScript in the context of other users' browser sessions via a specially crafted repository.
* **CVE-2026-16301** (CVSS score: 8.5) - An improper authorization vulnerability in the downstream pipeline creation service that could allow an authenticated user with Developer role to execute CI/CD pipelines on protected branches.
* **CVE-2026-14814** (CVSS score: 8.2) - A permissive regular expression vulnerability that could allow a user to poison cached responses for raw repository files, causing targeted users’ CI/CD pipelines to execute specially crafted content and potentially exposing protected environment variables.

The disclosure comes weeks after it remediated a critical flaw in AI Gateway ([CVE-2026-90970](https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html), CVSS score: 9.9) that could have allowed an authenticated user with Duo Agent Platform access to break out of the prompt template sandbox via a specially crafted flow configuration and achieve arbitrary command execution on the AI Gateway.

Last month, another maximum-severity security flaw in GitLab CE and EE ([CVE-2026-85706](https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html), CVSS score: 10.0) witnessed in-the-wild probes within hours of public disclosure.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

P7 DarkSword iOS Exploit Kit Adds Crypto Wallet Data Theft and Remote Commands](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html)

[![The Hacker News](data:image/svg+xml;base64...)

Anthropic Cuts Live Internet Access for Internal AI Tests After Claude Exploits Injection Flaws](https://thehackernews.com/2026/10/anthropic-cuts-live-internet-access-for.html)

[![The Hacker News](data:image/svg+xml;base64...)

FBI Arrests Another ShinyHunters Suspect Reportedly Involved in Its Jobs Portal Hack](https://thehackernews.com/2026/10/fbi-arrests-another-shinyhunters.html)

[![The Hacker News](data:image/svg+xml;base64...)

TP-Link Sued by Four More U.S. States Over Router Security and China Ties](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html)

[![The Hacker News](data:image/svg+xml;base64...)

Anthropic Launches Free AI Vulnerability Scanner for Open-Source Projects](https://thehackernews.com/2026/10/anthropic-launches-free-ai.html)

[![The Hacker News](data:image/svg+xml;base64...)

GoBalance Flaw Lets Attackers Hijack .onion Addresses by Recovering Tor-Format Keys](https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html)

[![The Hacker News](data:image/svg+xml;base64...)

Three Teams Demonstrate Remote Hacks of Fully Patched Google Pixel 10 at Pwn2Own](https://thehackernews.com/2026/10/three-teams-demonstrate-remote-hacks-of.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: Ransomware Affiliate Betrayal, WhatsApp RAT, Exposed Hacker Tools and 12 More Stories](https://thehackernews.com/2026/10/threatsday-ransomware-affiliate.html)

[![The Hacker News](data:image/s...