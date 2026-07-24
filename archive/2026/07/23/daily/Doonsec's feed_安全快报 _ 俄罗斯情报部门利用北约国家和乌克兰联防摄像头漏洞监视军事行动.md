---
title: 安全快报 | 俄罗斯情报部门利用北约国家和乌克兰联防摄像头漏洞监视军事行动
url: https://mp.weixin.qq.com/s/9V01iepOzB3hGFiqHbEKJw
source: Doonsec's feed
date: 2026-07-23
fetch_date: 2026-07-24T05:02:13.815522
---

# 安全快报 | 俄罗斯情报部门利用北约国家和乌克兰联防摄像头漏洞监视军事行动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibTFtoO0dlPbjY3Na05Ds1ynl3tawupS3PFFEsM2yNmicgNjl56xQIKvibdMWQA0icyZAhy1LH91yJl4NDXnzRNL1FMaz2x1xAYkbI/0?wx_fmt=jpeg)

# 安全快报 | 俄罗斯情报部门利用北约国家和乌克兰联防摄像头漏洞监视军事行动

天懋信息

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**本周安全事件速览**

**07月16日-07月22日**

**01**

**俄罗斯情报部门利用北约国家和乌克兰联防摄像头漏洞监视军事行动**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibQIHWJ6xXibv5bibfg2zJ2lRh8e5xBTbxzoo9jdpmTRc0K5d2wkJ3ib92xMQxd8hNGVqywOmxYQRsdTKVVPTq0yh5XFrTibMANDTlc/640?from=appmsg)

**简要介绍**

荷兰军民用情报机构（AIVD与MIVD）于7月10日联合发布警告，指控至少一个俄罗斯情报部门正系统性地入侵欧洲及乌克兰境内的联网安防摄像头。俄方利用这些摄像头监视北约国家的军事运输路线、运往基辅的武器shipments及乌克兰军队部署。入侵手段并不复杂，主要是扫描暴露在公网的设备，利用默认密码、过时固件和未更改的出厂设置进入摄像头，随后通过图像识别软件自动筛查视频中的军车与物资。荷兰当局仅在境内军事后勤路线附近确认了少量被入侵摄像头并已通知相关方。网络安全公司Censys的扫描数据显示，欧盟、北约成员国及乌克兰境内共有超过8.7万台联网摄像头存在已知漏洞，其中仅荷兰就有超过4.5万台可公开访问。

**文章来源：****The Hacker News**

**02**

**俄黑客组织利用ClickFix虚假验证码等社工手段对乌克兰发动大规模恶意软件攻击**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibSw6FBFNEFUBurKjaaaqYfrTkh6tJPpsFTrXBpBzlMw9J7lY3sM7M81ibKFvF95YOfjHYRlSiaG93LMSkRkicd4mUCDQ0eM9iaP1ia4/640?from=appmsg)

**简要介绍**

乌克兰计算机应急响应团队（CERT-UA）披露，与俄罗斯GRU有关联的黑客组织UAC-0145（Sandworm的子集群）在2026年6月至7月间，通过至少10个被入侵网站，利用ClickFix社会工程学手段对乌克兰发起攻击。攻击者使用定制工具SMARTAXE动态篡改网页，结合EtherHiding技术从以太坊智能合约获取恶意域名，向特定访客显示虚假CAPTCHA验证页面。用户被诱导在终端中执行PowerShell命令，从而下载GHETTOVIBE等多种恶意载荷，以实现持久化、信息侦察和数据窃取。攻击者还通过即时通讯应用，利用伪造的安全工具APK文件（如假ESET安装包），针对Android设备部署功能强大的COWARDDUCK后门，可窃取文件、联系人及实时位置。

**文章来****源****：The Hacker News**

**03**

**东南亚政府与外交机构自2021年起遭GoSerpent恶意软件组织持续窃取情报信息**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibQ7Yd28s5F0pCzJTrq2Le6q4QqW5oiaqW3JpAC6JszLPzlCD7NlQjcakMZGNibFpicQicPIv0qvaPmNbPeWzdbffnK0SkJDpeQQM54/640?from=appmsg)

**简要介绍**

