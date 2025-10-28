---
title: NetExec – Network Execution Toolkit for Windows and Active Directory
url: https://www.darknet.org.uk/2025/10/netexec-network-execution-toolkit-for-windows-and-active-directory/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-27
fetch_date: 2025-10-28T03:00:16.821720
---

# NetExec – Network Execution Toolkit for Windows and Active Directory

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# NetExec – Network Execution Toolkit for Windows and Active Directory

October 24, 2025

Views: 245

NetExec is a multi-protocol network execution toolkit focused on Windows and Active Directory (AD) environments. It exposes a single binary command, `nxc`, which supports multiple transport protocols including SMB, SSH, LDAP, WMI, WinRM, RDP, VNC, MSSQL, and NFS. The project is designed to allow operators to enumerate hosts and credentials, execute commands across a network, and integrate protocol-specific modules for everyday red-team tasks such as credential harvesting and remote command execution.

![NetExec - Network Execution Toolkit for Windows and Active Directory](https://www.darknet.org.uk/wp-content/uploads/2025/10/NetExec-Network-Execution-Toolkit-for-Windows-and-Active-Directory-640x427.jpg)

It was initially started in 2015 as [CrackMapExec, an Active Directory Post-exploitation tool.](https://www.darknet.org.uk/2017/07/crackmapexec-active-directory-post-exploitation-tool/)

## Features

NetExec provides a protocol-oriented workflow so operators can pick the right transport for the target environment. Key capabilities include concurrent execution via configurable threads, protocol modules for SMB/LDAP/WinRM/RDP, and more, credential handling,g and integration hooks for exporting data to graph tools or logs. The project includes documented modules for enumeration, command execution, and data exfiltration workflows designed for post-exploit lateral movement.

## Installation

The recommended installation method is `pipx` to install the package into an isolated environment. This preserves system-wide Python while giving you a globally available `nxc` command. The GitHub README shows the canonical install commands. Example:

python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install git+https://github.com/Pennyw0rth/NetExec.git

|  |  |
| --- | --- |
| 1  2  3 | python3 -m pip install --user pipx  python3 -m pipx ensurepath  pipx install git+https://github.com/Pennyw0rth/NetExec.git |

These steps come from the project repository and are the recommended quick-install method. Validate the installation by running `nxc --help`.

## Usage and validated –help output

NetExec exposes a global help and per-protocol help. Use `nxc --help` to list general options and available protocols. Below is the tool’s published help excerpt as shown in the official NetExec documentation:

#~ nxc --help
usage: nxc &#91;-h] &#91;-t THREADS] &#91;--timeout TIMEOUT] &#91;--jitter INTERVAL] &#91;--no-progress] &#91;--verbose] &#91;--debug] &#91;--version] {smb,ssh,ldap,ftp,wmi,winrm,rdp,vnc,mssql,nfs} ...
&lt;-- Banner -->
options:
-h, --help show this help message and exit
-t THREADS set how many concurrent threads to use (default: 100)
--timeout TIMEOUT max timeout in seconds of each thread (default: None)
--jitter INTERVAL sets a random delay between each connection (default: None)
--no-progress Not displaying progress bar during scan
--verbose enable verbose output
--debug enable debug level information
--version Display nxc version
protocols:
available protocols
{smb,ssh,ldap,ftp,wmi,winrm,rdp,vnc,mssql,nfs}
smb own stuff using SMB
ssh own stuff using SSH
ldap own stuff using LDAP
ftp own stuff using FTP
wmi own stuff using WMI
winrm own stuff using WINRM
rdp own stuff using RDP
vnc own stuff using VNC
mssql own stuff using MSSQL
nfs own stuff using NFS

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26 | #~ nxc --help  usage: nxc &#91;-h] &#91;-t THREADS] &#91;--timeout TIMEOUT] &#91;--jitter INTERVAL] &#91;--no-progress] &#91;--verbose] &#91;--debug] &#91;--version] {smb,ssh,ldap,ftp,wmi,winrm,rdp,vnc,mssql,nfs} ...    &lt;-- Banner -->  options:  -h, --help            show this help message and exit  -t THREADS            set how many concurrent threads to use (default: 100)  --timeout TIMEOUT     max timeout in seconds of each thread (default: None)  --jitter INTERVAL     sets a random delay between each connection (default: None)  --no-progress         Not displaying progress bar during scan  --verbose             enable verbose output  --debug               enable debug level information  --version             Display nxc version  protocols:  available protocols  {smb,ssh,ldap,ftp,wmi,winrm,rdp,vnc,mssql,nfs}  smb                 own stuff using SMB  ssh                 own stuff using SSH  ldap                own stuff using LDAP  ftp                 own stuff using FTP  wmi                 own stuff using WMI  winrm               own stuff using WINRM  rdp                 own stuff using RDP  vnc                 own stuff using VNC  mssql               own stuff using MSSQL  nfs                 own stuff using NFS |

The per-protocol help is available via `nxc <protocol> --help` and provides protocol-specific flags and options. Refer to the project’s documentation pages for per-protocol examples and recommended opsec settings.

## Practical attack scenario

Context: You hold credentials for a low-privileged domain user and want to verify lateral movement windows in a segmented AD environment.

Scenario (single realistic chain): Use NetExec’s LDAP module to enumerate domain users and groups, identify service accounts with delegated privileges, then use the WinRM or SMB modules to attempt command execution where delegation or weak service configuration exists. A practical sequence would be:

* Run `nxc ldap --domain-domain.example --user alice --pass 'password'` to collect users and group membership.
* Identify hosts where service accounts have local admin rights from the LDAP output.
* Use `nxc winrm` or `nxc smb` with the discovered service account credentials to execute a payload or scheduled task to test privilege escalation and persistence.

These steps mirror standard red-team lateral-movement workflows and demonstrate how NetExec can be used to validate detection coverage and escalation pathways. Operators must always obtain written authorization before running tests in production environments, unless explicitly permitted.

## Red team relevance and trade-offs

NetExec is relevant to red teams because it consolidates protocol modules into a single, scriptable CLI and supports high concurrency for rapid assessment. For adversary emulation and purple-team validation, this is an efficient way to exercise multiple attack paths from a single host. Trade-offs include opsec and detectability: aggressive threading and default payloads will trigger endpoint detection and intrusion prevention systems, so tune `-t`, `--timeout` and `--jitter` to match the target environment. Log and alert noise is likely if you run unthrottled scans.

## Detection and hunting guidance for defenders

Defenders should treat multi-protocol, rapid multi-host activity as a high-fidelity indicator of lateral movement. Key telemetry to collect and monitor includes:

* Unusually high-rate SMB or WinRM activit...