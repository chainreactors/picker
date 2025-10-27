---
title: 【安全圈】AI大模型新型噪声攻击曝光，可绕过最先进的后门检测
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064269&idx=2&sn=eafa279566b3550d20241148ad8c3eac&chksm=f36e664dc419ef5b7c42f5fb851d36537453f3bd0603bedfad83c6ed7007b0d5dd20433bbd71&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-10
fetch_date: 2025-10-06T18:28:40.307276
---

# 【安全圈】AI大模型新型噪声攻击曝光，可绕过最先进的后门检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMZibEjZJxzly9sHKnBNJiaGUDXuJQkcsYicXAl5XjIibgogkZDTfclPn5eQ/0?wx_fmt=jpeg)

# 【安全圈】AI大模型新型噪声攻击曝光，可绕过最先进的后门检测

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络攻击

据Cyber Security News消息，研究人员提出了一种噪声攻击（NoiseAttack） 的新型后门攻击方法，该攻击被称为是一种用于图像分类的后门攻击，针对流行的网络架构和数据集实现了很高的攻击成功率，并能绕过最先进的后门检测方法。

实验结果表明，该攻击能有效对抗最先进的防御系统，并在各种数据集和模型上实现较高的攻击成功率。它利用白高斯噪声（White Gaussian Noise）作为触发器，创建了一种针对特定样本的多目标后门攻击，可灵活控制目标标签。

与通常针对单一类别的现有方法不同，该攻击使用具有不同功率谱密度的白高斯噪声作为触发器，并采用独特的训练策略来执行攻击，因此只需最少的输入配置就能针对多个类别进行攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMJ6js3fBicIOWzK0wBPumqLiamM72xMewgo7WicTsRWvicf60MZYKPkL9Jg/640?wx_fmt=jpeg&from=appmsg)不同数据集和模型的攻击性能

这种噪声攻击在研究中被称为是一种用于图像分类的新型后门攻击 ，利用白高斯噪声（WGN）的功率谱密度（PSD）作为训练过程中嵌入的触发器。这种攻击涉及在精心制作的噪声水平和相关目标标签构建的中毒数据集上训练一个后门模型，从而确保模型容易受到触发，导致所需的误分类。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMIHyBXwghXYb8XuVgf5tZKlkxqpn65icKePIibv56giaf0aSvEVOgOGficA/640?wx_fmt=jpeg&from=appmsg)NoiseAttack 后门训练准备的中毒数据集概览

这种攻击为创建具有多个目标标签的后门提供了一种通用方法，从而为试图破坏机器学习模型的攻击者提供了一种强大的工具。

该框架能有效规避最先进的防御措施，并在各种数据集和模型中实现较高的攻击成功率。通过在输入图像中引入白高斯噪声，该攻击可以成功地将图像错误分类为目标标签，而不会明显影响模型在干净数据上的性能。这种攻击对 GradCam、Neural Cleanse 和 STRIP 等防御机制的较强鲁棒性表明，它有可能对深度神经网络的安全性构成重大威胁。此外，该攻击执行多目标攻击的能力也证明了它的多功能性和对不同场景的适应性。

参考来源Noise Attack: A New Backdoor Exploiting Power Spectral Density for Evasion

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhQV8P7VwvC6C2P0u35FEU8BPNpEKfax3v9Y9dfpaibzEESciaYIo2kWYQzn0bc6fWJE61BvYHcFmwA/640?wx_fmt=png)[【安全圈】快手发布通报：一员工泄露数据严重违纪 解除劳动合同](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=1&sn=7db74bfc9d62a009a6499c248abe8b38&chksm=f36e65b9c419ecaf0cdc78a3af144aa01d0b017649bc07fb268f93473b3b8cf534004fa97581&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljah7YPPrtpT9kaibYksxDAMTB5caU21ic5Plo19Pcu8lzT4TF0oRBVNic0icMDSEZAXtV6uLicFXPKibcg/640?wx_fmt=jpeg)[【安全圈】抢票软件不到1秒钟就能抢到票，黑客与“黄牛”被判刑](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=2&sn=4529003433add83f1f83a867c6f50d2f&chksm=f36e65b9c419ecaf377ce825c7e167e9c16e28822331da644bd6568eef0ec3f1cdf0c324d53d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHPK1GoY0vCUh4zb9B0lGym6MibYEib4iaCL9RxWO5S8v3IuPBwJKskHCcswS7QE7PKWI4LpyGDZUzuQ/640?wx_fmt=other)[【安全圈】GitHub 上有 3000 个“幽灵账户”传播恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=3&sn=be5b899e0bea8af3b290b45b6e5ef67f&chksm=f36e65b9c419ecafca6755f32b32c1b766aa4b099e2fed984e8a28f7e5d61de2cdfd0cc7797d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhQV8P7VwvC6C2P0u35FEU8Ng0qSrxJsA2UGgb1TYs2yMuS24ndPFEQnFcj0p4VLhtgMYCyTJzriag/640?wx_fmt=jpeg)[【安全圈】冒名顶替已下架 PyPI 套件，攻击手法 Revival Hijack 揭露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064249&idx=4&sn=61ffe75ef3405adbe977dbbc80ef8dbc&chksm=f36e65b9c419ecafb8672ebf32a39376f9d6995bc07948035c2f59bd600e4b196ae547e2f765&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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