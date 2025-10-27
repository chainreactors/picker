---
title: 【安全圈】微软 Win10 / Win11 新威胁：RID 劫持可提权至管理员控制你的 PC
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067606&idx=2&sn=efa053f9e1755bb17193b5a5868fb8ce&chksm=f36e7b56c419f24014b67943f6766ea3ab7b908882f20b4e0af01106172c63290014f9c24682&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-26
fetch_date: 2025-10-06T20:10:19.496283
---

# 【安全圈】微软 Win10 / Win11 新威胁：RID 劫持可提权至管理员控制你的 PC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgfD8qIW9YMJCTPkQt77totIUST2dlF24WraDR9A3CQpHgAiceqT2WFhqhTO9PZ2qhafkib9beBlfMw/0?wx_fmt=jpeg)

# 【安全圈】微软 Win10 / Win11 新威胁：RID 劫持可提权至管理员控制你的 PC

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

科技媒体 bleepingcomputer 昨日（1 月 24 日）发布博文，报道称黑客组织 Andariel 利用 RID 劫持技术，**欺骗 Windows 10、Windows 11 系统，将低权限账户视为管理员权限账户。**

注：RID 全称为 Relative Identifier，直译过来为相对标识符，隶属于 Windows 系统中安全标识符（SID），而 SID 是分配给每个用户账户的唯一标识符。

RID 的值指示账户的访问级别，例如管理员为 "500"，来宾账户为 "501"，普通用户为 "1000"，域管理员组为 "512"。

所谓的 RID 劫持，就是攻击者修改低权限账户的 RID，让其匹配管理员账户的 RID 值，Windows 系统就会授予其提升的访问权限。不过执行此攻击需要访问 SAM 注册表，因此黑客需要首先入侵系统并获得 SYSTEM 权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgfD8qIW9YMJCTPkQt77totOFZIlZTlu4tKO8HmAIyNa7ia3MBTIibUJB8hODlIJgKmibvXnjcWBM2Iw/640?wx_fmt=jpeg&from=appmsg)

博文详细介绍了 Andariel 的攻击流程如下：

Andariel 利用漏洞，获得目标系统上的 SYSTEM 权限。

他们使用 PsExec 和 JuicyPotato 等工具启动 SYSTEM 级别的命令提示符，实现初始权限提升。

虽然 SYSTEM 权限是 Windows 上的最高权限，但它不允许远程访问，无法与 GUI 应用程序交互，容易被检测到，并且无法在系统重启后保持。为了解决这些问题，Andariel 首先使用 "net user" 命令并在末尾添加 "'" 字符来创建一个隐藏的低权限本地用户。

这样，攻击者确保该账户无法通过 "net user" 命令看到，只能在 SAM 注册表中识别。然后，他们执行 RID 劫持以将权限提升至管理员级别。

Andariel 将他们的账户添加到远程桌面用户和管理员组。

通过修改安全账户管理器（SAM）注册表可以实现所需的 RID 劫持。黑客使用定制的恶意软件和开源工具来执行这些更改。

虽然 SYSTEM 权限允许直接创建管理员账户，但根据安全设置的不同，可能会有一些限制。提升普通账户的权限更加隐蔽，更难被检测和阻止。

Andariel 试图通过导出修改后的注册表设置、删除密钥和恶意账户，然后从保存的备份中重新注册来掩盖其踪迹，从而在不出现在系统日志的情况下重新激活。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgfD8qIW9YMJCTPkQt77totlCwPSD8w7JoLy7M9vu51Lf4Fiaa2xIvO9SHXnBzcsswanpaMdI4rhdQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgfD8qIW9YMJCTPkQt77totzkpcacGrs79AKsv1NE9S0UknLSYePw4kD7Yx0UqQmcuGnZdXV1Cia7g/640?wx_fmt=jpeg&from=appmsg)

为了降低 RID 劫持攻击的风险，系统管理员应该使用本地安全机构（LSA）子系统服务来检查登录尝试和密码更改，并防止对 SAM 注册表的未经授权的访问和更改。还建议限制 PsExec、JuicyPotato 和类似工具的执行，禁用 Guest 账户，并使用多因素身份验证保护所有现有账户。

***END***

阅读推荐

[【安全圈】斯巴鲁汽车漏洞让黑客利用 Starlink 远程控制数百万辆汽车](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067590&idx=1&sn=32ea96086da2a1f7d7b7c25530ca8d55&scene=21#wechat_redirect)

[【安全圈】GhostGPT – 黑客用来生成恶意软件和漏洞的新型 AI 黑帽工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067590&idx=2&sn=0963e1001cd7415a1987cb9c33807d8c&scene=21#wechat_redirect)

[【安全圈】思科曝9.9分关键权限提升漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067590&idx=3&sn=7379d9127186d37af92f08f7a9ced06e&scene=21#wechat_redirect)

[【安全圈】Chrome用户面临供应链攻击威胁，数百万人或受影响](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067590&idx=4&sn=ab568c073e0bfe554ca07ca03503f2da&scene=21#wechat_redirect)

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