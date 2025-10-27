---
title: List of clean mutexes and mutants
url: https://www.hexacorn.com/blog/2023/03/12/list-of-clean-mutexes-and-mutants/
source: Hexacorn
date: 2023-03-13
fetch_date: 2025-10-04T09:25:04.773093
---

# List of clean mutexes and mutants

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

[← Previous](https://www.hexacorn.com/blog/2023/03/10/threat-hunting-localization-issues/)
[Next →](https://www.hexacorn.com/blog/2023/03/28/converting-questionable-questions-into-unquestionable-opportunities/)

# List of clean mutexes and mutants

Posted on [2023-03-12](https://www.hexacorn.com/blog/2023/03/12/list-of-clean-mutexes-and-mutants/ "12:03 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

A few years ago I [released](https://www.hexacorn.com/blog/2014/12/23/santas-bag-full-of-mutants/) a list of ‘bad’ mutexes/mutants. That list was generated from my [malware sandbox reports](https://www.hexacorn.com/blog/2019/07/17/logs-from-1-6m-sandboxed-samples-release/).

I thought that it may be good to revisit the idea, but this time with a focus on a ‘clean’ list.

What do I mean by that?

Windows native binaries reference many ‘clean’ mutexes and mutants. By looking for references to CreateMutex\* and OpenMutex API invocations inside the native OS applications and DLLs we can build a list presented below.

I hope you will agree that amongst all the items presented, the *x9pv45dxghk* mutex looks the most suspicious, as if malware just hit your system, but … it’s actually not a bad guy! Also, some of these mutexes you will probably never see in your logs f.ex. anything [RAS](https://learn.microsoft.com/en-us/windows/win32/rras/about-remote-access-service)-related is kinda dead, because dialers are long gone (of course, RAS is a bit wider in scope, but you know what I mean). But then some of them may actually still be helpful in detecting interesting OS events f.ex. everything with a ‘RDP’ in name. There are also some eye-catching mutexes that may be worth further exploration, f.ex. *Global\SignedDriversMutex* is created before *driverquery.exe* runs a WQL query “*select \* from Win32\_PnpSignedDriver where DeviceName != NULL*“. Why that mutex is needed there? Hmm…

Let’s remember that mutexes often guard program’s important business logic. By understanding why these mutexes are created we may affect some of this logic and take over the program’s narrative. For example, the *WerMgr.exe* uses *Global\WerMgrUploadingLock* mutex to ensure only one instance of *WerMgr.exe* is uploading Windows Error Reports (for wemgr.exe options –*upload* and –*uploadforce*). It’s not very useful per se, but it makes the point.

Here’s the list I collected:

**2F8FA37B-8158-476F-9B22-3283D2A6FEC2**

* Windows\System32\phoneactivate.exe

**5615046C-3289-4BC3-A5C7-0E9B0FE4C2DA**

* Windows\System32\CourtesyEngine.dll

**ACTIONDIALOG\_MUTEX**

* Windows\System32\WindowsActionDialog.exe

**AD8DA490-28A3-4dfd-96BA-37453388BAEF**

* Program Files (x86)\Windows Photo Viewer\PhotoAcq.dll
* Program Files\Windows Photo Viewer\PhotoAcq.dll

**AMResourceMutex3**

* Windows\SysWOW64\quartz.dll
* Windows\System32\quartz.dll

**AccessibilitySoundAgentRunning**

* Windows\SysWOW64\PlaySndSrv.dll
* Windows\SysWOW64\sethc.exe
* Windows\System32\PlaySndSrv.dll
* Windows\System32\sethc.exe

**AppIDSvc\CertStore**

* Windows\System32\appidcertstorecheck.exe

**AppIDSvc\PolicyMutex**

* Windows\System32\appidpolicyconverter.exe

**AssignedAccessCspDataStore{2DB91A08-F99F-4E50-A831-6D917523A264}**

* Windows\System32\AssignedAccessCsp.dll

**AuthHostAppContainerMutex.SSO**

* Windows\SysWOW64\AuthBroker.dll
* Windows\System32\AuthBroker.dll

**AutoTune**

* Windows\SysWOW64\psisdecd.dll
* Windows\System32\psisdecd.dll

**BDATIF\_Mutex**

* Windows\SysWOW64\psisdecd.dll
* Windows\System32\psisdecd.dll

**BFFF9080-1DAE-43B1-96B6-738575D01524**

* Program Files (x86)\Common Files\Microsoft Shared\ink\mshwLatin.dll
* Program Files\Common Files\microsoft shared\ink\InputPersonalization.exe
* Program Files\Common Files\microsoft shared\ink\mshwLatin.dll
* Windows\System32\msTextPrediction.dll

**CB35EF5D-4591-41d9-BBA2-0363342F3783**

* Windows\System32\cscsvc.dll

**CSM Policy Key Mutex**

* Windows\SysWOW64\SearchIndexer.exe
* Windows\SysWOW64\srchadmin.dll
* Windows\System32\SearchIndexer.exe
* Windows\System32\srchadmin.dll

**CWpcTridentWebFilter::Initialize**

* Windows\SysWOW64\WpcWebFilter.dll
* Windows\System32\WpcWebFilter.dll

**ClearTypeTunerWizardMutex**

* Windows\SysWOW64\cttune.exe
* Windows\System32\cttune.exe

**CloudNotifications**

* Windows\SysWOW64\CloudNotifications.exe
* Windows\System32\CloudNotifications.exe

**Connection Manager Phonebook Access**

* Windows\SysWOW64\cmdl32.exe
* Windows\System32\cmdl32.exe

**Connection Manager Profile Installer Mutex**

* Windows\SysWOW64\cmstp.exe
* Windows\System32\cmstp.exe

**CredPicker.Mutex\_CAED75DD\_5855\_49C7\_A2FD\_4CC470A3575E**

* Windows\System32\Windows.Security.Credentials.UI.CredentialPicker.dll

**DBWinMutex**

* Windows\SysWOW64\KernelBase.dll
* Windows\System32\KernelBase.dll

**DSKQUOTA\_SIDCACHE\_MUTEX**

* Windows\SysWOW64\dskquota.dll
* Windows\System32\dskquota.dll

**DirectMusiCPcClockMutex**

* Windows\SysWOW64\dmusic.dll
* Windows\System32\dmusic.dll

**DirectMusicMasterClockMutex**

* Windows\SysWOW64\dmusic.dll
* Windows\System32\dmusic.dll

**DiskSnapshot-Mutex**

* Windows\System32\DiskSnapshot.exe

**DrvInst.exe\_mutex\_{5B10AC83-4F13-4fde-8C0B-B85681BA8D73}**

* Windows\System32\drvinst.exe
* Windows\System32\pnppolicy.dll

**EUPPSYNCLOCK**

* Windows\SysWOW64\msfeeds.dll
* Windows\System32\msfeeds.dll

**EduPrintProvSingleInstance**

* Windows\System32\EduPrintProv.exe

**EnterpriseIDMutex-61982412-20ce-4a9a-b974-55c3ce44b9b0**

* Windows\SysWOW64\efswrt.dll
* Windows\System32\efswrt.dll

**FinishInstallOperation\_mutex\_{13f20490-1533-411a-9489-1a6da95d2b85}**

* Windows\SysWOW64\newdev.dll
* Windows\System32\newdev.dll

**FlightActionManagerConsolidateMutex**

* Windows\SysWOW64\FlightSettings.dll
* Windows\System32\FlightSettings.dll

**GeneratingSchemaGlobalMapping**

* Windows\SysWOW64\propsys.dll
* Windows\System32\propsys.dll

**Global\552FFA80-3393-423d-8671-7BA046BB5906**

* Windows\SysWOW64\sppc.dll
* Windows\System32\sppc.dll
* Windows\System32\sppsvc.exe

**Global\AudioResourceAcquisitionMutex**

* Windows\System32\audioresourceregistrar.dll
* Windows\System32\audiosrv.dll

**Global\CDNDownloadMutex**

* Windows\SysWOW64\dmenrollengine.dll
* Windows\System32\DeviceEnroller.exe

**Global\ComPortNumberDatabaseMutexObject**

* Windows\SysWOW64\msports.dll
* Windows\System32\msports.dll

**Global\DFXLIB\_STORE\_MUTEX**

* Windows\SysWOW64\difxapi.dll
* Windows\System32\difxapi.dll

**Global\DVD\_Region\_Cntry\_List\_Mutex**

* Windows\SysWOW64\Storprop.dll

**Global\DeclaredConfigurationMutex**

* Windows\SysWOW64\dmenrollengine.dll
* Windows\System32\omadmclient.exe

**Global\DeviceManagementContainerMutex**

* Windows\SysWOW64\dmcmnutils.dll
* Windows\System32\dmcmnutils.dll

**Global\F659A567-8ACB-4E4A-92A7-5C2DD1884F72**

* Windows\SysWOW64\RacEngn.dll
* Windows\System32\RacEngn.dll

**Global\FillWindowsUpdatePrinterCatalog**

* Windows\SysWOW64\ntprint.dll
* Windows\System32\ntprint.dll

**Global\FindNetPrinters{60E245A9-955D-421b-985C-A48F7CBF0476}**

* Windows\SysWOW64\findnetprinters.dll
* Windows\System32\findnetprinters.dll

**Global\Fve-AAD-Mutex**

* Windows\System32\fveskybackup.dll

**Global\LicenseUI**

* Windows\System32\LicensingUI.exe

**Global\Lpksetup-TempFolderToken**

* Windows\System32\lpksetup.exe

**Global\MS ODBC PerfMon**

* Windows\SysWOW64\odbc32.dll
* Windows\System32\odbc32.dll

**Global\Microsoft.Windows.Setup.Box**

* Windows\System32\UpdateAgent.dll

**Global\Microsoft.Windows.Setup.SetupCln**

* Windows\SysW...