---
title: 汽车网络安全：SHA算法详细解析
url: https://mp.weixin.qq.com/s/o5mqG_6yFlAcnCDFdflbXQ
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:47:56.497307
---

# 汽车网络安全：SHA算法详细解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDHVkur8WKddcbI4jVNiapkXqk1bRyDyvLWicI55d4kjKqS0fnSiankHlwdYExS7ePnQw52qKgyzjxKzpjKeMnpNwHds9vW3T610k/0?wx_fmt=jpeg)

# 汽车网络安全：SHA算法详细解析

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575811&idx=2&sn=55c140dd2df955df133478463dd59bbf&scene=21#wechat_redirect)

**01**

**概要**

1.定义：

Hash函数将长度可变的数据块M作为输入，产生固定长度的Hash值h=H(M)。

2.特征：

（1）可变长度输入，固定长度输出；

（2）不可逆；

（3）小概率发生碰撞，只能减少碰撞概率，无法避免碰撞；

3.应用：

（1）消息认证；

（2）数字签名；

（3）登陆认证；

（4）入侵检测和病毒检测；

（5）构建伪随机函数和作为伪随机数发生器；

4.密码学Hash函数的安全性需求：

（1）固定长度输入，可变长度输出；

（2）效率高：哈希过程简单；

（3）不可逆；

（4）伪随机性：输出

（5）抗弱碰撞性：对给定的x，找到满足H（x）=H（y）且x≠y在计算上是不可行的；

（6）抗强碰撞性：找到任何满足H(x)=H(y)的数对（x,y）计算上是不可行的；

（5）和（6）可以理解为哈希函数碰撞是小概率事件。

主导有如下哈希算法：

SHA-1、SHA-2和SHA-3是美国国家标准与技巧研究所（NIST）发布的安全散列算法家族，用于生成固定长度的哈希值，常用于数据完整性验证和密码学应用。以下是它们的简要介绍：

* ‌SHA-1‌：由美国国家安全局（NSA）设计，于1995年发布。它生成160位（20字节）的哈希值，呈现为40个十六进制数。但SHA-1已被证明存在安全隐患，2017年被正式攻破，不推荐用于安全敏感场景。‌12
* ‌SHA-2‌：这是SHA-1的继任者，于2002年发布，包括SHA-224、SHA-256、SHA-384和SHA-512等变体。SHA-256是其中最常用版本，生成256位哈希值。SHA-2算法目前应用广泛且相对安全，其设计通过消息分块、预处理和迭代压缩函数来增强抗碰撞性。‌23
* ‌SHA-3‌：作为SHA-2的补充，SHA-3于2015年发布，基于不同的内部结构（海绵构造），给予与SHA-2类似的安全性。它包括SHA3-224、SHA3-256、SHA3-384和SHA3-512等变体。尽管SHA-3在理论上更抗量子计算攻击，但实际应用较少，尚未成为主流。

今天，这篇文章关键讲解SHA256的算法实现

**02**

**SHA256**

**2.1 SHA256简介**

SHA256是SHA-2下细分出的一种算法

SHA-2，名称来自于安全散列算法2（英语：Secure Hash Algorithm 2）的缩写，一种密码散列函数算法标准，由美国国家安全局研发，属于SHA算法之一，是SHA-1的后继者。

SHA-2下又可再分为六个不同的算法标准

包括了：SHA-224、SHA-256、SHA-384、SHA-512、SHA-512/224、SHA-512/256。

这些变体除了生成摘要的长度 、循环运行的次数等一些微小差异外，算法的基本结构是一致的。

回到SHA256上，说白了，它就是一个哈希函数。

一种从任何一种内容中创建小的数字“指纹”的途径。散列函数把消息或数据压缩成摘要，使得资料量变小，将数据的格式固定下来。该函数将数据打乱混合，重新创建一个叫做散列值（或哈希值）的指纹。散列值通常用一个短的随机字母和数字组成的字符串来代表。就是哈希函数，又称散列算法，

对于任意长度的消息，SHA256都会产生一个256bit长的哈希值，称作消息摘要。

个长度为32个字节的数组，通常用一个长度为64的十六进制字符串来表示就是该摘要相当于

来看一个例子：

干他100天成为区块链程序员，红军大叔带领着我们，fighting!

这句话，经过哈希函数SHA256后得到的哈希值为：

A7FCFC6B5269BDCCE571798D618EA219A68B96CB87A0E21080C2E758D23E4CE9

