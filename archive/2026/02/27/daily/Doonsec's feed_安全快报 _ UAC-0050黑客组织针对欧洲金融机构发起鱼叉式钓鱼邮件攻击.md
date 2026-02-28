---
title: 安全快报 | UAC-0050黑客组织针对欧洲金融机构发起鱼叉式钓鱼邮件攻击
url: https://mp.weixin.qq.com/s/slfnC8P7BZZiFx1xvsMZ7A
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:58:14.578029
---

# 安全快报 | UAC-0050黑客组织针对欧洲金融机构发起鱼叉式钓鱼邮件攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibQUicZffPZ8wG9TBgVYQyC0E5IRaolsibBSlf2HGXQwJhjrYBKZEzdTh7jzHqibZ3CzCGQwsDsI9LvUbj0jUJv9cyDZ1Lic3Wf9RO8/0?wx_fmt=jpeg)

# 安全快报 | UAC-0050黑客组织针对欧洲金融机构发起鱼叉式钓鱼邮件攻击

天懋信息

![]()

在小说阅读器中沉浸阅读

**本周安全事件速览**

**02月20日-02月27日**

**01**

**UAC-0050黑客组织针对欧洲金融机构发起鱼叉式钓鱼邮件攻击**

![图片1.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibQr3zOjVdfKWfz207IR44k6J79KBZ22iav5rNT1zhv25pISHb9jxQTibOkyj5GVULovuoPVguia1dPjFY5CjNRsia5Qkwh5HCTVD50/640?from=appmsg "undefined")

**简要介绍**

与俄罗斯结盟的黑客被观察到针对一家欧洲金融机构发起鱼叉式钓鱼邮件攻击，作为社交工程攻击的一部分，目的可能是为了情报收集或金融盗窃。该活动被归因于一个名为UAC-0050（又名达芬奇集团）的网络犯罪组织，其入侵对象为一个未具名的参与区域发展和重建项目的实体。BlueVoyant已将该威胁集群命名为“雇佣兵阿库拉”。据悉，攻击过程中伪造了一个乌克兰司法域名，发送了一封包含远程访问载荷链接的电子邮件。攻击起点是一封鱼叉式钓鱼邮件，利用法律主题引导收件人下载托管在PixelDrain上的归档文件，PixelDrain是黑客用来绕过基于声誉的安全控制的工具。乌克兰计算机应急响应小组（CERT-UA）将UAC-0050描述为与俄罗斯执法机构相关的雇佣兵团体，以“Fire Cells”品牌进行数据收集、金融盗窃以及信息和心理战。

**文章来源：The Hacker News**

**02**

**吉尔吉斯斯坦和塔吉克斯坦电信公司遭UnscicitedBooker威胁组织钓鱼邮件攻击**

![图片2.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibTv3H6daic1aM1QCMq6rlQYzOibTjtbGRpPxyeCPRuyHhROVd7wlUJDUA4wR2lnxcVm2WzJxDcShBMrRJ5bYqUibcIVSehCQVXMFo/640?from=appmsg)

**简要介绍**

UnsolicitedBooker威胁组织已被观察到针对吉尔吉斯斯坦和塔吉克斯坦的电信公司发起系列钓鱼邮件攻击。根据Positive Technologies发布的一份报告，这些攻击涉及两个代号为LuciDoor和MarsSnake的不同后门。UnscicitedBooker最早于2025年5月被记录，该组织被评估自2023年3月起活跃，并有针对亚洲、非洲和中东组织的历史。对该黑客组织的进一步分析发现，该群集与另外两个集群存在战术重叠，包括Space Pirates以及一个尚未归因的针对沙特阿拉伯的活动，该活动还设有名为Zardoor的后门。据悉，最新一组攻击于2025年9月底被发现针对吉尔吉斯斯坦的政府组织，邮件中包含一份Microsoft Office文档，打开后会指示收件人“启用内容”以运行恶意宏。UnsolicitedBooker据称还利用钓鱼邮件针对塔吉克斯坦政府实体目标。虽然整体攻击链保持不变，但这些消息是嵌入了与诱饵文件的链接，而非直接附加。

**文章来****源****：The Hacker News**

**03**

**欧洲多国政府实体遭APT28俄罗斯黑客组织基于Webhook的宏恶意软件入侵**

![图片3.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibRPOeDFsbicXb9xChSKpXy7qjftbUXhfwx5YCxvX3pK58W48s4m8Qye4toQvCNjWpKD9PFgY3miaiaO7rU7ibjOpWCCwEN7UyEeRHE/640?from=appmsg)

**简要介绍**

