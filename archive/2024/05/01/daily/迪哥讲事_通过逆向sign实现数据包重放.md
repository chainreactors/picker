---
title: 通过逆向sign实现数据包重放
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494461&idx=1&sn=a9c977da3756dfde7b035bd255f3dff5&chksm=e8a5e15edfd268487d7b4292a00245c264759f0160edde3571f9fb42b122006a9ae48a757339&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-01
fetch_date: 2025-10-06T17:19:31.568367
---

# 通过逆向sign实现数据包重放

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZbibCRA5Y6UbWIicicrFs8iazrJoxNO7vQhDqHzofLVQGUfTibGRDG7MBGCw/0?wx_fmt=jpeg)

# 通过逆向sign实现数据包重放

tiantang

迪哥讲事

### 前言

在对某次渗透测试任务中，目标为一个apk，对其进行渗透测试，在使用抓包测试中发现存在sign的数据包防篡改，通过分析获取加密方法。

### 初步渗透

配置好https证书，使用Burpsuite配置代理，抓取目标apk注册数据包

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZ7fx73rBKM7qVnxgOYccMiaRoJxBHbqto9OicdjBUE5OVppfojibGTgjMw/640?wx_fmt=png&from=appmsg)发现存在用户遍历的问题，不存在的用户会显示未注册，存在的用户显示已发送短信。放到intruder模块进行手机号爆破，看下有没有测试的手机号信息姜姜，修改mobile参数发现会显示认证失败，请求的数据包中存在sign参数

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZbehcWiaHvkLec6CTJXRuxFzbzhyWU2cA4eutqHQ1wb1kbmK4M2Hqc1A/640?wx_fmt=png&from=appmsg)

##### 这里解释下什么是sign

sign签名校验法本质上是对客户端传输数据合法性的一种校验手段其常用手法为，在用户客户端传输的数据中额外加上时间戳以及特殊字符，随后一起得出整体数据的加密值(常用MD5,SHA1等加密算法)这就导致了用户在不知晓程序的原始数据生成sign值的方法情况下，若对传输到服务端的数据进行篡改，在后端都会鉴权失败，导致用户篡改后的数据无效。

### 解决sign签名问题

目前想到的有三种方法：

1. 测试下sign是否为弱加密方法
2. 测试下sign是否可以置空绕过
3. 对apk进行逆向，分析其加密算法

首先看来下加密字符，长度不太像md5的，可能是其他的加密算法，丢到cmd5上也没解开，G下一个置空发送也是失败了

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZdcVuatyWdXNUgFmxqYpO8gq77BictkNqSIpAS4ISibURkzdawojRYoZg/640?wx_fmt=png&from=appmsg)

只能尝试最不擅长的apk分析源码了首先使用几个查壳工具查看下存不存在加壳

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZtIIxWjt5KJQPVaJUsd2MpR5icicAgXhUwqH4xb4GT73T1ia6wV1I9daxQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZQbeCAbB27KgLv2nD13vEeibsQ5ZicCRaVUlPNusWeVbxgkY7w2TXHiaMw/640?wx_fmt=png&from=appmsg)

还行，用了几个工具都没显示加壳了，省了不少事情使用AndroidKiller工具分析一下这个apk

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZTcWhj5F5XliaD0LZR2giaBZKBpFXvN7uiatWhQibEziaV2UkEzHibYch4OkQ/640?wx_fmt=png&from=appmsg)我干，试了好几个工具不知道为啥都会爆这个错误，有没有大佬讲解下的。既然这样不行的话只能使用frida-dexdump脱源码了，这里就不讲怎么操作了，网上应该都有操作流程。脱下来了两个dex文件，通过dex2还原成jar格式查看源码。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZf7DO3LAqKP6JUCay91BEklv4McOakiacH7pjHkPKgs4xtNr0HYgvwNg/640?wx_fmt=png&from=appmsg)通过搜索sign关键字，分析了半天，并未发现存在相关的加密代码。

