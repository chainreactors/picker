---
title: WerReportCreate API
url: https://www.hexacorn.com/blog/2026/04/16/werreportcreate-api/
source: Hexacorn
date: 2026-04-16
fetch_date: 2026-04-17T04:49:40.223856
---

# WerReportCreate API

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2026/02/26/shimbad-the-sailor-part-3/)

# WerReportCreate API

Posted on [2026-04-16](https://www.hexacorn.com/blog/2026/04/16/werreportcreate-api/ "11:19 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The API I want to talk about today is called [WerReportCreate](https://learn.microsoft.com/en-us/windows/win32/api/werapi/nf-werapi-werreportcreate). It takes a few arguments, but the most interesting is the first one, which is the Event Name.

Looking at Windows OS binaries, we can see this API being utilized by a number of native executables and libraries, and each invocation uses unique string for the event name:

* FaultTolerantHeap – AcLayers.dll
* AppxDeploymentFailureBlue – AppXDeploymentServer.dll
* CertPinning – cryptui.dll
* D3DDRED2 – D3D12Core.dll
* DMRCDeviceMetadataPackageFailure – DeviceMetadataRetrievalClient.dll
* DispBrokerTimeoutEvent – DispBroker.dll
* WWAJSE – EdgeContent.dll
* WindowsBlackScreenDiagnosticsV1 – explorer.exe
* ShellBrowserCancel – ExplorerFrame.dll
* ShellViewReentered – ExplorerFrame.dll
* FaultTolerantHeap – fthsvc.dll
* GDIObjectLeak – gdi32full.dll
* CompatEntityAnalysis\_1 – invagent.dll
* ScriptedDiagFailure – msdt.exe
* WindowsNonFatalSuspectedDeadlock – netprofmsvc.dll
* CommsNonFatalSuspectedDeadlock – PhoneProviders.dll
* CommsNonFatalSuspectedDeadlock – PhoneService.dll
* HamLkd – PsmServiceExtHost.dll
* RADAR\_PRE\_LEAK\_32 – radarrs.dll
* RADAR\_LEAK\_64 – rdrleakdiag.exe
* MemDiagV1 – RelPost.exe
* StartupRepairOnline – RelPost.exe
* WindowsBackupFailure – sdclt.exe
* WindowsBackupFailure – sdengin2.dll
* ServiceHang – services.exe
* SystemRestore – srcore.dll
* ShellThumbnailExtractionTimeout – thumbcache.dll
* ShellThumbnailExtractionTimeout – ThumbnailExtractionHost.exe
* UpdateAgentDiag – UpdateAgent.dll
* Windows Server Backup Error – wbengine.exe
* AppHangB1 – WerFault.exe
* BlueScreen – WerFault.exe
* LiveKernelEvent – WerFault.exe
* Temp – werui.dll
* WUDFUnhandledException – WUDFPlatform.dll

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/04/16/werreportcreate-api/ "Permalink to WerReportCreate API").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")