---
title: 安全简讯（2026.07.27）
url: https://mp.weixin.qq.com/s/r712OnXz1PcxUapMjlYGsQ
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:54:36.263735
---

# 安全简讯（2026.07.27）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZrwV9f40npI2j4qYKFPUb63sGdyvuGgxRI93B4DO9l3MebpBOhEbIzGInBRW1e4icTSoicGPwVgHsPPo22UibEo0tD1Q5QeBPfJiaC4/0?wx_fmt=jpeg)

# 安全简讯（2026.07.27）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. Steam论坛攻击：伪修复程序暗藏挖矿木马**

7月25日，近期，Steam讨论论坛正遭受大规模“ClickFix”社会工程攻击。威胁行为者通过创建随机账户，在论坛中发布看似解决游戏崩溃、物品丢失等问题的修复教程，诱导用户以管理员身份打开PowerShell并运行恶意命令。这些命令会静默下载并启动XMRig加密货币挖矿程序，占用受害者计算机资源进行门罗币挖矿。此类攻击通过显示虚假错误提示或优化进度条，伪装成合法维护工具，使受害者误以为在执行系统修复。由于用户手动操作，攻击可绕过部分安全防护机制。恶意脚本会创建特定目录、排除Defender扫描、添加防火墙规则，并设置计划任务实现持久化。用户若发现“C:\Windows\Background”目录、Defender排除项或“XMRig-”开头的计划任务，应立即进行杀毒扫描或手动清除，必要时重装系统以确保安全。切勿轻信论坛中未知用户提供的PowerShell命令，保持警惕是防范此类攻击的关键。

https://www.bleepingcomputer.com/news/security/steam-forum-clickfix-attacks-infect-gamers-with-xmrig-cryptominers/

**2. 伊朗黑客入侵美水务能源系统篡改PLC**

7月25日，近期，美国联邦机构更新网络安全公告，确认与伊朗有关联的黑客已成功入侵美国水务和能源领域的工业控制系统，且不仅限于窥探，而是直接篡改可编程逻辑控制器（PLC）这种小型工业计算机负责控制水泵、阀门和安全警报等关键设备。攻击者通过OT端口及SSH端口访问暴露在互联网上的工业控制器，使用Studio 5000、EcoStruxure Control Expert等厂商工具窃取项目文件，恶意修改或删除项目逻辑，包括附加指令（AOI），并操纵人机界面（HMI）和监控与数据采集系统（SCADA）的显示数据。更为严重的是，攻击者禁用了关键的关机和报警逻辑，使系统在未向操作员发出任何警报的情况下进入不安全状态，可能导致突发性停电或设备损坏。早在今年4月，相关机构已指出伊朗黑客专门攻击罗克韦尔自动化控制器，而此次更新的警告将施耐德电气和西门子设备也纳入攻击范围，显示威胁正在扩大。

https://securityaffairs.com/195991/apt/iran-linked-actors-breach-are-targeting-us-water-and-energy-control-systems.html

**3. 澳大利亚Origin Energy 200万客户数据泄露**

7月25日，近期，澳大利亚最大综合能源供应商之一Origin Energy披露了一起网络攻击事件，导致部分客户数据遭未经授权访问和泄露。一名自称“John Doe”的黑客声称对此次事件负责，并表示已窃取约200万客户的个人记录，威胁若公司未在14天内回应，将公开全部被盗数据。黑客通过电子邮件向澳大利亚媒体7News透露，曾联系Origin董事会、安全团队和客服部门，但公司未公开回应且未协商后续措施。该说法促使Origin迅速展开紧急调查。据Origin于7月23日发布的更新声明，确认部分客户数据确已泄露，受影响信息可能包括姓名、地址、出生日期、联系电话、账户信息以及信用卡后四位或银行账号后三位。Origin强调，不完整的支付信息无法用于购物或账户访问，同时表示运营系统未受影响，公司正与外部网络安全专家合作调查事件，并将逐一通知确认受影响的客户。此外，Origin已向澳大利亚网络安全中心、联邦警察和信息专员办公室等监管与执法机构通报情况。

https://securityaffairs.com/195973/data-breach/australian-energy-provider-origin-energy-disclosed-a-data-breach-impacting-customer-data.html

**4. OnTrac遭黑客入侵，客户数据面临泄露风险**

7月24日，美国私营包裹递送公司OnTrac近日披露，其企业网络遭黑客入侵，可能已导致客户个人信息泄露。该事件于2026年3月23日被发现，内部调查显示攻击者在3月20日至22日期间访问了某些文件。目前，除姓名外，具体泄露的信息类型尚不明确，公司向当局提交的样本通知中已删去敏感数据元素。针对此次事件，OnTrac已聘请第三方专家协助调查并采取补救措施，以确保数据重新得到保护。声明暗示公司可能已与攻击者达成协议（通常为支付赎金），以换取客户信息不被公开披露。OnTrac在通知中表示，尚未发现因本次事件导致的欺诈或信息滥用行为，也没有理由相信此类风险会变为现实。为降低潜在风险，公司为受影响客户提供为期12个月的免费信用监控和身份保护服务，注册期限为90天。同时建议客户定期检查信用报告和账户报表，若风险较大，可考虑设置欺诈警报或冻结信用。截至报道时，尚无勒索软件组织对该事件声称负责，OnTrac也未披露具体受影响客户数量或是否支付赎金。

https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/

**5. 酒店Wi-Fi遭篡改，用户被劫持至钓鱼页面**

7月24日，近期，黑客通过篡改酒店和会议中心Wi-Fi设备的DNS设置，将用户重定向至伪造的Microsoft 365登录页面以窃取凭据。ReliaQuest披露，该活动自6月起已影响金融服务、法律、医疗等多个行业，覆盖美、印、沙特等国，攻击手法疑似俄罗斯APT28组织所为。攻击者可能利用设备管理接口防护薄弱或漏洞获取权限，修改DNS后注册虚假域名搭建钓鱼门户。更隐蔽的是，攻击者利用设备代码认证流程，使用户在不知情下批准恶意会话，获取合法OAuth令牌从而绕过多因素认证。约三分之一案例还涉及滥用WPAD协议劫持流量。公共DNS无法防御此类攻击，建议使用全隧道VPN和加密DNS，并禁用WPAD及不必要的设备代码认证功能。

https://www.bleepingcomputer.com/news/security/hackers-hijack-hotel-wi-fi-dns-to-steal-microsoft-365-accounts/

**6. Clop团伙利用PTC漏洞攻击PLM系统窃取数据**

7月24日，勒索软件团伙Clop（亦称Cl0p）正发起新一轮数据窃取活动，目标为暴露在互联网上的PTC Windchill和FlexPLM实例。据ReliaQuest报告，攻击者利用编号CVE-2026-12569的严重输入验证错误漏洞（CVSS 9.3），在易受攻击的系统上部署JSP Web Shell，从而远程执行命令并窃取敏感产品数据。该漏洞允许未经身份验证的远程代码执行，影响广泛用于航空航天、国防、汽车、零售及医疗科技等行业的产品生命周期管理（PLM）平台。PTC已于6月17日发布安全补丁，并于6月26日向客户发出威胁加剧警告，CISA随即将其列入已知利用漏洞目录，要求联邦机构三天内完成修补；德国BSI更在半夜紧急联系客户，敦促尽快修复。ReliaQuest建议PTC客户立即为受影响系统打补丁，将其置于VPN或可信访问网关之后，并在怀疑遭入侵时隔离服务器、收集证据并轮换凭证。

https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/

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