---
title: 趋势科技披露针对亚洲政府、北约、记者和活动人士的黑客活动
url: https://mp.weixin.qq.com/s/u-4nUK-Fa92UV14v6zJkmw
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:27:50.614946
---

# 趋势科技披露针对亚洲政府、北约、记者和活动人士的黑客活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PaFY6wibdwyLn8BDJlWRV7xnpVWQAAkjBSibtf2CLSAdeNPmeFgcs3jaMSvs3GCaUibI2qcp2UPJCxyjVibh6RmYaConIZOzHbGj5L5Sosqmicqc/0?wx_fmt=jpeg)

# 趋势科技披露针对亚洲政府、北约、记者和活动人士的黑客活动

会杀毒的单反狗
会杀毒的单反狗

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

趋势科技安全研究人员披露一项新的间谍活动细节，该活动针对南亚、东亚和东南亚地区敏感部门，以及一个属于北约的组织。Trend Micro 将此活动归因于命名为 SHADOW-EARTH-053 的威胁组织。

趋势科技将此次活动归因于其追踪的威胁活动集群，该集群的临时名称为SHADOW-EARTH-053 。据评估，该组织至少从 2024 年 12 月起就一直活跃，并且与CL-STA-0049、Earth Alux 和 REF7707存在一定程度的网络重叠。

安全研究人员 Daniel Lunghi 和 Lucas Silva 在一份分析报告中指出：“该组织利用面向互联网的 Microsoft Exchange 和 Internet 信息服务 (IIS) 服务器中的Nday漏洞（例如ProxyLogon链），然后部署 web shell（Godzilla）以实现持久访问，并通过 DLL 侧加载合法签名的可执行文件来植入ShadowPad 。 ”

这些攻击活动的目标包括巴基斯坦、泰国、马来西亚、印度、缅甸、斯里兰卡、波兰和其他敏感地区。

趋势科技表示，他们观察到近一半的 SHADOW-EARTH-053 目标此前也曾受到名为 SHADOW-EARTH-054 的相关入侵集的攻击，尽管没有发现直接的行动协调证据。

攻击的起点是利用已知的安全漏洞入侵未打补丁的系统，并投放类似 Godzilla 的 Web Shell，从而实现持久远程访问。这些 Web Shell 作为命令执行的载体，能够进行侦察，并最终通过 AnyDesk 部署 ShadowPad 后门。该恶意软件通过 DLL 侧加载的方式启动。

至少在一个案例中，React2Shell（CVE-2025-55182）的武器化据称促成了Linux版Noodle RAT（又名ANGRYREBEL和Nood RAT）的传播。谷歌威胁情报小组（GTIG）已将此攻击链与一个名为UNC6595的组织联系起来。

![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyJ8CibK1BgV1VLFpibHhtnqaP7FhPIVoHKEydg1CeU3U5kgOur3pgAOm28VfkFsfBibR7xicyju5IMfVwJzKR0hhNctib9crPibE9s8o/640?wx_fmt=png&from=appmsg)

此外，攻击者还利用了开源隧道工具，例如 IOX、GO Simple Tunnel (GOST) 和 Wstunnel，以及RingQ来打包恶意二进制文件并逃避检测。

为了方便权限提升，SHADOW-EARTH-053 被发现使用了 Mimikatz，而横向移动则通过一个名为Sharp-SMBExec的自定义远程桌面协议 (RDP) 启动器和 SMBExec 的 C# 实现来实现。

趋势科技表示：“此次攻击活动的主要入口点是面向互联网的IIS应用程序中的漏洞。各组织应优先为Microsoft Exchange以及托管在IIS上的任何Web应用程序应用最新的安全更新和累积补丁。”

技术报告：

https://www.trendmicro.com/en\_us/research/26/d/inside-shadow-earth-053.html

新闻链接：

https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

军哥网络安全读报

**讲述普通人能听懂的安全故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

爱拍照的老李

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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