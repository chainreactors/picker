---
title: 安全简讯（2026.09.23）
url: https://mp.weixin.qq.com/s/wnJGclv6i79adG21MtBy6Q
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:02:59.848683
---

# 安全简讯（2026.09.23）

# 安全简讯（2026.09.23）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**1. AWS AgentCore曝提示注入漏洞**

9月21日，AWS的AgentCore平台上的AI代理可能将敏感凭证泄露给攻击者。Palo Alto Networks旗下Unit 42研究人员演示了一种提示注入攻击，尽管平台使用了加密凭证库，仍成功窃取凭证。AWS审查后认为报告仅供参考并结案，称客户需自行设置AI代理可访问的资源，默认配置存在泄露风险。AI代理需访问文件、工具和外部服务才能发挥作用，AgentCore Harness默认内置shell工具。AWS将令牌、密码和API密钥加密存储在AgentCore Identity保险库中，但当代理需用凭证认证时，密钥会临时解密并以明文存入内存，而shell工具可访问同一内存区域。代理以root运行，对原本隔离的系统拥有完全访问权限。研究人员让一个“更宽松模型”为虚假公司处理支持工单，在票据中植入恶意提示，引导运行Python脚本进行“诊断”，AI代理随即通过一个HTTP POST请求将JWT和MCP服务器URL泄露给模拟攻击者。该JWT是AI代理的永久主密钥，可解锁其连接的所有后端服务。研究凸显提示注入可危及shell工具可访问的一切，包括文件系统、网络、进程内存和下游服务；缩小shell范围又会剥夺代理功能。

https://cybernews.com/security/aws-agentcore-platform-credential-leak/

**2. ShinyHunters声称利用零日漏洞入侵FBI系统**

9月22日，ShinyHunters勒索团伙声称利用Oracle PeopleSoft全新零日漏洞入侵FBI系统，获得内部访问权限并窃取员工和求职者敏感数据。该组织称漏洞允许远程代码执行，周一晚间利用其访问FBI系统后横向转移至AWS GovCloud基础设施，声称窃取2TB至3TB数据，涉及现任及前任员工、求职者和其他内部记录，并破坏刑事司法、人力资源、Medlink等服务，还称正利用同一漏洞攻击财富500强公司。FBI证实正在调查相关未经授权活动，但未确认系统是否遭入侵或数据是否被盗。ShinyHunters分享截图显示FBI招聘网站被篡改，换上月亮伊布标志并声称所有FBI数据均已泄露，包括敏感PII/PHI及申请人信息。该组织称FBI很快将受影响系统下线，多个FBI网络访问权限同时被终止。ShinyHunters分享两条样本记录，据称分别与一名FBI特工及局长Kash Patel有关，但未获独立核实。404 Media率先报道，称收到约5,000条据称FBI员工记录样本并核实部分信息准确。ShinyHunters称通过PeopleSoft零日漏洞获得初始访问，删除活动证据后转向企业和财富500强公司，并声明此次攻击是对FBI FLASH 2026年5月报告的报复，否认相关指控，给FBI一周时间纠正报告，拒绝透露是否公布数据，称不担心被捕。

https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/

**3. Check Point 紧急修复高危零日漏洞**

9月22日，CheckPoint已发布针对CVE-2026-93616的紧急热修复程序，该漏洞是其安全管理服务器中的一个关键路径遍历漏洞，已被攻击者积极利用。攻击者无需登录即可利用此漏洞上传恶意脚本并在易受攻击的服务器上执行。由于管理服务器控制着CheckPoint部署中的安全策略、管理员活动和系统日志，一旦遭到入侵，可能对企业网络造成更广泛的影响。该漏洞不仅影响CheckPoint的主安全管理服务器，还影响安全管理服务器、多域安全管理服务器、日志服务器、多域日志服务器和SmartEvent等多个产品。CheckPoint已在R82.20安全热修复程序中修复该问题，并敦促客户尽快采取行动。该公司透露，该漏洞“已被广泛利用”，已知有少数客户遭受攻击，但实际受害者人数可能更高，因为部分入侵事件可能未被发现或从未向CheckPoint报告。该公司还在安全公告中发布了入侵指标（IOC），使安全团队能够检查系统和日志以发现攻击迹象。如果无法立即安装热修复程序，建议将存在漏洞的系统置于防火墙后，并仅允许来自受信任IP地址的访问，但这只是临时措施。

