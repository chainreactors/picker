---
title: 【安全圈】冒名顶替已下架 PyPI 套件，攻击手法 Revival Hijack 揭露
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=4&sn=61ffe75ef3405adbe977dbbc80ef8dbc&chksm=f36e65b9c419ecafb8672ebf32a39376f9d6995bc07948035c2f59bd600e4b196ae547e2f765&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-09
fetch_date: 2025-10-06T18:24:23.086713
---

# 【安全圈】冒名顶替已下架 PyPI 套件，攻击手法 Revival Hijack 揭露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhQV8P7VwvC6C2P0u35FEU8oXkHWBV66dDI3dYLskTjEfEibzZaZiaD5leVBmUmPu51WmuXBHgxoBKA/0?wx_fmt=jpeg)

# 【安全圈】冒名顶替已下架 PyPI 套件，攻击手法 Revival Hijack 揭露

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

漏洞

安全公司 JFrog 发布报告，公布一种名为 "Revival Hijack" 的攻击手法，黑客寻找已下架的合法 PyPI 包，重新注册相同名称并上传带有恶意木马的新包，由于用户通常不会注意到相关变更，因此极容易遭到攻击。

研究人员对下载超过 10 万次或运营超过半年的包进行了统计，发现这种冒名顶替式的攻击手法共计影响了 12 万个 PyPI 包。之所以这种冒名顶替式的攻击手法 " 如此常见 "，是因为 " 许多开发者经常下架包 "，据称 " 每月有超过 300 个包被下架 "，从而给予黑客可乘之机。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhQV8P7VwvC6C2P0u35FEU8Ng0qSrxJsA2UGgb1TYs2yMuS24ndPFEQnFcj0p4VLhtgMYCyTJzriag/640?wx_fmt=jpeg&from=appmsg)

为了防止黑客利用这种攻击手法，研究人员试图接管了一些已下架的包名，并上传版本号为 0.0.0.1 的空包以避免现有用户的 CI / CD 环境自动拉取和更新。然而即使采取了这些措施，根据研究人员统计，这些被接管的空包在几天内下载量仍达到数千次、三个月后总下载量超过 20 万次，这表明 Revival Hijack 的影响极为广泛。

目前该安全公司已将这一问题通报给 PyPI 团队，不过 PyPI 团队回应称他们早在 2022 年 7 月就已初步讨论过相关议题，但目前还需要进一步讨论解决办法。

研究人员强调， Revival Hijack 至今仍是极为有效的攻击手段，他们呼吁 PyPI 应制定严格政策，全面禁止重复使用相同的包名称，避免遭到黑客鸠占鹊巢。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0txpDfbyrQfVvE85QeUc8SNTTibheOUsR1V6fbGDu83akQoZrZgafh3iaw/640?wx_fmt=jpeg)[【安全圈】在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=1&sn=c35045938e79877d30f89b03edd0e1fb&chksm=f36e65ffc419ece90013b87874cd7798d71ec90c368fa3cd01b9772d200a1c28a3c179a97067&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0tbbeNaiaibcj5iaaFCJEXMpjtdKHpdBSUK8WFXxhkFSbSHrX7OAwRnusiaw/640?wx_fmt=png)[【安全圈】微软发布Windows Server 2025新预览版调整时间炸弹 请用户尽快更新](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=2&sn=1780528b58dfe68e94e96232787e9eac&chksm=f36e65ffc419ece9293ed88aae76bc78264cee9a48b12a868f4e30df06954de3b8f8450e3392&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliayAgNUicp8k6tBdiaTt9Ne0tvzZWFaB7j9wbQry52n6LyxZvqejZTWhJa9MYQoq3FX8eRwZ0YbpzbQ/640?wx_fmt=jpeg)[【安全圈】Microchip Technology 确认员工数据被盗](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=3&sn=54a0ddf43c0026e259668f2618ca0c2b&chksm=f36e65ffc419ece9b6366cf6730df99dce0a26885d6310c52bb5b820f8dc05ebbd72ed362f38&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzZuc9frHlJKxcK8vXZWV0YCun5qJwtzScxfSAgubKEncsnD45RuqELg/640?wx_fmt=jpeg&from=appmsg)[【安全圈】研究人员发现Yubikeys中存在一个难以利用但也难修复的漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064191&idx=4&sn=2fe0d56663512b21ba1785d9a22bcd38&chksm=f36e65ffc419ece95bd1e15cc3b1eb19a4fe27400937238106b5b34bde708be50cd7af470869&scene=21#wechat_redirect)

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