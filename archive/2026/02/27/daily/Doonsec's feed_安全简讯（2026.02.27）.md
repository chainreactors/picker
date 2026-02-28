---
title: 安全简讯（2026.02.27）
url: https://mp.weixin.qq.com/s/YxFE1GOnGqqFAl8UrybPxw
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:57:04.645675
---

# 安全简讯（2026.02.27）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZrwVdkdfnaza6lDiaZv2BacicDFNauxATIfNmpOMA394SJLlYjVzdnvgSSFBt7bXOSNXYVT6ialo1rmkVyUK9c2WicF7OicRgEicbTszc/0?wx_fmt=jpeg)

# 安全简讯（2026.02.27）

启明星辰安全简讯

![]()

在小说阅读器中沉浸阅读

**1. 科特迪瓦航空遭INC勒索软件攻击致数据泄露**

2月24日，服务于西非国家科特迪瓦的主要航空公司科特迪瓦航空公司遭遇网络攻击，被迫启动业务连续性计划。据公司声明证实，黑客于2月8日入侵其系统，导致信息系统部分内容受影响，技术团队紧急协助航班及其他运营维护。此次事件中，INC勒索软件团伙声称窃取了208GB数据，涉及服务提供商、乘客及员工敏感信息，并威胁在2月24日前支付未公开赎金，否则将泄露数据。科特迪瓦航空公司表示，已将事件通知法国国家信息系统安全局（ANSSI）和科特迪瓦电信监管局（ARTCI），并召集科特迪瓦计算机应急响应小组（CI-CERT）及国际专家展开调查，以确定数据泄露范围。公司强调，尽管系统受创，但航班计划保持稳定，将继续严格遵守国际安全标准运行，并尽一切努力减轻事件后果。

https://therecord.media/air-cote-divoire-confirms-cyberattack

**2. Optimizely遭语音网络钓鱼攻击致数据泄露**

2月23日，总部位于纽约的广告技术公司Optimizely近日遭遇严重数据泄露事件，威胁行为者通过复杂的语音网络钓鱼（vishing）攻击入侵其部分系统，窃取了“基本业务联系信息”。Optimizely在全球拥有21个办事处、近1500名员工，服务超过10,000家企业客户，包括H&M、PayPal、Zoom、丰田、沃达丰、壳牌、Salesforce和耐克等知名品牌。据Optimizely发送给受影响客户的违规通知信显示，2月11日，攻击者联系该公司并声称已获得系统访问权限。公司声明强调，攻击者虽成功入侵部分内部业务系统、CRM记录及后台运营文档，但未能提升权限、安装恶意软件或创建后门，且无证据表明其访问了敏感客户数据或个人信息。Optimizely表示，业务运营未受干扰，但警告客户警惕利用被盗数据发起的进一步网络钓鱼攻击。此次事件被指与ShinyHunters勒索组织存在关联。

https://www.bleepingcomputer.com/news/security/ad-tech-firm-optimizely-confirms-data-breach-after-vishing-attack/

**3. 朝鲜Lazarus用Medusa攻击美医疗及非营利机构**

2月24日，Symantec与Carbon Black威胁猎人团队最新报告显示，与朝鲜关联的Lazarus Group（别名Diamond Sleet、Pompilus）在中东一家未具名机构攻击中部署了Medusa勒索软件，并试图攻击美国医疗机构未遂。Medusa由网络犯罪组织Spearwing于2023年推出，作为勒索软件即服务（RaaS）项目，已宣称实施超366起攻击。分析Medusa数据泄露站点发现，2025年11月初以来，美国四家医疗及非营利机构遭袭，包括心理健康领域非营利机构和自闭症儿童教育机构，平均勒索金额达26万美元。此次攻击标志着Lazarus战术转变。该组织过去常使用定制勒索软件（如SHATTEREDGLASS、Maui、H0lyGh0st），但2024年10月起转向现成加密工具，如Medusa和Qilin。攻击中，Lazarus使用了多种工具：定制代理工具RP\_Proxy、凭证窃取程序Mimikatz、专用后门Comebacker、信息窃取工具InfoHook、远程访问木马BLINDINGCAN（别名AIRDRY、ZetaNile）及Chrome密码提取工具ChromeStealer。

