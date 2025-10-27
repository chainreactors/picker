---
title: Ruckus IoT Controller 1.7.1.0 Undocumented Backdoor Account
url: https://cxsecurity.com/issue/WLB-2025050027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-10
fetch_date: 2025-10-06T22:26:29.299092
---

# Ruckus IoT Controller 1.7.1.0 Undocumented Backdoor Account

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
|  |  | |  | | --- | | **Ruckus IoT Controller 1.7.1.0 Undocumented Backdoor Account** **2025.05.09**  Credit:  **[korelogic](https://cxsecurity.com/author/korelogic/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2019-1000018](https://cxsecurity.com/cveshow/CVE-2019-1000018/ "Click to see CVE-2019-1000018")** | **[CVE-2021-33216](https://cxsecurity.com/cveshow/CVE-2021-33216/ "Click to see CVE-2021-33216")**  CWE: **[CWE-912](https://cxsecurity.com/cwe/CWE-912 "Click to see CWE-912")** | |

# Exploit Title: CommScope Ruckus IoT Controller 1.7.1.0 - Undocumented Account
# Date: 2021.05.26
# Exploit Author: korelogic
# Vendor Homepage: https://www.commscope.com/globalassets/digizuite/917216-faq-security-advisory-id-20210525-v1-0.pdf
# Affected Product: Ruckus IoT Controller
# Version: 1.7.1.0 and earlier
# Tested on: Linux
# CVE : CVE-2021-33216,CVE-2019-1000018
KL-001-2021-007: CommScope Ruckus IoT Controller Undocumented Account
Advisory ID: KL-001-2021-007
Publication Date: 2021.05.26
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2021-007.txt
1. Vulnerability Details
Affected Vendor: CommScope
Affected Product: Ruckus IoT Controller
Affected Version: 1.7.1.0 and earlier
Platform: Linux
CWE Classification: CWE-798: Use of Hard-coded Credentials, CWE-912: Hidden Functionality
CVE ID: CVE-2021-33216
2. Vulnerability Description
An upgrade account is included in the IoT Controller OVA that
provides the vendor undocumented access via Secure Copy (SCP).
3. Technical Description
Once the OVA is imported into VirtualBox, a VMDK file is
created. The VMDK file can be mounted and the directory
structure and its contents can be perused.
An authorized\_keys file exists that allows an
individual/organization possessing the SSH private key to
access the virtual appliance using the 'vriotiotupgrade'
account. The 'vriotiotupgrade' account is restricted to scp,
per the rssh configuration.
Additionally, it appears that the IoT Controller has rssh version 2.3.4
installed and in use. At the time of this advisory, there are at least
three remote command injection vulnerabilities in this particular version
of rssh: CVE-2019-3463, CVE-2019-3464 and CVE-2019-1000018.
4. Mitigation and Remediation Recommendation
The vendor has released an updated firmware (1.8.0.0) which
remediates the described vulnerability. Firmware and release
notes are available at:
https://www.commscope.com/globalassets/digizuite/917216-faq-security-advisory-id-20210525-v1-0.pdf
5. Credit
This vulnerability was discovered by Jim Becher (@jimbecher)
of KoreLogic, Inc.
6. Disclosure Timeline
2021.03.30 - KoreLogic submits vulnerability details to
CommScope.
2021.03.30 - CommScope acknowledges receipt and the intention
to investigate.
2021.04.06 - CommScope notifies KoreLogic that this issue,
along with several others reported by KoreLogic,
will require more than the standard 45 business
day remediation timeline.
2021.04.06 - KoreLogic agrees to extend disclosure embargo if
necessary.
2021.04.30 - CommScope informs KoreLogic that remediation for
this vulnerability will be available inside of the
standard 45 business day timeline. Requests
KoreLogic acquire CVE number for this
vulnerability.
2021.05.14 - 30 business days have elapsed since the
vulnerability was reported to CommScope.
2021.05.17 - CommScope notifies KoreLogic that the patched
version of the firmware will be available the week
of 2021.05.24.
2021.05.19 - KoreLogic requests CVE from MITRE.
2021.05.19 - MITRE issues CVE-2021-33216.
2021.05.25 - CommScope releases firmware 1.8.0.0 and associated
advisory.
2021.05.26 - KoreLogic public disclosure.
7. Proof of Concept
With the VMDK file mounted at the current working directory:
$ find . -name authorized\_keys
./VRIOT/ap-images/authorized\_keys
./VRIOT/ops/ap-images/authorized\_keys
$ cat VRIOT/ap-images/authorized\_keys
ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAACAQCp1X4UH+0IALnLKsqbSZwgbzA1clXWXguNpTZ+Km7irkMaXVRt6IL78mdK+nKUvvQcRnAhQ0TgoqINrdLzMTYwoVaOcBq5Lw21A5JrP8IQANMAiVSM30umJYuTqnbPO4HHIi9/Gk/wUtJiwvD/ygNx7z0g1a9PIzQxOITLpwVkEU2iDdlrZDHR35jI/ddRRsbPe9ezeYGDoprgQagw634fa9tzI74oj5/Xh64679yjA0bQx+i8ZXSIHFPSHp0yiDyMZfvLIqdqb0mEAN1JnaHfIiq4o8/wa8zp7nVADo6Pxweklc1kqALFUxrzdP/6Z0hITp1Ke/xdA2S4LT3ye85QVM/k3Dd54qFpMAJsinYb18Ykyj0PTZskcBWB+l9VevpJXv+3DDH2+98Ledv/fnXQ9VapxW572fX2HkEoh4Nmt5VUx0JPR/0onwOVeuwQLp5qnHxmzgL8DMS62QkTT1VdaCqXS01DMPorKQUtmvAxohJUJX4df9JoOcwRpvKSspn+6UU1krPZHX1QYvPrRsfYhJ9SCzrVxmuC0DR3FqxGoix5su4DqCpRxq0QhwC4+DwIMt4KTIjF3p35s+bjP1luwITJOxVlIswpyZKS0hITFLJtAE7c493wX7hxUdy+LfyHXlMIoJcYM11WXLAysHcWyfmSpQ8H5GV0vxela0Qg7Q==
chandini.venkatesh@commscope.com
$ cat VRIOT/ops/ap-images/authorized\_keys
ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAACAQCp1X4UH+0IALnLKsqbSZwgbzA1clXWXguNpTZ+Km7irkMaXVRt6IL78mdK+nKUvvQcRnAhQ0TgoqINrdLzMTYwoVaOcBq5Lw21A5JrP8IQANMAiVSM30umJYuTqnbPO4HHIi9/Gk/wUtJiwvD/ygNx7z0g1a9PIzQxOITLpwVkEU2iDdlrZDHR35jI/ddRRsbPe9ezeYGDoprgQagw634fa9tzI74oj5/Xh64679yjA0bQx+i8ZXSIHFPSHp0yiDyMZfvLIqdqb0mEAN1JnaHfIiq4o8/wa8zp7nVADo6Pxweklc1kqALFUxrzdP/6Z0hITp1Ke/xdA2S4LT3ye85QVM/k3Dd54qFpMAJsinYb18Ykyj0PTZskcBWB+l9VevpJXv+3DDH2+98Ledv/fnXQ9VapxW572fX2HkEoh4Nmt5VUx0JPR/0onwOVeuwQLp5qnHxmzgL8DMS62QkTT1VdaCqXS01DMPorKQUtmvAxohJUJX4df9JoOcwRpvKSspn+6UU1krPZHX1QYvPrRsfYhJ9SCzrVxmuC0DR3FqxGoix5su4DqCpRxq0QhwC4+DwIMt4KTIjF3p35s+bjP1luwITJOxVlIswpyZKS0hITFLJtAE7c493wX7hxUdy+LfyHXlMIoJcYM11WXLAysHcWyfmSpQ8H5GV0vxela0Qg7Q==
chandini.venkatesh@commscope.com
$ grep "ap-images" etc/passwd
vriotiotupgrade:x:1002:1002::/VRIOT/ap-images/:/usr/bin/rssh
$ tail -8 etc/ssh/sshd\_config
Match User vriotiotupgrade
PasswordAuthentication no
AuthorizedKeysFile /VRIOT/ap-images/authorized\_keys
Match User vriotha
PasswordAuthentication yes
$ grep -v ^# etc/rssh.conf
logfacility = LOG\_USER
allowscp
umask = 022
The contents of this advisory are copyright(c) 2021
KoreLogic, Inc. and are licensed under a Creative Commons
Attribution Share-Alike 4.0 (United States) License:
http://creativecommons.org/licenses/by-sa/4.0/
KoreLogic, Inc. is a founder-owned and operated company with a
proven track record of providing security services t...