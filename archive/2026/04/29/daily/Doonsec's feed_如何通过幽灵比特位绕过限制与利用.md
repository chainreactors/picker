---
title: 如何通过幽灵比特位绕过限制与利用
url: https://mp.weixin.qq.com/s/w_OG-WYREo4emmpcfVoNnQ
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:27:17.421604
---

# 如何通过幽灵比特位绕过限制与利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkuc34Qs2x9qgZcQFuHtaLIqcVF2Rf0ibAKYh5LYUvPPE7pLYnUVl9otMA5VclNbGicWL2UWXbLpLR41x2GccYKdyYxonZXYct20/0?wx_fmt=jpeg)

# 如何通过幽灵比特位绕过限制与利用

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 579，阅读大约需 3 分钟

## 前言

非常好思路，使我 WAF 旋转。

凑个热闹，人捧人高。

Ghost bits 是 Java 字符处理的**特性**导致的，比如 char 2 字节强转为 byte 的时候，会把高字节丢掉，只保留低字节。

在 WAF 或强转前的验证阶段，字符还是一个普通的字符，强转后就成了有危害的特殊字符。

和 C 语言里变量类型强转差不多，PWN 里也有类似的思路。

原始 PDF 下载地址：
https://i.blackhat.com/Asia-26/Presentations/Asia-26-Bai-Cast-Attack-Ghost-Bits-4.23.pdf

## 注意

Burpsuite 本身作为 Java 写的工具，本身就对中文的适配性不是很好，用 Burpsuite 测试 Ghost bits 很容易出现 Burpsuite 自己把 Unicode 编码转为 byte 的情况。

hex 解码
![6a394123e8b9e84ff37cdfdb2dc3b1a1.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnic7weDdayVqo8LNiaP8D4fsLiaY19uK2g71Z9g8uicfrG5zxO9URDhRb35ia4ytOaiakEfBU1FTXT86SGK1N9o5uN8AGh9ngKTtQicI/640?from=appmsg "null")

6a394123e8b9e84ff37cdfdb2dc3b1a1.png

我还没发出去，你怎么就变了
![3ee576afb28ab35ac22024e4c44b8211.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkazIKliavibbIm7BAaqXrR2YOl4YAHlDlnmNmY4hCFKFR672jbKAAJvxYnkZ0dCDjf9eI5a6vz9erGHoAbs6YzTaPYqNeD3TTko/640?from=appmsg "null")

3ee576afb28ab35ac22024e4c44b8211.png

如果要用 Burpsuite 测试的话，可以使用下文的 Burpsuite 插件。

或者该用 Yakit，Yakit 的又一优势体现出来了。
![67267aa23d7cc4deddc7f3b075148bd8.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkwytF1NJm41pW4GichYicPNxINVWZ0KA5fQkURwvHicY6tfWVDOF4icQn5icPUAT7pOj6hfOMiajcwFLXXvRuNib8AtbOKibl117hvvWE/640?from=appmsg "null")

67267aa23d7cc4deddc7f3b075148bd8.png

## 利用条件

需要 Java 代码中用到强转，一般来说，调用框架的程序员，不太会在代码里用到 char 并强转为 byte 的情况。

但是，在 Java 的很多框架里用到了，比如 Spring MVC。

参考漏洞：Spring 框架因 Jetty URI 解析不一致导致的路径穿越漏洞（CVE-2025-41242）

> https://github.com/vulhub/vulhub/blob/master/spring/CVE-2025-41242/README.zh-cn.md

代码审计**常见关键词**
其中，ch 是变量名，可以是符合 Java 变量名称规则的任意值

```
(byte)ch
ch & 0xff
ch & 255
ByteArrayOutputStream.write(int)
OutputStream.write(int)
DataOutputStream.writeBytes(String)
StringBufferInputStream.read
String.getBytes(int, int, byte[], int)
RandomAccessFile.writeBytes
```

## 转换工具

### Burpsuite 插件

https://github.com/AugustineFulgur/GhostBitsGenerator

使用
![8b6564d4bb19590758fe7303f0eae138.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmxTmWNud5modjdzJ3rHmfKu26sJ6O22qwV7xh8mHKLz17BElGoDia6D0X9FibOdnD5icImRK4RMhRb6oA7owRtU7r4zeFo1W11PE/640?from=appmsg "null")

8b6564d4bb19590758fe7303f0eae138.png

### GhostBitsVerifier

https://github.com/TazmiDev/GhostBitsVerifier

![56637675ad502d321defeae813ac6556.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVneNECAg3pcc6I5jBy9dAVFnZODmTcyEzJCMgPZ5VKEUynQg9M2aPYpuasPuNm1ZWloFVytQR8787KLpGiaQib0Qptnl1hfFicA1Q/640?from=appmsg "null")

56637675ad502d321defeae813ac6556.png

