---
title: Chaos Mesh Critical GraphQL Flaws Enable RCE and Full Kubernetes Cluster Takeover
url: https://thehackernews.com/2025/09/chaos-mesh-critical-graphql-flaws.html
source: The Hacker News
date: 2025-09-17
fetch_date: 2025-10-02T20:16:17.184435
---

# Chaos Mesh Critical GraphQL Flaws Enable RCE and Full Kubernetes Cluster Takeover

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

# [Chaos Mesh Critical GraphQL Flaws Enable RCE and Full Kubernetes Cluster Takeover](https://thehackernews.com/2025/09/chaos-mesh-critical-graphql-flaws.html)

**Sep 16, 2025**Ravie LakshmananVulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrG4Y8oTdTQpISwTEucKZYJRdaCUFxv2UT9GVe0bfrSjRIsIypm5px4yBrNL2ZLx04HoxlZ1qq0lYUZ41lCbN7PISWgkl3O3v-q-RTWJko8qieWau0owLF7R0_tif35kJdo4Zbi4P8hfgJWJqHnfsSt_uQ6BVXu37vNW439tpdvi3pSytEIi9QWRiGKi1P/s790-rw-e365/mesh.jpg)

Cybersecurity researchers have disclosed multiple critical security vulnerabilities in Chaos Mesh that, if successfully exploited, could lead to cluster takeover in Kubernetes environments.

"Attackers need only minimal in-cluster network access to exploit these vulnerabilities, execute the platform's fault injections (such as shutting down pods or disrupting network communications), and perform further malicious actions, including stealing privileged service account tokens," JFrog [said](https://jfrog.com/blog/chaotic-deputy-critical-vulnerabilities-in-chaos-mesh-lead-to-kubernetes-cluster-takeover/) in a report shared with The Hacker News.

[Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh) is an open-source cloud-native [Chaos Engineering platform](https://chaos-mesh.org/docs/) that offers various types of fault simulation and simulates various abnormalities that might occur during the software development lifecycle.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The issues, collectively called Chaotic Deputy, are listed below -

* **[CVE-2025-59358](https://nvd.nist.gov/vuln/detail/CVE-2025-59358)** (CVSS score: 7.5) - The Chaos Controller Manager in Chaos Mesh exposes a GraphQL debugging server without authentication to the entire Kubernetes cluster, which provides an API to kill arbitrary processes in any Kubernetes pod, leading to cluster-wide denial-of-service
* **[CVE-2025-59359](https://nvd.nist.gov/vuln/detail/CVE-2025-59359)** (CVSS score: 9.8) - The cleanTcs mutation in Chaos Controller Manager is vulnerable to operating system command injection
* **[CVE-2025-59360](https://nvd.nist.gov/vuln/detail/CVE-2025-59360)** (CVSS score: 9.8) - The killProcesses mutation in Chaos Controller Manager is vulnerable to operating system command injection
* **[CVE-2025-59361](https://nvd.nist.gov/vuln/detail/CVE-2025-59361)** (CVSS score: 9.8) - The cleanIptables mutation in Chaos Controller Manager is vulnerable to operating system command injection

An in-cluster attacker, i.e., a threat actor with initial access to the cluster's network, could chain CVE-2025-59359, CVE-2025-59360, CVE-2025-59361, or with CVE-2025-59358 to perform remote code execution across the cluster, even in the default configuration of Chaos Mesh.

JFrog said the vulnerabilities stem from insufficient authentication mechanisms within the Chaos Controller Manager's GraphQL server, allowing unauthenticated attackers to run arbitrary commands on the Chaos Daemon, resulting in cluster takeover.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Threat actors could then leverage the access to potentially exfiltrate sensitive data, disrupt critical services, or even move laterally across the cluster to escalate privileges.

Following responsible disclosure on May 6, 2025, all the identified shortcomings were addressed by Chaos Mesh with the release of [version 2.7.3](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.7.3) on August 21.

Users are advised to update their installations to the latest version as soon as possible. If immediate patching is not an option, it's recommended to restrict network traffic to the Chaos Mesh daemon and API server, and avoid running Chaos Mesh in open or loosely secured environments.

"Platforms such as Chaos Mesh give, by design, complete control of the Kubernetes cluster to the platform," Shachar Menashe, vice president of security research at JFrog, said in a statement shared with The Hacker News. "This flexibility can become a critical risk when vulnerabilities such as Chaotic Deputy are discovered."

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

[Chaos Engineering](https://thehackernews.com/search/label/Chaos%20Engineering)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Command Injection](https://thehackernews.com/search/label/Command%20Injection)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)[Open Source](https://thehackernews.com/search/label/Open%20Source)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWin...