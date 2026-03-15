---
title: 【安全圈】紧急预警！Chrome再曝两个高危漏洞已被在野利用
url: https://mp.weixin.qq.com/s/oaK2D4KUDIzynzoelSOZbw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:42.402608
---

# 【安全圈】紧急预警！Chrome再曝两个高危漏洞已被在野利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFIzE3zVTb0po1qu8qicl1icT3AOicDprQhjXFszkra5Iic4BL6nkbAecsxiazH3rTzHlzsibfzxopjXQbyPyQmeFiaxGhz4rdsf2PUQA/0?wx_fmt=jpeg)

# 【安全圈】紧急预警！Chrome再曝两个高危漏洞已被在野利用

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Chrome漏洞

**就在刚刚，CISA出手了。**

3月13日，美国网络安全和基础设施安全局（CISA）直接将两个Chrome漏洞加入**已知利用漏洞（KEV）目录**。

这意味着什么？

**这两个漏洞，已经在真实攻击中被利用。**

---

漏洞详情

### CVE-2026-3909：Skia越界写入

* **影响范围**：Chrome < 146.0.7680.75
* **严重程度**：高危（CVSS未公开，但被CISA点名）
* **漏洞类型**：越界写入（Out of bounds write）
* **危害**：攻击者可通过精心构造的HTML页面，执行越界内存访问

### CVE-2026-3910：V8沙箱逃逸

* **影响范围**：Chrome < 146.0.7680.75
* **严重程度**：高危（CVSS 8.8）
* **漏洞类型**：V8引擎不当实现缺陷
* **危害**：攻击者可绕过沙箱限制，在受影响系统上执行任意代码

为什么这次特别严重？

**1. CISA亲自背书**

CISA将这两个漏洞列入KEV目录，意味着联邦机构必须立即修复。这是CISA对漏洞利用紧迫性的最高级别认定。

**2. 浏览器漏洞杀伤力极强**

Chrome是全球使用率最高的浏览器。一旦用户访问恶意页面，攻击者即可获取系统控制权，全程无需用户交互。

**3. 在野利用确认**

CISA不会轻易把漏洞列入KEV。这次行动说明，这两个漏洞的真实攻击案例已经出现。

---

影响范围

* 所有Chrome用户（桌面版）
* 基于Chromium的浏览器（Edge、Brave、Opera等）可能受影响
* Windows、macOS、Linux全平台

安全圈建议

### 立即行动

1. **立即更新Chrome**至最新版本（146.0.7680.75或更高）
2. 启用浏览器的**自动更新**功能
3. 提醒身边亲友尽快升级

### 企业用户

* 将CVE-2026-3909和CVE-2026-3910加入漏洞应急清单
* 通过终端管理平台批量推送Chrome更新
* 监控是否有异常的网络活动

---

延伸阅读：本周其他高危漏洞

本周安全圈不太平，除了Chrome，还有这些漏洞值得关注：

| 漏洞编号 | 产品 | 危害 |
| --- | --- | --- |
| CVE-2026-27577 | n8n工作流平台 | 远程代码执行 |
| CVE-2026-23662 | Azure IoT Explorer | 身份验证缺失 |
| CVE-2026-28710 | Acronis Cyber Protect | 弱认证机制 |

---

> **关键不是修复一个漏洞，而是建立持续更新的安全习惯。**

Chrome漏洞不是第一次，也不会是最后一次。

**今天的补丁，就是明天的防线。**

---

*本文由安全圈整理，转载需授权。*

**转发提醒：务必提醒身边人更新Chrome！**

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