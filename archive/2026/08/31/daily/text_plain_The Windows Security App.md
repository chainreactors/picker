---
title: The Windows Security App
url: https://textslashplain.com/2026/08/31/the-windows-security-app/
source: text/plain
date: 2026-08-31
fetch_date: 2026-09-01T06:59:52.292301
---

# The Windows Security App

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# The Windows Security App

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-312026-08-31](https://textslashplain.com/2026/08/31/the-windows-security-app/)Posted in[security](https://textslashplain.com/category/security/), [tech](https://textslashplain.com/category/tech/)Tags:[Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/), [UI](https://textslashplain.com/tag/ui/), [Windows](https://textslashplain.com/tag/windows/)

Going back as far as the 2004 release of Windows XP SP2, Windows has offered [various GUIs](https://en.wikipedia.org/wiki/Security_and_Maintenance) to help users understand the security state of their PC. In modern Windows 10 and Windows 11, this graphical user interface is called the “[Windows Security Center/App](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/windows-defender-security-center/windows-defender-security-center)“.

The Windows Security App (WSA) is a surface upon which Windows exposes various settings and information, including lightweight status for antivirus and firewall products (including those built by third-parties) and entry points to those products’ user-experiences.

The WSA can be launched via the Start Menu, or by clicking on various toast notifications sent by features within the app.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-65.png?resize=334%2C227&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-65.png?ssl=1)

The default view aims to provide a “single status screen” showing the state of the system’s security components:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-66.png?resize=750%2C724&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-66.png?ssl=1)

This UI provides entry points into configuring [SmartScreen network reputation](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/), [SmartScreen Application Reputation](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/), [Smart App Control](https://textslashplain.com/2026/04/28/smart-app-control/), [controlled folder access](https://textslashplain.com/2024/11/15/defensive-technology-controlled-folder-access/), [ransomware recovery](https://textslashplain.com/2025/11/19/defensive-technology-ransomware-data-recovery/), [exploit protection](https://textslashplain.com/2025/04/01/defensive-technology-exploit-protection/), [Windows Firewall](https://textslashplain.com/2025/03/31/defensive-technology-windows-filtering-platform/#:~:text=features%20in%20Windows.-,Windows%20Firewall,-Most%20prominently%2C%20WFP), and the device’s hardware security features.

## Defender Antivirus

By default, Windows includes Microsoft Defender Antivirus (MDAV) and the “Virus and Threat Protection” section of the WSA shows the state of MDAV, including details about the most recent scan, any previously-allowed threats, and the “Protection history” which outlines any threats previously encountered.

Notably, the WSA is also the *only* client graphical user-interface for Microsoft Defender Antivirus and Microsoft Defender for Endpoint security products: unlike all third-party security products on Windows there is not today a separate Defender app (*except our D4I product; keep reading*).

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-68.png?resize=582%2C483&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-68.png?ssl=1)

The **Quick scan** button allows invoking a quick scan of sensitive system locations (primarily, locations used by malware to establish persistence), while the Scan options link allows invoking other types of scans:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-69.png?resize=750%2C668&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-69.png?ssl=1)

With that said, as outlined previously in my post about [Understanding Defender AV Scans](https://textslashplain.com/2026/04/10/understanding-defender-av-scans/), there is rarely any need to manually kick off an AV Scan.

## Defender for Endpoint

Until recently, the WSA would not show anything special if a device was onboarded to [Microsoft Defender for Endpoint (MDE),](https://textslashplain.com/2024/11/18/security-software-an-overview/#:~:text=Microsoft%20Defender%20for%20Endpoint) the corporate version of Defender that adds numerous additional protection features beyond the free MDAV included with Windows. As I explained last month, it was previously non-trivial to determine whether a PC was [onboarded to Defender for Endpoint’s XDR](https://textslashplain.com/2026/07/22/offboarding-from-microsoft-defender-for-endpoint/) and monitored by a Security Operations Center.

Fortunately, this has recently changed, and the WSA now shows specific information when a device is onboarded, including which MDE features are enabled:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-70.png?resize=750%2C728&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-70.png?ssl=1)

The **Device Details** link in the footer reveals more information, including status and version numbers of the protection components:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-71.png?resize=647%2C714&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-71.png?ssl=1)

## Third Party Antivirus

When a 3rd party security product installs on a client version of Windows, it calls the Windows Security Center API to announce its presence and status. Supported products include **Virus and Threat Protection** products and **Firewall** products. *WSA previously showed a **Web Protection** category intended to indicate the status of any [Edge Legacy](https://textslashplain.com/2020/02/03/microsofts-three-browsers/) browser protection extensions, but this section was removed in a recent update because Edge Legacy was removed years ago.*

Registering a product in the Virus and Threat Protection category directs MDAV to enter “passive mode” (disabling real-time protection and other features), allowing the 3rd party product to be the active protection component of the system. The product in question has short window after each system startup to register with the API: if it fails to do so, or if it indicates that it is not working properly, MDAV resumes operations. The APIs for registering with the Windows Security Center are not fully public, and only callable by members of [the MVI program](https://learn.microsoft.com/en-us/unified-secops/virus-initiative-criteria).

When a 3P security product registers, the UI of the Windows Security Center is updated to show lightweight status information from that product and offer an **Open app** entry point into the 3P product’s (typically) richer user-interface.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-60.png?resize=750%2C586&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-60.png?ssl=1)

Windows Security App behind the 3P Sophos Home application spawned from the “Open app” button.

Multiple 3P products (AV and Firewall) may be installed at one time, although it’s generally recommended to only have one product of each time active to avoid conflicts and performance impact.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-62.png?resize=429%2C550&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-62.png?ssl=1)

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-61.png?resize=750%2C624&ssl=1)](https://i0.wp.com/textslashplain.com/wp-co...