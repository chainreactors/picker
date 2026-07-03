---
title: Whistleblowersoftware.com: confidentiality and anonymity leakage to third parties
url: https://seclists.org/fulldisclosure/2026/Jul/16
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:48:56.894364
---

# Whistleblowersoftware.com: confidentiality and anonymity leakage to third parties

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Whistleblowersoftware.com: confidentiality and anonymity leakage to third parties

---

*From*: Red Nanaki via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 21 Jun 2026 11:07:14 +0000

---

```
Whistleblowersoftware.com: confidentiality and anonymity leakage to third
parties

## Summary

The anonymous reporting flow on `whistleblowersoftware.com` encrypts report
text end-to-end in the browser but does not extend the same guarantee to
attachments and exposes the reporter's network identity and timing to a US-based
third party. Together these weaken the confidentiality and anonymity
properties the platform is expected to provide.

## Components

- `api.whistleblowersoftware.com`: public reporting and mailbox endpoints
- `ws-api-production-occurrence-data.s3.eu-central-1.amazonaws.com`: attachment
storage
- Front-end SPA on `whistleblowersoftware.com`

## Findings

### 1. Attachments are processed in plaintext by third parties (High)

Report text (title, description, and message responses) is encrypted in the
browser before transmission using a hybrid scheme (RSA public key plus AES,
with a PBKDF2-derived passphrase key at 600,000 iterations). Attachments are
not handled the same way.

To strip file metadata, the client uploads the **original, unencrypted** file to
a third-party storage bucket (Amazon S3, `eu-central-1`), the file is processed
off the user's device, and the client then retrieves the cleaned file in
**cleartext** before encrypting and re-uploading it. The plaintext attachment is
therefore handled by parties other than the recipient organisation: the platform
operator, anyone with access to the storage bucket, and Amazon as the cloud
provider can read the full contents of every attachment, and a plaintext copy
persists in the temporary storage prefix until it is removed.

No evidence of a data protection agreement (DPA) between the operator and Amazon
was found, so there is no documented contractual basis constraining how the
cloud provider may process or retain the plaintext attachments it receives.

Endpoints involved:

```text
POST /api/companies/file-entries/signed-s3-url/public # request upload URL
POST / # upload original file
POST /api/companies/file-entries/remove-metadata/public # server strips metadata
GET /tmp/ # cleaned file, in cleartext
```

On a whistleblowing platform, attachments are frequently the most sensitive and
most deanonymizing part of a disclosure (documents, photos, embedded
EXIF/author/GPS metadata). Stripping that metadata off the user's device means
the very data a reporter needs hidden is exposed to third parties before it is
removed.

**Impact:** loss of confidentiality for all uploaded evidence; exposure of
deanonymizing file metadata to the operator and the third-party cloud provider;
residual plaintext copies in temporary storage; no documented data protection
agreement governing the cloud provider's handling of that plaintext.

**Recommendation:** perform metadata removal client-side, in the browser,
before encryption, so the server never receives plaintext. If server-side
processing cannot be avoided, stop presenting attachments as end-to-end
encrypted, guarantee immediate verifiable deletion of temporary plaintext
objects (lifecycle in minutes), and treat the metadata-stripping service as an
in-scope, trusted component that sees plaintext.

### 2. Third-party telemetry on the anonymous reporter flow (Medium)

The reporter pages load a third-party error/telemetry SDK that transmits
session data to an externally hosted, US-operated endpoint during the
submission flow. Each session sends the reporter's source IP address, user
agent, application release, and millisecond-precision session start/stop
timestamps with correlatable session identifiers.

No report content was transmitted in this channel, but it discloses the
reporter's network identity and submission timing to a party outside the
recipient organisation, raises cross-border personal-data-transfer concerns for
an EU-targeted service, and is a latent content-leak vector should error capture
or breadcrumbs ever be enabled with default settings.

**Recommendation:** remove third-party telemetry from the reporter flow, or
self-host it within first-party, EU-resident infrastructure; disable PII,
session tracking, and breadcrumb capture on these pages; review all
cross-origin connection targets permitted on the reporter flow against the
anonymity threat model.

## Positive observations

- Report text, message responses, and file names are encrypted client-side
(RSA + AES; PBKDF2 at 600,000 iterations with a per-report salt).
- Strong transport and browser hardening: HSTS with preload, a strict Content
Security Policy (`default-src 'none'` on the API, `frame-ancestors 'none'`,
`object-src 'none'`, mixed content blocked), `X-Frame-Options: DENY`,
`X-Content-Type-Options: nosniff`, a restrictive `Referrer-Policy` and
`Permissions-Policy`.
- CORS restricted to the exact application origin rather than a wildcard.
- Attachment storage uses short-lived temporary credentials, a private ACL, and
upload policies that pin bucket, key, content type, and a content-length
range, with short upload and download expiry windows.
- Rate limiting is applied to report submission.
- The reporting flow uses no cookies, authorization headers, or other
identifying request metadata.

## Severity ranking

1. Attachments processed in plaintext by third parties: High
2. Third-party telemetry on the anonymous reporter flow: Medium
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Whistleblowersoftware.com: confidentiality and anonymity leakage to third parties** *Red Nanaki via Fulldisclosure (Jul 02)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools...