---
title: snap-confine must_mkdir_and_open_with_perms() Race Condition
url: https://cxsecurity.com/issue/WLB-2022120021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-10
fetch_date: 2025-10-04T01:05:17.409136
---

# snap-confine must_mkdir_and_open_with_perms() Race Condition

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
|  |  | |  | | --- | | **snap-confine must\_mkdir\_and\_open\_with\_perms() Race Condition** **2022.12.09**  Credit:  **[Qualys Security Advisory](https://cxsecurity.com/author/Qualys%2BSecurity%2BAdvisory/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-3328](https://cxsecurity.com/cveshow/CVE-2022-3328/ "Click to see CVE-2022-3328")** | **[CVE-2021-44731](https://cxsecurity.com/cveshow/CVE-2021-44731/ "Click to see CVE-2021-44731")** | **[CVE-2022-41973](https://cxsecurity.com/cveshow/CVE-2022-41973/ "Click to see CVE-2022-41973")** | **[CVE-2021-3995](https://cxsecurity.com/cveshow/CVE-2021-3995/ "Click to see CVE-2021-3995")** | **[CVE-2021-3996](https://cxsecurity.com/cveshow/CVE-2021-3996/ "Click to see CVE-2021-3996")** | **[CVE-2022-41974](https://cxsecurity.com/cveshow/CVE-2022-41974/ "Click to see CVE-2022-41974")**  CWE: **[CWE-362](https://cxsecurity.com/cwe/CWE-362 "Click to see CWE-362")** | |

Qualys Security Advisory
Race condition in snap-confine's must\_mkdir\_and\_open\_with\_perms()
(CVE-2022-3328)
========================================================================
Contents
========================================================================
Summary
Background
Exploitation
Acknowledgments
Timeline
I can't help but feel a missed opportunity to integrate lyrics from
one of the best songs ever: [SNAP! - The Power (Official Video)]
-- https://twitter.com/spendergrsec/status/1494420041076461570
========================================================================
Summary
========================================================================
We discovered a race condition (CVE-2022-3328) in snap-confine, a
SUID-root program installed by default on Ubuntu. In this advisory, we
tell the story of this vulnerability (which was introduced in February
2022 by the patch for CVE-2021-44731) and detail how we exploited it in
Ubuntu Server (a local privilege escalation, from any user to root) by
combining it with two vulnerabilities in multipathd (an authorization
bypass and a symlink attack, CVE-2022-41974 and CVE-2022-41973):
https://www.qualys.com/2022/10/24/leeloo-multipath/leeloo-multipath.txt
========================================================================
Background
========================================================================
Like the crack of the whip, I Snap! attack
Radical mind, day and night all the time
-- SNAP! - The Power
In February 2022, we published CVE-2021-44731 in our "Lemmings" advisory
(https://www.qualys.com/2022/02/17/cve-2021-44731/oh-snap-more-lemmings.txt):
to set up a snap's sandbox, snap-confine created the temporary directory
/tmp/snap.$SNAP\_NAME or reused it if it already existed, even if it did
not belong to root; a local attacker could race against snap-confine,
retain control over /tmp/snap.$SNAP\_NAME, and eventually obtain full
root privileges.
This vulnerability was patched by commit acb2b4c ("cmd/snap-confine:
Prevent user-controlled race in setup\_private\_mount"), which introduced
a new helper function, must\_mkdir\_and\_open\_with\_perms():
------------------------------------------------------------------------
142 static void setup\_private\_mount(const char \*snap\_name)
...
169 sc\_must\_snprintf(base\_dir, sizeof(base\_dir), "/tmp/snap.%s", snap\_name);
...
176 base\_dir\_fd = must\_mkdir\_and\_open\_with\_perms(base\_dir, 0, 0, 0700);
------------------------------------------------------------------------
55 static int must\_mkdir\_and\_open\_with\_perms(const char \*dir, uid\_t uid, gid\_t gid,
56 mode\_t mode)
..
61 mkdir:
..
67 if (mkdir(dir, 0700) < 0 && errno != EEXIST) {
..
70 fd = open(dir, O\_RDONLY | O\_DIRECTORY | O\_CLOEXEC | O\_NOFOLLOW);
..
81 if (fstat(fd, &st) < 0) {
..
84 if (st.st\_uid != uid || st.st\_gid != gid
85 || st.st\_mode != (S\_IFDIR | mode)) {
...
130 if (rename(dir, random\_dir) < 0) {
...
135 goto mkdir;
------------------------------------------------------------------------
- the temporary directory /tmp/snap.$SNAP\_NAME is created at line 67, if
it does not exist already;
- if it already exists, and if it does not belong to root (at line 84),
then it is moved out of the way (at line 130) by rename()ing it to a
random directory in /tmp, and its creation is retried (at line 135).
When we reviewed this patch back in December 2021, we felt very nervous
about this rename() call (because it allows a local attacker to rename()
a directory they do not own), and we advised the Ubuntu Security Team to
either not reuse the directory /tmp/snap.$SNAP\_NAME at all, or to create
it in a non-world-writable directory instead of /tmp, or at least to use
renameat2(RENAME\_EXCHANGE) instead of rename(). Unfortunately, all of
these ideas were deemed impractical (for example, renameat2() is not
supported by older kernel and glibc versions); moreover, we (Qualys)
failed to come up with a feasible attack plan against this rename()
call, so the patch was kept in its current form.
After the release of Ubuntu 22.04 in April 2022, we decided to revisit
snap-confine and its recent hardening changes, and we finally found a
way to exploit the rename() call in must\_mkdir\_and\_open\_with\_perms().
========================================================================
Exploitation
========================================================================
It's getting, it's getting, it's getting kinda heavy
It's getting, it's getting, it's getting kinda hectic
-- SNAP! - The Power
The three key ideas to exploit the rename() of /tmp/snap.$SNAP\_NAME are:
1/ snap-confine operates in /tmp to create a snap's temporary directory
(/tmp/snap.$SNAP\_NAME in setup\_private\_mount()), but it also operates in
/tmp to create the snap's \*root\* directory (/tmp/snap.rootfs\_XXXXXX in
sc\_bootstrap\_mount\_namespace(), where all of the Xs are randomized by
mkdtemp()), and the string rootfs\_XXXXXX is accepted as a valid snap
instance name by sc\_instance\_name\_validate() (when all of the Xs are
lowercase alphanumeric):
------------------------------------------------------------------------
286 static void...