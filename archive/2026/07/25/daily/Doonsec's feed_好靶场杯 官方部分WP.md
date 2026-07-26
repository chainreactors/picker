---
title: 好靶场杯 官方部分WP
url: https://mp.weixin.qq.com/s/IeuttGoPvTgye0AaC763GA
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:23:20.822424
---

# 好靶场杯 官方部分WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkb8pmnKtiabsTKAfzmhibNAibZJZhJZHUfeTicH8Ck1TJKOfFI4fEda0a5n0l5Z6IWsqicuoky0W0T2T3KtqJVMpXjVdWzbSnREPRs/0?wx_fmt=jpeg)

# 好靶场杯 官方部分WP

小叶Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于云晞科技Sec
，作者云晞科技Sec

![](https://wx.qlogo.cn/mmhead/uI5pczeERTZqp0sD97WA7qBqy6ibUHsZm4lhicSpR5icrNzcMUPHj2KOgCy7VPmrdVhEGPm3azP0nM/0)

**云晞科技Sec**
.

这里是网络安全探索基地！专注分享流量分析实战技巧、应急响应解决方案，深度剖析Web安全漏洞攻防。同时带来CTF竞赛解题思路与精彩笔记，助你快速掌握前沿技术，提升安全技能，共同筑牢数字世界安全防线！

**YunSee团队招新**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/nNzOrpxNkNMDupRfkbNbIW6mXS9bM9vOzCniciaURunvfYOGlfU3Utu7j8d7yVCcYcr62xpZCJ5a1ROzmZO3EswQ/640?wx_fmt=gif&from=appmsg)

为了进一步提升团队实力，现面向全网招募以下方向的师傅：

综合渗透（Web 渗透至内网渗透）、IoT 安全。

只要你热爱技术、愿意分享、喜欢和同好一起交流探索，我们都非常欢迎！

具有丰富 CTF 比赛经验，或在热门赛事中取得优异成绩者优先。

同时也欢迎想交流技术、组队打 CTF 的师傅加入“魔丸”交流群，一起学习，共同进步。

联系方式：

* 简历发邮箱：1013199991@qq.com
* 魔丸交流群：1034296865

# 古法赛道

## 贝斯的秘密

解压题目附近拿到一个流量包和一个被加密的flag压缩包。题目描述：对于键盘你了解多少？

![image-20260724110221400](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlyVQibcWb5noUCXZgKicHu6nlEAhB4UJQGaibr1Uk4uQe5Rw6qtZZuE8RH7EelzzwnIych8mZBlPibb9DAibsIJODH6TAMqAkR7Vn8/640?wx_fmt=other&from=appmsg)

image-20260724110221400

流量包中存在各种协议流量，但USB占比最多，依题目描述，断定是键盘流量相关。

![image-20260724110322882](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnicPbcNA0PgRsDu7XKaxntZvaTezS4ES32zciaNLZicVbibv5IEMIVpibVTjHv95PiaOySu8L5XNWFxpVcDfQ0ujuHZRwwGbmHB6IP8/640?wx_fmt=other&from=appmsg)

image-20260724110322882

使用LovelySpark工具能够直接得到键盘流量还原的明文

![image-20260724110603620](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlCbfiaVuricHKQ3HOSXiaoAyMgBQrm32ibClE89l5j8nuHLpia2iaf1MPNG0vpAJBcFh3Pe1UEibJFAzwVC794icS69ibLlaKDBGdjhsjo/640?wx_fmt=other&from=appmsg)

image-20260724110603620

手工分析

筛选USB流量，找到HID data，参照键盘功能键映射表。

![image-20260724121442920](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVliaGSUS7c35uibLiaIrR5a0veUt6djUZSQt31SiaicHQ5jvQj61BePhYY6rXl7gTkjm54AzmWhibIaeBxPUA5P0HibEhJ37Xz74mplTA/640?wx_fmt=other&from=appmsg)

image-20260724121442920

0x04表示按下了左Alt键

![image-20260724121259421](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVmftIj6IyicVfUsZPEiaF2qQmaUDH2PlO3RtBnSzlib5Q8lhDZEP5dOEtmnxmeZRLhuSOic0icKz523ribSerUkEk5Ib6yPz5YjZwv9k/640?wx_fmt=other&from=appmsg)

image-20260724121259421

后一条流量，多了0x59，参照键盘普通键映射表。0x59为小键盘的“1”