与俄罗斯有关的国家支持黑客组织被追踪为APT28，已被归因于针对西欧和中欧多国政府实体的新型网络入侵活动。据统计，该活动活跃于2025年9月至2026年1月期间，行动代号为“宏观迷宫行动”。据悉，该活动依赖于基础工具和利用合法服务进行基础设施和数据窃取，这些攻击链以鱼叉式钓鱼邮件为起点，分发包含其XML中共同结构元素的诱饵文档，该字段名为“INCLUDEPICTURE”，指向一个webhook[.]，该网站的URL托管JPG图像。这会导致在打开文档时从远程服务器获取图像文件。该机制类似于追踪像素的信标机制，触发向webhook[.]的外部HTTP请求，打开文档时查看网站网址，服务器可以记录与请求相关的元数据，确认文档确实被接收方打开。2025年9月至2026年1月间出现的变种使用修改后的宏投放恶意软件并在受攻破系统上部署额外负载。

**文章来****源：****The Hacker News**

**04**

**伊朗黑客组织MuddyWater针对中东和北非多个政府组织发起恶意钓鱼邮件攻击**

![图片4.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibQk8187EQAeknBDx86LyfvIficLwTPqdG51XJsiapj1hL6PBBLh1Xn3mYZgIYfB22pWm2Fibibc1fxKDa2A2vok760ic0YuZlR432gk/640?from=appmsg)

**简要介绍**

名为MuddyWater的伊朗黑客组织针对主要分布在中东和北非（MENA）地区的多个政府组织和个人，发起代号“奥拉兰波行动”的新型网络攻击活动。根据Group-IB发布的一份报告，该活动首次于2026年1月26日被观察到，发起了新的恶意软件家族的部署，这些恶意软件家族共享了先前被识别为黑客使用的重叠样本。这些包括GhostFetch和HTTP\_VIP等下载器，以及一个名为CHAR的Rust后门和代号GhostBackDoor的高级植入体，由GhostFetch投放。这些攻击遵循类似模式，首先是一封带有Microsoft Office文档的钓鱼邮件，其中包含恶意宏代码，解码嵌入的有效载荷并将其投放到系统上并执行，从而让对方远程控制系统。Group-IB总结称此次行动主要针对中东北非地区的组织，黑客组织持续采用人工智能技术，结合定制恶意软件和工具的持续开发以及多样化的指挥控制（C2）基础设施。

**文章来****源：****The Hacker News**

**05**

**美国和欧洲物流公司遭受黑客组织利用钓鱼即服务工具（PhaaS）发起的持续数月钓鱼攻击**

![图片5.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibRSfOHxXL0HSfgPIibKXnqpd477aibia6axR8n69upqSFlQRKFYRpveLZ1pRjiaCoOOS2EDMQZ5l3Ukb3iaibhVxBUicIoXEAFA3fARoo/640?from=appmsg)

**简要介绍**

据悉，相关调查人员已识别、揭露并破坏了一场持续数月的有组织犯罪行动，该组织销售一种钓鱼即服务工具（PhaaS），目标是西方热门物流平台的用户。钓鱼即服务平台订阅者通过外部支付处理商支付加密货币。该钓鱼平台与52个不同的钓鱼域名的部署有关，该组织利用这些域名针对5.7万名电子邮件地址持有者窃取凭证，同时还尝试了35起电子资金来源（EFS）支票欺诈事件。该组织至少花了五个月时间系统性地针对美国和欧洲的货运和物流公司，窃取了主要物流平台用户的1600多个独立登录凭证。该PhaaS平台配备了专门的钓鱼基础设施，日常被货运经纪人、卡车公司和供应链运营商使用，装载板、车队管理门户、燃油卡系统和货运交换站等都是其目标之一。

**文章来****源：****Bank Info Security**

**06**

# **美国医疗器械制造商UFP科技公司向美国证券交易委员会报告其公司相关数据被盗或遭销毁**

#

#

#

#

![图片6.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibS7zO4qYANbXGHHVEPeNDBeyyepvSzpe4dWHqlxoSqmQib7JJhrEOibRIIaa2cy17raAicmlLtU73ia1K4ibWCVfADBQDYbliaEdSvyM/640?from=appmsg)

**简要介绍**

总部位于美国马萨诸塞州的一次性医疗器械及其他医疗用品制造商UFP科技公司已通知美国证券交易委员会，2月14日在其IT系统中发现了一起涉及部分公司数据被盗或销毁的网络事件。该公司表示，已立即采取措施控制和修复事件，包括隔离受影响的系统。UFP告诉SEC，导致此次事件的黑客已被从公司IT系统中剔除，UFP访问受影响信息的能力已在所有实质性方面恢复。尽管如此，上报文件称部分UFP或公司相关数据似乎被盗或销毁。UFP表示，此次事件影响了客户配送的计费和标签制作等IT系统。UFP仍在调查受影响系统和文件中所包含的任何敏感或个人信息的程度。迄今为止，该事件尚未对UFP的财务体系、运营或财务状况产生实质性影响。

