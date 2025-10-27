---
title: 文档加密系统的探索与落地｜大湾区金融安全专刊·安全村
url: https://mp.weixin.qq.com/s?__biz=MzkyODM5NzQwNQ==&mid=2247496073&idx=1&sn=0f711e0c2a2526d7edbcc57a96911467&chksm=c21bd0bbf56c59adca80c7a8b3280711bff0257ea2e5cdf417ecc4b78ad61c3b6e444bb0349b&scene=58&subscene=0#rd
source: 安全村SecUN
date: 2024-11-06
fetch_date: 2025-10-06T19:20:03.014421
---

# 文档加密系统的探索与落地｜大湾区金融安全专刊·安全村

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kvCk9Nm6FzS5llJCXqvzCic5m0Bmb0fXKbJqv8KNkqOlu9ka3KOz4HGJE9A5t9APJlsI4kRAn3icxiaiaeGSaMuGhw/0?wx_fmt=jpeg)

# 文档加密系统的探索与落地｜大湾区金融安全专刊·安全村

薛峰&刘欢

安全村SecUN

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzTQIVRupkBz6icX1VsHSXEobYH9Jm89tib2uBaToVnKGUAflWqfuZHuX0AbVic4bUMfM2oicy34D2Ibhw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzS5llJCXqvzCic5m0Bmb0fXK2Gtiauicu96yzkTCkIcpZbsCG8OSiaaumjpWOPqqFahiaibwPr40ch4csAw/640?wx_fmt=png&from=appmsg)

**1.金融企业数据安全风险分析**

随着金融机构数字化转型的不断深入，业务部门对于数据的使用频度越发明显，业务数据、经营数据在终端上处理、流转、保存的需求日益旺盛。从源头来看，金融企业办公终端的数据来源主要包括本地自生成、内网应用（OA、邮箱、财务系统、人力资源系统、业务系统）、生产数据提取等途径，由于办公终端内部存储的电子文档极易复制，容易通过邮件、光盘、U盘、网络存贮等各种途径传播，数据安全保护面临严峻挑战。

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJ4vhq6wC3dMD4vkRDatAPxHP69ddjGLYoIU70FyupBE5taVZSnFQkaA/640?wx_fmt=png&from=appmsg)

现有的终端数据安全管控手段往往聚焦于桌面安全管理，面临以下安全隐患：

* 缺乏强制性保护措施

终端的外发途径管控不严或者不全面（如未禁用蓝牙、设备间文件共享、AirDrop、云文档等），导致内部员工可随意把企业内部文件甚至涉及公司机密的文件携带出去，无形中给企业造成巨大损失。

* 缺乏基于角色的用户权限管理措施

企业内部因部门不同、员工级别不同，针对文件使用范围也不同。然而企业内部管理人员无法根据实际需求设置不同权限部门、员工使用不同的文件。

* 缺乏对文件的使用权限控制措施

企业内部文件甚至核心机密文件不能合理地设置不同使用权限，造成文件在企业内部的滥用，从而给企业核心机密外泄带来了隐患。

* 缺乏终端数据销毁技术手段

员工电脑中保存大量数据，很多数据其实不需要长期保存，但员工很难做到数据用完即删，因此需要强制技术手段对超过使用期限、使用需求的数据进行删除或者取消用户访问权限。

* 缺乏对文件有效的离线控制

企业内部常常面临信息外携使用、交互使用的需求，然而却缺乏对文件有效的离线控制，文件一旦外携出去将处于不可控状态，离线文件可以被随意编辑、复制、刻录、打印。

**2.解决思路**

解决终端数据安全的风险，重点在解决终端文档全生命周期的安全管控，对此，需要一套对终端文件在生成、传输、共享、使用、销毁等各阶段的文档安全控制系统。系统应从数据生命周期的角度，从文档创建开始，对文档进行管控，对不同类型文档根据数据安全等级施行分级安全保护，融入强访问控制模型（MAC）、数据所有者、数据控制者、隐私保护等理念，实现终端文件级安全控制、明确数据主体和所有权、终端数据流动过程中的“谁使用、谁保护。

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJ9ib9SPm26DSKBOL3P1QTbT6Odw09NF54bzeic3ek16iacbLra4kZkmic8A/640?wx_fmt=png&from=appmsg)

系统应至少能实现如下场景的安全防护：

* 终端文档防护

各种有意或无意的泄密往往发生在用户的终端，所以在终端对重要文档进行加密防护更显得尤为重要。通过透明加解密明文文档被加密成密文，密文只有在安装了文档安全控制系统客户端、正常登录的情况下才能使用。文档被私自带离、发送出单位后无法打开。杜绝重要文档主动、被动泄密隐患。

