---
title: Local Privilege Escalations in needrestart
url: https://seclists.org/fulldisclosure/2024/Nov/15
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:22:24.813569
---

# Local Privilege Escalations in needrestart

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# Local Privilege Escalations in needrestart

---

*From*: Qualys Security Advisory via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 19 Nov 2024 16:28:37 +0000

---

```
Qualys Security Advisory

LPEs in needrestart (CVE-2024-48990, CVE-2024-48991, CVE-2024-48992,
CVE-2024-10224, and CVE-2024-11003)

========================================================================
Contents
========================================================================

Summary
Background
CVE-2024-48990 (and CVE-2024-48992)
CVE-2024-48991
CVE-2024-10224 (and CVE-2024-11003)
Mitigation
Acknowledgments
Timeline

    I got bugs
    I got bugs in my room
    Bugs in my bed
    Bugs in my ears
    Their eggs in my head
        -- Pearl Jam, "Bugs"

========================================================================
Summary
========================================================================

needrestart (from https://github.com/liske/needrestart) is a Perl tool
that is installed by default on Ubuntu Server since version 21.04. From
https://discourse.ubuntu.com/t/needrestart-changes-in-ubuntu-24-04-service-restarts:

------------------------------------------------------------------------
  What is needrestart, exactly?

  needrestart is a tool that probes your system to see if either the
  system itself or some of its services should be restarted. That last
  part is the one of interest in this document. Notably, a service is
  considered as needing to be restarted if one of its processes is using
  a shared library whose initial file isn't on the system anymore (for
  instance, if it has been overwritten by a new version as part of a
  package update).

  We ship this tool in our server images, and it is configured by
  default to run at the end of APT transactions, e.g. when doing apt
  install/upgrade/remove or during unattended-upgrades.
------------------------------------------------------------------------

We discovered three fundamental vulnerabilities in needrestart (three
LPEs, Local Privilege Escalations, from any unprivileged user to full
root), which are exploitable without user interaction on Ubuntu Server
(through unattended-upgrades):

- CVE-2024-48990: local attackers can execute arbitrary code as root by
  tricking needrestart into running the Python interpreter with an
  attacker-controlled PYTHONPATH environment variable.

  Last-minute update: an additional CVE, CVE-2024-48992, has been
  assigned to needrestart because local attackers can also execute
  arbitrary code as root by tricking needrestart into running the Ruby
  interpreter with an attacker-controlled RUBYLIB environment variable.

- CVE-2024-48991: local attackers can execute arbitrary code as root by
  winning a race condition and tricking needrestart into running their
  own, fake Python interpreter (instead of the system's real Python
  interpreter).

- CVE-2024-10224: local attackers can execute arbitrary shell commands
  as root by tricking needrestart into open()ing a filename of the form
  "commands|" (technically, this vulnerability is in Perl's ScanDeps
  module, but it is unclear whether this module was ever meant to
  operate on attacker-controlled files or not).

  Last-minute update: in the end, an additional CVE, CVE-2024-11003, has
  been assigned to needrestart for calling Perl's ScanDeps module with
  attacker-controlled files.

To the best of our knowledge, these vulnerabilities have existed since
the introduction of interpreter support in needrestart 0.8 (April 2014).
```

> ```
> From https://github.com/liske/needrestart#interpreters:
> ```

```
------------------------------------------------------------------------
  needrestart 0.8 brings an interpreter scanning feature. Interpreters
  not only map binary (shared) objects but also use plaintext source
  files. The interpreter detection tries to check for outdated source
  files since they may contain security issues, too. This is only a
  heuristic and might fail to detect all relevant source files. The
  following interpreter scanners are shipped:

  - NeedRestart::Interp::Java
  - NeedRestart::Interp::Perl
  - NeedRestart::Interp::Python
  - NeedRestart::Interp::Ruby
------------------------------------------------------------------------

We will not publish our exploits for now; however, please note that
these vulnerabilities are trivially exploitable, and other researchers
might publish working exploits shortly after this coordinated release.

========================================================================
Background
========================================================================

    And now the questions:
    Do I kill them?
    Become their friend?
    Do I eat them?
        -- Pearl Jam, "Bugs"

While idly watching an "apt-get upgrade" of one of our Ubuntu Servers,
we noticed a message that we had never noticed before: "Scanning
processes..."

We immediately wondered: What is printing this message? Is it scanning
userland processes? As root? Even processes that do not belong to root?

We quickly found out that this message is printed by needrestart, a tool
that scans the userland for processes that need to be restarted after a
package installation, upgrade, or removal. Naturally, needrestart scans
all userland processes as root, including unprivileged user processes;
i.e., possibly attacker-controlled processes.

========================================================================
CVE-2024-48990 (and CVE-2024-48992)
========================================================================

To determine whether a Python process (a process that is running the
Python interpreter) needs to be restarted, needrestart extracts the
PYTHONPATH environment variable from this process's /proc/pid/environ
(at line 193), sets this environment variable if it exists (at line
196), and executes Python ("$ptable->{exec}" at line 203) with a "-"
argument to read a short, hard-coded script from stdin (at line 204):

------------------------------------------------------------------------
135 sub files {
136     my $self = shift;
137     my $pid = shift;
138     my $cache = shift;
139     my $ptable = nr_ptable_pid($pid);
...
193     my %e = nr_parse_env($pid);
194     local %ENV;
195     if(exists($e{PYTHONPATH})) {
196         $ENV{PYTHONPATH} = $e{PYTHONPATH};
197     }
...
203     my ($pyread, $pywrite) = nr_fork_pipe2($self->{debug}, $ptable->{exec}, '-');
204     print $pywrite "import sys\nprint(sys.path)\n";
205     close($pywrite);
------------------------------------------------------------------------

Unfortunately, if a Python process belongs to a local attacker, then
needrestart executes Python (at line 203) with an attacker-controlled
PYTHONPATH environment variable, which allows the attacker to execute
arbitrary code as root (even though needrestart's hard-coded Python
script at line 204 is not attacker-controlled at all). This is
CVE-2024-48990.

For example, in our exploit we run a simple Python process (which
sleep()s forever) with a "PYTHONPATH=/home/jane" environment variable,
and plant a shared library "importlib/__init__.so" in our /home/jane.
As soon as needrestart executes Python with our PYTHONPATH en...