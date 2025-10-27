---
title: Leeloo Multipath Authorization Bypass / Symlink Attack
url: https://cxsecurity.com/issue/WLB-2022110004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-03
fetch_date: 2025-10-03T21:36:16.938277
---

# Leeloo Multipath Authorization Bypass / Symlink Attack

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
|  |  | |  | | --- | | **Leeloo Multipath Authorization Bypass / Symlink Attack** **2022.11.02**  Credit:  **[Qualys Security Advisory](https://cxsecurity.com/author/Qualys%2BSecurity%2BAdvisory/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-41973](https://cxsecurity.com/cveshow/CVE-2022-41973/ "Click to see CVE-2022-41973")** | **[CVE-2022-41974](https://cxsecurity.com/cveshow/CVE-2022-41974/ "Click to see CVE-2022-41974")**  CWE: **[CWE-59](https://cxsecurity.com/cwe/CWE-59 "Click to see CWE-59")** | |

Qualys Security Advisory
Leeloo Multipath: Authorization bypass and symlink attack in multipathd
(CVE-2022-41974 and CVE-2022-41973)
========================================================================
Contents
========================================================================
Summary
CVE-2022-41974: Authorization bypass
CVE-2022-41973: Symlink attack
Acknowledgments
Timeline
========================================================================
Summary
========================================================================
We discovered two local vulnerabilities (an authorization bypass and a
symlink attack) in multipathd, a daemon that is running as root in the
default installation of (for example) Ubuntu Server:
https://ubuntu.com/server/docs/device-mapper-multipathing-introduction
https://github.com/opensvc/multipath-tools
We combined these two vulnerabilities with a third vulnerability, in
another package that is also installed by default on Ubuntu Server, and
obtained full root privileges on Ubuntu Server 22.04; other releases are
probably also exploitable. We will publish this third vulnerability, and
the complete details of this local privilege escalation, in an upcoming
advisory.
The authorization bypass (CVE-2022-41974) was introduced in February
2017 (version 0.7.0) by commit 9acda0c ("Perform socket client uid check
on IPC commands"), but earlier versions perform no authorization checks
at all: any unprivileged local user can issue any privileged command to
multipathd.
The symlink attack (CVE-2022-41973) was introduced in May 2018 (version
0.7.7) by commit 65d0a63 ("functions to indicate mapping failure in
/dev/shm"); the vulnerable code was hardened significantly in May 2020
(version 0.8.5) by commit 40ee3ea ("simplify failed wwid code"), but it
remains exploitable nonetheless.
========================================================================
CVE-2022-41974: Authorization bypass
========================================================================
The multipathd daemon listens for client connections on an abstract Unix
socket (conveniently, the multipathd binary itself can act as a client,
if executed with non-option arguments; we use this feature extensively
in this advisory to connect and send commands to the multipathd daemon):
------------------------------------------------------------------------
$ ps -ef | grep 'multipath[d]'
root 377 1 0 13:55 ? 00:00:00 /sbin/multipathd -d -s
$ ss -l -x | grep 'multipathd'
u\_str LISTEN 0 4096 @/org/kernel/linux/storage/multipathd 18105
------------------------------------------------------------------------
The commands sent by a client to multipathd are composed of keywords,
and internally, each keyword is identified by a different bit; for
example, "list" is 1 (1<<0), "add" is 2 (1<<1), and "path" (which
requires a parameter) is 65536 (1<<16):
------------------------------------------------------------------------
155 load\_keys (void)
...
163 r += add\_key(keys, "list", LIST, 0);
164 r += add\_key(keys, "show", LIST, 0);
165 r += add\_key(keys, "add", ADD, 0);
...
183 r += add\_key(keys, "path", PATH, 1);
------------------------------------------------------------------------
53 #define LIST (1ULL << \_\_LIST)
54 #define ADD (1ULL << \_\_ADD)
..
69 #define PATH (1ULL << \_\_PATH)
------------------------------------------------------------------------
6 enum {
7 \_\_LIST, /\* 0 \*/
8 \_\_ADD,
..
23 \_\_PATH,
------------------------------------------------------------------------
In turn, each command is associated with a handler (a C function) by its
fingerprint -- the bitwise OR of its constituent keywords; for example,
the command "list path PARAM" is associated with cli\_list\_path() by the
fingerprint 65537 (LIST+PATH=1+65536), and the command "add path PARAM"
is associated with cli\_add\_path() by the fingerprint 65538
(ADD+PATH=2+65536):
------------------------------------------------------------------------
1522 void init\_handler\_callbacks(void)
....
1527 set\_handler\_callback(LIST+PATH, cli\_list\_path);
....
1549 set\_handler\_callback(ADD+PATH, cli\_add\_path);
------------------------------------------------------------------------
321 static uint64\_t
322 fingerprint(const struct \_vector \*vec)
...
325 uint64\_t fp = 0;
...
331 vector\_foreach\_slot(vec, kw, i)
332 fp += kw->code;
333
334 return fp;
------------------------------------------------------------------------
89 static struct handler \*
90 find\_handler (uint64\_t fp)
..
95 vector\_foreach\_slot (handlers, h, i)
96 if (h->fingerprint == fp)
97 return h;
98
99 return NULL;
------------------------------------------------------------------------
When multipathd receives a command from a client, it first performs an
authentication check and an authorization check (both at line 491):
------------------------------------------------------------------------
431 static int client\_state\_machine(struct client \*c, struct vectors \*vecs,
...
485 case CLT\_PARSE:
486 c->error = parse\_cmd(c);
487 if (!c->error) {
...
491 if (!c->is\_root && kw->code != LIST) {
492 c->error = -EPERM;
...
495 }
496 }
497 if (c->error)
...
501 else
502 set\_client\_state(c, CLT\_WORK);
...
522 case CLT\_WORK:
523 c->error = execute\_handler(c, vecs);
------------------------------------------------------------------------
- Authentication: if the client's UID (obtained from SO\_PEERCRED) is 0
(i.e., if is\_root is true), then the client is privileged; otherwise,
it is unprivileged.
- Authorization: if the client is privileged, it is allowe...