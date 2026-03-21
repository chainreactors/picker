---
title: 安全简讯（2026.03.20）
url: https://mp.weixin.qq.com/s/gN44AgZAiQ5aeFaRT_8ygA
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:05:57.731803
---

# 安全简讯（2026.03.20）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309ZrzKWyicxoBQDeAKXL2uJSC6GicPRMwicdkaIk2mrYgTkdFm0rD4I7pvicrtm2GjOfGFhdxrwol2CCcHdB2uTI3d5OUoLVa6CavaGoc/0?wx_fmt=jpeg)

# 安全简讯（2026.03.20）

启明星辰安全简讯

![]()

在小说阅读器中沉浸阅读

**1. 法国戴高乐号航母位置因Strava应用泄露**

3月20日，法国媒体《世界报》近日披露，2026年3月13日上午10时35分，法国海军年轻军官亚瑟（化名）在航母甲板上跑步，使用智能手表记录了约7公里、耗时35分钟的运动数据。由于该军官的Strava个人资料设置为“公开”，任何人都可查看其运动轨迹，从而暴露了法国海军航空母舰戴高乐号在地中海靠近塞浦路斯和土耳其附近的实时位置。法国总统马克龙于3月3日宣布部署法国海军特遣部队，包括戴高乐号航空母舰、三艘护卫舰和一艘补给舰。当时戴高乐号正在波罗的海参加北约演习，原计划停留至5月，但随后被部署至地中海区域。此次部署正值以色列、美国和伊朗之间战争爆发后数日。专家警告，此类数据可能帮助对手识别和锁定军事目标，凸显健身追踪器带来的持续隐私问题。

https://securityaffairs.com/189696/intelligence/french-aircraft-carrier-charles-de-gaulle-tracked-via-strava-activity-in-opsec-failure.html

**2. Navia数据泄露影响270万用户敏感信息**

3月19日，美国福利管理解决方案提供商Navia Benefit Solutions近日通知近270万人，其敏感信息在数据泄露事件中被攻击者获取。该公司为美国1万多家雇主提供灵活支出账户（FSA）、健康储蓄账户（HSA）、健康报销安排（HRA）、通勤福利和COBRA服务等福利管理服务。调查显示，黑客在2025年12月22日至2026年1月15日期间能够访问该公司系统，公司于1月23日发现可疑活动。Navia表示立即做出响应并启动调查以确定事件的潜在影响。调查确定未经授权的行为者在上述期间访问并获取了特定信息。被访问和可能外泄的数据类型包括：全名、出生日期、社会安全号码（SSN）、电话号码、电子邮件地址、健康报销安排（HRA）参与信息、灵活支出账户（FSA）信息、综合Omnibus预算协调法案（COBRA）注册信息。公司强调数据泄露未暴露索赔详情或财务信息。尽管如此，暴露的数据足以使威胁行为者针对受影响个人部署钓鱼和社会工程攻击。

https://www.bleepingcomputer.com/news/security/navia-discloses-data-breach-impacting-27-million-people/

**3. Speagle恶意软件劫持Cobra DocGuard窃取数据**

3月19日，网络安全研究人员近日发现名为Speagle的新型恶意软件，该软件劫持合法程序CobraDocGuard的功能和基础设施进行数据窃取。CobraDocGuard是由EsafeNet开发的文档安全和加密平台。此次攻击活动被追踪为Runningcrab，目前尚未归因。Speagle旨在秘密收集受感染计算机的敏感信息，并将其传输至被攻击者攻陷的CobraDocGuard服务器，将数据外泄过程伪装成客户端与服务器之间的合法通信。该恶意软件专门针对安装了CobraDocGuard数据保护软件的系统，表明攻击者可能有意针对特定组织进行情报收集或工业间谍活动。研究人员认为这最有可能是国家支持的行为者或可雇佣的私营承包商所为。Speagle为32位.NET可执行文件，启动后首先检查CobraDocGuard安装文件夹，然后分阶段收集并传输受感染机器的数据，包括系统详情和特定文件夹中的文件，如包含网页浏览器历史和自动填充数据的文件夹。

