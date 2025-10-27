---
title: Multiple Vulnerabilities Reported in Checkmk IT Infrastructure Monitoring Software
url: https://thehackernews.com/2022/11/multiple-vulnerabilities-reported-in.html
source: The Hacker News
date: 2022-11-03
fetch_date: 2025-10-03T21:41:18.366662
---

# Multiple Vulnerabilities Reported in Checkmk IT Infrastructure Monitoring Software

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Multiple Vulnerabilities Reported in Checkmk IT Infrastructure Monitoring Software](https://thehackernews.com/2022/11/multiple-vulnerabilities-reported-in.html)

**Nov 02, 2022**Ravie Lakshmanan

[![Checkmk IT Infrastructure Monitoring Software](data:image/png;base64... "Checkmk IT Infrastructure Monitoring Software")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhI2Y4IexjEy_dEZhKX-qVA_kkb6Euvy-4pZaloixMTfG4TgnhSib69Ehz66ud9_TD4tZsol2Y4nnKuOzXx2ZTKLl3GoBBOpTViIOUdjyBFrtKKAtCZRgPlMG3mijbUbG1Hg7E_Wpi7vSJOcU07PJAXs04q9MKwuIh9EmcoQJTD7a2bA_Zk87uGTKFQ/s790-rw-e365/code.jpg)

Multiple vulnerabilities have been disclosed in Checkmk IT Infrastructure monitoring software that could be chained together by an unauthenticated, remote attacker to fully take over affected servers.

"These vulnerabilities can be chained together by an unauthenticated, remote attacker to gain code execution on the server running Checkmk version 2.1.0p10 and lower," SonarSource researcher Stefan Schiller [said](https://blog.sonarsource.com/checkmk-rce-chain-1/) in a technical analysis.

Checkmk's open source edition of the monitoring tool is based on [Nagios Core](https://thehackernews.com/2021/09/new-nagios-software-bugs-could-let.html) and offers integrations with [NagVis](https://docs.checkmk.com/latest/en/nagvis.html) for the visualization and generation of topological maps of infrastructures, servers, ports, and processes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

According to its Munich-based developer tribe29 GmbH, its Enterprise and Raw editions are used by [over 2,000 customers](https://checkmk.com/company/our-customers), including Airbus, Adobe, NASA, Siemens, Vodafone, and others.

[![Checkmk IT Infrastructure Monitoring Software](data:image/png;base64... "Checkmk IT Infrastructure Monitoring Software")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKZacrzMt8yIJBo9B1JyrGh7UlrWCAtXSoIgCvsDax3bNLKzez5RQZbWbe_1k37Fzp39sj2aThwH33WfhXP9Kr5lR0u7GLYK9bFE07mIvzn_IiNe9Jsylnz3RycPuM9jg_HUbJmmCw_uqJywgmG1WVIyovxJ4h6FGsKKu7RRdpBME3bHyjv0Bp3hWB/s790-rw-e365/flaw.jpg)

The four vulnerabilities, which consist of two Critical and two Medium severity bugs, are as follows -

* A [code injection flaw](https://checkmk.com/werk/14383) in watolib's auth.php (CVSS score: 9.1)
* An [arbitrary file read flaw](https://checkmk.com/werk/14291) in NagVis (CVSS score: 9.1)
* A [command injection flaw](https://checkmk.com/werk/14384) Checkmk's [Livestatus](https://docs.checkmk.com/latest/en/livestatus.html) wrapper and Python API (CVSS score: 6.8), and
* A [server-side request forgery (SSRF) flaw](https://checkmk.com/werk/14385) in the host registration API (CVSS score: 5.0)

While these shortcomings on their own have a limited impact, an adversary can chain the issues, starting with the [SSRF flaw](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery) to access an endpoint only reachable from localhost, using it to bypass authentication and read a configuration file, ultimately gaining access to the Checkmk GUI.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This access can further be turned into remote code execution by exploiting a Code Injection vulnerability in a Checkmk GUI subcomponent called watolib, which generates a file named auth.php required for the NagVis integration," Schiller explained.

Following responsible disclosure on August 22, 2022, the four vulnerabilities have been patched in Checkmk version 2.1.0p12 released on September 15, 2022.

The findings follow the discovery of multiple flaws in other monitoring solutions like [Zabbix](https://thehackernews.com/2022/02/cisa-alerts-on-actively-exploited-flaws.html) and [Icinga](https://blog.sonarsource.com/path-traversal-vulnerabilities-in-icinga-web/) since the start of the year, which could have been exploited to compromise the servers by running arbitrary code.

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

[Checkmk](https://thehackernews.com/search/label/Checkmk)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials...