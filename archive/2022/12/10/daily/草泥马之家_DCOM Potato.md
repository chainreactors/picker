---
title: DCOM Potato
url: http://www.zcgonvh.com/post/DCOMPotato.html
source: 草泥马之家
date: 2022-12-10
fetch_date: 2025-10-04T01:03:35.754947
---

# DCOM Potato

# [草泥马之家](https://www.zcgonvh.com/)

### Windows与.Net.....

* [首页](https://www.zcgonvh.com/)
* [文档](https://www.zcgonvh.com/Documents.html)
* [工具](https://www.zcgonvh.com/Tools.html)
* [留言本](https://www.zcgonvh.com/guestbook.html)

现在的位置：
[首页](https://www.zcgonvh.com/ "返回首页")
＞
[Windows](https://www.zcgonvh.com/category-Windows.html "查看 Windows 分类下的所有文章")
＞正文

## DCOM Potato

###### 2022年12月09日 zcgonvh / Windows / 评论：0 / 浏览：4849

去年猫猫托梦带来的洞，两个EXP原理一样，只有服务不同，所以存在一些微小的差别。

漏洞原理是`McpManagement/PrinterNotify`这两个服务通过`svchost`托管，并公开了自己的DCOM对象。svchost有个特性，在[注册表](<https://www.geoffchappell.com/studies/windows/win32/services/svchost/process/index.htm>)可以配置自定义的`ImpersonateLevel`，这个值会传递给`CoInitializeSecurity`，从而更改所有远程`IUnknown`默认对外连接的模拟等级。

默认安装的情况下有且只有这两个服务配置了ImpersonateLevel，且均为`RPC\_C\_IMP\_LEVEL\_IMPERSONATE`：

```
#after 12r2
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost\print@ImpersonationLevel

#2022 only
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost\McpManagementServiceGroup@ImpersonationLevel
```

所以只要自己实现一个COM对象，在`IUnknown::QueryInterface/Release/Addref`中直接调用`CoImpersonateClient`，就能捕获到一个`SecurityImpersonation`等级的token，之后创建进程什么的就随意了。

核心技巧都是六七年前的东西，取Token可以认为是James Forshaw 15年那个祖传的`CaptureImpersonationToken.cpp`翻版；`PrinterNotify`服务20年decoder-it也提到过，只不过他们对DCOM理解不够深，还局限在`UnmarshalPwn`的思路上，没做这种利用；Token和模拟滥用就更古老了。

当然了，微软一直认为“SeImpersonatePrivilege to LOCAL SYSTEM is a feature by design, not a security boundary”，安心用一段时间还是可以的。

另致防御/应急/PR：“修补”方法是禁用没用的`PrinterNotify/McpManagement`服务，对服务器没有任何影响，哪怕它是个打印服务器。

Github：<https://github.com/zcgonvh/DCOMPotato/tree/master>

##### Tags： [Exploit](https://www.zcgonvh.com/tags-Exploit.html)   [工具](https://www.zcgonvh.com/tags-Tools.html)   [Windows](https://www.zcgonvh.com/tags-Windows.html)   [COM](https://www.zcgonvh.com/tags-COM.html)

【上篇】 [Advanced Windows TaskScheduler Playbook - Part.3 from RPC to lateral movement](https://www.zcgonvh.com/post/Advanced_Windows_Task_Scheduler_Playbook-Part.3_from_RPC_to_lateral_movement.html "Advanced Windows TaskScheduler Playbook - Part.3 from RPC to lateral movement")

* 留言列表:

发表留言:[取消回复](#divCommentPost)

名称(\*)

邮箱

网址

验证码(\*) ![](https://www.zcgonvh.com/zb_system/script/c_validcode.php?id=cmt)

正文(\*)

◎欢迎参与讨论，请在这里发表您的看法、交流您的观点。

搜索

最近发表
:   * [DCOM Potato](https://www.zcgonvh.com/post/DCOMPotato.html)
    * [Advanced Windows TaskScheduler Playbook - Part.3 from RPC to lateral movement](https://www.zcgonvh.com/post/Advanced_Windows_Task_Scheduler_Playbook-Part.3_from_RPC_to_lateral_movement.html)
    * [Advanced Windows Task Scheduler Playbook - Part.2 from COM to UAC bypass and get SYSTEM dirtectly](https://www.zcgonvh.com/post/Advanced_Windows_Task_Scheduler_Playbook-Part.2_from_COM_to_UAC_bypass_and_get_SYSTEM_dirtectly.html)
    * [Advanced Windows Task Scheduler Playbook - Part.1 basic](https://www.zcgonvh.com/post/Advanced_Windows_Task_Scheduler_Playbook-Part.1_basic.html)
    * [EfsPotato](https://www.zcgonvh.com/post/EfsPotato.html)
    * [CVE-2020-17144漏洞分析与武器化](https://www.zcgonvh.com/post/analysis_of_CVE-2020-17144_and_to_weaponizing.html)
    * [Windows任意文件下载的三个Tips](https://www.zcgonvh.com/post/tips_of_arbitrary_file_read_on_windows.html)
    * [CVE-2020-0688的武器化与.net反序列化漏洞那些事](https://www.zcgonvh.com/post/weaponizing_CVE-2020-0688_and_about_dotnet_deserialize_vulnerability.html)
    * [POP3 MITM思路与简单实现](https://www.zcgonvh.com/post/POP3_MITM_Example.html)
    * [RemoteFreeLibrary](https://www.zcgonvh.com/post/RemoteFreeLibrary.html)

最新留言
:   * [Now try the ysoserial.net directly, in fact, I was submitted a pull request for it a few years ago.You just need to use `ActivitySurrogateSelectorFromFile` and pass your own backdoor assembly to generate the payload, this is the large byte array named `stub` in the source.And, if the .net framework installed on the target server is updated(I forgot the exact time, maybe after 2020), the `ActivitySurrogateDisableTypeCheck` payload is also needed, this is the small byte array named `v48disablecheck` in the source.Have fun.](https://www.zcgonvh.com/post/weaponizing_CVE-2020-0688_and_about_dotnet_deserialize_vulnerability.html#cmt506 "zcgonvh @ 2024-12-06 21:43:26")
    * [Hi All.plz update code.thanks A lot.](https://www.zcgonvh.com/post/tips_for_cve_2017_7269.html#cmt503 "DocKer @ 2024-11-12 21:44:49")
    * [Hey currently in an active pentest and wanted to check out your Sharepoint CVE that just dropped. Any way to contact you and discuss?](https://www.zcgonvh.com/guestbook.html#cmt502 "Caring @ 2024-10-09 10:41:46")
    * [Hi.plz Update cve-2017-7269https://github.com/zcgonvh/cve-2017-7269-tool](https://www.zcgonvh.com/guestbook.html#cmt501 "lolminerx @ 2024-09-29 01:33:45")
    * [Hello first of all very thankful for your writeup and work done on the poc and rce.Wanted to ask you how did you generate the payload? where from etc.I tried generating the exact payload of your poc for example and didnt manage to get the same result or a result that worked.I need to generate my payload from zero so if you'd be able to explain how did you do that or give the source code of yours it will be very helpfulThanks alot](https://www.zcgonvh.com/post/weaponizing_CVE-2020-0688_and_about_dotnet_deserialize_vulnerability.html#cmt500 "hvnogcz @ 2024-09-23 20:38:02")
    * [I'm sorry it took me some time to find my report, I've sent you an email, please check it.](https://www.zcgonvh.com/post/MS15_015.html#cmt499 "zcgonvh @ 2023-12-27 20:48:19")
    * [Hi,I'am currently having some difficulty in trying to reproduce the CVE-2023-21706 and CVE-2023-21710 of yours, can you give me some hints.Nguyen](https://www.zcgonvh.com/post/MS15_015.html#cmt498 "Nguyen @ 2023-12-21 14:18:01")
    * [6](https://www.zcgonvh.com/post/aspxspy_2014_final.html#cmt496 "add @ 2023-11-09 09:14:47")
    * [我收回这句话，当我没说，解压密码找到了](https://www.zcgonvh.com/post/MS16_032_for_SERVICE_only.html#cmt491 "呀吼 @ 2022-12-23 15:19:23")
    * [压缩包双击打开，仔细看工具栏那里，有个《注释》选项，点开里面就是解压密码，其实楼主的名字就是解压密码](https://www.zcgonvh.com/post/MS16_032_for_SERVICE_only.html#cmt490 "呀吼 @ 2022-12-23 15:17:05")

分类归档
:   * [Sql (9)](https://www.zcgonvh.com/category-Sql.html)
    * [Exp (8)](https://www.zcgonvh.com/category-Exp.html)
    * [Asp.Net (5)](https://www.zcgonvh.com/category-AspDotNet.html)
    * [Web (4)](https://www.zcgonvh.com/category-Web.html)
    * [c/c++ (4)](https://www.zcgonvh.com/category-C-CPP.html)
    * [域渗透 (4)](https://www.zcgonvh.com/category-Domain.html)
    * [杂谈 (3)](https://www.zcgonvh.com/category-Others.html)
    * [Script (3)](https://www.zcgonvh.com/category-Script.html)
    * [.Net (2)](https://www.zcgonvh.com/category-DotNet.html)
    * [WinDbg (2)](https://www.zcgonvh.com/category-WinDbg.html)
    * [PowerShell (2)](https://www.zcgonvh.com/category-PowerShell.html)
    * [Wmi (1)](https://www.zcgonvh.com/category-Wmi.html)
    * [MITM (1)](https://www.zcgonvh.com/category-MITM.html)

RSS
:   * [![RSS](https://www.zcgonvh.com/zb_system/image/logo/rss-z.png)](https://www.zcgonvh.com/feed.php)

联系方式
:   - zcgonvh#at#qq.com
    - ![公众号](https://www.zcgonvh.com/zb_system/image/wx/wx.jpg)

### Copyright GMH's [Home](https://www.zcgonvh.com/zb_system/login.php). Powered By Z-Blog.