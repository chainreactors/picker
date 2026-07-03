---
title: OpenBlow Multiple Deanonymization Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Jul/15
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:48:57.215585
---

# OpenBlow Multiple Deanonymization Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# OpenBlow Multiple Deanonymization Vulnerabilities

---

*From*: Red Nanaki via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 21 Jun 2026 10:16:53 +0000

---

```
OpenBlow Multiple Deanonymization Vulnerabilities

Summary

A production deployment was observed (HTTP archive of a full, real whistleblower
submission) to route its anonymous reporting flow through Google. The intake
CAPTCHA is Google reCAPTCHA, enforced as a mandatory, server-validated gate
on report submission, and the UI additionally pulls a web font from
fonts.gstatic.com. As a result, every prospective whistleblower's browser
makes direct connections to www.google.com and www.gstatic.com before a
report can be filed, disclosing the reporter's source IP, browser fingerprint,
and the precise identity of the whistleblowing site to a third party. The
absence
of a Content-Security-Policy and Referrer-Policy is what permits these
cross-origin loads.

The defects, in severity order:

1. (Critical) Google reCAPTCHA is a mandatory gate on the anonymous
submission flow - a whistleblower cannot submit without first being exposed to
Google.
2. (High) A web font is loaded from fonts.gstatic.com, a second independent
IP/fingerprint disclosure to Google.
3. (Medium) No Content-Security-Policy and no Referrer-Policy on
responses, which is what allows the third-party loads above.

Component

deployment / configuration

Classification

valid

Evidence: HAR capture of one end-to-end flow (load intake → upload attachments →
POST /api/v0/whistleblower/tip → retrieve). The submission could not complete
without a Google reCAPTCHA token, which is present in the submission body and is
produced only after live calls to Google.

Details

Hosts contacted during a single anonymous submission:
(first-party API + assets)
www.google.com (reCAPTCHA: api.js, api2/anchor, api2/reload [POST], …)
www.gstatic.com (reCAPTCHA static bundle)
fonts.gstatic.com (Roboto .woff2 web font)

Submission endpoint:
POST /api/v0/whistleblower/tip
request body field "captcha" carries a Google reCAPTCHA token:
"captcha":"0cAFcWeA4BGSN1zd5E_vRIN…"
-> the token is required and server-validated: submission is gated on Google.

Site identity leaked to Google (reCAPTCHA anchor "co" parameter, base64):
co -> decodes to https://:443

1. (Critical) Mandatory Google reCAPTCHA on the anonymous intake path

The submission request carries a Google reCAPTCHA token in the captcha field of
the POST /api/v0/whistleblower/tip body, and that token can only be obtained
after the browser performs the reCAPTCHA handshake with Google (api.js →
api2/anchor → api2/reload). The flow therefore cannot proceed without
contacting Google.

Google consequently receives, for every prospective reporter:

- the source IP address of the whistleblower's browser;
- a browser/device fingerprint (reCAPTCHA's purpose is behavioural/device
scoring);
- the exact whistleblowing site being used - the reCAPTCHA co parameter
base64-encodes the full origin (https://:443).

This contradicts the platform's anonymity guarantee, under which no third party
must be able to learn the identity of a source. It also degrades Tor usability:
reCAPTCHA routinely blocks or challenges Tor exit nodes, pushing at-risk users
off Tor toward non-anonymous access.

2. (High) Web font served from fonts.gstatic.com

Independently of reCAPTCHA, the UI fetches a Roboto .woff2 from
fonts.gstatic.com - a second, separate disclosure of the reporter's IP to
Google on the same pages.

3. (Medium) Missing Content-Security-Policy and Referrer-Policy

None of the captured first-party responses carry a Content-Security-Policy or a
Referrer-Policy. The absence of a restrictive CSP is what permits the
cross-origin Google/gstatic loads in findings 1–2; a correct CSP would have
blocked them.

Observed first-party response headers (representative):

strict-transport-security: max-age=31536000; includeSubDomains # present
x-frame-options: SAMEORIGIN # present
x-content-type-options: nosniff # present
access-control-allow-origin: https:// # scoped
(no content-security-policy) # MISSING
(no referrer-policy) # MISSING

PoC

Steps to reproduce

From a HAR capture (or live DevTools → Network) of the submission flow:

# Confirm the gate is mandatory and server-validated - the submission body
# contains a Google reCAPTCHA token:
python3 - <<'PY'
import json
har = json.load(open(".har"))
for e in har["log"]["entries"]:
if "/whistleblower/tip?" in e["request"]["url"]:
b = json.loads(e["request"]["postData"]["text"])
print("captcha token present:", bool(b.get("captcha")))
PY

# Confirm the site identity is leaked to Google (anchor "co" param):
python3 - <<'PY'
import base64, urllib.parse as u, json
har = json.load(open(".har"))
for e in har["log"]["entries"]:
q = u.parse_qs(u.urlparse(e["request"]["url"]).query)
if "co" in q:
print(base64.b64decode(q["co"][0] + "==").decode("utf-8", "replace"))
PY

Expected result

An anonymous reporting flow must complete without the reporter's browser
contacting any third party. The CAPTCHA must be an offline, first-party
challenge;
all fonts/assets must be first-party; a strict CSP must prevent any cross-origin
script/font load.

Actual result

The submission cannot complete without a Google reCAPTCHA token; obtaining it
requires live connections to www.google.com/www.gstatic.com, and a web font is
fetched from fonts.gstatic.com. Google receives the reporter's IP, a device
fingerprint, and the exact site origin (https://:443). No
CSP/Referrer-Policy is present to prevent this.

Impact

A whistleblowing platform's central promise is that a source cannot be
identified
by any third party. This deployment forces every prospective source to disclose
their IP address, a browser/device fingerprint, and the precise identity of the
channel they are using to Google - as a mandatory precondition of filing a
report. An adversary with visibility into, or legal reach over, that third party
can correlate "who contacted reCAPTCHA for this specific whistleblowing origin,
from which IP, at what time" with the subsequently received report. The
Tor-hostility of reCAPTCHA compounds this.

Potential impact:

- Confidentiality: High (source deanonymization via third-party IP/fingerprint +
site-identity disclosure on the anonymous intake path).
- Integrity: None.
- Availability: Low (reCAPTCHA/Tor friction can block legitimate anonymous
submissions).

Remediation

1. Disable Google reCAPTCHA; use an offline, first-party CAPTCHA. The intake
flow must never depend on a third party.
2. Self-host all fonts and assets; remove fonts.gstatic.com (and any other
third-party origin) from the served pages.
3. Deploy a strict Content-Security-Policy (default-src 'self', no
third-party script-src/font-src/connect-src) and a hardened
Referrer-Policy (e.g. no-referrer), so third-party loads are structurally
impossible.

Severity

Critical. The defects require no privileges and no user interaction beyond a
victim attempting to use the platform for its intended purpose, are exploitable
by
a network/third-party observer, and defeat the platform's primary security
property (source anonymity) on the anonymous intake path (Scope: Changed).

Vector string

CVSS:3.1/AV:N/...