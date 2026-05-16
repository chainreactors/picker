---
title: Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence
url: https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html
source: The Hacker News
date: 2026-05-15
fetch_date: 2026-05-16T05:15:44.807741
---

# Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence

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

# [Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)

**Ravie Lakshmanan**May 15, 2026Vulnerability / AI Security

[![OpenClaw Flaws](data:image/png;base64... "OpenClaw Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz_tK9S8jS_n5CK694-FLGjQP5_Mmpg7z9ZRiBayWsJLsuFRIm-8j1hTlhH90779FvnvhpiFKeGP9CzI5RCPsxQEnOzAIQsPzUsAJhUWtNm9iwf9C1W9DbDmqoQ_jjHhM7huYDV210OB9o1L9NPoJ0IL6R9Xc-V4JQ91Kn-b47_2ravRJ6-qlZOVrqsuAz/s1700-e365/openclaw.png)

Cybersecurity researchers have disclosed a set of four security flaws in OpenClaw that could be chained to achieve data theft, privilege escalation, and persistence.

The vulnerabilities, collectively dubbed
**[Claw Chain](https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw)**
by Cyera, can permit an attacker to establish a foothold, expose sensitive data, and plant backdoors. A brief description of the flaws is below -

* **[CVE-2026-44112](https://nvd.nist.gov/vuln/detail/CVE-2026-44112)**
  (CVSS score: 9.6/6.3) - A time-of-check/time-of-use (TOCTOU) race condition vulnerability in the
  [OpenShell](https://docs.openclaw.ai/gateway/openshell)
  managed sandbox backend that allows attackers to bypass sandbox restrictions and redirect writes outside the intended mount root.
* **[CVE-2026-44113](https://nvd.nist.gov/vuln/detail/CVE-2026-44113)**
  (CVSS score: 7.7/6.3) - A TOCTOU race condition vulnerability in OpenShell that allows attackers to bypass sandbox restrictions and read files outside the intended mount root.
* **[CVE-2026-44115](https://nvd.nist.gov/vuln/detail/CVE-2026-44115)**
  (CVSS score: 8.8) - An incomplete list of disallowed inputs vulnerability that allows attackers to bypass allowlist validation by embedding shell expansion tokens in a
  [here document](https://en.wikipedia.org/wiki/Here_document)
  (heredoc) body to execute unapproved commands at runtime.
* **[CVE-2026-44118](https://nvd.nist.gov/vuln/detail/CVE-2026-44118)**
  (CVSS score: 7.8) - An improper access control vulnerability that could allow non-owner loopback clients to impersonate an owner to elevate their privileges and gain control over gateway configuration, cron scheduling, and execution environment management.

Cyera said successful exploitation of CVE-2026-44112 could allow an attacker to tamper with configuration, plant backdoors, and establish persistent control over the compromised host, whereas CVE-2026-44113 could be weaponized to read system files, credentials, and internal artifacts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The exploitation chain unfolds over four steps -

* A malicious plugin, prompt injection, or compromised external input gains code execution inside the OpenShell sandbox.
* Leverage CVE-2026-44113 and CVE-2026-44115 to expose credentials, secrets, and sensitive files.
* Exploit CVE-2026-44118 to obtain owner-level control of the agent runtime.
* Use CVE-2026-44112 to plant backdoors or make configuration changes and set up persistence.

The root cause for CVE-2026-44118, per the cybersecurity company, stems from the fact that OpenClaw trusts a client-controlled ownership flag called senderIsOwner, which signals whether the caller is authorized for owner-only tools, without validating it against the authenticated session.

"The MCP loopback runtime now issues separate owner and non-owner bearer tokens and derives senderIsOwner exclusively from which token authenticated the request," OpenClaw detailed the fixes in an advisory for the flaw. "The spoofable sender-owner header is no longer emitted or trusted."

Following responsible disclosure, all four vulnerabilities have been addressed in OpenClaw version 2026.4.22. Security researcher Vladimir Tokarev has been credited with discovering and reporting the issues. Users are advised to update to the latest version to stay protected against potential threats.

"By weaponizing the agent's own privileges, an adversary moves through data access, privilege escalation, and persistence -- using the agent as their hands inside the environment," Cyera said. "Each step looks like normal agent behavior to traditional controls, broadening blast radius and making detection significantly harder."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data theft](https://thehackernews.com/search/label/data%20theft), [OpenClaw](https://thehackernews.com/search/label/OpenClaw), [OpenShell](https://thehackernews.com/search/label/OpenShell), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Sandbox Escape](https://thehackernews.com/search/label/Sandbox%20Escape), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](data:image/svg+xml;base64... "30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign")

30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](https:...