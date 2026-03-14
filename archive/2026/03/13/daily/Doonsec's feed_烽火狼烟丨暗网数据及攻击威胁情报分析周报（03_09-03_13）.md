---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/09-03/13）
url: https://mp.weixin.qq.com/s/UwgtrCmFNzkeO22sOghT6Q
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:08:58.230712
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/09-03/13）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mxwq2AF6zpMyxqSneXXdbzKsbwGj9nTL7W7G6AOCdfw0dXqNEdWuqFAMSgAdS2yUSs1vELNZ8Lblrpadsmf6BMKNcpzv2MXJzca8jWOEZps/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/09-03/13）

盛邦安全应急响应中心

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件745起，同比上周增加112.86%。本周内贩卖数据总量共计279876.9万条；累计涉及8个主要地区及6种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpM8YXicGKlvuLJN99m77GtG3OD9fyIuHcFWslxoPUqSR9V08mKKrbTqNKibEoUYcwvicWC6VEaIW9VZZtxmnFnia8mAFWnXS2FfDFI/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及金融、个人信息、贸易等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpPevsXjZ9geq5fmtL2CmChkspkXjiaD0e2Qm9ibObyxyUNpmIol1ZqHIrhgcyqI66SR4tCrQ5ZTHN2CWicmJ09G4YYOBFARsvq0QU/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期主要威胁来自恶意软件、AI攻击及恶意插件，需加强关注；本周内出现的安全漏洞以OpenEMR AJAX图形库SQL注入漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP7079条，主要涉及扫描探测、组件漏洞攻击等类型。

**01.**

**重点数据泄露事件**

**加拿大公民数据泄露**

泄露时间：2026-03-09

泄露内容：黑客出售据称与加拿大公民相关的650 万条“线索”数据集。这些数据据称是从广告活动中收集的，包含客户姓名、电话号码、手机号码、电子邮件地址和国家/地区等字段。

泄露数据量：650万

关联行业：服务

地区：加拿大

**Canva用户账户泄露**

泄露时间：2026-03-09

泄露内容：黑客声称泄露了15.5万个Canva.com账户。Canva是一个全球知名的在线设计平台和图形设计工具，主要用于制作海报、PPT、社交媒体图片、Logo、视频等视觉内容。据称，泄露的数据集为CSV文件，包含用户名、密码、用户代理、日期、上次登录时间、国家/地区和电话号码等字段。

泄露数据量：15.5万

关联行业：互联网

地区：澳大利亚

**Rapikom数据泄露**

泄露时间：2026-03-09

泄露内容：攻击者声称泄露了与RAPIKOM VENEZUELA相关的免费数据库。Rapikom是一家来自委内瑞拉的金融科技公司，通过移动应用提供“先买后付”的分期消费服务。该数据集包含与5000家公司相关的记录，涉及联系方式、计划信息、购买和付款参考信息等业务字段，以及一个名为“usr\_clave”的密码字段。据攻击者称，该数据集还包含每家公司的银行账户信息和精确位置数据（纬度和经度）。

泄露数据量：未涉及

关联行业：金融

地区：委内瑞拉

**FNATH数据泄露**

泄露时间：2026-03-09

泄露内容：黑客声称正在出售与FNATH.org相关的数据库和文件。FNATH.org是一个旨在支持受事故、职业病、疾病和残疾影响的个人的协会。泄露的数据集包含一个名为“fnath\_clean.json”的数据库文件，内含4.5万条记录。

泄露数据量：4.5万

关联行业：服务

地区：法国

**AT&T数据泄露**

泄露时间：2026-03-09

泄露内容：黑客声称正在出售一个AT&T数据集，其中包含7348.1万行数据。AT&T是一家跨国通信与媒体公司，主要提供移动通信、宽带互联网、企业网络服务和数字通信解决方案。该数据集被拆分为两个文件，内含社会安全号码（SSN）和出生日期（DOB）等敏感字段。

泄露数据量：未涉及

关联行业：通信

地区：美国

**02.**

**热点资讯**

**病毒式传播的GitHub项目声称WiFi可“透视墙壁”**

