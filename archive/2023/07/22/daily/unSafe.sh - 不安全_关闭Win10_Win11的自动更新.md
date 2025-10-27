---
title: 关闭Win10/Win11的自动更新
url: https://buaq.net/go-172657.html
source: unSafe.sh - 不安全
date: 2023-07-22
fetch_date: 2025-10-04T11:52:27.678011
---

# 关闭Win10/Win11的自动更新

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

关闭Win10/Win11的自动更新

阅读： 7Win10的强制自动更新对许多群体不友好，搞网络安全的就不说了，搓火、辛酸。不少人想变「强制自动更新」为「按需手动更新」，懂行的那是八仙过海、各显神通，但
*2023-7-21 19:8:52
Author: [blog.nsfocus.net(查看原文)](/jump-172657.htm)
阅读量:25
收藏*

---

阅读： 7

Win10的强制自动更新对许多群体不友好，搞网络安全的就不说了，搓火、辛酸。不少人想变「强制自动更新」为「按需手动更新」，懂行的那是八仙过海、各显神通，但过去我看到的方案都不尽人意。

最近在「吾爱破解」上看到一个变相关闭Win10/Win11自动更新的方案，可能是副作用最小、最易实施的方案。

https://www.52pojie.cn/thread-1809122-1-1.html

将如下内容存成”DisableAutoUpdate.reg”，双击导入注册表即可。

————————————————————————–

[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings]
“FlightSettingsMaxPauseDays”=dword:1fffffff
“PauseFeatureUpdatesStartTime”=”2023-07-18T09:02:26Z”
“PauseFeatureUpdatesEndTime”=”2123-08-22T09:02:26Z”
“PauseQualityUpdatesStartTime”=”2023-07-18T09:02:26Z”
“PauseQualityUpdatesEndTime”=”2123-08-22T09:02:26Z”
“PauseUpdatesExpiryTime”=”2123-08-22T09:02:26Z”
————————————————————————–

可用如下命令确认注册表项设置成功

reg.exe query “HKLM\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings” /s

还能看到两个有意思的键值，未深究:

IsExpedited REG\_DWORD 0x0
InsiderProgramEnabled REG\_DWORD 0x0

如欲恢复自动更新，将如下内容存成”EnableAutoUpdate.reg”，双击导入。

————————————————————————–
Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings]
“FlightSettingsMaxPauseDays”=-
“PauseFeatureUpdatesStartTime”=-
“PauseFeatureUpdatesEndTime”=-
“PauseQualityUpdatesStartTime”=-
“PauseQualityUpdatesEndTime”=-
“PauseUpdatesExpiryTime”=-
————————————————————————–

Diable时普通用户即可，Enable时若失败，就换管理员权限。非专业人员看到此处，就可以了。

后面是一些逆向工程讨论。

52pojie帖子里有个”PauseUpdatesStartTime”，该键值可能是想当然弄出来的，在逆向工程中并未发现相应代码。

正常情况下，非LTSB版Win10可以暂停自动更新35天，该值在MusUpdateHandlers.dll
的PauseUpdatesUtility::GetMaxPauseQualityPeriodInDays()中固化。

Settings->Update & Security->Windows Update->Pause updates for 7 days

此处可以点击5次，也就是35天。该限制受注册表项FlightSettingsMaxPauseDays影响，缺省没有FlightSettingsMaxPauseDays，此时使用缺省值35天。通过设置该键值，可将暂停自动更新的天数上限推至极大，比如我将之设为0x1fffffff。一旦上限极大，即可不停地点击”Pause updates for 7 days”，不再因到达阈值而变灰。这是32位有符号整数，理论上最大可设成0x7fffffff，但担心有加法上溢，保守起见，设成0x1fffffff。

有两个StartTime，分别对应功能更新、质量更新，后者一般包含安全补丁。StartTime就是你第一次点击”Pause updates for 7 days”的起始时间。

有两个EndTime，分别与前两个StartTime对应。正常情况下，EndTime-StarTime不会超过35天。前例差值是100年，有生之年都不会再自动更新。

正常情况下，PauseUpdatesExpiryTime应与两个EndTime保持一致。也就是说，有两个起始时间、三个结束时间。

