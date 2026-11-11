---
title: Cheatsheet: Windows Forensics Analysis
url: https://fareedfauzi.github.io/2023/12/22/Windows-Forensics.html
source: Over Security
date: 2026-11-10
fetch_date: 2026-11-11T08:35:24.190643
---

# Cheatsheet: Windows Forensics Analysis

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Archive](/archive.html)
* [About](/about.html)

# Cheatsheet: Windows Forensics Analysis

* [DFIR](/archive.html?tag=DFIR)

* Dec 22, 2023

During a Windows Forensics engagement, I occasionally find myself forgetting essential tasks or unintentionally skipping analyzing importants artifacts. Therefore, this checklist (along with cheatsheet) could help myself (or readers) and ensure that I adhere to a systematic workflow when conducting Windows Forensics.

# Typical Forensic investigation flow

![image](https://github.com/fareedfauzi/fareedfauzi.github.io/assets/56353946/fd7dcfc9-f006-4343-895d-ad8d272382ab)

If you ask me the details on the acquisition and analysis part, here it is:

1. Evidence acquisition ⇛ Disk, memory
2. Live response, scanner and live forensics ⇛ Autoruns, process hacker, THOR or Loki, Inquisitor
3. Memory forensics ⇛ MemProcFS, volatility
4. Disk Image mounting ⇛ Mounting and Triage important artifact
5. Persistence analysis ⇛ Autoruns location, registry, WMI, Scheduled Tasks
6. Malware analysis ⇛ Static and Dynamic analysis
7. Checking system information ⇛ Registry
8. Root cause analysis ⇛ Logs, web, malware, file folder activity, exploit, email, executed file
9. Lateral movement investigation ⇛ event log, executed file, registry, file system
10. Timeline analysis ⇛ MFT, Logfile, UsnJ parsing
11. File access artifacts ⇛ File sharing, MountPoints, USB
12. Recovering deleted data ⇛ Recyclebin, MFT, VSS, File carving, Keyword search (Autopsy)
13. Malware reverse engineering
14. Writing report

# Tools

## Acquire artifact’s Tools

| Tools | Description |
| --- | --- |
| FTK Imager | Disk Imaging |
| Magnet RAM Capturer | Generate memory dump |
| KAPE | Triage only selected important artifacts instead of the whole disk image |
| Inquisitor / FastIR | Live analysis triage |
| Mandiant Redline | Collect live and file’s data and produce analysis |
| External Hard disk | To store the artifact acquisition |
| Velociraptor’s agent and server | Remote forensics framework |
| EDD | Check disk encryption |

## Forensic analysis tools

| Tools | Description |
| --- | --- |
| Arsenal Image Mounter | Mounting image |
| Autopsy / FTK Imager | Disk forensics |
| KAPE | Triage artifact and parse artifact |
| Eric Zimmerman tools | Artifact parser and viewer |
| Regripper | Registry parser |
| Volatility Workbench / MemProcFS / MemProcFS-Analyzer | Memory analysis tools |
| Event log explorer | Event log viewer |
| Reg\_hunter | Hunt for malicious registry in live forensics |
| Other open/close source tools | - |

## OS / Linux Distros

1. Windows
2. SIFT Linux
3. Tsurugi Linux
4. REMnux

# Acquire artifacts

1. Check disk encryption using EDD
2. Perform disk imaging using FTK Imager
3. Perform memory dump activity using Magnet RAM Capturer for example.
4. Save all files in the external harddisk
5. Optional:
   * Perform live analysis collection scanner such as Inquisitor
   * Scan the compromised using scanner such as THOR
   * Perform Registry scanner such as RegHunter
   * Perform memory scanner such as hollows\_hunter or moneta
   * Perform persistent scanner such as PersistenceSniper or Trawler

# KAPE cheatsheet

Basic command

```
# Target
.\kape.exe --tsource [DRIVE LETTER] --tdest [DESTINATION INCLUDE FOLDER NAME] --module [MODULE NAME] --gui
# Module
.\kape.exe --msource [DRIVE LETTER] --mdest [DESTINATION INCLUDE FOLDER NAME] --module [MODULE NAME] --gui
```

## Target

### KAPE target extraction

```
.\kape.exe --tsource E: --tdest D:\KAPE_cases\ --target KapeTriage,MessagingClients,RemoteAdmin,ServerTriage,WebBrowsers,WebServers,WSL,MemoryFiles --gui
```

## Module: Live Response

### Memory dump

```
.\kape.exe --msource C:\ --mdest D:\KAPE_cases\%m --module MagnetForensics_RAMCapture --gui
```

### Live response command and scanner

```
.\kape.exe --msource E:\ --mdest D:\KAPE_cases\%m --module PowerShell_Get-InjectedThread,PowerShell_Get-NetworkConnection,PowerShell_Netscan,PowerShell_Signed,SIDR_WindowsIndexSearchParser,WIFIPassView,MagnetForensics_EDD,Nirsoft_BluetoothView,Nirsoft_LastActivityView,Nirsoft_OpenedFilesView,NirSoft_USBDeview,NirSoft_VideoCacheView,NirSoft_WebBrowserPassView,Nirsoft_WhatInStartup,Nirsoft_WifiHistoryView,Nirsoft_WirelessKeyView,SysInternals_Autoruns,SysInternals_Handle,SysInternals_PsFile,SysInternals_PsInfo,SysInternals_PsList,SysInternals_PsLoggedOn,SysInternals_PsService,SysInternals_PsTree,SysInternals_Tcpvcon,Powrshell_LiveResponse_SystemInfo,PowerShell_Arp_Cache_Extraction,PowerShell_Bitlocker_Key_Extraction,PowerShell_Bitlocker_Status,PowerShell_Defender_Exclusions,PowerShell_DLL_List,PowerShell_Dns_Cache,PowerShell_Local_Group_List,PowerShell_LocalAdmin,PowerShell_NamedPipes,PowerShell_NetUserAdministrators,PowerShell_Network_Configuration,PowerShell_Network_Connections_Status,PowerShell_Network_Share,PowerShell_Process_Cmdline,PowerShell_ProcessList_CimInstance,PowerShell_ProcessList_WMI,PowerShell_Services_List,PowerShell_SMBMapping,PowerShell_SMBOpenFile,PowerShell_SMBSession,PowerShell_Startup_Commands,PowerShell_User_List,PowerShell_WMIRepositoryAuditing,Windows_ARPCache,Windows_DNSCache,Windows_GpResult,Windows_IPConfig,Windows_MsInfo,Windows_nbtstat_NetBIOSCache,Windows_nbtstat_NetBIOSSessions,Windows_Net_Accounts,Windows_Net_File,Windows_Net_LocalGroup,Windows_Net_Session,Windows_Net_Share,Windows_Net_Start,Windows_Net_Use,Windows_Net_User,Windows_netsh_portproxy,Windows_NetStat,Windows_qwinsta_RDPSessions,Windows_RoutingTable,Windows_schtasks,Windows_SystemInfo,Reghunter,hasherezade_HollowsHunter --gui

.\kape.exe --msource E:\ --mdest D:\KAPE_cases\%m --module Thor-Lite_Upgrade,Thor-Lite_Scan --gui

.\kape.exe --msource E:\ --mdest D:\KAPE_cases\%m --module Loki_LiveResponse --gui

.\kape.exe --msource E:\ --mdest D:\KAPE_cases\%m --module hasherezade_HollowsHunter --gui

.\kape.exe --msource E:\ --mdest D:\KAPE_cases\%m --module MagnetForensics_RAMCapture --gui
```

## Module: Parsing and scanning

### All in one artifact parsing

Warning: Super slow!

```
.\kape.exe --msource E:\ --mdest D:\KAPE_cases\ --module Loki_Scan,DensityScout,BackstageParser,BitsParser,CCMRUAFinder_RecentlyUsedApps,Chainsaw,DeepblueCLI,DHParser,EvtxHussar,hasherezade_HollowsHunter,INDXRipper,LevelDBDumper,OneDriveExplorer,PowerShell_Get-ChainsawSigmaRules,TeamsParser,ThumbCacheViewer,WMI-Parser,Zircolite_Scan,Zircolite_Update,LogParser_ApacheAccessLogs,LogParser_DetailedNetworkShareAccess,LogParser_LogonLogoffEvents,LogParser_RDPUsageEvents,LogParser_SMBServerAnonymousLogons,Nirsoft_AlternateStreamView,NirSoft_BrowsingHistoryView,NirSoft_FullEventLogView_AllEventLogs,NirSoft_FullEventLogView_Application,NirSoft_FullEventLogView_PowerShell-Operational,NirSoft_FullEventLogView_PrintService-Operational,NirSoft_FullEventLogView_ScheduledTasks,NirSoft_FullEventLogView_Security,NirSoft_FullEventLogView_System,NirSoft_TurnedOnTimesView,NirSoft_WebBrowserDownloads,Nirsoft_WinLogonView,SysInternals_SigCheck,TZWorks_CAFAE_Registry_System,Events-Ripper,Hayabusa,LogParser,MFTECmd,NTFSLogTracker,RECmd_AllBatchFiles,Reghunter,RegRipper,AmcacheParser,AppCompatCacheParser,EvtxECmd,EvtxECmd_RDP,iisGeoLocate,JLECmd,LECmd,PECmd,RBCmd,RecentFileCacheParser,SBECmd,SQLECmd,SQLECmd_Hunt,SrumECmd,SumECmd,WxTCmd,Sync_EvtxECmd,Sync_KAPE,Sync_RECmd,Sync_SQLECmd,Windows_ManageBDE_BitLockerKeys,Windows_ManageBDE_BitLockerStatus --gui
```

### Event log / log scanning and parsing

```
.\kape.exe --msource E:\ --mdest D:\KAPE_cases\ --module !!ToolSync,PowerShell_Get-ChainsawSigmaRule,Chainsaw,DeepblueCLI,EvtxHussar,Zircolite_Update,Zircolite_Scan,Events-Ripper,hayabusa_EventStatistics,hayabusa_OfflineEventLogs,hayabusa_OfflineLogonSummary,hayabusa_UpdateRules,EvtxECmd,EvtxECmd_RDP,LogParser,iisGeoLocate
```

### Program Execution

```
.\kape.exe --msource E:\ --mdest D:\KAPE_cases\ --module CCMRUAFinder_RecentlyUsedA...