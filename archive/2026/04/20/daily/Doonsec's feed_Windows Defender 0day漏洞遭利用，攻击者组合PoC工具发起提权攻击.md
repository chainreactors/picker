---
title: Windows Defender 0day漏洞遭利用，攻击者组合PoC工具发起提权攻击
url: https://mp.weixin.qq.com/s/D_9H3keQB-CQlGIwUsj7Lg
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:47:02.186580
---

# Windows Defender 0day漏洞遭利用，攻击者组合PoC工具发起提权攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2RzZf6IvRgNkztTPOIR6dPAOzDpZIrgCKhw8OZr03ic8CMQP9cEIQLXz49Pu7Ydm2gzpo6xBEzQTODbKXK9ic3oBcuFFzrPJuCM/0?wx_fmt=jpeg)

# Windows Defender 0day漏洞遭利用，攻击者组合PoC工具发起提权攻击

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3wcLQjianFR6Odr4uVMpnfJ1kTMibJWNyxibZiaQIibWolOxKl2iayJCiaA8IU1jU7sWI2A1nXtMwIcBMBR6gvlNhzKgWstZVWBoQpK0/640?wx_fmt=png&from=appmsg)

##

网络安全研究人员发现，近期泄露的三个Windows Defender提权漏洞正遭实际攻击利用。攻击者直接使用来自GitHub公开仓库的概念验证（PoC）漏洞利用代码，针对真实企业目标发起攻击。

2026年4月2日，化名Nightmare-Eclipse（又称Chaotic Eclipse）的安全研究员在与微软安全响应中心（MSRC）就漏洞披露流程产生分歧后，在GitHub发布了BlueHammer漏洞利用工具。该0Day漏洞现被编号为CVE-2026-33825，利用Windows Defender签名更新工作流中的TOCTOU（检查时间与使用时间）竞争条件和路径混淆缺陷，使本地低权限用户可在完全打补丁的Windows 10/11系统上提升至SYSTEM权限。

##

**Part01**

## ****漏洞利用技术剖析****

该漏洞利用手法涉及微软 Defender 文件修复逻辑、NTFS连接点、Windows云文件API和机会锁（oplocks）之间的交互，无需内核漏洞利用或内存破坏。BlueHammer发布后不久，Nightmare-Eclipse又发布了两款工具：RedSun（可在Windows 10/11和Windows Server 2019上获取SYSTEM权限，甚至在4月补丁星期二更新后仍有效）和UnDefend（通过破坏Defender更新机制逐步削弱其防护能力）。

**Part02**

## ****Huntress确认实际攻击活动****

Huntress研究人员观察到攻击者正在实战中组合使用这三种技术。攻击载荷被部署在低权限用户目录中，特别是Pictures文件夹和Downloads目录下的两位字母子文件夹，使用的文件名与原始PoC仓库一致（FunnyApp.exe和RedSun.exe），部分样本被重命名为z.exe。

2026年4月10日检测到BlueHammer通过以下路径执行：

* C:\Users\[REDACTED]\Pictures\FunnyApp.exe

Windows Defender实时拦截并隔离了该文件，标记为Exploit:Win32/DfndrPEBluHmrBZ（严重级别）。威胁在UTC时间19:43:37被检测到，两分钟内完成隔离。

2026年4月16日记录的第二起事件涉及：

* C:\Users\[REDACTED]\Downloads\RedSun.exe

此次调用触发了Virus:DOS/EICAR\_Test\_File警报——这是RedSun攻击技术的故意设计，通过EICAR测试文件诱使Defender实时引擎进入可被操纵的检测-修复循环。此外还检测到次级进程Undef.exe以-agressive参数运行，作为Explorer.EXE下cmd.exe的子进程启动，被ThreatOps Hunting规则标记为高风险。

值得注意的是，两次攻击尝试都伴随手动枚举命令，包括：

* whoami /priv —— 枚举当前用户权限
* cmdkey /list —— 识别存储凭据
* net group —— 映射Active Directory组成员关系

这种攻击前侦察模式强烈表明攻击者属于具备针对入侵能力的熟练对手，而非机会性自动化攻击。

**Part03**

## ****补丁状态与缓解措施****

微软已在2026年4月补丁星期二更新中修复CVE-2026-33825（BlueHammer），但截至本文发布时RedSun和UnDefend仍未打补丁，数百万Windows系统持续面临风险。安全团队应立即：

* 部署所有2026年4月Windows安全更新
* 监控用户可写目录（Pictures、Downloads子文件夹）中的未签名可执行文件
* 对非管理进程投放EICAR测试文件的行为设置警报
* 在终端遥测数据中追踪whoami /priv、cmdkey /list和net group执行链
* 实施最小权限原则以限制漏洞利用所需的本地访问途径

**参考来源：**

Leaked Windows Defender 0-Day Vulnerability Actively Exploited in Attacks

https://cybersecuritynews.com/windows-defender-0-day-vulnerability-exploited/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1O8uucFibpl8PczsdFCl05VYJ6SAC0hbGnY2ORo3zp7cw9tGtthViaRCO0qTggMtiampGyl7T4RbMmFXECrOhAnNwzV3vBWEBFN0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337048&idx=1&sn=7238361cc36d8446dbd7c8ed85cb2f42&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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