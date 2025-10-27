---
title: SEC Consult SA-20221213-0 :: Privilege Escalation Vulnerabilities (UNIX Insecure File Handling) in SAP Host Agent (saposcol)
url: https://seclists.org/fulldisclosure/2022/Dec/12
source: Full Disclosure
date: 2022-12-14
fetch_date: 2025-10-04T01:28:45.431399
---

# SEC Consult SA-20221213-0 :: Privilege Escalation Vulnerabilities (UNIX Insecure File Handling) in SAP Host Agent (saposcol)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20221213-0 :: Privilege Escalation Vulnerabilities (UNIX Insecure File Handling) in SAP Host Agent (saposcol)

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Tue, 13 Dec 2022 07:29:14 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20221213-0 >
=======================================================================
               title: Privilege Escalation Vulnerabilities (UNIX Insecure File
                      Handling)
             product: SAP® Host Agent (saposcol)
  vulnerable version: see section "Vulnerable /  tested versions"
       fixed version: see SAP security note 3159736
          CVE number: CVE-2022-35295
              impact: high
            homepage: https://www.sap.com/about.html
               found: 2022-02-18
                  by: Fabian Hagg (Office Vienna)
                      SEC Consult Vulnerability Lab

                      An integrated part of SEC Consult, an Atos company
                      Europe | Asia | North America

                      https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"SAP® Host Agent is an agent that can accomplish several life-cycle
management tasks, such as operating system monitoring, database
monitoring, system instance control and provisioning."

Source:
https://help.sap.com/viewer/141cbf7f183242b0ad0964a5195b24e7/202110.000/en-US/48c6f9627a004da5e10000000a421937.html

Business recommendation:
------------------------
By exploiting the vulnerabilities documented in this advisory, a
local attacker may escalate privileges on UNIX systems to fully
compromise vulnerable servers with root privileges.

SEC Consult recommends to implement security note 3159736 where the
documented issue is fixed according to the vendor. We advise installing
the corrections as a matter of priority to keep business-critical
data secured.

Vulnerability overview/description:
-----------------------------------
Multiple vulnerabilities were identified that could allow a local
attacker authenticated as <sid>adm to escalate privileges on SAP UNIX
systems. No additional user authentication is required to exploit
these issues. The vulnerabilities are due to the privileged saposcol
process generating files in its default working directory (/usr/sap/tmp;
defined by profile parameter DIR_PERF) owned by the <sid>adm user (sapsys
group), and following symbolic links (symlinks) when trying to open/create
these files. Note that in some environments the directory might not be
owned by the <sid>adm user account but be writable for all users of
group sapsys including <sid>adm.

An attacker is able to spoof the symbolic links, thus traversing the
file system and gaining access to unintended resources. This could permit
an attacker to read/write/corrupt files owned by the root user account
leading to privilege escalation.

1) UNIX Symlink Following and Insecure File Permissions in Detailed
    Lock Logging Feature of saposcol

The stand-alone saposcol binary available in UNIX systems at
/usr/sap/hostctrl/exe/saposcol provides a debugging feature called
"detailed lock logging". For this option to be activated, the user
<sid>adm can perform the following action:

- Starting the stand-alone saposcol binary with command line argument
   StartLockLog (/usr/sap/hostctrl/exe/saposcol StartLockLog).

Once executed, a special flag is set in shared memory that triggers
multiple running processes and services (sapstartsrv, saposcol) to
create a file called SaposcolMonAreaLocking.log in the default
working directory. This directory is writable by the user
<sid>adm (group sapsys). One of the processes trying to create the
file is the main saposcol service running in the context of the root
user account. It was observed that the file is created by the process
using the openat() syscall with flags O_WRONLY, O_CREAT and O_APPEND.

-----------------------------------------------------------------------
root@sapsrv:~# ps -efw
root 1998 /usr/sap/hostctrl/exe/saposcol -l -w60 pf=/usr/sap/hostctrl/
exe/host_profile

# Tracing the sapsocol process with PID 1998
root@sapsrv:~# strace -f -e trace=openat,chmod,chown -p 1998 -q
[...]
openat(AT_FDCWD, "/usr/sap/tmp/SaposcolMonAreaLocking.log", O_WRONLY|
O_CREAT|O_APPEND, 0666) = 6
chmod("/usr/sap/tmp/SaposcolMonAreaLocking.log", 0666) = 0
-----------------------------------------------------------------------

Since the openat() call does not have the O_EXCL flag set, it is not
ensured that the process actually creates the file. That is, if the
file under the given path already exists, the process tries to open
the existing file for appending data to it and changing its permissions
to world-readable/world-writable (666). Since the process, when
opening an existing file, does not check (e.g., by setting the
O_NOFOLLOW flag) whether it is a symbolic link that resolves to a
target outside of the intended directory, an attacker can cause the
process to operate on unauthorized files by placing a malicious symlink
before activating the detailed lock logging feature via the stand-alone
saposcol binary. This vulnerability may allow an attacker to gain read/
write access to arbitrary files owned by the root user account.

2) UNIX Symlink Following and Race Condition in Hardware Reporting
    Feature of saposcol

The main saposcol service running in the context of the root user
account allows to generate reports containing information about the
underlying operating system and hardware configuration. For these
reports to be generated, the user <sid>adm can perform different
actions:

- Using function GetSAPOSColHWConf of the saphostctrl binary
   (/usr/sap/hostctrl/exe/saphostctrl -function GetSAPOSColHWConf
   [-format <tree|flat>]) that generates a SOAP request for the host
   agent service (SAPHostControl) on port 1128/1129. The request is
   forwarded by sapstartsrv to the saposcol service for processing.

- Manually crafting a SOAP request identical to the one generated by
   the saphostctrl binary and sending it to localhost on port 1128
   /1129 via the loopback interface (e.g., using curl). This request
   is forwarded by sapstartsrv to the saposcol service for processing.

- Using the dialog interface of the stand-alone saposcol binary
   (/usr/sap/hostctrl/exe/saposcol -d) and its "ask" feature (ask
   Hardware/ ask HardwareXML) that communicates with the saposcol
   service using shared memory segments.

- Using transaction ST06 in the application layer (ABAP based
   instances only).

When requested via the SOAP interface of SAPHostControl (sapstartsrv),
the privileged saposcol process tries to generate the file
hwconfig_<host> / hw_<host>.xml (depending on whether the XML output
format is queried) in its working directory. The process then
collects information about OS resources and writes this data to the given
file. Once saposcol finished its work, the SAPHostControl service opens
and reads the file before providing the results to the caller via SOAP
response. That is, the newly created file is handled as a shared
resource by both processes. It was obs...