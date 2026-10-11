---
title: 知名云因勒索攻击瘫痪，政府交通银行民生等数百个组织受影响
url: https://mp.weixin.qq.com/s/_6r9PykNBiXoKPAmJ3s51Q
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:25.514011
---

# 知名云因勒索攻击瘫痪，政府交通银行民生等数百个组织受影响

# 知名云因勒索攻击瘫痪，政府交通银行民生等数百个组织受影响

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vI437xjqWcNyOqqwqLp91PIWOUkeSJhzu6HT2QVMuiaugoC6icsQ5RLzAzjicgywHzBGad8lIpR6w1g/640?wx_fmt=jpeg)

软银旗下云服务商IDC Frontier遭受勒索软件攻击，位于白河数据中心的东日本Region 1发生故障，4个可用区的虚机均无法启动，部分数据难以直接提取或恢复，官方建议用户使用自己独立备份的数据进行恢复；

官方称该事件影响了495家组织，其中涉及铁路、航空、物流、电商、政府等大量公共服务，大量组织纷纷报告服务中断和数据泄露，涉及JR东日本、JR九州、日水物流 等大型企业；

攻击者声称封锁上万个虚机，加密超3.6PB数据，甚至直接在客户的云管理控制台发布勒索信，目前尚不确定其身份信息。

前情回顾·云服务威胁态势

* [AI重塑网络威胁！孤狼黑客3天攻破跨国企业复杂云环境](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516248&idx=1&sn=f593ae42b73f230b52441d760fdf1742&scene=21#wechat_redirect)
* [阿里云核心域名遭劫持，Shadowserver扮演何种角色？](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247514485&idx=1&sn=b79ac979390502df50bea6aa05bdd19b&scene=21#wechat_redirect)
* [云存储巨头Snowflake被黑，165家知名企业遭殃](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247511918&idx=1&sn=84e8748273f6ebc4f412578d37a4d505&scene=21#wechat_redirect)
* [芬兰云服务商遭勒索攻击，导致瑞典众多公共机构系统瘫痪](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510898&idx=1&sn=c185ff8e9f62642b486415343e9ec597&scene=21#wechat_redirect)

安全内参10月10日消息，日本大型云服务商、软银旗下企业IDC Frontier近日披露，旗下IDCF Cloud云服务遭到勒索软件攻击，导致为日本东部地区提供服务的数据中心集群发生故障。

IDC Frontier表示，攻击于当地时间10月7日凌晨3时40分开始，公司被迫关闭相关网络和系统。

IDCF Cloud在公告中称：“经调查确认，东日本一区（East Japan Region 1）发生的服务中断是由第三方发起的勒索软件攻击所致。”公告还称，目前仍在调查事件的具体原因及影响范围。此次攻击影响了495家使用其云服务的企业和地方政府。

IDCF Cloud是IDC Frontier运营的基础设施即服务（IaaS）平台，该平台在日本的数据中心提供虚拟服务器、存储和网络资源，客户可用其运行网站、应用程序及业务系统。

攻击者声称封锁上万个虚机，

加密超3.6PB数据

IDC Frontier在发现攻击后，随即隔离并关闭了东日本一区的受影响系统，以防攻击进一步扩散。目前，公司正着手查明并阻断入侵路径，同时检查其他区域的安全状况。

在确认各区域安全之前，IDCF Cloud已主动暂停所有区域客户对管理控制台的访问。待确认安全后，公司将恢复相关访问权限。

有客户在管理控制台访问权限被锁定前截取了屏幕内容。截图显示，攻击者声称仅用7分钟就突破了IDCF Cloud东日本一区的基础设施防线。

攻击者还声称，他们加密了225个数据库，涉及数据总量达3.6 PB；入侵了239台虚拟机管理平台（Hypervisor）；封锁了1.6万个虚拟机磁盘；并删除了554153个快照。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NACxXf8s4eAeWiarzQOENS7Ix980zoic5KZAWaqhydzuRzUushJSMVhKBpnyx7SDqJbFPlFhBUic3CG7Xn3fTKFowpWYdRhpCAwRg/640?wx_fmt=jpeg&from=appmsg)

图：IDCF Cloud客户在平台管理控制台上看到的攻击者留言

大量组织报告服务中断和数据泄露

日本最大的铁路运营商JR东日本及其旗下的信用卡公司View Card，是最早确认受到影响的企业之一。两家公司表示，由于使用了IDCF Cloud的邮件发送服务，最多可能有609万条记录被他人获取；而JR九州则报告称，有130万封电子邮件受到影响。  两家公司均表示，信用卡号码、家庭住址和电话号码没有泄露。

日本水产及食品企业日水株式会社在7日宣布，旗下物流子公司日水物流使用的第三方数据中心疑似遭到未经授权的访问，导致相关系统中断。

受此影响，日水物流目前无法正常发货或收货，并正在调查是否有个人信息或客户数据泄露。尚不清楚日水此次中断是否与IDCF Cloud遭受的攻击有关。

据Japan Cyber Watch统计，已有茨城县警察、电商平台FutureShop、新闻社Jiji Press等数十家组织确认，受到此次事件影响。

日本网络威胁态势日益严峻，

政府发布预警

网络安全企业Macnica的研究人员Yutaka Sejiyama表示，近期已有多家日本大型企业成为网络攻击目标。

Macnica的数据显示，今年年初以来，该公司记录了119起涉及个人信息被盗或数据暴露的网络安全事件，其中83起发生在7月1日至10月6日期间。相比之下，按相同标准，该公司2025年全年记录了84起此类事件，2024年全年则仅有62起。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NCaLxe6VVAfeGu3eIlcs5E01EibjGWVGNm7HAzzOc49SJiayx0j9y5bqMh4eSkeIw9jmVlicRSjvbvbOVzUIknzhbm7F7sKwnbk4A/640?wx_fmt=jpeg&from=appmsg)

图：针对日本机构的已确认网络攻击事件数量

这些事件表明，攻击者正不断探测网站和API，寻找访问控制、配置及身份验证方面的安全弱点，并利用已公开一段时间的已知漏洞（即N日漏洞）实施攻击。

Sejiyama表示，过去，要发现特定网站的安全漏洞，通常需要投入大量时间和精力，因此小型目标对攻击者的吸引力相对有限。

如今，功能日益强大且成本低廉的AI工具不断涌现，可能正在改变这一局面，使攻击者能够更广泛、更深入地排查系统安全弱点。

日本政府已于周五发布警告，要求各方提高警惕，防范数量持续增加、手段日益复杂的网络攻击。

日本国家网络安全办公室已向各政府部门下发相关指示，并要求进一步向地方公共机构和私营企业传达。

指示内容包括及时更新安全防护措施、使用高强度密码，以及加强整个供应链的网络安全防护。指示还提醒各方，要警惕攻击者可能冒充网络安全防护人员实施攻击，并指出AI正在让安全漏洞变得更加复杂。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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