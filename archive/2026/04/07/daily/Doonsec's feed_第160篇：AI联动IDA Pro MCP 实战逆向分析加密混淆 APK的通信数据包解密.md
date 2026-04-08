---
title: 第160篇：AI联动IDA Pro MCP 实战逆向分析加密混淆 APK的通信数据包解密
url: https://mp.weixin.qq.com/s/SkGa7gIbXNtyvuYM1AZJdA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:33:48.339830
---

# 第160篇：AI联动IDA Pro MCP 实战逆向分析加密混淆 APK的通信数据包解密

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2b7d7TONuTjjJZdMDkickgleXVurTntStZLAOPAZAKsHJZljeIa800CGXlobqR7oeaFB3iaYwTYMCic69ibwBvq0v4ribEuoXyx2r4A/0?wx_fmt=jpeg)

# 第160篇：AI联动IDA Pro MCP 实战逆向分析加密混淆 APK的通信数据包解密

GSCL Sec

![]()

在小说阅读器中沉浸阅读

以下文章来源于希潭实验室
，作者abc123info

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fmEcY2bcaelEq3UFVKWcPYSM5dibWwP6KNJRapia8tbPQ/0)

**希潭实验室**
.

ABC\_123，2008年入行网络安全，希潭实验室创始人，某工业大学客座教授，某部委授课讲师、省级专家裁判，省评标专家。专注于安全咨询、网络安全培训、APT技战法分析、代码审计、渗透测试。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

Part1 前言

大家好，我是ABC\_123。最近听说 IDA Pro MCP 非常强大，一开始我其实是半信半疑的。于是索性亲自上手试了一下，我的认知又被刷新了，现在AI发展得真是太强了。我特意挑选了一个难度不低的 APK：Java 代码经过混淆处理，连 so 文件也做了加密和混淆；结果AI分析不到1个小时，竟然连加密数据包的解密函数都被还原并写了出来，不可思议。文末有知识星球二维码，欢迎大家扫码加入，一起学习进步。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aSrrFtI5259NPOqfK7yzKpB8TQVkJFclAY9Ulom70TA8cKybkkhHVh4DVjB7edf4vsMBwvMtSWTgS7lKtib6YvLKmBYzDlhV5g/640?wx_fmt=png&from=appmsg)

Part2 技术研究过程

* 前期准备工作

首先，经过一系列折腾，成功抓到了apk的通信数据包，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2Zrcaexliarz20e77GWZYQgWJIibcibpwxm6rsld5U63gZuBicHc3VcO6icKI3vTXrpfN6p1L9DuC3YmTwvG2MBkRWUu7TVxhjmesak/640?wx_fmt=png&from=appmsg)

使用jadx打开apk，然后将参数名r0SwHu作为关键字进行搜索，定位到关键java代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YqsRxfibvjp68ZJedSKPVXApcfh1ebWJ70FWCHOoxBWwfdryRpzttvg7AeH7AUZCS3T2MOiayQQLKMaUiciaJdY3QIm6VFmmaCbMQ/640?wx_fmt=png&from=appmsg)

通过分析可以看到，核心逻辑被封装在 `BeinasongTowerHelper` 类中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bTQ1Zrt9ASWdNrmn0kdbEGHgnJO0fgo8PagiceCibmWfNJfXgdbnFCHuVKw8lj4ialh4cQmJbKa55qPVrRGZagqMs7Fzu1xH0WO8/640?wx_fmt=png&from=appmsg)

最终涉及的数据处理函数 `drj` 和 `epj` 都是通过 `System.loadLibrary` 调用 so 文件实现的。也就是说，加密解密逻辑实际被封装在 so 文件里。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2alJt1PN1mtteD95NahU2vQLL5jWyPncXuTpug73EibpRmvNaKwRDlFEXUINEdhCc9nOiaA6ibghicrbKp8qz7WlWKWcic7DjCQW30k/640?wx_fmt=png&from=appmsg)

