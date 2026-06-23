---
title: 请求响应包都加密时，如何用大模型分析明文数据包来挖洞
url: https://mp.weixin.qq.com/s/eDadHY0Far_cVL-md6zK3w
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:05.708059
---

# 请求响应包都加密时，如何用大模型分析明文数据包来挖洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkQCIOKRcYvX0KJVrE41ialvw9eO8sxIG2j7zNMpUw0JnvUcibuSA0tNlBhMvd9mEmMtDUkRL9y4EJpIic7WSvFoibnTJZFewZUOxE/0?wx_fmt=jpeg)

# 请求响应包都加密时，如何用大模型分析明文数据包来挖洞

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 782，阅读大约需 4 分钟

## 前言

先恭喜 NIKO 拿 major 冠军，太硬了。

之前写过遇到系统请求和响应都加密的情况，当时给的解决思路是让大模型写一个 autodecoder 的脚本，从而实现明文加解密的。

* • Agent 分析 JS 加解密函数自动生成 autodecoder 脚本 [https://mp.weixin.qq.com/s/UN-f97ebDmJ\_F64ikiDvfw](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247490193&idx=1&sn=d87a2b730519275b7915f4c261cc1a73&scene=21#wechat_redirect)

虽然能手工测试了，但是这种情况下，没办法给大模型来分析，Burpsuite mcp 用不了了。

没有大模型的渗透测试，都变得没自信了，脚软了。

## 两种解决思路

如果请求包加密的方法是对称加密，如 SM4、AES、DES 的，可以直接在抓到请求包的时候，将加密字符串解密为明文，操作完再加密回去。

正常来说，都是非对称加密 KEY，对称加密 data，这种就能做。如果遇到的是直接 RSA 加密 data 的，不在意性能的系统，那就用不了这招了。就只能从修改返回的 JS 下手了，比如替换 JS 当中的非对称公钥为自己的公钥，中间 Burpsuite 抓到后用自己的私钥解开，然后修改完再用原本的公钥加密。或者直接对 JS 删删减减，让前端发送的请求就是明文，不加密了，裸奔！靠 burp 来加密。

扯远了，继续来说对称加密的情况。
**方法 1**
用 MITM 做中间人，

browser ——》MITM 解密 ——》Burpsuite/Yakit ——》MITM 加密 ——》服务端

**方法 2**
把浏览器 Network 当中的原始请求响应包下载到本地，或者直接开启 Burpsuite 的 MCP，Agent 连接 mcp，自动获取 history 中的请求和响应包。

从浏览器 Network 下载，在 Android webview 开启调试的情况下，我用的比较多。虽然`chrome://inspect/#devices`中能看到，但实际流量还是走 Android 真机发出去的，如果没代理的 Burpsuite，是看不到的。

如果是从浏览器里拿到的 HAR，可以导入 Yakit，如果直接用 Burpsuite 或者 Yakit 抓到了，就没那么多事情了。

![950a0d8468338ed88ed09aab35ee1c7a.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk4sekvTJP1454h68Q9g3u8Am2sJ3eU8Cq5hnARribszxNXgHK42BCYOf17U0HpnfjUtbdsB1UnQLzZicoPMzPbgDcYfialevXs8A/640?from=appmsg "null")

950a0d8468338ed88ed09aab35ee1c7a.png

![067070ebfda5172c6948140a648ee62e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVl6jK9slo8iadw35JJsoUsa6bWdZDTHrpMpJFNlyg8moUtmmUticHkOuMAJbzOicu2H1AYHPc6XgrhomMqUVkVVXicV6vZbkKibtGEs/640?from=appmsg "null")

067070ebfda5172c6948140a648ee62e.png

Yak Mcp 开启
![1f7947cad170fcfe73a176c70d1405c8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVn9EItsPyLp407jWmk0ick1bAfbickhZhCxmgLaBQaZkbZCsbLd0vwNvSTvUHWgiaYgoBticn9dZ2lXZJ8eGetQUdu1gzSELVx0ibD0/640?from=appmsg "null")

1f7947cad170fcfe73a176c70d1405c8.png

```
claude --dangerously-skip-permissions
```

**提示词**

```
通过 Yak mcp，连接yakit，分析history当中的流量，将其中所有的请求和响应包，解密后保存到本地的markdown文件中

加解密的办法参考脚本：
autoDecoder_sm4_sign.py # 加密脚本是之前分析JS写的，给autodecoder用的

python命令为python不是python3

markdown文档格式：
仅保留路径为 /api/xxx 的流量，像js、svg、gif后缀的路径不保存
保存的数据包仅保存解密后的明文，不要原始密文，保存后的数据包可以直接使用
```

原本
![93665881ef8b319c7e8bf498ed9ec016.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnfcTTiaqeb1yrHJiarzO27PQm563E5zVibicLvGPctZxNDNKypUIrSmibW7ddjQNZ1qGwibIOw2EKzc0nkD3slBSZmCU8JhFtpp19O0/640?from=appmsg "null")

93665881ef8b319c7e8bf498ed9ec016.png

结果，markdown 中
![7c5774d654ed0d34938a5645cf8332e4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm5Fe9hEPliamTqC0LYbHqRlYhjibvEUt8PIphxTVwC4ANUiakIGuL1KsHMoFgfxzxHf3bibpIfn9JjLp8icvEW1yG7lyssOPXwsaicg/640?from=appmsg "null")

7c5774d654ed0d34938a5645cf8332e4.png

明文
![63cf63ae9585568b0bf044b2e413c7dd.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkVibjj3GbTxkgrKxVwBEicBkQODfrbictQFUxiaEMVEdyJa56rfCaUQErRW3Al7lJkqKrnF9oHl0oBY41XHj8Bzsy5JVwQX6SMWZA/640?from=appmsg "null")

63cf63ae9585568b0bf044b2e413c7dd.png

## 扩展

### Yak 热加载

yak mcp 还可以用来实现 yakit 的热加载脚本

提示词

```
分析autoDecoder_sm4_sign.py，写一个yak 热加载的脚本，热加载脚本参考：
<复制的热加载样本代码>
```

![00c869db745c250218b0d947443e05b4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlRibViat3DOI0hDia1pG1u5ibrKMplQCLNzW6Fe6IkcauR7pOsVNKDIfvLEnZSy9KPwvY0JAmzicRicyHEoJe7c9DXWlL7U8JHl1y4A/640?from=appmsg "null")

00c869db745c250218b0d947443e05b4.png

结果
![63b38b4317cd18e11f68d6b985132f9e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmTickfl5JDsLOotTJODrcEWx5CEMYibvPHejqu91cxzERJc0WRicgIWnDjKEiajEa42cCaA8NAD64Qxt2QVj2aqD8XxAFibCOUMicWw/640?from=appmsg "null")

63b38b4317cd18e11f68d6b985132f9e.png

history 当中的真是请求包
![e4380661b26775a14e4f7ea1f4749449.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkDe3bhfgtuoCpIKVDDiciaGPByYrePODI0gs3RQd92oK4licO2zcPK0VwVJXr6gu7zGJ9BKurpv2Ww7PkhLGg7l887IWRujdhG5c/640?from=appmsg "null")

e4380661b26775a14e4f7ea1f4749449.png

原本解密
![5af0d2c6450c5851d2275a83550dd3be.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkt5DVjZlib9dJFrvu52LqgAcIvHZbXgibUIHeUGsazf1LZ4jIq4pAtTysUSUA5XhZh1aV4ibTFwFF7ib1ywmC81bBxDhGAycIzb2g/640?from=appmsg "null")

5af0d2c6450c5851d2275a83550dd3be.png

**web fuzzer 中复制热加载样本代码**
![3fe2d9a56eb7ddf3c5bcfe2d98f1e5c3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkYTgXhLpdV4kuxVGIIVC4hDkHKYxmObhsCb0mlicxnTW3GFdgtSf9h0yd94shUBN2VEIwsh13tq4Sqa9iciae16glEdhDia1J6Ceo/640?from=appmsg "null")

3fe2d9a56eb7ddf3c5bcfe2d98f1e5c3.png

**Yakit 开启 Yak mcp**
![0e09cec69016335efccb83399a81afb2.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmuxQvS1HeANAXy0YDqwicIc8xhUq12P0ZQLg6HicPyuCaCfSXTea6q9se4R0pYkWxm3SmeVkzibOeezVl5Q5GTibEojpo8sdFjyxI/640?from=appmsg "null")

0e09cec69016335efccb83399a81afb2.png

cc-switch
![ed937d70c76b20a275cac17605f6d529.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkYt1YMTMsiabVNtGNibf2Jqic9ZC9DnbfYvdmMHYp8qQq8icpnOb2zaclo9BC74RP6XcvDfBoUn18keQW0P8eFo0uj25yZ7iat7y5Q/640?from=appmsg "null")

ed937d70c76b20a275cac17605f6d529.png

## 总结

又是大模型提升生产力的一天。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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