https://securityaffairs.com/199549/security/check-point-fixes-a-new-actively-exploited-critical-security-flaw.html

**4. 新型恶意软件利用AI模型自主决策攻击**

9月22日，ClosedQuorum是一种新型Windows恶意软件，利用Google Gemini、DeepSeek、Qwen和Mistral AI模型自主决定攻击后的入侵行动。该恶意软件基于Go语言编写，无需人类操作员命令即可运行，通过侦察信息和投票系统决定下一步行动，投票相同时由DeepSeek做最终决定，其次是Qwen、Mistral和Gemini。Cisco Talos研究人员称，这些模型仅限于一组预定义决策：窃取（LSASS凭证转储、浏览器凭证窃取、加密货币钱包提取）、注入（生成shellcode后使用进程空心化或Early Bird APC注入）、持久化（执行持久化模块）、横向移动（被列为可能决策，但所分析构建中无对应处理程序）。窃取信息通过Discord webhook传递给操作者，除传播外攻击可完全自动化。Talos称这是首个将C2决策委托给AI模型的Windows植入程序，可提升攻击速度与可扩展性并消除人为干预，但可能受速率限制或API不可用影响。该恶意软件尚不清楚是否属测试性质，但研究人员警告其代表“攻击链自动化架构的转变”。Cisco Talos表示未确认实际部署，但发现开发者与犯罪论坛上可追溯至2025年的盗刷信用卡帖子有关。所分析二进制文件含占位符API凭据和虚拟Discord webhook。

https://www.bleepingcomputer.com/news/security/new-closedquorum-windows-malware-uses-ai-for-attack-decisions/

**5. 微软联合执法打击EvilTokens钓鱼平台**

9月22日，微软数字犯罪部门联合Health-ISAC、执法部门及SpyCloud，对导致超10,000个组织、12,000多个微软账户遭入侵的EvilTokens钓鱼即服务平台实施基础设施拆除。该平台2月出现，是首个大规模支持设备代码认证并提供AI诱饵定制和收件箱筛选的服务。两名32岁和38岁男子在英国被捕，涉嫌为网站管理员，已获保释。微软追踪该威胁行为者为Storm-2992，称受影响行业包括批发分销、建筑、金融、房地产、高等教育和医疗保健。该服务滥用OAuth 2.0设备授权流程获取令牌，即使有MFA也可在无需窃取凭证下入侵账户。SpyCloud数据显示79个国家6,585个企业域中超8,708个账户遭入侵，97.5%为企业域。该服务通过Telegram推广，月费500美元或一次性1500美元，提供44个可定制钓鱼工具包。获得访问后，它使用Microsoft Graph映射组织关系并用AI分析邮箱，搜索电汇、发票和高管信函以生成BEC邮件，并通过多阶段重定向、PDF、HTML附件和虚假CAPTCHA逃避检测。微软通过法律授权查封相关基础设施，但威胁依然存在，关联方已创建APToken等克隆平台。防御建议包括在不需要时禁用设备代码认证、阻止设备代码流、核实验证应用、监控可疑登录并使用FIDO2安全密钥或通行密钥。

https://www.bleepingcomputer.com/news/security/eviltokens-phaas-disrupted-after-compromising-12-000-microsoft-accounts/

**6. CISA将Zyxel交换机漏洞列入KEV目录**

9月22日，美国网络安全和基础设施安全局（CISA）将Zyxel GS1900系列交换机的一个漏洞（编号CVE-2026-7273，CVSS评分8.8）添加到其已知利用漏洞（KEV）目录中。该漏洞是基于栈的缓冲区溢出，攻击者可利用其执行任意操作系统命令。安全公告称，Zyxel GS1900系列交换机固件的CGI程序中存在基于堆栈的缓冲区溢出漏洞，可能允许基于LAN的未经身份验证的攻击者通过精心构造的HTTP请求执行操作系统命令。该漏洞影响Zyxel GS1900交换机固件的CGI组件，本地网络上未经身份验证的攻击者可通过发送特制HTTP请求利用此漏洞，并有可能获得在设备上执行操作系统命令的权限。CISA未披露利用此漏洞发起的攻击技术细节，也未透露幕后黑手。CISA命令联邦机构在2026年9月24日之前修复该漏洞。

https://securityaffairs.com/199518/hacking/u-s-cisa-adds-zyxel-flaw-to-its-known-exploited-vulnerabilities-catalog.html

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