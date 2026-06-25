---
title: Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks
url: https://thehackernews.com/2026/06/cordyceps-cicd-flaws-expose-300-github.html
source: The Hacker News
date: 2026-06-24
fetch_date: 2026-06-25T06:10:33.905293
---

# Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks](https://thehackernews.com/2026/06/cordyceps-cicd-flaws-expose-300-github.html)

**Ravie Lakshmanan**Jun 24, 2026Open Source / Supply Chain Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjl_D6QzBWfQRZAXbjo9RhhLXSedzJR2Q2sUQoQYnDxpC7yETzJgn3KnpT8CcoqlfXdqkcnTCNcEpR1QKphy77NvG_9PIO57hHNF27x8pBb1pLf_4n3A6pTBs3qXQMsz81rvzpGIOqHZn7VqvJoJoB98o7COHOxi5wfkQvxhL4LcOxBkziY4MLxVCEOljX8/s1700-e365/1000085115.jpg)

Cybersecurity researchers have flagged a new class of CI/CD workflow weakness that allows attackers to hijack workflows and compromise open-source supply chains.

The "critical exploitable pattern" has been codenamed **Cordyceps** by Novee Security. The issue can allow full attacker control of repositories at dozens of the largest organizations worldwide, including Microsoft, Google, Apache, and Cloudflare.

"The flaw is exploitable by any unauthenticated user," Elad Meged, founding engineer and security researcher at Novee Security, [said](https://novee.security/blog/cordyceps/). "No org membership or special privileges; a free account is enough to forge approvals, push code, or steal credentials."

The penetration-testing company's scan of about 30,000 high-impact repositories has revealed more than 300 to be fully exploitable, enabling attacker-controlled code execution, credential theft, and supply chain compromise, which can have severe downstream impacts.

The core of the problem trickles down to weak CI/CD configurations that grant pull requests (PRs) more permissions than they should have. PRs are [proposals](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to merge code changes from one branch into the main project. However, because an untrusted PR can trigger privileged workflows, it can open the door to command injection, privilege escalation, and supply chain compromise.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"This supply chain vulnerability lies in the foundational open-source plumbing the entire industry runs on, and the kind of issue that hides from scanners because, technically, every individual piece is working as designed," Novee explained. "The workflow does what it was told. The vulnerability exists only in the composition – untrusted data crossing a trust boundary that no one audited."

On Microsoft's Azure Sentinel, for example, Novee found a comment on a PR that could run anonymous attacker code on Microsoft's CI and steal a non-expiring GitHub App key. In a similar case, a PR on Google's AI Agent Development Kit ("adk-samples") could execute attacker code on Google's CI to gain complete authority over a Google Cloud repository.

Other findings are listed below -

* Apache Doris, where two zero-click attacks cause a single comment on any PR or a forked PR to run attacker code and exfiltrate hard-coded CI credentials or a token with full write permissions
* Cloudflare Workers SDK, where a PR with a crafted branch name can execute arbitrary commands on Cloudflare's CI runners
* Python Software Foundation's Black, where a single pull request from anyone could execute attacker code on Black's build systems and steal the automation token, which can then be used to approve pull requests.

Following responsible disclosure, both Microsoft and Google confirmed impact, while Cloudflare, Python, and Apache have applied hardening and patches, respectively.

"The nature of agentic coding means these CI/CD vulnerabilities are reproduced persistently, at scale, 'infecting' repositories at an exponential rate," Meged said. "Because anonymous users can use them to gain control over the software supply chain, we like to think of it as 'puppeteering' the repositories of some of the world's biggest companies, silently manipulating their workflows."

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

[CI/CD Security](https://thehackernews.com/search/label/CI/CD%20Security), [Command Injection](https://thehackernews.com/search/label/Command%20Injection), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [GitHub](https://thehackernews.com/search/label/GitHub), [Google](https://thehackernews.com/search/label/Google), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Open Source](https://thehackernews.com/search/label/Open%20Source), [Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security), [Workflow Security](https://thehackernews.com/search/label/Workflow%20Security)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](data:image/svg+xml;base64... "Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now")

Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html)

[![Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](data:image/svg+xml;base64... "Researchers Build Self-Repli...