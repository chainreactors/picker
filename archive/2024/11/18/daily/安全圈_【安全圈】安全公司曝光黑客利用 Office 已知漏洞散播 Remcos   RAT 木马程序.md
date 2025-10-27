---
title: 【安全圈】安全公司曝光黑客利用 Office 已知漏洞散播 Remcos   RAT 木马程序
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=2&sn=cf11d094cb7fc2770df2100227dc34db&chksm=f36e7cb8c419f5ae9268e1d2eb9675ef94bccbcfe66627cb209b0883944215f205a8d17b7028&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-18
fetch_date: 2025-10-06T19:14:54.045128
---

# 【安全圈】安全公司曝光黑客利用 Office 已知漏洞散播 Remcos   RAT 木马程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaZ8picWZtpojNtG0Sd01FibnJfMYGAHLibBRiaWVUljibteic0PDeBBAhlybAgPn7WwL8aqgV47edjuPRw/0?wx_fmt=jpeg)

# 【安全圈】安全公司曝光黑客利用 Office 已知漏洞散播 Remcos RAT 木马程序

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

安全公司 Fortinet 发布报告，称最近有黑客利用 5 年前公布的 CVE-2017-0199 漏洞，瞄准 Office 企业用户发动攻击。

IT 之家参考报告获悉，相关黑客首先发送一批伪造成公司业务往来信息的网络钓鱼邮件，其中带有含有木马的 Excel 附件。一旦收件人打开附件，就会看到相关文件受到保护，要求用户启用编辑功能才能查看内容，**在用户点击 " 启用编辑 " 按钮后，便会触发 CVE-2017-0199 远程代码执行漏洞**，之后受害者设备便会在后台自动下载运行黑客预备的 HTML 文件（HTA）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaZ8picWZtpojNtG0Sd01FibntdwCMLv7WI6KKEdJSxwQ6X3oFicRVibslZKCMTLMJsyz2vXsfpeS4BOQ/640?wx_fmt=jpeg&from=appmsg)

▲ 黑客制造的虚假邮件

值得注意的是，这一 HTA 文件据称使用 JavaScript、VBScript 等脚本并结合 Base64 编码算法和 PowerShell 命令进行多层包装以避免被安全公司发现。一旦 HTA 文件被启动，它会将黑客预备的 dllhost.exe 下载到受害者设备上运行，而后相关 exe 文件会将恶意代码注入到一个新的进程 Vaccinerende.exe 中，从而传播 Remcos RAT 木马。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaZ8picWZtpojNtG0Sd01Fibnjba3tgzuUfmjTDhNWfLSuJiaSRibnia2tiaeYtdWOILUibeSRogo8OYdM7Q/640?wx_fmt=jpeg&from=appmsg)

▲ 黑客的 HTA 文件采用多重包装以防止遭到安全公司分析

研究人员指出，黑客为隐藏其踪迹利用了多种反追踪技术，包括 " 异常处理 "、" 动态 API 调用 " 等手段，以达到规避检测的目的。就此，安全公司提醒企业及用户个人应及时更新 Office 软件，降低被黑客攻击的风险。

***END***

阅读推荐

[【安全圈】手机主板植入恶意软件，98万部手机被远程操控！他在深圳被抓](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=1&sn=1f067ab157601babcd85f75fb2d922a9&chksm=f36e7ca8c419f5be9fff3e8d1553cb7aebf180697c5d3b407014247a0aa1cbbba084b9acb79c&scene=21#wechat_redirect)

[【安全圈】非法购买38万条个人信息获利 获刑3年1个月](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=2&sn=0992fce67c63d8241382ad131084b639&chksm=f36e7ca8c419f5be90f76bf60938259deed1098709925a964d4699975ce428aefef533f804a3&scene=21#wechat_redirect)

[【安全圈】利用“爬虫”技术非法抓取电商数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=3&sn=168ceadc13c78d0c128517b6cfe7df0b&chksm=f36e7ca8c419f5bedf9c689eb7c76cd562abee0f8331f373e8494d8f1cf80322fb0b68c56086&scene=21#wechat_redirect)

[【安全圈】俄罗斯黑客利用文件拖放、删除操作触发 Windows 0day 漏洞攻击乌克兰目标](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=4&sn=46592438737abae8701b9ba1b7160d86&chksm=f36e7ca8c419f5be0b5de8218474b566a05a2871e02c5f1b86f0a13769a0651d6087bd35a84d&scene=21#wechat_redirect)

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