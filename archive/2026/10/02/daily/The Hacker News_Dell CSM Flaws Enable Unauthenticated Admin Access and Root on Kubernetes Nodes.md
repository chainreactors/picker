---
title: Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes
url: https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html
source: The Hacker News
date: 2026-10-02
fetch_date: 2026-10-03T07:13:21.472699
---

# Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes

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

# [Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes](https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html)

**Ravie Lakshmanan**Oct 02, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiypcfC3W6keUc31zSJympZfpI6eLwDhyphenhyphen4uy_0M3VFljfoSn2pjzBmS3yyAZTzILPxi_sXeOx2jyeu6mdSPKqjiFv7LAMd2mn6Q8GvIRq6yVXUoQm5MiXeEs96i9IT-ZCP2W7hAzR08B9JOuOJv8NNI7o7DfCSa7cplzrsT_x_0R0dPVSQxKmdLP8NvAsnp/s1700-nu-rw-lo-l85-e365/dell.jpg)

Dell has [released](https://www.dell.com/support/kbdoc/en-us/000515771/dsa-2026-448-security-update-for-dell-container-storage-modules-multiple-vulnerabilities) security updates to address multiple critical security flaws in Dell Container Storage Modules (CSM) that could be exploited by bad actors to take over susceptible systems.

The vulnerabilities are listed below -

* **CVE-2026-63688** (CVSS score: 10.0) - A missing authentication for critical function vulnerability in the csm-authorization-storage gRPC server that an unauthenticated remote attacker could exploit to obtain unauthorized access to storage backend administrator credentials for all registered storage arrays.
* **CVE-2026-63692** (CVSS score: 10.0) - A missing authentication for critical function vulnerability in the authorization proxy and tenant service that an unauthenticated network attacker could exploit to bypass authentication controls and gain administrative-level privileges.
* **CVE-2026-67269** (CVSS score: 9.9) - An improper privilege management vulnerability in the ContainerStorageModule Custom Resource reconciler that a low-privilege remote attacker could exploit to escalate privileges and gain root-level access on cluster nodes.
* **CVE-2026-54472** (CVSS score: 9.8) - A use of hard-coded credentials vulnerability in the CSM Authorization module that a remote unauthenticated attacker could exploit to forge cryptographically valid administrative tokens and gain unauthorized administrative access to the CSM Authorization proxy.
* **CVE-2026-61421** (CVSS score: 9.8) - A use of hard-coded cryptographic key vulnerability in the JWT authentication component of karavi-authorization that a remote unauthenticated attacker with knowledge of this publicly available signing secret could exploit to forge authentication tokens and gain administrative privileges.
* **CVE-2026-67273** (CVSS score: 9.6) - An improper neutralization of special elements used in a template engine vulnerability that a low-privilege attacker with remote access could exploit to escalate privileges, access sensitive information, and carry out unauthorized RBAC tampering.

"This vulnerability is considered critical as it enables a complete bypass of the csm-authorization security model, allowing an attacker to gain full administrative control over the storage infrastructure spanning all five supported Dell storage product families," Dell said about CVE-2026-63688.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

As for CVE-2026-63692, Dell noted that successful exploitation could enable an unauthenticated attacker to gain complete administrative control over the authorization service, and allow them to access or manipulate storage resources across all tenants.

The PC maker also noted that an attacker can exploit CVE-2026-67269 to compromise all nodes in a Kubernetes cluster through a single custom resource submission. CVE-2026-54472, on the other hand, can be weaponized to sidestep authentication controls for the CSM Authorization proxy and enable unauthorized management of storage access policies across all connected tenants. Dell is recommending that customers apply the updates and rotate any JWT signing secrets.

"Successful exploitation grants the attacker cluster-wide read access to Kubernetes Secrets and the ability to create cluster-scoped RBAC resources, effectively bypassing the intended Kubernetes access controls," Dell said in its advisory for CVE-2026-67273.

The flaws, which affect all versions of CSM prior to 1.17.0, have been addressed in 1.18.0. There are no workarounds or mitigations other than updating to the latest version. With vulnerabilities in Dell products ([CVE-2021-21551](https://thehackernews.com/2022/10/hackers-exploiting-dell-driver.html) and [CVE-2026-22769](https://thehackernews.com/2026/02/dell-recoverpoint-for-vms-zero-day-cve.html)) having come under active exploitation in recent years, it's essential to apply the necessary fixes for optimal protection.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Container Security](https://thehackernews.com/search/label/Container%20Security), [Dell](https://thehackernews.com/search/label/Dell), [Kubernetes](https://thehackernews.com/search/label/Kubernetes), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https://thehacker...