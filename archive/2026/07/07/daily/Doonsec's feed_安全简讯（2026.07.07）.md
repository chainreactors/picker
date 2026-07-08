---
title: 安全简讯（2026.07.07）
url: https://mp.weixin.qq.com/s/HO1XLgDqdDBR2b-Rhe2pFg
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:03:34.926616
---

# 安全简讯（2026.07.07）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZrznC1gkVSrrdXM554sUezfVA8bcImP0IPkQAv1DsG9PSJcq61hsffvO6QeGIWfYAAMJ5ictZ24VPibKoT2Y3CD3gKXTc5iaPPaePA/0?wx_fmt=jpeg)

# 安全简讯（2026.07.07）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. PamStealer恶意软件伪装Mac组件盗取密码**

7月3日，安全研究人员发现，不法分子通过仿冒域名maccyapp(.)com推广伪造的开源剪贴板管理器Maccy，实际安装的是名为PamStealer的Rust语言信息窃取程序。攻击始于一个包含恶意AppleScript脚本的磁盘映像，用户被诱导在脚本编辑器中运行，恶意逻辑隐藏在长段空白文本之后。脚本会检查CPU架构、语言、时区等环境信息，并对俄罗斯等国家进行区域过滤以规避特定地区的感染。随后，下载器使用原生API检索第二阶段有效载荷，避免使用curl等常见命令行工具以降低检测风险。最终安装的恶意程序伪装成macOS系统组件（如"Finder.app"），复制真实图标，运行时无窗口显示。该窃取程序可读取浏览器数据库、访问钥匙串、持续监控剪贴板，所有数据经加密后发送至命令与控制服务器。该恶意软件通过高度仿真的系统对话框诱骗用户输入密码，并利用PAM模块验证密码有效性，仅当输入正确密码后才继续执行，随后显示虚假错误消息掩盖恶意行为。它还会诱导用户授予"完全磁盘访问权限"以窃取邮件和备份等受保护数据，并通过双重注册登录项实现持久化。

https://hackread.com/pamstealer-malware-macos-fake-maccy-clipboard-app/

**2. 社交工程攻破承包商，AdaptHealth患者数据泄露**

7月4日，美国医疗设备公司AdaptHealth近日披露，威胁行为者通过社交工程攻击成功欺骗第三方承包商，获取了该公司云环境的访问权限并窃取了大量患者数据。据提交给美国证券交易委员会（SEC）的文件显示，攻击者利用社会工程手段破坏了与第三方承包商相关的合法用户会话，从而绕过安全边界进入AdaptHealth的多个基于云的业务应用程序。发现问题后，AdaptHealth迅速采取应对措施，包括禁用受影响的账户、重置所有相关凭据，并部署了额外的访问控制机制以遏制事件进一步扩大。该公司于6月27日正式认定该事件具有重大意义，依据监管要求向SEC进行披露。在入侵过程中，攻击者成功渗透了内部患者管理系统和文档存储平台，窃取了与保险结算相关的密码等关键数据，同时获取了患者的个人身份信息（PII）和受保护的健康信息（PHI）。不过AdaptHealth在文件中特别澄清，其系统并不存储患者的社会保障号码、个人财务账户信息或支付卡信息，这在一定程度上限制了数据泄露可能造成的财务损害。

https://cybernews.com/news/adapthealth-patient-data-theft/

**3. 冒名招聘设局，连环跳转钓鱼窃谷歌账密**

7月6日，近期，攻击者冒充Adobe、Netflix、可口可乐、OpenAI等30余个知名品牌，以虚假招聘面试为诱饵，针对营销专业人士窃取Google账户凭证。该攻击并非简单发送恶意链接，而是通过多重跳转的“信任链”，利用合法平台降低受害者防备，最终引入伪造登录页面。钓鱼邮件伪装成“市场营销岗位招聘”，发件人信息取自真实招聘人员。邮件引导收件人点击日历链接后，经Salesforce域名和Wise Agent等多级跳转，才进入钓鱼页面，普通用户难以察觉异常。抵达后，攻击者采用“浏览器中的浏览器”（BitB）技术，用HTML和CSS渲染伪造的Google登录弹窗，骗取用户账号密码，且不触发危险域名请求。该活动已持续至少五个月，涉及34个以上域名，被冒充行业涵盖航空、食品、奢侈品、咨询、酒店、体育等众多领域。攻击者如何获得合法平台权限尚不明确，推测为注册真实账户或使用被盗凭证，平台本身未被攻破，而是被滥用为“中转站”。

