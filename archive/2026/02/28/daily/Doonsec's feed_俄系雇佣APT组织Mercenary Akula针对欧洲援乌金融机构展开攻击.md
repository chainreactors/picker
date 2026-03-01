---
title: 俄系雇佣APT组织Mercenary Akula针对欧洲援乌金融机构展开攻击
url: https://mp.weixin.qq.com/s/F6ylokgrxYl_Kxpbb2vRBw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:23:30.791714
---

# 俄系雇佣APT组织Mercenary Akula针对欧洲援乌金融机构展开攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMINeYG0xg4btBInpvgswiaLDvMezqC0jzMYgNaiagu4ktmbPMeMNPegmKe7JaecHMuibo8tvBd5w2ZUOw/0?wx_fmt=jpeg)

# 俄系雇佣APT组织Mercenary Akula针对欧洲援乌金融机构展开攻击

原创

BaizeSec
BaizeSec

白泽安全实验室

![]()

在小说阅读器中沉浸阅读

近日，一家深度参与区域发展与乌克兰重建项目的欧洲金融机构，成为了一场高度定向网络攻击的目标。网络安全公司BlueVoyant的安全运营中心识别并响应了此次攻击事件，并将其归因于一个与俄罗斯有关联的、名为“Mercenary Akula”的威胁组织（也称为DaVinci Group和Fire Cells Group）。该组织被乌克兰CERT追踪为UAC-0050，兼具经济驱动的雇佣兵性质，同时涉及网络间谍活动和心理信息战。此次攻击的特殊之处在于，其目标并非以往主要针对的乌克兰境内实体，而是一家支持乌克兰重建的西欧金融机构，这暗示着该组织的攻击范围可能正在向乌克兰的境外支持者扩展。被选定的目标是该机构一名高级法律与政策顾问，其工作涉及采购领域，能够接触到机构的内部运作和财务机制，这直接反映出攻击者获取情报或实施金融盗窃的意图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HBRznhxajkZmzVWvCGJClqXhdktT6qsGJEVgmAFYu9SxUzUAzp0TQhhZq1ExkC3dpnbBcuXm2sXLYlNpFJNRNQoXeME96EZTtaNLsYx8Mfs/640?wx_fmt=png&from=appmsg)

图 1 Mercenary Akula组织钓鱼邮件示例

研究人员通过详细的技术分析发现，攻击始于一次精心构造的鱼叉式网络钓鱼邮件。这封以“来自切尔尼戈夫行政法院关于案件81435126的请求”为主题的邮件，发件地址看似来自乌克兰官方域名，实则经过精心伪造。邮件诱导收件人从一个名为Pixeldrain的公共文件分享服务下载一个压缩包文件，这是Mercenary Akula组织惯用的伎俩，旨在利用公共存储服务绕过基于声誉的安全检测。该压缩包名为“电子法院请求 №837744-8-2026 від 09.02.2026 — 865.zip”，内部嵌套了多层混淆结构：首先是一个ZIP压缩包，解压后得到一个RAR格式文件，其中还包含一个受密码保护的7-Zip文件，而密码则放在一个名为“Код.txt”（即“代码.txt”）的文本文件中。这种多阶段解压流程是一种已知的规避技术，旨在挫败自动化安全扫描，并通过复杂的操作步骤让用户对可疑活动逐渐习以为常。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HBRznhxajkZAGXv02mqgjgkLqgJESicibpibHGr8HF2GAr9zlTNCqiagbA7fT1SkKCPKfjiaz5aRzswd9XQ4H6ZxVyMmsQ0IUCHbmreT80cJl6pg/640?wx_fmt=png&from=appmsg)

图 2 Код.txt文件里的密码提示

最终解压出的有效载荷是一个名为“Електронний судовий запит №837744-8-2026 від 09.02.2026.pdf.exe”的可执行文件，它利用双层扩展名技巧伪装成一个PDF文档。一旦用户执行此文件，它就会部署一个名为Remote Manipulator System (RMS)的MSI安装程序。RMS是由俄罗斯公司TektonIT开发的一款合法的远程管理工具。Mercenary Akula组织有长期滥用RMS、LiteManager等商业远程访问软件以及Remcos、QuasarRAT等远程访问木马的历史。这种“离地生存”的攻击手法使得攻击者能够获得持久且隐蔽的访问权限，同时常常能规避传统防病毒软件的检测。技术分析显示，该MSI安装程序中嵌入了预配置参数，例如指向RMS开发商域名的伪URL和一系列用于静默安装的指令，如安装路径、防火墙集成、自动启动等设置，以及用于远程连接的序列标识符。这表明攻击者意图以最少用户交互的方式，快速部署一个预先配置好的远程访问后门。

