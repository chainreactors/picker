---
title: AES加密过程白话版解析
url: https://mp.weixin.qq.com/s/-X8y4Vc5cv-x4XKUjxdx4w
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:28:11.498741
---

# AES加密过程白话版解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDJ8TSgjp6vFVicmQFEuuvjbNma2OlEqFsp6AVfic2uSCoImvUKCPsMWYUOde2hPswkVmZa3dHqCe27uYoPsiaJwXl3WvaqmSrxwg/0?wx_fmt=jpeg)

# AES加密过程白话版解析

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于Autosar汽车电子进阶
，作者initiallizer

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Y2Txlt70icdZCwxkb0rL3RKI5wEAVUfGd9vaoz8NNTRQ/0)

**Autosar汽车电子进阶**
.

多年汽车电子软件开发工程师，CSDN专家博主，专注于Autosar汽车电子软件开发分享，包括但不限于诊断，通信，XCP，模式管理，功能安全，信息安全等，渡己渡人。

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

AES(Advanced Encryption Standard)算法是一种对称加密算法，由美国国家标准与技术研究院（NIST）在2001年发布，旨在取代早期的数据加密标准（DES），并提供更高的安全性，目前该算法被广泛应用于各种安全需求中，AES算法以其高度的安全性和效率成为目前最流行的对称加密算法之一。

其实网络上有很多前辈已经写了很多关于AES加密算法，模式，填充规则等文章，但是大家的侧重点不同，在系统学习时很难把这些知识串起来，所以才有了本系列对AES不同加密算法，加密模式，加密原理，填充算法及AES-CMAC算法的系统介绍，本文先对AES加密过程及模式进行介绍，本文大纲如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIF4mC70UKpktn8lrH9tKtJxiaicfichLpexCso1tI04O3FrweibLD7yWRkww/640?wx_fmt=png&from=appmsg)

**0.1AES加密算法的加解密基本流程**

AES加解密基本流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFIhNRnDNEfmpSavqunfUoM1VrxFUPFAQv4PMPVh9nhwuTvTmfWhQMFw/640?wx_fmt=png&from=appmsg)

AES加密函数为E，则 C = E(K, P),其中P为明文，K为密钥，C为密文。

AES解密函数为D，则 P = D(K, C),其中C为密文，K为密钥，P为明文。

**0.2不同AES算法区别**

AES根据密钥长度的不同有：AES128，AES192，AES256三种算法，对应的密钥长度分别对应于AES-128、AES-192和AES-256三种变体，区别如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFHlJTcQWYcTWOoPQDvFUCNxE1TKsIHggQPvrvqpicroVhiaw1Mwq9wewQ/640?wx_fmt=png&from=appmsg)

**01**

**AES加密过程介绍**

在加密前首先需要选择加密模式及当最后一个block需要填充时的填充算法，之后即可开始密钥扩展，对明文分组处理及多轮加密的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFiaFoe4DB8WITEIaTR6SqccicxkkMbElRrwjWkicsCxW1es9bwaGZOkvPQ/640?wx_fmt=png&from=appmsg)

**1.1密钥扩展**

根据密钥，通过密钥扩展算法扩展生成每一轮操作所需的子密钥。扩展密钥生成方式：

AES首先将初始密钥输入到一个4\*4的状态矩阵中，k0~k15，将每一列的字节组成一个字，如k0~k4，组成W[0]，接着将W数组扩充四十个新列，构成44列扩展密钥数组。

扩展新列的产生方式：

1.如果i不是4的倍数，那么第i列由如下等式确定：W[i]=W[i-4]⨁W[i-1]；

2.如果i是4的倍数，那么第i列由如下等式确定：W[i]=W[i-4]⨁T(W[i-1])，其中，T是一个函数，由字循环、字节代换和轮常量异或部分组成。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFXWnRNfJmexD9rEar8c7XjYxm9s3h4akkUnwXYuIvoRGicsc9zfybezQ/640?wx_fmt=png&from=appmsg)

**1.2分组处理**

将待加密的明文按照分组长度（128位）进行划分，得到多个分组，对于最后一组需要根据对应的填充规则进行填充。

**1.3多轮加密**

对每个分组进行多轮的迭代操作，包括字节替代、行移位、列混淆和轮密钥加等步骤，最终得到密文。以AES128加密算法为例，其加密过程为：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFY9KUKTRbgthguAUiauPwDbs1Gdpqpygy2BvLQMnHicq8hibZ1QL4xf1lw/640?wx_fmt=png&from=appmsg)

十轮的加密过程如下：

1）在第一轮迭代之前，先将明文和原始密钥进行一次异或加密操作；

2）加密的第1轮到第9轮的轮函数一样，包括4个操作：字节代换、行位移、列混合和轮密钥加。

3）最后一轮加密字节代换、行位移和轮密钥加，但不执行列混合。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFRfJDexf5856ibDFZsR638ibLgP7TDnk6uT1j2ICtQRp8u2STpdzWgrSw/640?wx_fmt=png&from=appmsg)

**02**

**几种加密方法介绍**

**2.1字节替换**

字节替换： 属于非线性替换，具体为通过一个替换表（S盒）对每个字节进行查表替换，查表时将每一个字节的前4位作为行值，后4位作为列值，去S盒查找，进行输出。

如下为S盒（x表示行，y表示列），例如字节为0x14，那么前四位的16进制为1，后四位的16进制为4，去查找s盒中的第1行第4列的值，可以看出为0xfa，就把原先的字节0x14替换为0xfa。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFiaNXaebjuKoHT2LnC5lf9ibgvHJMiaKyvmHWTKkonsAfGLzCplXJPica4Q/640?wx_fmt=png&from=appmsg)

解密过程与此相同，唯一就是采用的是逆S盒。

**2.2行移位**

对于4\*4的矩阵，操作为：第n行循环左移n个字节，如第0行保持不动，第1行循环左移1个字节，第2行则循环左移2个字节。解密过程变为循环右移，每行移动字节数与加密过程相同，如下为示意图。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIF33SZbibnybxCIHqo9vHk2QmUd0xwHa5rEojScIBj5LEH0HlkajY5fDw/640?wx_fmt=png&from=appmsg)

**2.3列混淆**

实际上为4\*4的矩阵与另一个4\*4矩阵异或相乘（右乘操作），重新得到一个4\*4的矩阵，如下图所示。

解密过程为重新与此矩阵异或，因为两次异或得到的值为原数据本身。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFLblWzYzRdOm58cNz4fBC4z55DgJsQnH8NGkeNeTjOkdXrbkrbT0ib4w/640?wx_fmt=png&from=appmsg)

**2.4轮密钥加**

轮密钥与状态矩阵进行逐比特异或操作。轮密钥由1.2.2章节中种子密钥通过密钥编排算法得到的，并且轮密钥长度与分组长度相同。解密过程与之相同，两次异或得到原始数据。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw89oOBe3IRGPREuftMubzIFIeDpdEv9FkwsRicXiad9hWm0f8TQKVOv5wicmiclicsIldT8nv0WrtnIicMw/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/mmbiz_png/3...