---
title: 【安全圈】Ivanti VPN 零日漏洞正在被黑客利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067274&idx=3&sn=8eb5cc6c0a00bef351ca6ec387133310&chksm=f36e798ac419f09cca9472d89e0009706062cc803d7b61065e39083441ba8c9e646c932b6efe&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-12
fetch_date: 2025-10-06T20:09:29.887747
---

# 【安全圈】Ivanti VPN 零日漏洞正在被黑客利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljDjicoppMX1mCgRTtPTwDS2Bc6QjtENkWwTGyM3LTuGQgCiaGGPyLvj1sdzicD3KXic0rkyoMaf9XQ7A/0?wx_fmt=jpeg)

# 【安全圈】Ivanti VPN 零日漏洞正在被黑客利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

VPN

Ivanti 公开披露了影响 Connect Secure (ICS) VPN 设备的两个关键漏洞：CVE-2025-0282 和 CVE-2025-0283。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljDjicoppMX1mCgRTtPTwDS24XWGHXu2icjbCfotBo15qSZXwfGGOhaPaOcZhjTAWIGwhq7I0aWkkRQ/640?wx_fmt=jpeg&from=appmsg)

网络安全公司 Mandiant 的报告称，CVE-2025-0282 零日漏洞利用活动开始于 2024 年 12 月中旬。这一漏洞的利用引发了人们对潜在网络漏洞以及受影响组织后续损害的担忧。

比较而言，CVE-2025-0282 是两个漏洞中更为严重的一个，被描述为未经身份验证的基于栈的缓冲区溢出漏洞。

利用该漏洞，攻击者无需身份验证即可实现远程代码执行，从而为他们在受感染的网络中部署恶意软件或进行进一步攻击提供立足点。

CVE-2025-0283 的信息尚未完全披露，但同样被认为是关键漏洞。

Mandiant 的持续调查表明，CVE-2025-0282 正在被利用于针对多个组织的定向攻击活动中。

攻击者在发起攻击前展示了探测 ICS 设备版本的高超技术，特别是针对特定软件版本中的漏洞进行攻击。

Mandiant 观察到威胁行为者利用了一系列恶意软件家族，包括已知的 SPAWN 生态系统（SPAWNANT 安装程序、 SPAWNMOLE 隧道工具和 SPAWNSNAIL SSH 后门）。

在受感染的设备中还识别出了两个新的恶意软件家族：DRYHOOK 和 PHASEJAM。

## **攻击技术和持久化方法**

攻击者在利用 CVE-2025-0282 时典型的攻击步骤包括禁用 SELinux 等安全功能、写入恶意脚本、部署 Web Shell 以及篡改系统日志以隐藏入侵痕迹。

特别令人担忧的是，攻击者植入了在系统升级后仍然能够存活的持久化恶意软件组件，确保即使系统被修补，攻击者仍能保持访问权限。

分析还揭示了攻击者在 ICS 软件组件中部署了 Web Shell，以实现远程访问和代码执行。

例如，PHASEJAM 恶意软件会劫持系统升级过程，利用基于 HTML 的虚假升级进度条，从视觉上让管理员误以为升级正在进行。实际上，恶意行为者会悄悄阻止合法升级，确保系统仍然受到入侵威胁，同时保持攻击不被发现。

另一种恶意软件 SPAWNANT 则通过将自身嵌入系统文件来确保升级过程中的持久性。

在漏洞利用后，还观察到威胁行为者从设备的多个关键区域删除了入侵证据：

* 使用 dmesg 清除内核消息，并从调试日志中删除漏洞利用期间生成的条目
* 删除故障排除信息包（状态转储）以及进程崩溃生成的任何核心转储
* 删除与系统日志故障、内部 ICT 故障、崩溃痕迹和证书处理错误相关的应用程序事件日志条目
* 从 SELinux 审计日志中删除已执行的命令

## **幕后黑手是谁？**

##

Ivanti 和 Mandiant 认为此次攻击活动带有间谍活动的痕迹。

受感染的 ICS 设备数据库缓存已多次被泄露，这引发了人们对暴露的 VPN 会话数据、 API 密钥、凭证和证书的担忧。

网络安全专家警告称，如果这些漏洞的概念验证利用代码被公开，可能会吸引更多威胁行为者参与，从而导致攻击的范围扩大。

## **Ivanti 对零日漏洞的响应**

Ivanti 正在处理零日漏洞 CVE-2025-0282 和 CVE-2025-0283，这两个漏洞影响了 Ivanti Connect Secure 、Policy Secure 以及 Neurons for ZTA 网关。

修复程序可以通过下载门户获取。

***END***

阅读推荐

[【安全圈】日本炒作“中国疑似参与黑客攻击”，外交部：日方判断既不专业也不负责任](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067255&idx=1&sn=a41ccbc8f9fc9de8ed0dfe5c7a296033&scene=21#wechat_redirect)

[【安全圈】数百万电子邮件服务器因缺少 TLS 加密而暴露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067255&idx=2&sn=c42d9289f9097a99b0e9de5638c25da5&scene=21#wechat_redirect)

[【安全圈】超4000个Web后门通过注册过期域名被劫持](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067255&idx=3&sn=12454a2419a60abfe0219df1db8fc9ff&scene=21#wechat_redirect)

[【安全圈】联合国航空机构确认招聘数据库存在安全漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067255&idx=4&sn=3fd244b5403280e26cbc308f9d938be2&scene=21#wechat_redirect)

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