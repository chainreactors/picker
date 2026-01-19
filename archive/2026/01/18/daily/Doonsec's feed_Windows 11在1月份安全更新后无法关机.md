---
title: Windows 11在1月份安全更新后无法关机
url: https://mp.weixin.qq.com/s/hbEJnHZM6-WQ1i_bcngjLQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:43:11.209636
---

# Windows 11在1月份安全更新后无法关机

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eCL9rXDTWqT82icT7smGp7x7uuX2O7YNDc1iahjQdbjhpDfvstnBsNq6DurLDdmBs0VDOmzsfgbl1yud9ShTvzNQ/0?wx_fmt=jpeg)

# Windows 11在1月份安全更新后无法关机

祺印说信安

![]()

在小说阅读器中沉浸阅读

以下文章来源于豫说网数安
，作者何威风

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM59AUe157CquBULm3Sn1mS0bZLHRaoSOicaicgKiaq5h5rsQ/0)

**豫说网数安**
.

网络安全人人有责，贯彻网络安全为人民，网络安全靠人民。网络安全和信息化是相辅相成的。安全是发展的前提，发展是安全的保障，安全和发展要同步推进。

![](https://mmbiz.qpic.cn/mmbiz_png/eCL9rXDTWqT82icT7smGp7x7uuX2O7YNDqialnvycobN9NEYlDbPDGwPtRYSTzK8YbL0GOhqFs5xHvgnPbYk1iaKA/640?wx_fmt=png&from=appmsg)

微软于2026年1月13日发布的Windows 11引发了一个令人沮丧的错误：受影响的电脑拒绝关机或休眠，而是重新启动。

该问题由KB5073455引起，该更新针对Windows 11版本23H2上的操作系统版本22621.6491。该问题于1月15日首次被报告，原因是其干扰了安全启动（Secure Launch），安全启动是一种基于虚拟化的安全 (VBS) 功能，旨在保护启动过程免受rootkit等固件威胁的侵害。

Secure Launch 是 Windows 系统防护套件的一部分，它使用虚拟机监控程序保护的代码完整性在启动期间验证固件环境。

隔离核心信任根度量可以防止持久性恶意软件篡改操作系统前的环境。讽刺的是，本月旨在加强防御的补丁却破坏了这一功能，导致兼容硬件无法正常关机。

# 受影响的系统和范围

此次故障仅影响Windows 11 23H2的企业版和物联网版，家庭版和专业版不受影响。Windows Server等服务器平台不受影响。

微软通过其支持门户网站架构等合规性标准。

受监管行业（包括金融和政府部门）的管理人员反映，车队中存在这个问题，引发了人们对电源管理可靠性的担忧。

虽然该漏洞本身并非安全漏洞，但它暴露了风险：陷入重启循环的设备会更快地耗尽电池电量，这可能会导致数据丢失或无人值守的运行时间，从而加剧未修补威胁带来的风险。

微软提供了一个通过命令提示符解决关机问题的临时方案：从搜索栏启动cmd ，然后运行shutdown /s /t 0。这将强制立即关机，绕过图形用户界面 (GUI) 的故障提示。休眠模式没有类似的解决方法；用户必须保存工作并选择完全关机，以防止意外断电。

该公司承诺将在即将发布的更新中修复此问题，并敦促IT团队密切关注 Windows更新渠道。在此期间，通过禁用安全启动（计算机配置 > 管理模板 > 系统 > 设备防护）可以恢复功能，但会降低启动完整性——对于权衡固件攻击风险的威胁猎手来说，这是一个需要权衡的因素。

此次事件凸显了每月“补丁星期二”发布机制的双刃剑效应。企业在修复零日漏洞的同时，此类回归问题也凸显了分阶段测试的必要性，尤其是在安全加固的配置上。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTibWNx9ARWmJry3EdlWaJ61fpNvcajYeq9iaicmJEMxX83jySkhKCmwDVadpzqKsDFScYjsz4CcCkdb7pGibq5yOA/0?wx_fmt=png)

祺印说信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rTibWNx9ARWmJry3EdlWaJ61fpNvcajYeq9iaicmJEMxX83jySkhKCmwDVadpzqKsDFScYjsz4CcCkdb7pGibq5yOA/0?wx_fmt=png)

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