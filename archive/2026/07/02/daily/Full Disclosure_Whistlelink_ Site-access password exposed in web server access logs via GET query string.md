---
title: Whistlelink: Site-access password exposed in web server access logs via GET query string
url: https://seclists.org/fulldisclosure/2026/Jul/14
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:48:57.505249
---

# Whistlelink: Site-access password exposed in web server access logs via GET query string

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Whistlelink: Site-access password exposed in web server access logs via GET query string

---

*From*: Red Nanaki via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 21 Jun 2026 09:44:34 +0000

---

```
Whistlelink: Site-access password exposed in web server access logs via GET
query string

Severity: CRITICAL

SUMMARY

The Whistlelink reporting portal protects optionally-enabled, password-gated
whistleblowing sites with a site-access password. When a visitor unlocks such a
site, the client validates the password by issuing an HTTP GET request that
carries the password as a URL query-string parameter:

GET /sys/api/v1.0/wl/publish_site/check_password?password=

The value is only Base64-encoded (js-base64), which is a reversible transport
encoding, not encryption or hashing. Because the secret travels in the request
line / URI, it is written verbatim into the front-end web server's access log
(the deployment fronts the application with nginx, which logs the full request
URI by default) on every unlock attempt, and is similarly retained by any
reverse proxy, load balancer, WAF, CDN, observability / log-aggregation
pipeline, log backup, and the user's browser history.

Anyone able to read those logs can trivially Base64-decode the value and recover
the cleartext site-access password, defeating the access control for the entire
protected whistleblowing site. For a whistleblowing platform - where the
confidentiality of who may reach the reporting channel is a primary protection
goal - this is treated as CRITICAL.

CVSS

CVSS v3.1 Base: 7.7 (High)
CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N

CVSS v3.1 Environmental (whistleblowing asset, Confidentiality Requirement
High): 9.8 (Critical)
CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N/CR:H

CVSS v4.0: High
CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:N/VA:N/SC:L/SI:N/SA:N

The operative rating for this product class is the environmental score: the
protected asset is a whistleblowing channel whose access confidentiality is
paramount (potential whistleblower-safety consequences), justifying CR:H, which
raises the score to 9.8 / Critical and the CRITICAL tag.

Metric justification (v3.1 Base):

- Attack Vector: Network. Access logs are routinely centralized to
network-reachable systems (log/observability platforms, off-host backups,
object storage). If logs are only local files, AV:L applies and the Base
score drops to ~6.
- Attack Complexity: Low. The secret is present, in recoverable form, in every
check_password log line; decoding Base64 is trivial.
- Privileges Required: Low. Reading the logs requires some access to logging /
operations infrastructure - a materially lower and broader-trust bar than
knowing the site password itself. If logs are exposed to an unauthenticated
party (e.g. a misconfigured log bucket), PR:N applies and Base ~ 8.6.
- User Interaction: None. No victim interaction needed to read the stored value.
- Scope: Changed. The vulnerable component (the web application) writes the
secret into a separate security authority (the host / log subsystem), and the
impact lands on the protected site and its users.
- Confidentiality: High. Full disclosure of the site-access credential (and,
where reused, the underlying password), granting access to the protected
whistleblowing site.
- Integrity / Availability: None. The flaw discloses data; it does not directly
modify or deny service.

Score derivation (v3.1):

- ISCBase = 1 - (1 - 0.56) = 0.56
- Impact (Scope Changed) = 7.52 x (0.56 - 0.029) - 3.25 x (0.56 - 0.02)^15 ~
3.99
- Exploitability = 8.22 x 0.85 (AV) x 0.77 (AC) x 0.68 (PR, scope-changed) x
0.85 (UI) ~ 3.11
- Base = Roundup(min(1.08 x (3.99 + 3.11), 10)) = Roundup(7.67) = 7.7 (High)
- Environmental with CR:H: MISC = min(1 - (1 - 0.56 x 1.5), 0.915) = 0.84
-> Modified Impact ~ 5.93
-> Roundup(min(1.08 x (5.93 + 3.11), 10)) = 9.8 (Critical)

COMPONENT

backend (API endpoint design) / packaging (web server logging configuration)

FOUND BY

Passive HAR traffic audit + static analysis of the published client bundle.

AFFECTED ENDPOINT

GET /sys/api/v1.0/wl/publish_site/check_password?password=

Client request construction (published JS bundle, de-minified):

// password validation service
checkPassword: function (t) {
return C.a.get("".concat(T, "/check_password"), { params: { password: t } });
}

// caller - submit handler of the password gate
submit: function () {
// ...
cs.checkPassword(ds["a"].encode(this.password)).then(function (e) {
if (e.data.data) {
localStorage["authtoken"] = ds["a"].encode(this.password); // reversible Base64,
also reused as the Auth header
// route into the protected site
}
});
}

ds is js-base64 v3.7.8 (standard alphabet A-Za-z0-9+/=), so
ds.a.encode(password)
is plain, reversible Base64 - not a hash and not encryption.

DETAILS

Two distinct defects combine:

1. CWE-598 - Sensitive information transmitted in a GET request query string.
The site-access password is sent as the "password" query parameter rather than
in a request body. URLs / query strings are persisted far more widely than
request bodies: front-end web server access logs (nginx logs the full request
URI by default), reverse proxies, load balancers, WAFs, CDNs,
log-aggregation / observability pipelines, log backups, and the local browser
history. Even over TLS, the value is recorded in cleartext at these endpoints.

2. CWE-261 / CWE-312 - Weak (reversible) encoding of a credential.
The value is only Base64-encoded. Base64 provides no confidentiality; anyone
reading a log line recovers the cleartext password by decoding it. The same
reversible token is also placed in localStorage and replayed as the Auth header
on every request, broadening exposure.

The combined result (CWE-532 - Insertion of Sensitive Information into Log
File):
the cleartext site-access password is durably stored, in recoverable form, in
web
server access logs on every unlock attempt. The password is a single shared
secret
gating the whole protected site, so a single log read defeats the access control
for all visitors.

IMPACT

- Disclosure of the site-access credential to any party with read access to web
server / proxy / aggregated logs or their backups - a broader and lower-trust
population than those authorized to access the protected site (operations
staff, log-platform users, backup holders, third-party log processors, or an
attacker who obtains logs via a separate flaw).
- Complete bypass of the password gate for the protected whistleblowing site,
exposing the existence, configuration, and reporting channel that the password
was meant to keep confidential.
- Credential-reuse blast radius: if the configured site password is reused
elsewhere (common for shared, human-chosen site passwords), the impact extends
beyond the platform.
- Long-lived exposure: log retention and backups mean the secret remains
recoverable long after any password rotation, until all historical logs are
purged.

ATTACK SCENARIO

1. A whistleblowing site is configured with site-access password protection.
2. Visitors (and the operator during setup / testing) unlock the site; each
unlock emits GET .../check_password?password=, logged by nginx and
downstream systems.
3. A log-platform user, ba...