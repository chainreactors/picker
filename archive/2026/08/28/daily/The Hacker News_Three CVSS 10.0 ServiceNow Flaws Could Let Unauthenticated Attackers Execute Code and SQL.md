---
title: Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL
url: https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html
source: The Hacker News
date: 2026-08-28
fetch_date: 2026-08-29T08:33:12.856648
---

# Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)

**Swati Khandelwal**Aug 28, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitiido-BqtV-H4U0qEAovU_m3NGb3PHF5O3IEh53W_rllGDplhA8aluEKIUULFq3L7iNQue-NLxQDR3wSF7PaaAhGg14rWdqHoB6jBZC1YfslM0wyj5xhESZKTbIxgjO_lnZqVOrKx_E2hK-wXtE85EPJW-pV8D3eMv9CWgMF8eXzsJgq3xevdBY9hCs0/s1700-e365/servicenow.jpg)

ServiceNow has released patches for four security flaws impacting the ServiceNow AI Platform, three of them rated 10.0 on the CVSS scoring system and exploitable, in certain circumstances, by an unauthenticated attacker.

The company said it deployed a security update to hosted instances and provided the update to its partners and self-hosted customers, which leaves organizations that run their own instances to apply the fixes themselves.

The advisory was published on August 27, 2026, and the four vulnerabilities are listed below -

* [CVE-2026-18885](https://www.cve.org/CVERecord?id=CVE-2026-18885) (CVSS score: 10.0) - A code injection vulnerability in the GraphQL Composite Data API that could enable an unauthenticated user to execute arbitrary code and gain access to, or modify, instance data
* [CVE-2026-18886](https://www.cve.org/CVERecord?id=CVE-2026-18886) (CVSS score: 10.0) - An improper access control vulnerability in the system configuration image upload processor that could enable an unauthenticated user to create or modify instance data, resulting in privilege escalation
* [CVE-2026-74820](https://www.cve.org/CVERecord?id=CVE-2026-74820) (CVSS score: 10.0) - A SQL injection vulnerability reached through a dynamic schema ORDER BY clause that could enable an unauthenticated user to execute arbitrary SQL statements against the instance's underlying database
* CVE-2026-6876 (CVSS score: 8.7) - A sandbox escape in the Now Platform that could allow an unauthenticated user to execute arbitrary code

The three maximum-severity flaws share the vector `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H`, describing a network-reachable attack of low complexity that requires no privileges and no user interaction, and that carries high impact to confidentiality, integrity, and availability in both the vulnerable component and the systems connected to it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The advisory follows CVE-2026-6875, a pre-authentication sandbox escape in the same platform. Searchlight Cyber reported that flaw to ServiceNow on April 1, 2026. ServiceNow published the advisory for it on July 13.

Threat intelligence firm Defused said days after the July advisory that it was observing in-the-wild exploitation of CVE-2026-6875. It subsequently issued a correction stating that the captured payload matched Searchlight Cyber's [published proof-of-concept (PoC) exploit](https://www.slcyber.io/research/smashing-the-servicenow-sandbox-pre-authentication-rce).

"ServiceNow is aware of a cybersecurity company's recent publication regarding exploitation activity associated with a previously disclosed security vulnerability, identified as CVE-2026-6875," a ServiceNow spokesperson told The Hacker News. "Based on our investigation to date, we have not observed evidence that this activity is related to instances that ServiceNow hosts."

"We have provided updates and patches designed to address this issue, and we encourage our self-hosted and ServiceNow-hosted customers to apply the relevant patches if they have not already done so. In addition, we will continue to work directly with customers who need assistance in applying the patches," the spokesperson said.

The 10.0 ratings are ServiceNow's own. The company is the CVE Numbering Authority for its products, and since April 15, 2026, NIST has enriched only vulnerabilities that appear in [CISA's Known Exploited Vulnerabilities catalog](https://thehackernews.com/2026/08/cisa-adds-six-exploited-flaws-to-kev.html), affect federal government software, or are designated critical under Executive Order 14028.

None of the four flaws appeared in the catalog as of August 28, 2026, leaving ServiceNow's ratings as the only severity assessment on record.

ServiceNow rated all three of the new maximum-severity flaws at low attack complexity. It scored [the sandbox escape reported exploited](https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html) in July at 9.5 under the same version of the scoring system, with every metric identical to the three except attack complexity, which it set to high.

ServiceNow lists the following versions as affected in [its August advisory](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3152242) -

* **Xanadu** - any version before Patch 11 Hot Fix 7a
* **Yokohama** - any version before Patch 12 Hot Fix 3b, and any version before Patch 13 Hot Fix 4
* **Zurich** - any version before Patch 7b Hot Fix 3, Patch 8 Hot Fix 5, Patch 9 Hot Fix 6, Patch 10 Hot Fix 2m (m-branch), Patch 10 Hot Fix 3 (standard), Patch 11, or Patch 12
* **Australia** - any version before Patch 2 Hot Fix 3, Patch 3 Hot Fix 2, Patch 3m, Patch 4, or Patch 5

The record for CVE-2026-18886 marks "Any version before Australia Patch 5" with a status of unknown, where the records for the other three mark the same version as affected. All four set a default product status of unaffected, so a release the list does not name falls outside the affected set.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

ServiceNow describes CVE-2026-6876 as an issue that could allow an unauthenticated user to execute arbitrary code within the Now Platform, while the CVSS vector it assigned to the same flaw specifies `PR:L`, or low privileges required.

That vector also records no impact to systems beyond the vulnerable...