接下来是一些具体的逆向工程活动。

用Process Monitor监控”Settings->Update & Security->Windows Update”，在其中搜索相应键值的读取操作，命中后查看PID及调用栈回溯。

PauseFeatureUpdatesEndTime

7 KERNELBASE.dll RegGetValueW + 0x254 0x7ffe13e92fe4 C:\Windows\System32\KERNELBASE.dll
8 UpdatePolicy.dll PolicyHelpers::ReadPolicyString + 0xd3 0x7ffe02efa0cf c:\windows\system32\UpdatePolicy.dll
9 UpdatePolicy.dll PolicyHelpers::ReadPolicyRegistry + 0x4c 0x7ffe02efa478 c:\windows\system32\UpdatePolicy.dll
10 UpdatePolicy.dll EnterprisePolicyReader::ReadPolicyWithFallbackInternal + 0x2a0 0x7ffe02eeea4c c:\windows\system32\UpdatePolicy.dll
11 UpdatePolicy.dll EnterprisePolicyReader::ReadPolicyWithFallback + 0x105 0x7ffe02eee755 c:\windows\system32\UpdatePolicy.dll
12 WaaSAssessment.dll DeviceAttributes::GetFeatureUpdatePauseStatus + 0x64 0x7ffdfea9ca14 C:\Windows\System32\WaaSAssessment.dll
13 WaaSAssessment.dll AssessmentCore::GetFeatureUpdateAssessmentReason + 0x142 0x7ffdfea97432 C:\Windows\System32\WaaSAssessment.dll
14 WaaSAssessment.dll AssessmentCore::GetAssessmentReason + 0x74 0x7ffdfea97794 C:\Windows\System32\WaaSAssessment.dll
15 WaaSAssessment.dll AssessmentCore::IsCurrent + 0x84 0x7ffdfea97834 C:\Windows\System32\WaaSAssessment.dll
16 WaaSAssessment.dll AssessmentCore::PerformAssessment + 0xf2 0x7ffdfea96de2 C:\Windows\System32\WaaSAssessment.dll
17 WaaSAssessment.dll AssessmentCore::GetOSUpdateAssessmentInternal + 0xf5 0x7ffdfea96bd5 C:\Windows\System32\WaaSAssessment.dll
18 WaaSAssessment.dll AssessmentCore::GetOSUpdateAssessment + 0x6d 0x7ffdfea96a6d C:\Windows\System32\WaaSAssessment.dll
19 usosvc.dll <lambda\_2ec50c5c930836d3269795c4434eaa5a>::operator() + 0x204 0x7ffdf74c0b78 c:\windows\system32\usosvc.dll
20 usosvc.dll UxUpdateManager::GetIsWaaSOutOfDate + 0x8a 0x7ffdf74c08aa c:\windows\system32\usosvc.dll
21 RPCRT4.dll Invoke + 0x73 0x7ffe1614b4b3 C:\Windows\System32\RPCRT4.dll
22 RPCRT4.dll Ndr64StubWorker + 0xb0b 0x7ffe161ae77b C:\Windows\System32\RPCRT4.dll
23 RPCRT4.dll NdrStubCall3 + 0xc9 0x7ffe160ed479 C:\Windows\System32\RPCRT4.dll

PID是5484，查看对应服务:

tasklist /svc /fi “pid eq 5484”
“Z:\Green\Windows Kits\10\x64\Debuggers\x64\tlist.exe” -s | findstr Svcs | findstr 5484
sc queryex UsoSvc
sc qc UsoSvc

这是”Update Orchestrator Service (UsoSvc)”服务。在管理员级cmd中执行

net use Z: “\\vmware-host\Shared Folders”
“Z:\Green\Windows Kits\10\x64\Debuggers\x64\cdb.exe” -noinh -snul -hd -o -p 5484
.prompt\_allow +reg +ea +dis

> lm m UpdatePolicy
start end module name
00007ffe`02ee0000 00007ffe`02f1d000 UpdatePolicy

用IDA反汇编UpdatePolicy.dll，Rebase后直奔调用栈回溯中的地址，查看相应代码。

PauseUpdatesExpiryTime:

