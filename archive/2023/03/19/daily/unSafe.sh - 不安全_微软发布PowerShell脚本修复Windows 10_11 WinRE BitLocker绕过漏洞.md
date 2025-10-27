---
title: 微软发布PowerShell脚本修复Windows 10/11 WinRE BitLocker绕过漏洞
url: https://buaq.net/go-154090.html
source: unSafe.sh - 不安全
date: 2023-03-19
fetch_date: 2025-10-04T10:01:51.479888
---

# 微软发布PowerShell脚本修复Windows 10/11 WinRE BitLocker绕过漏洞

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

![](https://8aqnet.cdn.bcebos.com/60405ce65867cddb99a8d18b980d2c24.jpg)

微软发布PowerShell脚本修复Windows 10/11 WinRE BitLocker绕过漏洞

微软本周向企业IT管理员推出专用的PowerShell脚本 , 这些脚本的目的是用于修复CVE-2022-41099号漏洞。该漏洞首发时间是2022年11月8日 , 攻击者物理接触到P
*2023-3-18 23:36:57
Author: [www.landiannews.com(查看原文)](/jump-154090.htm)
阅读量:21
收藏*

---

微软本周向企业IT管理员推出专用的PowerShell脚本 , 这些脚本的目的是用于修复CVE-2022-41099号漏洞。

该漏洞首发时间是2022年11月8日 , 攻击者物理接触到PC的情况下 , 可以利用漏洞绕过 BitLocker 磁盘加密。

对企业来说这是个安全隐患，攻击者可以绕过加密策略获取存储设备上的文件，所幸这个功能不能远程利用。

微软之前已经发布安全更新修复该漏洞，现在发布的脚本是为那些至今仍然无法安装安全更新的设备准备的。

[![微软发布PowerShell脚本修复Windows 10/11 WinRE BitLocker绕过漏洞](https://img.lancdn.com/landian/2023/03/97894.png)](https://img.lancdn.com/landian/2023/03/97894.png)

▲图片来自@[BP](https://www.bleepingcomputer.com/news/security/microsoft-shares-script-to-fix-winre-bitlocker-bypass-flaw/)

**KB5025175号更新：**

该安全更新指的就是这次发布的PowerShell脚本 ，微软提供2份脚本，企业IT管理员可以按需使用这些脚本。

推荐使用的脚本是PatchWinREScript\_2004plus.ps1，该脚本支持 Windows 10 Version 2004 及以上版本。

该脚本更健壮但支持的系统版本有限，使用该脚本时系统将自动安装最新的系统动态更新并更新WinRE镜像。

PatchWinREScript\_General.ps1脚本支持Windows 10/11所有版本包括旧版，但安全逻辑不如前面的脚本。

如果企业仍然无法安装更新 , 还有个办法启用TPM+PIN保护 , 这种情况下黑客拿不到PIN则也无法解密数据。

以上脚本执行时均需联网，如果担心翻车，最好提前做好数据备份或者利用第三方软件对系统创建恢复镜像。

**微软提供的其他说明：**

当脚本执行时系统将自动装在当前版本的WinRE映像文件，注意此时装载的还是当前系统的版本并非新版本。

随后脚本会通过系统更新目录提供的安全操作系统动态更新 (Safe OS) 在线更新WinRE映像，随后卸载映像。

接着BitLocker TPM保护程序会为BitLocker服务重新配置WinRE映像 , 此时使用的就是更新之后的新映像了。

[有关 KB5025175 更新的内容及脚本下载地址点击查看](https://support.microsoft.com/en-us/topic/kb5025175-updating-the-winre-partition-on-deployed-devices-to-address-security-vulnerabilities-in-cve-2022-41099-ba6621fa-5a9f-48f1-9ca3-e13eb56fb589)，[有关CVE-2022-41099漏洞的内容请点击这里查看](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41099)。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/97894.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/97894.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)