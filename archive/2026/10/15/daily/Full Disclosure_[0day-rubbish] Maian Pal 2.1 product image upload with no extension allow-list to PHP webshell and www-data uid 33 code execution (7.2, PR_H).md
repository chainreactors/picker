---
title: [0day-rubbish] Maian Pal 2.1 product image upload with no extension allow-list to PHP webshell and www-data uid 33 code execution (7.2, PR:H)
url: https://seclists.org/fulldisclosure/2026/Oct/17
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:52.096602
---

# [0day-rubbish] Maian Pal 2.1 product image upload with no extension allow-list to PHP webshell and www-data uid 33 code execution (7.2, PR:H)

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

# [0day-rubbish] Maian Pal 2.1 product image upload with no extension allow-list to PHP webshell and www-data uid 33 code execution (7.2, PR:H)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:22:02 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Maian Pal
2.1, the self-hosted PHP shopping-cart script from Maian Media (United Kingdom),
oriented at PayPal checkout and distributed as a commercial closed-source archive,
verified end to end against a real installation of that version in three
independent reproductions.

Type: unrestricted upload of a file with a dangerous type (CWE-434 primary, with
CWE-94 and CWE-693 contributing - the stored object is subsequently interpreted as
code, and the served upload directory lacks the execution restriction that
equivalent directories in the same product carry), realised as OS command
execution (CWE-78 describes what the demonstration payload does once it runs and
is not scored separately). The product-image handling of the administration
product create and update operations, `ajax-ops=add` and `ajax-ops=add-edit`,
passes the multipart field fm[ifile][] to products::pictures() at
`class.products.php:333` through `class.products.php:410`. The stored name is
chosen from the client-supplied filename by a single ternary:

    // class.products.php:372  - no extension allow-list anywhere on this path
    $picPath = ($cfg['rename'] == 'yes'
                ? $cfg['imgprf'] . $ID . '-' . $nextPic . strrchr($name, '.')
                : $name);

    // class.products.php:~390  - written before any validation
    move_uploaded_file($temp, $picFldr . '/' . $picPath);

With $cfg supplied by thumbcfg() at `class.products.php:615`, whose shipped
default is 'rename' => 'no', that assignment reduces to $picPath = $name, so the
client controls the entire stored name including the extension and a .php file
lands on disk intact as content/products/<ID>/<name>.php. There is no extension
allow-list and no deny-list, no finfo or MIME verification, no re-encoding to
strip an embedded payload, no server-generated filename with a type-derived
extension, and no rollback of the write when later validation fails. strtolower()
appears only in the non-default rename='yes' branch and is cosmetic.

The root cause has two independently fixable halves, and this advisory keeps them
separate because fixing one without the other leaves the chain standing.

The first half is the handler: what may be written. The second is the directory:
whether what is written may execute. That second half lines up in this product
because the destination sits inside the document root and the front-controller
rewrite claims only paths that do not exist on disk - `RewriteCond !-f` guarding
`RewriteRule ^([^?]*) index.php?_msw_=$1 [L,QSA]` - so a file that exists is handed
straight to the PHP handler, and requesting it with a query string executes it.
Nothing in content/products/ disables that handler. Our review of the shipped tree
found an Apache deny file carrying `Deny from all` present in admin/import/, and
found content/products/ carrying no such file.

The contrast that makes this an omission rather than a design decision is inside
one product and one shipped version: two handlers accept files from a browser, and
one of them checks the extension and writes into a deny-protected directory while
the other does neither. We are precise about the evidentiary weight of each half
of that comparison, because it matters. That admin/import/ carries `Deny from all`
and that content/products/ carries nothing are both anchored artefacts of the
shipped tree. The statement that the product's attachment upload path applies an
extension allow-list into a deny-protected directory is a source-level reading of
the shipped PHP that we did not reduce to a line citation, and we label it as
such. It is offered here the same way we put it to the seller: as a contrast worth
confirming, since part of the argument that this is an omission rests on it.

The ordering inside the handler makes the failure path worse rather than safer,
and this is the detail most likely to be missed by a fix that only adds a check
downstream. move_uploaded_file() runs before any thumbnail inspection, and the
validation that does run is not fatal. getimagesize() inside thumbnail() runs
after the write and is used only to select a thumbnail strategy, never to accept
or reject the upload; for a PHP file it fails, the switch falls through to a
suppressed @copy(), and the original is never unlinked. So a non-image upload
leaves two objects in a served directory - the original plus a tmb_-prefixed
sibling - deletes neither, and still reports {"status":"ok"}. The failure path
yields two files rather than zero, silently. Any cleanup that removes only the
obviously named object leaves the second one behind.

Turning rename on would not fix this either, and it deserves emphasis because it
is the obvious operator-facing knob: in the rename='yes' branch the stem is
server-generated but the extension is still taken from the client filename via
strrchr(), so a .php upload produces a server-named file that is still
executable. We derived that from the assignment expression and did not run the
rename='yes' configuration, so it is an argument from code rather than a dynamic
result.

Commands execute as the web server service account, observed as
`uid=33(www-data) gid=33(www-data) groups=33(www-data)` in three independent
reproductions with distinct random filenames, plus a marker written to an absolute
path outside the document root and read back afterwards from the host. No
privilege escalation of any kind was attempted or observed: no kernel exploit, no
sudo right, no writable service unit, no container escape. Root was not reached
and is not claimed; the ceiling of this finding is code execution as the web
server user.

How confirmation works. The chain is two requests. One POST creates the object
and the create response itself embeds `?p=add&id=<ID>`, so the attacker learns
the numeric product directory without guessing and the filename is one they
chose - predictability of the final URL is total. One GET to
`/content/products/<ID>/<name>.php?cmd=<command>` executes it and returns the
output in the response body, prefixed by a marker that proves the body came from
PHP execution rather than from static file serving. Both operations report
{"status":"ok"}. What was deliberately not reproduced: no data theft, no database
modification, no persistence beyond the uploaded file, no lateral movement and no
exploitation of a live third-party system - all verification targeted our own
instance, and the payload's default command is a non-destructive identity query.

Scoring. One score is published: 7.2 High,
CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H, the CVSS 3.1 base arithmetic for
which is shown in full in the advisory and was re-checked against an independent
implementation of that formula. AV:N because the sink sits on the product's
ordinary HTTP(S) listener, with no separate management port, no RPC endpoint and
no background listener, and nothing in the chain depends on source ad...