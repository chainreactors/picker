---
title: G.O.S.S.I.P 阅读推荐 2024-09-10 名师教你学之《后量子密码算法标准介绍》
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498842&idx=1&sn=8c17254b7527527126dc0812e9ec56aa&chksm=c063d283f7145b958faae45e5a12da3d8df7d484692f131364beb01e9756bb8357d5b3f876dc&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-09-11
fetch_date: 2025-10-06T18:29:12.823095
---

# G.O.S.S.I.P 阅读推荐 2024-09-10 名师教你学之《后量子密码算法标准介绍》

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FByfuyLicKBJUfSqHaUPCOXIvB7rqmq3JRJqUFZyoj1qic2z87BIUovS3IP2Fo4T093lU7xKx4pEEA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-10 名师教你学之《后量子密码算法标准介绍》

原创

G.O.S.S.I.P

安全研究GoSSIP

今天是第40个教师节，记得小时候看《烛光里的微笑》哭得稀里哗啦，看《死亡诗社》被最后“Oh Captain，my Captain”感动得涕泪交加。从小到大遇到的各个老师，不管是雷厉风行还是春风化雨，总是会潜移默化地被每个老师影响。大刘的科幻短篇《乡村教师》刻画了老师这个群体的最大特点——人类文明的摆渡人。也许AI有一天会超越人类，但是把知识和爱传递给下一代的任务，恐怕只能由老师来完成，因此我们要祝所有老师节日快乐，谢谢你们给我们传道授业解惑！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FByfuyLicKBJUfSqHaUPCOXfN2Bb3UGVjoYRAcqsulQgBL4FyQtMKIRnRyicm8jVLiaqMgesg4V0d9Q/640?wx_fmt=png&from=appmsg)

---

既然是教师节，今天我们要介绍一位名师的课程教学，这就是滑铁卢大学的知名密码学专家Alfred Menezes教授的新课程——《后量子密码算法标准介绍》，这门课主要介绍的后量子密码算法是上个月NIST正式确认的首批3项后量子加密标准中的两个：ML-KEM（前身是Kyber）和ML-DSA（前身是Dilithium）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FByfuyLicKBJUfSqHaUPCOXkvr8vqqmogGr6s3IUOfQpr1EJ660ic1c676PZKnRJ33ImZZibT1nK1Ag/640?wx_fmt=png&from=appmsg)

你可能要问，Alfred Menezes何许人也？如果对密码学比较熟悉的读者恐怕都听说过两本书——《应用密码学手册》和《椭圆曲线密码学导论》，这两本书都是由加拿大的研究人员合作完成，而Alfred Menezes正是两本书的共同作者之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FByfuyLicKBJUfSqHaUPCOXRBEvufUr85ze0wdKY7UcmGFofPayIDe0nXRW2c1bhhn0JBamtCXG9w/640?wx_fmt=png&from=appmsg)

时隔多年，Alfred Menezes教授再度出手，把自己对于后量子密码的理解制作成了课程，无偿公开在网络上，更重要的是，他特别考虑了我们中国的学生，专门请自己的学生把视频上传到了B站，因此我们可以每天刷刷B站，总共不到6小时就可以就学完这门课了！

> https://space.bilibili.com/3546754452556116/channel/seriesdetail?sid=4347362
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FByfuyLicKBJUfSqHaUPCOXQqGJK3jFPQ0qPygoIu1h0kqNSmvjSKx8JtBVTpngyiaWsK148O17TFw/640?wx_fmt=png&from=appmsg)

当然，课程网站上也有很多相关的内容（包括课件），大家可以访问。更重要的是，Alfred Menezes教授还许诺大家会把更多的密码学教学内容放在他这个网站（https://cryptography101.ca 看名字就很好）！

> https://cryptography101.ca/kyber-dilithium/

当然，除了通过课程来学习，你一定也想了解一下怎么通过代码实现相关的后量子密码算法，我们还要再额外推荐一个**现在可能是最完善的后量子密码算法库——PQMagic**

> PQMagic密码算法库主页：https://pqcrypto.dev
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FByfuyLicKBJUfSqHaUPCOXxd0bJ6JcL0Wibf4zwd4FAxxoWGPl3Ud7oJ9eybs0qgkxrxcpgkvoCrA/640?wx_fmt=png&from=appmsg)

这个算法库不仅完整地实现了NIST刚刚标准化的FIPS 203、204和205，还结合了我们国家的商密算法实现了一个基于商密算法的FIPS标准的替代，同时也包含了一系列国内研究人员自己设计的后量子算法，大家完全可以通过这个算法库来了解更多的实现细节，或者不想关心细节也可以直接拿来上手就用（完全开源的哦），开发者甚至还贴心地为大家提供了一个小的示范——PQSign（https://pqcrypto.dev/applications/pqsign/ 使用 Aigis-sig 算法对文件做签名/验签 ）。

三人行，必有我师。有这么多好的老师，你还不赶紧抓紧学习，搭上后量子密码时代的顺风车？

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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