近期，GitHub上一个名为WiFi-DensePose的开源项目声称可利用普通WiFi信号分析墙后人体的活动，通过分析信号传播和反射的细微变化，结合信号处理与人工智能模型，将无线信号转换为类似人体骨架的数字模型，从而推测人体姿态、移动轨迹及呼吸等微小动作，无需摄像头或可穿戴设备。不过，开发者和安全研究人员对其实际能力表示怀疑，认为它更接近概念验证，距离现实应用仍有较大差距；尽管该技术引发了隐私担忧，专家指出利用无线信号感知人体活动的研究已在学术界存在多年，但在真实环境中实现稳定、精确的“穿墙感知”仍需更复杂的硬件和算法支持。

消息来源：

https://cybernews.com/security/viral-github-project-wifi-see-through-walls/

**恶意广告利用Meta平台传播全球投资诈骗**

一个大规模的恶意广告投资诈骗网络利用Meta旗下社交平台传播虚假投资项目，全球范围内共发现310个协同诈骗活动，涉及2.6万条以上恶意广告，覆盖25个国家和15种以上语言。这些广告伪装成新闻报道或金融投资机会，假冒BBC、英格兰银行等知名机构诱导用户点击，随后将用户重定向至伪造的新闻页面或投资平台注册页面，窃取姓名、电话、邮箱等个人信息。之后，诈骗团伙以“投资顾问”身份联系受害者，诱导其向虚假账户存入资金，并通过伪造的交易面板展示“盈利”以诱骗追加投资，但资金几乎无法提现。安全专家提醒用户对社交媒体上的“高收益投资广告”保持警惕，避免通过广告链接进入投资平台，并通过官方渠道核实平台真实性以防资金损失。

消息来源：

https://cybernews.com/security/malvertising-investment-scam-meta-platform/

**AI攻击代理两小时攻破麦肯锡内部聊天机器人**

安全公司进行的一项实验表明，一个AI自动攻击代理能在无凭证、无内部信息、无人工干预的情况下，仅凭公开信息在约两小时内成功入侵McKinsey&Company的内部AI聊天系统Lilli。该代理获得了系统的完全读写权限，访问到约4650万条聊天记录、72.8万个文件、5.7万个用户账户和95个系统提示。研究人员指出，可被修改的系统提示和公开暴露的API接口是导致入侵的关键弱点，攻击者不仅可窃取敏感数据，还能篡改AI生成建议影响企业决策。专家表示，该实验显示AI驱动的自动化攻击正成为新的网络安全威胁，企业需加强对AI系统、API接口和提示词安全的保护。

消息来源：

https://cybernews.com/security/ai-agent-cracked-mckinsey-chatbot/

**Chrome插件因所有权转移导致恶意软件传播**

安全研究人员警告称，一些原本合法的Chrome浏览器插件在更换所有者后被恶意利用，形成浏览器插件供应链攻击。例如，一款名为QuickLens的插件在开发者变更后推送了恶意更新，其能够绕过浏览器安全机制，在用户访问的网站中注入隐藏脚本，以窃取会话令牌、执行远程命令并下载更多恶意程序。由于浏览器插件通常自动更新，一次恶意更新就可能影响成千上万的用户。专家指出这类攻击利用用户对已安装插件的信任，在积累一定用户后可能被出售给恶意行为者，从而推送恶意更新。建议用户定期检查浏览器扩展，仅保留必要插件，并对权限过高或来源不明的扩展保持警惕。

消息来源：

https://cybernews.com/security/chrome-extension-ownership-transfer-malware/

**伪造简历攻击瞄准企业HR部门**

安全研究人员发现一项针对企业人力资源部门的网络攻击活动，攻击者通过发送看似正常的求职简历或申请链接，诱导招聘人员下载并打开恶意ISO镜像文件，从而在企业网络中部署恶意软件。该恶意程序的主要目标是关闭或绕过杀毒软件和EDR（端点检测与响应）系统等安全防护机制，一旦防护被禁用，攻击者即可进一步窃取数据、安装后门或发动后续攻击。研究人员指出，招聘流程中频繁处理陌生人附件和链接的特性使HR成为理想目标，建议企业加强对招聘邮箱和附件的安全扫描，并提醒HR人员谨慎处理未知来源文件以降低风险。

