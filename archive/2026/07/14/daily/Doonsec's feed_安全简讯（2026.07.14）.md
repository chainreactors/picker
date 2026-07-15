---
title: 安全简讯（2026.07.14）
url: https://mp.weixin.qq.com/s/DSn2dbUAPUFy-b8r6n9RrQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:44:49.460622
---

# 安全简讯（2026.07.14）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309ZrxiaVfuVv06VXiaObGA8XfYwhGL4aJIFB3H8JsPtibBnsorHdkic8esJcUWCg81oqibcURwk9fUbbsq7NbwcN7W24Ddbe82CQeBH0rY/0?wx_fmt=jpeg)

# 安全简讯（2026.07.14）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. GitHub现200余诱饵库传播Windows恶意软件**

7月10日，供应链安全公司Socket披露，威胁行为者构建了由200多个GitHub代码库组成的网络，用于传播Windows恶意软件。这项名为“泥浆与负载行动”的活动涉及190个账户中的222个诱饵仓库，核心是一个伪装成DNS扫描工具（基于合法项目dnsub）的Go模块，旨在触发完整感染链。自2026年1月24日以来，攻击者已发布超1200个软件包版本，其中约700个为恶意版本。异常的发布频率源于攻击者利用GitHub Actions工作流反复生成带时间戳的提交以掩盖恶意本质。该模块包含的PowerShell命令在任何扫描逻辑前运行，利用大量空格隐藏自身，获取的脚本可绕过执行策略限制，再从公开投放点获取加密有效载荷，该载荷充当解析器、下载器、提取器和启动器，解密URL、检索受密码保护的压缩包并执行其中内容。攻击者使用Pastebin、YouTube、Telegram、Google Docs等多个公共平台托管镜像材料，提高攻击弹性。最终部署的有效载荷包括AsyncRAT、Quasar RAT、Remcos类远控木马、Vidar信息窃取程序，以及XMRig/BitMiner门罗币挖矿程序。

https://www.securityweek.com/network-of-200-github-repositories-used-for-malware-infection/

**2. Lidl第三方服务商遭攻击，多国客户数据泄露**

7月10日，折扣超市巨头Lidl近日向比利时、德国和荷兰的顾客发出通知，告知其个人信息因第三方服务提供商的IT安全事件而遭到泄露。受影响客户已收到电子邮件，警告他们警惕后续可能出现的网络钓鱼攻击。根据Lidl发送的邮件说明，一家未具名的第三方服务提供商遭遇安全入侵，导致一名身份不明的攻击者获取了Lidl在线商店的详细客户信息。泄露的数据字段包括姓名、电话号码、电子邮件地址、出生日期和客户编号。Lidl在通知中坦承：“目前，我们不能排除此次泄露涉及密码、账单地址、送货地址、银行账户信息或其他支付信息。”但公司同时强调，客户的在线账户本身未受到直接影响，即账户登录凭证和内部功能保持安全。事件发生后，Lidl表示该第三方服务提供商已立即响应，采取了必要措施全面恢复受影响的IT系统。同时，Lidl已向警方报案，并聘请外部安全专家对事件展开调查，以确定漏洞的根本原因和全部影响范围。比利时、德国和荷兰的数据保护监管机构均已获悉此事，Lidl正在配合相关部门的询问和要求。

https://cybernews.com/security/microsoft-ai-patch-tuesday-future-security-updates/

**3. 日本最大的出租车运营商遭受网络攻击**

7月13日，日本最大的出租车运营商日本交通公司近日证实，其内部系统在周末凌晨遭受网络攻击，导致包括出租车调度系统在内的多项核心服务瘫痪。该公司年收入约10亿美元，拥有超过1.8万名员工，运营着逾万辆出租车和专车。攻击发生后，公司紧急切断受感染系统以防止损害扩散，但汽车租赁、网上及电话预订、调度管理等多个内部系统至今仍未恢复。受此影响，东京、横滨、埼玉等主要城市的“分娩出租车”服务被迫暂停，给急需就医的孕妇带来极大不便；普通乘客则被建议改用“GO”叫车应用或前往路边站点候车。日本交通已聘请外部网络安全专家展开调查和系统修复，目前虽未确认发生数据泄露，但正评估该可能性，并承诺如有新进展将及时公告。同时，公司提醒客户警惕冒充官方的可疑邮件，避免打开附件或点击链接。截至报道发布，尚无勒索团伙宣称对事件负责。

