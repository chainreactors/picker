---
title: [0day-rubbish] CloudPanel 2.5.4-3 site-settings rootDirectory nginx virtual-host injection to host root code execution (8.8)
url: https://seclists.org/fulldisclosure/2026/Oct/14
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:53.206610
---

# [0day-rubbish] CloudPanel 2.5.4-3 site-settings rootDirectory nginx virtual-host injection to host root code execution (8.8)

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

# [0day-rubbish] CloudPanel 2.5.4-3 site-settings rootDirectory nginx virtual-host injection to host root code execution (8.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:21:18 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in CloudPanel
Community Edition 2.5.4-3+clp-bookworm, the closed-source server-management panel
from cloudpanel.io (Germany) that provisions and supervises nginx, php-fpm,
MariaDB and hosted web sites from a Symfony application listening on port 8443.
The build under advisory is the vendor's own distribution package, 69,183,476
bytes, md5 24c36a4739ce065c5c188c89def06f29, on Debian bookworm x86_64. Only
this build was tested; no other version, edition or deployment target is
claimed, in either direction.

Type: injection of control characters into a configuration file that a second
parser then reads as syntax, CWE-93 primary, with CWE-20, CWE-74 and CWE-269 /
CWE-250 contributing. This is not command injection and we do not classify it as
CWE-78: the writer that puts the text on disk is
`echo %s | /usr/bin/sudo /usr/bin/tee %s` with both substitutions passed through
`escapeshellarg`, so the newlines travel inside a single-quoted shell argument as
data and no shell metacharacter reaches a command line. The sink is the virtual-host
renderer. `RootDirectory.php` owns the `{{root}}` placeholder and composes it at
label `b9892` as
`rtrim(sprintf("root /home/%s/htdocs/%s;", $siteUser, $rootDirectory), "/")`.
That `rtrim` is dead code, because the format string always ends with a semicolon
and so its result can never end with a slash. Between the value entering the
method and being composed into a directive there is no call of any kind - no
`basename`, no `realpath`, no `preg_match`, no allowlist, no blacklist, no length
check, no character check. The database value is the concatenated value. The
attacker therefore does not control the `root` directive's value but its tail,
which is sufficient: a leading semicolon terminates the already-started directive
cleanly and the injected blocks that follow land at server context ahead of the
template's own `location` blocks, where the `^~` prefix match outranks regex
locations. `{{root}}` appears twice in the hosting template, so the payload is
inserted twice, once per server block, which is consistent with the observed
file growth.

The double standard is the useful part for anyone auditing a similar form. The
same form family validates the domain name with a dedicated constraint whose
pattern excludes `/` and `\`; the command-line channel clamps the identical
root-directory value with `ltrim(rtrim($x,"/"),"/")`; and a neighbouring
free-text field on the same page has a four-step pre-submit normalization that
rewrites double quotes to single ones. The web-channel `rootDirectory` value
passes through none of these. Its only declared constraint is a not-null check,
and its entity setter performs no sanitization.

What turns a configuration write into host-root execution is vendor packaging,
not attacker choice. The vendor's own `nginx-common 1.30.4-1+clp-bookworm` ships
an `/etc/nginx/nginx.conf` whose line 1 is literally `user root;` and whose line
119 is `include /etc/nginx/sites-enabled/*.conf;` (md5
6727bffeb96cb3e03b85d00eac39c47c, 3,077 bytes, taken from the package payload
rather than transcribed from a note). The same package ships
`/home/clp/services/php-fpm/fpm/pool.d/file-manager.conf` declaring
`user = root` and `group = clp` on `/run/clp-fm-php-fpm.sock`, with no
`php_admin_value`, no `open_basedir`, no `disable_functions` and no
`security.limit_extensions` anywhere in its seventeen lines. So an injected
block carrying `dav_methods PUT; create_full_put_path on; alias /tmp/;` yields an
anonymous WebDAV write primitive, and a second injected block carrying
`root /tmp; include /etc/nginx/fastcgi_params; fastcgi_pass unix:/run/clp-fm-php-fpm.sock;`
hands anonymous PHP execution to a pool that runs as root.

The identity reached is host `uid=0(root) gid=1000(clp) groups=1000(clp),0(root)`,
corroborated in the same response body by `posix_getuid()` and `posix_geteuid()`
returning 0, by `whoami` returning `root`, by the uploaded file landing as
`-rw------- 1 root root`, and by a filesystem-type read showing the marker landed
on durable overlay storage rather than tmpfs. The exact shape of that identity
string matters and it is not decoration: `id` run from outside the container
prints `gid=0(root) groups=0(root)`, and a pool declaring only `user = root`
would print the same, so the `gid=1000(clp) groups=1000(clp),0(root)` that came
back over HTTP can only have been produced by the product's own execution path
through a pool declaring `user = root; group = clp;`. Labelled honestly, that is
a morphological inference from verbatim strings in two independent rounds plus a
packaged pool file whose bytes are on record; the reviewing pass did not itself
start a File Manager pool to observe the shape directly.

Confirmation and what was deliberately not reproduced. The save answers 302 with
no error text, and the product cannot report failure at all, because its reload
success check returns true unconditionally and the reload is backgrounded. So the
proof channel is the two anonymous requests plus the marker body, and four
requirements were defined in advance and checked in every round: a live `id`
containing `uid=0(root)` with no uid hardcoded in the uploaded script; device
self-attestation values in the body that are absent from our own payload and our
own script, with a positive control proving the search works and with two
witnesses downgraded honestly (the boot identifier is shared across containers on
one host kernel and the application secret is a factory constant, so the genuinely
device-unique witness is the container hostname, differing between the two sets
and independently embedded by `uname`); a fresh nonce per round appearing
simultaneously in the uploaded filename, in a comment line inside the written
virtual host and in the marker body, paired with the post-reload digest of that
specific file and a per-nonce `nginx -T` hit count that goes 0 to 1 for the
current round and back to 0 for the previous one; and evidence being response-body
content and size, never a status code, since 201 and 200 both occurred in failed
rounds too.

Deliberately not reproduced, and not claimed: cross-tenant impact, because no
second tenant was present; whether an illegal payload is rolled back under
vendor-native wiring, since both native sets used legal payloads and the
no-rollback behaviour was measured only under harness wiring; where injected text
lands in the PHP-site template, because that template is not in the package at all
and is imported at install time by a `git clone` of an external repository into a
database column; the second injection point of the same shape feeding the
`{{settings}}` placeholder, which static analysis says has the same exposure but
for which no dynamic round was run and no control was constructed; and whether a
local console invocation of the same sink, which the sudoers drop-in grants to any
local user, can inject this fie...