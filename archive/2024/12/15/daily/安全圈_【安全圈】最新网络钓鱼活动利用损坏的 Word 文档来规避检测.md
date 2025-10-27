---
title: 【安全圈】最新网络钓鱼活动利用损坏的 Word 文档来规避检测
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066606&idx=3&sn=d6db5800165d61a841b21b917d975bde&chksm=f36e7f6ec419f6787f017edfcbed384c8dad810704e071c9c8471adc69f4aa635df0e747e56c&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-15
fetch_date: 2025-10-06T19:38:02.983757
---

# 【安全圈】最新网络钓鱼活动利用损坏的 Word 文档来规避检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljYiaSm3aibFgF6YGfcwfc1FpO2NTE08fnnh0qcBpSmT3f9ptMULSegUjKgRANG3icicWXibGqvm1oe9Wg/0?wx_fmt=jpeg)

# 【安全圈】最新网络钓鱼活动利用损坏的 Word 文档来规避检测

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络钓鱼

新出现的网络钓鱼攻击滥用 Microsoft 的 Word 文件恢复功能，将损坏的 Word 文档作为电子邮件附件发送，使它们能够绕过安全软件，但仍可由应用程序恢复。

威胁者不断寻找新方法来绕过电子邮件安全软件并将网络钓鱼电子邮件放入目标的收件箱中。恶意软件狩猎公司 Any.Run 发现了一种新的网络钓鱼活动，利用故意损坏的 Word 文档作为电子邮件中的附件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljYiaSm3aibFgF6YGfcwfc1FpdGsxDLEtnKaogO37vgLAF3cZujV17te7RJs4zOsiaX4YbfOc5Zvq1wg/640?wx_fmt=jpeg&from=appmsg)

网络钓鱼电子邮件

这些附件使用广泛的主题，几乎全部围绕员工福利和奖金。打开附件时，Word 将检测到文件已损坏，并指出它在文件中 " 发现不可读的内容 "，询问您是否要恢复它。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljYiaSm3aibFgF6YGfcwfc1FpTBSy59UaP2lPiaSsrmvIEAic5T92lvZgvkaNwVibI5RHLvWL03J8heBlQ/640?wx_fmt=jpeg&from=appmsg)

通过网络钓鱼电子邮件发送的 Word 文档已损坏

这些网络钓鱼文档的损坏方式很容易恢复，并显示一个文档，告诉目标扫描二维码以检索文档。如下所示，这些文档都带有目标公司的徽标，例如下面所示的示例：

修复后的 Word 文档

扫描二维码会将用户带到一个冒充 Microsoft 登录名的钓鱼网站，试图窃取用户的凭据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljYiaSm3aibFgF6YGfcwfc1FpOMlEC7K1cOodojwUfeCTcwZnee4icib1sOjicrUDXKm1QPMxNYmYoko2Q/640?wx_fmt=jpeg&from=appmsg)

网络钓鱼页面窃取 Microsoft 凭据

虽然这种网络钓鱼攻击的最终目标并不新鲜，但它使用损坏的 Word 文档是一种逃避检测的新策略。尽管这些文件在操作系统中可以成功运行，但由于未能对其文件类型应用正确的程序，大多数安全解决方案仍然无法检测到它们。

它们已上传到 VirusTotal，但所有防病毒解决方案都返回 " 干净 " 或 " 未找到项目 "，因为它们无法正确分析该文件。因此，这些附件相当成功地实现了他们的目标。

从附件来看，几乎所有附件在 VirusTotal 上的检测量都是零 [ 1,2,3,4 ] ，只有一些 [ 1 ] 由 2 个供应商检测到。同时，这也可能是由于文档中没有添加恶意代码，仅显示二维码所致。一般规则仍然适用于保护用户免受网络钓鱼攻击。

如果收到来自未知发件人的电子邮件，尤其是包含附件的电子邮件，应立即将其删除或在打开之前与网络管理员确认。

***END***

阅读推荐

[【安全圈】俄罗斯完成断开国际互联网测试 持续24小时完全无法访问国际互联网](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066594&idx=1&sn=108b48500d4663a7195c6641fa5dbec1&scene=21#wechat_redirect)

[【安全圈】大众和斯柯达曝12个组合漏洞，攻击者可在10米内无接触入侵](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066594&idx=2&sn=b944b25addf57bec5231e17520c14d2c&scene=21#wechat_redirect)

[【安全圈】关键的Windows UI自动化框架漏洞允许黑客绕过EDR](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066594&idx=3&sn=fb1485e3b4a0ed439c616f967bfc2543&scene=21#wechat_redirect)

[【安全圈】Ivanti最严重的 CSA 认证绕过漏洞曝光](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066594&idx=4&sn=b010357e9e80003c07a80b440507c355&scene=21#wechat_redirect)

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