![image-20260724121536176](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmb73DvLL675Hds5uUa45VzGnpXRY1CYWHicolBgEt4yzwSLic4bU8p52BcwmwNa8V7yQ3rktOa3rqUWJxWbnhhSg8VgjL8K7B4I/640?wx_fmt=other&from=appmsg)

image-20260724121536176

![image-20260724121744447](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVlLepA7XrvQApiaEDvOcibdHuT41icfPyF7dLuFdibzAib4BEWwWuRB5IValIfBgw36NfXLAAtIyia2xbz9NABTQrROYZKcXqs9x2oy8/640?wx_fmt=other&from=appmsg)

image-20260724121744447

下一条流量，只有0x04。表示松下小键盘的“1”键

![image-20260724121859555](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVmRWsibqpXsM14unGy86nyQp0iccUlw39tQnRUz77mMGXQKufzJCWfdYxT01YhWa30tB63aibibfZq2eGx0lH4o3tQP9uvmcWa6Rb0/640?wx_fmt=other&from=appmsg)

image-20260724121859555

顺着流量向下复现，发现其实这是经典的 **Windows Alt+小键盘码** 快捷方式。得到结果如下：

![step1](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlxRHywdaaC94CR4BRgqoDxXWUKmhXI3WGQFrCapVDRtrmDrSZUt4PVSEZHGYfWqibwiaeibkwO3bIeOCQoX8icr02MSH27Fiahucf0/640?wx_fmt=other&from=appmsg)

step1

解压flag.zip得到Aztec 码

![image-20260724123744545](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmx6pQtia4xPqNCUbUKV9dxHgJuaDyfvXTaGRXeY9qJWOLXxom8gkBoYsawQYcHCiawZLLjknYpvlxgJiaiafpIUctuA0zaxhiaSJzA/640?wx_fmt=other&from=appmsg)

image-20260724123744545

在线解码平台得到字符串：

```
UloN0pPJgaMkphWzOLvT0EQRW48HLFPFDjtEeHx
```

![image-20260724123840696](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnI7e4O7oqo3z4MlgSSllQ87kiaIWedmSjNAqX7UlwZA3Iic9PRbIqHOTyg0zr7uNYp9zH3EeVBc8sqZAchIa541lV4RfQuvlA28/640?wx_fmt=other&from=appmsg)

image-20260724123840696

回顾zip的解压密钥：`pza90ZAq`

倒序过来取中间部分就是base家族的字符集，base62

AZ09az

![image-20260724124040698](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVn0Xghsx04nia5hcWUhERjaCgdlWdl1qsvv5MvrrmW6iaBX8IyibBAtwdgncYFLUmX5H8ECj7kF4icTVCCtEzhSnOQVBnibRVjiaWib7g/640?wx_fmt=other&from=appmsg)

image-20260724124040698

## 吉尔的秘密

这题，题目名和描述已经给了明显的提示了。吉尔 -> Gilbert，辛巴 -> Cimbar

![image-20260724125601452](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVlYD4DYPdVKxkUnickOFCsAhLVcNsicK7X5v2ubErAlnfz28c6MBVKicwDIbEEoOxS68uBl1M9gvvLkSKRHHu7N868PgOT02HQ4uE/640?wx_fmt=other&from=appmsg)

image-20260724125601452

fl.png 使用该开源项目逆向解密

![image-20260724125939002](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkyJQgHQKibqKR0aSeRJ8NTSQwUWdHmibyN3Me1ibwBcnG7SHnkMvweYX4NBvGdlzdpsElwrg7rI47bibk2feTvJ57Mc6VibmQaQsc8/640?wx_fmt=other&from=appmsg)

image-20260724125939002

解密

```
python -m cimbar.cimbar fl.png -o fl_de.png
```

![image-20260724130922756](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkuicpbjK0oqWb82qGVwzhgusVhLLiaJJlncAwRricTBic3VOjXYibmzvToiajiaibF4dcOLs7mhOWjfQjmEbxbY34ep6Ca08U1doHGrQY/640?wx_fmt=other&from=appmsg)

image-20260724130922756

得到一半flag

```
flag{Y0u_g0t_c1mb4r
```

![image-20260724131012120](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVnokENExIoDWD7TqaggnplvbXHNRXm0KDGichvDGiaTDKXwKMmTlaTWylV4ibtVhlxibMMia4AQNMm5JGxglA1pFSrYUq0iaquLZnv34/640?wx_fmt=other&from=appmsg)

image-20260724131012120

