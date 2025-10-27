---
title: 浅谈云安全 | FreeBuf甲方社群直播回顾
url: https://www.freebuf.com/fevents/370512.html
source: FreeBuf网络安全行业门户
date: 2023-06-29
fetch_date: 2025-10-04T11:48:10.446360
---

# 浅谈云安全 | FreeBuf甲方社群直播回顾

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

浅谈云安全 | FreeBuf甲方社群直播回顾

* ![]()
* 关注

* [活动](https://www.freebuf.com/fevents)

浅谈云安全 | FreeBuf甲方社群直播回顾

2023-06-28 13:23:48

所属地 上海

伴随新技术的诞生，新的安全问题陆续浮现。如今，各行各业正在掀起上云狂潮，云安全的概念随之爆发。

企业对云安全的市场需求也逐步迎来爆发期，越来越多的企业开始增加对安全方面的投入，同时细分领域和场景的安全实践推动云安全市场需求水涨船高。

6月27日，互联网科技运维经理王明松在FreeBuf甲方社群第十二期内部直播中担任主讲嘉宾，以“浅谈云安全”为主题进行分享，带大家系统的了解云安全。王明松讲述了云与传统IDC架构的区别、分析了云上安全的一些特点、并举例了一些经典的云安全"坑"，以帮助更多企业的安全人员轻松上手云安全。

![1687923760_649bac302cde68699221b.png!small](https://image.3001.net/images/20230628/1687923760_649bac302cde68699221b.png!small)

## 一、云服务的责任共担模型

AWS责任共担模型可以减轻客户的运营负担，因为 Aws 负责运行、管理和控制从主机操作系统和虚拟层到服务运营所在设施的物理安全性的组件。客户负责管理来宾操作系统（包括更新和安全补丁）、其他相关应用程序软件以及 Aws提供的安全组防火墙的配置。

客户应该仔细考虑自己选择的服务，因为他们的责任取决于所使用的服务，这些服务与其 IT 环境的集成以及适用的法律法规。

![1687930176_649bc5406fe993edb806e.png!small?1687930176123](https://image.3001.net/images/20230628/1687930176_649bc5406fe993edb806e.png!small?1687930176123)

## 二、云安全的特点

Aws核心服务包括Config 跟踪资源库和变更、CloudTrail 跟踪用户活动和 API 使用情况、以及IAM 安全地管理身份以及对 Aws 服务和资源的访问、CloudFormation 为您的所有云基础设施资源建模并对其进行预置。

![1687930662_649bc726ac67cf794aee9.png!small?1687930662246](https://image.3001.net/images/20230628/1687930662_649bc726ac67cf794aee9.png!small?1687930662246)

Config可以跟进云上资源变更，可以定期检查包括我现在有多少台服务器、有多少的对象存储、网络状况如何等等这些资源的情况，并且对它的一些配置做一些审计，为安全审计带来一定的便利。

CloudTrail是一项云审计功能，但这个审计主要针对操作而不是资源。比如我跟踪一些用户的活动、或者一些API使用，可能由机器发起、也可能由人发起。这就是我们传统意义上所指的那种操作的一种审计服务。

IAM是一项身份认证、身份管理服务，几乎所有云都有。该服务主要是针对管理能力，能够有效地去管理用户并提供临时的授权。

CloudFormation是偏向于资源编排的一项服务，你可以通过一些代码来把资源创建出来。不过这个在国内的应用场景不是特别多。只要拥有这项服务就可以通过代码把资源给编码出来。它们基于一些代码或者配置文件就把资源创建出来。好处在于如果你在做一些测试或者开发环境的时候想临时起一套环境或者有某个临时的服务，可以先在此做测试、压测，扫描，这项编排服务可以帮你把所有对应的资源都创建出来以提高效率。

## 三、云上的特色服务

云上特色服务最重要的是对象存储，几乎所有的公有云和私有云都有对象存储的服务。对象存储是一种以非结构化格式（称为对象）存储和管理数据的技术。现代组织需要创建和分析大量非结构化数据，例如照片、视频、电子邮件、网页、传感器数据和音频文件。

云对象存储系统将这些数据分布在多个物理设备上，但允许用户从单个虚拟存储库有效地访问内容。对象存储解决方案非常适合用于构建需要扩展和灵活性的云原生应用程序；您还可以使用这些解决方案导入现有数据存储以进行分析、备份或存档。

![1687931723_649bcb4b0918dfdd8dd62.png!small?1687931722616](https://image.3001.net/images/20230628/1687931723_649bcb4b0918dfdd8dd62.png!small?1687931722616)

## 四、不同分类的云服务安全

要想实现云迁移，要分多个层次。首先第一层次是直接迁移，大多数使用的都是这个模式。相当于将云直接当成IDC去使用，直接将代码迁移当虚机，基本上修改一下配置即可成功实现迁移。

另外一个模式是直接使用SaaS，比如将数据库换成RDS，把存储换成对象存储，这就是一个更换的过程。

云安全在不同分类下有一些注意点，就是IaaS层次和SaaS层次。

IaaS层次跟IDC 比较相似，它有VPC的概念，等于所有的资源都是在一个虚拟的私有网络里边。作为甲方有足够的网络权限的话，那么防护重点是网络安全。

![1687932542_649bce7ee07ea666c60fe.png!small?1687932542470](https://image.3001.net/images/20230628/1687932542_649bce7ee07ea666c60fe.png!small?1687932542470)

SaaS没有租户VPC的概念，可能有（区域Region）的概念，主要靠认证来保证安全，防护的重点是鉴权部分。

![1687932816_649bcf9014a4aeff05cf7.png!small?1687932815621](https://image.3001.net/images/20230628/1687932816_649bcf9014a4aeff05cf7.png!small?1687932815621)

## 五、问答环节

在问答环节，有观众提到，如何做云安全产品的选型？对此，王明松表示理论上AWS所有的原生云安全产品应该都有功能更好的第三方替代，所以是选原厂还是选第三方取决于你的需求和预算。一般 Aws 自带的契合度好，但是功能略微简单一些，比较适合要求不高的团队简单使用。

还有用户提出，什么样的云是安全的？云的安全如何做评估？

王明松认为首先可以简单的看一下云服务和的相关认证，做一下简单对比，认证是一个比较好的评估手段。其次，尽量不要选择太小的服务商，也不要选择跟你有利益冲突的服务商。如果说的是自己的云服务，我觉得权限设计得当，不断更新维护的云服务才是安全的。

![1687933398_649bd1d69abd2d1f56729.jpg!small?1687933398269](https://image.3001.net/images/20230628/1687933398_649bd1d69abd2d1f56729.jpg!small?1687933398269)

最后，主持人和演讲嘉宾们一起抽取了幸运互动观众，送出精美礼品。

## ****六、********加入FreeBuf甲方社群****

本期直播精彩回顾到此结束啦~此外，FreeBuf会定期开展不同的甲方社群直播，想了解更多话题和观点，快来扫码免费申请加入FreeBuf甲方群吧！

更多精彩内容尽在FreeBuf甲方会员专属社群，小助手周周送福利，社群周周有惊喜，还不赶快行动？![](https://image.3001.net/images/20230404/1680603146_642bf80ad434fe7b7149b.png!small)

【申请流程：扫码申请-后台审核（2-5个工作日）-邮件通知-加入会员俱乐部】

![](https://image.3001.net/images/20230404/1680603103_642bf7dfc5073e1e05af4.png!small)

【如有疑问，也可扫描上方二维码添加小助手微信哦！】

# 云安全 # FreeBuf直播

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

一、云服务的责任共担模型

二、云安全的特点

三、云上的特色服务

四、不同分类的云服务安全

五、问答环节

六、加入FreeBuf甲方社群

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)