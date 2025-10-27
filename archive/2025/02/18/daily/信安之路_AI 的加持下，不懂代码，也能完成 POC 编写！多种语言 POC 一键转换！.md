---
title: AI 的加持下，不懂代码，也能完成 POC 编写！多种语言 POC 一键转换！
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247499795&idx=1&sn=0e6f5223c5dcf3b6c27eb6bda791e21d&chksm=ec1df03bdb6a792d27b470d2e16d8cde9fbe2b8d7ee530b8f2806a87d0f88503c534444453f1&scene=58&subscene=0#rd
source: 信安之路
date: 2025-02-18
fetch_date: 2025-10-06T20:39:40.875431
---

# AI 的加持下，不懂代码，也能完成 POC 编写！多种语言 POC 一键转换！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvOYgsFZZpHpC5SwicbPicIVlEgnop7cPY45PWMcTYrPicYV1ZOiaGibxU93g/0?wx_fmt=jpeg)

# AI 的加持下，不懂代码，也能完成 POC 编写！多种语言 POC 一键转换！

原创

xazlsec

信安之路

历史漏洞是渗透测试过程中必然关注的部分，因为有大量知名系统历史上存在过漏洞，而测试其是否存在由于未及时更新的漏洞是第一步。

互联网上有非常多测试历史漏洞的工具，比如知名的 xray、goby、nuclei、pocsuite 等，由商业产品，也有开源产品，还有很多不知名的产品，同样具备历史漏洞 POC 检测的能力。

各个产品之间存在着差异，有语言差异，也有 POC 编写格式差异，由于格式不统一，导致无法一次完成所有历史漏洞的检测，可能需要尝试多个工具之后，才能完成检测。

信安之路 POC 系统，致力于将全网公开 POC 进行格式统一化，将其转为 nuclei 可识别和使用的 POC，从而实现一键完成基于指纹的 POC 分类，最大程度提高检测效率。

如今 AI 大模型盛行，如何利用大模型来提高效率是我们每一个人都要具备的能力，之前尝试使用大模型给予数据包、漏洞接口编写 nuclei 的 POC 模板，而还存在大量 POC 是以 go、python 等语言实现，加入我们并不具备任意语言的阅读能力，如何实现 POC 的编写？

为此，我在 github 上任选了一个 POC，以 python 脚本编写，尝试使用大模型来完成 POC 的转换，具体要求如下：

![image-20250217115211359](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvO9CHrRBibRnjJA7l5LH3CIGFz6QXcSibrVM2h50UoBBjNdXes7jfa0kQ/640?wx_fmt=png&from=appmsg)

测试使用的大模型分别包括：Deepseek、百度文心一言、阿里通义、讯飞星火、kimi 五种，从结果上看，Deepseek 的结果最符合我的要求，下面一一测试。

### DeepSeek

生成的 yaml 格式内容如下：

![image-20250217115450312](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvv0UHVKicAOthW6CicR6m9V2tbP5Ljtrxg8zTXkKnkYCib8N8iamQqiammM1w/640?wx_fmt=png&from=appmsg)

直接保存后，进行测试扫描，结果如图：

![image-20250217115615376](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvELtOPwVUBEOcjo5Deq5qKqwls3d4lnfjUh1O5F3CxjVGf1nPtEqBuQ/640?wx_fmt=png&from=appmsg)

无需任何更改就可以直接拿来使用。

### 百度文心一言

文心大模型 3.5 所得结果如图：

![image-20250217115719584](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvx7BGQqfoict9JEfYo559BNqicic5l7UMWYkAP1q8D1Ur2vQAzSWHdItGQ/640?wx_fmt=png&from=appmsg)

直接保存后，无法正常运行，如图：

![image-20250217115824488](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvnSMkl1JAW98qmWDAUA58Tibf9yiaibtFdzWVebJWTgiaT6aiccgiayJoTsCA/640?wx_fmt=png&from=appmsg)

模板存在错误，而且匹配部分直接匹配关键词 root，结果会存在大量误报的情况。

### 阿里通义

结果如下：

![image-20250217124028176](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvoqicwDEuibONqnWolhyFTPC1icVteUgKO6pLNbaibSPbPyQajRGlpDEj5g/640?wx_fmt=png&from=appmsg)

通义生成的 POC 模板没啥问题，可以检测，但是匹配规则没有 deepseek 的更准确：

![image-20250217124129334](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvLjrKcNo5onWSk5qmJhR8qoL8t1IUJZOQXrTcs4icy7z4B6JUdue2mVA/640?wx_fmt=png&from=appmsg)

### 讯飞星火

生成的 POC 如图：

![image-20250217124218631](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvv4v4uKM5C9Sfq6zz2JbHEcfTeNfvQqdwMlKnAiaGUOG2KBHiaIF2d0OpA/640?wx_fmt=png&from=appmsg)

匹配部分，状态码不对，给它的检测函数并没这两个状态码，还自己发挥，匹配 404 和 403，而且无法直接运行：

![image-20250217124357658](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvv9I7yaZdtuNwyaDib24Lk6RH9DEiaw84N4zicbibEt2hALvWOFnz4MnTq0w/640?wx_fmt=png&from=appmsg)

### Kimi

![image-20250217124424845](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvv8O9wqWtcRia8ESu3I8ic0eW0ej1DRmRrHXFWJ1h6VLBFLkQ4bLbicqN4A/640?wx_fmt=png&from=appmsg)

kimi 生成的 POC 也可以直接运行，结果如图：

![image-20250217124502635](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAffwYRjbVCtTsicTCRicQVcdvvz65VxZic6zH0fGmcwFIrvwyGaJGmMvWtlrPEUFNbgypE45qhU8wT7hg/640?wx_fmt=png&from=appmsg)

它会自动添加一些字段，漏洞评级信息，还有最后的结果导出。

以上就是测试几个知名大模型的结果，之前还测试了几个复杂一些的脚本，deepseek 的表现是比较好的，只不过老是出现“服务器繁忙，请稍后再试。”有点烦人。

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfc1ibbG6mEdqV5Xpw0yu9UxtIoLlhiazxU4NakInEiam1mOnHHYw4pVq3nrrCc8tpnn5ictdhmNLUaHuA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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