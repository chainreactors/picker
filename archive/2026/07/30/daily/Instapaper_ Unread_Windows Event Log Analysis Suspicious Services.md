---
title: Windows Event Log Analysis Suspicious Services
url: https://digitalinvestigator.blogspot.com/2026/07/windows-event-log-analysis-suspicious.html
source: Instapaper: Unread
date: 2026-07-30
fetch_date: 2026-07-31T05:31:22.336485
---

# Windows Event Log Analysis Suspicious Services

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Windows Event Log Analysis: Suspicious Services

Joseph Moronwi
July 29, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj__PnhFc2eUuoTE7AyIfXW8TUL9Oye7jd8FTkwq_hIcTzpEFHi-VqQ05ZRmpoleKwe25aRatsz_K93VN25f3D0C7v6Mf6bdjQ_pKLt2IlLEGziqkkqmwhKBRovBEKAKFdRyt89A94RdxPJVGL_ijbr7fIpuPTLwo7R2U-hYNtIpwN7f_RgpE4UyxuciW0/w647-h339/microsoft-windows-endpoint-forensics-readiness-booster_hu_c37ffd2549a20ad9.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj__PnhFc2eUuoTE7AyIfXW8TUL9Oye7jd8FTkwq_hIcTzpEFHi-VqQ05ZRmpoleKwe25aRatsz_K93VN25f3D0C7v6Mf6bdjQ_pKLt2IlLEGziqkkqmwhKBRovBEKAKFdRyt89A94RdxPJVGL_ijbr7fIpuPTLwo7R2U-hYNtIpwN7f_RgpE4UyxuciW0/s768/microsoft-windows-endpoint-forensics-readiness-booster_hu_c37ffd2549a20ad9.webp)

Windows Services constitute a near-ubiquitous control surface within the operating system's process architecture. A service is a privileged process capable of executing independently of any interactive user session and irrespective of logon state. Because of their elevated privileges, persistence potential across reboots, and ability to run in the context of SYSTEM or other high-integrity accounts, services represent a high-value target for adversaries seeking durable execution, defense evasion, or lateral movement. Consequently, service-related artifacts frequently yield high-fidelity indicators of compromise during incident response and forensic examination.

Service-related telemetry resides exclusively within the System event log under the Service Control Manager (SCM) provider. The SCM is responsible for transmitting control codes to services and drivers, maintaining their runtime status, and committing the corresponding telemetry to the System log. Within this corpus, the following Event IDs are of primary investigative utility:

* **Event ID 7034** — Unexpected service termination (crash). The event records that a service process exited abnormally and enumerates the cumulative failure count. While legitimate causes (resource exhaustion, driver instability, orderly shutdown races) exist, anomalous or repeated 7034 events—particularly when correlated with injection-based tradecraft (process-injection techniques or DLL side-loading)—warrant prioritized scrutiny.
* **Event ID 7035** — Successful transmission of a start or stop control by the SCM. On legacy platforms (Windows XP / Server 2003), this event frequently populated the User field with the initiating principal; on modern Windows, the user context is inconsistently present, and informational events may be suppressed by policy or log configuration.
* **Event ID 7036** — Confirmed state transition (service entered the running or stopped state). This event is the authoritative indicator that the control issued in 7035 was acted upon. Correlative analysis of 7035/7036 pairs establishes both intent and outcome.
* **Event ID 7040** — Modification of a service’s start type. The event documents the transition among the canonical start types: Boot, System, Automatic (including Automatic Delayed Start), Manual (Demand / “On Request”), and Disabled. Changes that elevate a service to Boot or System start, or that disable security-relevant services, constitute classic persistence and defense-evasion techniques. Coverage is reliable for native Windows services and most third-party services that register with the SCM; certain specialized or non-SCM-managed components may not generate 7040 telemetry.
* **Event ID 7045** — Beginning with Windows Vista / Server 2008 (commonly observed from Windows 7 / Server 2008 R2 onward in enterprise baselines), Event ID 7045 was introduced in the System log to record the installation of a new service. Because service installation is comparatively rare relative to routine start/stop activity, 7045 exhibits a high signal-to-noise ratio and is an excellent starting point when hunting for suspicious services. Tools that create ephemeral services and subsequently delete them (e.g., PsExec and functional equivalents) still generate a distinct 7045 on each installation cycle, providing an opportunistic detection opportunity for transient malicious services.
* **Event ID 4697** — This appears in the Security log and is generated only when the “Audit Security System Extension” advanced audit policy subcategory is enabled for Success. It is the Security log counterpart to System Event 7045 and therefore facilitates correlation with other Security log events. However, the Subject field frequently resolves to SYSTEM (or the machine account) rather than the interactive or remote principal that actually initiated the installation; correlation with the corresponding 7045 and surrounding logon events is, therefore, required to recover actor context. Service Start Type is recorded numerically in registry-compatible form (0 = Boot, 1 = System, 2 = Automatic, 3 = Manual/Demand, 4 = Disabled).

On Windows XP / Server 2003 the classic runtime and control events (7034, 7035, 7036, 7040) were already present; the nearest equivalent for service installation was Event ID 601. Modern investigations should therefore prioritize the 7045/4697 pair on Vista and later platforms while retaining the classic quartet for legacy systems and for ongoing lifecycle analysis. Collectively, these events—examined in temporal correlation with binary path, service account, parent process, and surrounding logon or process-creation artifacts—form a core analytical set for detecting and attributing malicious service activity.

## Suspicious Services: PsExec

The Sysinternals PsExec utility furnishes a canonical illustration of how newly installed services can surface otherwise stealthy remote execution. Each invocation of the authentic Microsoft binary registers a transient service (default name PSEXESVC) with the Service Control Manager, thereby generating System Event ID 7045 by default and, when the “Audit Security System Extension” subcategory is enabled, Security Event ID 4697. Because legitimate services are engineered for non-interactive, background operation, they are almost invariably configured to run under built-in accounts such as NT AUTHORITY\SYSTEM or NT AUTHORITY\LOCAL SERVICE. Consequently, the appearance of a domain-user or interactive-user SID (e.g., S-1-5-21-572887454-1858499753-1978773125-1003) in the service account field is anomalous and merits immediate investigation; such misconfigurations frequently expose high-value credentials or signal adversary activity.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-6wP-CikaoNms8iZ7FTUUwC-Ij-U4IL3Whyphenhyphenv_vI3zydc7LCiUg-xlo8AYgVnZr2ivM_P1DOMMsahfL9F_F3O6FXeiAQ4SHchZTqS3TOH-jW11uqHsXlfyxUJZFGH_KH12FMIlZ1fAg-oHhiBSaTTgGlhuSnh-cJf-d6Nkmk5iYedc16t98j1sREKBIHo/w657-h295/1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-6wP-CikaoNms8iZ7FTUUwC-Ij-U4IL3Whyphenhyphenv_vI3zydc7LCiUg-xlo8AYgVnZr2ivM_P1DOMMsahfL9F_F3O6FXeiAQ4SHchZTqS3TOH-jW11uqHsXlfyxUJZFGH_KH12FMIlZ1fAg-oHhiBSaTTgGlhuSnh-cJf-d6Nkmk5iYedc16t98j1sREKBIHo/s1156/1.png)

In the figure above, two discrete PsExec sessions oc...