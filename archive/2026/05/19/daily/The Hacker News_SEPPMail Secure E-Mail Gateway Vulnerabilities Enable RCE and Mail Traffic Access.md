---
title: SEPPMail Secure E-Mail Gateway Vulnerabilities Enable RCE and Mail Traffic Access
url: https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html
source: The Hacker News
date: 2026-05-19
fetch_date: 2026-05-20T06:05:28.319008
---

# SEPPMail Secure E-Mail Gateway Vulnerabilities Enable RCE and Mail Traffic Access

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

# [SEPPMail Secure E-Mail Gateway Vulnerabilities Enable RCE and Mail Traffic Access](https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html)

**Ravie Lakshmanan**May 19, 2026Vulnerability / Email Security

[![SEPPMail Secure E-Mail Gateway Vulnerabilities](data:image/png;base64... "SEPPMail Secure E-Mail Gateway Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiortK4EUp9FwJsfVYW-j20LfpbM5qMNelk5-T8BbZ7dEcmBLXnqhWW9loE8GD6aexZv3h-xHEgn_N7ECjV8KXdcGwNxsbhCPP07COzt9c8BhMaVTF4OaSnKD2b98mJjsU1d57OXj2FQtOhKyeo6oPcT0-rrOi-_dKf1iielQQnhsprZ43tHyYFbiYhgFK8/s1700-e365/email-hacking.jpg)

Critical security vulnerabilities have been disclosed in [SEPPMail Secure E-Mail Gateway](https://www.seppmail.com/products/secure-email-gateway/), an enterprise-grade email security solution, that could be exploited to achieve remote code execution and enable an attacker to read arbitrary mails from the virtual appliance.

"These vulnerabilities could have been exploited to read all mail traffic or as an entry vector into the internal network," InfoGuard Labs researchers Dario Weiss, Manuel Feifel, and Olivier Becker [said](https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/) in a Monday report.

The list of identified flaws is as follows -

* **[CVE-2026-2743](https://www.cve.org/CVERecord?id=CVE-2026-2743)** (CVSS score: 10.0) - A path traversal vulnerability in the SeppMail User Web Interface's large file transfer (LFT) feature that could enable arbitrary file write, resulting in remote code execution.
* **[CVE-2026-7864](https://www.cve.org/CVERecord?id=CVE-2026-7864)** (CVSS score: 6.9) - An exposure of sensitive system information vulnerability that leaks server environment variables through an unauthenticated endpoint in the new GINA UI.
* **[CVE-2026-44125](https://www.cve.org/CVERecord?id=CVE-2026-44125)** (CVSS score: 9.3) - A missing authorization check vulnerability for multiple endpoints in the new GINA UI that allows unauthenticated remote attackers to access functionality that would otherwise require a valid session.
* **[CVE-2026-44126](https://www.cve.org/CVERecord?id=CVE-2026-44126)** (CVSS score: 9.2) - A deserialization of untrusted data vulnerability that allows unauthenticated remote attackers to execute code via a crafted serialized object.
* **[CVE-2026-44127](https://www.cve.org/CVERecord?id=CVE-2026-44127)** (CVSS score: 8.8) - An unauthenticated path traversal vulnerability in "/api.app/attachment/preview" that allows remote attackers to read arbitrary local files and trigger deletion of files in the targeted directory with the privileges of the "api.app" process.
* **[CVE-2026-44128](https://www.cve.org/CVERecord?id=CVE-2026-44128)** (CVSS score: 9.3) - An eval injection vulnerability that allows unauthenticated remote code execution by taking advantage of the fact that the /api.app/template feature directly passes user-supplied upldd parameter into a Perl eval() statement without any sanitization.
* **[CVE-2026-44129](https://www.cve.org/CVERecord?id=CVE-2026-44129)** (CVSS score: 8.3) - An improper neutralization of special elements used in a template engine vulnerability that allows remote attackers to execute arbitrary template expressions and potentially achieve remote code execution depending on the enabled template plugins.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

In a hypothetical attack scenario, a threat actor could exploit CVE-2026-2743 to overwrite the system's syslog configuration ("/etc/syslog.conf") by making use of the "nobody" user's write access to the file and ultimately obtain a Perl-based reverse shell. The end result is a complete takeover of the SEPPmail appliance, permitting the attacker to read all mail traffic and persist indefinitely on the gateway.

One significant hurdle that an attacker must overcome to achieve remote code execution is that [syslogd](https://linux.die.net/man/8/syslogd) re-reads the configuration only upon receiving the [SIGHUP](https://en.wikipedia.org/wiki/SIGHUP) (aka "signal hang up") signal. Syslogd is a Linux system daemon responsible for writing system messages to log files or a user's terminal.

"The appliance uses newsyslog for log rotation (e.g., leading to logfile.0), which runs every 15 minutes via cron," the researchers explained. "newsyslog rotates files that exceed a size limit and then automatically sends a SIGHUP to syslogd. By bloating log files like SEPPMaillog, which has a 10,000 KB limit in this case, we can force a rotation and a subsequent config reload. These can be filled by just sending web requests."

While CVE-2026-44128 is said to have been [fixed](https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html) by version 15.0.2.1, CVE-2026-44126 was addressed with the release of version 15.0.3. The remaining vulnerabilities have been patched in version 15.0.4.

The disclosure comes weeks after SEPPmail shipped updates to resolve another critical flaw ([CVE-2026-27441](https://www.cve.org/cverecord?id=CVE-2026-27441), CVSS score: 9.5) that could allow arbitrary operating system command execution.

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
[![Facebook Messenger](data:image/png;b...