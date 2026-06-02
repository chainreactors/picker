---
title: bmcweb (OpenBMC web server): four vulnerabilities — two unfixed, GHSA without a CVE
url: https://seclists.org/fulldisclosure/2026/May/24
source: Full Disclosure
date: 2026-06-01
fetch_date: 2026-06-02T06:33:15.156862
---

# bmcweb (OpenBMC web server): four vulnerabilities — two unfixed, GHSA without a CVE

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# bmcweb (OpenBMC web server): four vulnerabilities — two unfixed, GHSA without a CVE

---

*From*: binreaper via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 27 May 2026 10:32:42 +0000

---

```
Hi all,

Posting a brief summary of a four-finding disclosure on bmcweb (the OpenBMC HTTP/Redfish web server), which ships in
BMC firmware on most modern enterprise servers — Intel, IBM, HPE, NVIDIA, and various ODMs.

Full timeline and analysis on the blog:

  https://binreaper.pages.dev/posts/2026-05-27-bmcweb-disclosure/

## Why bmcweb matters

A Baseboard Management Controller boots before the host CPU, has full control over the server (power, firmware,
console, in some configurations DMA), and is reachable from the management network. bmcweb is OpenBMC's HTTP front door
— Redfish API, web UI, KVM/console WebSocket. C++23 on Boost.Beast, single-threaded async, supports HTTP/1.1 and HTTP/2.

The single-threaded design means any blocking operation, large allocation, or event-loop stall takes the entire
management interface offline.

## The four findings

All reported 2026-02-23 to openbmc-security () lists ozlabs org.

| ID | Title | CVSS | Status |
|----|-------|------|--------|
| CONN-F2 | `Expect: 100-continue` bypasses body_limit (pre-auth OOM) | 7.5 | FIXED — commit `0b2049b0` (2026-04-21),
GHSA-p3gc-68x5-g9w3 |
| H2-F2 | HTTP/2 `Content-Length` trusted for `std::string::reserve()` (instant OOM) | 7.5 | FIXED — commit `62526bb0`
(2026-04-21), silent (no advisory) |
| H2-F1 | HTTP/2 no body_limit per stream (pre-auth OOM via streamed DATA frames) | 7.5 | UNFIXED — Gerrit 90580 today |
| AUTH-F6 | mTLS UPN suffix matching authenticates parent-domain / TLD-only certs | 6.8 | UNFIXED — Gerrit 90581 today |

## Three things worth flagging to this audience

1. **GHSA-p3gc-68x5-g9w3 has no CVE attached** (`cve_id: null`). It is not in NVD, OSV, the GitHub global Advisory
Database, or any distro security tracker that I checked. From a downstream-propagation perspective, the GHSA exists
only on the bmcweb security tab. The upstream maintainer's 2026-05-14 reply: "As far as I'm aware, there will be no CVE
assigned for this."

2. **One of two coordinated 2026-04-21 patches got an advisory; the other didn't.** CONN-F2 (the HTTP/1.1 bug) got
GHSA-p3gc. H2-F2 (the HTTP/2 sibling, same severity band, fix landed in the same minute) got no advisory at all. Anyone
applying bmcweb 3.0.0 because of the published advisory gets the H2-F2 fix as a side effect but doesn't know it.

3. **Intel firmware containing the unpatched binary is still on Intel's Download Center.** M50FCP BMC 2.94-0 (Download
Center ID 775817), dated January 2026, predates the upstream fix. I submitted CONN-F2 to Intel's bug bounty program
(Intigriti); triage accepted the scope, then closed out-of-scope under an "open-source projects we contribute to"
clause five hours later, despite the submission being explicitly about the vendor-distributed binary.

## H2-F1 (unfixed, posted today)

bmcweb's HTTP/1.1 path inherits its body limit from Boost.Beast's parser; the HTTP/2 path does not.
`HttpBody::reader::put()` in `http/http_body.hpp` appends incoming DATA-frame bytes to `value.str()` (a `std::string`)
with no size check. Authentication runs in `onRequestRecv()` on END_STREAM — i.e., after the full body has been
received and buffered. nghttp2 auto-replenishes flow-control windows by default; bmcweb does not set
`nghttp2_option_set_no_auto_window_update`.

Result: any client that can complete the TLS handshake (ALPN h2 is the default protocol path) can stream unlimited DATA
frames before authentication is ever attempted. The single-threaded event loop dies from OOM.

Suggested fix in Gerrit 90580 (https://gerrit.openbmc.org/c/openbmc/bmcweb/+/90580): per-stream byte counter on
`HttpBody::reader`, bound at the existing `BMCWEB_HTTP_BODY_LIMIT` (30 MiB by default).

## AUTH-F6 (unfixed, posted today)

`isUPNMatch()` in `http/mutual_tls.cpp` performs domain suffix matching when validating mTLS client certificates in
UserPrincipalName mode. The algorithm walks dot-separated labels right-to-left and returns true once the UPN domain
runs out of labels, regardless of how many hostname labels remain. The project's own existing unit test asserted the
consequence as expected behaviour:

  EXPECT_TRUE(isUPNMatch("user@com", "hostname.region.domain.com"));

A certificate with a UPN that is just a TLD authenticates any BMC in that TLD; a parent-domain certificate
authenticates any nested BMC. CVSS 6.8 because UPN mode is opt-in (default is CommonName) and requires a CA-signed
client cert with the broad UPN.

Suggested fix in Gerrit 90581 (https://gerrit.openbmc.org/c/openbmc/bmcweb/+/90581): replace the walk with exact-match
plus one-label-prefix tolerance (preserves `user () domain com` matching `bmc-01.domain.com`; rejects deeper nesting).

## Disclosure status

Maintainer-side track is closed per Ed Tanous's 2026-05-14 reply ("This bug is no longer embargoed, and the fix is on
master. There's no longer a reason to send direct messages to the security responders. If you believe further action is
needed, please use the normal project communication channels."). Earlier today the H2-F1 and AUTH-F6 disclosures went
to openbmc () lists ozlabs org with their respective Gerrit changes. This Full Disclosure post is the broader-audience
signal.

Reproducers exist for CONN-F2 and H2-F1 (Python; pocs/bmcweb/ in my files). I am not attaching them; happy to share
with downstream vendor PSIRTs or fork maintainers on request.

Best regards,
binreaper
bobdabot () proton me

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **bmcweb (OpenBMC web server): four vulnerabilities — two unfixed, GHSA without a CVE** *binreaper via Fulldisclosure (May 31)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](h...