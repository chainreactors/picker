---
title: [0day-rubbish] Abyss Web Server X1 2.16.22.0 first-run console credential takeover to configuration-write log-as-CGI command execution (7.5)
url: https://seclists.org/fulldisclosure/2026/Oct/12
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:53.924004
---

# [0day-rubbish] Abyss Web Server X1 2.16.22.0 first-run console credential takeover to configuration-write log-as-CGI command execution (7.5)

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Abyss Web Server X1 2.16.22.0 first-run console credential takeover to configuration-write log-as-CGI command execution (7.5)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:20:48 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability chain in
Abyss Web Server X1 2.16.22.0, the free edition of the closed-source Abyss
web server from Aprelium (Tunisia), a product family that has shipped for
more than twenty years. The release artefacts identify 2.16.22.0 as the
vendor's current official release. Between first start and the moment an
administrator sets a console password, any client admitted by the shipped
console access rule can register that administrator with no credential at
all, and three ordinary configuration forms afterwards convert the
configuration plane into an execution plane: the host access log becomes a
shell script inside CGI scope, and any anonymous request to the log path
executes it.

Type and root cause. CWE-306, missing authentication for a critical
function, is primary, and CWE-78, OS command injection, is co-equal rather
than subordinate. CWE-284, CWE-73, CWE-362, CWE-352, CWE-328 and CWE-250
contribute and are reported separately without raising any metric. The two
primary classifications are co-equal because removing either one alone
removes the chain while leaving every other weakness discussed here intact.
It is worth stating what this finding is not, because the technique is the
interesting part: there is no memory corruption, no deserialisation gadget
and no file-upload primitive anywhere in it. The write primitive is the
product's own supported configuration form, and the command enters the
written file through a quote-context escape in a request header field. A fix
that only adds authentication to the console leaves the log-as-interpreter
collision in place; a fix that only filters the header leaves the
unauthenticated credential creation in place. Neither half is sufficient on
its own.

The console authenticates with HTTP Basic on its default port 9999, binds
`bindip` `*` by default, and issues no session cookie anywhere - every
endpoint answers without `Set-Cookie`, including the endpoint that creates
the administrator. On first start the generated `abyss.conf` carries a
`<console>` node with no `<login>` and no `<password>` element, and the
startup terminal prints a message telling the operator to browse
`http://127.0.0.1:9999` to continue with the console access configuration.
While that state holds, `GET /console/` answers a distinctive `302` and the
bootstrap chain leads to `GET /console/credentials` answering `200` with a
creation form plus a `$$xxvxd` page token; a credential-free `POST` to that
endpoint installs the administrator. On an instance that has never been
configured the redirect first passes through `/console/language`; on an
instance whose language is already chosen it goes straight to
`/console/credentials`. Both shapes are unauthenticated throughout. After the
install the same endpoint answers `401` with
`WWW-Authenticate: Basic Realm="Abyss Web Server Console"`, so the
attacker's own POST is what closes the window.

The three forms that follow are a direct serialisation of the configuration
tree - each HTML control's `NAME` is the XML key path it writes - so what
they accept is exactly what the configuration can hold.

  - `POST /hosts/host@0/edit/scripting/paths/path@0/edit` takes
    `vpath=/` with `type=0` (CGI) and writes
    `<paths><path><vpath>/</vpath><type>0</type>...</path></paths>`. A
    `vpath` of `/` places the entire virtual path space of the host inside
    CGI scope, which includes files the server writes into the document root
    itself. There is no minimum-depth requirement and no warning about scope
    width.
  - `POST /hosts/host@0/edit/log` takes an arbitrary absolute filesystem
    path in its `file` control and a `format` of `.combined`, writing
    `<log><file>(absolute path inside the document root)</file><denied/>
    <format>.combined</format></log>`. No whitelist, no restriction to a log
    directory, no rejection of a destination inside the document root, and no
    canonicalisation. The control renders with a `Browse` selector that walks
    the target's directory tree from the filesystem root downwards, so the
    document root does not have to be guessed.
  - `POST /hosts/host@0/edit/scripting/interpreters/interpreter@0/edit`
    takes an arbitrary executable path with `interface=0`, `checkexists=yes`
    and `type=0`, and a second-step extensions sub-form then associates an
    arbitrary extension string. Submitting `/bin/sh` and `ext=log` writes
    `<interpreters><interpreter><file>/bin/sh</file>...<ext>log</ext>
    </interpreter></interpreters>`. `checkexists=yes` is satisfied because
    `/bin/sh` exists; nothing reasons about whether the extension names a
    content type rather than a destination type, whether the interpreter is a
    general-purpose shell, or whether the server itself writes files with
    that extension.

`POST /` carrying `/restart=Restart` - the product's own restart button, with
the main page showing "The configuration has changed. Press [Restart] to
apply the modifications." and host status `Running(Updated)` - applies all
three. The request-serving slave process bounces, and only the new
generation writes into the newly configured log destination. The access log
is now a shell script inside CGI scope. A request whose `User-Agent` is
`zz"; (command); #` appends a `.combined` line in which that value lands
inside the format's own double-quoted field, where the quote closes the
field, the semicolon separates a statement and the trailing comment swallows
the remainder. An anonymous `GET` on the log path then makes the product
start the CGI child `/bin/sh (log file)`, and the shell reads the whole file
line by line, executing the semicolon segment. Commands run as the identity
of the server process.

How confirmation works. The final trigger answers `500`, not `200`, and that
is the appearance of success rather than failure: `/bin/sh` writes no CGI
headers, so the product cannot construct a valid CGI response and answers
with its standard 348-byte error page while the CGI log records `Broken pipe`
for that invocation. Proof is server-side and three-channel rather than
client-observed. The product's own CGI error log names the child it spawned
directly, `CGI: [/bin/sh x.log ]  URI: /x.log`, interleaved with the shell's
own diagnostics `x.log: line N: 127.0.0.1: command not found` - those are the
log's ordinary leading fields being treated as command words, and they do not
stop execution of later lines, which is why a noisy log prefix is harmless.
The diagnostics incremented from two lines to four as the log grew between
fires, which is causality visible in the log: each fire re-reads the whole
file and re-executes every line. A marker file written by the injected
command contained `uid=uid=0(root) gid=0(root) groups=0(root)`, 43 bytes and
root-owned; the doubled prefix is the injected command's own literal, not a
product string, and the identity the server process ran under is
`uid=0(...