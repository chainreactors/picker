---
title: 侧信道分析测评套件新功能—Kyber明文检查预言机
url: https://mp.weixin.qq.com/s/8XiskVhQ85K5bVyIwryCBA
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:48.830465
---

# 侧信道分析测评套件新功能—Kyber明文检查预言机

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Vcvo4WRFGwXEQkx0ohRWODicc5V7iazXdmPBKcRxJk5dicYibdLeWT23NianZsKFiajIwB8ZlDKoUDXalY4IuWxCB71anAyX0NNbxU99MDrCAp7gA/0?wx_fmt=jpeg)

# 侧信道分析测评套件新功能—Kyber明文检查预言机

匡柄宇
匡柄宇

数缘信安社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/Vcvo4WRFGwUzyghasZq2nC8r13BOoTN1BorE3IdDTWAarJ9xwnCib1ZuZBPwSakj25KjynzlF8pvTE5ib3iceq4CaATaoupaaf7NibmuU4MSVLg/640?wx_fmt=jpeg)

**NEWS**

**探索后量子算法的侧信道安全性**

**01**

**功能背景**

ML-KEM（原称Kyber）是NIST于2024年正式标准化的后量子密钥封装机制（Key Encapsulation Mechanism, KEM），主要用于在不安全信道上协商共享密钥，因其基于模格上容错学习（Module-LWE）问题的安全性保障，被广泛视为抵御量子计算威胁的核心密码方案之一。ML-KEM在数学结构上能够抵御已知量子计算攻击，被广泛应用于需要长期抗量子安全性的通信系统、安全芯片与密码模块中。

随着后量子密码算法逐步落地，如何在真实硬件实现中评估其侧信道安全性，是近几年密码测评领域的关键课题。

**02**

**安全风险**

虽然ML-KEM在数学结构上难以通过传统密码分析方法直接攻破，但在实际硬件环境中，解密过程仍可能可能泄露出功耗、电磁辐射等侧信道信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwVE9HG3nUaoDOFZkqqVSmr373kgpxiaJcKedSHeysHRWEeIbW89unLm8LXNoXo97Nys746nZyYALXKKPvvhvyMHM9PTNaNtStkE/640?wx_fmt=png)

实际硬件环境下的侧信道泄漏信噪比

FO（Fujisaki-Okamoto）变换是一种后量子算法通用的实现IND-CCA（抵抗选择密文攻击）安全的方法，其大致流程如下：

1. 用私钥解密密文c，得到明文m'；
2. 对解密后的明文m'重新进行加密（即重加密），得到密文c'；
3. 如果原密文c等于重加密后的密文c'，则认为密文有效，否则说明密文是伪造的或者有经过篡改。

虽然ML-KEM引入FO变换的初衷是好的，但他也是导致后量子算法侧信道泄漏的罪魁祸首。我们考虑以下两种情况：

**情况一：当密文c没有被篡改时，即解密得到的明文m'等于参考明文m时**

由于参考明文c是攻击者自己生成的固定值，所以解密得到的明文m'的值也是固定的，进一步地，由m'进行重加密得到的波形也是稳定的，可复现的（忽略噪声）。

**情况二：当密文c被篡改时**

由于密文c被篡改，解密后的明文m'的值将是随机的，此时对m'进行重加密，得到的波形将与情况一的波形完全不一样。

这两类波形的差异足够显著，攻击者只需采集大量已知篡改状态的密文波形作为训练集，即可训练出一个二分类模型。此后，该模型仅凭一次解密时采集到的重加密波形，就能判断出当前密文是否被篡改。

在研发人员的预期中，FO变换本是一道防篡改的“安全锁”，但在实际的硬件环境下，这把锁反倒成了侧信道攻击的“指路牌”。

**03**

**分析方法**

侧信道分析测评套件新增的“Kyber明文检查预言机”功能，覆盖从波形采集到密钥恢复的全链路：

**1. 训练阶段**

* 向目标设备发送大量精心构造的密文；
* 采集功耗轨迹，标记消息比特标签；
* 基于LDA线性判别分析降维，建立消息值为0/1的统计模板。

**2. 攻击阶段**

* 构造明文检查预言机所需的特殊密文；
* 采集测试波形并应用已训练模板进行分类；
* 多次采波投票，恢复消息比特；
* 通过Kyber解密代数关系，推导出密钥s的每个系数。

**04**

**软件界面**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwUxIkau14v8o8nZf1bGLZGibhvneIJWltBfw1c8umxKAKBqvZOaSWbrWXHqFVibFKn8QXbibcg6qbwdS7aSrxWTJRIOxbn2Mc5B5Q/640?wx_fmt=png)

采波界面

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwUTh3a9iahC1kCD2aibjHAK3EbDl7hvjvtAOFA9QwOyWe9BZFHerOYfEaIvLKWiawRB3AlcpCxOZ4Ax6lzuM4pTWT4p91e32bfnMA/640?wx_fmt=png)

模板建立界面

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwXZLGTibia1ngB2iaFrpOC4SxZPhB1W90mFibdW9rTLcSP5YZzO7o1OPJO2GY4nAOV7Fhu6cm05LOfHe1jOR828Xic9drjtR32ZqNBo/640?wx_fmt=png)

模板匹配界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwV8ujhGHZYicDxy6UiagUKNrScUEzx6s3Yw9p1QMKv0o6IV3ZQqyPwXRiboiaV4U6icFia9AbJ08zxjV96Q4f5yAnxibM1xVJ1zcia9zD8/640?wx_fmt=png)

恢复结果

关

于

数

缘

数缘科技于2017年研发的侧信道分析测评套件，已为30余家密码厂商提供密码芯片与产品物理安全性测试评估、密码芯片IP核设计、密码产品解决方案咨询等服务，其中服务的3家厂商的产品已获得国密三级认证证书。2021年，数缘科技承担某国家级检测中心“板卡类密码产品检测平台非入侵式攻击检测功能模块”项目，打造面向智能密码钥匙、PCIe密码卡的非入侵式攻击检测平台，通过排除密码芯片物理安全隐患，加固密码产品实现方案，推动我国密码芯片与产品物理安全性水平的整体提升。2024年，数缘科技进一步承担该中心“高等级密码模块安全分析检测平台”中“非入侵式安全检测模块”建设，帮助中心构建了各种常见检测方法的标准化测试流程，并基于人工智能算法提供了更便捷的安全测评方法，进一步丰富了我国密码芯片物理安全测试方法，提高了我国密码芯片安全分析水平。

![](https://mmbiz.qpic.cn/mmbiz_png/ZPwe5TesXJDBCQRM6LTJHRibMkjqsv8foXmicVnFVp9LOiaNP9QlMcHmvmIKscpNadVroiaSdwcibKzp3uMVZAr1Gvw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Vcvo4WRFGwVAhKb9dicRicSMSDvoBFDm8eDohwuJOMvicOvrPox92yoVOV0ibcySx1z7dicRyGaxo2n2JKplovQica5puSVXzmVqyVxYHocymaQgg/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sSglg2t6pLdibP1eoMFnDyyCjXAfpDzbcSiahmcJJVCJGlVlhz3tn375M3T7671B9c4QAkhj2KBp6yynY1uOsU8w/0?wx_fmt=png)

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