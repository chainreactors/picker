---
title: 安全简讯（2026.08.18）
url: https://mp.weixin.qq.com/s/5MVinphTWZoJxNRE0ZbVFw
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:54:19.200198
---

# 安全简讯（2026.08.18）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309ZryfZbAnAAaTt3lIwbg9z692t6pgfoKw3Wnmq18V15k0RMRd2La40AFus3N47NhV35PfCKyWxvtK2zkKN3o81cBFpZB6h04JCT4/0?wx_fmt=jpeg)

# 安全简讯（2026.08.18）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. SAP惊现满分漏洞，补丁三天即遭攻击**

8月15日，SAP Commerce Cloud近日曝出一个编号为CVE-2026-58231的严重漏洞，CVSS评分高达10.0分，属最高风险等级。该漏洞源于授权检查和输入验证不足，允许未经身份验证的攻击者滥用默认身份验证客户端，向缺乏充分验证的功能提交精心构造的恶意输入，成功利用后可导致任意代码执行，并危及内部组件安全，严重影响应用程序的机密性、完整性和可用性。SAP发布安全补丁后仅三天，研究机构Defused Cyber即观察到针对蜜罐的实际攻击尝试。值得关注的是，该漏洞此前并无公开的概念验证代码，也未曾有被利用记录，攻击者的身份目前仍不明确。由于SAP Commerce Cloud广泛应用于全球企业电子商务平台，该漏洞的快速利用引发了对企业系统安全响应时效性的高度关注，也凸显了高风险漏洞在补丁发布后短期内即被武器化的现实威胁。

https://securityaffairs.com/197244/security/sap-commerce-cloud-cve-2026-58231-exploited-in-the-wild.html

**2. 新型Mirai变种Evooo1Bot多方位攻击网关设备**

8月15日，网络安全研究人员发现一种名为Evooo1Bot的新型Mirai变种僵尸网络，针对互联网网关设备，将其转为SOCKS5代理节点。自7月起，该恶意软件已攻击Alcatel、NETGEAR、D-Link等多个品牌设备。它重用了Mirai的DDoS引擎，但扩展了加密C2通信、SSH暴力破解、凭证嗅探及漏洞利用等模块。新版本还针对海康威视、Atlassian Confluence、Zyxel、TP-Link等产品。感染后，恶意软件根据CPU架构下载对应版本并清除痕迹，通过443端口加密通信，执行前会检测调试器和沙箱以规避分析。持久化依赖systemd和cron作业。其主要功能包括交互式shell控制、文件传输、HTTP凭证窃取、SOCKS5代理（支持中继模式以隐藏流量和变现）、150种组合的SSH暴力破解，以及16种DDoS攻击方法。建议用户更新固件、修改默认密码、关闭远程访问以防御威胁。

https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/

**3. 苏格兰政府承包商泄露雇员数据**

8月14日，苏格兰政府一家外部承包商发生数据泄露事件，导致约300名苏格兰皇家检控署（COPFS）雇员的个人信息被泄露，包括姓名、职务和工作邮箱地址。COPFS于8月13日披露此事，称该机构于8月5日参与了一项由第三方管理的在线数据成熟度评估，期间评估机构内部网络出现“可疑活动”，从而导致数据丢失。案件、受害者和证人相关信息未受影响。然而，此次泄露的实际范围可能更大，因为数据成熟度评估是苏格兰政府自2021年起启动的“数据成熟度计划”的一部分，每年有多批政府机构参与培训和评估，COPFS可能并非唯一受影响的机构。经调查，负责该评估的主要第三方机构为英国研究公司Data Orchard，该公司近期还与WWF和威尔士政府等大型机构合作。截至发稿，Data Orchard尚未被正式确认为泄露源头，苏格兰政府的其他部门是否同样受影响仍不明确。安全专家警告，即便仅数百名员工的基础信息泄露，攻击者仍可利用姓名、职务和邮箱等信息实施高度定向的网络钓鱼攻击，一旦得手，可能进一步渗透更广泛的政府系统。

https://www.darkreading.com/cyberattacks-data-breaches/scottish-govt-data-breach-prosecutors-office

**4. 壳牌遭Clop勒索，89GB数据被窃**

8月14日，能源巨头壳牌公司近日证实，正在调查一起潜在的安全事件，此前Clop勒索软件团伙声称从该公司窃取了89GB数据。据Clop在暗网泄露网站上的帖子，被盗文件包括工程图纸、设施测试报告、项目计划及设施照片等。壳牌发言人确认已获悉此事，并表示正与安全团队及专家合作开展调查。此次攻击疑似与Clop团伙利用编号为CVE-2026-12569的严重输入验证漏洞有关，该漏洞影响了PTC Windchill和FlexPLM等产品生命周期管理平台。Clop在本次攻击中还声称从通用电气和飞利浦等科技巨头窃取了敏感数据。PTC于6月17日发布补丁，但未确认漏洞已被实际利用。此外，勒索软件信息共享中心和非营利组织ReliaQuest均证实了Clop针对Windchill和FlexPLM的攻击，并指出攻击者部署JSP webshell以窃取PLM平台中的敏感数据。目前壳牌及通用电气、飞利浦等公司尚未就数据泄露细节作进一步回应。

https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/

**5. RingCentral遭入侵，160万账户信息泄露**

8月14日，云通信平台RingCentral于今年7月28日披露，其系统在一次复杂的社会工程攻击后遭入侵，导致部分客户数据被窃取。该公司表示已采取补救措施并停止进一步未经授权的活动，核心平台未受影响，服务持续正常运行。尽管RingCentral未透露攻击者身份，但勒索组织ShinyHunters于7月27日声称对此负责，称窃取了623GB数据。在公司拒绝支付赎金后，该团伙在暗网泄露了包含280GB文件的压缩存档。数据泄露通知服务Have I Been Pwned事后确认，泄露数据包含约160万个账户记录，涉及姓名、电子邮件、电话号码和实际地址。RingCentral作为服务超60万家企业的云通信平台，此次事件再次暴露了第三方服务提供商面临的社会工程攻击风险。目前RingCentral已直接联系受影响客户，未收到通知的用户即未被波及，相关调查仍在进行中。

https://www.bleepingcomputer.com/news/security/ringcentral-data-breach-exposed-info-of-16-million-accounts/

**6. 贷款公司云遭入侵，73万人数据泄露**

8月18日，美国债务整合贷款公司Heights Finance今年5月遭遇一起重大网络安全事件，其使用的第三方云平台被黑客入侵，导致约73.5万名客户的大量敏感财务与个人信息遭泄露。此次事件波及所有通过该公司或其关联品牌获得贷款或咨询过贷款产品的客户，也涉及母公司Curo Management的部分客群。泄露信息极为广泛，不仅包括联系方式，还涵盖银行账号、路由号码等财务数据，以及社会安全号码、税务识别号、驾照或州身份证等政府颁发的身份证明文件，甚至包含客户与公司客服互动时留下的各类个人资料。Heights Finance于5月7日发现此次入侵，当时检测到黑客已成功侵入存储客户数据的云平台。公司强调，该事件仅限于云平台本身，并未影响其贷款管理系统或其他内部网络，且已确认云平台已恢复安全可靠，当前不存在持续威胁。为应对此事，公司已聘请专业网络安全公司持续监控暗网论坛、市场及其他地下平台，试图追踪是否有被盗信息流出。截至公司向德克萨斯州监管机构报告时，尚未发现任何证据表明泄露信息已在暗网上被公开或流通，也没有黑客组织公开声称对此次攻击负责。

https://therecord.media/financial-info-leak-debt-consolidator

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