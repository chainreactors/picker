---
title: Re: MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client
url: https://seclists.org/fulldisclosure/2025/Feb/18
source: Full Disclosure
date: 2025-02-28
fetch_date: 2025-10-06T20:47:41.048124
---

# Re: MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# Re: MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client

---

*From*: Jordy Zomer <jordy@pwning.systems>
*Date*: Fri, 21 Feb 2025 12:16:24 +0100 (CET)

---

```
Hey all,

First of all, cool findings! I've been working on the CodeQL query and have a revised version that I think improves
accuracy and might offer some performance gains (though I haven't done rigorous benchmarking). The key change is the
use of `StackVariableReachability` and making sure that there's a path wher e `var` is not reassigned before taking a
`goto _;`. Ran it on an older database, found some of the same bugs with no false-positives so far.

This is the revised query.
```
import cpp
import semmle.code.cpp.controlflow.StackVariableReachability

// A call that can return 0
class CallReturningOK extends FunctionCall {
    CallReturningOK() {
     exists(ReturnStmt ret | this.getTarget() = ret.getEnclosingFunction() and ret.getExpr().getValue().toInt() = 0)
    }

  }

class GotoWrongRetvalConfiguration extends StackVariableReachability {
    GotoWrongRetvalConfiguration() { this = "GotoWrongRetvalConfiguration" }

    // Source is an assigment of an "OK" return value to an access of v
    // To not get FP's we get a false successor
    override predicate isSource(ControlFlowNode node, StackVariable v) {
        exists(AssignExpr ae, IfStmt ifst | ae.getRValue() instanceof CallReturningOK
        and v.getAnAccess() = ae.getLValue() and  ifst.getCondition().getAChild() = ae  and
        ifst.getCondition().getAFalseSuccessor() = node)

    }

    // Our intermediate sink is a `goto _` statement, but it should have a successor that's a return of `v`
    override predicate isSink(ControlFlowNode node, StackVariable v) {
        exists(ReturnStmt ret | ret.getExpr() = v.getAnAccess() and
        node instanceof GotoStmt and node.getASuccessor+() = ret.getExpr())
    }

    // We don't want `v` to be reassigned
    override predicate  isBarrier(ControlFlowNode node, StackVariable v) {
        exists(AssignExpr ae | ae.getLValue() = node and v.getAnAccess() = node)
    }
}

from ControlFlowNode source, ControlFlowNode sink, GotoWrongRetvalConfiguration conf, Variable v, Expr retval
where
// We want a call that can `return 0` to reach a goto that has a ret of `v` sucessor
conf.reaches(source, v, sink)
and
// We don't want `v` to be reassigned after the goto
not conf.isBarrier(sink.getASuccessor+(), v)
// this goes from our intermediate sink to retval
and sink.getASuccessor+() = retval
// Just making sure that it's returning v
and exists(ReturnStmt ret | ret.getExpr() = retval and retval = v.getAnAccess())
select retval.getEnclosingFunction(), source, sink, retval
```

Hope that's helpful, please reach out if you have any questions :)

Cheers,

Jordy
```

> ```
> On 02/18/2025 11:28 AM CET Qualys Security Advisory via Fulldisclosure <fulldisclosure () seclists org> wrote:
>
>
> Qualys Security Advisory
>
> CVE-2025-26465: MitM attack against OpenSSH's VerifyHostKeyDNS-enabled
> client
>
> CVE-2025-26466: DoS attack against OpenSSH's client and server
>
>
> ========================================================================
> Contents
> ========================================================================
>
> Summary
> Background
> Experiments
> Results
> MitM attack against OpenSSH's VerifyHostKeyDNS-enabled client
> DoS attack against OpenSSH's client and server (memory consumption)
> DoS attack against OpenSSH's client and server (CPU consumption)
> Proof of concept
> Acknowledgments
> Timeline
>
>
> ========================================================================
> Summary
> ========================================================================
>
> We discovered two vulnerabilities in OpenSSH:
>
> - The OpenSSH client is vulnerable to an active machine-in-the-middle
>   attack if the VerifyHostKeyDNS option is enabled (it is disabled by
>   default): when a vulnerable client connects to a server, an active
>   machine-in-the-middle can impersonate the server by completely
>   bypassing the client's checks of the server's identity.
>
>   This attack against the OpenSSH client succeeds whether
>   VerifyHostKeyDNS is "yes" or "ask" (it is "no" by default), without
>   user interaction, and whether the impersonated server actually has an
>   SSHFP resource record or not (an SSH fingerprint stored in DNS). This
>   vulnerability was introduced in December 2014 (shortly before OpenSSH
>   6.8p1) by commit 5e39a49 ("Add RevokedHostKeys option for the client
>   to allow text-file or KRL-based revocation of host keys"). For more
>   information on VerifyHostKeyDNS:
>
>   https://man.openbsd.org/ssh_config#VerifyHostKeyDNS
>   https://man.openbsd.org/ssh#VERIFYING_HOST_KEYS
>
>   Note: although VerifyHostKeyDNS is disabled by default, it was enabled
>   by default on FreeBSD (for example) from September 2013 to March 2023;
>   for more information:
>
>   https://cgit.freebsd.org/src/commit/?id=83c6a52
>   https://cgit.freebsd.org/src/commit/?id=41ff5ea
>
> - The OpenSSH client and server are vulnerable to a pre-authentication
>   denial-of-service attack: an asymmetric resource consumption of both
>   memory and CPU. This vulnerability was introduced in August 2023
>   (shortly before OpenSSH 9.5p1) by commit dce6d80 ("Introduce a
>   transport-level ping facility").
>
>   On the server side, this attack can be easily mitigated by mechanisms
>   that are already built in OpenSSH: LoginGraceTime, MaxStartups, and
>   more recently (OpenSSH 9.8p1 and newer) PerSourcePenalties; for more
>   information:
>
>   https://man.openbsd.org/sshd_config#LoginGraceTime
>   https://man.openbsd.org/sshd_config#MaxStartups
>   https://man.openbsd.org/sshd_config#PerSourcePenalties
>
>
> ========================================================================
> Background
> ========================================================================
>
> OpenSSH heavily uses the following idiom throughout its code base:
>
> ------------------------------------------------------------------------
> 1387 int
> 1388 sshkey_to_base64(const struct sshkey *key, char **b64p)
> 1389 {
> 1390         int r = SSH_ERR_INTERNAL_ERROR;
> ....
> 1398         if ((r = sshkey_putb(key, b)) != 0)
> 1399                 goto out;
> 1400         if ((uu = sshbuf_dtob64_string(b, 0)) == NULL) {
> 1401                 r = SSH_ERR_ALLOC_FAIL;
> 1402                 goto out;
> 1403         }
> ....
> 1409         r = 0;
> 1410  out:
> ....
> 1413         return r;
> 1414 }
> ------------------------------------------------------------------------
>
> - at line 1390, the return value r is safely initialized to a non-zero
>   error code (to prevent sshkey_to_base64() from mistakenly returning
>   success, i.e. zero);
>
> - at line 1398, if sshkey_putb() fails (if it returns a non-zero error
>   code), then r is automatically set to this error code and immediately
>   returned at line 1413;
>
> - at line 1400, if sshbuf_dtob64_string() fails (if it returns NULL),
>   then r is manually reset to a non-zero error code at line 1401 and
>   immediately returned at line 1413;
>
> - if no error occurs at all in sshkey_to_base64(), then at line 1409 r
>   is se...