---
title: 信息安全——DES加密算法原理以及3DES
url: https://mp.weixin.qq.com/s/qjoSY2da50R3b6vK0SvLRg
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:30:35.218972
---

# 信息安全——DES加密算法原理以及3DES

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCrYMoFz1wibh81wfibiaGhyI94fGFQpiauibKv4icNKDGGMcNtvypA0rHPicRaNFHpgASJFHJPzygo6o9uUIzHDyhRYhmN9jfD2SVS3Y/0?wx_fmt=jpeg)

# 信息安全——DES加密算法原理以及3DES

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**算法简介**

DES（Data－Encryption－Standard）又称为美国数据加密标准。是一种对称加密算法（对称加密就是加密和解密用的是同一个密钥），属于采用密钥加密的块算法。DES算法要将明文和密钥分开进行处理，首先是对明文的处理，明文按64位进行分组，分组后的明文块和密钥通过DES加密后形成一个密文块，所有的密文块拼到一起输出就是密文。DES的密钥长64位，但实际上只有54位密钥参与了DES运算（其中的第8/16/24/32/40/48/56/64位是校验位）。由于DES是对称加密，就要求发送方和接收方使用相同的密钥进行加密和解密，所以在传输数据之前双方得约定好密钥。

**02**

**算法原理**

DES算法 的原理流程图如图2.1所示

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAB5Qv6jsm2XHcjulao4AD7tJkHecZUXC4FFClkQ8PGdZjhQS0Xt3WwjtwUiaEH6q5C31Cg7eicEGYhqEQjdxH1KKViaNWaCIZGoA/640?wx_fmt=png&from=appmsg)

图 2.1

**03**

**流程详解**

**（1）初始置换**

就是将原来的明文的64位二进制数调整顺序重新排列，初始置换表如图3.1所示，置换规则需按照置换表，输出的第一位的数据是输入的第五十八位上的数据，输出的第二位数据是输入的第50位的数据，依此类 推，初始置换示例如图3.1所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCc0a8CsqJjBicibDUO0WCWLu0MqXa6oynChqzdic1ic9xrBK7ib7Fu5XziaoyCnGDxke00jSsaZjvmPNy75TzNhTfLZSOaLnPHF9GcQ/640?wx_fmt=png&from=appmsg)

图 3.1

**（2）Round区域**

**a. EP（拓展置换）**

输入的32位二进制数分为八组通过拓展置换之后变为48位二进制数，拓展置换是指将每组的第一位数减一的结果作为新的第一位，最后一位数加一的结果作为新的最后一位，这样每组由原来的四位二进制数变成了六位二进制数，经过拓展置换之后形成了一个48位二进制数。如图3.2是一个拓展置换的示例

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCefVIwicX902XkYzKLZiaicSFoCdscg5wUAoaHXEUs9DQXZx2MTxYhtLtEw3ic1WVicsa4GYqxLD8fj6UmByqUcwM886d9q5Rj47OE/640?wx_fmt=png&from=appmsg)

图 3.2

**b. 异或运算**

第一次异或运算是由经处理之后的部分明文（也就是经过上一步的拓展之后的48位明文）与秘钥进行异或运算（相同为0，不同为1）

**c.S盒压缩置换**

经过异或运算之后的结果分为八组（每组六位）输入到S盒中，每一组对应一个S盒，每一组的数字由第一位和最后一位组成一个二进制数转换为十进制之后作为行号，中间的四位组成一个二进制数转换为十进制之后作为列号，经过俩组数字得到的行列对应S盒中相应位置的压缩数元素，把这个数转化为二进制之后就得到了一个压缩后的四位二进制数（共有八组，每组四位），如图3.3所示是八个S盒里的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCzLOZPyt2gIGQrReicicwa36mCGoVuhHVO0TtmPT9MaC6d1UqKUq4yDLX29cyoS3SXeytx1t0oibCX7CACfOYVLHLqpagfTDp2n0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBye1YJ5AiaDMRwsBodouD8uOgw2PQdrSJR4CCroOiccTxuMktJpp7SAhTd5qc3pDwgG12Z3tUfRbJHaNhRnjrIDVRibib4LZebcEk/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAibHz0qk5CRkQu2tdq8DOIBzicjQOlKZAJHG2PM9N5EBrUquB7B99GMACruCAJje75o7Oh4HfatIZic2lWRdJOY0OvFicF38P3dXc/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCJlf92oLuF3G5ia0lfcw1EZUAib41s0vqZus6bfvL39wjT7Dcecz9zZTG8JV5NuMBpq1LE98JiaXZOz6iaoYzrrR3lI0aesdO5X14/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCq1EpJp9YZfuOIWSXdEGvh3umyI0sZGpk055wqbqIXox6OaBjMkOd5BaamNZ3vv1DpWULibDicl5oZ1mGFZ2rOyJgLQlVGXbRTQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA5eH9EtbqV3G73WQbO2QyHQo3BleAUTUPVcZTTcSxF9Hagg2zxAnoqk1vpnmM89mvTaWIc7bGg3VCsgwdIMNwHlz01wFTXnIg/640?wx_fmt=png&from=appmsg)

