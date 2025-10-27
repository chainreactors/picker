---
title: 大力出奇迹之js文件爆破
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495986&idx=1&sn=a72a6a2f6ed539e6f27f35c6e820c744&chksm=e8a5fb51dfd27247c6384365bdc389ed905e0d06dcaa9e3b27ca62cf7f04aa64a5c7da686d12&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-01
fetch_date: 2025-10-06T18:53:45.750975
---

# 大力出奇迹之js文件爆破

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6bDTZoeIMUEVg6EK6n3RF6VduwGOLFBgFxfKO1nYiawfkteQFAGb4YJib7KKr4BgOj9ekno2X1dl6A/0?wx_fmt=jpeg)

# 大力出奇迹之js文件爆破

迪哥讲事

以下文章来源于火线Zone
，作者303

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7OlSoscb5LEHb2Ge6ph01nFr96XGgwBtasrpfd92T7Gg/0)

**火线Zone**
.

火线Zone是由火线安全平台打造的安全技术专家聚集和交流的社区，旨在推动数智时代的安全生态。

## **0x01 引言**

当我们遇到一个登录框或者统一授权登陆(SSO)的时候，一顿瞎操作，sql注入不成功，账户密码爆破不出来，源代码找不到，端口扫描没有结果。此时总是苦于不知道该如何进一步做渗透测试和漏洞挖掘。笔者遇到一个有趣的现象，就是登陆后才可以看得见的js文件是可以未授权访问的。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15RHcialrxJrlrFBNZhu6Stc3oHJ261BlKobHcHeCWNwwCQzHWEJGyMaEg/640?wx_fmt=png "null")

## **0X02 初步探测**

利用扫描工具探测存在的路径。

• 目录存在会返回403:

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15RvWKEibuSQpVXQBMLkCH5ftIYa9HO6TtQKzgtszg63eFdXJU3d0nicYEA/640?wx_fmt=png "null")

• 目录不存在则返回404:

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15RP5J1CuBGYxEBHA4fy9vQbUyjownoLU2ubDuftXuyicHSDwEYDt7kNrQ/640?wx_fmt=png "null")

经过递归爆破以后发现个有趣的路径:

```
/routes/admin/
```

## **0X03 js文件爆破**

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15R5icsyWXUSgficfMpSNOnk8iaiaSx1FNibibye0stMJqp7Pz4jTw7mI5sXG8w/640?wx_fmt=png "null")

## **0X04 利用linkfinder发现api接口**

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15R8eBY5DxlbXwJA9Ukpvu1NibG6I4XzlmNsmwFSVXfCLsF4gWheH8A8xg/640?wx_fmt=png "null")

发现一处有趣的api，但是由于缺少必要参数，没有任何响应。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15ROsW5dJpA1iaOSKm38ESoheOdl4icP6ejAxrwPYhiaEJMX5y8n4d41iaU0Q/640?wx_fmt=png "null")

## **0x05 Fuzz请求参数**

掏出我的祖传大字典，fuzz一波：

• 参数不存在返回200

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15RKtRX2pYqichJu2Zw0x1w7z1xrUR1kPwKbr4FUtSSpobPGAUm4icrgz9A/640?wx_fmt=png "null")

• 参数存在返回500

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15REia9cibapCD7xbfFibLQ8gd4aKVHC8y9S3otXPKOvRocjH35pmBk4rVPA/640?wx_fmt=png "null")

**最终构造出来的请求：**

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaSRR7yyWtexarrS0BMOb15R8oEk8KhWMadiah9Cq9AtIDHT11yeJjjUMgXwUHpzbrLZILiclrIUSQNg/640?wx_fmt=png "null")

**暴露了大量敏感信息，经厂商评定，严重漏洞。**

## **0x06 小结**

**目录探测 --> js文件爆破 --> api提取 --> 参数fuzz --> 发现漏洞 --> 获得赏金**

**如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款**

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

## **0x07 参考**

1. https://github.com/ffuf/ffuf

2. https://wordlists.assetnote.io[1] 推荐个字典

3. https://github.com/GerbenJavado/LinkFinder

4. https://wordlists-cdn.assetnote.io/data/automated/httparchive\_js\_2021\_03\_28.txt

published from :大力出奇迹之js文件爆破[2]

### **References**

`[1]` https://wordlists.assetnote.io: *https://wordlists.assetnote.io/*
`[2]` 大力出奇迹之js文件爆破: *https://articles.zsxq.com/id\_xwtpdnw3wtjk.html*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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