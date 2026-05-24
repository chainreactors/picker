---
title: 汽车ECU软件安全更新技术详解：从基本要求到实现流程
url: https://mp.weixin.qq.com/s/g2I9h_ygbkKKwXlMvA8GlQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:44.706492
---

# 汽车ECU软件安全更新技术详解：从基本要求到实现流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCgr7wpfu3zqFgka6y221pEKefPb2fZquMPlN1BpNt8IW0OKpjCatWopN2GY51qGgDRH0kric8LnTVDK2AiaTNKoWhxgZPwJElibY/0?wx_fmt=jpeg)

# 汽车ECU软件安全更新技术详解：从基本要求到实现流程

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

目前，汽车ECU的软件更新主要可分为三类：

* 工厂刷写模式：用于出厂前的大批量刷写或升级，通常在车辆生产阶段完成。
* 工程模式：由4S店或工厂等专业人员执行的ECU固件更新，涉及动力、转向、车控等关键系统。
* 车主模式：车主根据云端推送信息，通过IVI系统完成应用软件更新；目前也出现利用该模式进行ECU固件更新的趋势。

但是一谈到软件或者固件的更新，不可避免地就会讨论到待更新软件的可信度，即信息安全问题；而今天要聊到的就是ECU如何实现安全更新，即防止ECU被恶意/无意更新到错误的软件版本，从而威胁到汽车驾驶人员的人身财产安全。

**01**

**安全更新的基本要求**

所谓安全更新，是指确保待更新的软件是目标ECU所需的版本。从信息安全角度看，即需要保障软件的完整性和真实性。

* 完整性：软件未被破坏或篡改。
* 真实性：软件由授权的提供方签发。

这些特性依赖于密码技术。信息安全威胁与对应密码技术的总结如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA8Qz7TJxTS4ncJxHa2WdNNhP9xQCB7xkl0UJSb0g3kvSVz43IOGTgzn1udicibFgeEJjUlFu7EI4icKGBWLicNZkUAMDgWn5arKU8/640?wx_fmt=png&from=appmsg)

真实性和完整性依赖数字签名、摘要算法、消息认证码等密码技术。

结合国产替代的背景，密码算法库的需求建议如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAQccPDMB6qyZcZnxxJDxywYTXn09ZHrKw14raH5LVkRz6EntFiaERibem8S5RFaBicPo1p9vjYV2oFtx444erBIfbyVZHdgydqnQ/640?wx_fmt=png&from=appmsg)

**02**

**安全更新的文件格式**

汽车ECU软件的常见Flash布局如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB9mDzeib3TRiadAxK1RGoxMAdPj5dO8tnoTdXIgxRNO4xZXKNlv8C1eibUMPJgWiaFfU3ibBicG7XntwAlG4KIDON20awice46TdIEnM/640?wx_fmt=png&from=appmsg)

在更新过程中，通常做法是将BootManager中的Updater（对称加密后的密文）解密并加载到RAM中执行更新操作。

为了保证待更新软件的完整性和真实性，需要在应用程序、标定数据等分区中增加签名段，示例如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCN5DYrzhNGZkZhSa4lMNx3THlL4Vg9cSdopGS43ryxZ0mbGZFA8Sib7tiazj0dXOAvFZ6mxIMRQHpSDXucSZpC3xY9UedEib2FDM/640?wx_fmt=png&from=appmsg)

签名段具体包含哪些内容？以应用程序为例，应包括两类信息：

* 对签名段本身的签名信息
* 对元数据（应用程序数据）的签名信息

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDOgGek4jDIibeEUCs9rDeg1rUkl89PDkPYzdlzdAM70dXspzpy3y96noibhtrX7nbUP6FTsGObmO5tmVGeEIibOb5HpEQDCxibLEo/640?wx_fmt=png&from=appmsg)

签名段主要为Updater提供密码服务支持，应用程序元数据以明文形式写入ECU。

需要说明的是，这里讨论的是工程模式刷写，与TBox作为OTA主控的场景不同。受限于当前MCU的RAM容量，无法先将应用程序元数据接收至RAM完成验签后再刷写。因此，流程是先验证签名段的完整性和真实性；验签通过后，再请求传输应用程序元数据，直接写入Flash目标位置，最后通过摘要计算和公钥算法完成完整性与真实性的验证。

**03**

**安全更新的基本流程**

安全更新的基本流程示例如下。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCNib7GjttYmmCnt9FkmuEgK5quS20mMS70zpZykM72ScuTNv0s6qTibibX9BnutWh9nCZicrCpWDGywIjGrPvmHoLJlfzsXYJFpVg/640?wx_fmt=png&from=appmsg)

这里就和常规的UDS刷写没有太多差异，需要着重讨论的就是验签的过程。

以签名段验签为例：签名段首先由签发工具使用特定哈希算法计算摘要，然后用签名私钥对摘要进行签名，将签名段、签名后的摘要及公钥一并下发给ECU。ECU获取所有数据后，先根据预置在Updater中的相同哈希算法计算签名段的摘要，再用公钥解密收到的签名摘要，比对两者是否一致。若一致，则进入下一步。

**04**

**安全更新实现的工具要求**

基于上述分析，安全刷新工具主要分为两类：

* 更新文件签发工具：仅供具备特定权限的人员使用，用于根据待更新的应用程序、标定数据等生成签名段，并合并为完整的Hex或S19文件。
* 更新流程上位机工具：用于执行安全更新。需根据格式要求将Hex或S19文件解析为签名段和元数据，更新时先传输签名段，待ECU验签通过后再传输元数据。此外，还需解析ECU返回的验签错误结果，该功能通常放在0x37服务中实现；若验签失败，返回自定义的NRC。

来源：

https://blog.csdn.net/king110108/article/details/135842882

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

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

[一文带你了解智能汽车车载网络通信...