* 业务系统文档下载防护

文档安全控制系统为OA、ERP、档案、PDM等业务系统提供防护，保证系统中文档的安全。通过文档安全控制系统与业务系统的整合，对业务系统中的重要文档进行加密防护与授权，将业务系统中文档的安全区域扩展到用户桌面。

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJsHSPbxrKfCmY0YhohiaoWpU5Q5hnEwwG4BiaWicmhwKO1vmbXgjxvGObw/640?wx_fmt=png&from=appmsg)

* 文档分级管理

根据文档的重要程度建立文档的安全防护体系。按照文档的密级对不同用户、用户组授权，灵活控制不同用户对文档的阅读、编辑、复制、打印、截屏等权限。结合用户的文档使用管理制度，实现文档的分级防护。

* 文档安全传输

文档在传递途中容易因为传输遭到拦截、侦听，装有文档的载体丢失、被窃造成泄密。在重要文档进行传送时在发送端进行加密与授权，再通过载体或者网络进行传送，只有被授权的接收者才能在使用密文。保证了用户各个机构间数据传递与交互的安全。

* 文档外发防护

通过离线模式保证敏感文档在单位外使用的安全性，在经过审批后敏感文档可以带离或外发出单位使用，使用时间、使用权限都会受到严格的限制。保证敏感文档外发给客户、第三方合作机构后的安全。

**3.落地场景探索与效果**

* 自主用数平台报表加密导出

随着数字化转型的不断深入，部分银行单位已经建立了自主用数平台，平台面向业务部门提供BI报表展现与下载、向数据分析人员提供数据分析与建模的平台。自主用书平台用户对报表数据导出有强需求，传统的应用系统字段脱敏导出、线下流程审核和权限控制等方式能够一定程度上控制数据安全风险，但在溯源追踪、安全监控以及导出文件权限控制上仍有优化提升空间。

该场景下，通过自主用数平台文件导出接口与文档安全控制系统后台对接，当发生下载请求时自动触发文档安全控制系统对下载文档进行加密并配置相应不同的文件权限，即满足用户在本地加密客户端使用数据文件的需求，同时实现对导出、使用数据的行为提供全面的监测与事后审计，保障交付数据的安全。

**实现效果：**自主用数平台报表导出实现下载即加密、文件级权限控制。

对导出文件的权限控制颗粒度主要包括如下：

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzS5llJCXqvzCic5m0Bmb0fXKuwIha64FuYcPEr1odljvHFLWM4icH14G0dIoEyUOn4YS1G8We2BrZAw/640?wx_fmt=png&from=appmsg)

* 生产数据提取与外发

业务部门因业务开展、经营管理、统计分析、监管报送等需要日常会申请提取生产数据，对生产数据的提取与共享是生产数据跨域流动的主要场景之一，也是终端使用生产数据的重要渠道之一，业务部门在获取生产数据后，仍面临明文存储、随意转发、无限期使用、数据未按时销毁等风险，对此，通过文档加密系统实现对生产数据源的加密与权限控制，实现生产数据的文件级、用户级控制，并实现数据到期销毁。

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJ6HiagpiaOkGHmOgAQU4YbVSpRNyvesMUo1AqoBTjm2icibRGsVWIQ35MPQ/640?wx_fmt=png&from=appmsg)

文件加密支持所有Microsoft Office系列、WPS、记事本、写字板、Adobe Arcobat、Auto CAD、3D MAX、JPEG(JPG)、BMP、TIFF（TIF）、Catia、Solidworks、PDMS、GIF等以及源代码编译平台所产生的文件格式Java、VC、VB等。

* 终端敏感文件扫描加密

针对用户终端上的存量文档，有些可能是涉及到敏感级及以上的数据，对于这类文档，可通过文档安全控制系统，定期对终端磁盘内所有文档进行扫描，文档内容符合后台预设的密级规则时，则进行自动加密授权，并实现文档确权、权限控制。

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJCdJK1x5mAficOcqeKfIoVstqSw11VraVuXLDNoEwYaibpDRathbuMKlw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJwb7ficgvicFd4OaUzFJiat6gBJRYo9PFQ9T6jnO65jJNvH0IDQ7VNFNhQ/640?wx_fmt=png&from=appmsg)

* 敏感文档泄露溯源

内部敏感文档可能外泄到互联网上或者暗网，难点是如何分析泄露文档的泄露路径、还原泄露过程。对此，需要通过明水印、隐水印来追溯其来源，水印信息包括计算机名、用户名、ip、mac地址、日期等属性，当出现数据泄露情况，可追溯其来源，后台支持对水印信息、透明度、颜色等信息进行配置。

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJGm74kCjhJFbk4jQneFMODVzKe6ZPkGVYib3rt03p7osxeicsRNGAfV1w/640?wx_fmt=png&from=appmsg)

