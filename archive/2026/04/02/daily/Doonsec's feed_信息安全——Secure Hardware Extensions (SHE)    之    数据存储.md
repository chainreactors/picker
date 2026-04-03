---
title: 信息安全——Secure Hardware Extensions (SHE)    之    数据存储
url: https://mp.weixin.qq.com/s/gz3Rm-AydN0hjOt7ZYaZog
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:26:02.449500
---

# 信息安全——Secure Hardware Extensions (SHE)    之    数据存储

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DK3l4HOfpuVjmNKXDAhmy4qpttQNUibEok32dCV4BH045TxftV883iaIPLIz4OQGSMImBL868xvWmSebqVLCmwNw/0?wx_fmt=jpeg)

# 信息安全——Secure Hardware Extensions (SHE) 之 数据存储

谈思实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于车载软件回收站
，作者如花哥哥

![](http://wx.qlogo.cn/mmhead/WD4FduqfeKJsMFJQuUqEbfgBbgclcQK1MFPaTEywrjGfW8kib8v4iaaFVo7mywaIuakAIibO9tiaQ5c/0)

**车载软件回收站**
.

介绍车载cp Autosar相关知识，涉及理论、实操、经验等

**01**

**SHE的memory slots**

SHE 需要内存去存储密钥和 MAC。

SHE 的永久内存被划分为各个逻辑块，这些逻辑块称为内存槽--memory slots，每个内存槽的宽度为 128 位，外加最多5个安全bit，以及一个具有 2^28 种状态的无符号计数器。即该槽被分为实际密钥、安全 bit 和一个用于防重放攻击的 counter。

下图是SHE的逻辑结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBuTAgntXmvhBQGS67BbEx46zGIjg6CguzwUzr8vl2XEU6VGURficsDvDCQ5Gn9K7FU3SJ5EdU4Ds4DXibIVN5IB0uebKktYCBlg/640?wx_fmt=png&from=appmsg)

SHE中的内存槽有3种，分别是：

* Non-volatile memory slots：非易失性内存槽
* volatile memory slots：易失性内存槽
* Read-Only memory slots：只读内存槽

**02**

**Security flags for memory slots**

Security flags for memory slots，即秘钥槽的安全bit。值“0”表示标志未设置，值“1”表示标志已设置。至于哪个密钥受哪些安全位保护的详细信息，参见下图。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCvUqOpIQRopDLic1miabnoqic67jhkhNZmmvJWH9cFz5udEnUmEvT2bkPJiao4CsnTDzyjy0MWicfoehMcNf043vhnVyoOhFNqWv2U/640?wx_fmt=png&from=appmsg)

支持如下安全bit，

* Write-protection of memory slots：写保护
* Disabling keys on boot failure：安全启动失败时禁用此密钥
* Disabling keys on debugger activation：debug时禁用此密钥
* Disable wildcard usage for key updates ：禁用通用方式更新密钥
* Key usage determination：设置密钥是否用于加密/解密/CMac
* Plain key flag: 表示key是否是明文注入，只针对Ram\_key

**03**

**Non-volatile memory slots**

MASTER\_ECU\_KEY：仅用于更新 SHE 内的其他内存槽

BOOT\_MAC\_KEY：安全启动时用来验证软件的真实性； 也可以用于验证 MAC

BOOT\_MAC：存储安全启动时的bootloader的 MAC

KEY\_<n>: 可用于任意功能的key。n 的取值为 3..10，即 SHE 至少必须实现3个，最多实现10个任意用途的密钥。

PRNG\_SEED:存储伪随机数生成器的种子，只能由 CMD\_INIT\_RNG 访问。由芯片内部固化。

**04**

**volatile memory slots**

RAM\_KEY：可以用于任意操作。可以依赖KEY\_<n> 写入，也可明文写入

PRNG\_KEY：不能被任何用户函数直接访问，但会被伪随机数生成器使用。

PRNG\_STATE：保存伪随机数生成器的状态。

**05**

**Read-Only memory slots**

SECRET\_KEY：芯片的唯一密钥，芯片生产时固化。

Unique identification item UID：芯片的唯一标识，120 位bit，芯片生产时固化。

**06**

**Identification of memory slots**

CPU可使用的所有内存槽必须可以通过4 bits值寻址。内部的物理地址可能不同，但是逻辑地址已经规范定义清除了。表4.1显示了每个key的逻辑地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAobwd1viaKGkTAm2SGib98OIp42FE78cFlf8xTTT1lNyXWxIcqw5cUVB1sUqsUfsIic93M1JyI1GJ0x0vJUOu6ZAbet711RTpg2o/640?wx_fmt=png&from=appmsg)

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

[系统安全架构之车辆网络安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247520446&idx=1&sn=27e10e455264cecb2a1b49d91484d036&chksm=e927d465de505d73c59a6fb4cb066c7c7d07a96ef49a841ffe598c23d28be545c5874dec7de4&scene=21#wechat_redirect...