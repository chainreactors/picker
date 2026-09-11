---
title: Redtail Payload Analysis &#x5b;Guest Diary&#x5d;, (Wed, Sep 9th)
url: https://isc.sans.edu/diary/rss/33326
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-10
fetch_date: 2026-09-11T06:53:09.578164
---

# Redtail Payload Analysis &#x5b;Guest Diary&#x5d;, (Wed, Sep 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33324)

Click HERE to learn more about classes Guy is teaching for SANS

# [Redtail Payload Analysis [Guest Diary]](/forums/diary/Redtail%2BPayload%2BAnalysis%2BGuest%2BDiary/33326/)

**Published**: 2026-09-09. **Last Updated**: 2026-09-10 12:58:10 UTC
**by** [Aaron Ng, SANS.edu BACS Student](/handler_list.html#aaron-ng,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Redtail%2BPayload%2BAnalysis%2BGuest%2BDiary/33326/#comments)

[This is a Guest Diary by Aaron Ng, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Following a RedTail Linux Payload from DShield to Dynamic Analysis**

During monitoring of my DShield honeypot, I observed an attacker uploading a collection of Linux executables targeting several processor architectures. The files included ARM, ARM64, i686, RISC-V and x86-64 variants named as part of a RedTail deployment package. Rather than relying only on static indicators or public threat-intelligence results, I extracted the captured payloads from Cowrie and analyzed the x86-64 variant in an isolated malware-analysis environment.

The x86-64 sample analyzed in this article has the following SHA-256 hash:
63be5f38b520b3143732962a5f8fec1f9abd1f483dbc741ed324e58f955dd35e

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic1.png)

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic2.png)

Dynamic analysis showed that the payload did considerably more than simply execute. It changed its visible process identity, terminated other processes, killed one of the filesystem-monitoring processes used during the experiment, and created a TCP listening socket. A matched pair of pre- and post-execution memory images was also acquired from the Proxmox hypervisor to preserve the malware's runtime state independently of the infected guest.

**From Cowrie Upload to Malware Sample**

The original files were recovered from the Cowrie download directory on the DShield honeypot and copied into a separate folder named after the event.code on the [DShield SIEM](https://github.com/bruneaug/DShield-SIEM) “attack-a7fc773a9f1a”. The attack delivered multiple architecture-specific versions of the same malware family together with shell scripts responsible for deployment and cleanup.

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic3.png)
![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic4.png)

The recovered set included variants for:

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic5.png)

The associated deployment script inspected the host architecture and selected the appropriate RedTail executable. Static inspection of the x86-64 binary identified it as a statically linked ELF executable. Strings extracted from the sample also contained an indication that it had been processed with the UPX executable packer.

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic6.png)
![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic7.png)

For the controlled experiment described here, I selected redtail.x86\_64, matching the architecture of the Ubuntu analysis VM.

**Isolated Analysis Environment**

The malware was executed inside an Ubuntu 24.04 virtual machine hosted on Proxmox. The victim was assigned:
10.66.66.10/24

and was connected only to an isolated malware-analysis network.

An [INetSim](https://www.inetsim.org/index.html) server at:

10.66.66.2
provided simulated network services. The victim had no default route to the Internet. Before execution, connectivity to INetSim was verified while attempts to reach an external address such as 8.8.8.8 returned Network is unreachable.

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic8.png)
![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic9.png)

This design allowed the malware to encounter DNS and network services without allowing it to communicate with real external infrastructure.

Several monitoring mechanisms were started before staging the sample. These included auditd syscall and filesystem rules, inotifywait filesystem monitoring, continuous process and socket sampling, journal and kernel logging, tcpdump on both the victim and INetSim systems, and strace around the actual malware execution.

In addition, guest memory was acquired from outside the infected system using QEMU's dump-guest-memory functionality on the Proxmox host.

Detonating the redtail.x86\_64 Elf executable only (Setup.sh and Clean.sh were not ran)

There were three runs (Run 001.1, Run 001.2 and Run 002) of the malware detonation executed, with the VM reverted back to original pre-detonation state between RUN 001 and RUN 002. In RUN 001, the malware file was detonated twice. RUN 001 was run as user privileges but RUN 002 was run as root.

This report will focus on analyzing RUN 002 with comparisons made to RUN 001.1 and 1.2 to establish similiarities and differences between the runs.

Analysing Run 002, two memory images were collected:

vm610-baseline-pre-redtail.elf
vm610-post-redtail.elf

Both images were approximately 6 GB and were independently SHA-256 verified after acquisition. The baseline image was collected after all monitoring processes had been started but before the malware was staged, making the two images suitable for later differential analysis.

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic10.png)![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic11.png)

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic12.png)

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic13.png)

**Controlled Execution**

For the second experiment, the malware was executed directly with the argument observed during the earlier investigation:

**redtail.x86\_64 ssh**
strace confirmed successful execution:
execve("/analysis/run-002/sample/redtail.x86\_64",
       ["/analysis/run-002/sample/redtail.x86\_64", "ssh"],
       ...) = 0

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic14.png)

This was important because it established that the subsequent behavior belonged to a successfully executing instance of the recovered Cowrie payload rather than to a failed launch or unrelated process.
Two RedTail-backed processes remained running after execution:

PID 10395
PID 10404

Both /proc/<PID>/exe links resolved to:
/analysis/run-002/sample/redtail.x86\_64
and hashing those executable mappings produced the same SHA-256 as the original recovered sample.
Despite this, neither process presented itself as redtail.x86\_64.
Instead, both appeared as:

php-fpm: pool www

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic15.png)
![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic16.png)

**Process Masquerading**

The strace output captured the mechanism RedTail used to alter its visible process name:
prctl(PR\_SET\_NAME, "php") = 0
The successful return value demonstrates that RedTail deliberately modified its task name.
The result was a process that appeared in ordinary process listings as a legitimate PHP-FPM worker:
php-fpm: pool www
while /proc/<PID>/exe continued to identify the executable as the original RedTail sample.

This creates a useful forensic distinction. A process listing by itself could suggest that PHP-FPM was running on the system, while examining /proc/<PID>/exe and hashing the mapped executable revealed that the apparent PHP process was actually the RedTail binary.

This behavior was also consistent with an earlier experimental run in which surviving RedTail processes presented themselves using a PostgreSQL-like process name. The repeated observation suggests that RedTail uses legitimate-looking service names to make malicious processes less conspicuous in routine process inspection.

![](https://isc.sans.edu/diaryimages/images/Aaron_Ng_pic17.png)

**Process Ter...