消息来源：

https://cybernews.com/security/fake-resumes-target-hr-departments/

**03.**

**热点技术**

**利用Microsoft Teams社工攻击传播恶意软件**

近期攻击者冒充企业IT支持人员，通过Microsoft Teams发送社交工程消息，诱导员工授予远程访问权限，进而传播名为A0Backdoor的隐蔽恶意软件。获得访问权限后，攻击者利用远程支持工具（如Quick Assist）投放伪装成Teams更新的恶意MSI安装包（如“Update.msi”），并利用DLL侧加载技术，在系统目录中放置合法微软签名程序搭配恶意hostfxr.dll文件，以解密并加载隐藏恶意程序。安全专家建议企业加强对协作平台的安全监控，提高员工对社交工程攻击的警惕，并限制远程支持工具的使用，以减少此类攻击带来的风险。

消息来源：

https://www.esecurityplanet.com/threats/teams-social-engineering-campaign-drops-a0backdoor-malware/

**伪造Claude Code安装页面传播信息窃取软件**

近期攻击者通过克隆官方网站创建伪造的Claude Code安装页面，并利用搜索引擎广告推广，诱导开发者复制执行被篡改的终端命令。该命令实际会从攻击者服务器下载并运行恶意脚本，进而部署信息窃取木马，用于收集浏览器数据、会话令牌和系统信息等敏感信息，并将其发送至攻击者控制的服务器。此攻击主要针对Windows和macOS系统，特别瞄准开发者和AI编程工具用户，利用其对官方安装流程的信任实施窃密活动。

消息来源：

https://www.esecurityplanet.com/artificial-intelligence/fake-claude-code-install-pages-spread-infostealer-malware/

**恶意Chrome插件针对imToken钱包用户窃取加密资产**

一款伪装成颜色可视化工具的恶意Chrome浏览器插件正针对imToken加密钱包用户发动攻击。安装后，该插件会打开伪装成钱包导入界面的钓鱼页面，诱导用户输入助记词或私钥；一旦用户提交，攻击者即可立即控制钱包并转移加密资产。imToken作为非托管钱包，官方并未推出Chrome扩展，因此任何声称相关的浏览器插件均属恶意。安全专家提醒用户避免安装来源不明的插件，并通过官方渠道访问钱包服务以防资产被盗。

消息来源：

https://www.esecurityplanet.com/threats/malicious-chrome-extension-targets-imtoken-wallet-users/

**伪造CleanMyMac网站在macOS上传播SHub窃密木马**

近期攻击者通过伪造的CleanMyMac下载网站（如cleanmymacos[.]org）诱导macOS用户在终端中执行安装命令，从而传播信息窃取恶意软件SHub Stealer。该攻击利用社会工程手段让用户主动运行恶意脚本，因此可绕过Gatekeeper、应用签名验证和XProtect等macOS安全机制。一旦安装，SHub Stealer会窃取浏览器密码、Apple Keychain内容、Telegram会话、iCloud数据和加密货币钱包信息等敏感数据，并发送至攻击者控制的服务器；部分样本还会替换加密钱包应用或建立持久后门以实现持续控制。安全专家提醒，正常软件不会要求用户在终端中粘贴命令，用户应仅通过官方渠道或应用商店下载软件以避免感染。

消息来源：

https://www.esecurityplanet.com/threats/cleanmymac-imposter-site-installs-shub-stealer-on-macs/

**伪造OpenClaw npm软件包传播GhostClaw恶意软件**