另一个使用在线网站即可解码

关键字：小番茄图片混淆

![image-20260724131124687](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmVfaXic0LiaWnAwVNezXfeWDKDzKjmxy07ibTw1x0QFqYFnb01d87QOhwWyCgibJwqv0aTbF4Mcg2jAxBpbkWJoUTTQ8CUuGmAWA0/640?wx_fmt=other&from=appmsg)

image-20260724131124687

得到另一半flag

```
_and_gilbert}
```

![image-20260724131205819](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnP4Ad1BWZIt2BNyWK4eOEQ1RJYhA6roqtekZ4RyOIdMUDlvdicAZ4KyzSSFVj1pwpKL40QR7FSfzU2F4B6SfxwibQCW1iaogBpLk/640?wx_fmt=other&from=appmsg)

image-20260724131205819

## 峡谷的秘密

![image-20260724131629684](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnkgFENVdfu0KjWocKUic7vJpHjD24lYRC6Zga8y5v8FFeibwHAG2iacGTIsgsdDXz6x4dDk0p5Giaia99ias4t01thez2ojF7bH2SRg/640?wx_fmt=other&from=appmsg)

image-20260724131629684

电刀特效是干扰项，看普攻拖影是有黑白煞气的。符合武则天的神器·明辉仪

![image-20260724131500084](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVnWmMjyo8eibOKGg979CsZ3az1XbQ6jqycUibFkRl1dB20eYiaHJjMGA1E5DSZunUIde51Th4YzYojWH5tA9McIrNhtoCNtSJGtw8/640?wx_fmt=other&from=appmsg)

image-20260724131500084

![image-20260724131445306](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmcMmkgsm3OUrMuMkibQxKVwRtknuwk78wJE7G79VkcIqbFUvGKMYcXicD6AoicL4Tibla30rAsMfxlxaVY3HUQibyIiccQibuaib6QgZg/640?wx_fmt=other&from=appmsg)

image-20260724131445306

## 算术的秘密

![image-20260724132334853](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkywx6R7FTtMryib6cXNiad8OiaVHB1KHf1xgvO9H7jpSpkGicgCRXCEhFkgEbOYLl8MX4jkcXibUnFrw5bQe4rgXxtUN6fzdpMuciaU/640?wx_fmt=other&from=appmsg)

image-20260724132334853

看图算出最终水果值

![image-20260724132940277](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnCUCyZ8Pj4c54rlrsqhrYDXtmYSGYURxPgOiclDUNSHG025Qu3GrHcF1lDKsBtxzoB2MoU7JTNCgscfP8iccrP5GxWaSfyHG1ZI/640?wx_fmt=other&from=appmsg)

image-20260724132940277

得到seed、nonce、enc

**这题并没有给密钥流的具体构造，也没有提供一个可以验证密码对错的接口（其实接口被我删掉了，但不影响解题**

看似要我们去解密enc，其实这题是黑盒PWN

![image-20260724133024412](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVnXySa6XFiaib7GnyDIKwfedBuNDE7JGsawPqJhbxUMwRq9Rgrv5PYFV6Adol0hicygx7zKRTUxUU9mryQDODZFurxHHe1bstxTQc/640?wx_fmt=other&from=appmsg)

image-20260724133024412

输入的`%p`显然被直接交给了`printf`

![image-20260724135556590](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVnTm0wHmGfRnXNa1SKIxKlNro9DU2l6NCF42ElRp6nFuNrNVbE1GN8ia8PyEW2oR5sbKiaaoGenPofl3NibjXEQUb4J3MBhxHo7Xg/640?wx_fmt=other&from=appmsg)

image-20260724135556590

第六个参数故意放了一个 `nope`，所以想靠 `%6$s` 一把梭是不行的。不过 `%p` 能正常工作，就说明栈上的内容仍然可以顺序泄露。

![image-20260724135732251](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVlTsibC9carb1cptfkBvNK2blgzVQo49YhKeEAKANGOUd0V8FnwRwbibJFBicfAfH3SFjW1FQqNqhicPrI231ag54VMiat7kCMb8ees/640?wx_fmt=other&from=appmsg)

image-20260724135732251

输入长度可能有限制，我用了 40 个 `|%p`，后半段里出现了这些值

```
0x3831357b67616c66
0x6331623539616361
0x3561386138323435
0x3331663032656261
0x7d3565336332
```

![image-20260724135834071](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmNzfxByCRE2unkP72Ok...