https://thehackernews.com/2026/02/lazarus-group-uses-medusa-ransomware-in.html

**4. CarGurus遭ShinyHunters泄露1200万账户数据**

2月25日，美国数字汽车交易平台CarGurus遭遇大规模数据泄露，超1240万账户敏感信息被ShinyHunters组织泄露。该平台作为线上购车领域核心参与者，每月吸引约4000万访客，业务覆盖美国、加拿大和英国，提供车辆定价、经销商评价及历史记录等工具。此次泄露源于勒索未遂，泄露数据包含电子邮件、账户ID、金融申请详情、经销商信息、姓名、电话号码、地址、IP地址及汽车金融申请结果，文件压缩后达6.1GB，已被数据泄露监控服务HaveIBeenPwned收录。泄露事件带来多重风险：姓名、邮箱、电话等个人信息可被用于高仿真网络钓鱼和社会工程攻击；金融申请数据泄露为身份盗窃和金融诈骗提供便利；账户信息泄露加剧账户盗用风险，尤其是密码复用场景；物理地址和IP数据泄露引发隐私担忧，可能招致定向营销、跟踪骚扰等恶意行为。ShinyHunters近期频繁针对大型企业发动攻击，团伙主要利用社会工程手段，特别是语音钓鱼（vishing），窃取凭证并访问Salesforce、Okta、Microsoft 365等SaaS平台。

https://securityaffairs.com/188491/cyber-crime/shinyhunters-cyberattack-on-cargurus-impacts-12-4-million-users.html

**5. 永利度假村遭ShinyHunters数据泄露**

2月25日，永利度假村证实其服务器遭网络犯罪团伙ShinyHunters攻击，导致员工敏感数据被盗。黑客声称已删除数据，但永利无法验证这一说法，引发对勒索谈判及赎金支付的猜测。此次事件中，ShinyHunters于2月20日宣称攻击，并披露利用Oracle PeopleSoft漏洞及员工凭证在2025年9月入侵系统，泄露数据包括员工全名、邮箱、电话、职位、薪水、入职日期、出生日期等个人信息。永利度假村发言人表示，事件发生后立即启动响应协议，联合外部网络安全专家展开调查，并强调“数据安全是首要任务”。公司向员工提供免费信用监控及身份保护服务，但拒绝评论是否支付赎金。Huntress安全专家Dray Agha指出，黑客“删除数据”的承诺通常是勒索谈判完成的标志，但不可信，数据副本可能被保留、共享或出售，无法通过技术手段验证彻底删除。

https://www.theregister.com/2026/02/25/wynn\_resorts\_shinyhunters/

**6. UFP Technologies遭网络攻击致文件被盗及系统中断**

2月25日，马萨诸塞州医疗器械制造商UFP Technologies于2026年2月14日检测到IT系统入侵事件，周二向美国证券交易委员会提交8-K文件披露细节。作为专注于医疗器械、无菌包装及医疗保健组件的合同制造商，该公司此次事件涉及文件被盗、部分IT系统中断，并影响计费及客户送货标签生成系统。调查显示，攻击者窃取了文件，但具体泄露信息类型及是否包含个人信息仍在确认中。UFP强调，公司已启动应急预案并依托数据备份系统，自事件发现以来，运营在所有实质性方面均已恢复，且预计大部分控制与调查费用将由保险承担，未对财务造成实质性影响。尽管事件特征符合勒索软件攻击模式（数据窃取与文件加密恶意软件部署），但截至目前尚无已知勒索软件组织宣称对此负责。公司表示，此次事件未导致长期运营中断，应急措施有效保障了业务连续性。

https://www.securityweek.com/medical-device-maker-ufp-technologies-hit-by-cyberattack/

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