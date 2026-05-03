---
title: 汽车以太网测试之UpperTester
url: https://mp.weixin.qq.com/s/rzQg8yVvof961rqsNR9bTg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:21.525296
---

# 汽车以太网测试之UpperTester

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD2hFLV2APx6Bksp5e55JmSjibnNLzF83JYGHWH4VYru8Pwq6P06NfAGqhStVBZFf813r9lzOnUtfv3OX1vexibtaHgWcCIib7HUU/0?wx_fmt=jpeg)

# 汽车以太网测试之UpperTester

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

UpperTester，简称UT。UT是用于辅助实现测试设备和被测设备（DUT）进行通信指令传输，并执行相应指令的代码或应用程序。之所以需要UT，原因在于汽车以太网的通信是点对点通信，需要由客户端和服务端两者的交互行为来实现，而客户端和服务端的通信行为恰好是不一样的；如果仅将DUT作为服务端进行通信，那么DUT作为客户端的行为将无法进行覆盖测试；UT的实现则通过传输指令的方式触发了DUT作为客户端的行为，进而实现对DUT的协议栈，即IUT，进行了完整的覆盖测试。

在AUTOSAR中的定义如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmwu6QV7Y0v3qa1a4Ykjc4sWvV1cMCp3pu3e3gUBgQ51VBNjywrjdXbw/640?wx_fmt=png&from=appmsg)

UT通过汽车以太网接口传输的通信指令格式在AUTOSAR的AUTOSAR\_PRS\_TestabilityProtocolAndServicePrimitives文档中进行了详细定义。该控制指令默认使用UDP的10000端口（可配置修改）进行传输，指令格式使用类SOME/IP的格式进行封装，其详细定义如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmvMD6C3hCukicWRXBsHicOiciaHtPQZ459zYqNecnvXFLZDIqXC9f3Fgfpg/640?wx_fmt=png&from=appmsg)

UT的指令类型有三种：请求、响应、事件；UT单条指令的交互类型有2种，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmgLnGIbv55LXibBwtowjx9UI5UPqpoCBwV6nkjbibIh6bLEUTIwb4pNfw/640?wx_fmt=png&from=appmsg)

UT支持的协议类型GID定义如下表：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmlzr10qKBBlibaW9Zw8iblAou38gnrjUXXiceueDf21zVq2ZpsiaqSAInOQ/640?wx_fmt=png&from=appmsg)

UT支持的错误类型RID定义如下表：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmdVUnejQYBTg2ic8hEmNTFBkAk1thf2ZqkonsYdHzv0XsxtK9dhsyUgw/640?wx_fmt=png&from=appmsg)

以下是四种比较典型的测试用例报文交互序列图：

DUT通过UDP发送数据

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmg0kKjtoQf2r3SyAKGXo4c1kkNGxpe1SeKXh4VYS1lPycE9DcN5sUiaw/640?wx_fmt=png&from=appmsg)

DUT通过UDP接收和转发数据

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmWwU9SlDMFlXOI0ZA2lRYC9nONicGGEjTAOm9Zo0o1rcUm2QFNZ4iag5g/640?wx_fmt=png&from=appmsg)

DUT作为TCP服务端发送数据

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmM3WzknNJawotp7OiaD7wA7F3hiaAVSlDz2RM232VqH73Haiaf6Cdd4DpQ/640?wx_fmt=png&from=appmsg)

DUT作为TCP客户端接收和转发数据

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9O1lxVZ5icjmHu01MY3zYwmUPStseiax34yCNDToHn1jjc0CUicykqfYwr1ZZaGUUianrPn8yiaeV1pfQ/640?wx_fmt=png&from=appmsg)

总的来说，L3/L4层的一致性测试需要UT进行辅助才能完整覆盖TCP/IP协议栈测试的所有行为。对于AUTOSAR类的操作系统来讲，该测试主要通过SoAd模块接口来实现指令的行为；对于Linux、QNX等开源操作系统来讲，该测试主要通过Socket应用接口来实现指令的行为。

来源：

https://blog.csdn.net/u011941262/article/details/143480435

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

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

[汽车数据安全合规重点分析](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519068&idx=1&sn=78c66e13bd8798afd46c766b8f18abe7&chksm=e927cf87de504691c816f78b55daf93bdfb72fc1cb870d926de8b471e...