* 文档外发管控

主要实现针对于第三方用户（业主或合作伙伴等），限制第三方用户使用文档，并保证文档不会被第三方进行二次传播，泄密。

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQjr98wE32srHV7ZTMiaEJbJeQsEIj8BsoH3Pnudup6M14JRG8OibetxEC2A2yHNJh29XW5AZVEYIng/640?wx_fmt=png&from=appmsg)

文件外发功能可以直接将加密后的文档外发给合作伙伴或客户进行使用。对方无需安装任何客户端软件。该工具可为合作伙伴设置阅览文件的权限和时间。通过外发用户管理功能，可对加密后的文档做时间延长或者权限变更，无需重复的传递原始加密后的文档。

**实现效果：**

+ 对发布到外部机构的加密文档进行“时间控制”
+ 外发后的文件仅在规定的有效期内可以使用，到时间文件自动销毁。
+ 对发布到外部机构的加密文档进行“权限控制”
+ 外发后文件只能按规定权限使用。权限分为（阅读、编辑、打印、复制）
+ 对发布到外部机构的涉密文件进行“打开次数限制”
+ 外发后的文件打开次数限制。当涉密文件到达文件的有效打开次数，文件自动失效。
+ 对发布到外部机构的涉密文件实现“防止二次传播功能”
+ 外发文件可与光盘、U盘等载体相绑定后发布给外部机构人员。从而实现文件无法脱离载体的使用模式。有效防止涉密文件被二次传播。

**4.展望与总结**

对于终端数据安全使用文档安全控制系统，难点在于应用推广，一是站在用户的角度，用户已长期习惯安全跟业务无关、跟自己无关，安全是科技部门、安全部门的事情，而文档安全控制系统的设计理念是“数据谁使用、谁负责”，将安全的职责分散到数据使用人、资产所有者，所以文档安全控制系统的推广使用过程会比较困难，需要试点、宣贯、培训等方式让用户接受和习惯，也需要“自上而下、部门协同”的方式自顶向下推动；二是安全的策略落地会改变业务习惯，因此在文档安全控制系统的用户友好度方面需要进一步打磨，让用户用起来简单、方便，尽量优化用户体验，平衡好业务和安全；三是在维护方面，考虑到终端的文档使用，需要7\*24的运维机制，当用户在使用文档安全控制系统的过程中，如果遇到问题可以快速解决。四是需要考虑业务扩展、用户量增加的弹性扩容，终端的用户量的增加会带来对文档加解密处理性能、存储空间的指数级增加，因此需要提前预判分析用户数与文档安全控制系统扩容需求的关系。

***作者介绍***

**恒丰银行安全管理团队**

**关于 大湾区金融安全专刊**

大湾区专刊现已发布第1辑和第2辑，集合了全国数十家金融和科技机构的网络安全工作经验总结，更邀请了大湾区港澳金融机构的安全专家分享独到见解。文章内容涉及防御体系、安全运营、数据安全、研发安全、业务安全、资产管理、攻防演练、前沿分析等主题方向，希望能为从业者提供网络安全防护方面的整体思路，向行业传播可持续金融创新和实践经验，为推动可持续金融生态发展汇聚智慧与力量。

**关于 安全村**

安全村始终致力于为安全人服务，通过博客、文集、专刊、沙龙等形态，交流最新的技术和资讯，增强互动与合作，与行业人员共同建设协同生态。

![](https://mmbiz.qpic.cn/mmbiz_png/tds1LtegHbDicAIYWzMZKgkzUsBOeQpI7Y4UQqicF1NbPndQX0hicx3y4rdn6qePPRE8BSVSot4Wd7y5ciaYvfiaJwQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**专刊获取方式**

本次专刊的合作机构如下

赶紧关注他们

联系获取纸质版专刊吧！

![](https://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzQDBOclm0wibnwxZFl5f1ibRZ3VFKnSKyYHmtGNDA20PePia3Fq9v6cwEmB9SIQO5PzSiaiaZ1gdrRvbqg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzRGMuTrYpXpG6QcU1hu3hPRZuNFOWGNGYBFFTtxeiaiar1T5oJTB5Qo0TTVuCibFZtulDDvHFklutuBQ/0?wx_fmt=png)

安全村SecUN

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzRGMuTrYpXpG6QcU1hu3hPRZuNFOWGNGYBFFTtxeiaiar1T5oJTB5Qo0TTVuCibFZtulDDvHFklutuBQ/0?wx_fmt=png)

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