恶意软件GoSerpent自2025年底以来被用于针对东南亚政府实体发起网络攻击，目的是长期访问和收集情报。据悉，该活动于2026年2月发现，其目标是该地区的政府和外交机构。GoSerpent旨在联系外部服务器并部署次级负载，用于系统上的敏感数据和凭证收集。基于Go语言编写的后门程序通过与外部服务器建立加密连接，接收并执行命令。其功能全面，支持启动远程Shell、文件上传下载、建立SOCKS5代理隧道以路由流量并隐藏攻击者真实IP等。攻击链中，GoSerpent还会部署多种辅助工具：用于文件收集的ThumbcacheService、用于凭证转储的Mimikatz和QuarksDumpLocalHash。2026年5月，攻击者重返受害环境，部署了Stowaway代理工具及TmcLoader/TmcPayload数据外泄模块，窃取此前数月收集的敏感文件。据悉，该恶意软件的早期迭代版本自2021年起便已出现。

**文章来****源：****The Hacker News**

**04**

**超20个巴西政府官方网站遭PhantomEnigma恶意攻击劫持被迫沦为网络攻击分发渠道**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibSRJA4ZEVhiahhjvoytq6CZAWI9EUdkFM75b0FOT2JdGjI01EeobIibllfLGusPjYicChLDUiavKvhmA8VD7OJLgy8wobS8agdQ5hw/640?from=appmsg)

**简要介绍**

网络安全机构披露了一起代号为“PhantomEnigma”的大规模网络攻击活动。攻击者成功入侵并劫持了超过20个巴西政府官网（包括市政、公共安全及司法部门门户），将这些高可信度的.gov.br域名用作恶意软件的分发通道，同时利用被盗邮箱发送伪造的警方传票或数字授权书。这些邮件有些包含二维码，另一些则引导收件人前往看似合法政府资源的链接，通过SPF、DKIM和DMARC等身份验证欺骗受害者点击链接，并通过被入侵的政府网站跳转，最终植入恶意安装程序。该恶意软件已进化为模块化的Node.js后门，能在受感染设备中建立持久性，每180秒轮询命令，执行JavaScript或下载窃密程序、远程管理工具等二次载荷。攻击者借此可窃取凭证、访问内部系统，对银行和公共机构构成严重威胁。

**文章来****源：****The Hacker News**

**05**

**第三方医疗供应商英国Craneware与美国Abbott分别遭遇黑客攻击并被窃取数据**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibQ8f458dcH9t2KlbKMUKr1NlibkTxZy4GtfdGOGq3cO5CXHnk9vl2yrRkSYvnMjoBH6ricTibDaWaYEKvKv1hBRB4fzEZMCzXB9Qo/640?from=appmsg)

**简要介绍**

两家知名医疗相关企业先后披露网络安全事件。英国医疗软件公司Craneware Group通报其系统遭遇数据窃取事件，影响了员工数据及部分客户与合作伙伴记录。该公司表示事件已得到控制，未对客户服务及公司运营造成中断。调查显示有大量文件名被查看和窃取，但其中很大一部分数据属于非敏感或已公开的监管数据。与此同时，美国医疗设备与实验室测试巨头Abbott也确认其癌症诊断业务部门的IT系统遭到未经授权访问。该公司强调，该事件未影响任何业务运营、产品生产或服务患者的能力。网络犯罪团伙ShinyHunters声称从Abbott的Exact Sciences业务中窃取了数据。而另一个团伙ShadowByt3$则声称通过入侵Abbott的LabCentral客户门户，窃取了大量产品文件。对此，Abbott表示该门户仅存放公开技术文档，不含敏感客户或商业信息。

**文章来****源：****Bank Info Security**

**06**

# **日本冷冻食品巨头日冷公司遭网络攻击导致冷链物流瘫痪波及全国供应链**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibRgrnDT6jwg1j04qngHPnbtfUA4opJsoRicpY2gbBiamfh2HNr7cBAYsgEticS5kUkbvzyqQfEV62hFfTQWBMdHaZrGYDUvHWnhvI/640?from=appmsg)

**简要介绍**