进一步的调研分析揭示，此次“法院请求”只是该组织一场持续多年、运用多种定制化社会工程学诱饵的广泛行动中的最新案例。同期，该攻击者还同时使用了冒充乌克兰司法机构以及“M.E.Doc”会计软件相关通知的诱饵。M.E.Doc是乌克兰广泛使用的会计软件，历史上曾被用作重大攻击的初始入口。以M.E.Doc为主题的诱饵表明，攻击者对目标机构使用的业务软件有具体了解，并试图直接瞄准财务和会计人员。这直接契合了Mercenary Akula以金融盗窃为首要目标的特点，正如CERT-UA此前警告的，通过此类诱饵入侵的会计人员，其系统可能在数小时内就会被用于发起欺诈性的银行转账。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HBRznhxajka79icrYQ48YzDib2icPz29hRV3XHGpuSCtO0jW8393DRnHH5sk4k1cUVG0Q78nQSrVDbYKsYGQ7vpuhVI0fSHIQP2NVewfpYVa8U/640?wx_fmt=png&from=appmsg)

图 3 DaVinci Group/Agency DaVinci组织标志

研究人员技术分析关键发现表明，此次攻击事件并非孤立案例，而是Mercenary Akula组织成熟、持久且高度适应性的运作模式的体现。结合历史信息来看，该组织以乌克兰为中心，专注于高价值财务和情报目标。乌克兰国家计算机应急响应小组（CERT-UA）的历史评估将该组织定性为与俄罗斯执法部门相关联的雇佣兵实体，其行动具备初始访问中间商般的速度与精准度。网络安全机构BushidoToken补充的开源情报分析进一步确认，该组织以“DaVinci Group/Agency DaVinci”为对外代号，同样指向其与俄罗斯执法部门的关联及初始访问中间商的角色定位。与此同时，CERT-UA将该攻击主体实施的心理战与信息作战行动归属于Fire Cells Group虚拟身份，该实体曾针对乌克兰驻外使馆及媒体机构发起炸弹威胁攻击活动，这一研判也得到Recorded Future相关报告的交叉印证。另外，此次针对欧洲金融机构的攻击，完全符合该组织反复出现的攻击特征：利用高度可信且本地化的诱饵，通过公共云服务分发多层混淆的恶意载荷，最终部署合法远程管理工具以实现双重目的——快速实施金融盗窃或进行长期网络间谍活动。这一事件不仅证实了Mercenary Akula组织是对在乌克兰运营的组织的持续威胁，更向所有支持乌克兰的境外机构发出了明确信号，即它们也可能成为该组织下一阶段扩张攻击的目标。

参考链接：

https://www.bluevoyant.com/blog/mercenary-akula-hits-financial-institution

往期推荐

[LockBit勒索组织发布声明并重建泄露网站——每周威胁情报动态第166期（2.23-2.29）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492114&idx=1&sn=8d7c5643b4d7b9e6ba5fdb73db25f5ac&chksm=e90dc838de7a412e358185c880ff13f5960c816f47faef975adecc92aa229dd947eaed7c1543&scene=21#wechat_redirect)

[GoldFactory组织开发针对iOS系统的GoldPickaxe木马病毒——每周威胁情报动态第165期（2.9-2.22）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492108&idx=1&sn=9a94a877d19aae993613beabfed515b9&chksm=e90dc826de7a4130e9c14fbecc4bb470c785600d65f4eca984822a3772b801007188d753444b&scene=21#wechat_redirect)

[新APT组织APT-LY-1009针对亚美尼亚政府投递VenomRAT——每周威胁情报动态第164期（02.02-02.07）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492097&idx=1&sn=53ec18ecbac467ab6dddeef971e8630f&chksm=e90dc82bde7a413df05e08bc4d6136b60d4a339310cdb66a046cc0645bb90e447b8564e16180&scene=21#wechat_redirect)

[APT28组织对全球多个组织发起NTLMv2哈希中继攻击——每周威胁情报动态第163期（01.26-02.01）](http://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492083&idx=1&sn=2c985de24dfa929181ba8e6ae63b02ab&chksm=e90dcbd9de7a42cf2f738cbe44a3859ab3f78636b84ef2b930dfc29ecbfc05542ae161ab4e16&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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