这里找到了一个SHA256在线验证软件，可以用来进行SHA256哈希结果的验证，后面也可以用来检验自己的SHA256代码是否正确。用起来很方便，不妨感受下。

**2.2 SHA256原理详解**

以输入“RedBlockBlue”为例，它对应的二进制码是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDLXRBLHgdLYlmFdjvJpBA834r4zzDGfCqQb7TMxAcxYmm8OtPr92opJOwbBeGJjNLALzJiaE7ibkYngqSnFZRpteKuvFpNxJDhQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBt9cvFTh6zfXKgdlET1pbr2tbGCAPF48iak0ofEibiaAFRkEn8cTPjclg8TPHTfa7eWLMeAD08uqlsP3YMQ8doEicXgj1dqo9cibyQ/640?wx_fmt=png&from=appmsg)

**2.2.1 预处理**

1、我们要求的输入是512的倍数

目前的长度是96bit，所以我们向上取整到最接近的整数：512bit

在输入末尾添加一个1，接着不停添加0，直到距离512的倍数还差64bit: 512-448=64

剩下的64bit，用原始输入长度编码为64位二进制

举个栗子：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBJmcY5B6xTzpF3kyQp8BWkRR18qB2O4byKXNo1Ej3B2Gvdp30GYdA05Uhhug4y48nbdlcnkicmibTcFo3tz4oMwoVbcEIWibszVU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD46jYVdibyJiaicZMugbm11KG9RqYmpLaxG7KbP7IJf5gfwYbLBu7icADVGowqHAzDIWMfeh5zy1CLnfN9oJZLRblQ5WIX0tAsHos/640?wx_fmt=png&from=appmsg)

回到我们的例子中

“RedBlockBlue”的二进制码是：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBxar2u5g67yQz0kFy4YBTzOPFHP5NVMKJNnPKbWjarUKmwzQzV4fPkOTM2iceia7d9zLgic8AfeYSD5XDaJiaI5iatg38q3mhR167I/640?wx_fmt=png&from=appmsg)

填充好是

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDN9ibJ7wqicj0egHH1fT2T6muDGU7mVUGm0EffWKYiaC9opL1mvU2gLlGH8EmBgNCicoZBSyk0s0GP2UxTxXU31U2mgPxDJMO5QJY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCqicDCmu6ehgmjbuRw6aIyviaiaohEEaopO9G6ZZdXOibwybNkexPVt7NVU7qM2gyyxTicfXIiawrDTNic5cdiamZ6VrITRBMTPTnib7uA/640?wx_fmt=png&from=appmsg)

**2.2.2 消息分块：把输入分成512位的块**

因为在我们的例子中输入只有512位，所以我们只有一个块

把512位的块分成16个32位的字

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaByOLxx8HBA9ibfpF4YTWHSbsYexlVK8Lk3XhR5a3jm9sdXSicn7v2qJFO93cibCXLQr8abLopEoJdrUDHPecCAzKtHIFJDt1fial8/640?wx_fmt=png&from=appmsg)

**2.2.3. 设置初始值： 哈希值**

总共有八个，每个哈希值32bits，也就是总共256bits

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDXAX4U0Jy4crUqQedUnnibzZrI1EiajcIm8g6icCJbzbO07ToeuBokjf1iast9hAoYWWzhRlDic72TyJ9VxG6Z9lkCBkWaKjgLxD2c/640?wx_fmt=png&from=appmsg)

这些数字从何而来呢？

取前8个质数（2,3,5,7,11,13,17,19）的平方根的小数部分的前32bits

第一个质数是2，它的平方根是

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCwDeiaa2XQ2IpoictHwuXNMpf1wEiaocEYJLurAzquPaeRdAktaKBvR2YALPmOfNfhIUPs7LIQaXDztFEBhxNAg3ynS5eh66skRk/640?wx_fmt=png&from=appmsg)

取它的小数部分

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD4OB92aZueex5TOSfUwev5e1EVINPCN8RtBc7yzxZpD0xRl7sWHrNdueibPEsrSJxsyicQPvWzIeaBOz2yucccR2y31licjUNPVE/640?wx_fmt=png&from=appmsg)

将其转换为二进制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBEnHT4gyicPpfw1ynMzheeH8f5ibhSibCIiadgN64dH7FZpERy83nOOZK2kEXaJAjicGMldjLGSj352ucQBEEP0aL2vJIJCmWYEPzk/640?wx_fmt=png&from=appmsg)

**2.2.4 64个常量**

