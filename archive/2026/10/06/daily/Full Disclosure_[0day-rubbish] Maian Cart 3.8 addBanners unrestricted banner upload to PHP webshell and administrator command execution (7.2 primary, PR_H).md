---
title: [0day-rubbish] Maian Cart 3.8 addBanners unrestricted banner upload to PHP webshell and administrator command execution (7.2 primary, PR:H)
url: https://seclists.org/fulldisclosure/2026/Oct/6
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:41.544541
---

# [0day-rubbish] Maian Cart 3.8 addBanners unrestricted banner upload to PHP webshell and administrator command execution (7.2 primary, PR:H)

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Maian Cart 3.8 addBanners unrestricted banner upload to PHP webshell and administrator command execution (7.2 primary, PR:H)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Oct 2026 17:53:29 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Maian
Cart 3.8, the self-hosted PHP shopping-cart system from Maian Media (Maian
Script World), verified end to end against a real installation of that
version.

Type: unrestricted upload of a file with a dangerous type (CWE-434), realized
as OS command execution (CWE-78) through an attacker-supplied PHP webshell,
with CWE-269 bearing on the execution privilege context. The Store Banners
page of the administration backend (route /admin/index.php?p=settings&s=9)
dispatches multipart uploads to addBanners() in
admin/control/classes/class.system.php:376-413, which reads the raw client
filename at line 386, derives the stored extension from it at line 392 with
strrchr on the lower-cased name, composes the stored name at line 393 as the
banner prefix plus a counter from the banners table plus that extension, and
writes the file with move_uploaded_file at line 401, a second call site being
recorded at line 410. There is no extension allow-list, no MIME or finfo
validation and no getimagesize() content check anywhere on the path;
mc_safeImport at line 377 is an SQL-escaping pass over $_POST and never
touches $_FILES, and is_uploaded_file only confirms the file arrived over
HTTP. With the shipped defaults RENAME_BANNERS=1 and BANNER_PREFIX='img_',
an upload named shell.php is stored as img_1.php: the rename regenerates the
base name and preserves the attacker's extension. The destination,
content/_theme_default/images/banners/, is inside the document root and
carries no deny rule, in explicit contrast to admin/import/.htaccess,
admin/attachments/.htaccess and content/_theme_default/cache/.htaccess, all
of which ship Deny from all, so a plain GET for the stored img_<id>.php is
handed to the PHP interpreter and a one-line shell_exec webshell yields
command execution in the web server process context. move_uploaded_file runs
before the INSERT INTO banners statement, so the shell survives even a failing
INSERT. The product's own image allow-list ($imgAllow at class.products.php:9,
applied at :1213 and :1907 in addAdditionalProductPictures) is the one-line
control this handler omits.

Scoring. Four readings are published with their vectors, labelled, rather than
one number:
- PRIMARY, and the only classification this advisory claims: 7.2 High,
  CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H. The sink sits behind the
  webmaster gate at admin/control/system-load.php:79
  (mc_isWebmasterLoggedIn, whose underlying test at functions.php:324-336
  requires a fully populated webmaster session array).
- CONDITIONAL, 9.8 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H,
  for a deployment that retains an unchanged, known or guessable
  administrator credential. This reading is this advisory's own construction,
  not a figure produced by the research record, which scores the finding only
  under the 7.2 vector and records that the unauthenticated objective was not
  reached. It describes deployment state rather than product state: the
  product ships no fixed factory credential, the install wizard writes the
  operator-chosen USERNAME and PASSWORD into access.php, and no installation
  whose credentials were guessable was verified. Its sole basis is the
  companion observation that the installer-provisioned credential is never
  forced to rotate (a CWE-798-class note about persistent provisioned
  credentials without a rotation gate). It does not change the primary
  classification.
- CONSIDERED AND NOT ADOPTED: 8.8 High,
  CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H, which differs from the
  primary vector only in Privileges Required and was not adopted because no
  role below webmaster reaches the settings module in the recorded gate
  model; and 9.1 High,
  CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H, which would require Scope
  Changed and does not fit, the vulnerable component and the impacted
  component being the same security authority.

Authentication: administrator session. The login handler
(admin/control/modules/system/portal.php:26-47) requires process=1, a cs_rf
CSRF token matching the hidden field served on the login page, a user value
equal to the USERNAME constant in access.php and a password verified through
mc_PassHash; the trigger is isset($_POST['process_banners']) at
settings.php:84-87. The unauthenticated objective was pursued and exhaustively
ruled out: ajax.php exposes no file-write or command primitive an
unauthenticated caller can steer; forging the persistent administrator cookie
is infeasible because mc_encrypt(SECRET_KEY . DB_NAME) requires the
per-installation database name, which is not remotely discoverable; the only
gadget found was PHPMailer's __destruct, not exploitable into a dangerous sink
in this codebase, so no object-population chain exists; the login path is not
injectable; and every move_uploaded_file call site identified sits under the
gated /admin/ backend. No unauthenticated route to the sink is claimed.

Impact: arbitrary OS command execution as the web server process, uid=0(root)
in the laboratory capture because the test web tier ran as root, typically
www-data or apache in production. Full read and write access to store source
code, application configuration including the database credentials the
application itself reads, uploaded order attachments and the surrounding file
system; database access with the application's own privileges, meaning the
store's orders, customer records and settings; persistence, since the stored
img_<id>.php outlives the administrator session and nothing in the product
scans for or removes it; and a pivot into whatever segments the store host can
reach. For an insider or credential-holder the upload is audit-invisible: it
appears in the interface as an ordinary banner addition.

Verification boundary, stated plainly. Verified end to end against a real Maian
Cart 3.8 installation: the product's own install wizard run to completion on a
Linux laboratory host, creating 62 database tables and populating the settings
rows, with MySQL 8.0.46 on a dedicated laboratory schema and account, and the
web tier being the PHP built-in server bound to loopback for laboratory
safety. That process ran as root for the session in question, which is why
uid=0(root) was observed and why the stored 39-byte shell, exactly the length
of the one-line payload, was owned by root. Three independent runs reached
command execution, the third being a from-scratch re-analysis pass by an
independent reviewer who rebuilt the audit and shipped a second, distinctly
named shell through the same handler, stored as img_3.php. An adversarial
refutation review searched for a global upload sanitizer, a deny rule for the
banners directory, FilesMatch restrictions on .php, getimagesize usage on this
path, web-server configuration hardening and install-time hardening, found
none, and left the finding standing. No vendor-hosted or third-party
installation ...