6 KernelBase.dll RegQueryValueExW + 0x108 0x7ffe13e93808 C:\Windows\System32\KernelBase.dll
7 MusUpdateHandlers.dll RegistryManager::HKLMValueExists + 0x16a 0x7ffded14a90a C:\Windows\System32\MusUpdateHandlers.dll
8 MusUpdateHandlers.dll PauseUpdatesUtility::GetPauseUpdatesExpiryTimeRegValue + 0x62 0x7ffded156ad6 C:\Windows\System32\MusUpdateHandlers.dll
9 MusUpdateHandlers.dll PauseUpdatesUtility::AreUpdatesPaused + 0x26 0x7ffded1567fa C:\Windows\System32\MusUpdateHandlers.dll
10 MusUpdateHandlers.dll SystemSettings::Update::CMusOrchModel::SaveInsiderProgramStatus + 0xf 0x7ffded10fa4f C:\Windows\System32\MusUpdateHandlers.dll
11 MusUpdateHandlers.dll SystemSettings::Update::CMusOrchModel::SingletonInitialize + 0x55a 0x7ffded107502 C:\Windows\System32\MusUpdateHandlers.dll
12 MusUpdateHandlers.dll SystemSettings::Update::CMusOrchModel::OnSingletonInit + 0x1a 0x7ffded107f0a C:\Windows\System32\MusUpdateHandlers.dll
13 MusUpdateHandlers.dll SystemSettings::DataModel::CSingletonHelper<unsigned long>::\_Initialization + 0x89 0x7ffded0b3f01 C:\Windows\System32\MusUpdateHandlers.dll
14 MusUpdateHandlers.dll SystemSettings::DataModel::CSingletonHelper<unsigned long>::s\_InitializationThread + 0x9 0x7ffded0b4039 C:\Windows\System32\MusUpdateHandlers.dll
15 SHCore.dll \_WrapperThreadProc + 0xe9 0x7ffe15e2bf69 C:\Windows\System32\SHCore.dll

FlightSettingsMaxPauseDays:

6 KernelBase.dll RegQueryValueExW + 0x108 0x7ffe13e93808 C:\Windows\System32\KernelBase.dll
7 MusUpdateHandlers.dll RegistryManager::HKLMValueExists + 0x16a 0x7ffded14a90a C:\Windows\System32\MusUpdateHandlers.dll
8 MusUpdateHandlers.dll PauseUpdatesUtility::GetMaxPauseQualityPeriodInDays + 0x40 0x7ffded156970 C:\Windows\System32\MusUpdateHandlers.dll
9 MusUpdateHandlers.dll SystemSettings::Update::CMusUpdatePauseUpdate2::InitializeState + 0x1ce 0x7ffded0dc61e C:\Windows\System32\MusUpdateHandlers.dll
10 MusUpdateHandlers.dll <lambda\_caa38285ec31a58b02b71299ca7d801b>::operator() + 0x122 0x7ffded0c6b72 C:\Windows\System32\MusUpdateHandlers.dll
11 MusUpdateHandlers.dll std::thread::\_Invoke<std::tuple<<lambda\_caa38285ec31a58b02b71299ca7d801b> >,0> + 0xe 0x7ffded0c81ee C:\Windows\System32\MusUpdateHandlers.dll
12 ucrtbase.dll thread\_start<unsigned int (\_\_cdecl\*)(void \*),1> + 0x42 0x7ffe14181bb2 C:\Windows\System32\ucrtbase.dll

PID是6732，对应下列进程:

“C:\Windows\ImmersiveControlPanel\SystemSettings.exe” -ServerName:microsoft.windows.immersivecontrolpanel

直接在cmd中执行上述命令，会失败，不信可以试试。

“Z:\Green\Windows Kits\10\x64\Debuggers\x64\cdb.exe” -noinh -snul -hd -o -p 6732
.prompt\_allow +reg +ea +dis

> lm m MusUpdateHandlers
start end module name
00007ffd`ed0a0000 00007ffd`ed1c2000 MusUpdateHandlers

用IDA反汇编MusUpdateHandlers.dll并Rebase。

FlightSettingsMaxPauseDays阻止通过UI无限暂停，但无它也无所谓。可先手动暂停35天，以生成StartTime、EndTime、ExpiryTime等键值，然后直接...