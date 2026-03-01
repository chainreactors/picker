---
title: 热门游戏工具隐藏恶意软件？电脑或被远程操控
url: https://mp.weixin.qq.com/s/mXaqWe4KzTetOYPej53dzg
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:16:04.230600
---

# 热门游戏工具隐藏恶意软件？电脑或被远程操控

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ricqMN2UMva5V0FpD3YgSdq0IVIvtzY57gxIqzKwFmSc6PLH3ha348Eztf1DYwToNczMOhhaKQ4qNMYiak60gxyQymAVkrxyzgtzXK2icmP9qM/0?wx_fmt=jpeg)

# 热门游戏工具隐藏恶意软件？电脑或被远程操控

HackerNews
HackerNews

安全威胁纵横

![]()

在小说阅读器中沉浸阅读

高危漏洞

**紧急修复指南**

RCE Patch

网络犯罪分子找到了绕过用户防御的新方法 —— **将恶意软件隐藏在看似正常的游戏工具中**。微软安全团队发现一项活跃攻击活动，攻击者向毫无防备的用户**分发热门游戏工具的木马化版本**。

推测e

这些伪造工具一旦运行，会静默部署远程访问木马（RAT），使攻击者获得对受感染主机的完全无限制控制权。

该攻击活动标志着威胁行为者的攻击方式发生明显转变，他们利用日常软件攻击范围更广、警惕性更低的受害者群体。

恶意软件通过浏览器和聊天平台传播，用户极易在不知情的情况下下载并运行受感染文件。

该活动中使用的两个主要文件名为 Xeno.exe 和 RobloxPlayerBeta.exe，选择这些名称是因为它们对游戏玩家而言看起来熟悉且完全可信。

通过针对游戏社区，攻击者赌定年轻用户或休闲用户对运行从聊天群或非正规第三方网站下载的可执行文件警惕性较低。

该手段有效降低受害者警惕性，并显著提升攻击者的整体成功率。

微软威胁情报分析师识别出该恶意软件并追踪其完整攻击链，揭示出一个经过精心策划的多阶段感染流程。

研究人员指出，最终载荷是一种多功能威胁，可同时充当加载器、执行器、下载器和 RAT。

这种组合能力使其远胜于单纯的数据窃取工具，攻击者可随时利用其安装更多恶意软件、执行远程命令并窃取敏感信息。

该攻击活动的影响十分严重，不可低估。

一旦 RAT 成功安装，攻击者通过 IP 地址为 79.110.49 [.] 15 的命令与控制（C2）服务器连接受害者主机。从此时起，受攻陷系统完全处于攻击者控制之下。

主机上的个人文件、登录凭据以及所有存储或输入的数据均可被静默窃取，用户毫无察觉。

对于员工可能使用个人设备办公的机构而言，该威胁会造成严重且深远的后果。

**0****1**

**感染机制与持久化手段**

该攻击活动的巧妙之处在于恶意软件的自安装方式及规避安全工具检测的手段。

受害者运行木马化游戏工具后，恶意下载器会在主机上静默部署便携式 Java 运行环境，随后执行名为 jd-gui.jar 的恶意 Java 归档文件。

使用便携式 Java 运行环境意味着攻击者无需受害者设备预先安装 Java，恶意软件自带所需全部组件。

为避免被检测，下载器采取多项谨慎措施。它利用 PowerShell 及系统自带工具（LOLBins）—— 特别是合法 Windows 工具 cmstp.exe—— 以融入正常系统活动的方式执行代码。

下载器完成任务后会自删除，以清除在系统中的所有痕迹。攻击者还直接在 Microsoft Defender 中为 RAT 组件添加排除项，实质上让安全工具完全忽略恶意文件。

为确保恶意软件在系统重启后依然运行，攻击者创建了计划任务和名为 world.vbs 的启动脚本。

这些持久化机制确保 RAT 在每次系统启动时运行，为攻击者在受感染系统中提供稳定持久的立足点。

机构与个人用户应采取以下措施防御该威胁：

* 拦截或监控指向已知恶意域名与 IP 地址的外连流量，并对**从非企业来源下载 java [.] zip 或 jd-gui.jar 设置告警**。
* 利用 EDR 遥测数据在终端中检索相关进程与组件。
* 审计 Microsoft Defender 排除项与计划任务，**排查可疑或随机命名条目，并删除恶意任务与启动脚本**。

* 发现受影响终端后**立即隔离**，收集 EDR 遥测数据，并重置受攻陷主机上所有活跃用户的凭据。

入侵指标（IOC）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ricqMN2UMva7U7EUp6ZgRvZAMFxpXdj55Jg36vv6vUl0cicyaVwugj4fyWbIk9CjVPDFUbyvp19UcbR6Qjwiaich6OObzNRc755wwibEy5cJBMwM/640?wx_fmt=png&from=appmsg)

转载请注明出处@安全威胁纵横，封面来源于网络；

**消息来源：https://cybersecuritynews.com/microsoft-defender-uncovers-trojanized-gaming-utility-campaign/**

更多网络安全视频，请关注视频号“知道创宇404实验室”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAEhiaraapUTicic4reqx4oC5ssbTLiauoq7YZl4nnCOPicsCDHZzINJibpc5ck9YEpe1cqgLJ7mbWM7TpZw/0?wx_fmt=png)

安全威胁纵横

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAEhiaraapUTicic4reqx4oC5ssbTLiauoq7YZl4nnCOPicsCDHZzINJibpc5ck9YEpe1cqgLJ7mbWM7TpZw/0?wx_fmt=png)

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