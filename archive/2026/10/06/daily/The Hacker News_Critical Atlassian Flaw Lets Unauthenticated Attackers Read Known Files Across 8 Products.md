---
title: Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products
url: https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:35.703130
---

# Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products](https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html)

**Swati Khandelwal**Oct 06, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGQge2pd9O29G6qjsswRMYKnpM66wzyEWHOnRljkIZUZpCGVGACovyKIiji1HQ4jZOsypuaveJUBxx0r7-tT-Icd3COeo_prgm0TbMWDJBYFYpWHOC3lBjb8sZo6f2qWPkzeztOAjMW1CjrE_fDe3nWBU2FEOOjUWDpNUbtY1okTyx_iFE7xcI5jxOeiQ/s1700-nu-rw-lo-l85-e365/file.jpg)

A critical flaw in 8 Atlassian Data Center products, which customers host themselves, allows an attacker with no login access to read specific files in each product's web application root directory.

The attacker must already know a file's exact name and path and cannot list what the directory holds. Atlassian [disclosed the flaw](https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html), **CVE-2026-21589**, on October 5, rated it 9.3 out of 10, and listed a fixed version for each product.

The web application root directory is the folder on the server that holds the web application itself. In some configurations, it may contain sensitive files, which raises the risk, according to Atlassian.

Atlassian's cloud products affected by the flaw have already been patched, and cloud customers do not need to take any action.

Atlassian advises customers who cannot upgrade all at once to take the instance offline if possible. Any instance reachable from the public internet, including one that requires a login, should be restricted from outside network access until it is upgraded or a temporary blocking rule is in place.

### Affected Products and Fixed Versions

The flaw affects all versions of the 8 products before the fixed versions listed below. That may include versions that have reached end of life, according to Atlassian, which recommends upgrading to a fixed long-term support (LTS) version or later.

Atlassian listed these fixed versions as of October 6:

| Product | Fixed versions |
| --- | --- |
| [Bitbucket Data Center](https://jira.atlassian.com/browse/BSERV-20604) | 9.4.26, 10.2.8, 10.5.1 |
| [Confluence Data Center](https://jira.atlassian.com/browse/CONFSERVER-104488) | 9.2.26, 10.2.19 |
| [Jira Software Data Center](https://jira.atlassian.com/browse/JRASERVER-79546) | 9.12.40, 10.3.26, 11.3.12 |
| [Jira Service Management Data Center](https://jira.atlassian.com/browse/JSDSERVER-16809) | 5.12.40, 10.3.26, 11.3.12 |
| [Bamboo Data Center](https://jira.atlassian.com/browse/BAM-26567) | 10.2.24, 12.1.12 |
| [Crowd Data Center](https://jira.atlassian.com/browse/CWD-6610) | 6.3.7, 7.0.3, 7.1.7, 7.2.4 |
| [Crucible](https://jira.atlassian.com/browse/CRUC-8741) | 4.9.15 |
| [Fisheye](https://jira.atlassian.com/browse/FE-7583) | 4.9.15 |

For Crowd's 7.1 branch, the ticket's fix version field said 7.1.7. A table in the same ticket showed 7.1.6, which the ticket also listed as an affected version.

The [CVE record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/21xxx/CVE-2026-21589.json) Atlassian filed gave different numbers for 2 products. For Crowd, it listed 7.1.1, which the [Crowd 7.1 release notes](https://confluence.atlassian.com/crowd/crowd-7-1-release-notes-1652918282.html) date to November 27, 2025, more than 10 months before the flaw was disclosed. For Bamboo, one field said 10.2.4, while the record's own description said 10.2.24.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The CVE record also listed the Server editions of these products, Atlassian's older self-hosted line, which the advisory did not mention. It marked every version of Bamboo Server, Bitbucket Server, Confluence Server, and Crowd Server as affected and listed no fixed versions for them.

For Jira Software Server, the record listed versions from 9.12.40 as unaffected, for Jira Service Management Server from 5.12.40, and for Crucible Server and Fisheye Server from 4.9.15. It did not say whether Server licenses can run those versions.

Crowd has had no Server release since version 5.2 in September 2023, according to Atlassian's [Crowd release notes](https://confluence.atlassian.com/crowd/crowd-release-notes-199094.html), so none of the fixed Crowd versions are Server releases.

### If You Cannot Upgrade Yet

Atlassian labels the flaw a path traversal in the CVE record. In a path traversal, a request uses a specially built file path to reach files it should not.

Atlassian describes 3 temporary blocking rules, which it calls mitigations. All 3 block requests whose URL contains .. directly next to /, \ or ::, including URL-encoded forms.

Which ones apply depends on the product:

* **All 8 products:** a rule on a web application firewall (WAF) or reverse proxy that blocks matching URLs.
* **Confluence, Jira Software, Jira Service Management, Bamboo and Crowd:** a Tomcat RewriteValve rule, installed on each node, which must be shut down and restarted.
* **Bitbucket:** a rule in urlrewrite.xml, applied to every node, mirror and mirror farm node, followed by a restart.

Crucible and Fisheye have only the first option. The [advisory](https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html) gives the rule and the file changes for each one.

The mitigations "are limited and not a replacement for patching your instance," Atlassian says in its product tickets.

### Checking for Past Access

Atlassian said its affected cloud products have been patched and that its investigation has not found evidence of exploitation. Bitbucket Cloud is not affected.

The advisory does not say whether attacks on self-hosted instances have been seen. "Atlassian cannot confirm if your instances have been affected by this vulnerability," it says.

It tells customers to have th...