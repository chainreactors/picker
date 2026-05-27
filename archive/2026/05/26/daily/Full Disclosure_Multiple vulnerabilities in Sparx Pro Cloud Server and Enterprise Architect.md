---
title: Multiple vulnerabilities in Sparx Pro Cloud Server and Enterprise Architect
url: https://seclists.org/fulldisclosure/2026/May/17
source: Full Disclosure
date: 2026-05-26
fetch_date: 2026-05-27T06:12:48.649707
---

# Multiple vulnerabilities in Sparx Pro Cloud Server and Enterprise Architect

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# Multiple vulnerabilities in Sparx Pro Cloud Server and Enterprise Architect

---

*From*: Adamczyk Blazej <blazej.adamczyk () gmail com>
*Date*: Fri, 22 May 2026 12:47:33 +0200

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Multiple vulnerabilities in Sparx Pro Cloud Server and Enterprise Architect
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

General information
═══════════════════

  Multiple vulnerabilities in Sparx Pro Cloud Server (PCS) versions <=
  6.1 and Sparx Enterprise Architect versions <=17.1 allow a remote
  unauthenticated attacker to execute arbitrary sql queries (both read
  and write) within any configured database. In case where PCS is
  installed with WebEA the vulnerabilities allow further for remote
  unauthenticated code execution (RCE) within the web server context.

  CVSSv4 chained score: *10.0 Critical*
  (AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H)

Fix
═══

  Currently vendor *did not resolve* any of the CVEs. The PCS
  authentication bypass and race condition seem to be easy to implement
  and I hope vendor will release patches soon.

  As a workaround it is best to isolate the PCS instances from internet
  and untrusted networks. Create frequent backups and review access logs
  if possible. You could also setup a proxy to limit the PCS
  authentication bypass (dropping requests with no or wrong model query
  parameter.

[Vulnerabilitiy #1] Sparx Pro Cloud Server SQL Command Execution
════════════════════════════════════════════════════════════════

CVE
───

  CVE-2026-42096 - Broken Access Control in Sparx Pro Cloud Server

Affected versions
─────────────────

  Sparx Pro Cloud Server versions <= 6.1 build 167

CVSSv4
──────

  9.4 Critical
  (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H)

Impact
──────

  PCS works as a remote model for a thick client, running on user's
  computers, called Enterprise Architect (EA). EA connects to PCS and
  works with the exposed database by directly running SQL queries.
  Besides user authentication (which is also vulnerable - see
  vulnerability #2 below) there is no additional access control. Any low
  privileged user can actually run any sql queries permitted by the
  configured external database user. Usually the user configured is at
  least having full access to the model database - thus any low
  privileged user can actually destroy the whole model, retrieve and
  change other user's password hashes and more.

  The problem seems to be with legacy thick client EA architecture which
  simply works on a database to manage all the model details.

Details
───────

  The client (EA) is connecting to the PCS HTTP server. The server might
  require authentication *if it is properly configured* - an admin can
  check "Enable Security" in EA but still not select "Require a secure
  and authenticated connection" in PCS configuration what results in *NO
  SERVER SIDE authentication at all*.

  Assuming the server side authentication is required the PCS verifies
  the authentication according to configuration - e.g. login/password,
  Active Directory or OpenID.

  Then the EA client sends request to perform SQL queries on the
  database in an ecrypted form but the whole encryption scheme is built
  into the client EA binary (actually downloadable from the vendor
  webside without any authentication - as trial version). The encryption
  is symmetric using a key contained within the binary itself thus
  simply this is not any security measure (security by obscurity).

  An attacker can obtain the key and then *create and send custom SQL
  queries to be performed by the database*.

PoC
───

  Exploit: https://github.com/br0xpl/sparx_hack/blob/main/eacrypt.py
  is a python script which exploits the SQL vulnerability by encrypting
  any SQL command and sending it to the server. For security,
  the real key is removed from the exploit code.

  This script receives all users and their hashes from PCS:
  ┌────
  │ python3 eacrypt.py http://${PCS_HOSTNAME} model "select * from t_secuser, t_xref where t_xref.Type='User Setting'
and t_xref.Name ='SHA-256' and t_xref.Client=t_secuser.UserID"
  └────

Solution
────────

  It will be hard to introduce proper authorization for all types of SQL
  queries - this would require to rewrite the logic to use some higher
  abstraction API which can be properly authorized.

  Until a proper authorized API will be provided a quick solution could
  be at least to verify the SQL queries executed and block the most
  dangerous like asking about other users' passwords and so on. Maybe a
  query whitelist with limiting the view of some critical assets like
  hashes.

  For sure it should be transparently stated in the PCS and EA
  documentation web page. Some integrators and admins are aware of this
  risk (there are some topics on the forum mentioning that the model
  security is not in fact security) but this *should be well described
  in both product documentations* as a limitation and risk which needs
  to be understood by clients and taken into consideration at an early
  stage while designing a production system. Otherwise it poses a high
  risk for any company using those products.

[Vulnerability #2] Sparx Pro Cloud Server Authentication Bypass
═══════════════════════════════════════════════════════════════

CVE
───

  CVE-2026-42097 - Authentication Bypass in Sparx Pro Cloud Server

Affected versions
─────────────────

  Sparx Pro Cloud Server versions <= 6.1 build 167

CVSSv4
──────

  9.2 Critical
  (CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)

Impact
──────

  An attacker can *omit PCS authentication* and e.g. combined with the
  previous vulnerability be able to remotely execute arbitrary SQL
  commands (read and write) *without authentication*.

Details
───────

  It seems that PCS requires authentication based on requested URL. EA
  clients sending the encrypted SQL query to PCS are using an url which
  looks as follows:

  ┌────
  │ https://${PCS_SERVER_HOSTNAME}/SparxCloudLink.sseap?model=${MODEL_NAME}
  └────

  PCS seems to look at the URL and decides how to authenticate the
  request. Unfortunately the SQL command query sends a POST request with
  a binary blob where the model name is defined one more time and this
  is the value that is further used by PCS to execute the query.

  Thus an attacker can simply omit the model query parameter and send
  the model name only in the binary blob in both TLS and non-TLS ports
  and the query will be executed even thought there was no
  authentication.

PoC
───

  To quickly verify compare the authenticated response for a request:
  ┌────
  │ curl 'https://${PCS_HOSTNAME}/SparxCloudLink.sseap?model=${MODEL_NAME}'; -X POST  -vvv --data 'whatever' -k
  └────

  which responds 401 Access Denied to response of a request without the
  query param:

  ┌────
  │ curl 'https://${PCS_HOSTNAME}/SparxCloudLink.sseap'; -X POST  -vvv --data 'whatever' -k
  └────

  which responds 500 Internal Server Error.

  To proof this properly use the python code which exploits the #1
  SQL vulnerability and uses the URL without model query parameter to
  omit the authentication.

Sol...