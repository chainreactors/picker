---
title: [0day-rubbish] Synametrics Syncrify 6.2 build 1178 authenticated PublicLink chunk-upload path traversal to /etc/cron.d and root command execution (7.5)
url: https://seclists.org/fulldisclosure/2026/Oct/21
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:50.729397
---

# [0day-rubbish] Synametrics Syncrify 6.2 build 1178 authenticated PublicLink chunk-upload path traversal to /etc/cron.d and root command execution (7.5)

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Synametrics Syncrify 6.2 build 1178 authenticated PublicLink chunk-upload path traversal to /etc/cron.d and root command execution (7.5)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:23:01 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Synametrics
Syncrify 6.2 build 1178, the closed-source incremental backup and
file-replication server from Synametrics Technologies, Inc. (United States). The
product is written in Java, distributed for Linux as a tarball archive, and
served by an embedded Tomcat 9.0.113 through the vendor's in-house sradef
framework, whose single front controller routes every request as
/app?operation=<op>&st=<step> to a handler registered in WorkerMappings.xml.

Type and root cause. Path traversal, CWE-22 primary, with CWE-269 improper
privilege management and CWE-78 OS command injection as contributing
classifications that describe the deployment shape converting a file write into
an execution rather than a defect inside the application. The PublicLink
handler, operation=pb, implements the server's PublicLink client protocol. Its
chunked-upload branch, selected by st=u, reads a length-prefixed binary frame
straight from request.getInputStream(), which means the server's parameter
parsing, form decoding and any framework-level parameter validation are all
bypassed by construction: the field that decides the write destination is not a
parameter. At PublicLink.java:70-110 the decompiled method reads four big-endian
int32 values and one length-prefixed UTF-8 string, then does this:

    int protocol    = readInt(in);     // 4-byte big-endian
    int chunkNumber = readInt(in);     // read, then not used to bound
                                       // or place the write
    int totalChunks = readInt(in);     // read, then not used either
    int size        = readInt(in);     // declared length of the body
    String filename = readString(in);  // [int32 len][UTF-8 bytes],
                                       // attacker-controlled

    File base   = E();                 // this user's PublicLinks folder
    File target = new File(base, filename);
    if (!target.getParentFile().exists()) {
        target.getParentFile().mkdirs();
    }
    BufferedOutputStream out = new BufferedOutputStream(
        new FileOutputStream(target, true));   // append mode
    byte[] buf = new byte[size];
    readFully(buf);
    out.write(buf);
    out.close();
    return 0;                          // 0 means success to the caller

new File(base, filename) is reached with no rejection of "..", no rejection of
path separators, no base-name extraction and no canonical containment check.
base is /opt/Syncrify/PublicLinks/<user>/<generated-folder>, five components
below the filesystem root, so a chunk name of ../../../../../etc/cron.d/<name>
leaves the per-user PublicLinks folder and lands a cron fragment, creating any
missing parent directory on the way because of the mkdirs() call. The branch
returns 0, f() at PublicLink.java:127 converts that into the client reply
code="1" with <payload>0</payload>, and the host cron daemon then reads the
fragment as a root-authored job definition and runs its command field through a
shell on the next minute boundary. The application itself never constructs,
quotes or invokes a command line, and every execution site in the product uses
an argument vector with no shell, so this could not have been fixed by argument
hygiene at the application layer; the execution happens one component later.

The identity reached was observed rather than inferred, and it is uid=0(root)
gid=0(root) groups=0(root). Two independent artifacts establish that the writer
process held uid 0: the fragment landed as -rw-r--r-- 1 root root at mode 0644,
and a file's owner after creation is the effective uid of the process that
created it; and the scheduled job's own output reported uid 0, the fragment
naming root in its user field, which a scheduler will not honour for a job file
it does not already trust.

What makes this an oversight rather than a design decision is the asymmetry
with the rest of the same tree. Three sibling families in the same product,
written against the same client protocol, check the same kind of field and
reject the same kind of content: the profile-upload, profile-fetch and
file-splitter handlers refuse names containing path separators by testing
character codes with indexOf(47) and indexOf(92); the multipart upload path
collapses the client-supplied name through getName() of a constructed File,
which discards every directory component; and the download path runs the name
through indexOf("..") and answers 404 on a match. The chunk-upload branch calls
none of them. When one member of a family omits the defense all of its siblings
implement, the economical explanation is that the check was not written rather
than that it lives somewhere else. There is also no decoding step between the
socket and the constructor on this branch, so no encoding trick is involved and
none is needed: what the client puts in the frame is what the path is built
from.

How confirmation works, and what was deliberately not reproduced. Confirmation
is by host-side artifacts, not by the HTTP reply, and that distinction matters.
The reply is a success oracle, so an attacker learns from the network alone that
a write was accepted and can iterate on naming from there, but a successful
reply is not proof of a successful destination: the code never inspects the
resolved path, so a wrong traversal depth still yields code="1" and simply
writes somewhere else with intermediate directories created as needed. The
read-back of the marker file is the only sufficient signal. Four controls were
exercised and the published tool automates one of them. A traversing name and a
non-traversing name were driven through identical authentication, identical
framing and the identical route in the same session; the benign write was
accepted and landed inside the user's own PublicLinks folder, and the assertion
that neither the cron fragment path nor the marker path existed is what isolates
the traversal as the cause of the outcome and of nothing else. A sibling-handler
control confirmed at the Java level that the multipart family's getName()
collapse, applied to a traversing name against the same PublicLinks base,
returns the bare final component and keeps the write inside the root. A dispatch
control built against st=f instead reached a different void E() overload at
PublicLink.java:951 that parses a request parameter named ed as a Long and
performed no write anywhere; that control is what fixed the sink to this branch
rather than to the handler in general, since an initial static reading had
attributed the upload to st=f and the request built on that reading produced no
file at all. Authentication controls established that the credential gate is
live. The published advisory reproduces the identity string and the frame field
lengths derived from the field values, but deliberately not the run's own byte
capture, which was not preserved; not the generated PublicLinks folder name,
which embeds the run's timestamp;...