最后，我以压缩包形式打开 APK 文件，定位到对应的 so 文件。这里很可能是加密算法的具体实现，而其他 so 文件基本都是官方标准库。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bUQ8bfLNa0cibvHAtdzx8DRWO9fZibQrDb1ZsY1s0bDZa75icoeGtJ8hx87O682t6rsiaAiceuSz3CggaaROyuDiarKkCicvtzbLAuicE/640?wx_fmt=png&from=appmsg)

接下来使用IDA Pro 9.3 打开这个so文件，文件分析完毕后，在Plugins中开启MCP Server服务端。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2aickGxia8eLSb9wVkdNdOPp7Cds1UmJWmJQibfO5LKS2eKscv9NxEkAwRcJ95BAO561SlkwPCVpiajDFT61X2vRjEtTfckVVDMNLw/640?wx_fmt=png&from=appmsg)

随后，我配置好 Claude，并通过 Claude 调用 IDA Pro 对 so 文件进行逆向分析。在分析之前，需要确认 IDA Pro MCP 的配置是否正确，这一步非常关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bTczxK1OwbYf1OBQkX3QhyUjsW0SFpwZnrc4KFfFImQfo6aYbaQTnsROMmCyuDgjBsP7YZHy2MnVd01MrupRlia8MwI5lrVmnM/640?wx_fmt=png&from=appmsg)

* 构造AI提示词

配置确认无误后，开始对 APK 中的加密函数进行自动分析，提示词如下：“这个是apk反编译后的代码，epj是加密函数，drj是解密函数，请参考这段代码，从IDA Pro MCP中分析的so文件中，找到这两个函数的具体实现”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YIpmXgzDCoibMGDwtk4RNlQpxcKjGMmAqwW0rgRhM59Z10SDLRIvbuicqTvNy7D9KlmrSQbkFtMz1omAzRMc1oUE8lmq3Izx9ibQ/640?wx_fmt=png&from=appmsg)

接下来，使用 IDA Pro MCP 的 list\_funcs 功能，快速定位 JNI 函数的调用情况。通过 decompile 功能，我逐步分析了函数调用流程，并定位到两个核心函数的实现。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZicNW4YJUZo8yTQibG6qk38dG1thNpL30vsYNQUM1agOZXRVbyjMHyibicpRhvJRRZwRmfcfAZ5ArrJWDSj6HH6jM986qH8ExHS3U/640?wx_fmt=png&from=appmsg)

最终经过几分钟Claude + IDA Pro + MCP的联动分析，成功找到了两个函数的实现。加密函数 epj，对应着JNI 入口：sub\_1AF34；解密函数 drj JNI 入口：sub\_1B534。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bBO2cNFUMejTdlxYiblwfnUZhzbncSNyic69lHJNfPLAv1jViahprG50uLUKFoHmShzibickB5McGlibL39r2EMT2KWFNPHYF792TJk/640?wx_fmt=png&from=appmsg)

接下来，AI继续分析 `sub_14B5C` 函数的实现。通过 IDA Pro MCP，可以快速查看函数的 Base64 相关逻辑，进一步使用 MCP 的 `analyze_function` 和 `decompile` 功能，逐步解析了函数内部的处理流程，包括 `sub_165D8` 和 `sub_177F0` 等子函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZHf4ffECJS8GAIaEQP5ZjZ0QXGiafSqlRJJLbiaOKibBtSohI4vF7CctjibZPOrZ7FEzS5CqcueuFJqbBMAAO33FGmgLDydAQRx0A/640?wx_fmt=png&from=appmsg)

接下来我们回到IDA Pro界面中，手工看一下sub\_1B534函数的实现，可以看到加密过程完全是加密混淆的，基本上看不懂。对于这种情况一般只能动态调试，慢慢分析把算法解开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZxKllzOgA3D9TosMIL9CTxKrys8lSTOx4gXia1uicLExero6Nsx0Vn2elfQStCaCAZiaAzmuWTGNN3ANqbkunnS13cXNFv11W93M/640?wx_fmt=png&from=appmsg)

