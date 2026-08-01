---
title: 【安全圈】Unturned开源22天就爆RCE漏洞！创意工坊模组成攻击入口
url: https://mp.weixin.qq.com/s/moyCLhDg-kljP4sqlBaqDg
source: Doonsec's feed
date: 2026-07-31
fetch_date: 2026-08-01T05:09:25.390575
---

# 【安全圈】Unturned开源22天就爆RCE漏洞！创意工坊模组成攻击入口

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyEY1wOjySNRYKYKl2VIBff8mzzQFEJ9U1buqvCESGtmV7CukLAbmliaHLoxz1ZCXAvmhMm6qBqy32Ontjwqct2X9K84UyY2WWz4/0?wx_fmt=jpeg)

# 【安全圈】Unturned开源22天就爆RCE漏洞！创意工坊模组成攻击入口

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

🚨 想象一下：一款热门生存游戏刚刚开源，黑客们就像嗅到血腥味的鲨鱼一样蜂拥而至。这不是假设，而是正在发生的事情。

Steam平台上的经典僵尸生存游戏 **Unturned**，在7月7日开源仅22天后，就被发现存在通过创意工坊模组利用的**远程代码执行（RCE）漏洞**。攻击者可以利用这个漏洞在受影响的服务器上执行任意代码，后果不堪设想。

━━━━━━━━━━━━━━━━━

**📋 事件概述**

🎮 **游戏名称：**Unturned（Steam免费游戏）

📅 **开源时间：**2026年7月7日

🔓 **漏洞发现：**2026年7月30日（开源后仅22天）

🎯 **漏洞类型：**远程代码执行（RCE）

🔧 **修复版本：**3.26.3.6

👥 **GitHub仓库：**SmartlyDressedGames/U3-SDK（3,274 ⭐）

━━━━━━━━━━━━━━━━━

**⚡ 漏洞原理**

🔍 **攻击途径：**通过Steam创意工坊（Workshop）模组利用

🧠 **漏洞机制：**Unity事件系统（UnityEvent）的滥用

🎯 **利用方式：**攻击者通过创意工坊模组上传恶意预制件

💥 **危害：**在服务器上执行任意代码，完全控制系统

━━━━━━━━━━━━━━━━━

**💀 修复后遗症**

⚠️ **玩家无法加载服务器：**修复后验证过于激进，导致合法模组被误删

🔌 **创意工坊失效：**多个服务器报告创意工坊模组无法正常工作

🔄 **紧急补丁：**开发者SDGNelson在12小时内发布3.26.3.6补丁

👥 **社区协作：**多名开发者和玩家在GitHub上讨论修复方案

━━━━━━━━━━━━━━━━━

**🔍 技术分析**

1️⃣ **漏洞位置：**StaticUnityEventPrevention.Validate方法

2️⃣ **验证逻辑：**对Unity激活事件钩子进行安全检查

3️⃣ **误判问题：**GetComponents()在脚本缺失时返回null

4️⃣ **修复方案：**检查方法名是否为空，区分静态和动态调用

━━━━━━━━━━━━━━━━━

**💡 开源安全启示**

🔓 **开源≠安全：**代码公开反而让漏洞更容易被发现

👥 **社区响应：**白帽黑客和开发者快速协作修复

⏱️ **响应速度：**从漏洞发现到修复仅12小时

🛡️ **安全建议：**模组开发者需要遵循安全编码规范

━━━━━━━━━━━━━━━━━

💬 **编者按：**Unturned的开源安全事件为我们敲响了警钟：当游戏源代码公开后，安全研究人员和黑客都能更容易地分析代码寻找漏洞。这既是挑战也是机遇——漏洞被更快发现，但修复也更迅速。对于玩家来说，及时更新游戏、谨慎安装第三方模组是保护自己的关键。

🎮 **记住：安全不是一劳永逸的，而是持续迭代的过程。**

***END***

阅读推荐

[【安全圈】密码改了也没用！俄罗斯黑客用这招永久窃取邮箱](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078077&idx=1&sn=0f70e12e13f216d394d77f9f76129ea5&scene=21#wechat_redirect)

[【安全圈】Cisco 防火墙惊现后门，黑客登录只需一个密码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078077&idx=2&sn=f9c9a8e55b7db560ec392c85530a0c15&scene=21#wechat_redirect)

[【安全圈】30个水厂一夜瘫痪，美国供水系统遭毁灭性打击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078077&idx=3&sn=1b88cc217fba783a326bb5afe7e4f29a&scene=21#wechat_redirect)

[【安全圈】Check Point 紧急修复！认证绕过漏洞 PoC 已公开，CVSS 9.3](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078064&idx=1&sn=79d6a8b9aa80aaae459d916c7b6cb35a&scene=21#wechat_redirect)

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