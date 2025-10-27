---
title: 【安全圈】谷歌在Gemini对话AI机器人中增加盲文本水印 可以用来检测内容由AI生成
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065749&idx=4&sn=6e7a08939bc1fa5bc0f516088d6be4c8&chksm=f36e6395c419ea830fe214a47a37b257668ca9ae62ab4e5fca65bf8374f3c0e376ce592fa8b3&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-07
fetch_date: 2025-10-06T19:19:02.217823
---

# 【安全圈】谷歌在Gemini对话AI机器人中增加盲文本水印 可以用来检测内容由AI生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgrLiboGCZ98GBJ5o4skCdn3KGeuNAQoXX6bLcbLxUv8uMdenl9ia3mj02pdrDGFL08udoXyVia6ysBQ/0?wx_fmt=jpeg)

# 【安全圈】谷歌在Gemini对话AI机器人中增加盲文本水印 可以用来检测内容由AI生成

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

人工智能

基于人工智能的对话机器人正在快速渗透到我们的生活中，由于不合适的利用导致的问题也非常多，例如学生使用 AI 机器人写作业或撰写论文。

针对这类问题此前 OpenAI 就尝试开发文本分类器用来检测内容是否是由 ChatGPT 生成的，但因为检测成功率太低最终 OpenAI 放弃了。

现在谷歌宣布在 Gemini 机器人中添加用户不可见的盲水印，这种盲水印本质上是一种算法，利用算法将特定字词嵌入到文本中，用户虽然看不出来但检测器可以根据算法识别出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgrLiboGCZ98GBJ5o4skCdn3eup8mNHZ75rjbyIJkydhywsYI3SWI3MsGicXKObrdSoMjByQ6iajwXPA/640?wx_fmt=png&from=appmsg)

这个系统的名称叫做 SynthID-Text，谷歌称已经将该系统集成到 Gemini 机器人中，同时谷歌还开源了这个系统供开发者和企业快速检测特定文本内容是否来自他们的大型语言模型。

也就是后续包括 OpenAI 和 Anthropic 都可以使用这个系统 (如果他们愿意的话)，提前在模型里埋上盲水印即可，接下来就能成功检测。

SynthID-Text 的原理也不算复杂，谷歌开发了一种算法，首先将特定的提示词集成到 AI 模型中，这个提示词会干预 AI 模型向用户输出的内容。

被干预后 AI 模型生成的某些字词具有一定的特点，用户应该发现不了这种情况，但算法可以重新检测出来，DeepMind 研究人员称这种修改会在生成的文本中统计签名，在水印检测阶段，可以重新测量签名以确定文本是否确实由带有盲水印的 AI 模型生成。

AI 模型或者叫大型语言模型 (LLM)，本质上就是利用海量数据预测下一个最有可能的字词，SynthID-Text 通过随机为候选字词分配数字分数让 LLM 输出分数较高的词进行干扰。

因此各位接下来使用 Gemini 进行对话时，长期使用可能会注意到某些字词被其他字词替代，那说明这些字词就是盲水印，当然用户应该很难发现这种情况。

那有办法能够干扰这种盲水印呢？也确实有，既然谷歌开源了检测器，那就可以使用对文本内容的字词使用其他字词替代，然后再使用检测器进行测试，直到查重率降低到检测器能够接受的阈值。

只不过这样相对来说就麻烦了很多，于此如此不如直接使用没有盲水印的 AI 机器人。

来源：https://www.landiannews.com/archives/106449.html

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