在SHA256算法中，用到的64个常量如下

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBiakl4ict0ndF91iam7m1P6FrwniaqGTJImIrGgU5LWP0OXib10yLF6r7BYwyRFmgCicbUA8gm1B4gOibpWwA6WHDCBnRKFnO7q0xgsA/640?wx_fmt=png&from=appmsg)

对自然数中前64个质数

(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97…)的立方根的小数部分取前32bit而来就是和8个哈希初值类似，这些常量

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBl6RjIIyZMGON64kyhFEJz70eoUliaVef8zibVCsfIQvJSREJPFmWPbYIwbCe0FseFgOIMvgZRmLy3WD34MQfhD8Bgk5vgJawib0/640?wx_fmt=png&from=appmsg)

**2.2.5 逻辑运算**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCZdFgI8QUx1kYYia33El0lWmWSa8c1g49j573ibPic1yUjOatiaLmrqiavn1xzq13qosicjZFkLVoGoUibC2bJeG5Ltjn1YsUTibFClibQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDlmbLA4Aiahxz2Ww5vvOAaTYG2cOibQpazYibAllsVzZNvPgg0P3E9nmJW2XnffbORQcWcbzMKQENwkicB36BwGXkzFf0skJeSNVc/640?wx_fmt=png&from=appmsg)

W0到W15，

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAV2iaaahfsIoQTIiaTCmy5atCmN0icJBQGVaQMdyZRNkUdtDuhxMP8PibrtpJUxAGow5ms9DR7LuQJY5yIb8a63jeaiby11BR8bkxk/640?wx_fmt=png&from=appmsg)

W16到W63，由以下工时迭代计算得出

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaABRkTahCzhrv5uD4BW3gxhKxyx8xkrsXMR0Csd9kicWDeWdDxdPM8nYq22hTH77xrQJZdXd4DlysyS3ZVBd9XOaialKtEkO3eFU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAiazTib0Vnqwru6GicY9fQM6QxFmxEInEXkbcMzic1gkhMM9uHdIeBjBmk0LnOLRKMt4pvicaOojnxUBBAMKyueXfGxiblh9mBK9ylU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCm2nqyo0VtupIuR4V3GBvg0tWtUDA47dsrWqqqCJf4N2fhh7dmQg2sbHkA7mTOicWPibiaxmXrTXibRygYJz88M8aiaVXZffWVJmp0/640?wx_fmt=png&from=appmsg)

假设x值如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAfrKp4CwlcJtXsJR2WN9KpKUtt9Y4ib71CHxee4QalQka1H0Z0ViawLTCcaibDoFicAsWqSW2NARsvFNzbbxsQWUtMfsTgLTrGrDc/640?wx_fmt=png&from=appmsg)

首先对x进行循环右移7位

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDhbdfkwMURTnkTsBM7LUuIUQDvhZgOKlRzRob0OG6yu7YPwtopruLruCJibeMuICnDibpXTEoVicQgWDE9sDl3BZPQria89DsnbBM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAB9ricibialBUOO5008Iib5msxiax8BTE9SUW1LIstgLvjJdGUxyWcVFbCTKXcKRCzKic3KAicwV2JCM9sSsA63KZcbdkcF3lxcnIDxU/640?wx_fmt=png&from=appmsg)

对x进行循环右移18位

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCURyxhRkyot8zHlib7ngV6GpCzz1VxlgNNJjn6IFPPSz8ggT0Pj7shPnsRDhoGRXZu4veoUaJNfPM8oOKV60pzYKxcXkT44icnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCmicPbrP5ZvQc8JmIybs7RYgXZSlutJghzGVJ6a4un0SSP5a0Wd8NH6S4bsayb9C7FdnyuxriaTRbU3QUibDiaia7fBYRpX78ywiaAM/640?wx_fmt=png&from=appmsg)

对x进行右移3位

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBOIxLAEh8icH2uv3D7coAoSU3WgfmPf9YIxib9B4U38Xt389M0WbiaibJKAMDbpxl6oqNhmBrficPLd8xdd5xqQ5eIXjKIvoppY8vo/640?wx_fmt=png&from=appmsg)

最终“异或”算法：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB7GSzfwJG3dUsXSyGpcEqPhbewyQCU2xPdIziav903GFibTia7dcvxgVdqlkZCb1ENBDDCLSfJo6zNWdhxc2XmTHCIoWpmFYMZVM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCugPGNVxN63YKsuvnBOecJnTlIKMjCBbOvPoGlMng7Ljas92ztIbpabO9YJ8BwuiaE9AjrBiaWOBsn04uK5VFCLP47OWIqg8xh0/640?wx_fmt=png&from=appmsg...