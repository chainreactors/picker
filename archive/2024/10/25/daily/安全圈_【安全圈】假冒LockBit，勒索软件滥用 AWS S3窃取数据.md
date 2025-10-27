---
title: 【安全圈】假冒LockBit，勒索软件滥用 AWS S3窃取数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065447&idx=3&sn=17066f0904fe5e34fa4fc9bd7c2caf67&chksm=f36e62e7c419ebf1e412505adcd61886d5de049f5a5e80fceb1a858b18a44693afac674d7fde&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-25
fetch_date: 2025-10-06T18:52:10.196581
---

# 【安全圈】假冒LockBit，勒索软件滥用 AWS S3窃取数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljChO1pW8DeTrvJ4hzjZicC1S1mdr0rau7LmoYl1ZXm4ltkauPNdCOENytWqPhBn1WqgDq2xLzxgiag/0?wx_fmt=jpeg)

# 【安全圈】假冒LockBit，勒索软件滥用 AWS S3窃取数据

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

勒索软件

据The Hacker News消息，有攻击者正滥用 Amazon S3 Transfer Acceleration 功能实施勒索软件攻击，并将 Golang 勒索软件伪装成臭名昭著的LockBit，以迫使受害者支付赎金。

趋势科技的研究人员称，勒索软件工具被发现嵌入了硬编码的AWS凭证，以方便将数据外泄到云中，表明攻击者正越来越多地利用流行的云服务提供商来实施攻击活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljChO1pW8DeTrvJ4hzjZicC18MdhTH6wMJCe7Qsu6f2vqAicicYg8DacyQgbFzOwAmFJZTHlD4GyFEVg/640?wx_fmt=jpeg&from=appmsg)攻击流程

据推测，该活动中使用的AWS账户来自攻击者自身所属，或者是被泄露的账户。在向 AWS 安全团队进行披露后，已确认的 AWS 访问密钥和账户已被暂停。

趋势科技表示，已检测到30多个嵌入了AWS访问密钥ID和秘密访问密钥的样本，表明恶意软件的开发工作仍在进行中。目前还不清楚这种跨平台勒索软件是如何发送到目标主机上的，一旦被执行，就会获取设备的通用唯一标识符（UUID），并执行一系列步骤生成加密文件所需的主密钥。

初始化步骤之后，攻击者会枚举根目录并加密与指定扩展名列表相匹配的文件，但在此之前，攻击者会通过 S3 Transfer Acceleration (S3TA) 将文件渗入 AWS 以加快数据传输。

加密文件完成后，勒索软件会将壁纸更改为显示有LockBit的图像，以此让受害者误以为自己被强大的LockBit勒索软件攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljChO1pW8DeTrvJ4hzjZicC1lgicm4ltQMQESuDBjF1MVvBJJzn46ibb7I48vrUBCcvfNx0CqsKXsUFQ/640?wx_fmt=jpeg&from=appmsg)显示LockBit 2.0字样的壁纸

研究人员称，攻击者还可能把他们的勒索软件样本伪装成另一个更广为人知的变种，因为越是知名的勒索软件，其使受害者越容易支付赎金。

在今年2月多国执法部门针对LockBit 基础设施进行联合打击后，该恶意软件活动已经缩减，但其他勒索软件如RansomHub、Akira已越发活跃，后者在年初短暂地单独进行数据窃取和勒索攻击后，又转回了威胁更大的双重勒索战术。

参考来源：Ransomware Gangs Use LockBit's Fame to Intimidate Victims in Latest Attacks

***END***

阅读推荐

[【安全圈】水军狂喜？Claude AI现在可以控制PC并自己移动鼠标完成任务操作](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=1&sn=b934e5d1eacd20db87c29744a60e9747&chksm=f36e62d8c419ebcee92754914fb085938a5fd00ef2e9c04cb09422f2cfe22a02973d1a40af0e&scene=21#wechat_redirect)

[【安全圈】高通64款芯片存在0Day漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=2&sn=c5c869e24ab938b185e97679ede50f75&chksm=f36e62d8c419ebced3dfe7c7c112dd6fa9c2cce62710befa6d8ed1a4619a93818b4963036f5a&scene=21#wechat_redirect)

[【安全圈】K8s曝9.8分漏洞，黑客可获得Root访问权限](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=3&sn=8dd024db6fb200b80ea9bd4b0ab86a5a&chksm=f36e62d8c419ebceefe101ff0bc1b587b6e99447dcd96e41f562f8cf9aa4303b7eec61418712&scene=21#wechat_redirect)

[【安全圈】三星设备曝出高危零日漏洞，已在野外被利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=4&sn=e821667ba35126b55834a52a98cbf559&chksm=f36e62d8c419ebcee6861d148234c4240e97f32ff3ae4d2ecce99feef2c26006edc5b720092f&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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