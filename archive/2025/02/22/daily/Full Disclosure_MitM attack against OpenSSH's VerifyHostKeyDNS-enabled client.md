---
title: MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client
url: https://seclists.org/fulldisclosure/2025/Feb/17
source: Full Disclosure
date: 2025-02-22
fetch_date: 2025-10-06T20:47:17.602584
---

# MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client

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

# MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client

---

*From*: Qualys Security Advisory via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 18 Feb 2025 10:28:30 +0000

---

```
Qualys Security Advisory

CVE-2025-26465: MitM attack against OpenSSH's VerifyHostKeyDNS-enabled
client

CVE-2025-26466: DoS attack against OpenSSH's client and server

========================================================================
Contents
========================================================================

Summary
Background
Experiments
Results
MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client
DoS attack against OpenSSH's client and server (memory consumption)
DoS attack against OpenSSH's client and server (CPU consumption)
Proof of concept
Acknowledgments
Timeline

========================================================================
Summary
========================================================================

We discovered two vulnerabilities in OpenSSH:

- The OpenSSH client is vulnerable to an active machine-in-the-middle
  attack if the VerifyHostKeyDNS option is enabled (it is disabled by
  default): when a vulnerable client connects to a server, an active
  machine-in-the-middle can impersonate the server by completely
  bypassing the client's checks of the server's identity.

  This attack against the OpenSSH client succeeds whether
  VerifyHostKeyDNS is "yes" or "ask" (it is "no" by default), without
  user interaction, and whether the impersonated server actually has an
  SSHFP resource record or not (an SSH fingerprint stored in DNS). This
  vulnerability was introduced in December 2014 (shortly before OpenSSH
  6.8p1) by commit 5e39a49 ("Add RevokedHostKeys option for the client
  to allow text-file or KRL-based revocation of host keys"). For more
  information on VerifyHostKeyDNS:

  https://man.openbsd.org/ssh_config#VerifyHostKeyDNS
  https://man.openbsd.org/ssh#VERIFYING_HOST_KEYS

  Note: although VerifyHostKeyDNS is disabled by default, it was enabled
  by default on FreeBSD (for example) from September 2013 to March 2023;
  for more information:

  https://cgit.freebsd.org/src/commit/?id=83c6a52
  https://cgit.freebsd.org/src/commit/?id=41ff5ea

- The OpenSSH client and server are vulnerable to a pre-authentication
  denial-of-service attack: an asymmetric resource consumption of both
  memory and CPU. This vulnerability was introduced in August 2023
  (shortly before OpenSSH 9.5p1) by commit dce6d80 ("Introduce a
  transport-level ping facility").

  On the server side, this attack can be easily mitigated by mechanisms
  that are already built in OpenSSH: LoginGraceTime, MaxStartups, and
  more recently (OpenSSH 9.8p1 and newer) PerSourcePenalties; for more
  information:

  https://man.openbsd.org/sshd_config#LoginGraceTime
  https://man.openbsd.org/sshd_config#MaxStartups
  https://man.openbsd.org/sshd_config#PerSourcePenalties

========================================================================
Background
========================================================================

OpenSSH heavily uses the following idiom throughout its code base:

------------------------------------------------------------------------
1387 int
1388 sshkey_to_base64(const struct sshkey *key, char **b64p)
1389 {
1390         int r = SSH_ERR_INTERNAL_ERROR;
....
1398         if ((r = sshkey_putb(key, b)) != 0)
1399                 goto out;
1400         if ((uu = sshbuf_dtob64_string(b, 0)) == NULL) {
1401                 r = SSH_ERR_ALLOC_FAIL;
1402                 goto out;
1403         }
....
1409         r = 0;
1410  out:
....
1413         return r;
1414 }
------------------------------------------------------------------------

- at line 1390, the return value r is safely initialized to a non-zero
  error code (to prevent sshkey_to_base64() from mistakenly returning
  success, i.e. zero);

- at line 1398, if sshkey_putb() fails (if it returns a non-zero error
  code), then r is automatically set to this error code and immediately
  returned at line 1413;

- at line 1400, if sshbuf_dtob64_string() fails (if it returns NULL),
  then r is manually reset to a non-zero error code at line 1401 and
  immediately returned at line 1413;

- if no error occurs at all in sshkey_to_base64(), then at line 1409 r
  is set to zero (success) and eventually returned at line 1413.

This idiom left us pondering: what if the manual reset of the return
value r at line 1401 were missing? Then sshkey_to_base64() would
mistakenly return zero (success) if sshbuf_dtob64_string() fails at line
1400, because r was automatically set to zero at line 1398 (because, to
reach line 1400, sshkey_putb() necessarily succeeded, at line 1398).

The consequences of such a mistake (a function that returns success
although it clearly failed) would of course depend on the exact nature
of the affected function and its callers; but we began to suspect that,
in a large code base such as OpenSSH, some of the manual resets of the
return values r were inevitably missing, and some of these mistakes may
very well have security consequences.

Note: the same basic idea also underlies Kevin Backhouse's beautiful
CVE-2023-2283, an authentication bypass in libssh; for more information:

  https://securitylab.github.com/advisories/GHSL-2023-085_libssh/
  https://x.com/kevin_backhouse/status/1666459308941357056

========================================================================
Experiments
========================================================================

To confirm our suspicion, we adopted a dual strategy:

- we manually audited all of OpenSSH's functions that use "goto", for
  missing resets of their return value;

- we wrote a CodeQL query that automatically searches for functions that
  "goto out" without resetting their return value in the corresponding
  "if" code block.

Warning: our rudimentary CodeQL query (below) might hurt the eyes of
experienced CodeQL programmers; if you, dear reader, are able to write a
query that runs faster or produces less false positives, please post it
to the public oss-security mailing list!

------------------------------------------------------------------------
/**
 * @kind problem
 * @id cpp/test
 * @problem.severity error
 */

import cpp

Stmt getRecChild(Stmt s) {
  result = s or
  result = getRecChild(s.getChildStmt())
}

ControlFlowNode getRecPredecessor(ControlFlowNode n) {
  result = n or
  result = getRecPredecessor(n.getAPredecessor())
}

from Function f, ReturnStmt r, LocalVariable v, IfStmt i, Stmt b
where f.getBlock().getLastStmtIn() = r and
      exists(VariableAccess a | a.getTarget() = v and not a.isModified() and a.getEnclosingStmt() = getRecChild(r)) and
      v.getType() instanceof IntType and
      i.getEnclosingFunction() = f and
      i.getThen() = b and
      (b instanceof GotoStmt or b instanceof BlockStmt and ((BlockStmt)b).getLastStmtIn() instanceof GotoStmt) and
      not exists(Assignment a | a.getEnclosingFunction() = f and a.getLValue().toString() = v.getName() and
a.getEnclosingStmt() = getRecChild(i)) and
      not exists(Assignment a | a.getEnclosingFunction() = f and a.getLValue().toString() = v.getName() and
a.getEnclos...