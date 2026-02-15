---
title: 汽车网络安全风险评估方法
url: https://mp.weixin.qq.com/s/SXvuwqwhwsHBGx89G0aOfA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:16:55.404465
---

# 汽车网络安全风险评估方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAt8cFW2RKia14p7HDFuUG7xvQIzQeY9KMOQnBE5JH0cyO5Y3uv4V1ajoaTLrmmAjDAZ4vjh0lYibZsEfDw2hazM0vgL94F6tXW8/0?wx_fmt=jpeg)

# 汽车网络安全风险评估方法

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247566311&idx=2&sn=27d2cf53ef824bfde9b824f90e864ec6&scene=21#wechat_redirect)

**01**

**概述**

THREAT ANALYSIS & RISK ASSESSMENT AND VULNERABILITY ANALYSIS METHODS 是概念阶段用到的核心方法，也是整个系统安全的起点工程。在计算机网络发展的多年来，也提出了很多方法。本文主要介绍针对汽车工程的两个方法EVITA和HEVENS。

**02**

**EVITA**

E-Safety Vehicle Intrusion Protected Applications是欧盟于2008年发起的一个针对网联汽车安全的项目，其目标是设计一个车载网络的体系结构的原型，使其中与网络安全相关的组件受到保护。EVITA方法主要参考ISO/IEC 15408 (7)和ISO 26262，设立了四个安全目标：可用性（Operational），功能安全（safety），隐私（privacy）和资产（Financial）。

对于每个网络安全目标，EVITA项目考虑:

威胁识别:使用“暗面”场景和攻击树来识别一般性威胁，从而识别一般性威胁网络安全的需求。威胁分类:根据威胁结果的严重程度和成功攻击的概率，制定了对威胁风险进行分类的建议。

对于每个严重度等级可以从下表获得（与26262相比，其拓展了非功能安全相关的目标）

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9v20eCbW5jEQHZjhloSnZPQniaoALJMz3ibwCHoR7Dw8ibsiaBNcfNpGsZQ/640?wx_fmt=png&from=appmsg)

在EVITA中成功攻击的概率基于IT安全评估中使用的“攻击潜力”概念，并同时考虑攻击者和系统。对于攻击者，攻击潜力考虑许多因素，例如攻击者确定如何攻击系统和成功执行攻击所需的时间、攻击者所需的专业知识、系统所需的知识、对专业设备的需求等。每一个因素都应用一个矩阵表示（就像严重度一样），最后攻击潜力由以下矩阵确定。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9Jj2QPNIzmDY8nibm6tzJDnoDfFITicEf08t71SlMUANveGuabh3crjzA/640?wx_fmt=png&from=appmsg)

将以上两者作为两个维度就可以合成威胁的等级，不过这个又分为了两类；一类是privacy, financial, and operational这三个no-safety的，而safety的要再考虑可控性（同26262）。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9lYFS1CHBVNqeswuqwlMy3icFibAoUrL6vZjzE3zfdm995ghefPuibTUbg/640?wx_fmt=png&from=appmsg)

可控性用于评估人类以某种方式避免与安全相关的潜在事故的可能性。可控性分类为C1- C4。其中C1表示正常的人类反应有可能避免事故，C4表示人类不能以任何方式避免事故。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9pHiaFgzG1PkY014Lk3avb5bHY3Ce0yukeRrbPVD71uoJvpu80hMIQ8w/640?wx_fmt=png&from=appmsg)

最后safety类的风险矩阵为：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9IyHygmr8NXZ7sia9icIT3Oa8MibrX0aZQ0T5XswicDLts1RNxick7qw267Q/640?wx_fmt=png&from=appmsg)

EVITA方法是一个总体性架构。在面对特定的特征或系统层面的时候采用THROP方法，ＴＨＲＯＰ方法脱胎于HAZOP (Hazard and Operability Analysis)方法，只不过将风险分析变为威胁分析。其分为三步：

1. 确定特征的最小功能，作为分析对象
2. 确定潜在威胁
3. 确定“暗面”的最坏场景

然后就按照EVITA方法进行风险等级的确定。

**03**

**HEVENS**

HEVENS方法也是欧洲的一个项目产生的，很多相关研究可以参考查尔姆斯理工大学的一些详细研究。

HEVENS: link.

其方法主要有三个过程：

威胁分析―――风险评估―――安全需求

**威胁分析**

-输入：描述的功能用例图；输出：资产与威胁的映射，威胁与安全要素的映射（采用STRIDE方法）

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9raB6Ogwd4EgvngPjwrNibFmjhiaRX8p1Un4H39XLecLRia5ib6SMN0cJfA/640?wx_fmt=png&from=appmsg)

**风险评估**

-输入：资产与威胁的映射、威胁等级、影响等级；输出：风险（安全）等级

威胁等级确定：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9iatzWT8D6xGmeq4OS3fPobBOBHxN7iatfAicMdURTsWC0JI1QZMWLT1ibg/640?wx_fmt=png&from=appmsg)

影响等级确定（影响等级对应的四个目标与EVITA一致）

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9oZesn4SBWOFUvuY1qfFia44C23eNxBFRH3yFZiaREBkzvocA6grjhhUQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9kcItHNoeJzgcscvQW86Ma9Fdg6fSuqLhJTrVeOYYuFperXL2LQuz2Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9ooricI5oNpnP5TV4V1vKuickibcrc3PptJCtlXyWLiaAHBhWhdqsWnn2jg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9yhyAMTbcLiaiaibu4jwMtQ7sqibsvjdR36aUicibgDRSwnSniajibk1fFFC73A/640?wx_fmt=png&from=appmsg)

最后将以上四个合成最后的IL

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9qnyy6VVb5QbMicEj9sghibKnrs2iaY3bls646ibDQibg720dSfN6r8CV9Hg/640?wx_fmt=png&from=appmsg)

最后第二步的输出为

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8owF5Swd6hnxGvUBMCvOx9sxsZ6mUAo3AhkJJs5rwmibENq75YCW4LhcnicnmjqdoSFj5ZBogpOEqg/640?wx_fmt=png&from=appmsg)

**安全需求**

-输入：威胁与安全要素的映射、安全等级；输出：最高等级的安全需求（因为对同一资产可能有不同的安全等级，这里取最高的）

**04**

**小结**

HEVENS和EVITA明显的一个区别就是在威胁分析的时候，HEVENS是基于安全要素的，采用STRIDE而EVITA是基于场景的，采用攻击树。另外，HEVENS考虑的维度更细致，其流程更加规范。

来源：CSDN@闻着文也

原文链接：

https://blog.csdn.net/Pan\_w\_w/article/details/106022699

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b...