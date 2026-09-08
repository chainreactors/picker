---
title: N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw
url: https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html
source: The Hacker News
date: 2026-09-07
fetch_date: 2026-09-08T06:42:27.052896
---

# N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw

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

# [N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw](https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html)

**Swati Khandelwal**Sep 07, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOtysh_bb-hej1pQzey0RUhPD2w29ONlPDQMzE9Nc4lM529hKaHhuLKfGXEnqVZyUkMKhJchEeoN1clSKo3-opm2_BQkN6FJ72xBZOZwxX6sTwU4Zzk_j6taOwBpioZOnolR9idUjpydUlQ84TQ9pdWUlUm61JH0Xh8-6_0fo3VieeW3xVQwk4UvXcSu4/s1700-nu-rw-lo-l85-e365/nable.jpg)

Every on-premises N-central build below 2026.3.1.14 — including servers updated to Hotfix 3 a day earlier — needs Hotfix 4. N-able's incident notice says the flaw has been exploited in the wild; its release notes say that is unconfirmed.

N-able has released its [fourth hotfix](https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/) in five weeks for the N-central remote monitoring and management (RMM) platform, this time for a maximum-severity vulnerability that could allow remote code execution on the N-central server without authentication.

The company's own communications disagree on whether the flaw has already been exploited.

The vulnerability, tracked as [CVE-2026-86218](https://www.cve.org/CVERecord?id=CVE-2026-86218), carries a CVSS 4.0 score of 10.0, assigned by N-able as the CVE Numbering Authority, and is classed as a static code injection weakness (CWE-96).

It affects every N-central build before 2026.3.1.14, the build shipped as 2026.3 Hotfix 4 in the early hours of September 6 (UTC). That includes servers already updated to [Hotfix 3](https://status.n-able.com/2026/09/05/n-central-2026-3-hotfix-3-cve-2026-86206-and-cve-2026-86207/) (2026.3.1.13), which N-able had published a little over eight hours earlier for two flaws that it says are unrelated to the new one.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

N-able said hosted N-central (NCOD) instances have already been patched. On-premises customers are told to upgrade to 2026.3.1.14 immediately; the [release notes](https://documentation.n-able.com/N-central/Release_Notes/GA/Content/N-central_2026.3_HF4_Release_Notes.htm) list direct upgrade paths from 2025.4, 2026.1, 2026.2, 2026.3, and the 2026.3.1 hotfixes, and say agents do not need to be upgraded to be protected from this CVE.

The release notes, status post, and incident notice contain no indicators of compromise, no interim mitigation, and no detection guidance beyond a recommendation to audit N-central user accounts for unexpected users.

Huntress, which has been tracking attacks on N-central since August, has advised administrators to restrict inbound access to the console with IP allowlisting or a VPN and, where a server is still reachable from the internet, to consider taking it offline until the hotfix is applied.

On the question of exploitation, N-able's channels diverge. The Hotfix 4 release notes and status post state that a third party responsibly disclosed the vulnerability through the company's security disclosure program and that N-able has "no confirmations that this vulnerability has been exploited in production environments."

The same release notes on N-able's documentation site also describe it as a "critical zero-day vulnerability," a term N-able does not define.

N-able's [incident notice](https://uptime.n-able.com/event/201814/) on its uptime status page goes further. It says a third, independent security researcher alerted the company to a new vulnerability unrelated to the previously disclosed CVEs and that, unlike those, the newly identified flaw "has been observed being exploited in the wild."

The notice does not say who observed the exploitation, where, or when, and N-able has not attributed the activity to any actor. As of September 7, the incident was still listed as open on N-able's status page, as mirrored by the status-page aggregator [IsDown](https://isdown.app/status/n-able/incidents/650347-urgent-n-central-immediate-hotfix-required).

The Hacker News has reached out to N-able for clarification on which statement is current and what evidence of exploitation the company holds.

[Huntress said](https://www.huntress.com/blog/n-able-vulnerability-exploitation) it cannot settle the question from its own data. The company began investigating on September 4 after a customer's fully patched N-central production environment was compromised. It said it reproduced a proof-of-concept exploit chain against build 2026.3.1.10 that may use one or both of the two flaws later fixed in Hotfix 3, but the appliance's logs had already rotated, leaving it "unable to say whether this new CVE was the vulnerability exploited" in that intrusion.

The hotfix is the fourth N-able has issued for the 2026.3 line since August 2 and covers the third distinct set of vulnerabilities:

* **Hotfix 1 (2026.3.1.7), August 2** — [CVE-2026-18577](https://thehackernews.com/2026/08/n-able-says-attackers-take-over-n.html), an incomplete fix for CVE-2026-18556 that still allowed authentication bypass and account takeover; exploited in the wild
* **Hotfix 2 (2026.3.1.10), August 6** — [additional hardening](https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html) for a related attack path
* **Hotfix 3 (2026.3.1.13), September 5** — [CVE-2026-86206](https://www.cve.org/CVERecord?id=CVE-2026-86206), unauthorized access to internal APIs through the access control filter, and [CVE-2026-86207](https://www.cve.org/CVERecord?id=CVE-2026-86207), an authentication bypass in internal-only APIs
* **Hotfix 4 (2026.3.1.14), September 6** — CVE-2026-86218, pre-authentication remote code execution

N-able described the two Hotfix 3 flaws as "high-CVSS-rated" vulnerabilities that could allow an unauthorized party to bypass authentication controls and gain full access to the platform.

Its own CVE records score CVE-2026-86207 at 7.7 (High) and CVE-2026-86206 ...