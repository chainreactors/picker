---
title: SilverFox黑客利用Go语言RAT+内核Rootkit发起多阶段渗透攻击
url: https://mp.weixin.qq.com/s/BCtolZMOGDAFZq0hw5q_Bw
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:02:20.861434
---

# SilverFox黑客利用Go语言RAT+内核Rootkit发起多阶段渗透攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3HaZibv2UXP5WfrxEo1DBu1OJM4IFpAq2noN8eRk3IAibm3GKicUAKIDRXHne17j9SJPM2VPp4M2J8Ura9tDA9fLOHcaQWYsPGWk/0?wx_fmt=jpeg)

# SilverFox黑客利用Go语言RAT+内核Rootkit发起多阶段渗透攻击

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3GueKo7bibyFgxO6WzuOaoBKngLPic7o8qRMdQlSV0IrichTicjhwNn6IJgwamyphGpnK39U7O01jZyo0FvNjauOskVZs3wsjiaBqM/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3PtHNXrG4YnvOaR7rbzTJataibaV0zbURia6hm3I9E0EmzlFes0ibwa8g4srun63hE0fYx2diaMhd329Ric6S52CkBhX5QEpGWJdq4/640?wx_fmt=png&from=appmsg)

Part01

新型多阶段攻击框架

一种新型远程访问恶意软件正悄然渗透企业网络，其行为模式完全颠覆了安全团队对该威胁组织的既往认知。这款被追踪为ValleyRAT的恶意软件由名为SilverFox的黑客组织部署，其最显著特征是采用前所未有的多阶段攻击链。与仅搭载单一有效载荷的常规远程访问木马（RAT）不同，ValleyRAT通过八个连续阶段实现设备完全控制，每个阶段都隐藏着下一阶段的触发机制，最终部署的内核级Rootkit甚至能直接接收来自RAT的指令。

Part02

隐匿技术深度剖析

这种分层架构绝非虚张声势。相比普通的信息窃取程序或后门，ValleyRAT的检测、分析和清除难度呈指数级上升，这也解释了为何该攻击活动能长期活跃而不被发现。Gen Threat Labs分析师在追踪异常安装程序时发现了该活动，这些安装文件会针对每个新受害者进行自我修改。研究人员指出，这是迄今为止对SilverFox工具链最清晰的观察案例。

攻击始于DLL侧加载技术，恶意文件通过合法签名应用程序作掩护。运行后，恶意软件会先禁用日志工具和杀毒扫描功能，随后将下一阶段有效载荷隐藏在看似普通的PNG图像像素数据中。这种基于隐写术的藏匿手段在攻击链中多次重复使用——在获取更高权限后，恶意软件会从第二张图像中提取新载荷，再通过名为Donut的内存加载器解压shellcode，该工具因能避免在磁盘留下明显痕迹而备受攻击者青睐。

Part03

复合型攻击武器库

ValleyRAT控制器随后会启动用Go语言编写的RAT模块，该组件通过WebSocket和QUIC协议与命令控制（C2）服务器通信，这些协议能轻易伪装成正常网络流量。RAT会将专门设计的杀毒软件禁用工具注入到svchost.exe（一个极少引发怀疑的核心Windows进程）中，最终安装支持65种以上指令代码的内核级Rootkit，通过命名管道接收RAT下发的指令。

Part04

数据窃取与持久化机制

除控制系统外，ValleyRAT还具备精密的数据窃取功能：实时监控剪贴板中的加密货币钱包地址，将其替换为攻击者控制的地址——这种手法在过往攻击中已悄无声息地转移了大量资金。恶意软件还会窃取受感染设备上的Telegram数据，获取私密对话和账户信息。更危险的是，攻击者能通过命名管道向已感染设备推送附加插件，实现攻击工具集的动态扩展。

在持久化方面，研究人员在12天内观测到13个经过多态变异的样本，每个样本的细微差异都能有效规避基于签名的检测。恶意文件每日在C:\Drivers目录下轮换路径，这种设计极大削弱了静态检测规则的有效性。攻击载体主要利用经过篡改的合法签名安装程序，借此绕过用户和安防软件对签名程序的默认信任。

Part05

防御建议与威胁指标

企业安全团队应重点监控以下异常行为：非常规的命名管道活动、svchost.exe进程下的异常子进程、以及不符合已知安全签名的安装程序。此案例警示我们：现代RAT已远非简单的远程控制工具，防御者必须应对多阶段加载器、基于图像的载荷隐藏、以及能与用户空间恶意程序直接交互的Rootkit等复合型威胁。

**攻击指标（IoCs）**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0qmFEKL7Wspg4o8m5llN0r67nFs2z22sQObIgrKaS4jx46AByuWIPd6ib8wXibYBvZN4jQ5ARQ2pk4vsfSNSHhug8sp22rEnTow/640?wx_fmt=png&from=appmsg)

（注：域名中的方括号为防误触设计，实际分析时需移除）

参考来源：

SilverFox Hackers Use Go RAT, AV Killer, and Kernel Rootkit in Live ValleyRAT Campaign

https://cybersecuritynews.com/silverfox-hackers-use-go-rat-av-killer/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0ctiaj5Z87Tg1RMJbr06lrE2fqlFoKFB0d4hx9AsKnZwJlVP4C7SBicZtVYotXf2IOL9UhETZBwFP2Q5D9A7vpdzWjR2M6r7abc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

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