---
title: KARR蓝牙漏洞危机：220万辆车陷远程控制风险，共用密钥暴露安全隐患
url: https://mp.weixin.qq.com/s/TIJAWL7rkG4JVEecTlnEMw
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:21:44.935209
---

# KARR蓝牙漏洞危机：220万辆车陷远程控制风险，共用密钥暴露安全隐患

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnuPP5FuqSPfDXibSBwNRwzBsZ4hatnAlrmTsibUF2c7q46yF7BqBv4QcYrA5xlQcs1c2GG0jf5WzrOxXpKuhVp72s0KoMNOoh2ZI/0?wx_fmt=jpeg)

# KARR蓝牙漏洞危机：220万辆车陷远程控制风险，共用密钥暴露安全隐患

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJntZEIM128fc30OCu3e1wScexnrHk7knuY0hPeemQcpO9KnGnFxELUhIPt4syibsGiaicEnoG4hIyLNeDCb9VtlNPTZdn6nRNvTyWQ/640?wx_fmt=png&from=appmsg)

加州大学圣迭戈分校研究人员近日披露，售后安装的KARR安全系统存在蓝牙漏洞，导致约220万辆汽车面临远程攻击风险，攻击者可在蓝牙范围内未经授权解锁车门、操控警报系统甚至使车辆无法启动。

该漏洞由加州大学圣迭戈分校研究人员发现，凸显了经销商预装硬件带来的新型风险——此类设备游离于传统汽车安全框架之外，却深度接入车辆关键控制系统。经销商通常在车辆售前安装KARR系统作为防盗措施，但即便车主未激活或拒绝付费服务，硬件仍普遍保留在车辆中。

这种做法导致大量车主在不知情的情况下成为受影响用户，其中许多车辆即使处于未激活状态，仍持续发射蓝牙信号。

KARR Bluetooth Vulnerability
研究人员指出，攻击者只需处于蓝牙通信范围内，即可向车辆警报系统发送指令。这些指令包括锁闭或解锁车门、关闭警报、触发车灯与喇叭，以及阻止发动机启动。尽管该漏洞无法实现对行驶中车辆的远程驾驶控制，但通过为窃贼提供静默进入车厢的途径，显著降低了盗窃门槛。

漏洞根源在于所有KARR设备预置了相同的认证密钥。研究人员通过逆向分析官方KARR手机应用，成功提取这一通用密钥，并开发出概念验证版安卓应用以模拟合法用户身份。借助该工具，他们无需针对特定设备定制攻击手段，即可成功操控多辆测试车辆。

加州大学圣迭戈分校研究人员利用众源WiGLE无线电数据库绘制了全美KARR设备车辆分布图（来源：appleinsider）。

尽管Acrisure Protection Group将KARR攻击描述为“技术复杂且风险较低”，但研究人员强调，一旦密钥泄露，攻击方法将变得极为简单，且可规模化应用于所有受影响系统。

缓解措施面临特殊挑战：由于KARR未集成至汽车制造商原生系统，传统空中传输更新或厂商召回机制均不适用。据AppleInsider报道，Acrisure在2025年1月获知漏洞后，于2026年7月20日发布固件补丁，但车主必须手动确认车辆是否安装KARR硬件，并通过KARR手机应用完成更新。

除活跃攻击风险外，该漏洞还引发隐私隐患。KARR系统在车辆使用期间及熄火后短时间内持续发射可识别蓝牙信号。研究人员利用WiGLE无线追踪数据库评估了此类系统的广泛部署情况，并演示了历史信号数据如何暴露车辆移动轨迹或高频访问地点。

在圣迭戈周边的一次短途路测中，研究人员即检测到近100辆搭载KARR系统的车辆信号，印证了被忽视的售后设备可能在数百万车辆中制造重大安全缺口。

车主应检查驾驶员侧车窗或仪表板下方是否存在KARR或SWDS标识。安装KARR Security应用并更新至最新固件是当前主要缓解手段。若无法确认设备存在或完成更新，建议联系经销商或KARR技术支持。

此次事件凸显了汽车网络安全的深层挑战：第三方硬件可能绕过既有安全控制体系，导致制造商与消费者均缺乏风险可见性，并延缓响应能力。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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