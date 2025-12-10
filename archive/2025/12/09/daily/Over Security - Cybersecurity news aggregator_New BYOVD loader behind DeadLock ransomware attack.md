---
title: New BYOVD loader behind DeadLock ransomware attack
url: https://blog.talosintelligence.com/byovd-loader-deadlock-ransomware/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-09
fetch_date: 2025-12-10T03:22:50.797952
---

# New BYOVD loader behind DeadLock ransomware attack

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2025/12/DeadLock.jpg)

# New BYOVD loader behind DeadLock ransomware attack

By
[Jordyn Dunk](https://blog.talosintelligence.com/author/jordyn/),
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Tuesday, December 9, 2025 06:00

[Threat Spotlight](/category/threat-spotlight/)
[ransomware](/category/ransomware/)

* While tracking ransomware activities, Cisco Talos uncovered new tactics, techniques, and procedures (TTPs) linked to a financially motivated threat actor targeting victims with DeadLock ransomware.
* The actor used the Bring Your Own Vulnerable Driver (BYOVD) technique with a previously unknown loader to exploit the Baidu Antivirus driver vulnerability ([CVE-2024-51324](https://nvd.nist.gov/vuln/detail/CVE-2024-51324)), enabling the termination of endpoint detection and response (EDR) processes.
* The actor ran a PowerShell script that bypasses User Account Control (UAC), disables Windows Defender, terminates various security, backup, and database services, and deletes all volume shadow copies to prevent system recovery.
* The DeadLock ransomware targets Windows machines with a custom stream cipher encryption algorithm that uses time-based cryptographic keys to encrypt files.
* This custom encryption method allows DeadLock ransomware to effectively encrypt different file types in enterprise environments while preventing system corruption through selective targeting and anti-forensics techniques, which complicate recovery.

## Disabling EDR services via BYOVD technique

[T1211 – Exploitation for defense evasion](https://attack.mitre.org/techniques/T1211/)

Talos observed a threat actor leveraging a BYOVD technique to disable endpoint detection and escalate privileges in an attack that eventually delivered DeadLock ransomware as the payload.

The attack relied on “BdApiUtil.sys”, a legitimate Baidu Antivirus driver containing an Improper Privilege Management vulnerability with [CVE-2024-51324](https://nvd.nist.gov/vuln/detail/CVE-2024-51324)—which the actor disguised using the file name “DriverGay.sys”. This Improper Privilege Management vulnerability exposes a critical function in the driver program that allows unprivileged users to terminate any process on the system at the kernel level.

The attack began when the actor dropped the loader (using the file name “EDRGay.exe”) and the vulnerable driver into the victim's Videos folder and ran the loader. The loader, running in user mode, initializes the driver and establishes a connection via the `CreateFile()` Windows API. It specifies the driver's real device name (“\\.\BdApiUtil”) to obtain a handle which essentially acts as a "ticket" to authorize future communication between the loader and the driver.

Once connected, the loader enumerates running system processes to identify the process ID (PID) of the target antivirus or EDR solution. To trigger the exploit, it calls the `DeviceIOControl()` function, passing the target PID along with the specific I/O Control Code (IOCTL) 0x800024b4.

This 32-bit IOCTL value is structured to instruct the driver exactly how to operate:

* Device Type: 0x8000
* Access: 0x0 (FILE\_ANY\_ACCESS)
* Method: 0x0 (METHOD\_BUFFERED)
* Function Code: 0x92D

![](https://blog.talosintelligence.com/content/images/2025/12/image10.png)

Figure 1. Function snippet of the loader, EDRGay, loading the driver and sending the IOCTL command.

Upon receiving the request, the driver decodes the function code 0x92D as a "terminate process" command. Due to the CVE-2024-51324 vulnerability, the driver fails to validate if the user-mode program has the necessary permissions to make this request. Because the driver operates in kernel mode with the highest system privileges, it blindly accepts the command and executes `ZwTerminateProcess()`, instantly killing the targeted security service.

![](https://blog.talosintelligence.com/content/images/2025/12/image11.png)

Figure 2. Function snippets of vulnerable drivers for terminating the targeted processes.

## PowerShell script for inhibiting system recovery

[T1548.002 - Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)

[T1490 – Inhibit system recovery](https://attack.mitre.org/techniques/T1490/)

Talos observed that the threat actor executed a PowerShell script in the victim’s machine before the encryption process. The PowerShell script is a pre-encryption preparation component of the attack that the actor used to bypass the UAC, disable the detection services, and inhibit the system recovery of the victim machine.

The script implements aprivilege escalation mechanism through the `Test-Admin` function that automatically detects current user permissions and re-launches itself with administrative privileges using the Verb `RunAs` parameter, ensuring it operates with the necessary system-level access required for service manipulation and shadow copy deletion. This elevation technique bypasses UAC prompts through the `exec bypass` execution policy override, allowing the script to execute without standard PowerShell security restrictions.

![](https://blog.talosintelligence.com/content/images/2025/12/image.png)

Figure 3. Snippet of the PowerShell script escalating the privilege.

The main functionality of the script centers around service termination, designed to disable security software, backup systems, and database applications that could affect the ransomware encryption process. It includes an extensive exclusion list of Windows services that must remain operational to maintain basic functionality of the system for ransom payment discussions and processing, including core networking services (Winrm, Dns, Dhcp), authentication mechanisms (Kdc, Netlogon, Lsm), and essential system components (Rpcss, Plugplay, Eventlog).

The script targets the running services ou...