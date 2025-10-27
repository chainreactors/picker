---
title: 第二章 离散对数与Diffie-Hellman （练习题）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247496966&idx=1&sn=b0af543199fda960afde9533b98fe220&chksm=fa5220b8cd25a9ae143ec8542041a6a1f58922bc9fb74df6c4bd7f1101d5da8b4f537f687e43&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-10-15
fetch_date: 2025-10-03T19:57:41.189957
---

# 第二章 离散对数与Diffie-Hellman （练习题）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnT784uE3edQia5EzaT9optYjjJtbyviaHdQPXrU7MpFoicxOfL7mDicqNYAGUMgVUD9LlPmtxjWETzmHg/0?wx_fmt=jpeg)

# 第二章 离散对数与Diffie-Hellman （练习题）

原创

核心基础实验室

山石网科安全技术研究院

习题部分久等，对应内容可翻阅合集前期公众号。

下面是第二章练习题第一部分的参考答案，部分是笔者自证，所以读者若是发现有纰漏之处，还望指正（可私信公众号）。

### Section 2.2 The Discrete Logarithm Problem

#### 2.3

**假设****为****下的原根。**

（a）假设同余式  的解为 ，证明 ，且解释为什么映射

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnT784uE3edQia5EzaT9optYj3B699H6UFrweREmhOwneIXHiaUcHajXKVcuDe175Kb8zlAzNaZVYCLg/640?wx_fmt=jpeg)

是well-defined function。

**证：**已知 ，我们有 ，由于  为原根，所以其阶为 ，即 ，因此  ： This means the  is well-defined up to adding or subtracting multiples of p − 1, so the map (2.1) is well-defined.

（b） 证明

**证：** 我们有

因此 ，更准确些：

（c）证明

**证：** 我们有

因此

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT784uE3edQia5EzaT9optYjUqpYr8OhSBB83ViaUQ7R6oRgIDBFmeUzkrqmkQq0k68lnHB1hlnlp9A/640?wx_fmt=png)

#### 2.4

**计算下列离散对数问题**

（a） \*\*

**答：**

（b）

**答：**

（c）

**答：**

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT784uE3edQia5EzaT9optYjUqpYr8OhSBB83ViaUQ7R6oRgIDBFmeUzkrqmkQq0k68lnHB1hlnlp9A/640?wx_fmt=png)

#### 2.5

**设****为奇素数，****为模****下的原根。证明当且仅当离散对数****在模****下为偶数时****为模****下的二次剩余。**

**证：**证明取自命题 3.61，设

显然如果 ，那么  为二次剩余。

另外，如果  为奇数，，并假设  为二次剩余，即 ，根据费马小定理（定理1.24），我们有

然后  等价于

根据费马小定理，

所以我们会有

但这与  为原根这一假设相矛盾，因此所有  的奇数幂次都为二次非剩余。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT784uE3edQia5EzaT9optYjUqpYr8OhSBB83ViaUQ7R6oRgIDBFmeUzkrqmkQq0k68lnHB1hlnlp9A/640?wx_fmt=png)

### Section 2.3 Diffie–Hellman key exchange

#### 2.6

  **Alice 和 Bob 在Diffie-Hellman密钥交换协议中使用素数****和基数****。Alice 向 Bob 发送值****。Bob 请求您的帮助，因此您告诉他使用秘密指数****。Bob应向Alice发送什么值****，以及他们的秘密共享值是什么？你能找出 Alice 的秘密指数吗？**

**答：** Bob 应该发送  给 Alice，这样他们的秘密共享值为  。而对于 Alice 的秘密指数，我们没有一个直接的方法去求解，但是可以用 babystep–giantstep 方法去求解，最终我们可以计算出 ，所以 Alice 的秘密指数为 。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT784uE3edQia5EzaT9optYjUqpYr8OhSBB83ViaUQ7R6oRgIDBFmeUzkrqmkQq0k68lnHB1hlnlp9A/640?wx_fmt=png)

#### 2.7

  **设****为素数，****为整数。Diffie–Hellman决策问题如下。假设给你三个数字 、、****，并且假设****和****满足**

**在你不一定知道指数****和****的值的情况下，判断****是否等于****。请注意，这与前面描述的 Diffie–Hellman 计算问题不同。Diffie-Hellman 计算问题要求您实际计算****的值。**

（a） 证明求解 Diffie-Hellman 计算问题的算法可用于求解 Diffie-Hellmman 决策问题。

**证：** 显然，如果能够解决 Diffie-Hellman 问题，就能够实际的计算出 ，直接检查是不是等于  即可。

