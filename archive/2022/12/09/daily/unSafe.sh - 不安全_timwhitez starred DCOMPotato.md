---
title: timwhitez starred DCOMPotato
url: https://buaq.net/go-139229.html
source: unSafe.sh - 不安全
date: 2022-12-09
fetch_date: 2025-10-04T00:57:16.912833
---

# timwhitez starred DCOMPotato

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

![](https://8aqnet.cdn.bcebos.com/c58da63fbf6c196a35ca5460c4325428.jpg)

timwhitez starred DCOMPotato

writeupDCOM use RPC\_C\_IMP\_LEVEL\_IDENTIFY as default impersonation level, for the defa
*2022-12-8 23:6:47
Author: [github.com(查看原文)](/jump-139229.htm)
阅读量:33
收藏*

---

## writeup

DCOM use `RPC_C_IMP_LEVEL_IDENTIFY` as default impersonation level, for the default out-bound `IUnknown` call, see <https://learn.microsoft.com/en-us/windows/win32/com/com-security-defaults>. Of course, COM Server can override by call `CoInitializeSecurity` explicitly.

We known most windows service register their DCOM Server to provide features, [Shared Process Service](https://learn.microsoft.com/en-us/windows/win32/services/service-programs) was hosted by `svchost`, read the default impersonation level from [registry](https://www.geoffchappell.com/studies/windows/win32/services/svchost/process/index.htm).

If we pass a malicious `IUnknown` object as parameter at some DCOM call, service process will call `IRemUnknown::RemQueryInterface/RemRelease/RemAddref` on the ProxyObject, now we can got a `SecurityImpersonation` token by `CoImpersonateClient` because we are `DCOM Server` at this time.

Follow was the explicit setting `ImpersonationLevel` as `RPC_C_IMP_LEVEL_IMPERSONATE` in default installation:

```
#after 12r2
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost\[email protected]

#2022 only
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost\[email protected]
```

The services are `PrinterNotify` and `McpManagementService`, running as `SYSTEM`.

## build

Note this code was supports x64 and NetFX 4.x only, but you can do a little change for FX2.0/x86 compatibility(IUnknown vtbl hook, see `McpManagementPotato`).

```
csc /unsafe PrinterNotifyPotato.cs
csc /unsafe McpManagementPotato.cs
```

## usage

```
McpManagementPotato/PrinterNotifyPotato <command>
```

[![](https://raw.githubusercontent.com/zcgonvh/DCOMPotato/master/images/McpManagementPotato.png)](https://raw.githubusercontent.com/zcgonvh/DCOMPotato/master/images/McpManagementPotato.png)

[![](https://raw.githubusercontent.com/zcgonvh/DCOMPotato/master/images/PrinterNotifyPotato.png)](https://raw.githubusercontent.com/zcgonvh/DCOMPotato/master/images/PrinterNotifyPotato.png)

**Thanks for [UnmarshalPwn](https://github.com/codewhitesec/UnmarshalPwn)!**

(and love my cat, Vanilla, can someone make it nekogirl?)

文章来源: https://github.com/zcgonvh/DCOMPotato
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)