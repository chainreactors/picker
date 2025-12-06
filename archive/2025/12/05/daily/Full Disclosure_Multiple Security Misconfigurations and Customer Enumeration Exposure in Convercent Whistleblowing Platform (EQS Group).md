---
title: Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)
url: https://seclists.org/fulldisclosure/2025/Dec/4
source: Full Disclosure
date: 2025-12-05
fetch_date: 2025-12-06T03:11:55.913693
---

# Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)

---

*From*: Yuffie Kisaragi via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 04 Dec 2025 16:27:53 +0000

---

```
Advisory ID: CONVERCENT-2025-001
Title: Multiple Security Misconfigurations and Customer Enumeration Exposure in
Convercent Whistleblowing Platform (EQS Group)
Date: 2025-12-04
Vendor: EQS Group
Product: Convercent Whistleblowing Platform (app.convercent.com)
Severity: Critical
CVSS v4.0 Base Score: 9.3
Vector: AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:L/SC:N/SI:N/SA:N

Summary

A series of security weaknesses were identified in the Convercent whistleblowing
platform operated by EQS Group. These issues include missing critical HTTP
security headers, insecure and duplicated session cookies, inconsistent SameSite
attributes, incomplete clickjacking protection, and an unauthenticated API
endpoint that leaks internal customer legal entities. The vulnerabilities were
observed on multiple customer instances (e.g., Milliman, Röchling Group,
BorgWarner) demonstrating that the weaknesses affect multiple Convercent tenants
and appear systemic.

Because Convercent processes sensitive whistleblower reports, internal
misconduct disclosures, and protected-identity information, these
vulnerabilities pose a severe risk to confidentiality, integrity, and
operational privacy.

Findings

1. Missing Critical Security Headers

The platform does not send several essential browser security headers,
including:

- Content-Security-Policy
- Referrer-Policy
- Permissions-Policy
- Cross-Origin-Embedder-Policy
- Cross-Origin-Opener-Policy
- Cross-Origin-Resource-Policy

The lack of these protections leaves Convercent pages vulnerable to cross-site
scripting, clickjacking, browser API misuse, cross-origin data leakage, and
weakened process isolation.

2. Weak HSTS Configuration and Formatting Issues

The platform currently sends the following Strict-Transport-Security header:

- Strict-Transport-Security: max-age=86400;includeSubDomains

This configuration uses an unusually small max-age value (24 hours), causing
browsers to quickly discard the HTTPS-only policy and leaving users vulnerable
to downgrade and SSL-stripping attacks. The missing space after the semicolon
(;includeSubDomains) is not an RFC violation but may affect parsing reliability
in certain intermediaries or older clients, reducing consistency and enforcement
of security expectations.

A more robust and industry-aligned configuration would be:
- Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

This longer duration, proper formatting, and optional preload directive provide
stronger, long-term HTTPS enforcement appropriate for a high-sensitivity
whistleblowing platform.

3. Duplicate Session Cookies
Multiple instances were found issuing two identical ASP.NET_SessionId cookies.

Duplicate session cookies may cause authentication instability, session override
conditions, and session fixation. This constitutes a protection mechanism
failure (CWE-693) and may indicate inconsistent load balancer or
application-layer handling.

4. Missing Secure Attribute on Affinity Cookie

One affinity cookie (ApplicationGatewayAffinity) lacked the Secure attribute,
exposing session metadata to potential interception on non-encrypted channels.
This is a serious misconfiguration for a system that handles sensitive
disclosures.

5. Inconsistent SameSite Attributes

Cookies within the platform defined mixed or absent SameSite values.

Such inconsistency may permit cross-site request leakage, session forwarding to
unintended origins, and unpredictable behavior in modern browsers. This
increases exposure to CSRF and related session compromise risks.

6. Incomplete Clickjacking Protection

The platform sets X-Frame-Options twice but does not define modern framing
restrictions using Content-Security-Policy’s frame-ancestors directive. As a
result, clickjacking protection is incomplete and can be bypassed.

7. Customer Enumeration via Unauthenticated API Endpoint

An unauthenticated API endpoint was found:

https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=

This endpoint returns internal customer legal entities based on the supplied
search fragment.

By querying the endpoint with common legal-suffix search terms such as “plc”,
“ag”, “sa”, “nv”, “ab”, “publ”, “oyj”, “asa”, it is possible to identify
publicly traded companies using Convercent. Since these suffixes correspond to
stock-quoted entities across various jurisdictions, attackers can derive a
meaningful portion of Convercent’s publicly listed customers.

E.g.:
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=plc
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=ag
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=sa
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=nv
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=ab
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=publ
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=oyj
-
https://app.convercent.com/en-US/Anonymous/IssueIntake/GetLegalEntity?searchText=asa

Critical Implications of Customer Enumeration

- Identification of organizations using the platform, even when such information
is not publicly disclosed;
- Construction of target lists for phishing, insider-trading intelligence,
extortion attempts, or regulatory exploitation;
- Exposure of sensitive business relationships and internal compliance
structures;
- Automated harvesting of thousands of customer entities through scriptable,
unauthenticated queries;
- Violation of expected confidentiality surrounding whistleblower
infrastructure, which is often deliberately undisclosed.

Impact

Confidentiality: High
Sensitive metadata, session information, and customer identity details can be
disclosed.

Integrity: High
Session fixation, cookie manipulation, and framing attacks could enable
unauthorized actions.

Availability: No
The vulnerabilities do not directly impair availability.

Scope: Changed
The absence of COOP/COEP and the presence of cross-origin weaknesses enable
privilege extension beyond the originating tenant.

Given the nature of data processed by whistleblowing systems, these weaknesses
represent a critical failure of security design and operational hardening.

Mitigation

The Convercent platform should implement the following:

Enforce modern security headers:

- Content-Security-Policy
- Referrer-Policy
- Permissions-Policy
- COEP, COOP, CORP

Revices HTSTS configuration.

Ensure only one session cookie is issued and add Secure and consistent SameSite
attributes to all cookies.

Implement proper clickjacking protection using CSP frame-ancestors.

Remove or restrict the GetLegalEntity API endpoint or require authentication to
prevent customer enumeration.

Conduct a platform-wide review of cookie handling, tenant configuration, and
load balancer behavior.

Affected Examples

Publicly reachable Conver...