---
title: Linux 6.6 Race Condition
url: https://cxsecurity.com/issue/WLB-2024110041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-26
fetch_date: 2025-10-06T19:16:57.756587
---

# Linux 6.6 Race Condition

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
|  |  | |  | | --- | | **Linux 6.6 Race Condition** **2024.11.25**  Credit:  **[Jann Horn](https://cxsecurity.com/author/Jann%2BHorn/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-50066](https://cxsecurity.com/cveshow/CVE-2024-50066/ "Click to see CVE-2024-50066")**  CWE: **[CWE-362](https://cxsecurity.com/cwe/CWE-362 "Click to see CWE-362")** | |

Summary
I found a security-relevant race between mremap() and THP code. Reaching the buggy code typically requires the ability to create unprivileged namespaces. The bug leads to installing physical address 0 as a page table, which is likely exploitable in several ways: For example, triggering the bug in multiple processes can probably lead to unintended page table sharing, which probably can lead to stale TLB entries pointing to freed pages.
I also found two other (untested) theoretical races, but those arguably might not even count as bugs, and I'm pretty sure they're not security bugs. I am including my analysis of the closely related non-issues 2 and 3 as context in case you're curious, but I think they're stuff we can deal with on the public list later (or maybe even just leave as-is). Feel free to ignore that part of this report.
I will send a suggested patch for the security bug, but I think it's unclear if my patch is actually the right way to fix it.
This bug is subject to a 90-day disclosure deadline. If a fix for this issue is made available to users before the end of the 90-day deadline, this bug report will become public 30 days after the fix was made available. Otherwise, this bug report will become public at the deadline. The scheduled deadline is 2024-12-31.
For more details, see the Project Zero vulnerability disclosure policy: https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-policy.html
Security bug: move\_normal\_pmd vs MADVISE\_COLLAPSE
Description
In mremap(), move\_page\_tables() looks at the type of the PMD entry and the specified address range to figure out by which method the next chunk of page table entries should be moved. At that point, the mmap\_lock is held in write mode, but no rmap locks are held. For PMD entries that point to page tables and are fully covered by the source address range, move\_pgt\_entry(NORMAL\_PMD, ...) is called, which first takes rmap locks, then does move\_normal\_pmd().
move\_normal\_pmd() takes the necessary page table locks at source and destination, then moves an entire page table from the source to the destination:
/\* Clear the pmd \*/
pmd = \*old\_pmd;
pmd\_clear(old\_pmd);
VM\_BUG\_ON(!pmd\_none(\*new\_pmd));
pmd\_populate(mm, new\_pmd, pmd\_pgtable(pmd));
flush\_tlb\_range(vma, old\_addr, old\_addr + PMD\_SIZE);
The problem is: The rmap locks, which protect against concurrent page table removal by retract\_page\_tables() in the THP code, are only taken after we have inspected the PMD entry to decide how to move it. So we can race as follows (with two processes that have mappings of the same tmpfs file that is stored on a tmpfs mount with huge=advise):
process A process B
========= =========
mremap
mremap\_to
move\_vma
move\_page\_tables
get\_old\_pmd
alloc\_new\_pmd
\*\*\* PREEMPT \*\*\*
madvise(MADV\_COLLAPSE)
do\_madvise
madvise\_walk\_vmas
madvise\_vma\_behavior
madvise\_collapse
hpage\_collapse\_scan\_file
collapse\_file
retract\_page\_tables
i\_mmap\_lock\_read(mapping)
pmdp\_collapse\_flush
i\_mmap\_unlock\_read(mapping)
move\_pgt\_entry(NORMAL\_PMD, ...)
take\_rmap\_locks
move\_normal\_pmd
drop\_rmap\_locks
In this case, while move\_normal\_pmd() expects to see a PMD entry pointing to a page table, the PMD entry has actually been cleared. So this line:
pmd\_populate(mm, new\_pmd, pmd\_pgtable(pmd));
runs pmd\_pgtable() on a cleared PMD entry. On typical implementations (including the X86 one), this simply masks off some bits of pmd and assumes that the remainder is a physical address - so pmd\_pgtable(0) returns a pointer to the page for physical address 0. Then, pmd\_populate() constructs a PMD entry that points to this physical address as a page table.
So this ends up installing physical address 0 as a page table.
Fixing it
I guess there are two ways we could fix this:
Hold the rmap locks much more broadly in move\_page\_tables(). In particular, take them before inspecting the source pmd, and if we do a PMD-level move, keep them held throughout the entire move.
Add a bunch of extra recheck/retry logic.
I think the first option is nicer in terms of code complexity. Moving the lock up requires a small bit of refactoring though, and the broader locking could conceivably degrade the performance of concurrent rmap access.
I will send a suggested patch for the first option in a minute (and I have tested that with that patch, my reproducer no longer triggers); but we might want to do some more bikeshedding of whether this is the right way to patch it, and if yes, whether the patch is doing too little lock-dropping for performance or adds too much complexity with the lock-dropping...
Reproducer
I made a testcase that triggers this issue after a while and causes a splat when the kernel later tries to unmap this page table at physical address 0:
#define \_GNU\_SOURCE
#include <err.h>
#include <sched.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/stat.h>
#include <sys/prctl.h>
#include <sys/mount.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <sys/ioctl.h>
static void pin\_to(int cpu) {
cpu\_set\_t cset;
CPU\_ZERO(&cset);
CPU\_SET(cpu, &cset);
if (sched\_setaffinity(0, sizeof(cpu\_set\_t), &cset))
err(1, "set affinity");
}
#ifndef MADV\_COLLAPSE
#define MADV\_COLLAPSE 25
#endif
#define SYSCHK(x) ({ \
typeof(x) \_\_res = (x); \
if (\_\_res == (typeof(x))-1) \
err(1, "SYSCHK(" #x ")"); \
\_\_res; \
})
static void write\_file(char \*name, char \*buf) {
int fd = SYSCHK(open(name, O\_WRONLY));
if (write(fd, buf, strlen(buf)) != strlen(buf))
err(1, "write %s", name);
close(fd);
}
static void write\_map(char \*name, int outer\_id) {
char bu...