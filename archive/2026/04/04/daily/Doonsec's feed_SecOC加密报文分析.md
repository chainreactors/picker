---
title: SecOC加密报文分析
url: https://mp.weixin.qq.com/s/pRJ6tYzh8DgB5FVwot56_w
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:36.785545
---

# SecOC加密报文分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDWgw01btWpwUzebV4tcNQ5KE8J21WIRcdrDl0hrofUsrCm0xsT7Js5pc23yKBnW1vCd6nstsL2yHHYNZ8KqRCNqicxP959qUJA/0?wx_fmt=jpeg)

# SecOC加密报文分析

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

SecOC通过对PDU（Protocol Data Unit，协议数据单元）进行加密保护，保证车辆内部各个ECU之间通信的真实性、完整性、机密性。但对初学者而言，这些解释，字都认识，但着实有点难理解。

究竟一个加密后的PDU的格式是怎么样的？这篇文章，希望通过报文解析，加深下对SecOC 原理的理解。

Note: PDU，协议数据单元。在分层网络结构中，数据需按照一定协议逐层处理后才能生成进行网络传输。每一层加工完之后的信息可以认为是一个PDU。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA41mNCciaKwAvcTlDUP0qq02Dia5WTia5KBbnpKktH0uaVWWFktmvhWRB6A18054Y4eX0Pbf3wfCa7WTfwS9vPj8IibazeFJy3byw/640?wx_fmt=png&from=appmsg)

**01**

**报文**

使用CANoe 截取量产车辆CAN 总线上报文，选其中一个SecOC加密后的PDU进行分析，如下图。PDU结构上包含4部分。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCiba527p2Vu06CEg24rn0GNRiajTDmRwLEaxjg0tCzIt7cA0eyuQ1RL2C81iaozJ4ZC9EJ3ht4EU1IkuXo2QQtOS1s9qeiaxkASO4/640?wx_fmt=png&from=appmsg)

**第一部分，CRC校验值。**

发送方将即将要发送的报文进行处理，生成CRC校验值。接收方收到数据后，采用相同算法进行CRC计算，结果若与发送方发送的CRC相同，则校验通过。

CRC能够对数据的完整性进行校验，算法比较简单，逻辑是将需要校验的数据与校验标准式进行异或运算。大多数情况下，数据源不同，CRC的校验值也不同。当然，CRC 并不能识别出所有的传输错误，但算法简单，占用资源少，所以也被广泛使用。

**第二部分，是应用数据。**

图中要传输的数据是电机转速，扭矩等应用信息。个人理解，这些信息对于整车比较关键，一旦被篡改对整车影响较大，所以需要安全加密。总线的通信矩阵可以查看哪些PDU进行了加密。当然，哪些信息需要加密，是需要在开发阶段定义。

**第三部分，SQC，PDU 发送的计数器。**

占用一个字节。初始值为0，最大值255，发送端每发送一次PDU，计算器加1。个人理解，该计数器代表报文发送的时序，SQC的连续性有助于确认报文发送过程是否错乱。下图是实际的SQC的数值。需要注意的是，总线休眠/ECU reset，SQC从0开始，即使SQC 未达到255。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD3nHDGQbR6ZzgZ89KnuVUF6jNR3G86PVDHJcqVJQAe1w4k7h8Afv4ibvZeZYvFqtyS2wfpqxhrE6sdSbJic0eya1cMxOBXRERibA/640?wx_fmt=png&from=appmsg)

**第四部分，新鲜度值和认证信息。**

SecOC加密的关键信息，包含新鲜度值和认证信息。从安全等级考虑，数据本身会比较长，并有一定的结构形式，实际报文中只是按照一定的规则截取其中一部分，以降低总线带宽占用。

* 新鲜度值，在AutoSAR里有相关的说明，可以有不同的方案生成。但总的来说，新鲜度值和报文发送时的时间标志位相关，有了这些标志位，可以唯一确定这个报文。
* 认证信息，一般指的是MAC（Message Authentication Code），消息认证码。MAC的计算过程如下，期间会结合整车密钥、信息源内容及新鲜度值等相关数据生成对应的MAC值。 其中，Secret Key是整车相关的密钥，各个主机厂所采用的形式及计算方法不同。但以个人理解，Secret Key 应与单个车辆本身强相关，如VIN 码。另外，需要有一套密钥管理系统，负责密钥的管理和发放。当然这个密钥的管理，应该要覆盖生产过程、售后维修，以确保密钥被控制器安全存储并使用。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDnLqicKIfMfJlibLTBicgQp0fjXPmu4wrybJHpDiaGXiamdR44WIfdmAs1YxQQW6UghILtYZDnlmo3HcEgM5xSibAueAv1Ybv5Zr7e4/640?wx_fmt=png&from=appmsg)

来源：CSDN@「Fresh\_flash」

https://blog.csdn.net/Fresh\_flash/article/details/145169260

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c3549c7ae2ceb362959dbcb159324b2593d70bce78d82a9&scene=21#wechat_redirect)

[汽车数据安全合规重点分析](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519068&idx=1&sn=78c66e13bd8798afd46c766b8f18abe7&chksm=e927cf87de504691c816f78b55daf93bdfb72fc1cb870d926de8b471eb3e1be61058498327b1&scene=21#wechat_redirect)

[浅析汽车芯片信息安全之安全启动](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247512151&idx=1&sn=7fabbeeec206ce615a5a3c574bed4c43&chksm=e927f48cde507d9ab6bfd4b8389b5eafea37586707682bfe60f294feb54e1c36cb07bad4d26d&scene=21#wechat_redirect)

[域集中式架构的汽车车载通信安全方案探究](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519952&idx=2&sn=709860de942501f20e923d15330ced9a&chksm=e927ca0bde50431df0b47ad1a2da63bf98ee637c9c00482145fbdb8755851b61421357aab4bf&scene=21#wechat_redirect)

[系统安全架构之车辆网络安全架构](http://m...