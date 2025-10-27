---
title: Local information disclosure in apport and systemd-coredump
url: https://seclists.org/fulldisclosure/2025/Jun/9
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:23.745839
---

# Local information disclosure in apport and systemd-coredump

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# Local information disclosure in apport and systemd-coredump

---

*From*: Qualys Security Advisory via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 29 May 2025 17:26:22 +0000

---

```
Qualys Security Advisory

Local information disclosure in apport and systemd-coredump
(CVE-2025-5054 and CVE-2025-4598)

========================================================================
Contents
========================================================================

Summary
Mitigation
Local information disclosure in apport (CVE-2025-5054)
- Background
- Analysis
- Proof of concept
Local information disclosure in systemd-coredump (CVE-2025-4598)
- Background
- Analysis
- Proof of concept
Acknowledgments
Timeline

========================================================================
Summary
========================================================================

We discovered a vulnerability in apport (Ubuntu's core-dump handler),
and a similar vulnerability in systemd-coredump (which is the default
core-dump handler on Red Hat Enterprise Linux 9 and Fedora for example):
a race condition that allows a local attacker to crash a SUID program
and gain read access to the resulting core dump (by quickly replacing
the crashed SUID process with another process, before its /proc/pid/
files are analyzed by the vulnerable core-dump handler).

We developed two proofs of concepts for these vulnerabilities (one for
Ubuntu 24.04, and one for Fedora 40 and 41, but other distributions are
probably also vulnerable and exploitable): they allow a local attacker
to obtain the contents of /etc/shadow (password hashes) from the core
dump of a crashed unix_chkpwd process (unix_chkpwd is a SUID or SGID
program that is installed by default on most Linux distributions).

Last-minute update: while working on these vulnerabilities, we
eventually realized that systemd-coredump does not specify %d (the
kernel's per-process "dumpable" flag) in /proc/sys/kernel/core_pattern;
consequently a local attacker can crash (with kill(SIGSEGV) for example)
root daemons that fork() and setuid() to the attacker's uid, gain read
access to the resulting core dumps, and therefore to the root daemons'
memory. For example, we wrote a trivial proof of concept that dumps the
memory of OpenSSH's sshd-session, systemd's sd-pam, and the cron daemon,
and obtained secret information such as half of sshd's private ed25519
host key, password hashes from /etc/shadow, other users' crontabs, ASLR
addresses, stack canaries. This second attack (against root daemons) is
powerful, different from the first attack (against SUID programs), and
can certainly be further improved; and other secrets can certainly be
obtained from other daemons, but this is left as an exercise for the
interested reader.

The fix for these vulnerabilities is twofold:

- always take account of the kernel's per-process "dumpable" flag (the
  %d specifier), in every code path, to decide whether a non-root user
  should be given read access to a core dump or not;

- use the new %F specifier in /proc/sys/kernel/core_pattern (a pidfd to
  the crashed process), which was implemented during this coordinated
  vulnerability disclosure, to detect whether the crashed process was
  replaced or not with another process, before its analysis; for more
  information:

  https://lore.kernel.org/all/20250414-work-coredump-v2-0-685bf231f828 () kernel org/

========================================================================
Mitigation
========================================================================

To mitigate these vulnerabilities, /proc/sys/fs/suid_dumpable can be set
to 0 (SUID_DUMP_DISABLE, "No setuid dumping"). This prevents all SUID
programs and root daemons that drop privileges from being analyzed in
case of a crash, but it can act as a temporary fix if the vulnerable
core-dump handler itself cannot be patched immediately.

========================================================================
Local information disclosure in apport (CVE-2025-5054)
========================================================================

------------------------------------------------------------------------
Background
------------------------------------------------------------------------

After our discovery of three bypasses in Ubuntu's unprivileged user
namespace restrictions, we decided to look for a real-world example of a
vulnerability that requires a user namespace with full capabilities. One
perfectly obvious example would be a kernel vulnerability that requires
CAP_SYS_ADMIN or CAP_NET_ADMIN, but finding and exploiting such a kernel
vulnerability would most likely take us months, so we decided to look
for a simple userland vulnerability instead.

One target that immediately came to mind is apport, Ubuntu's core-dump
handler, because it suffered from multiple vulnerabilities related to
namespaces (containers) in the past; for example, the following
excellent write-ups by Tavis Ormandy and Sander Bos:

- CVE-2015-1318: https://www.openwall.com/lists/oss-security/2015/04/14/4
- CVE-2017-14180: https://bugs.launchpad.net/ubuntu/+source/apport/+bug/1726372
- CVE-2019-11483: https://bugs.launchpad.net/apport/+bug/1839420

But as soon as we started to read apport's source code, we realized that
it has been considerably hardened over the years:

- The most common attack vector against apport, which consisted in
  tricking apport into dumping an attacker-controlled core file into a
  root-owned directory such as /etc/sudoers.d/ or /etc/logrotate.d/, has
  been completely eradicated: apport now dumps all core files into a
  hard-coded directory (/var/lib/apport/coredump/ by default).

- The race condition that allows a local attacker to replace a crashed
  process with another process, before its /proc/pid/ files are analyzed
  but after apport has started, has been largely mitigated in apport (by
  thorough security checks in its consistency_checks() function).

To further detail this last point: perhaps surprisingly, a local
attacker can send a SIGKILL signal to an already-crashed process, thus
allowing the attacker to recycle the crashed process's pid (by creating
many new processes until the crashed-and-killed process's pid is reused)
and tricking apport into analyzing the /proc/pid/ files of the wrong
process. This race condition has been exploited several times in the
past; for example, the following outstanding write-ups by Philip
Pettersson, Kevin Backhouse, Ryota Shiga, and Itai Greenhut:

- CVE-2015-1325: https://www.openwall.com/lists/oss-security/2015/05/21/10
- CVE-2019-15790:
https://github.blog/security/vulnerability-research/ubuntu-apport-pid-recycling-security-vulnerability-cve-2019-15790/
- CVE-2020-15702: https://flatt.tech/research/posts/race-condition-vulnerability-in-handling-of-pid-by-apport/
- CVE-2021-25684: https://alephsecurity.com/2021/02/16/apport-lpe/

But as mentioned earlier, this race condition has now been largely
mitigated in apport, by:

- immediately open()ing a file descriptor to the crashed process's
  /proc/pid/ directory and accessing all the files in this directory
  through this file descriptor and the *at() syscalls (openat() etc);

- checking tha...