#### 神奇的思路二

想着既然java代码里没有，它又是存在加密的想到可能是通过js实现的，所以想着怎么把apk中的其他源码搞出来。在网上搜寻找到了一个方法，在没有壳的情况下，把apk后缀名改成zip方法，在解压缩，获取到了更多的信息了

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZQaarBhcxAZkj54ic0KgLfasFODMpNqBHoqNXJYxqjEwRzaECCpG6oew/640?wx_fmt=png&from=appmsg)使用idea再次进行搜索，终于在漫长的查询中发现了其加密的算法，果然是在js当中的。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZiamtEF5p4saGJwefcbomy4W8jN4Vac1nIdDlgqOPIuh0lmJ6VHny7DA/640?wx_fmt=png&from=appmsg)存在一个为secretKey的加密密钥，通过跳转也获取到了

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZVpYZ820qZiaicFQTqUWKAeOqNW9qCb7RiarV2m9Licketwk5SvEJ3FAd8Q/640?wx_fmt=png&from=appmsg)

懒得写python的脚本，直接丢给chatgpt，帮我写一下。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZChehYlCnsSzOWzP5IHRAiaiaBKTTCGgQLib0KZneWOWs3nk8flAVeCsOw/640?wx_fmt=png&from=appmsg)gpt牛皮，面向gpt渗透不过目前还是有个问题，不知道是传什么样的值来做加密，主要因为菜看不懂js，调的层级太多了。

想到了两种方法：

1. 通过hook查看能不能获取到加密之前的信息
2. 通过分析猜一下，会加密那些数据包信息

测试方法一：因为我安装了现成的环境，使用xp框架配合Inspeckage来进行hook

首先打开Inspeckage，选择你要抓取的apk，然后打开目标的apk程序

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZkd94iagvQP10mB5gBjsEDgnIXzYu6GiaQaibCiciaZ3XJmZp1TOIYSPdY5g/640?wx_fmt=png&from=appmsg)然后使用adb工具执行下面的命令adb forward tcp:8008 tcp:8008

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZq6OgqsDGuthpicMBtVOPxrkJFlicx6bul5TDQAlGMAf9Gr16m8kuIBow/640?wx_fmt=png&from=appmsg)

打开你本机的127.0.0.1:8008

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZyZG5oCexMuE3WiaZ1QpBBGTdRLVF9gINh6V3ssAHiaWwicHZfKEeQZ7CA/640?wx_fmt=png&from=appmsg)要保证App is running: true Module enable: true都为true然后打开burp进行抓包，获取当前加密的sign值

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZ6cAYDlqicRCrwevGpgEuEOS6mQQCmBx2eu2L541qdKSiafxUeZa9Jniaw/640?wx_fmt=png&from=appmsg)

获取到的为d3开头的，打开网页点击成on状态，然后查看hash

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZ7BDlMs4cQScrSNFqicaibWgwcrBBCfRvgkCVRFud68YrCm3S1XKLw7sg/640?wx_fmt=png&from=appmsg)又陷入的坑里，发现并没有存在我想要的值，只能把最后的希望放到方法二了

方法二：首先需要判断下这个sign有没有把head包也做了加密，还是只是data的数据一些数据。通过测试发现，更改cookie的信息和token都不会影响sign的认证，只有在改data里面的值会显示认证失败。那就好办了直接把data要发送的数据，放到py脚本中，进行加密，看看加密后的结果一不一致

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4wWicO1VF5NkEuWf7lFpgKZ96LopoFAPurDKGRpWDpL3zALVsnTrKYl5S88s9YH5qoyxpQZqFXmNA/640?wx_fmt=png&from=appmsg)

奈斯

### 后言

这是本小白的第一次进行sign的逆向，中间遇到了很多挫折，绕过很多弯路，搞了好几天才成功，总体过程中也学到了很多知识点，只能说坚持就是胜利，成功就在眼前。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

原文:https://forum.butian.net/share/2290

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