---
title: 安全简讯（2026.05.06）
url: https://mp.weixin.qq.com/s/jfS2EYW2HVYUn57DMWELUg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:27:38.051390
---

# 安全简讯（2026.05.06）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309Zrwb7o1amPfuGVXRtyaJSKOFfSF8J3snZn8Xj0PkSSftviapeLZfE00Z565cb8g4ej3llSgU96X5E84XL2fBrcNERIabKktCxaRE/0?wx_fmt=jpeg)

# 安全简讯（2026.05.06）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. 教育巨头Instructure被黑，2.8亿用户数据泄露**

5月5日，近期，自称为ShinyHunters的勒索团伙声称，已成功攻破教育技术巨头Instructure的系统，并窃取了约2.8亿条与学生和教职工相关的数据记录，涉及8809所高校、学区和在线教育平台。Instructure是一家以Canvas学习管理系统闻名的云教育技术公司，全球众多学校和大学依赖该系统管理课程作业、评分及沟通。上周五，该公司披露正在调查一起网络攻击事件，随后确认发生数据泄露，用户姓名、电子邮件地址及私人信息被曝光。威胁行为者随后公布了一份包含8809个受影响机构的名单，并附有每个机构的记录数量，少则数万，多则数百万。攻击者声称，他们利用了Canvas的数据导出功能，包括DAP查询、配置报告及用户API，成功收集了数百GB的用户记录、消息及注册数据。尽管Instructure未就多次邮件询问作出回应，部分高校已开始发布相关声明。科罗拉多大学博尔德分校警告称，这是一起全国性事件，波及多家机构；罗格斯大学表示尚未收到直接影响通知，Canvas平台仍正常使用；蒂尔堡大学则确认调查正在进行中，尚无法确定学生和教职工数据是否受到影响。

https://www.bleepingcomputer.com/news/security/instructure-hacker-claims-data-theft-from-8-800-schools-universities/

**2. 高纬环球确认数据泄露，两大黑客组织声称负责**

5月5日，房地产服务巨头高纬环球（Cushman & Wakefield）近日证实发生数据泄露事件，此前两个网络犯罪组织ShinyHunters和Qilin分别声称对此次攻击负责。该公司一位发言人告诉《注册报》，此次攻击范围“有限”，源于一次语音钓鱼攻击，表明一名员工受到了社交工程的欺骗。该发言人表示，公司已启动应对方案，采取措施遏制未经授权的活动，并聘请第三方专家协助调查，强调系统和运营仍在正常进行，对客户数据安全负有高度责任。ShinyHunters在发给媒体的消息中声称，他们于5月1日攻击了高纬环球，窃取了“超过50万条Salesforce记录，其中包含个人身份信息及其他内部公司数据”，并设定了5月6日的最后期限要求公司联系以防止数据泄露，但据称这一期限并未得到回应。Qilin则于5月4日在其数据泄露网站上列出了高纬环球，但未详细说明攻击方式。

https://www.theregister.com/2026/05/05/cushman\_wakefield/

**3. Vimeo数据泄露事件导致11.9万人的个人信息曝光**

5月5日，据数据泄露通知服务Have I Been Pwned披露，ShinyHunters勒索团伙在4月份入侵在线视频平台Vimeo后，窃取了超过11.9万人的个人信息。Vimeo于4月27日披露，在数据异常检测公司Anodot发生数据泄露事件后，客户和用户数据遭到未经授权的访问。Vimeo表示，被访问的数据库主要包含技术数据、视频标题和元数据，在某些情况下还包括客户的电子邮件地址。但公司强调，此次攻击未造成任何业务中断，攻击者也未能获取用户的登录凭证或财务信息。检测到漏洞后，Vimeo立即禁用了所有Anodot凭证，移除了Anodot与系统的集成，聘请第三方安全专家协助调查，并通知了执法部门。在Vimeo披露此事后，ShinyHunters因勒索未果，在其暗网数据泄露网站上发布了106GB的被盗文件存档。该勒索团伙声称，因Anodot的安全问题导致Vimeo的Snowflake和BigQuery实例数据泄露，并指责公司未能与其达成协议。

https://www.bleepingcomputer.com/news/security/vimeo-data-breach-exposes-personal-information-of-119-000-people/

**4. 黑客利用Weaver E-cology严重漏洞实施远程攻击**

5月4日，自3月中旬以来，黑客一直在利用Weaver E-cology办公自动化系统中的一个严重漏洞（CVE-2026-22679）执行侦察命令。该漏洞影响3月12日之前的E-cology 10.0版本，是一个未经身份验证的远程代码执行漏洞。其根源在于系统暴露的调试API端点不当地允许用户提供的参数在未经身份验证或输入验证的情况下，直接到达后端远程过程调用功能，攻击者可借此传递精心构造的值，在服务器上以系统命令权限执行任意代码。值得注意的是，攻击行为发生在软件供应商发布安全更新后的第五天，以及漏洞公开披露前的两周，表明攻击者可能通过逆向补丁或独立发现了该漏洞。据威胁情报公司Vega的研究人员记录，这些恶意活动持续了约一周时间，每次攻击包含多个不同阶段。攻击者虽然有机会利用漏洞实现远程代码执行，却从未在目标主机上建立持久会话。

https://www.bleepingcomputer.com/news/security/weaver-e-cology-critical-bug-exploited-in-attacks-since-march/

**5. Trellix披露源代码库遭未授权访问**

5月4日，网络安全公司Trellix近日披露了一起数据泄露事件，攻击者获得了其源代码库“部分”的访问权限。Trellix是由McAfee Enterprise和FireEye于2021年10月合并而成的全球性网络安全公司，为全球超过5万家企业和政府客户提供服务，保护着超过2亿个终端设备。根据周一更新的官方声明，该公司目前正在外部法医专家的协助下对事件进行调查。Trellix表示，截至目前尚未发现威胁行为者利用或篡改其所访问源代码的任何证据。公司强调，在发现源代码库遭未授权访问后，已立即与顶尖取证专家合作处理此事，并同时通知了执法部门。根据当前调查结果，公司没有发现任何证据表明源代码发布或分发过程受到影响，也未发现源代码被实际利用。Trellix在其官方声明中表示，将在调查结束后酌情分享更多细节。

https://www.bleepingcomputer.com/news/security/trellix-discloses-data-breach-after-source-code-repository-hack/

**6. Ameriprise Financial数据泄露影响近4.8万人**

5月3日，Ameriprise Financial近日披露了一起数据泄露事件，约4.8万名美国个人的个人信息遭到未经授权访问。该公司在入侵开始约16天后，于2026年3月18日发现此次事件，并向缅因州总检察长提交了泄露通知。Ameriprise表示，攻击者访问了包含姓名、地址、财务账户详情、部分情况下的社会安全号码等个人身份信息的存储数据和文件。公司确认未发生任何未经授权的交易或资金转移，业务运营也未受到影响。目前，Ameriprise已聘请外部网络安全专家协助调查，并为受影响的个人提供信用和身份监控服务。值得关注的是，与后续诉讼相关的法庭文件显示，ShinyHunters勒索团伙声称对此次事件负责，并威胁泄露超过200GB的内部数据，但相关诉讼已被撤销，Ameriprise也未公开证实ShinyHunters与该事件的关联。

https://securityboulevard.com/2026/05/ameriprise-financial-data-breach-exposes-personal-information-of-48000-customers/

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