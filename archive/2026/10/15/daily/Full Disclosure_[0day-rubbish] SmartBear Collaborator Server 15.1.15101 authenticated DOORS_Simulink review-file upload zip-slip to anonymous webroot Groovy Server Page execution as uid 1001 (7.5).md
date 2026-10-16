---
title: [0day-rubbish] SmartBear Collaborator Server 15.1.15101 authenticated DOORS/Simulink review-file upload zip-slip to anonymous webroot Groovy Server Page execution as uid 1001 (7.5)
url: https://seclists.org/fulldisclosure/2026/Oct/19
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:51.447492
---

# [0day-rubbish] SmartBear Collaborator Server 15.1.15101 authenticated DOORS/Simulink review-file upload zip-slip to anonymous webroot Groovy Server Page execution as uid 1001 (7.5)

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] SmartBear Collaborator Server 15.1.15101 authenticated DOORS/Simulink review-file upload zip-slip to anonymous webroot Groovy Server Page execution as uid 1001 (7.5)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:22:32 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in SmartBear
Collaborator Server 15.1.15101, the closed-source peer and technical code-review
platform from SmartBear that runs as a Java web application on Apache Tomcat. One
low-privilege authenticated account plants a Groovy Server Page in the Tomcat
webroot through an archive-extraction path traversal, and any anonymous client -
a crawler, a scanner, anyone - then executes it with an ordinary GET, yielding
operating-system command execution as uid=1001(collab) inside the product's own
JVM. Root was not reached, is not claimed, and no privilege escalation was
attempted.

Read the deployment-shape caveat first, because it decides whether this chain
works at all and it is the reason the published headline carries Attack
Complexity High. The only shipped artifact this research exercised was the
vendor's official container image, and in that image used exactly as shipped THE
CHAIN DOES NOT WORK. The image declares the webserver content directory as a
VOLUME and the installer never creates that path, so the container runtime
creates the mount point itself as drwxr-xr-x owned by root while the service runs
as uid 1001; the first filesystem call of the whole feature,
Files.createDirectories(destVersionDir.toPath()) at
HtmlBaseFilesUploadService.java:77, fails with EACCES before any archive entry is
read and no byte is ever written. That block cannot be worked around from inside
the product, because setWebserver has exactly one call site, at startup, from the
content-webserver context parameter declared at ROOT.xml:92 with
override="false". The shape in which the chain does succeed is the native,
non-container install, and that shape was never run on a real host: the claim
that a native install leaves that directory owned by the service account is a
labelled structural inference from the shipped archive, not a measurement. This
advisory therefore does not claim that every deployment of this product is
exploitable.

Type and root cause. CWE-22, path traversal through archive entry names, with
CWE-94 (code generation via the *.gsp template mapping), CWE-732, CWE-693,
CWE-668 and CWE-916 contributing. The JSON-API command
ReviewService.addDoorsFiles accepts a zip archive from any authenticated user
and dispatches through ReviewServiceImpl.addZipFiles:969-1001 to the first-party
extractor com.smartbear.ccollab.doors.DoorsFilesUploadService.upload. Across that
extraction loop the only validation of an entry is that the entry object is not
null (:73-75) and the only filter is the keyword list
IGNORE_FILES_KEYWORDS = {"__MACOSX"} declared at :63 and applied at :79. The
entry name is passed through a cosmetic square-bracket substitution at :77 -
Strings.replaceSquareBracketsToRound, which exists to satisfy the downstream
DOORS document parser and has nothing to do with paths - and is then concatenated
into a destination at :78 with

    File entryDestination = new File(uploadContext.getDestVersionDir(), fileName);

The two-argument File(File, String) constructor concatenates lexically: it does
not canonicalise, does not resolve against the base and does not reject
parent-directory segments. There is no normalize() call, no startsWith(destDir)
containment test, no canonical-path comparison, no rejection of an absolute name,
no rejection of a backslash-separated name, no extension allowlist or blocklist
on this route, no cap on entry count or cumulative uncompressed size, and no
per-object authorisation on the caller-supplied reviewId. Line :83 then creates
whatever parent directories the attacker's name implies and line :84 opens the
output stream, new FileOutputStream(entryDestination), which is the sink. An
entry named ../../../../../webapps/ROOT/<name>.gsp escapes the per-review version
directory and lands in the Tomcat webroot.

A sibling implementation shares the identical defect and the identical parent
class: com.smartbear.ccollab.matlab.SimulinkFilesUploadService.copyFilesFromZip
at :186-203 resolves destDir.resolve(zipEntry.getName()).toFile() at :188 with
no normalize(), no startsWith(destDir) and no .. rejection, and is reachable from
ReviewService.addSimulinkFiles. Its checkArchive at :157-161 constrains only the
first entry, which must be named exactly webview.html, and then ignores the rest
- a format assertion, not a containment control. One root cause with two code
instances is reported here as a single finding; the Simulink instance was never
exercised end to end and carries two further gates, so its practical
exploitability is strictly weaker and is claimed on source reading only. A
restricted-file-pattern check that genuinely exists lives only in the sibling
servlet VersionContentUploadServlet:90-93, on the JSON-API-free route, and it
validates the version's already-existing paths rather than names inside the
archive.

The destination geometry is what makes a relative traversal practical instead of
theoretical. The shared parent fixes the base: HtmlBaseFilesUploadService builds
webServerFolder as <mode>/<reviewId>/<zip name without extension> at :70-71,
joins it to SystemGlobals.getWebserver() at :74, and
SystemGlobals.java:130 declares that value as the relative string
"collaborator-webserver", so it resolves against the JVM working directory,
measured as /usr/local/ccollab_server/tomcat. The complete destination is
therefore

    /usr/local/ccollab_server/tomcat/collaborator-webserver/<mode>/<reviewId>/
        <zipbase>/ver<N>

Every segment is fixed by product logic or returned to the attacker, so the
required climb is a deterministic function the attacker can compute: depth = 4 +
n, where n is the number of path segments in the declared zip name after
stripping .zip, and the constant 4 counts ver<N>, the mode segment, the review
identifier and the webserver directory-name segment. Two independent
measurements agree with it at two different values of n - five segments for a
flat zip name, six for a zip name of the form <dir>/<name>.zip, both markers
executing anonymously. Depth must be exact in both directions, and overshooting
is not a safety margin: POSIX clamps ".." at the filesystem root, so too many
segments turn the target into the absolute path /webapps/ROOT/<name>.gsp and the
mandatory pre-write Files.createDirectories at :83 then fails with EACCES with
nothing written, while undershooting lands silently inside the content tree, is
served behind the authenticated /webserver/* prefix where an anonymous client
receives 401, and leaves an attacker file on disk.

The execution half is first-party configuration. The ROOT webapp's own
web.xml:271-278 maps *.gsp to the upstream groovy.servlet.TemplateServlet on the
anonymous surface, so a plain unauthenticated GET of the planted path compiles
the page in memory and evaluates it. That is what converts a
post-authentication arbitrary file write into code execution trig...