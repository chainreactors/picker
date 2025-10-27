---
title: 原创 | OPC UA .NET Standard Stack可信应用认证绕过漏洞分析
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247532214&idx=1&sn=3f16187309ec36daaa844062ec769cb2&chksm=fa93c877cde441616fda0e7930ed46bdd8227679670fe12f6824c182169be2ce232ddab464b4&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-10-26
fetch_date: 2025-10-03T20:54:52.919882
---

# 原创 | OPC UA .NET Standard Stack可信应用认证绕过漏洞分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176l24kjj4JaOhZuIKMe8icDzhAWcmia6Y4taciay6wHIvJBicicydibduWbWqJGB6xSunlr5lP449FXhodqQ/0?wx_fmt=jpeg)

# 原创 | OPC UA .NET Standard Stack可信应用认证绕过漏洞分析

原创

CISRC

网络安全应急技术国家工程中心

**漏洞概述**

OPC UA .NET
Standard Stack是OPC基金会官方维护的OPC UA协议栈的参考实现。该参考实现采用.NET语言开发，包含了可移植的OPC UA协议栈和核心库（包含客户端、服务端、配置、复杂类型支持库等）。

OPC UA协议是工业控制领域中的一种十分流行的通讯协议，启明星辰ADLab研究员在漏洞情报跟踪中发现该可信应用认证绕过漏洞（编号为CVE-2022-29865）后对该漏洞进行了深入分析和验证。

**漏洞分析**

该漏洞影响OPC UA
.NET Standard Stack的应用认证机制。根据协议规范，OPC UA客户端和OPC UA服务端是通过创建Secure Channel来进行应用层（Application Layer）的会话（Session）数据传输，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176l24kjj4JaOhZuIKMe8icDzhkcQhM566UjyeQSYGd3KHW2INfFSGe45h4pA1SFsBjlXPOxIWZHYJmw/640?wx_fmt=jpeg)

图 1、OPC UA安全架构-客户端/服务端[1]

在客户端和服务端创建Secure
Channel时，有一个应用认证机制（App Authentication），该机制是基于应用证书（Application
Instance Certificate）来实现的。具体参见OPC UA security
architecture 6.1.3【2】:

An Application decides if another application is trusted
by checking whether the Application Instance Certificate for the
other application is trusted. Applications shall rely on lists
of Certificates provided by the Administrator to determine
trust. There are two separate lists: a list of
trusted Applications and a list of
trusted Certificate Authorities (CAs). If an application is not
directly trusted (i.e. its Certificate is not in the list of trusted
applications) then the application shall build a chain
of Certificates back to a trusted CA.

OPC UA 标准规范详细规定了如何判定一个应用证书是否可信，如下图2所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176l24kjj4JaOhZuIKMe8icDzhdWnicE9vop2M2iaC2Ur3UV0iapudLW0rCiccW3B4dbd85nJdzb1ScmxfIg/640?wx_fmt=jpeg)

图 2、确定应用证书是否可信

漏洞CVE-2022-29865即是针对此证书校验机制的绕过。OPC UA .NET Standard Stack校验应用证书的关键代码位于协议栈源码文件CertificateValidator.cs的InternalValidate函数中，如下图的关键代码逻辑：

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhk7IU6u6NbUJBlbpToLED8WSjqL6UTjAvtE7ccrZtzU76u25oBvv16g/640?wx_fmt=png)

在883行处，调用GetIssuersNoExceptionsOnGetIssuer获得待校验证书的颁发者，并检查其是否为信任的证书颁发者。在该函数中，首先通过GetIssuersNoException函数来获取客户端证书的Issuer并创建证书链，然后检查证书链中的Issuer是否在自己的信任列表中。在检查Issuer过程中，调用了Match函数。

Match函数将待校验证书Issuer名称和潜在Issuer证书的Subject Name进行对比，此外还检查证书的X.509 Extension中Authority Key Identifier属性中的Serial
number和潜在Issuer证书的Serial number是否匹配或者key id是否匹配。如果issuer名匹配且serial number或key\_id中有一项匹配，则GetIssuersNoExceptionsOnGetIssuer会返回true。

Match函数调用CompareDistinguishedName进行匹配，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhDiavibQFuiaOD35OUEoT0I5Z88WZZ5HNxJArBsibEFbQCSVO5AbyyO2QPw/640?wx_fmt=png)

图 3、Match函数调用CompareDistinguishedName对比Issuer Name

但是，函数CompareDistinguishedName内部直接忽略了大小写，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzh3A7SpVI2CibFnTEXoka6zXCXKPxtibEAiaLK9Q5xBeJFzWJRhkLnibjcmA/640?wx_fmt=png)

