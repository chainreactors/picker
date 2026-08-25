---
title: Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account
url: https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html
source: The Hacker News
date: 2026-08-24
fetch_date: 2026-08-25T03:00:41.177413
---

# Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account

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

# [Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account](https://thehackernews.com/2026/08/critical-keycloak-password-reset-flaw.html)

**Swati Khandelwal**Aug 24, 2026Vulnerability / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhB3jURz2EzucPTALqHju1yDNnbHFvawrKxEfvNEprkdA3QIDyOjuUqvHOyTyiZuYJR-4KwewHnd8CdT37TDxBMBK3OLknOxym2a0klblR6rNUc2lqXHdAQUl1JO8uE7bGupO-WqsaEM0UDLUGyWICu5fkA6x4GwNUCo_w3quxp8joYWhNX8grP55eVg8/s1700-e365/keylock.jpg)

Red Hat and the Keycloak project have released patches to address a critical security flaw in the open-source identity and access management server that could allow an unauthenticated remote attacker to take over any user account by forcing a password reset.

The vulnerability, assigned the CVE identifier **CVE-2026-18963**, is rated 9.1 on the CVSS scoring system by Red Hat, which acts as the CVE Numbering Authority (CNA) for the flaw. It has been classified as a weak password recovery mechanism for a forgotten password (CWE-640).

Users of upstream Keycloak are advised to update to version 26.7.2, released August 19, 2026, while customers running Red Hat build of Keycloak (RHBK) should apply the updates shipped for 26.4.15 and 26.6.6.

There is no evidence that the flaw has been exploited, and no verified public exploit has been located as of August 24, 2026.

Red Hat said in [its CVE advisory](https://access.redhat.com/security/cve/CVE-2026-18963) that the root cause is "improper state validation within the reset-credentials authentication flow," the sequence Keycloak runs when a user requests password recovery. The company assessed the severity as Critical because an unauthenticated remote attacker can exploit the flaw without any user interaction.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The defect lies in how the flow's state is managed, according to [the Red Hat bug report](https://bugzilla.redhat.com/show_bug.cgi?id=2511595). An attacker sends a specially crafted request to the reset-credentials endpoint. The authentication session then transitions directly to the password update phase. The action token that Keycloak normally sends via email is never required.

Successful exploitation results in a complete account takeover of any user, "including administrative accounts," by resetting their password.

Escape researcher Enzo Mongin, writing about [a separate Keycloak access-control flaw](https://escape.tech/blog/escape-research-pii-disclosure-keycloak-cve-2026-17059/) he disclosed in July, said an attacker who crosses one of the server's boundaries does not stop at Keycloak, and that "they get into everything sitting behind it."

Red Hat issued four errata on August 18, 2026 ([RHSA-2026:56519](https://access.redhat.com/errata/RHSA-2026%3A56519), [RHSA-2026:56520](https://access.redhat.com/errata/RHSA-2026%3A56520), [RHSA-2026:56523](https://access.redhat.com/errata/RHSA-2026%3A56523) and [RHSA-2026:56524](https://access.redhat.com/errata/RHSA-2026%3A56524)), covering the standalone server packages and the container images for two RHBK streams. The [fixed versions](https://www.keycloak.org/security) are as follows -

* **Red Hat build of Keycloak 26.4** is unaffected from operator bundle 26.4.15-1, and from the rhbk/keycloak-rhel9 and rhbk/keycloak-rhel9-operator images 26.4-23
* **Red Hat build of Keycloak 26.6** is unaffected from operator bundle 26.6.6-1 and from the keycloak-rhel9 and operator containers 26.6-12
* **Upstream Keycloak** is fixed in 26.7.2

[The GitHub advisory](https://github.com/advisories/GHSA-4gv3-mc9p-5wqc) for the flaw lists both the affected and the patched versions as unknown, and the CVE record carries only Red Hat product references.

The initial CVE record listed Red Hat Single Sign-On 7 as unaffected and the Red Hat JBoss Enterprise Application Platform Expansion Pack as affected. A later revision narrowed the product list, and NVD's display truncates it, so the current status of both is not established.

For deployments that cannot be updated immediately, Red Hat has published a temporary mitigation -- turn off the "Forgot password" functionality across all realms. In the RHBK administration console, the setting sits under Realm settings, then Login, then Forgot password. Red Hat said the setting must be applied to every realm and that customers should upgrade to a fixed version as soon as possible.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

CVE-2026-18963 was one of eight CVE identifiers listed as fixed in [the Keycloak 26.7.2 release notes](https://www.keycloak.org/2026/08/keycloak-2672-released). The same release addressed CVE-2026-15571, a predictable account-linking hash that enables account takeover through a malicious OpenID Connect (OIDC) client.

Two weeks earlier, on August 5, 2026, Keycloak 26.7.1 shipped [fixes for twelve CVEs](https://github.com/keycloak/keycloak/releases), including a SAML identity-provider-initiated broker login that bypassed a link-only restriction and a default dynamic client registration policy that allowed role forgery via user property mappers.

Separately, Univention said in a post published August 20 that "Nubus is not affected by this issue" because the forgotten-password feature is not activated in its Keycloak deployments. Red Hat credited James Paremain with reporting the flaw.

No source addresses whether the fix fully resolves the flaw.

Whether every realm with the forgotten-password feature enabled is exploitable, or only certain reset-credentials flow configurations, is not stated by any of the published sources.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/...