https://thehackernews.com/2026/03/speagle-malware-hijacks-cobra-docguard.html

**4. Magento PolyShell漏洞允许未授权代码执行**

3月19日，电子商务安全公司Sansec近日披露名为"PolyShell"的新漏洞，该漏洞影响所有MagentoOpenSource和AdobeCommerce稳定版2.4.9安装，允许未授权攻击者执行代码和接管账户。目前尚未发现该漏洞在野外被积极利用的迹象，但Sansec警告利用方法已在传播，预计自动化攻击即将开始。该安全问题源于Magento的RESTAPI接受文件上传作为购物车项目自定义选项的一部分。当产品选项类型为"文件"时，Magento会处理嵌入的file\_info对象，其中包含base64编码的文件数据、MIME类型和文件名。文件被写入服务器上的pub/media/custom\_options/quote/目录。"PolyShell"名称源于其使用多态文件，该文件可同时作为图像和脚本运行。根据Web服务器配置，该漏洞可通过远程代码执行（RCE）或存储型跨站脚本（XSS）实现账户接管，影响Sansec分析的大多数商店。研究人员调查了所有已知的Magento和AdobeCommerce商店，发现许多商店暴露了上传目录中的文件。

https://www.bleepingcomputer.com/news/security/new-polyshell-flaw-allows-unauthenticated-rce-on-magento-e-stores/

**5. Bitrefill遭朝鲜Bluenoroff黑客组织攻击**

3月19日，加密货币礼品卡商店Bitrefill近日表示，月初遭受的攻击很可能由朝鲜Bluenoroff黑客组织实施。调查期间，该平台观察到与之前归因于朝鲜威胁行为者的攻击相似的指标，包括战术、恶意软件、IP和电子邮件地址。Bitrefill是一家中型电子商务平台，允许用户使用加密货币在150个国家的商店购买礼品卡。该平台支持全球600多家移动运营商和数千个品牌。3月1日，Bitrefill宣布网站和应用访问出现技术问题。次日，公司披露发现安全问题并将所有服务下线。调查发现，攻击源于被攻陷的员工笔记本电脑。攻击者窃取了旧版凭据，并使用这些凭据访问包含生产密钥的快照，随后将访问权限升级至Bitrefill更大的基础设施，包括部分数据库和一些加密货币钱包。此次攻击被发现是因为Bitrefill注意到可疑的供应商采购模式、礼品卡库存和供应链被利用，以及一些"热"钱包被掏空。约18,500条购买记录在泄露中被暴露，包含客户电子邮件地址、IP地址和加密货币支付地址。其中1,000条购买记录的客户姓名也被暴露。尽管这些信息以加密形式存储，Bitrefill指出攻击者可能已获得解密密钥。

https://www.bleepingcomputer.com/news/security/bitrefill-blames-north-korean-lazarus-group-for-cyberattack/

**6. Perseus安卓恶意软件窃取用户笔记敏感信息**

3月19日，移动安全公司ThreatFabric近日发现名为Perseus的新型安卓恶意软件，该软件专门检查用户创建的笔记以窃取密码、恢复短语或财务数据等敏感信息。该威胁趋势在过去八个月出现，用户寻求免费或低成本方式观看体育直播。攻击者利用IPTV应用诱饵分发恶意软件，其中一款传播恶意软件的应用名为RojadirectaTV，是流行的体育流媒体服务。Perseus的加载器可绕过安卓13及以上版本的侧载限制，与分发Klopatra和Medusa恶意软件的加载器相同。Perseus主要针对土耳其和意大利的金融机构以及加密货币服务。通过滥用安卓辅助功能，Perseus赋予操作者完全远程控制权限，可连续截取屏幕截图并串流至操作端、模拟点击和滑动、开启或阻止应用、启用黑屏覆盖隐藏活动、实施覆盖攻击和键盘记录。Perseus的不寻常功能是针对安卓笔记应用，这是首次发现安卓恶意软件检查设备个人笔记中的敏感详情。

https://www.bleepingcomputer.com/news/security/new-perseus-android-malware-checks-user-notes-for-secrets/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

启明星辰安全简讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

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