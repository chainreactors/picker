---
title: Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored Credentials
url: https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html
source: The Hacker News
date: 2026-03-11
fetch_date: 2026-03-12T04:09:06.825755
---

# Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored Credentials

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored Credentials](https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html)

**Ravie Lakshmanan**Mar 11, 2026 Vulnerability / Application Security

[![n8n](data:image/png;base64... "n8n")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMTLKLDP1BIQuPb3-fnJrl5cpfhjHBhFF0Onswskul1eyu4fTPyEpOzUa13oWHQsl-83zPhaSVWBfIDj_RIeaQFrbr9VwCDLVXfUp-QDt5V6Dtd91VvXCO5O0Zm9hPTLOUhbXPQKb6tKdWecJ_ejME8fZX8rQRsRFkg67WdzlSv-g0mOuvhcsFKh9eeG-A/s1700-e365/n8n.jpg)

Cybersecurity researchers have disclosed details of two now-patched security flaws in the [n8n](https://thehackernews.com/2026/02/critical-n8n-flaw-cve-2026-25049.html) workflow automation platform, including two critical bugs that could result in arbitrary command execution.

The vulnerabilities are listed below -

* **[CVE-2026-27577](https://github.com/n8n-io/n8n/security/advisories/GHSA-vpcf-gvg4-6qwr)** (CVSS score: 9.4) - Expression sandbox escape leading to remote code execution (RCE)
* **[CVE-2026-27493](https://github.com/n8n-io/n8n/security/advisories/GHSA-75g8-rv7v-32f7)** (CVSS score: 9.5) - Unauthenticated expression evaluation via n8n's Form nodes

"CVE-2026-27577 is a sandbox escape in the expression compiler: a missing case in the AST rewriter lets process slip through untransformed, giving any authenticated expression full RCE," Pillar Security researcher Eilon Cohen, who discovered and reported the issues, [said](https://www.pillar.security/blog/zero-click-unauthenticated-rce-in-n8n-a-contact-form-that-executes-shell-commands) in a report shared with The Hacker News.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The cybersecurity company described CVE-2026-27493 as a "double-evaluation bug" in n8n's Form nodes that could be abused for expression injection by taking advantage of the fact that the form endpoints are public by design and require neither authentication nor an n8n account.

All it takes for successful exploitation is to leverage a public "Contact Us" form to execute arbitrary shell commands by simply providing a payload as input into the Name field.

In an advisory released late last month, n8n said CVE-2026-27577 could be weaponized by an authenticated user with permission to create or modify workflows to trigger unintended system command execution on the host running n8n via crafted expressions in workflow parameters.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikVLx0cfKQLD34PZ2yoj-CYprRJ_mQkkAB_D2Y5H8_Vw0NM24o_7OxpYSbyp12BzYTFulE5SozgsOwC7_u2Sc4FL9ZWw9slrNxc6Tcuhcf7SzvqOesGDb1_wQEyF8CebGB77mhZBYukY7sqBcSsRHH5wXidkEFDWJEPPrZuoYXBsyq5pH0DJ18166hoWb0/s1700-e365/para.png)

N8n also noted that CVE-2026-27493, when chained with an expression sandbox escape like CVE-2026-27577, could "escalate to remote code execution on the n8n host." Both vulnerabilities affect the self-hosted and cloud deployments of n8n -

* < 1.123.22, >= 2.0.0 < 2.9.3, and >= 2.10.0 < 2.10.1 - Fixed in versions 2.10.1, 2.9.3, and 1.123.22

If immediate patching of CVE-2026-27577 is not an option, users are advised to limit workflow creation and editing permissions to fully trusted users and deploy n8n in a hardened environment with restricted operating system privileges and network access.

As for CVE-2026-27493, n8n recommends the following mitigations -

* Review the usage of form nodes manually for the above-mentioned preconditions.
* Disable the Form node by adding n8n-nodes-base.form to the NODES\_EXCLUDE environment variable.
* Disable the Form Trigger node by adding n8n-nodes-base.formTrigger to the NODES\_EXCLUDE environment variable.

"These workarounds do not fully remediate the risk and should only be used as short-term mitigation measures," the maintainers cautioned.

Pillar Security said an attacker could exploit these flaws to read the N8N\_ENCRYPTION\_KEY environment variable and use it to decrypt every credential stored in n8n's database, including AWS keys, database passwords, OAuth tokens, and API keys.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

N8n versions 2.10.1, 2.9.3, and 1.123.22 also resolve two more critical vulnerabilities that could also be abused to achieve arbitrary code execution -

* **[CVE-2026-27495](https://github.com/n8n-io/n8n/security/advisories/GHSA-jjpj-p2wh-qf23)** (CVSS score: 9.4) - An authenticated user with permission to create or modify workflows could exploit a code injection vulnerability in the JavaScript Task Runner sandbox to execute arbitrary code outside the sandbox boundary.
* **[CVE-2026-27497](https://github.com/n8n-io/n8n/security/advisories/GHSA-wxx7-mcgf-j869)** (CVSS score: 9.4) - An authenticated user with permission to create or modify workflows could leverage the Merge node's SQL query mode to execute arbitrary code and write arbitrary files on the n8n server.

Besides limiting workflow creation and editing permissions to trusted users, n8n has outlined the workarounds below for each flaw -

* **CVE-2026-27495** - Use external runner mode (N8N\_RUNNERS\_MODE=external) to limit the blast radius.
* **CVE-2026-27497** - Disable the Merge node by adding n8n-nodes-base.merge to the NODES\_EXCLUDE environment variable.

While n8n makes no mention of any of these vulnerabilities being exploited in the wild, users are advised to keep their installations up-to-date for optimal protection.

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
[**...