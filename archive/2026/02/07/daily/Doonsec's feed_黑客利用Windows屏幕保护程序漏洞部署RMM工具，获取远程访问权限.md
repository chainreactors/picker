---
title: 黑客利用Windows屏幕保护程序漏洞部署RMM工具，获取远程访问权限
url: https://mp.weixin.qq.com/s/zk-LYFz3SAUzX_K8ddX_jw
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:17.030376
---

# 黑客利用Windows屏幕保护程序漏洞部署RMM工具，获取远程访问权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnsaPBEZ6NyuSPg5hBO1ZsWhsRl7Z2ibcS08B7cqibrJN9H14CIlIRGpXeXkntJovKer21xAFnicsIZoAXlD4YzZE6rvAktzBQtZWM/0?wx_fmt=jpeg)

# 黑客利用Windows屏幕保护程序漏洞部署RMM工具，获取远程访问权限

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnv3n3rdSwTEuQ1EEeicZ3eKlRk6NuJ2tsnUElZLhhn7S69AWa4AqwgIqOKHC6ZgibbnrJDg1sw4iaZYZHoAZJpRRlzlBNvJA11j7s/640?wx_fmt=jpeg&from=appmsg)

**一种新型钓鱼攻击活动利用被遗忘的文件类型绕过现代防御体系**。攻击者正在引诱受害者下载Windows屏幕保护程序(.scr)文件，这些文件会**悄无声息地部署合法的远程监控与管理(RMM)软件**，从而在目标系统中建立**持久化控制**。

该活动采用**简单而有效的交付机制**，旨在规避基于信誉的检测。

攻击始于一封**带有商业主题诱饵的鱼叉式钓鱼邮件**，例如"InvoiceDetails.scr"或"ProjectSummary.scr"。

这些文件托管在GoFile等**公共文件共享平台**上，使恶意链接能够绕过可能会标记直接附件或已知恶意域名的标准邮件安全网关。

对普通用户而言，屏幕保护程序文件看似无害。然而，在Windows环境中，.scr文件在技术上是一个**可移植可执行文件(PE)**，功能与.exe文件完全相同。当用户双击其下载文件夹中的文件时，**代码会立即执行**。

**利用合法RMM工具进行攻击**
ReliaQuest观察到，与端点检测系统可能立即识别的自定义恶意软件不同，此活动安装的是**合法的RMM代理**，如SimpleHelp。

这种"Living off the Land"（白利用）方法因以下两个原因而危险：

* **规避性**：安全工具通常信任RMM软件，因为它被IT部门广泛用于合法支持。安装过程不会产生典型的"恶意软件"信号。
* **持久性**：一旦安装，RMM工具为攻击者提供**交互式、持久的远程访问**，即使系统重启后仍能保持连接。

从这一立足点出发，攻击者可以**混入正常网络流量**，同时提升权限、窃取凭证、外泄敏感数据或为勒索软件部署准备环境。

**防御重点**
此活动揭示了当前许多安全态势中的**关键缺口**：对可执行文件类型和远程支持工具缺乏严格管控。

为防御此威胁，组织必须转变对"特权"应用程序的定义。

**关键缓解策略包括**：

* **限制.scr执行**：将屏幕保护程序文件与.exe或.msi文件同等对待。配置应用控制策略（如AppLocker或Windows Defender应用控制），阻止从下载、临时和桌面等用户可写目录执行.scr文件。
* **强制RMM白名单**：维护授权远程管理软件的严格白名单。默认情况下应阻止此列表之外的任何RMM工具。
* **监控相关痕迹**：安全团队应关注与未知RMM供应商相关的意外计划任务、服务或ProgramData文件夹的创建。

通过加强对被忽视文件扩展名的控制并监控未经授权的远程访问工具，防御者可以在攻击者转向最终目标之前**切断此攻击链**。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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