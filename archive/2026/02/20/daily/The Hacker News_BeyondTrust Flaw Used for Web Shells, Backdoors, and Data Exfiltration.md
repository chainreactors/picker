---
title: BeyondTrust Flaw Used for Web Shells, Backdoors, and Data Exfiltration
url: https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html
source: The Hacker News
date: 2026-02-20
fetch_date: 2026-02-21T04:01:09.907176
---

# BeyondTrust Flaw Used for Web Shells, Backdoors, and Data Exfiltration

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [BeyondTrust Flaw Used for Web Shells, Backdoors, and Data Exfiltration](https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html)

**Ravie Lakshmanan**Feb 20, 2026Vulnerability / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjMKRB_5ww1tcCh0no0OxbE4Bhcg4nVEe4y-cHBLi03rhgJFM_8y6EatBQ_L00yCHRNRJmaiVq3fMGo2NUAjPLCbcXdWG2wqAG4qZtT0MAedKcFEiXHr_g2gRd0GuTc_wD8X5_Ss0Azn1YhZnEXO88hApw52GJI3_6hnJmf8aNueuEYFCLtdhaHBSg8i0a/s1700-e365/bt-main.jpg)

Threat actors have been observed exploiting a recently disclosed critical security flaw impacting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) products to conduct a wide range of malicious actions, including deploying VShell and

The vulnerability, tracked as [**CVE-2026-1731**](https://thehackernews.com/2026/02/researchers-observe-in-wild.html) (CVSS score: 9.9), allows attackers to execute operating system commands in the context of the site user.

In a report published Thursday, Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/) it detected the security flaw being actively exploited in the wild for network reconnaissance, web shell deployment, command-and-control (C2), backdoor and remote management tool installs, lateral movement, and data theft.

The campaign has targeted financial services, legal services, high technology, higher education, wholesale and retail, and healthcare sectors across the U.S., France, Germany, Australia, and Canada.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The cybersecurity company described the vulnerability as a case of sanitization failure that enables an attacker to leverage the affected "thin-scc-wrapper" script that's reachable via WebSocket interface to inject and execute arbitrary shell commands in the context of the site user.

"While this account is distinct from the root user, compromising it effectively grants the attacker control over the appliance's configuration, managed sessions and network traffic," security researcher Justin Moore said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEA8ao30WZa4rOXWsMMqdCbBscgV9n3Hhe7ShhHFJ3FmkBebjP-qWMx8CtZGyTix4U-RPfupjD089Lr8Jkrao5UYvrMiMaKXh5lEsVGMtuycpFsy0eNYTIskKYnRiG3MGAssJXxmx-Y34lbTJcHwx2hn6ltPc5d1rvoF1IFZ5wyQPCzIUjeFkml8GJCGFu/s1700-e365/bash.png)

The current scope of attacks exploiting the flaw range from reconnaissance to backdoor deployment -

* Using a custom Python script to gain access to an administrative account.
* Installing multiple web shells across directories, including a PHP backdoor that's capable of executing raw PHP code or running arbitrary PHP code without writing new files to disk, as well as a bash dropper that establishes a persistent web shell.
* Deploying malware such as [VShell](https://www.trellix.com/blogs/research/the-silent-fileless-threat-of-vshell/) and [Spark RAT](https://thehackernews.com/2023/01/chinese-hackers-utilize-golang-malware.html).
* Using out-of-band application security testing (OAST) techniques to validate successful code execution and fingerprint compromised systems.
* Executing commands to stage, compress and exfiltrate sensitive data, including configuration files, internal system databases and a full PostgreSQL dump, to an external server.

"The relationship between CVE-2026-1731 and [CVE-2024-12356](https://thehackernews.com/2025/02/beyondtrust-zero-day-breach-exposes-17.html) highlights a localized, recurring challenge with input validation within distinct execution pathways," Unit 42 said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

"CVE-2024-12356's insufficient validation was using third-party software (postgres), while CVE-2026-1731's insufficient validation problem occurred in the BeyondTrust Remote Support (RS) and older versions of the BeyondTrust Privileged Remote Access (PRA) codebase."

With CVE-2024-12356 exploited by China-nexus threat actors like [Silk Typhoon](https://thehackernews.com/2025/03/china-linked-silk-typhoon-expands-cyber.html), the cybersecurity company noted that CVE-2026-1731 could also be a target for sophisticated threat actors.

The development comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [updated](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-1731&field_date_added_wrapper=all&field_cve=&sort_by=field_date_added&items_per_page=20&url=) its Known Exploited Vulnerabilities (KEV) catalog entry for CVE-2026-1731 to confirm that the bug has been exploited in ransomware campaigns.

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

[Android Smishing Vulnerability](https://thehackernews.com/search/label/Android%20Smishing%20Vulnerability), [BeyondTrust](https://thehackernews.com/search/label/BeyondTrust), [Command and Control](https://thehackernews.com/search/label/Command%20and%20Control), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data exfiltration](https://thehackernews.com/search/label/d...