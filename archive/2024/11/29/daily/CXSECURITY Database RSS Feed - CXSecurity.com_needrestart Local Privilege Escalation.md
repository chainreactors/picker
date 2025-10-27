---
title: needrestart Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2024110044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-29
fetch_date: 2025-10-06T19:14:26.139593
---

# needrestart Local Privilege Escalation

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **needrestart Local Privilege Escalation** **2024.11.28**  Credit:  **[Qualys Security Advisory](https://cxsecurity.com/author/Qualys%2BSecurity%2BAdvisory/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-48992](https://cxsecurity.com/cveshow/CVE-2024-48992/ "Click to see CVE-2024-48992")** | **[CVE-2024-11003](https://cxsecurity.com/cveshow/CVE-2024-11003/ "Click to see CVE-2024-11003")** | **[CVE-2024-48991](https://cxsecurity.com/cveshow/CVE-2024-48991/ "Click to see CVE-2024-48991")** | **[CVE-2024-48990](https://cxsecurity.com/cveshow/CVE-2024-48990/ "Click to see CVE-2024-48990")** | **[CVE-2024-10224](https://cxsecurity.com/cveshow/CVE-2024-10224/ "Click to see CVE-2024-10224")** | **[CVE-2022-30688](https://cxsecurity.com/cveshow/CVE-2022-30688/ "Click to see CVE-2022-30688")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

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
>From https://github.com/liske/needrestart#interpreters:
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
====================================...