---
title: 【安全圈】黑客在HuggingFace上传包含恶意代码的AI模型对开发者展开攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067721&idx=3&sn=e5e71e4b9b41dab1cc4c012bcce9bb59&chksm=f36e7bc9c419f2df607b73260b05a18d1568a973f3bf4ef39f907f48f4256fa81aa4051de938&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-10
fetch_date: 2025-10-06T20:37:09.205194
---

# 【安全圈】黑客在HuggingFace上传包含恶意代码的AI模型对开发者展开攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1oOYoHUQm0a2cy9I03m1loVk6UqRgxMHfyX77P1cmELMxAbFLzamsd15jGicFePiaPQj6CaGutONg/0?wx_fmt=jpeg)

# 【安全圈】黑客在HuggingFace上传包含恶意代码的AI模型对开发者展开攻击

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

HuggingFace 是目前最热门的模型托管平台，各大 AI 公司都将自己的开源或开放模型托管在该平台供开发者们下载，因此也总有些黑客试图通过该平台展开攻击。

网络安全研究人员 Karlo Zanki 就注意到该平台出现两个包含恶意代码的机器学习模型，这些模型通过技术手段绕过 HuggingFace 的安全性检测。

HuggingFace 使用名为 Picklescan 的工具检测恶意模型，该工具本质是就是用来检测可疑的 Pickle 文件，但此次黑客使用的方式可以绕过检测。

![黑客在HuggingFace上传包含恶意代码的AI模型对开发者展开攻击](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylj1oOYoHUQm0a2cy9I03m1lia5vXdXksRskhXrwD5RiaNF7clEjuXFXFa7KbZ4J6KVERwL43Yh3OrCQ/640?wx_fmt=png&from=appmsg)

具体来说黑客创建的这些模型通过 PyTorch 格式存储，这是压缩的 pickle 文件，默认情况下 PyTorch 使用 ZIP 格式进行压缩，但被识别出来的这两个恶意模型使用 7z 格式压缩。

对提取出来的内容进行分析后，研究人员发现这些模型包含恶意负载，可以连接到硬编码的 IP 地址，借助 shell 收集设备信息并对开发者展开攻击。

所以各位在网上下载模型时也需要提高警惕，一方面应当通过 HuggingFace 这类较为知名的平台下载模型，另一方面也要确认模型的发布者，尽可能选择经过认证的公司 / 开发者。

这两个恶意模型名称：

glockr1/ballr7

who-r-u0000/0000000000000000000000000000000000000

来源：https://www.landiannews.com/archives/107804.html

***END***

阅读推荐

[【安全圈】韩某某投敌叛变，48小时内被国安抓捕归案](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=1&sn=7f31eb8f0f2b9706fa2bb95c56de54b9&scene=21#wechat_redirect)

[【安全圈】慧与Office 365 邮件服务遭攻击，至少 16 名员工隐私数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=2&sn=3fed7e8c8d5ff870c7d74733e568e26f&scene=21#wechat_redirect)

[【安全圈】微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=3&sn=42ec007bcefb5e73b814bbd77c03cb62&scene=21#wechat_redirect)

[【安全圈】曝英国要求苹果留“后门”：允许其检索全球任何用户上传到云端的所有内容](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=4&sn=932d329534a041f36ccec808cef39b2e&scene=21#wechat_redirect)

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