日本冷冻食品企业日冷公司于2026年7月13日确认遭受网络攻击，导致系统瘫痪。为控制损害影响面，该公司当天即切断集团内部系统连接，致使冷藏仓库装卸及冷冻食品出货全面停滞。此次事件迅速波及全国供应链，日本肯德基因部分食材缺货导致部分门店暂停营业，永旺等大型超市出现冷冻食品库存不足，江崎格力高冰淇淋、藏寿司等企业的冷链配送均受到严重影响。影响甚至蔓延至学校供餐，部分学校被迫更改菜单。日冷公司此次被攻击凸显关键基础设施瘫痪对社会组织的连锁冲击影响。部分受影响服务器存有个人信息，存在数据泄漏风险，公司已向日本个人信息保护委员会提交报告。日冷已成立应急总部，与外部专家合作调查并逐步恢复运营，7月17日起冷链物流已部分重启。

**文章来****源：****Security Affairs**

**07**

**Kratos钓鱼工具窃取多国Microsoft 365会话并绕过多重身份验证**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibSUB6DjEaQVONC3m2zaQcKZJpEJ5eO0ia7hSVqnRm4KLEndURSmuWnfH0Xmz6QhibCZTDibGe43WZbFiaFxLwqbVfDjWzHXwWlFxT8/640?from=appmsg)

**简要介绍**

德国和美国执法部门已摧毁了Kratos钓鱼工具的核心基础设施，印尼当局逮捕了据称开发并运营该套件的黑客。法兰克福检察官网络犯罪部门（ZIT）与德国联邦刑事警察局（BKA）联合宣布，已将200多台服务器下线。调查人员估计，大约有1800名付费用户每月使用Kratos发动约15000次钓鱼活动。Kratos收集的不仅仅是密码。BKA表示，该套件设计用来窃取会话Cookie和登录信息，而该Cookie足以让用户通过双因素认证进入账户。该业务类似于特许经营，BKA称客户为加盟商。他们用加密货币支付，并通过专门网站和Telegram商店注册管理账户和组织活动，即使是技术低的黑客也能将可用的AiTM工具对准目标。自2024年底以来，受害者人数达数十万，分布在30多个国家，主要集中在欧洲和美国。

**文章来****源：****The Hacker News**

**08**

**安永会计师事务所遭未经授权第三方访问导致敏感信息泄露**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibQraVAc9tFmmS6TLlJpS3u8icK2QTwFZTOte9vuFA7EgZk5ibB3tyEzfibFUfibKNOHaJibGvXs7ia4iamTKzIj9QZibthXKORADibbl6RI/640?from=appmsg)

**简要介绍**

安永会计师事务所披露了一起与其IT团队使用的第三方支持工单系统被攻破相关的数据泄露事件。据悉，安永会计师事务所提供审计、税务和交易咨询服务。该公司披露于4月23日在其网络上检测到异常活动，并在外部网络安全专家的协助下启动了对此次安全漏洞的调查。该公司确定在3月28日至4月12日期间有未经授权的第三方访问了该其平台并下载了多份文件。被泄露的信息包括某些个人和财务数据，这些数据包含在或用于准备税务申报时。目前尚不清楚有多少客户受到了此次事故的影响，尚无勒索软件组织宣称对此次攻击负责。安永宣布已确保系统安全，移除未授权访问，并通知联邦当局。公司指出，没有证据显示泄露文件被滥用或针对特定个人进行有针对性的攻击。

**文章来****源：****Security Affairs**

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCWnp4MYTluo2ib4Pibo5QAoxm2iaJME3yPXPLr1QYibicibCZibDib4185YxjKdxtvrcRspzxXj8BqZlnUhibA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCXHBrgOytxrXj5Isuu7Wa0bM6XhWyfjejlJia5dbBFcSpxZGvYibRndWGfODicNTYEpBFkXzuvp547cw/640?wx_fmt=gif)

往期回顾：

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/76BUAjRsqibRssVBTVHhGqVrzZArPQFubticgj5KeASVNMDocDFOAyrWxu2VWfia512IZ5qL6W4nickIKNUuufnB5emPMSWxgribBiaibQ6Z9ic4msM/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247494033&idx=1&sn=53f3d8da45e4860ab7860dc309ecbed7&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/76BUAjRsqibSRHQQM7AZbpurJsJBvNqhfGgrfp9zGLicw5oNhxpW1CicVlo4DjB67EhdwyKbffZgtVCXafjMLpN9qQNqwc8jAWibBYEP2ic1Ud1M/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247494026&idx=1&sn=f09aeeca0518e213960900f79d46ee25&scene=21#wechat_redirect)

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