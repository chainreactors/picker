---
title: RunDll Exporters
url: https://www.hexacorn.com/blog/2025/09/19/rundll-exporters/
source: Hexacorn
date: 2025-09-20
fetch_date: 2025-10-02T20:25:54.997844
---

# RunDll Exporters

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

[← Previous](https://www.hexacorn.com/blog/2025/09/19/enter-sandbox-30-static-analysis-gone-wrong/)

# RunDll Exporters

Posted on [2025-09-19](https://www.hexacorn.com/blog/2025/09/19/rundll-exporters/ "11:13 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

One of the most interesting classes of functions that are exported by DLLs are functions that use the RunDll interface (this [archived article](https://web.archive.org/web/20150109234931/http%3A//support.microsoft.com/kb/164787) describes it).

Thanks to traditional (today kinda old-school) programming conventions, many coders name their exported functions compatible with the RunDll interface in a way that makes them easy to identify. Basically, they often include the reference to ‘rundll’ in a function name.

Knowing that, we can make an attempt to comb through many ‘good’ DLLs to discover a list of libraries where some of the APIs they export… follow this simple naming convention. Analysis of my small DLL repo gave me the results shown below.

Looking at these results I can immediately see that some of them are very familiar Windows API names (f.ex. Control\_RunDLL variants), but there are many others that are mostly unknown. And many of libraries that export these functions come from other vendors than Microsoft, the exported APIs have almost no documentation and a minimalistic footprint online – basically, googling some of them brings very limited results.

I have a gut feeling that at least some of them are good lolbin potentials.

```
549  _InfEngUnInstallINFFile_RunDLL@16
485  InfEngUnInstallINFFile_RunDLL
426  RunDLLEntryW
353  RunDll32Interface
252  ShowHidPropPageRunDll32
252  BluetoothUpdateSendToRunDll32
195  DelNodeRunDLL32
167  RunDLL32EP
133  ShowHidPropPageRunDll32W
132  UninstADrvRunDll
114  Rundll_Dial
 62  RunDLLEntry
 62  Control_RunDLL
 60  SHHelpShortcuts_RunDLL
 60  PrintersGetCommand_RunDLL
 60  OpenAs_RunDLL
 58  SRS_InitializeEndpoints_Rundll32
 58  SRS_CleanupEndpoints_Rundll32
 58  SHHelpShortcuts_RunDLLW
 58  SHHelpShortcuts_RunDLLA
 58  PrintersGetCommand_RunDLLW
 58  PrintersGetCommand_RunDLLA
 58  OpenAs_RunDLLW
 58  OpenAs_RunDLLA
 58  Control_RunDLLW
 58  Control_RunDLLA
 54  RunDllDoPreInstall
 54  Control_FillCache_RunDLL
 52  Control_FillCache_RunDLLW
 52  Control_FillCache_RunDLLA
 50  BTINS_RunDll
 46  _RunDLLEntry@16
 41  ShellExec_RunDLLW
 41  ShellExec_RunDLLA
 41  ShellExec_RunDLL
 41  CplRunDll32
 41  Control_RunDLLAsUserW
 40  RunDll
 39  RunDllW
 38  SHCreateLocalServerRunDll
 38  Options_RunDLLW
 38  Options_RunDLLA
 38  Options_RunDLL
 38  AppCompat_RunDLLW
 32  Activate_RunDLL
 30  RunDll32ShimW
 30  HomeNetWizardRunDll
 25  TestRunDll
 24  ctCVWUtilityRunDLL32EP
 24  ctCVWIntroRunDLL32EP
 24  RundllUninstallA
 24  RundllInstallA
 23  ctCVWConsoleRunDLL32EP
 22  ctCVWParentalRunDLL32EP
 22  RunDllPromptForReboot
 20  SetupRunDll32Entry
 20  SelectSetupRunDll32Ex
 20  RunDllRegister
 19  UpgradePrinterRunDll32Ex
 18  RunDLL_InstallOEMDeviceEx
 18  RunDLL_InstallOEMDevice
 17  DelNodeRunDLL32W
 17  DelNodeRunDLL32A
 16  RunDLL_ExtractCabinetFile
 16  RunDLL32_UnregisterApplication
 16  RunDLL32_RegisterApplication
 16  RunDLL32_FilterRunOnceExRegistration
 15  RunDllEntryPoint
 13  SxsRunDllInstallAssemblyW
 13  SxsRunDllInstallAssembly
 12  IID_IShellRunDll
 11  usb_uninstall_service_np_rundll
 11  usb_install_service_np_rundll
 11  usb_install_driver_np_rundll
 11  TestPrint_RunDLLW
 11  RunDLL_InstallMultipleOEMDevicesEx
 11  @Jvjclutils@RunDll32Internal$qqruix17System@AnsiStringt2t2i
 11  @Jvjclutils@RunDLL32$qqrx17System@AnsiStringt1t1oi
 10  usb_touch_inf_file_np_rundll
  9  @Registryscan@TRegistryScan@HandleRundll32$qqr17System@AnsiStringo
  9  @PRunDLLCommand@saveGuts$xqr6RWFile
  9  @PRunDLLCommand@restoreGuts$qr6RWFile
  9  @PRunDLLCommand@newSpecies$xqv
  9  @PRunDLLCommand@myAtom
  9  @PRunDLLCommand@isA$xqv
  9  @PRunDLLCommand@copy$xqv
  9  @PRunDLLCommand@classIsA$qv
  9  @PRunDLLCommand@binaryStoreSize$xqv
  9  @PRunDLLCommand@UnExecute$qv
  9  @PRunDLLCommand@SetThirdParam$qrx9RWCString
  9  @PRunDLLCommand@SetSecondParam$qrx9RWCString
  9  @PRunDLLCommand@SetFunctionType$q12ERunDLLTypes
  9  @PRunDLLCommand@SetFunctionName$qrx9RWCString
  9  @PRunDLLCommand@SetFirstParam$qrx9RWCString
  9  @PRunDLLCommand@SetDLLName$qrx9RWCString
  9  @PRunDLLCommand@GetVersion$xqv
  9  @PRunDLLCommand@GetThirdParam$xqv
  9  @PRunDLLCommand@GetSecondParam$xqv
  9  @PRunDLLCommand@GetFunctionType$xqv
  9  @PRunDLLCommand@GetFunctionName$xqv
  9  @PRunDLLCommand@GetFirstParam$xqv
  9  @PRunDLLCommand@GetDLLReturnValue$xqv
  9  @PRunDLLCommand@GetDLLName$xqv
  9  @PRunDLLCommand@Execute$qv
  9  @PRunDLLCommand@$beql$xqrx11MPersistent
  9  @PRunDLLCommand@$bdtr$qv
  9  @PRunDLLCommand@$bctr$qv
  9  @PRunDLLCommand@$bctr$qrx14PRunDLLCommand
  9  @PRunDLLCommand@$basg$qrx14PRunDLLCommand
  8  _Java_com_sun_java_accessibility_AccessBridge_runDLL@8
  8  InstallSecurityPromptRunDllW
  8  DeviceProperties_RunDLLW
  8  DeviceProperties_RunDLLA
  7  DriverStoreRunDllW
  7  DeviceProblenWizard_RunDLLW
  7  DeviceProblenWizard_RunDLLA
  7  ?runDll@SV_HttpdAPI@@AAE_NPBD@Z
  6  extract_RunDLL
  6  WOW64Uninstall_RunDLLW
  6  UsersRunDll
  6  SxspRunDllDeleteDirectoryW
  6  SxspRunDllDeleteDirectory
  6  S3Disp_RunDll
  6  Rundll32RegisterServer
  6  RunDllProcW
  6  RunDllProcA
  6  RunDllEntry
  6  RunAsNewUser_RunDLLW
  6  PrepareDiscForBurnRunDllW
  6  LaunchMSHelp_RunDLLW
  6  AddNetPlaceRunDll
  6  @Jcldotnet@RunDll32ShimW$qqsxuixuipbxi
  5  RunDll_SetDefaultPrinter
  5  RunDll32Main
  5  PublishRunDll
  5  PassportWizardRunDll
  5  CscPolicyProcessing_RunDLLW
  5  CSCOptions_RunDLLW
  5  CSCOptions_RunDLLA
  5  CSCOptions_RunDLL
  4  update_start_rundll_old
  4  update_start_rundll
  4  uninstall_start_rundll_old
  4  uninstall_start_rundll
  4  rundll32_shellexec
  4  Wizard_RunDLL
  4  Rundll_EntryPoint
  4  DiskCopyRunDllW
  4  DiskCopyRunDll
  4  CI3_CreateShortcut_RUNDLL_32
  3  fnRunDll32
  3  _rundll32_shellexec@16
  3  WdipLaunchRunDLLUserHost
  3  Rundll32
  3  RunDll_UpdateDriver
  3  RunDll_Reenumerate
  3  RunDllHardwareTest
  3  RunDllA
  3  News_RunDLL
  3  NdfRunDllHelpTopic
  3  NdfRunDllDuplicateIPOffendingSystem
  3  NdfRunDllDuplicateIPDefendingSystem
  3  NdfRunDllDiagnoseWithAnswerFile
  3  NdfRunDllDiagnoseNetConnectionIncident
  3  NdfRunDllDiagnoseIncident
  3  Mail_RunDLL
  3  LogOffRunDLL
  3  Java_com_sun_java_accessibility_AccessBridge_runDLL
  3  CreateRegWizard_RunDll
  3  BoxedAppSDK_RunDll32_Callback
  2  rundll_analyze
  2  rundllIsAdmin
  2  _RunDll
  2  _RunDLLReport@16
  2  ShowRunDLLW
  2  ShowRunDLL
  2  ServiceRunDll
  2  RunDll32
  2  RunDLL_SaveImageFile
  2  RunDLL_RemoveDevice
  2  RunDLL_MountFileW
  2  RunDLL_MountFile
  2  RunDLL_DoCleanupW
  2  RunDLL_DoCleanupA
  2  RunDLLReport
  2  NotifyDevicesNeedRebootRunDllW
  2  ICRemoveByRundll
  2  ICInstallByRundll
  2  GetRunDllModule
  2  FromRunDll
  2  DllUnregisterServer_RunDll
  2  DllRegisterServer_RunDll
  2  DllIsRegisterServer_RunDll
  1  rundll_install_npq2f_srv2003
  1  rundll_install_npq2f
  1  rundll_install_ex
  1  rundll_install
  1  rundll_config
  1  dtuSerialRunDll
  1  dpuRunDllXML
  1  _RunDLL_SaveImageFile@16
  1  _RunDLL_RemoveDevice@16
  1  _RunDLL_MountFileW@16
  1  _RunDLL_MountFile@16
  1  UsersRunDllW
  1  Rundll32Call
  1  RunDllUnregisterMAPI
  1  RunDllRegisterMAPI
  1  RunDllInterfaceW
  1  RunDLLCommand
  1  RunDLL
  1  RegisterRunDll
  1  NetAccWizRunDll
  1  MigrateRunDll32
  1  Ma...