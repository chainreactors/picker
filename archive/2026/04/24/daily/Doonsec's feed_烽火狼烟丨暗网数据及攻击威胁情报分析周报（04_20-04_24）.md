---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（04/20-04/24）
url: https://mp.weixin.qq.com/s/ayH-I3r42DMdfEK1m70e5w
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:33.781662
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（04/20-04/24）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mxwq2AF6zpN5tGAuO8FPvpV6HftDesZaSU6HJNeYl8xThUoibz1tRHoxePZNKuJUroc09BnBwo0qYRrSPbpSuehekm3DyNHsvMawm9JdcUuU/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（04/20-04/24）

盛邦安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件602起，同比上周减少31.4%。本周内贩卖数据总量共计254846.5万条；累计涉及8个主要地区及7种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpMp6ZNJJgQSicK58d3BXS7xia1Ma4lsd6BAatWoGv6j45xTXibM9KNGnAZfGEm17LM1gpJO6Fs01zDrM11JqKak6M9dQhnkWWxPCw/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及个人信息、医疗、服务等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpPFNcfnlyXXOQW8icoY32OQibYBicxKNNiaBN5ERcghxad1Rsnf8764HJ4A6jt2oO2ibKuf41InL7bJCLgO1DxpxLm0amm20RW6CO1E/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期的安全威胁主要来自漏洞攻击，尤其是与数据泄露、供应链攻击以及身份凭证滥用相关。本周内出现的安全漏洞其中以OASP.NET Core 权限提升漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP8821条，主要涉及命令注入、组件漏洞攻击等类型。

**01.**

**重点数据泄露事件**

**印度电信用户数据疑似泄露**

泄露时间：2026-04-22

泄露内容：攻击者在某暗网论坛出售一个据称包含印度电信运营商Reliance Jio Infocomm用户数据的数据库，该公司主要提供移动通信和数据服务。该数据集包含用户姓名、手机号码、性别、SIM卡激活地区及电子邮箱等信息。

泄露数据量：5300万

关联行业：通信

地区：印度

**巴西医疗机构数据疑似泄漏**

泄露时间：2026-04-20

泄露内容：攻击者在某暗网论坛发布信息称已入侵巴西医疗机构Instituto Maria Schmitt（IMAS），并出售相关数据。该机构是一家负责管理公立医院、诊所及医疗中心的医疗服务组织，数据集具体内容未被详细披露。

泄露数据量：未披露

关联行业：医疗

地区：巴西

**墨西哥州安全秘书处数据疑似泄露**

泄露时间：2026-04-20

泄露内容：攻击者在某暗网论坛出售一个包含墨西哥州安全秘书处（Secretaría de Seguridad del Estado de México）相关数据的数据库，该机构是负责墨西哥州公共安全及执法行动的政府部门，相关数据集包含该机构系统中的敏感信息。

泄露数据量：未披露

关联行业：政府

地区：墨西哥

**Analog Gold数据疑似泄露**

泄露时间：2026-04-19

泄露内容：攻击者在某暗网论坛发布信息称已获取Analog Gold相关数据，该平台是一个面向圭亚那（Guyana）用户的金融、支付及数字资产服务平台，数据集包含用户全名、电子邮件地址、电话号码、地址以及与帐户相关的标识信息等内容。

泄露数据量：16万

关联行业：金融

地区：圭亚那

**尼日利亚银行业特许协会数据疑似泄露**

泄露时间：2026-04-20

泄露内容：攻击者在某暗网论坛发布信息称已获取并上传The Chartered Institute of Bankers of Nigeria (CIBN)的数据库，该机构是尼日利亚银行专业人员的行业协会，负责银行业从业资格认证与行业标准，相关数据集包含数据库备份文件以及成员个人信息等内容。

泄露数据量：65万

关联行业：金融

地区：尼日利亚

**02.**

**热点资讯**

**Checkmarx开发工具链疑遭投毒**

近期，安全研究人员发现，Checkmarx旗下KICS相关Docker镜像及部分VS Code扩展版本疑遭供应链投毒，恶意代码可在扫描或扩展激活过程中收集并外传敏感信息。受影响内容包括被篡改的Docker标签以及1.17.0、1.19.0等版本扩展，窃取目标涉及GitHub令牌、云服务凭证、SSH密钥、环境变量及MCP配置等。攻击者还可能进一步利用被盗凭证创建恶意仓库、植入GitHub Actions工作流并污染npm包，显示该工具已具备从单点窃密向更广泛供应链扩散的特征。

消息来源：

https://thehackernews.com/2026/04/malicious-kics-docker-images-and-vs.html

**Anthropic封锁“Mythos”**

Anthropic虽未向公众开放高能力模型“Mythos”，但Claude相关AI能力实际上已嵌入Salesforce等企业SaaS环境。文章指出，Mythos在漏洞发现方面表现出极强能力，前沿AI一旦被滥用，可能显著压缩攻击者从发现漏洞到实施利用的时间窗口。与此同时，企业当前面临更现实的风险，是嵌入业务系统的AI功能正在扩大数据暴露、权限失控、影子AI和治理盲区等安全问题。