图 4、CompareDistinguishedName忽略大小写对比Issuer Name

显然，在这个证书匹配过程中，没有对证书的签名进行校验，而仅仅根据证书的元信息进行匹配，而且在Issuer时还忽略大小写。因此，可伪造证书元信息来通过该函数校验。

在909行处，InternalValidate函数使用X509Chain进行待校验证书的证书链创建。如下图所示，该过程对证书的签名等信息进行校验，在创建后通过CheckChainStatus函数来检查证书链是否存在问题，结果在result中保存。如果证书链检查没有问题，则result变量为空。至此，证书校验的大部分工作已经完成，后续还会对证书的密钥用途、长度等进行校验。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhx9nvrziaw5Vqjpa3RsicFsU7MRR1Kq2VIsoAco91nrW2RfAxw8NDnPRQ/640?wx_fmt=png)

在CheckChainStatus函数中，将根据证书链元素的不同状态返回不同的结果。但是，对于UnTrustedRoot状态，只需要证书的签名合法，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhznjlAhThsqic3iaKJJWzXJ39THUNvN11l0NhibUjkfibI8qCZPdzl0bapQ/640?wx_fmt=png)

因此，可通过伪造证书来使验证中：GetIssuersNoExceptionsOnGetIssuer函数返回true，CheckChainStatus函数因UntrustedRoot不产生错误，从而使InternalValidate函数因正常返回而通过证书校验。

**漏洞复现**

## **复现环境**

* OPC UA Vulnerable Server

OPC UA .NET Standard Reference Server（Version:
UA-.NETStandard-1.4.368.53）

* OPC UA Client

Unified
Automation UA Expert

## **复现过程**

首先，编译OPC UA
.NET Standard Reference Server。修改配置文件Quickstarts.Reference Server.Config.xml，将Server应用证书从默认的自签名证书修改为由CA颁发的证书。然后，将CA证书添加到Server的信任证书列表中。最后，启动该OPC UA Server。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhRuwKiapTbPiaNknicMgvRuniaTDtSa7M9qica5wzU41seOqX6O36jucLrzw/640?wx_fmt=png)

图 5、配置OPC UA Server证书

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhL9CItAd85fQVop4zc3qFPU8Xj3uTcbBTt64fIPyTpZcRsrQY5PrgZw/640?wx_fmt=png)

图 6、配置OPC UA Server可信证书存储

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhHSHoWzVxPcAPiaPg9eddjZgtedudMVqsYqjWTAkIIicmOUHtytnKIOjg/640?wx_fmt=png)

图 7、OPC UA Server应用证书和CA证书

根据OPC UA
Server的应用证书信息（可在OPC UA客户端认证的时候获得），使用python cryptography库生成伪造证书，并将其设置为uaexpert应用证书，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzh79PKK9UwmwW2Ka9Af4yq0XvTqLwV2IAeQebkcSN0hMQZfnnYSY5WIA/640?wx_fmt=png)

图 8、OPC Client UaExpert使用的伪造应用证书

在UaExpert中配置OPC UA Server信息，使用上述伪造的应用证书登录成功。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhwmsVTxPCEc0jM30BBknYQwVQsxdJzRsh5GrPgBa4ptvHneWwhNe1KA/640?wx_fmt=png)

图 9、UaExpert配置Server信息

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhXWFDs5eVA00vljtAZicdkSicaSSg0CC1YXPl4vr2yuF6HmHWTBFrlsVg/640?wx_fmt=png)

图 10、UaExpert使用伪造证书成功登录OPC UA Reference Server

**漏洞修复**

根据OPC UA的官方漏洞公告【3】，该漏洞在OPC UA .NET Standard 1.4.368版本中修复。实际在Commit
51549f5ed846c8ac060add509c76ff4c0470f24d中该问题就已被修复。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176l24kjj4JaOhZuIKMe8icDzhWDqU3z0T4dKOGzqaK5Dpx5GKqjGicVGV5jFyXESy4WrvAqa6tW2NQFA/640?wx_fmt=png)

主要修复的方式如下：

1.证书信息对比采用了二进制方式对比。

2.增加了对证书链构造的校验，确保证书验证中构造的两个证书链是一致的。

# **参考：**

1.https://reference.opcfoundation.org/v104/Core/docs/Part2/4.5.1/

2.https://reference.opcfoundation.org/v104/Core/docs/Part4/6.1.3/

3.https://files.opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2022-29865.pdf

转载请注明来源：网络安全应急技术国家工程研究中心

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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