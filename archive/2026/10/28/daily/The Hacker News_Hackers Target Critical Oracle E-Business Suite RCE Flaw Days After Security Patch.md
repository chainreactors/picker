---
title: Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch
url: https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html
source: The Hacker News
date: 2026-10-28
fetch_date: 2026-10-29T07:52:55.288996
---

# Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch](https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html)

**Ravie Lakshmanan**Oct 28, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBB03AGS7veiAqQ7-xPeadzhhaRvDmhOlLgQcDN0y-r1na_us5yomWjBEXCbwbw8OW_o8SSGjjqk4VZFQ4ZxLiWKQPZxlcBkzJ5lv3OlEV0rOETUKyQzWoZ74LGpSjOjrScmk1rVf0OhRmDACHG3jwSDfBnnta75I_3s_nuoWGZmcfg7NZfHBp_PEIl8aj/s1700-nu-rw-lo-l85-e365/oracle-hack.jpg)

Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber.

The vulnerability in question is **[CVE-2026-101767](https://nvd.nist.gov/vuln/detail/cve-2026-101767)** (CVSS score: 9.8) , a case of improper authentication in the Oracle Application Object Library of Oracle E-Business Suite. It was patched by Oracle last week as part of its [Critical Patch Update](https://www.oracle.com/security-alerts/cpuoct2026.html).

Security researchers Brandon Peterson, Jimi Sebree, and Noah King of Horizon3.ai have been credited with discovering and reporting the flaw to Oracle on July 24, 2026.

"Our Oracle E-Business Suite decoys recorded exploratory exploits against CVE-2026-101767, an unauthenticated SQL injection in EBS's Thin Client Framework servlet that chains to remote code execution, this morning, October 27," Defused Cyber [said](https://x.com/DefusedCyber/status/2115099999973364147) in an X post.

In an advisory for the vulnerability, Horizon3.ai described it as an unauthenticated SQL injection vulnerability that could be chained to achieve remote code execution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

"The vulnerability allows an attacker with network access to the affected Thin Client Framework (TCF) servlet to execute SQL as the APPS database user, then run operating system commands as the EBS application account," the cybersecurity company [said](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/).

Specifically, an attacker can issue a crafted request to the vulnerable TCF servlet at "/OA\_HTML/AppsTCFServer" to run SQL with the privileges of the APPS database user and ultimately enable system command execution with the privileges of the EBS application account.

Successful exploitation of CVE-2026-101767 can permit an attacker to read or modify application data accessible to APPS and execute commands on the application host.

"Depending on the deployment, affected data may include financial, payroll, HR, and procurement records. Operating system access is governed by the permissions of the compromised EBS application account," Horizon3.ai warned.

While internet-facing EBS deployments present the most risk, internal EBS systems can also be exploited if an attacker can reach the vulnerable servlet from a compromised system or another accessible network segment.

Users are advised to update to the latest version as soon as possible. If immediate patching is not an option, the following workarounds can be applied -

* Remove /OA\_HTML/AppsTCFServer, associated with oracle.apps.fnd.tcf.SocketServer, from the EBS URL firewall allowlist.
* Restrict access to the EBS web tier to trusted networks.
* Monitor the EBS application host and database for signs of compromise.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Horizon3.ai has also shared the below indicators of compromise -

* Unauthenticated POST requests to /OA\_HTML/AppsTCFServer that instantiate the Gantt data-server class (oracle.apps.jtf.gantt.server.GanttDataServer), followed by backend database activity.
* SQL reconnaissance shortly after unauthenticated web requests (database version, current user, directory objects).
* Unexpected files in $APPLPTMP and the oracle account spawning /bin/sh via the Concurrent Manager to run OS commands.

Vulnerabilities in EBS are a hot target for attackers. Over the past year, two critical flaws in the same product ([CVE-2025-61882](https://thehackernews.com/2025/10/oracle-ebs-under-fire-as-cl0p-exploits.html) and [CVE-2026-46817](https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html), CVSS scores: 9.8) have come under active exploitation, with the former leveraged by the Cl0p ransomware and extortion crew.

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

[cyber attacks](https://thehackernews.com/search/label/cyber%20attacks), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Unpatched Broadcom Wi-Fi Flaw Lets Attackers in Range Run Code as Root on Routers](https://thehackernews.com/2026/10/unpatched-broadcom-wi-fi-flaw-lets.html)

[![The Hacker News](data:image/svg+xml;base64...)

OpenCode Console Breach May Have Exposed OpenAI, Anthropic, and Google API Keys](https://theh...