---
title: 【软考网规】第一章计算机网络基础
url: https://mp.weixin.qq.com/s/zH2C6HYL04wbjQTNpMawMw
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:26.488304
---

# 【软考网规】第一章计算机网络基础

# 【软考网规】第一章计算机网络基础

原创

成渝Sec
成渝Sec

成渝Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKICskbgBZNZcrBrm7psTGwcSzTFGgJ6nlNictshJzdGNIVaA33H3K5NQBVxBYkBwslKPMCVxAaCGKRWibOsxJag1iaoCTpDsbeEdC8/640?wx_fmt=png&from=appmsg)

### **软考与证书**

计算机技术与软件专业技术资格（水平）考试，简称软考。

这是由国家人力资源和社会保障部、工业和信息化部领导下的国家级考试，其目的是科学、公正地对全国计算机与软件专业技术人员进行职业资格、专业技术资格认定和专业技术水平测试。

## **第一章 计算机网络基础**

## 计算机网络是计算机技术与通信技术相结合的产物，是信息收集、分发、存储、处理和消费的重要载体。计算机网络作为一种生产和生活工具被人们广泛接纳和使用之后，对人类社会的经济、政治和文化生活产生了重大影响。本章讲述计算机网络的基本概念和体系结构、数据通信基础知识、局域网与无线通信网络以及网络管理等理论基础知识。

### **1.1考点分析**

本章主要介绍网络基础，考试主要以选择题形式出现。重点掌握OSI、TCP/IP模型。

### **1.2 计算机网络分类**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKICZbkcctOVsjfMITaMdbOicibJpGrzGSja6MgibNEAUfc0ftqO9JCeoIS14PJGKkVtcUib8WwrGduwoYeoLf1VXPeibict57gxoEtDV8/640?wx_fmt=png&from=appmsg)

#### **1.2.1计算机网络分类1：通信子网与资源子网**

通信子网：通信节点（集线器、交换机、路由器）和通信链路（电话线、同轴电缆、无线电线路、卫星线路、微波中继器和光纤缆线）。

用户资源子网：PC、服务器等。

#### **1.2.2 计算机网络分类2：网络TOP结构**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIC6Y9TFtjW0yQxX3TcdLM1dHyLRx9U1BNC4J0VSsApx7ztaiaMWQC14qsqgY1S0Lic5of8vAHtMyVgFaveSGd65ic3uERxjRn1Gyk/640?wx_fmt=png&from=appmsg)

#### **1.2.3 计算机网络分类3：LAN MAN WAN**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIC0oYe3JVxb0vRZxu0NUMibFcicY0Iur2GGFu1UFllNacd48yMRuDr1eUYz9iaajaJicueWawZMrFjPD0ExKABnI7jL2v0MxuZrGe0/640?wx_fmt=png&from=appmsg)

#### **1.2.4 其他分类方式**

按照交换技术：电路交换网络、报文交换网络和分组交换网络。（选择题考点）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAjhQbqyFiau7xPxy0NuhJgOXBuv5roK1DJz91X43IEt8lQdqWbwFicdLbslHASibxFCqF3r8G2tOW3zDuzx6yOLxhAJBzA1N6H6c/640?wx_fmt=png&from=appmsg)

按采用协议分类：IP网、IPX网等。

按传输介质分类：无线网和有线网，有线网又能分为双绞线网络、同轴电缆网络和光纤网络等。

按用途分类：教育网络、科研网络、商业网络及企业网络。

### **1.3 OSI和TCP/IP参考模型**

#### **1.3.1 OSI参考模型：CPU/内存/硬盘/显卡/主板等标准化**

某一层所做的改动不会影响到其他的层，利于设计开发和故障排除。通过定义在模型的每一层实现功能，鼓励产业的标准化。通过网络组件的标准化，允许多个供应商协同进行开发。允许各种类型的网络硬件和软件互相通信，无缝融合。促进网络技术快速迭代，降低成本。

#### **1.3.2 OSI参考模型**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAyVgglzibp7tJoTAyQXEeb6hiaXmFj5IvUlxZfWzxcfaInjnPzrty4Fb62vEUf04UteeDXNFhibg2jdeJnUZmdkkCUdiasRBjcKys/640?wx_fmt=png&from=appmsg)

#### **1.3.3 TCP/IP模型**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAqVxTA3gZCAmDYLNLASJRwxb1nn4MEBqyO2kO1CbgMWRITic0UG7qBaw6ft3pggIITRbHylVT5icFXjWt4ZWSZaMkDknicXsvy9U/640?wx_fmt=png&from=appmsg)

1.3.4 TCP/IP各层功能

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKID2EnXluiaJzPyDAzxXj5363LUAATI3PJzV175ASLO6d9AE06F0fjl2EFL6ns1nN3nQCoe5PibQHKHbbBamL4l96A7ibfMQ1ia76HI/640?wx_fmt=png&from=appmsg)

#### **1.3.5 TCP/IP参考模型对应协议**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDMEbnVdMwgibTficCmRV8Bd5fPojHUbB0SpSWVnvANLTwKl3WCzMelfKSoMYIRvdRxnORMMKaOkmOBiben9iaRyuqJicqS6nHFOy9c/640?wx_fmt=png&from=appmsg)

### **1.4 数据的封装与解封装**

#### **1.4.1 借助OSI模型理解数据传输过程（封装）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICRbMQPkkgxQQxVHaRYTib5ExdoPs5VeodKeV3Qw7EEmicJNfFG1hibgJ7JhtgibMgOcEckl53HQHdEvNghtYj8W72doiaImM843HXU/640?wx_fmt=png&from=appmsg)

#### **1.4.2 借助OSI模型理解数据传输过程（解封）**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIArmkNB4nX2Ya2oXwPjADL0XiaFInO5YFJyUmhmm9yQavd54n22DNcBQlibXo3Vh5ddWcWOtcJpclY819ibPBX1wG7rHBLTKic0tgo/640?wx_fmt=png&from=appmsg)

### **1.5 真题**

即学即练·网规2016年11月第11题

（1）数据封装的正确顺序是（C）。

A.数据、帧、分组、段、比特

B.段、数据、分组、帧、比特

C.数据、段、分组、帧、比特

D.数据、段、帧、分组、比特

答案：C

即学即练·网工2005年11月第18-19题

（2）在ISO OSI/RM中，（18 B）实现数据压缩功能。在OSI参考模型中，数据链路层处理的数据单位是（19 B）

（18）A.应用层    B.表示层 C.会话层    D.网络层

（19）A.比特    B.帧    C.分组    D.报文

答案：B    B

即学即练·网工2021年11月第13题

（3）在OSI参考模型中，传输层上传输的数据单位是（D）。

A.比特    B.帧    C.分组    D.报文

答案：D

**![图片](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)如果文章**对你有帮助，请关注我的公众号：****

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4U7y70dsprCjIyYyHgQufrWbicAMWEzOdQGaibvZL3xqtoYyyrmWzhOWSFTJ84u4UwKb6FicXF3DHxiakOAjPw0eHg/0?wx_fmt=png)

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