一个名为@openclaw-ai/openclawai的恶意npm软件包伪装成OpenClaw安装工具，针对开发者传播GhostClaw恶意软件。该包在安装时通过postinstall脚本自动执行隐藏代码，并将自身安装到系统全局路径以实现长期驻留；运行时会显示伪造的安装界面以降低用户警惕，同时在后台从攻击者服务器下载并解密第二阶段载荷，悄悄窃取浏览器凭据、SSH私钥、加密货币钱包、开发者令牌及AWS、Azure、GCP等云平台凭证，并发送至攻击者控制的服务器。此类攻击属于开源软件供应链攻击，利用开发者对开源工具的信任传播恶意代码，安全专家建议安装npm包前仔细检查来源并使用安全扫描工具检测依赖。

消息来源：

https://www.esecurityplanet.com/threats/fake-openclaw-npm-package-installs-ghostclaw-malware/

**04.**

**热点漏洞**

**sigstore-ruby验证绕过漏洞（CVE-2026-31830）**

sigstore-ruby是一款纯Ruby实现的sigstore验证工具，提供对cosign项目验证命令的支持，用于检查软件工件的签名和完整性。sigstore-ruby存在验证绕过漏洞。该漏洞产生的原因是Sigstore::Verifier#verify在artifact摘要与in-toto证明主体摘要不匹配时未能正确传播验证失败状态。攻击者可利用该漏洞，在未授权状态下使用包含in-toto语句的DSSE捆绑包绕过验证，导致无效工件被标记为验证成功。

影响版本：

sigstore-ruby<0.2.3

**Flowise HTTP节点服务器端请求伪造漏洞（CVE-2026-31829）**

Flowise是一款用于构建自定义大语言模型流程的拖拽式用户界面工具，提供AgentFlow和Chatflow中的HTTP节点功能。Flowise存在HTTP节点服务器端请求伪造漏洞。该漏洞产生的原因是HTTP节点未对用户控制的URL目标进行有效限制。攻击者可利用该漏洞，通过已认证低权限用户身份与公开的chatflow交互，迫使Flowise服务器向内部网络资源发起请求，从而获取无法从公网访问的敏感信息。

影响版本：

Flowise<3.0.13

**Alienbin TTL索引滥用拒绝服务漏洞（CVE-2026-31827）**

Alienbin是一款匿名代码和文本分享Web服务，提供帖子保存和时效设置功能。Alienbin存在TTL索引滥用拒绝服务漏洞。该漏洞产生的原因是/save端点在每次提交新帖子时都会重新创建整个post集合的TTL（生存时间）索引。攻击者可利用该漏洞，通过已认证用户身份反复提交短TTL的帖子导致索引过期时间被覆盖，从而使所有现有帖子被提前删除。

影响版本：

Alienbin<=1.0.0

**pypdf内存耗尽拒绝服务漏洞（CVE-2026-31826）**

pypdf是一款免费开源的纯Python PDF库，提供PDF文档解析、内容处理和文件生成功能。pypdf存在内存耗尽拒绝服务漏洞。该漏洞产生的原因是程序在解析内容流时未能对/Length值进行有效校验。攻击者可利用该漏洞，通过诱导用户打开特制PDF文件触发大量内存分配，从而导致应用程序崩溃。

影响版本：

pypdf<6.8.0

**OpenEMR AJAX图形库SQL注入漏洞（CVE-2026-32127）**

OpenEMR是一款免费开源的电子健康记录和医疗实践管理应用，提供患者管理、医疗记录和图形数据展示功能。OpenEMR存在AJAX图形库SQL注入漏洞。该漏洞产生的原因是图形库未能对用户输入进行有效验证。攻击者可利用该漏洞通过已认证用户身份注入恶意SQL代码，从而获取或篡改数据库中的敏感信息。

影响版本：

OpenEMR<8.0.0.1

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpNJibPR0GicibGuZibZWVA9SuH7qsrHPnsN8RpxS904nTk9ic1w0NOb9IHhPWoTe9zkulibSWWdVPDZibViaiaWS26rETIRN8TbBzsEKLNU/640?wx_fmt=png&from=appmsg)

*请注意：以上均为监测到的情报数据，盛邦安全不做真实性判断与检测*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNiabToHw1T09Myv7Q/0?wx_fmt=png)

盛邦安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNiabToHw1T09Myv7Q/0?wx_fmt=png)

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