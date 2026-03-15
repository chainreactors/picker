---
title: 【安全圈】3月漏洞风暴：思科48个洞、微软83个CVE，这个月不太平
url: https://mp.weixin.qq.com/s/0165k-v2sSdn2xy9uPUndg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:45.707277
---

# 【安全圈】3月漏洞风暴：思科48个洞、微软83个CVE，这个月不太平

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGFicnvwfc4p44rC6nlRibu8vTXhv7p01bEicHTMMrUOEJEH1pthoicQZo8lN4w6l7OqYyoQMUNibmTiaI0qOt2rfU7WvGTibuvxAUFB4/0?wx_fmt=jpeg)

# 【安全圈】3月漏洞风暴：思科48个洞、微软83个CVE，这个月不太平

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

> 2026年3月的安全圈，注定不太平。思科一次性修复48个漏洞，微软发布83个CVE，Chrome又被曝零日……这是什么概念？相当于安全团队还没喘过气来，下一轮攻击已经整装待发。安全圈的朋友们，这个月你们的补丁打得过来吗？

思科史上最大规模更新：2个CVSS 10.0漏洞

3月6日，思科发布了该公司有史以来最大规模的安全更新，一口气修复了防火墙产品线中的**48个安全漏洞**。这个数量直接刷新了思科产品安全更新的纪录。

但真正让人睡不着的是：这48个漏洞中，包含了**2个CVSS评分高达10.0的最高级别漏洞**。

什么是CVSS 10.0？这是通用漏洞评分系统（CVSS）中的最高等级，意味着这些漏洞可以被**无条件利用**，造成**灾难性后果**。换句话说，攻击者不需要任何身份验证，只要能访问到受影响的设备，就能为所欲为。

思科这次修复的漏洞涉及多个产品线，包括Firepower下一代防火墙、ASA防火墙等企业核心安全设备。安全圈内有句话：**思科的设备都敢出问题，那还有谁是安全的？**

微软3月补丁星期二：83个CVE + 2个零日

如果说思科的48个漏洞已经够刺激，那微软的3月更新更是重量级。

微软2026年3月安全更新共披露**83个漏洞**，其中：

* **7个高危**
* **76个严重**
* **2个零日漏洞**已被公开利用

重点漏洞包括：

* **Windows内核特权提升漏洞**
* **SMB服务器远程代码执行**
* **Winlogon提权漏洞**
* **SQL Server特权提升漏洞（CVE-2026-21262）**

更值得警惕的是，微软还修复了可通过**预览窗格**利用的Office漏洞，以及一个Excel信息泄露问题。安全研究人员指出，这个Excel漏洞可能会被滥用，通过**Copilot Agent模式外泄数据**——AI时代的数据泄露方式，又多了一种。

Chrome零日又被点名：CVE-2026-3909

还没完，Chrome用户也要注意了。

安全团队发现，Chrome浏览器中存在一个正在被积极利用的零日漏洞——**CVE-2026-3909**。这是Skia图形库中的越界写入漏洞，CVSS评分高达8.8分。

Skia是Chrome的核心2D图形引擎，一旦被攻破，攻击者可以：

* 在用户浏览器中执行任意恶意代码
* 窃取浏览器存储的敏感数据
* 配合其他漏洞实现更高权限的提升

Google已经紧急发布补丁，但可以预见的是，在补丁广泛部署之前，这个漏洞仍将是被重点利用的目标。

n8n工作流平台：4个严重漏洞可RCE

除了巨头们的漏洞，开源工具也没闲着。

工作流自动化平台n8n近日被披露存在**4个"严重"级别**的安全漏洞，其中最关键的是：

* **CVE-2026-27577**：表达式沙箱逃逸漏洞，允许认证用户通过精心构造的工作流参数在n8n主机上执行任意系统命令
* **CVE-2026-27493**：Form节点中的"双重评估"缺陷，公开表单无需认证即可被利用

这两个漏洞可以**链式利用**，意味着攻击者不需要任何账号，就能通过公开表单注入恶意代码，最终实现远程代码执行（RCE）。企业使用n8n做自动化运维的，这波必须立刻打补丁。

安全圈视角：漏洞爆发背后的趋势

**1. 攻击面持续扩大**

从防火墙到浏览器，从操作系统到企业应用，攻击者的可选目标越来越多。任何环节的疏漏都可能成为突破口。

**2. 漏洞利用门槛持续降低**

零日漏洞的活跃利用、PoC的快速传播，让即便是脚本小子也能造成实质性威胁。

**3. AI带来新的攻击面**

微软 Copilot Agent 模式的数据泄露风险预示着：AI工具正在成为新的攻击向量。

结语

**这个3月，安全圈注定是加班的一个月。**

思科的10.0漏洞、微软的83个CVE、Chrome零日、n8n RCE……一轮接一轮的补丁打下来，安全团队的神经已经绷到了极致。

但这也是常态。在网络安全这个领域，**永远没有绝对的安全，只有持续的对抗。**

各位安全圈的老铁们，补丁打起来，告警监控开起来，这个月咱们一起扛过去。

> *注：本文提及的漏洞详情和修复建议，请参考各厂商官方安全公告。*

***END***

阅读推荐

[【安全圈】涉及违规收集个人信息、窗口乱跳转，工信部通报 24 款 App 及 SDK](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074672&idx=1&sn=257b16999a2c0a4af4db096660acd6d7&scene=21#wechat_redirect)

[【安全圈】阿联酋国防部网络中心机密文件数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074672&idx=2&sn=0ccdef7c5a1b3ce01b4cfd8a8d22e057&scene=21#wechat_redirect)

[【安全圈】16 年心血归零！全球 PS 奖杯第一人账号遭索尼永久封禁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074672&idx=3&sn=52b9a55ed436e56880166d853ff4289b&scene=21#wechat_redirect)

[【安全圈】首批付费卸载龙虾的用户已出现，专家回应：卸载也难永绝后患](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074639&idx=1&sn=61b8b11214169b3c7accfb49dc75ce3b&scene=21#wechat_redirect)

[【安全圈】新型 “Zombie ZIP” 技术让恶意软件绕过安全工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074639&idx=2&sn=a9136aab554468e0643fa955a64f6248&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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