https://www.bleepingcomputer.com/news/security/phishing-poses-as-big-brand-job-interview-to-steal-google-accounts/

**4. Adobe ColdFusion高危漏洞遭火速利用**

7月6日，近日，Adobe公司发布紧急安全警告，其ColdFusion产品中存在一个最高级别漏洞CVE-2026-48282。该漏洞属于路径遍历问题，未经身份验证的远程攻击者可利用其执行任意代码，受影响的版本包括ColdFusion 2025.9、2023.20及更早版本。Adobe明确警告称，该漏洞极易被利用，且极有可能在现实攻击中被广泛采用。安全研究机构的警告很快成为现实，在CVE-2026-48282的详细技术信息公开后不到两个小时，已有攻击者开始实际利用该漏洞发起攻击。监测数据显示，这些早期攻击源自位于印度的攻击者。如此迅速的武器化过程，凸显了高危漏洞在当今威胁环境下面临的严峻挑战，攻击者紧盯安全社区和厂商发布的技术细节，一旦公开即可在极短时间内转化为攻击武器。针对此次曝光的CVE-2026-48282，Adobe已发布相应的安全更新补丁。使用Adobe ColdFusion的组织被敦促尽快安装最新更新，以保护自身系统免受正在进行的攻击活动的侵害。

https://securityaffairs.com/194837/hacking/adobe-coldfusion-flaw-cve-2026-48282-now-exploited-in-the-wild.html

**5. APT组织Armored Likho锁定政府和电力机构**

7月6日，卡巴斯基披露，新APT组织Armored Likho正攻击俄罗斯、巴西、哈萨克斯坦等国政府与电力机构，兼具经济犯罪和间谍目的。其恶意工具以BusySnake Stealer和Go2Tunnel为主，可隐蔽控制主机、窃取凭证并按需部署模块。初始入侵依靠鱼叉钓鱼邮件，通过可执行文件或LNK文件植入恶意载荷，后台下载Python环境和窃密程序。BusySnake采用动态加解密、无窗口运行等规避技术，功能涵盖剪贴板窃取、文件枚举、截图、密码Cookie提取、OTP窃取、加密货币钱包查找、Telegram凭据收集及反向SSH隧道建立。该组织已将Go2Tunnel的隧道功能整合进窃密器，实现持久远程控制。其活动与Eagle Werewolf组织存在重叠，后者使用的AquilaRAT在结构和持久化上与BusySnake相似。相关机构应加强邮件防护，监控异常Python进程和GitHub流量，并更新终端响应策略。

https://www.securityweek.com/armored-likho-apt-targeting-government-electric-power-entities/

**6. 冒充IT打Teams电话，EtherRAT渗透企业内网**

7月6日，Unit 42披露，攻击者通过Microsoft Teams语音冒充IT支持，诱骗员工安装EtherRAT，获取企业网络初始访问权。攻击始于一封“员工调查”钓鱼邮件，受害者打开后不久便接到外部Teams通话，对方自称“系统管理员”。攻击者利用屏幕共享功能诱导安装HopToDesk或AnyDesk等合法远程工具，随后从恶意域名下载MSI加载器，启动Node.js编写的EtherRAT。该木马支持命令执行、文件操作、数据窃取，其C2地址通过以太坊智能合约检索，传统封堵手段难以奏效。Unit 42在分发服务器发现v1至v9多个版本，表明攻击持续迭代。此前同类攻击已针对金融、医疗机构，微软也于四月警告外部Teams滥用趋势上升。为应对威胁，微软新增外部来电警告标识和第三方机器人会议大厅策略。专家建议加强员工安全意识培训，限制外部Teams联系权限，并监控异常远程桌面行为，相关入侵指标已在GitHub公开。

https://www.bleepingcomputer.com/news/security/fake-it-support-calls-on-microsoft-teams-push-etherrat-malware/

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