---
title: New Fragnesia Linux Kernel LPE Grants Root Access via Page Cache Corruption
url: https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html
source: The Hacker News
date: 2026-05-14
fetch_date: 2026-05-15T05:53:28.414868
---

# New Fragnesia Linux Kernel LPE Grants Root Access via Page Cache Corruption

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

# [New Fragnesia Linux Kernel LPE Grants Root Access via Page Cache Corruption](https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html)

**Ravie Lakshmanan**May 14, 2026Vulnerability / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZEVPJhl5rAx5o22-s1GQ6E1KKHMlOsazAfObgwK72r5EGxr52OkNRHHQXJdHt39DQop0SAhxE_t9nMKgXxHNgYv1zyB-ZR1IqCIKUK2feTpx1swr4dZzKLpZ5uldjrOAX6qH-wYnUfRWieA2xQWPbAUB1JpXhkBGq4AA0Ft07F7MFqZSHCS9SMR6uXjoC/s1700-e365/linux-2.jpg)

Details have emerged about a new variant of the recent [Dirty Frag](https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html) Linux local privilege escalation (LPE) vulnerability that allows local attackers to gain root access, making it the third such bug to be identified in the kernel within a span of two weeks.

Codenamed **[Fragnesia](https://github.com/v12-security/pocs/blob/main/fragnesia/README.md)**, the security vulnerability is tracked as CVE-2026-46300 (CVSS score: 7.8) and is rooted in the Linux kernel's XFRM ESP-in-TCP subsystem. It was discovered by researcher William Bowling of the V12 security team.

"The vulnerability allows unprivileged local attackers to modify read-only file contents in the kernel page cache and achieve root privileges through a deterministic page-cache corruption primitive," Google-owned Wiz [said](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

Advisories have been released by multiple Linux distributions -

* [AlmaLinux](https://almalinux.org/blog/2026-05-13-fragnesia-cve-2026-46300/)
* [Amazon Linux](https://aws.amazon.com/security/security-bulletins/rss/2026-029-aws/)
* [CloudLinux](https://blog.cloudlinux.com/fragnesia-mitigation-and-kernel-update)
* [Debian](https://security-tracker.debian.org/tracker/CVE-2026-46300)
* [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-46300)
* [Red Hat Enterprise Linux](https://access.redhat.com/security/cve/cve-2026-46300)
* [SUSE](https://www.suse.com/security/cve/CVE-2026-46300.html)
* [Ubuntu](https://ubuntu.com/security/CVE-2026-46300)

"This is a separate bug in the ESP/XFRM from Dirty Frag which has received its own patch," V12 said. "However, it is in the same surface and the mitigation is the same as for Dirty Frag. It abuses a logic bug in the Linux XFRM ESP-in-TCP subsystem to achieve arbitrary byte writes into the kernel page cache of read-only files, without requiring any race condition."

Fragnesia is similar to [Copy Fail](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/) and [Dirty Frag](https://www.automox.com/blog/dirty-frag-what-you-need-to-know-and-how-to-respond) (aka Copy Fail 2) in that it immediately yields root on all major distributions by achieving a memory write primitive in the kernel and corrupting the page cache memory of the /usr/bin/su binary. A proof-of-concept (PoC) exploit has been released by V12.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1NJaK0nCMXjJwS7xgaP032Qftq9s8wBWBP8BBqIvKk4s5HNcp-kesbeXWBBOvEJNegDhIs1Szf8eAM9_TECR1kpI8etIwdNu7SxAXlEkgA0JebWupE9dIDUZXzlms2I9Oo1GtcPGdWYzwYYEOJh64XEVdSylsqMLKspRKz6jlW3shyphenhyphenztanz8UcZHESZa8/s1700-e365/linux.gif)

"Customers who have already applied the Dirty Frag mitigation need no further action until patched kernels are released," CloudLinux maintainers said. Red Hat [said](https://access.redhat.com/security/vulnerabilities/RHSB-2026-003) it's performing an assessment to confirm if existing mitigations extend to CVE-2026-46300.

Wiz also noted that AppArmor restrictions on unprivileged user namespaces may serve as a partial mitigation, requiring additional bypasses for successful exploitation. However, unlike Dirty Frag, no host-level privileges are required.

"A patch is available, and while no in-the-wild exploitation has been observed at this time, we urge users and organizations to apply the patch as soon as possible by running update tools," Microsoft [said](https://x.com/MsftSecIntel/status/2054701609024934064). "If patching is not possible at this point, consider applying the same mitigations for Dirty Frag."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

This includes disabling esp4, esp6, and related xfrm/IPsec functionality, restricting unnecessary local shell access, hardening containerized workloads, and increasing monitoring for abnormal privilege escalation activity.

The development comes as a threat actor named "berz0k" has been observed advertising on cybercrime forums a zero-day Linux LPE exploit for $170,000, claiming it works on multiple major Linux distributions.

"The threat actor claims the vulnerability is TOCTOU-based (Time-of-Check Time-of-Use), capable of stable local privilege escalation without causing system crashes, and leverages a shared object (.so) payload dropped into the /tmp directory," ThreatMon [said](https://x.com/MonThreat/status/2054516027912769579) in a post on X.

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

[cybersecurity](htt...