图 3.3

**d. P盒置换**

经S盒压缩之后的数据要进行P盒置换如图3.4所示是P盒置换的顺序，置换规则同初始置换一样，给出的位置是置换前的数据在置换后的位置

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB6adQ6Zzp43ACVphBYzEsk7ko4SibDAQws8ZQXVvCWiav5SxrYHE95r0WicOOom8IMYYO8G9uSlGoZZ6wRup67eSBREy41lLLCtk/640?wx_fmt=png&from=appmsg)

图 3.4

经过P盒置换之后的数据要再经过一次和另一部分明文进行异或运算后一个完整的Round才执行完，最后进行输出。第一个Round的输出结果作为第二个Round的输入结果，依此类推，最后一个Round的输出结果要经过终止置换后才能得到密文

**（3）终止置换**

终止置换是初始置换的逆运算，也就是说一个二进制数经过初始置换后再进行终止置换，结果还是它本身，终止置换的表如图3.5所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC09GKdMwOfUP7agnolOwDJVQf9Qsia4egSa3o0Fd9eDeKcZI3JxOr2DicVIjGibIg4UCsLkrb5JEwJupZlroBNBeCibPicUWfRjAxo/640?wx_fmt=png&from=appmsg)

图 3.5

**04**

**密钥处理**

密钥的处理要经过三步分别是置换处理、循环左移、压缩置换，一个64位的密钥经过处理之后成为一个48位的密钥

**a. 置换处理**

同明文的初始置换、终止置换一样，也需要置换表进行，一个64位二进制数经过置换处理之后变为了56位二进制数，置换表如图3.6所示（其中没有第8、16、24、32、40、48、56、64位，他们作为校验位），将得到的56位二进制数分为两部分28位的二进制数，然后对这两部分分开进行循环左移处理

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBYPE2xmqbnCqrup9lSxibefdNG1DbnT8Lh8cAJQfMkyII4Evef7gyib6micJuYm8OPV29TicoyGM3hlWvnnEUQ7wFXnDDHB1bUibqw/640?wx_fmt=png&from=appmsg)

图 3.6

**b.循环左移**

将两个28位二进制数循环左移，然后对左移之后的结果进行合并。循环左移的位数由轮次（Round）决定（除了第1、2、9、16轮是循环左移一位，其余轮次都是循环左移两位）

**c. 压缩置换**

循环左移之后再进行压缩置换，压缩表如图3.7所示，在压缩至换中既缩短了数据位数，又改变了数据顺序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBFEXFKuJZ7MVbSqxickbAw1olqHZJiafdZliaXqd47Ql01PvcsHdUUNuWgxh2RzjxKibPe8XTykEzHIicQrlvtJJibq3luscTmMNQbc/640?wx_fmt=png&from=appmsg)

图 3.7

以上就是对密钥的处理的三个步骤，在每一轮次结束之后，将密钥用于Round中的明文处理，结束后依次对密钥再次进行以上三个步骤的处理用于第二个Round中的明文处理

以上就是DES算法中加密 的全部流程。对于解密是执行和加密一样的步骤，不同的是要倒置密钥的使用顺序，即第16个密钥用于第1Round中，依次类推。

由于DES算法思想是开源的，通过DES加密的密文其安全性完全取决于密钥，如果对其进行暴力破解还是很容易破解出来的，因此在DES之上进行改进，增加其加密操作，也就是对一个明文使用不同的三个密钥对其依次进行DES加密、DES解密、DES加密得到的密文安全性较原始的DES高一些，这个加密过程称之为3DES加密算法，其加密流程图如图4.1所示，对于3DES算法，它的加密时间要比DES多一点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB0gLVlkrvGDA3lucradBuoTrHybQB9CykQwVSUmJM6NqEia9rHPGrI2jicIualYZMq2XBCicqZ6mLyrySryicgjsEng5E5MTIkTXI/640?wx_fmt=png&from=appmsg)

图 4.1

tips：本篇文章中的秘钥默认为密钥

来源：CSDN@「码龄七年的小白·乐安兰」

https://blog.csdn.net/weixin\_45454242/article/details/127062307

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

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appms...