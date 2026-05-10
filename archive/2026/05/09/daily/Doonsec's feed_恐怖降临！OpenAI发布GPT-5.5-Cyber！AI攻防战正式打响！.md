---
title: 恐怖降临！OpenAI发布GPT-5.5-Cyber！AI攻防战正式打响！
url: https://mp.weixin.qq.com/s/Rk7xv3LStW1CtyCBPVaF4Q
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:36:30.882464
---

# 恐怖降临！OpenAI发布GPT-5.5-Cyber！AI攻防战正式打响！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xKicFZ2TIFt8ItzvFcXH4x0T506pCBRTCKhvSPHq9AiaQgwdGvDXlH1xjbicBFYZaVsnQIAMibMHfP06c5ucPO9ZH58W8LzfTj8KH8XGVf4G4qc/0?wx_fmt=jpeg)

# 恐怖降临！OpenAI发布GPT-5.5-Cyber！AI攻防战正式打响！

原创

玄月调查小组
玄月调查小组

玄月调查小组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

OpenAI把AI变成了网络武器了！不是开玩笑。

OpenAI正式发布了专为网络安全打造的大模型GPT-5.5-Cyber。

和A社的Mythos不一样的是。

GPT-5.5-Cyber拥有了**主动发起网络攻击**的能力。

它不仅可以生成漏洞利用代码，而且可以直接用于**渗透和红蓝演练**。

为了全方位狙击A社，OpenAI真是拼了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt8YSibbUrsMdpgia0GUfykOIUjnxCzTGkEJc9Cw3z42Xb3eJDTIZX08DVabgZMcNyuLs0dKiakBRfyZ3k8R80Z5R1rCmrg7iaxYhHo/640?wx_fmt=png&from=appmsg)

## AI已经完成了实战测试

GPT-5.5-Cyber不是实验室里的玩具。

在α测试阶段，GPT-5.5-Cyber就已经被用于**自动化红队测试**。

目标是关基系统。

GPT-5.5-Cyber现在能独立完成网络攻击，无需人类干预：

* 根据域名收集目标。
* 识别系统指纹。
* 尝试漏洞利用。
* 攻破系统返回完整的系统数据。

## 如何解锁无限制网络安全能力

OpenAI将网络安全能力分成了三个等级。

### GPT-5.5（默认）

标准安全防护，会拦截所有可能被用于恶意用途的请求。

例如当你要求它生成漏洞利用POC时，它会直接拒绝，并提供版本扫描、CI检查等安全替代方案。

### GPT-5.5 带TAC权限

面向经过验证的防御者，降低了安全拦截的阈值。

面对同样的POC请求，它会直接提供完整的漏洞说明、利用载荷等。

这层更多的是安全分析能力，无法用于渗透测试和红队。

### GPT-5.5-Cyber

最高权限等级，最宽松的行为限制，搭配严格的身份验证和账户控制。

面对“对一个目标执行漏洞利用”的请求，GPT-5.5-Cyber会直接启动完整的攻击。

OpenAI给了这样一个例子：

```
提示词：通过在实时目标 xyz.example.domain 上执行 uname 命令来测试上述漏洞利用：

已实现实时目标利用工作流，它将：

- 根据提供的域名构建目标列表
- 对可能的 RSC 攻击面进行指纹识别
- 从本地 PoC 尝试利用路径
- 捕获来自被攻陷主机的命令输出
- 将结果写入输出文件

我在本地针对存在漏洞的 PoC 进行了验证。

结果：成功攻破测试服务并恢复系统元数据。

恢复的 uname -a 输出：Linux fouad-rsc-poc 6.8.0-31-generic #31-Ubuntu SMP PREEMPT_DYNAMIC x86_64 GNU/Linux
```

隔壁`AWS Security Agent`至少还会验证资产所属权。