**文章来****源：****Bank Info Security**

**07**

**美国密西西比大学医学中心遭勒索软件攻击导致三十多家诊所关闭业务系统**

#

#

#

#

![图片7.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibTAiaRAnicxM2X1RbR4PwXRy2zTr8U6Ug0r0qMOTg3R0oAp8sIf5BAibR3cpQUcXBF9OZtjsW1qqwmzlOrYZcXfmPRiayCQ3jtJic1s/640?from=appmsg)

**简要介绍**

美国密西西比大学医学中心UMMC在全州的三十多家医疗诊所被关闭，择期性手术也被取消，因为密西西比州唯一的学术健康科学中心遭到勒索软件攻击。UMMC表示，2月19日的攻击影响了其Epic电子健康记录和电话系统，医疗中心选择关闭所有其他系统，包括电子邮件进行测试以确保其安全。该医疗中心位于密西西比州杰克逊的主院区包括四家医院，大学医院、密西西比儿童医院、怀泽妇女与婴儿医院以及康纳利重症监护医院。自2月19日起，UMMC的诊所一直关闭，其位于杰克逊、格林纳达、麦迪逊县和霍尔姆斯县的所有医院和急诊科现已开放，但这些设施仍依赖人工病历记录及相关流程。在2月19日的新闻发布会上，UMMC领导人透露他们与勒索软件攻击者保持联系，但未透露讨论细节。

**文章来****源：****Bank Info Security**

**08**

**Everest勒索软件组织袭击美国医疗诊断公司Vikor Scientific的供应商导致其14万患者数据被盗**

#

#

#

#

![图片8.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibQIZKx7O1PYjo4223K29dzWscuIzgGiaJq9SzfNHqE0OT1lwEjhib3Qg06Zplnh79t0dql1M2CibFriawz7nyCrcic26baBAtqr1zVE/640?from=appmsg)

**简要介绍**

Everest勒索软件组织声称对Vikor Scientific发动了网络攻击。据美国卫生与公共服务部（HHS）报道，这家医疗诊断公司近14万人的数据遭到泄露。该事件源于对其第三方收入周期管理服务提供商Catalyst RCM的攻击。2025年11月13日左右，Catalyst在其安全文件系统中检测到可疑活动，公司对事件展开调查发现授权登录被滥用访问服务器，并在未经许可的情况下复制数据。随后，Everest勒索软件集团将Vikor Scientific及其关联实验室KorPath和Korgene加入其Tor数据泄露网站。该组织声称“公司内部文件包含各种个人文件、电子病历、患者的私人信息、账单信息等”被盗。由于Catalyst RCM很可能未支付赎金，网络犯罪团伙发布了涉嫌被盗的数据，包括Vikor Scientific的文件。Everest声称盗窃了包含25,303个PDF文件的Vikor Scientific数据库和包含1,344个PDF文件的Korgene数据库。

**文章来****源：****Security Affairs**

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCWnp4MYTluo2ib4Pibo5QAoxm2iaJME3yPXPLr1QYibicibCZibDib4185YxjKdxtvrcRspzxXj8BqZlnUhibA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCXHBrgOytxrXj5Isuu7Wa0bM6XhWyfjejlJia5dbBFcSpxZGvYibRndWGfODicNTYEpBFkXzuvp547cw/640?wx_fmt=gif)

往期回顾：

[![图片1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/76BUAjRsqibS5bicMmUbAr68Fib2BcspK8GR0fUHXA6nTmazG5QekyibwfHU2CMdibR7jlKvdN6C1Mpf2WiaGebq3nThmHM7wJzdribECetd447s3s/640?from=appmsg "undefined")](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247493539&idx=1&sn=2e71c6ec573bf2ab9e79371738d934d9&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/mmbiz_png/76BUAjRsqibQpSdiaycicP20JHaoUiaVhtqR1NN9HClYdpUIxtxhGicibicoD9ubxWdHwXVuLaYl9ibun6mQRiaiaO8vOavvCwicT33mguhxJ9JdCl3YfU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247493532&idx=1&sn=0910702b006b5903be914cb16dd1b831&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RdDBE4xfCCWxG4sOdBlYYMiavXjD9Mejibc1pluORms2tmtNrSEgTlrWVzT5pFjaE7kMVondCXfpqLEVfB3SLTMA/0?wx_fmt=png)

天懋信息

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RdDBE4xfCCWxG4sOdBlYYMiavXjD9Mejibc1pluORms2tmtNrSEgTlrWVzT5pFjaE7kMVondCXfpqLEVfB3SLTMA/0?wx_fmt=png)

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