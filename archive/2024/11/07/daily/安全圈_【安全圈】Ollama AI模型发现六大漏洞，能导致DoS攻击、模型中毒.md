---
title: 【安全圈】Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065749&idx=1&sn=b8878258d3b73972d34180a4f45b9858&chksm=f36e6395c419ea83933909751917712797ee725716d53445c905e31288295910cc4fae20086d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-07
fetch_date: 2025-10-06T19:18:58.858122
---

# 【安全圈】Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgrLiboGCZ98GBJ5o4skCdn3SX8knBykicputvc8UFeovrykuy6ggibibeWhd8JgAGicjHEbWkUzGWVvRA/0?wx_fmt=jpeg)

# 【安全圈】Ollama AI模型发现六大漏洞，能导致DoS攻击、模型中毒

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据The Hacker News消息，网络安全研究人员披露了 Ollama 人工智能模型中的六个安全漏洞，攻击者可能会利用这些漏洞执行各种操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgrLiboGCZ98GBJ5o4skCdn3OA9jpLianauzdAfibUztLhiabvqFOc4YDhySCic3pDXHr7HW7Rdv8mPe8Q/640?wx_fmt=jpeg&from=appmsg)

Ollama 是一个开源应用程序，允许用户在 Windows、Linux 和 macOS 设备上本地部署和操作大型语言模型 （LLM）。迄今为止，该模型在 GitHub 上的项目存储库已被分叉 7600 次。

研究员在一份报告中指出，这些漏洞可能允许攻击者通过单个 HTTP 请求执行广泛的恶意操作，包括拒绝服务 （DoS） 攻击、模型中毒、模型盗窃等。

这 6 个漏洞的简要描述如下 -

* CVE-2024-39719（CVSS 评分：7.5）：攻击者可以使用 /api/create 端点利用该漏洞来确定服务器中是否存在文件（已在版本 0.1.47 中修复）
* CVE-2024-39720（CVSS 评分：8.2）：越界读取漏洞，可通过 /api/create 端点导致应用程序崩溃，从而导致 DoS 情况（已在 0.1.46 版本中修复）
* CVE-2024-39721（CVSS 分数：7.5）：在将文件“/dev/random”作为输入传递时，重复调用 /api/create 端点时，会导致资源耗尽并最终导致 DoS 的漏洞（已在 0.1.34 版本中修复）
* CVE-2024-39722（CVSS 分数：7.5） ：api/push 端点中的路径遍历漏洞，暴露了服务器上存在的文件以及部署 Ollama 的整个目录结构（已在 0.1.46 版本修复）
* 无 CVE 标识符，未修补 漏洞：可通过来自不受信任的来源的 /api/pull 终端节点导致模型中毒
* 无 CVE 标识符，未修补 漏洞：可能导致通过 /api/push 终端节点向不受信任的目标进行模型盗窃

对于上述两个未解决的漏洞，Ollama 的维护者建议用户通过代理或 Web 应用程序防火墙过滤哪些端点暴露在了互联网上。

研究人员称，发现了 9831 个运行 Ollama 面向互联网的独特实例，其中大多数位于美国、中国、德国、韩国、中国台湾、法国、英国、印度、新加坡和中国香港。其中有四分之一的服务器被认为容易受到这些漏洞的影响。

另外，云安全公司Wiz在四个多月前披露了一个影响Ollama的严重漏洞（CVE-2024-37032），该漏洞可被利用来实现远程代码执行。

研究人员表示，因为Ollama 可以上传文件，并具有模型拉取和推送功能，因此将未经授权的Ollama暴露在互联网上，就相当于将Docker套接字暴露在公共互联网上，从而容易被攻击者利用。

参考来源：Critical Flaws in Ollama AI Framework Could Enable DoS, Model Theft, and Poisoning

***END***

阅读推荐

[【安全圈】乌官员：谷歌地图泄露了乌军部署](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065731&idx=1&sn=d5f75cc5c304f1bb8066b8224922a73d&chksm=f36e6383c419ea95d8b702fbc21e9e48cf6da5d3c414d248f842a275e2f7a3ab6c53cf46f03a&scene=21#wechat_redirect)

[【安全圈】微软SharePoint RCE漏洞，安装火绒杀毒后导致安全防护崩溃](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065731&idx=2&sn=ec1234ec73aa6227c6092ac7f59a2a1d&chksm=f36e6383c419ea95b652d8e0d3e28f413e419b31f88142e6e6631f248ff8921ae09270e90b14&scene=21#wechat_redirect)

[【安全圈】诺基亚被黑客攻击，泄露大量内部敏感数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065731&idx=3&sn=e036ef5d22b5f53c925f2f31881dbd4d&chksm=f36e6383c419ea958e36b2f462b9a3e5d12858fbf90002d18580e19fb7bb3fe162ca8eb1053a&scene=21#wechat_redirect)

[【安全圈】重大突破，谷歌AI大模型首次找到0Day漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065731&idx=4&sn=1865f8c94d510093c5028b8b63f9b02a&chksm=f36e6383c419ea9504d4986e57eb7b3947367eebcc2f52aa9f277891a3fa457671970378d39b&scene=21#wechat_redirect)

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