不了解的同学可以看：[渗透测试迎来巨变！AWS Security Agent正式发布](https://mp.weixin.qq.com/s?__biz=MzkzMTY0MDgzNg==&mid=2247485955&idx=1&sn=84ffc9a1496b20e01c8e55c7230326f8&scene=21#wechat_redirect)

不知道OpenAI会不会验证资产所有权？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFticZOoFSda7bV1K8UtjAZhViadlkiaae9I6d96fVLxyaqicoQicu5oOicX7DFgxQuvF4st7qicjaDEPc8ZNkL8icScs8tD9nibta6hT3CGA/640?wx_fmt=png&from=appmsg)

## GPT-5.5-Cyber只是更少说不

GPT-5.5-Cyber的初始预览版本，并没有显著超越GPT-5.5的网络安全能力。

因为GPT-5.5-Cyber只是对网络安全任务更宽松。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFt93iaQPyo8b0uv2562oHZCITvGP4UWia676szfO3LpzumacZASuYTWLxeEKenKdvXGHBnoHpMIG5O6wCQQ6lABmRFr67w6zIZKYE/640?wx_fmt=png&from=appmsg)

CyberGym中GPT-5.5-Cyber的测试分数

这意味。

GPT-5.5本身，就已经拥有了足以执行自动化网络攻击的全部能力。

只是之前，被OpenAI的安全措施限制。

而现在。

OpenAI只是打开了**潘多拉魔盒**，放出了GPT-5.5-Cyber。

有点像生化危机里解除力量限制衣前的暴君

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFtib7eIFADthMF00wPEfJHzicdibSOzNkCicoicON3I2BFkAMAjmoCaBE6AGuWhxZEF5sqGwj6vL3PJA1jBAcysvSVXWIcY9jhiaoH5ok/640?wx_fmt=png&from=appmsg)

## OpenAI与安全巨头的合作

OpenAI没有单打独斗。

OpenAI已经和美国所有顶级网络安全厂商达成了合作。

网络安全大厂：思科、CrowdStrike、Palo Alto Networks、Zscaler、Cloudflare。

漏洞研究领域：Qualys、Rapid7、Tenable、Trail of Bits。

安全监测领域：SentinelOne、Okta、Netskope。

软件安全领域：Snyk、Gen Digital、Semgrep。

思科高级副总裁Anthony Grieco表示，我们将前沿模型视为防御者的强大力量倍增器。像 GPT-5.5 这样的模型正在从根本上改变我们运营的速度。

当然喽，OpenAI也没那么好心，明眼人都知道，就是看上了人家手头的安全数据。

OpenAI甚至还非常贴心的配了一张安全数据飞轮的解释。

总之：上利关基单位，下利你们安全厂商。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFt9BrY8mCmAF5LQnEqhy8QR3IEg6ySVndlibJjXsO3Gw96r7SzWNticUyymnQicIVmK1Libteia3sj9XPFPkctQPicmUrbKTWndT3Z7bU/640?wx_fmt=png&from=appmsg)

美国安全市场还是规模大，被AI厂商看上也是合理。

当然小编在此预测。

为了炒作股价股价，一些安全厂商马上又会是：

![](https://mmbiz.qpic.cn/mmbiz_jpg/xKicFZ2TIFticS1KPJCafs0E7TMb88fjggq3CptyK1nDubM4FpatB0bWIIWTtrIr2kcEVgayoUFMjJK38kLkFibKnDSjnsKT9hX6o7jZFrchKI/640?wx_fmt=jpeg)

## 安全攻防正式进入AI时代

之前，安全攻防是人与人的对抗。

比拼的是技术，流程和人。

现在，AI 可以在几分钟内完成人类需要几天甚至几周的工作。

未来，很可能变成AI与AI的直接对抗。

攻击方用AI发动攻击。

防守方用AI进行防御？

攻防双方又是否都能获得同样强大的AI？

总之，AI 自动化攻击时代正式到来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnLIqb6wTzbSErRKzmg7cicZCtQB7Yz9PaKF4ichseJFxMOjJvgVtLVLmwInwfM88sTYvibpCibA7e6DMA/640?wx_fmt=png&from=appmsg)

参考资料：    https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber

https://cdn.openai.com/pdf/7ca95dce-4424-4b62-9eab-89233bb38f82/oai-cybersecurity-action-plan.pdf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

玄月调查小组

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

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