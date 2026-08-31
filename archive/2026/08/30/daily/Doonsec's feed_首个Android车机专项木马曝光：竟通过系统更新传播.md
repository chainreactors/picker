---
title: 首个Android车机专项木马曝光：竟通过系统更新传播
url: https://mp.weixin.qq.com/s/oAfFPdRbL2JaDXwJP4eZeQ
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:51:19.281133
---

# 首个Android车机专项木马曝光：竟通过系统更新传播

# 首个Android车机专项木马曝光：竟通过系统更新传播

看雪学苑
看雪学苑

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88UvWNnwZluy752zz9IhvMmYPImEQoaWfhwgkx5Ltic3p1IIDOPCJ8Ol6CVl9Hf1PbD7thW779wLTvKeHF6aeBypiaBJEiatQBVkmA/640?wx_fmt=gif&from=appmsg)

近日，卡巴斯基（Kaspersky）安全团队披露了**全球首例专门针对Android车机（Head Unit）设计完整攻击链的恶意软件事件。**与以往诱导用户下载钓鱼App不同，此次攻击者盯上了车机内置的**合法软件更新通道，**将恶意程序直接推送到中控大屏，使其沦为广告欺诈与代理僵尸网络的节点。

![](https://mmbiz.qpic.cn/mmbiz_png/esHL7Vicu7E8L95iamicnib9UblSdRxUx7rejwIKF5w1GplPYGP3OQKggmCiaUxibwiaR2bqZibdgvPXYM0tYU4LSaXdquqL6FibGzUL5ma4wQ3vnCE0/640?from=appmsg)

奇袭“信任链”：合法更新组件沦为投毒入口

![](https://mmbiz.qpic.cn/mmbiz_png/GibojqibaGeT03xrtfzVBo0Zc8nxgL5XG1LHqJicfyx53naftPicHhUokIWJfE6Z4ZM0sibOicCgoeXejGuEG8iaFhNDYyT089hSaRLNZcRCBUDA0g/640?from=appmsg)

此次攻击的突破口并非第三方破解，而是车机中一个名为 TWCore 的正规系统应用。该应用本用于收集数据及执行固件更新，依赖MQTT消息代理接收指令。

攻击者通过操控托管于 cardoor[.]cn 的MQTT服务，下发包含恶意APK下载地址的消息。关键在于，TWCore具备 installNotExists 功能——即使设备未曾预装该应用，也可强制安装。这一原本便于OTA升级的“后门”，被恶意利用，导致名为 JarService 的恶意Dropper（投放器）被静默下载至车机，全程用户无感知。

![](https://mmbiz.qpic.cn/mmbiz_png/esHL7Vicu7E8L95iamicnib9UblSdRxUx7rejwIKF5w1GplPYGP3OQKggmCiaUxibwiaR2bqZibdgvPXYM0tYU4LSaXdquqL6FibGzUL5ma4wQ3vnCE0/640?from=appmsg)

三段式隐匿链条：层层剥离，直抵核心

![](https://mmbiz.qpic.cn/mmbiz_png/GibojqibaGeT03xrtfzVBo0Zc8nxgL5XG1LHqJicfyx53naftPicHhUokIWJfE6Z4ZM0sibOicCgoeXejGuEG8iaFhNDYyT089hSaRLNZcRCBUDA0g/640?from=appmsg)

该恶意软件采用了复杂的“三段式”加载机制，以规避安全检测：

1. Stage 1（投放器 JarService）：无任何UI界面，安装后不显示图标。其内部存放了多块经XOR简单加密的数据，启动后解密并反序列化，用于加载下一阶段的核心入口。

2. Stage 2（加载器 Loader）：该组件利用Java反射机制动态执行代码，并向C2服务器发起POST请求，上报设备userId、包名、渠道号等信息。服务器随即返回包含第三阶段payload下载链接的JSON数据。

3. Stage 3（核心载荷 Clicker）：最终阶段的恶意程序会伪装成常规应用在后台运行。它默认每隔90分钟向C2服务器（如 `/cpc/api/task` 路径）发送心跳包，上报设备型号、分辨率、Wi-Fi名称及MAC地址，并接收云端指令。

![](https://mmbiz.qpic.cn/mmbiz_png/esHL7Vicu7E8L95iamicnib9UblSdRxUx7rejwIKF5w1GplPYGP3OQKggmCiaUxibwiaR2bqZibdgvPXYM0tYU4LSaXdquqL6FibGzUL5ma4wQ3vnCE0/640?from=appmsg)

从导航屏到“肉鸡”：反向代理与广告欺诈

![](https://mmbiz.qpic.cn/mmbiz_png/GibojqibaGeT03xrtfzVBo0Zc8nxgL5XG1LHqJicfyx53naftPicHhUokIWJfE6Z4ZM0sibOicCgoeXejGuEG8iaFhNDYyT089hSaRLNZcRCBUDA0g/640?from=appmsg)

经安全人员分析，攻击者的核心目标是变现。该木马支持多达9种远程指令，包括执行HTTP请求、WebView注入JS脚本、更新配置等。

研究记录显示，攻击者主要执行了两个操作：

1. 加载“zhima”模块：这是一个反向代理（Reverse-Proxy）模块，感染后，车机的网络连接被劫持，成为黑客代理池中的一个节点，用于隐匿恶意流量。

2. 执行广告欺诈：指令控制车机在后台偷偷访问特定网页或模拟点击，骗取广告商的流量分成。

![](https://mmbiz.qpic.cn/mmbiz_png/esHL7Vicu7E8L95iamicnib9UblSdRxUx7rejwIKF5w1GplPYGP3OQKggmCiaUxibwiaR2bqZibdgvPXYM0tYU4LSaXdquqL6FibGzUL5ma4wQ3vnCE0/640?from=appmsg)

幕后黑手：指向MoYu Group与BADBOX渊源

![](https://mmbiz.qpic.cn/mmbiz_png/GibojqibaGeT03xrtfzVBo0Zc8nxgL5XG1LHqJicfyx53naftPicHhUokIWJfE6Z4ZM0sibOicCgoeXejGuEG8iaFhNDYyT089hSaRLNZcRCBUDA0g/640?from=appmsg)

卡巴斯基研究人员高置信度地将此次攻击归因于 MoYu Group。该组织与臭名昭著的 BADBOX 僵尸网络关联密切。通过对比命名规则、基础设施重叠（如代理服务平台PXYEDGE和ProxyForU），以及过往对电视盒子的攻击手法，研究人员确认了此次车机攻击是BADBOX生态向车载领域的扩张。

![](https://mmbiz.qpic.cn/mmbiz_png/esHL7Vicu7E8L95iamicnib9UblSdRxUx7rejwIKF5w1GplPYGP3OQKggmCiaUxibwiaR2bqZibdgvPXYM0tYU4LSaXdquqL6FibGzUL5ma4wQ3vnCE0/640?from=appmsg)

安全建议与影响范围

![](https://mmbiz.qpic.cn/mmbiz_png/GibojqibaGeT03xrtfzVBo0Zc8nxgL5XG1LHqJicfyx53naftPicHhUokIWJfE6Z4ZM0sibOicCgoeXejGuEG8iaFhNDYyT089hSaRLNZcRCBUDA0g/640?from=appmsg)

受影响的车机固件主要涉及厂商 DoFun。好消息是，该厂商在收到通报后已修复了相关安全漏洞。

**车主应对措施：**

- 核实固件：若车机系统为DoFun方案，建议咨询经销商确认是否已推送安全补丁。

- 关注异常：留意车机是否出现不明来源的应用安装请求，或异常的网络卡顿（流量被劫持）。

- 正规渠道：仅通过官方渠道进行OTA升级，避免连接不可信的USB设备或安装第三方不明APK。

资讯来源：本文内容基于Securelist（卡巴斯基）发布的报告《The invisible passenger in your car》、The Hacker News等相关报道。

转载自：看雪学苑

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88VEzjic1f7B8a9prz3icdEgQpXH1gOGyCYoZHyUAicqvDfdkVCKTCYm9qicEVTGF7fAosbaxdibXgxBT9na3DsrMjxBOyiadNzFvx5Po/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[【征稿启事】2026 IEEE网络韧性与内生安全国际会议（IEEE CRESS 2026）相约南京，诚邀投稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88Xr95JLPMCj3IEsZGAL0znMgDYy7QcmFibtBvxLR6nTbq4W4vTMnUhAdaobhKG9mibWfVugG7kFoImZBUEf8MqpF5H8AibmLbk1eI/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[欢迎报名！“联盟货架” 征集工作正式启动](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[聚力协同发展 | 中国质量认证中心有限公司南京分公司正式加入联盟，成为副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

2026-06-17

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XRibsIKXF2TFo31YtyfTpzRKp3lqA3JpyMFdGWKGGVtONQDgr2Hfm8pibrCwAiaQn5RWPJxTgelQxwFln0ZDrAwK8YuDWUgNaxFE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

[携手共建产业生态 | 紫光恒越正式升级联盟副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

2026-06-18

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88Ug4pM2QBleSEh81Xt2icXIibBY5o6icibpSFMbFcu4TN9eNvibibict0BCDx8nCYrYViclCu2KGMdx7RnIAdrEvuSGtxKa20mBqH9IPhI/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)**

[里程碑时刻：智己LS9 Hyper搭载原创内生安全技术](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538132&idx=1&sn=77e4efcb6eea205e082f79b82336cc65&scene=21#wechat_redirect)

[邬江兴院士：构建内生安全质量检测体系，筑牢人类可控可信 AI 根基](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539044&idx=1&sn=1791fd1aad5f130fe5d87c46cc4b8687&scene=21#wechat_redirect)

[工信部定调：6G是"十五五"重中之重，商用时间表首次明确](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539882&idx=1&sn=ba4669e35b87fe44673807be8f1832d4&scene=21#wechat_redirect)

[倒计时！一文掌握《公安机关网络空间安全监督检查办法》核心要点，10月1日生效](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539917&idx=1&sn=3b444d9f11c86980921625ba0c82c62f&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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