（b） 你认为Diffie-Hellman决策问题是难还是容易？为什么？

**答：** 如果不解决 Diffie-Hellman 计算问题，至少目前没有人知道如何解决 Diffie-Hellmin 决策问题。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT784uE3edQia5EzaT9optYjUqpYr8OhSBB83ViaUQ7R6oRgIDBFmeUzkrqmkQq0k68lnHB1hlnlp9A/640?wx_fmt=png)

### Section 2.4. The Elgamal Public Key Cryptosystem

#### 2.8

 **Alice 和 Bob 协商在 Elgamal 公钥密码系统中使用素数****，基**

（a）Alice 选择  作为她的私钥，那么她的公钥  是什么？

**答：**

（b）Bob 选择  作为她的私钥，那么他的公钥是 ，Alice 使用临时密钥  加密消息 ，那么 Alice 要发送给 Bob 的密文为？

**答：**

（c）Alice 使用新的私钥  和公钥 ，Bob 给 Alice 发送了密文 ，请解密。

**答：**

（d）Bob 又生成了一个新的私钥，并且公开了他的公钥 ，Alice 使用该公钥加密并发送密文  给 Bob。Eve 拦截到了该消息，请帮助 Eve 解决这个离散对数问题 ，并使用  解密获取原消息。

**答：** 同余式  的解为 ，即 Bob 的私钥，所以解密：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT784uE3edQia5EzaT9optYjUqpYr8OhSBB83ViaUQ7R6oRgIDBFmeUzkrqmkQq0k68lnHB1hlnlp9A/640?wx_fmt=png)

####

#### 2.9

 **假设Eve能够解决Diffie–Hellman计算问题。更准确地说，假设 Eve 得到两个值****，并且她能够计算****。请说明 Eve 能够打破 Elgamal 公钥密码系统。**

**答：**在Elgamal 公钥密码系统中，Alice 的公钥为 ，密文：，其中  是 Bob 的临时密钥。由于 ，因此如果 Eve 获取了  能够计算  的话，那么他就能够通过计算  来解密密文，获得明文。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT784uE3edQia5EzaT9optYjUqpYr8OhSBB83ViaUQ7R6oRgIDBFmeUzkrqmkQq0k68lnHB1hlnlp9A/640?wx_fmt=png)

#### 2.10

 **这道题描述了一种公钥密码系统，要求 Bob 和 Alice 交换多条消息。我们用一个例子来说明这个系统。**

  Alice 和 Bob 确定一个公开素数 ，而其他使用的数值都是私密的。Alice 准备传输她的消息  ，她选择一个随机指数 ，计算并发送 ，Bob 选择一个随机指数  并发送  给 Alice。Alice 随后计算  并发送给Bob，Bob最后计算  即可恢复 Alice 想要传输给 Bob 的消息：。

（a）解释为什么这个算法可行，Alice使用了  作为指数，他们有何相关；同样的， Bob 的指数  又有何关联？

**答：**Bob 和 Alice 的指数满足

（b）使用变量表述该系统，并证明其在一般情况下有效。

**答：**Alice 选择一个满足  的整数 ，并计算 ，发送给Bob

Bob 选择一个满足  的整数 ，并计算 ，发送给Alice

Alice计算  在模  下的逆元  并计算 ，发送给Bob

Bob 计算  在模  下的逆元  并计算

为了证明最后一个等式成立：

由于  在模  下互为逆元，  在模  下互为逆元。根据费马小定理我们有

（c）与Elgamal相比，这种密码系统的缺点是什么？（提示：Alice和Bob必须交换多少次数据？）

**答：**ElGamal 只要求 Alice 给 Bob 发送一条消息。这个新密码系统要求 Alice 向 Bob 发送两条消息，Bob 将消息发送回 Alice。因此，这种新密码系统比起 ElGamal 需要更多次沟通。

（d）这个密码系统比Elgamal有什么优势吗？特别是，如果 Eve 能解决离散对数问题，她能破解它吗？如果 Eve 能解决Diffie–Hellman计算问题，她能破解它吗？

**答：**这种新密码系统的优点是比起 ElGamal，Alice 和 Bob 透露的信息要少一些。当然，如果 Eve 能解DLP，那么既然她知道 、 和，她就能解  并恢复 ，然后她就可以计算  来恢复 。

  然而，如果 Eve 知道如何解决 Diffie-Hellman 计算问题，她似乎没有一个简单的方法来打破这个系统。因此，如果 DHP 比 DLP 更容易求解，这种新密码系统可能比 ElGamal 更安全。

关注公众号，开启更多精彩内容~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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