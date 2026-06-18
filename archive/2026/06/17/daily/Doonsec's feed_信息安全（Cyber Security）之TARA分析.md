---
title: 信息安全（Cyber Security）之TARA分析
url: https://mp.weixin.qq.com/s/ljW0j-vtc-9uq3k8V8KypA
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:49:08.194803
---

# 信息安全（Cyber Security）之TARA分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBibLrw5mebrbLDicIy19P4haD82m5FzmBubajnyTFv6KKgRNqg6hPHaZ3fIDDguTUS6ySCAZQw95lSQVcYjM4FRBcn8emJicxW1E/0?wx_fmt=jpeg)

# 信息安全（Cyber Security）之TARA分析

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

零部件的TARA分析方法，可以分为5个大步骤：

1. 分析准备，充分了解零部件软硬件架构及功能实现逻辑
2. 绘制DFD流图，明确各场景数据流转关系，识别资产
3. 开展危险分析，应用STRIDE模型构建危险场景
4. 开展风险评估，通过IL 、TL两个维度评估风险等级
5. 根据风险评估结果制定网络安全目标及需求

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDicLGrBibjEoEOGX00EDmhGylz8yYjz5M6j9fKeqFKtd9icRyPHcDEzibfwtd8tHFsXrPh6sHCQYyAnens8MYZgdcNnKRicbhu6ibtA/640?wx_fmt=png&from=appmsg)

**01**

**分析过程**

1）TARA分析准备：

在开展TARA分析前，先做准备工作，将产品的现状进行调研并做材料梳理。

调研内容从多个层面展开：

1）产品整体功能及架构

2）硬件层

3）操作系统层

4）软件层

5）数据层

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBRNib41uHUymZzLibL3Ukxjyu647JjeOITHozeXpH6tjwdjQiaxdyI6qWoXIliaibTJDSZxticXKLZ3776Fpv2gDbnxCgUQIZ9zLRjs/640?wx_fmt=png&from=appmsg)

2）绘制数据流图DFD：

数据流图也称为数据流程图  Date Flow Diagram DFD，是一种便于用户理解和分析系统数据流程的图形工具，是数据流、数据存储区和数据源与目标之间关系的图形化表示。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAibnicQzRnAw6mchpEXZJ5ibVchhdgkjHH830ltAtOC1bLRV9frYHcliaPnB6qpp2VWs4kp6kpLvc3unOYDJSkiawiatL9LXrA2ElD0/640?wx_fmt=png&from=appmsg)

3）DFD分级：

DFD按照划分详细度，可分为3个等级，分别为Level0，Level1，Level2。Level0：在零件级打包，不打开内部结构。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCOkbbVk8G8FVEWuC7chpVtPv3YH9PuLjfwqjEhUcrqew0ia9hR39ib8Q6V2icul5ibLiaZxVDUHQ4kFboicFyWkeYJaohbAZNHdj3UU/640?wx_fmt=png&from=appmsg)

Level1：在零部件层级Level1，应将自身零部件“打开”，识别内部零部件中的个组件，并根据在某特定场景下，将各组件的数据流转关系，绘制出来。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaALVia83HQcBnsNq9NRRVP0r3oXRmY35gp0o1IX2YOSaTuHWNIk052lHSAmVmicwcWZBGhbgkEBIpCbmcTmuhGVaTMj7SySufCV8/640?wx_fmt=png&from=appmsg)

Level2：在零部件层级Level2，进一步将复杂进行打开，明确复杂进程内部的不同组部分，并分析他们的数据流转关系以识别重要的网络安全资产。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC9XJDuNqrN1o2Srcdxbft6u6MaQmmoaCSz2wA3bnfxbLDR3KJTvBBibCRJzswfoVuibxbWUC737evgU6RMtPlbPdgy73lh8GMXM/640?wx_fmt=png&from=appmsg)

4）威胁分析：

利用STRIDE模型来识别威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCUS5eXwGFwDZECLEicz8wtKEFNWtVw3YZqQq087UuIHdWbsDPP2ahLL3b4To2gGib2N8naqVyFXhblQGmvBnFIPxtOofhfyo8xg/640?wx_fmt=png&from=appmsg)

每类 元素可能面临的威胁，可看出，只有进程才可能面临STRIDE 6种所有威胁，需要对6种威胁逐个全部分析，外部实体只有S和R项有（对号，被选中），即指实体只能面临“伪冒”和“抵赖”两种威胁，数据流对应的TID有（对号，被选中），数据流就只有分析“篡改”和“信息泄露”、“拒绝服务”三种威胁。在数据存储这里有个需要注意的，R项的勾是红色，是指数据存储的R（抵赖）可能有也可能没有，只有当分析的数据存储用作审计时，采要去分析R抵赖的威胁，不作为审计使用就不用分析R抵赖威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDU9icmaDTnvTgmm8wk2KthZagRibNXcJrURIBr38p99Fz5eerjRD0KLhUlDTSfLK5AzeETNKOVHRNKk6xbtMXw364QO1hbsHXgo/640?wx_fmt=png&from=appmsg)

根据DFD，识别到产品种的资产包括以下内容，二针对不同资产及类型，又可以应用STRIDE模型进行威胁分析。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB3CDDYJvEspxiaybMErNF1R0queDqhWHTIibZboRhDZFT9F70iaZf63wKK1EwFHExicOuVHnticTH6nkDALFMEdibpVffzoEicprNlag/640?wx_fmt=png&from=appmsg)

5）风险评估（安全等级评估）：

威胁等级TL是由以下因素组成（每个因素各分4档打分，最后通过计算模型综合评价）

* 攻击者花费的时间
* 攻击者的专业水平
* 攻击者对被攻击对象的了解情况
* 攻击者的机会窗口
* 攻击所需要的设备

影响等级IL包括四个方面的影响（每个方面的影响都在按照4档打分）：

* 安全影响Safety
* 财务影响Finanaical
* 隐私影响Privacy
* 运行控制印象Operation

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAZyMROqvcp5MVPNdwAqBzFCrrDRsdBwBrYUeRQ7zTCYMap0Ziboia2JqtjMDsQ7OML9kBaYpjC6Wd9ehicoHGvejjiaAhKqbiaMKjY/640?wx_fmt=png&from=appmsg)

来源：

https://blog.csdn.net/king110108/article/details/129763773

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

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

# [不要错过哦，这可能是汽车网络安全产业最大的专属社...