消息来源：

https://www.reco.ai/blog/anthropic-wont-let-you-run-mythos

**美破获勒索软件中间人串通黑客牟利案件**

近日，美国司法部披露，一名曾任勒索软件谈判员的佛州男子承认在2023年协助BlackCat组织攻击多家美国企业。调查显示，其在为受害者提供谈判服务期间，暗中向黑客泄露客户保险额度、谈判策略等敏感信息，帮助对方抬高赎金金额，并从中获利。案件中有一家受害企业被勒索约120万美元比特币，当局已查扣其价值约1000万美元的资产。

消息来源：

https://thehackernews.com/2026/04/ransomware-negotiator-pleads-guilty-to.html

**Harvester 组织新增 Linux 平台 GoGra 后门攻击**

威胁组织 Harvester 被检测到使用全新 Linux 版本 GoGra 后门开展针对南亚地区的网络间谍攻击活动。该组织此前便长期针对南亚政府、电信、媒体等领域实施窃密攻击，此次将原有 GoGra 后门拓展适配 Linux 系统，依旧沿用微软 Graph API、Outlook 邮箱作为隐蔽 C2 通信通道，借助合法云服务绕过边界防护。攻击者通过社会工程学诱导用户打开伪装成 PDF 的恶意 ELF 文件实现植入，后门通过指定邮箱收发指令、执行系统命令并回传窃取数据，事后清除痕迹隐匿攻击行为。跨平台版本的更新、相同的硬编码特征均证实为同一攻击者开发，体现该组织持续扩充攻击工具链、扩大攻击目标范围的活动趋势。

消息来源：

https://thehackernews.com/2026/04/harvester-deploys-linux-gogra-backdoor.html

**账号凭证窃取类入侵风险日益凸显**

当前企业面临的高频入侵风险，已不再局限于漏洞利用，而是越来越多地来自失窃账号和密码被直接用于登录系统。攻击者通常通过撞库、密码喷洒及钓鱼邮件获取有效凭证，以近乎合法的身份进入企业网络，从而绕过传统边界防护和常规检测机制。完成初始访问后，其往往会进一步窃取更多凭证、实施横向移动，并逐步扩大战果，最终演变为勒索攻击、数据泄露或长期潜伏。随着AI提升钓鱼内容生成和凭证测试效率，身份攻击的规模化与隐蔽性正持续增强。

消息来源：

https://thehackernews.com/2026/04/no-exploit-needed-how-attackers-walk.html

**03.**

**热点技术**

**新型AirSnitch攻击可绕过企业WiFi加密防护**

近日，名为 AirSnitch 的新型攻击技术被披露，指出企业长期依赖的 WiFi 加密和客户端隔离机制并非绝对安全。研究显示，该攻击利用协议与基础设施交互中的细微缺陷，可削弱 WPA2 和 WPA3 Enterprise 提供的安全保障，影响多家主流厂商设备及 Android、iOS、macOS、Windows、Ubuntu 等操作系统。文章提醒企业重新评估无线网络防护能力，防范加密失效带来的横向渗透风险。

消息来源：

https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/

**开源软件供应链投毒与凭证窃取风险加剧**

CanisterSprawl开源供应链被检测到蠕虫攻击活动，攻击者利用被盗 npm 开发令牌，通过恶意软件包安装钩子窃取开发者主机各类密钥、云凭证、浏览器凭据等信息，并跨 npm、PyPI 生态持续上传恶意包扩散攻击；同时近期开源社区还曝出多起供应链攻击事件，包括仿冒 K8s 工具搭建各类代理并滥用大模型 API 网关窃取密钥、仿冒企业发布恶意 npm 包窃取凭证、攻击者借助 GitHub Actions 漏洞批量窃取仓库凭据并试图投毒开源包，整体开源软件供应链投毒、凭证窃取与跨生态扩散风险持续高发。

消息来源：

https://thehackernews.com/2026/04/self-propagating-supply-chain-worm.html

**新型 Mirai 攻击利用 D-Link 路由器漏洞大规模入侵设备**

安全团队监测到新型 Mirai 衍生恶意软件攻击活动，攻击者利用CVE-2025-29635（D-Link DIR-823X 路由器高危命令注入漏洞）发起真实在野攻击，通过构造恶意 POST 请求实现远程代码执行，下载并植入 tuxnokill 恶意程序构建僵尸网络，发动各类 DDoS 攻击。同时攻击者还联合利用多款老旧路由器漏洞开展规模化入侵，而涉事 D-Link 设备已终止产品生命周期，基本无法获得官方补丁修复，风险长期存在，厂商建议用户更换新型设备、关闭远程管理、修改默认密码以防范风险。

消息来源：

https://www.bleepingcomputer.com/news/security/new-mirai-campaign-exploits-rce-flaw-in-eol-d-link-routers/

**UNC6692 组织滥用 Microsoft Teams 钓鱼**