但是有了AI就不一样了，我们不需要去理解它的具体实现，直接给出如下提示词：“使用python还原sub\_1B534函数”。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZRohN3eVbYrm5icSYoWNdyJdFwqwMHm6ib39q95ZYhicxonqiar2Rye1IefU3gAUZCZQK6jeXTup9wbqaTZp4pNLPvNg3yRFHyEyw/640?wx_fmt=png&from=appmsg)

最终还原出来的python代码并不能解密，最后修改提示词，"这个是需要解密的从apk中抓到的文本，可能需要url解码一次"，并将前面我们抓包到apk通信加密数据包作为样本，供AI去试错解密。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bicJGlBbAzQ3ibxC8KVaTlVE1P6Qrl5uOmvs43ng7F4eiaFuiaRTeFIiczJjDaDEQuPxFCrjdEctXnyZkDdHaXpPjukUBk6pgskeng/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZpODAqn0Xmn86vYZW0v1xabFgYdck0yvlq50HS2HLOz62SaUrUVpKxoOU3ztCfiaXeLKRGIfqHrK1S5422CgsE1C8OUBQXPeNo/640?wx_fmt=png&from=appmsg)

最终，通过 Python 脚本执行解密逻辑，我成功将 APK 中的加密数据包还原为明文，并输出为可直接使用的 JSON 格式数据。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bwZU9QCyy1I6ibHiaj9O57Zcf80YywKl5sibCEgIhIud8SWvTTVcNCxWtxN69nzzxIibMN0BtuNBlDcqxOJ63Pv2gONf3LkzibnwpI/640?wx_fmt=png&from=appmsg)

Part3 总结

1.  时代真的变了，AI 的发展速度已经超乎想象。

2.  本次案例通过结合 so 文件分析、Base64/Salt 处理解析及 JNI 调用追踪，实现加密函数 `epj` 与解密函数 `drj` 的完整还原。

3.  借助 Claude + IDA Pro + MCP，能够快速定位 APK 中的关键加密函数，节省手动逆向分析的大量时间。

4.  欢迎大家扫码加入知识星球，一起学习进步。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2bJDIugO0JGOo1viaoNvcmQ9KGuaV9Tb4iaiawib4e4ZhU7F2lOe1Pria3hX2ypoiaEgZTPlp6AbIgNWdEUr6IsJ3tfKGGictvHIm6j3Q/640?wx_fmt=jpeg&from=appmsg)

知识星球分为以下几个板块：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2bDWdyOzOyHS0aPL6AeXBqWdvS7G4SvQ19NoxWZjhOD3eJEl3TgIicqHn4emfP99t8g4IL7GfHOX45OQoST8LgN3vCIB8pCEAVk/640?wx_fmt=jpeg&from=appmsg)

知识星球的每一篇PDF文档、PPT文档都细心整理，配有3到9张关键截图。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2asOuDN4oUOteG005XfBSKeHicvaPJVKv679ywAYOaeicyLNYk2y2JotQS6jnxzPrOPzFmxk6qLzpGN9MxkBxiacjjQ7pV40kUZhg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

知识星球的每一个工具都是精心筛选，都附带有实测评价及使用说明。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2ZWpO3Ao3P5kIoiaUiamEfZ7WbYBZzgR5pRgWgFMMRUCjvfuxibNEeIfIftokxL0QtH2rhR903lYbn5xMCUv2QVticXhuX6gico0gXw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

欢迎大家扫码加入知识星球，一起学习进步！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2apEeHZ8ItP5en6lFck6DQyciaAk311XbeiajUibHPVrdFPFWxiaaPt95dkvqY8beLEeEpTb1pgiaFXTwYCiaT2iag0POsTHDdxedCOkA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**OR 2332887682#qq.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hTLmv2vrtibFchs6aOA0xbpZP9t5UCDUiciaZ0vTzXC77swIj8fkKWfibOmBxtNghoaghQAVObfJQ4B27GJyMzX2Mw/0?wx_fmt=png)

GSCL Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hTLmv2vrtibFchs6aOA0xbpZP9t5UCDUiciaZ0vTzXC77swIj8fkKWfibOmBxtNghoaghQAVObfJQ4B27GJyMzX2Mw/0?wx_fmt=png)

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