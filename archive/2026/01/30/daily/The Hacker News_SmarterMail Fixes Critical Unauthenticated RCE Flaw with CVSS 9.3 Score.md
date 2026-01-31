---
title: SmarterMail Fixes Critical Unauthenticated RCE Flaw with CVSS 9.3 Score
url: https://thehackernews.com/2026/01/smartermail-fixes-critical.html
source: The Hacker News
date: 2026-01-30
fetch_date: 2026-01-31T04:05:15.231175
---

# SmarterMail Fixes Critical Unauthenticated RCE Flaw with CVSS 9.3 Score

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

# [SmarterMail Fixes Critical Unauthenticated RCE Flaw with CVSS 9.3 Score](https://thehackernews.com/2026/01/smartermail-fixes-critical.html)

**Ravie Lakshmanan**Jan 30, 2026Vulnerability / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg68yf4tK-m7j1I6zRCo-SBeQ4cCXmLiwvPRMoEXS_I8m7V53UUmULEbWr2vVAEJd34U0hknt8J5wnzcNv1kGayBLApw6mu0UmRZRyCstoXJAteTDrnRZBnoh5n3ROzBarjsRgPXeV_1WDsxQmg5ysAETrtYI3L9oNWnX246xTksVuWWqi34CzJCJnFc0uv/s1700-e365/smartertools.jpg)

SmarterTools has addressed two more security flaws in SmarterMail email software, including one critical security flaw that could result in arbitrary code execution.

The vulnerability, tracked as **CVE-2026-24423**, carries a CVSS score of 9.3 out of 10.0.

"SmarterTools SmarterMail versions prior to build 9511 contain an unauthenticated remote code execution vulnerability in the ConnectToHub API method," according to a [description of the flaw](https://www.cve.org/CVERecord?id=CVE-2026-24423) in CVE.org.

"The attacker could point the SmarterMail to the malicious HTTP server, which serves the malicious OS [operating system] command. This command will be executed by the vulnerable application."

watchTowr researchers Sina Kheirkhah and Piotr Bazydlo, [CODE WHITE GmbH's Markus Wulftange](https://code-white.com/public-vulnerability-list/), and [VulnCheck's Cale Black](https://www.vulncheck.com/advisories/smartertools-smartermail-unauthenticated-rce-via-connecttohub-api) have been credited with discovering and reporting the vulnerability.

The security hole has been addressed in version Build 9511, released on January 15, 2026. The same build also patches another critical flaw ([CVE-2026-23760](https://thehackernews.com/2026/01/smartermail-auth-bypass-exploited-in.html), CVSS score: 9.3) that has since come under active exploitation in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

In addition, SmarterTools has shipped fixes to plug a medium-severity security vulnerability (CVE-2026-25067, CVSS score: 6.9) that could allow an attacker to facilitate NTLM relay attacks and unauthorized network authentication.

It has been described as a case of unauthenticated path coercion affecting the background-of-the-day preview endpoint.

"The application base64-decodes attacker-supplied input and uses it as a filesystem path without validation," VulnCheck [noted](https://www.vulncheck.com/advisories/smartertools-smartermail-unauthenticated-background-of-the-day-path-coercion) in an alert.

"On Windows systems, this allows UNC [Universal Naming Convention] paths to be resolved, causing the SmarterMail service to initiate outbound SMB authentication attempts to attacker-controlled hosts. This can be abused for credential coercion, NTLM relay attacks, and unauthorized network authentication."

The vulnerability has been [patched](https://www.smartertools.com/smartermail/release-notes/current) in Build 9518, released on January 22, 2026. With two vulnerabilities in SmarterMail coming under active exploitation over the past week, it's essential that users update to the latest version as soon as possible.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [email security](https://thehackernews.com/search/label/email%20security), [network security](https://thehackernews.com/search/label/network%20security), [NTLM](https://thehackernews.com/search/label/NTLM), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [SmarterMail](https://thehackernews.com/search/label/SmarterMail), [SMB](https://thehackernews.com/search/label/SMB), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [windows security](https://thehackernews.com/search/label/windows%20security)

Trending News

[![Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites](data:image/svg+xml;base64... "Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites")

Google Gemini Prompt Injection Flaw Exposed Private Calendar Data via Malicious Invites](https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html)

[![Hackers Use LinkedIn Messages to Spread RAT Malware Through DLL Sideloading](data:image/svg+xml;base64... "Hackers Use LinkedIn Messages to Spread RAT Malware Through DLL Sideloading")

Hackers Use LinkedIn Messages to Spread RAT Malware Through DLL Sideloading](https://thehackernews.com/2026/01/hackers-use-linkedin-messages-to-spread.html)

[![Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution](data:image/svg+xml;base64... "Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution")

Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution](https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html)

[![CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution](data:image/svg+xml;base64... "CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution")

CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution](https://thehackernews.com/2026/01/certcc-warns-binary-parser-bug-allows.html)

[![LastPass Warns of Fake Maintenance Messages Targeting Users’ Master Passwords](data:image/svg+xml;base64... "LastPass Warns of Fake Maintenance Messages Targeting Users’ Master Passwords")

LastPass Warns of Fake Maintenance Messages Targeting Users' ...