威胁组织UNC6692，依托 Microsoft Teams 开展社交工程钓鱼攻击。攻击者先对目标邮箱发送大量垃圾邮件制造紧急场景，随后冒充企业 IT 运维人员通过 Teams 联系受害者，诱导点击钓鱼链接下载恶意脚本，在设备上部署包含 SNOWBELT、SNOWGLAZE、SNOWBASIN 在内的模块化恶意软件套件，实现浏览器植入后门、内网隧道通信、系统持久化控制。攻击者后续通过端口扫描、权限提升、哈希传递等方式开展内网横向移动，窃取域内敏感数据，并大量利用 AWS 云存储托管恶意文件以绕过常规防护检测。该攻击手法源自已停运的 Black Basta 组织，且近期同类 Teams 仿冒客服钓鱼攻击频发，协作平台已成为主要高危攻击入口。

消息来源：

https://thehackernews.com/2026/04/unc6692-impersonates-it-helpdesk-via.html

**新型 NGate 恶意软件依托正规应用开展支付信息窃取攻击**

研究人员发现 NGate 恶意软件家族全新变种，攻击者不再使用此前的 NFCGate 工具，转而篡改具备 NFC 数据传输功能的正规安卓应用HandyPay，植入疑似 AI 生成的恶意代码。该恶意程序主要针对巴西安卓用户，通过虚假彩票网站、仿冒谷歌 Play 页面进行分发，可窃取用户银行卡 NFC 数据与支付 PIN 码并回传至控制服务器，实现非接触盗刷、ATM 取款等恶意行为。攻击者选用该正规应用意在降低使用成本、提升隐蔽性，本次攻击活动自 2025 年 11 月起持续活跃，恶意版本并未上架官方应用商店，同时也反映出 AI 工具降低了网络攻击门槛、NFC 支付领域安全风险持续加剧。

消息来源：

https://www.welivesecurity.com/en/eset-research/new-ngate-variant-hides-in-a-trojanized-nfc-payment-app/

**04.**

**热点漏洞**

**Qibo CMS服务端请求伪造漏洞（CVE-2026-6649）**

Qibo CMS是一款内容管理系统，提供网站内容发布与管理等功能。Qibo CMS 1.0存在服务端请求伪造漏洞，该漏洞产生的原因是/index/image/headers接口对参数starts缺乏有效校验，攻击者可利用该漏洞通过远程构造恶意请求诱导服务器向任意地址发起请求，从而实现对内网资源的探测或访问。

影响版本：

Qibo CMS == 2.1.1

**ASP.NET Core 权限提升漏洞（CVE-2026-40372）**

ASP.NET Core 是一个用于构建现代云端应用的跨平台开发框架。ASP.NET Core 存在权限提升漏洞。攻击者可能利用该漏洞在特定条件下提升权限，从而对系统造成潜在安全风险。

影响版本：

10.0<ASP.NET<10.0.7

**rowboat认证绕过漏洞（CVE-2026-6635）**

rowboatlabs rowboat是一款提供工具调用与Webhook集成功能的应用程序。rowboatlabs rowboat 0.1.67及之前版本存在认证绕过漏洞，该漏洞产生的原因是tools\_webhook组件中apps/experimental/tools\_webhook/app.py文件的tool\_call函数对请求头X-Tools-JWE未进行有效校验，攻击者可通过远程构造恶意请求绕过认证机制，从而利用该漏洞未授权调用接口或访问敏感功能。

影响版本：

rowboatlabs rowboat <= 0.1.67

**MetaCRM SQL注入漏洞（CVE-2026-6629）**

MetaCRM是一款由美特软件开发的客户关系管理WEB应用系统。MetaCRM 6.4.0及之前版本存在SQL注入漏洞，该漏洞产生的原因是接口组件中sql.jsp文件的Statement.executeUpdate函数对参数sql未进行有效过滤，攻击者可利用该漏洞通过远程构造恶意SQL语句执行非预期的数据库操作，从而获取敏感数据或篡改数据库内容。

影响版本：

MetaCRM<=6.4.0

**Yifang CMS跨站脚本漏洞（CVE-2026-6633）**

Yifang CMS是一款用于网站内容管理和后台扩展管理的WEB应用系统。

Yifang CMS 2.0.5及之前版本存在跨站脚本漏洞，该漏洞产生的原因是扩展管理模块中plugins/yifang\_backend\_account/logic/admin/L\_rbac\_admin.php文件的store函数对参数Account未进行有效过滤，攻击者可利用该漏洞通过远程构造恶意脚本在受害者浏览器中执行，从而窃取用户敏感信息或实施钓鱼攻击。

影响版本：

Yifang CMS <=2.0.5

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpMhH9Q0I5NzyfeiczPrYZwsiaUPBeo0j6UELaYBChia1iajibN0pFw1icGr2hjibyMM2kVz5cryicQ431iadicJP699463G1CnBot7DhxzMs/640?wx_fmt=png&from=appmsg)

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