内置 Poc
![1786691e8a73fb8025e3ddcba44a8dd6.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnt43YjJzrjDWA9mSqMIuIMvicFuraeP02Ybzso4wmtNybVDWW9f9L7uqnmd59U18jdwPd0wHy1NYlhsJfREntMp84D4WUPRYFg/640?from=appmsg "null")

1786691e8a73fb8025e3ddcba44a8dd6.png

### ghost\_bits\_tool

Python 脚本地址：https://github.com/boqiqibo/securityScriptsPython/blob/main/ghost\_bits\_tool.py

unicode 编码转 ascii

```
python ghost_bits_tool.py --mode lowbytes --input "阮严灵丰丰甲来"
```

![c6e165a779534b23b7592ac57f0a9c90.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl5GKib2Am5G1mkr6U9lb1cIFT1JOJib4fnSzicEWRBITohaghAHowThiabibEvgqcI4QI0EoplgUKqC9hN35E57fkicZP3el6uT2qfU/640?from=appmsg "null")

c6e165a779534b23b7592ac57f0a9c90.png

ascii 转可见 unicode 编码

```
python ghost_bits_tool.py --mode genbystr --string ".%u002e" --count 1
```

![1fa0d370dda85b81654d2404429601d3.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVneKoBo3K9ZtlUmx9oUXKdOOibojoTSatgP14ibUrY8Dibib18gY1bYYDvBoUfnia0Mkwo3icK3NIYqRRqMmota6Bic1HzmFicia3upWFY4/640?from=appmsg "null")

1fa0d370dda85b81654d2404429601d3.png

## 在线靶场

### 好靶场

http://www.loveli.com.cn/see\_bug\_one?id=1008

![d6f76996ed6da65ab98f25e7d209fab7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkZXK6Ep8DiadicXmWTS6ehialbIf16xszunicKWf6tSAR0A6ic8x6KeuPPthuvUJh5HW4ODr7d8I4g6ArVl6c06G5bIniao2xicqPKwg/640?from=appmsg "null")

d6f76996ed6da65ab98f25e7d209fab7.png

通过插件修改 jsp 后缀
![8b6564d4bb19590758fe7303f0eae138.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmxTmWNud5modjdzJ3rHmfKu26sJ6O22qwV7xh8mHKLz17BElGoDia6D0X9FibOdnD5icImRK4RMhRb6oA7owRtU7r4zeFo1W11PE/640?from=appmsg "null")

8b6564d4bb19590758fe7303f0eae138.png

发送成功上传
![a4408e5107fb91eb6c572ba3a75d27c5.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkP7icKGlx5pJOzSl88OznhfgMzrFNyV7sGJhvQlHhnQV72wHVuHbEkwqTicIw7ibkp4NWnV0w94TosLZbW2s0jdfRiba4JnBbFFmg/640?from=appmsg "null")

a4408e5107fb91eb6c572ba3a75d27c5.png

结果
![4a656a3c98c9b5cd51341bee003436f4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnasyUr3lozePdicvZa3belTlH8frMB9yI1qHubLJltAv7aftnnbGKzATfjdicUwiaua60l2C64ktPTrMqpMTRKa59LWa3xOBzly4/640?from=appmsg "null")

4a656a3c98c9b5cd51341bee003436f4.png

### Vulnhub 靶场

https://github.com/vulhub/vulhub/blob/master/spring/CVE-2025-41242/README.zh-cn.md

![4c03fb5fb33f956ca4e3ef4fdaa57dbc.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkJnx2iayMXIxv9ib1MRmYibSnlCWM0aVdc5Swic6rA91Cf5icuyol48FbSibwEf0mbTVwHLe7gkg2Z9lDicWibg3GnmywsKIltl4waaH0/640?from=appmsg "null")

4c03fb5fb33f956ca4e3ef4fdaa57dbc.png

## 总结

原文 PDF 中内容很多，正好马上五一了，没事在家研究一下。

我很热爱学习，绝不是因为没抢到音律联觉门票只能当家里蹲。

## 参考资料

* • 【WAF 集体沦陷】Java "幽灵比特位"（Ghost Bits）引发的新型 WAF 绕过与注入攻击 [https://mp.weixin.qq.com/s/DTGdGNGXPtHc-I6DEr6Dqg](https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247493202&idx=1&sn=ba0de89223f151234d296d5d883419e3&scene=21#wechat_redirect)
* • 影响面较大的新型 WAF 绕过详细解读 [https://mp.weixin.qq.com/s/Utx64ue7Phs44pCHrpJbrQ](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493669&idx=1&sn=6d6d7ed38645b0703153071e07a6b86f&scene=21#wechat_redirect)
* • Ghost Bits，绕 waf 神器 [https://mp.weixin.qq.com/s/vEErAiJ2TCqUf2vd\_br5eA](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247488243&idx=1&sn=32723122841e814a7b4af2a6ad85edab&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

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