https://www.bleepingcomputer.com/news/security/japans-largest-taxi-operator-shuts-systems-after-cyberattack/

**4. Jscrambler npm包遭篡改，近1500次下载**

7月13日，客户端网络安全公司Jscrambler近日披露，其官方npm包遭威胁行为者篡改，发布了包含信息窃取恶意软件的恶意版本，涉及8.14、8.16、8.17和8.20四个版本。这些恶意包在“预安装”钩子阶段即执行恶意代码，窃取开发者本地环境中的敏感数据。事件发生后的两小时内，恶意包被下载多达1479次，尽管Jscrambler迅速弃用问题版本并发布安全版本8.22，同时替换了受影响的四个依赖包，但影响范围已相当广泛。据应用安全公司Socket检测分析，该恶意软件利用ChaCha20-Poly1305加密算法对恶意代码进行高度混淆，大幅增加了逆向分析难度，其窃取目标涵盖源代码、项目文件、开发者凭证、主流云服务密钥、AI编码工具配置、加密货币钱包助记词、浏览器Cookie及保存的凭据，甚至包括Slack、Discord、Telegram等即时通讯应用数据，几乎覆盖了开发者工作环境中的所有关键信息。Jscrambler表示，此次入侵源于npm发布凭据泄露，公司已撤销相关凭证并在发布流程中增设额外安全控制措施。

https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/

**5. macOS恶意软件CrashStealer窃取凭证加密钱包**

7月13日，安全研究人员发现一款名为CrashStealer的新型macOS信息窃取恶意软件，伪装成苹果崩溃报告工具，通过经签名公证的投放器绕过Gatekeeper安全机制。启动后显示伪造密码提示，骗取用户输入以解锁钥匙串，进而窃取Safari登录信息、Wi-Fi密码、私钥及证书。同时瞄准80余款加密钱包扩展（如MetaMask、Phantom）和14款密码管理器（如1Password、Bitwarden），并扫描用户文档目录下的文件。窃取数据采用AES-256-GCM强加密，打包后上传至命令与控制服务器。该恶意软件5月被发现开发中，7月初已用于实际攻击。初始传播通过6月下旬注册的虚假软件网站分发，下载需输入PIN码，表明攻击具有针对性。CrashStealer具备重新签名能力，可动态改变哈希值以逃避检测。尽管与Atomic等家族目标重叠，其独特加密机制和原生C++实现使其独树一帜。安全公司Jamf已发布入侵指标报告，建议macOS用户仅从官方渠道下载软件，警惕异常密码提示。

https://www.bleepingcomputer.com/news/security/new-crashstealer-malware-poses-as-apple-crash-reporting-tool/

**6. 九国警告俄黑客利用路由器漏洞攻关键设施**

7月13日，美国、英国、澳大利亚、加拿大等九国的网络安全机构近日联合发布警告，指称俄罗斯联邦安全局第16中心的黑客组织正系统性地以存在漏洞和配置不当的路由器为跳板，渗透关键基础设施网络。该组织被追踪为Berserk Bear、Energetic Bear、Dragonfly等多个代号，其攻击手法主要是扫描公网IP地址段，寻找仍使用默认或常见SNMP（简单网络管理协议）团体字符串的路由器，随后利用伪造IP地址发送指令，复制设备配置文件并通过TFTP协议泄露至外部控制服务器。此外，FBI早在2025年8月便警告称，同一组织自2021年11月以来持续利用Cisco IOS和IOS XE软件智能安装功能中的高危漏洞CVE-2018-0171，对关键目标实施入侵。受威胁最严重的行业包括能源、通信、国防工业基地、医疗保健、金融服务及政府服务等。为应对这一持续威胁，联合咨询报告提供了详尽的缓解措施，包括升级至更安全的SNMPv3、禁用Cisco Smart Install功能、强制执行强密码策略、在边缘防火墙封堵TFTP和SNMP流量、及时更新固件并替换已停产的设备。

https://www.bleepingcomputer.com/news/security/us-and-allies-share-defense-tips-against-russian-hackers-targeting-critical-infrastructure/

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