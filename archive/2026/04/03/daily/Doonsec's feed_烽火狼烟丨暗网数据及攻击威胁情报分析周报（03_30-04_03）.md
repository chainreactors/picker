---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/30-04/03）
url: https://mp.weixin.qq.com/s/yXaDnsslTpvpu_7grOzYVQ
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:14:43.488914
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/30-04/03）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mxwq2AF6zpOnmntotqDtcbicSmVRT1So4XshDmbbOYhDVNMzUc82jNO8jtPAAAavpAXp2GCwbaFeCdN5kqX1jDKDJpNAzqLwSTakJoJ7lhK8/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/30-04/03）

盛邦安全应急响应中心

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件676起，同比上周增加35.74%。本周内贩卖数据总量共计894055.8万条；累计涉及8个主要地区及8种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpMKic7XPxwcqS6UIgN4vPAzYK0qiazE4eSiaOMMFYMPS184PwuibHibotluZy4Txs6iaLR8p4WxGgYKgia2J5LjKWkC5EUG9vttcwcvSM/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及个人信息、金融、政府等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpNJ3g2JNDGVMXxwq2fNqtdpEibkpoMRgiaYicWXA0X36FR8kA4BLcia1r5npVdkHurOu2iaFTSqg3FjXxkk2zHhgUCVYibCuGMGKgvxI/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期主要威胁来自钓鱼攻击、恶意软件及供应链攻击，需加强关注；本周内出现的安全漏洞以SciTokens SQL注入漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP7774条，主要涉及命令注入、组件漏洞攻击等类型。

**01.**

**重点数据泄露事件**

**摩萨德数据库泄露**

泄露时间：2026-03-30

泄露内容：攻击者在暗网论坛上声称出于政治动机泄露了摩萨德的相关信息。摩萨德（Mossad）是以色列的情报机构。据称该数据集包含高度敏感的个人数据，可用于人肉搜索、身份冒用以及有针对性的社会工程攻击。

泄露数据量：未涉及

关联行业：政府

地区：以色列

**Nakamura.co.id数据库泄露**

泄露时间：2026-03-30

泄露内容：攻击者在暗网论坛上售卖一个与nakamura.co.id关联的大型数据库列表。nakamura.co.id是印度尼西亚一家美容与健康连锁机构。该列表声称拥有超过85万名会员，数据集大小超过17GB，其包含庞大的客户或会员记录集。

泄露数据量：17GB

关联行业：医疗

地区：印度尼西亚

**Odido数据泄露**

泄露时间：2026-03-31

泄露内容：黑客组织将窃取的Odid公司的客户数据在网上公开，该组织据称试图以此勒索Odid公司。Odido公司是荷兰一家提供电信服务的公司。据报道泄露的数据包括姓名、地址、电话号码、出生日期、银行账号和身份证号码。

泄露数据量：未涉及

关联行业：电信

地区：荷兰

**ManoMano数据泄漏**

泄露时间：2026-03-31

泄露内容：攻击者在BreachForums论坛上声称窃取了ManoMano公司约43GB的数据。ManoMano是一家总部位于法国的在线零售平台，专注于提供家居、建筑和花园相关产品。据称该数据集包含与3780万个用户帐户相关的信息、超过90万个服务工单以及超过1.3万个附件。

泄露数据量：43GB

关联行业：服务

地区：法国

**CarGuru数据泄漏**

泄露时间：2026-03-31

泄露内容：黑客声称泄露了CarGuru的数据。CarGurus是一家总部位于美国的在线汽车市场平台，主要提供买卖二手车和新车的服务。据报道泄露的文件大小为6.1GB，但最初的访问方式尚未明确。泄露的信息包含个人信息和财务数据，包括实际地址、电话号码和融资相关信息。

泄露数据量：6.1GB

关联行业：服务

地区：美国

**02.**

**热点资讯**

**Vertex AI安全风险曝光**

Google Cloud的Vertex AI存在“双面代理”安全风险，该风险源于平台默认服务代理的权限过高。攻击者可构造恶意AI代理，提取服务账号凭证并以该身份执行操作，进而访问用户项目中的云存储数据、Google内部私有容器镜像以及部分基础设施信息。这类恶意代理在表面上执行正常任务的同时，会暗中窃取数据、建立后门并破坏系统隔离机制，从而形成难以察觉的内部威胁。

消息来源：

https://unit42.paloaltonetworks.com/double-agents-vertex-ai/

**CrystalX恶意软件集窃密和恶搞于一体**

研究人员发现一种名为CrystalX的新型恶意软件，兼具间谍、信息窃取和恶搞功能，能窃取浏览器凭据、系统信息并监控用户行为，同时通过戏弄性操作增加隐蔽性和迷惑性，被称为“会笑的RAT”。该案例显示恶意软件正向多功能化与隐蔽化发展，专家建议用户避免下载不明文件并加强终端防护。

消息来源：

https://www.cybersecurity-review.com/a-laughing-rat-crystalx-combines-spyware-stealer-and-prankware-features/

**一次提问触发ChatGPT批量读取文件**

研究人员披露，一次普通的ChatGPT提问触发了大规模数据读取事件：员工仅询问单点登录的配置问题，系统却在42毫秒内通过已授权的Google Drive集成，检索了400多个内部文件，包括产品路线图、财务记录及客户资料等敏感信息。整个过程无黑客入侵、无告警触发，完全在合法OAuth权限下由AI后台自动完成，其行为并非只检索相关文件，而是执行了类似全盘扫描的批量读取操作，从而绕过了传统依赖用户行为的安全监控机制。专家建议采用最小权限原则严格控制AI工具权限范围，并加强对AI集成行为的审计与监控。

消息来源：

https://cybernews.com/security/chatgpt-query-mass-file-retrieval/

**假LinkedIn求职邮件用来窃取账号**

研究人员发现，一种新型钓鱼攻击利用伪造的LinkedIn消息提醒邮件窃取登录凭据：攻击者发送看似来自LinkedIn的任职通知邮件，用户点击链接后会被重定向至伪造的LinkedIn登录页面，一旦输入账号密码，信息即被攻击者窃取，用于账号接管或进一步攻击。安全专家指出，该攻击利用求职机会这一常见诱因，通过制造紧迫感等情绪驱动手段提高成功率，钓鱼活动正变得更加专业化和精准化。建议用户避免点击邮件中的登录链接，通过官方渠道访问平台，并开启多因素认证（MFA）。

消息来源：

https://cybernews.com/security/fake-linkedin-job-emails-steal-login-credentials/

**Ajax曾隐瞒2017年数据泄露事件**

荷兰足球俱乐部Ajax早在2017年就发生数据泄露事件，一名黑客发现其票务系统漏洞可访问客户、员工及球员的个人信息，但俱乐部未公开漏洞，反而要求黑客签署保密协议（NDA）禁止披露。此事近期才被曝光，与后续影响30万球迷的数据泄露事件一同显示出Ajax在安全问题处理上的争议，专家认为隐瞒漏洞会延误修复并削弱网络安全透明度。

消息来源：

https://cybernews.com/security/ajax-silenced-hacker-2017-data-breach/

**03.**

**热点技术**

**macOS信息窃取攻击借助ClickFix传播**

研究人员发现，一种针对macOS的新型恶意软件活动，利用名为ClickFix的社会工程学手法，从伪造的Cloudflare CAPTCHA验证页面入手，诱导用户手动打开终端并粘贴执行恶意命令，从而绕过传统的安全防护机制。命令运行后，会下载并安装Infiniti Stealer信息窃取程序，移除系统安全标记并在后台持续运行，可窃取浏览器账号密码、Keychain数据、加密钱包信息、开发者敏感文件（如.env）及屏幕截图；该恶意程序还通过特殊打包方式伪装成正常应用以提升隐蔽性。专家指出此类攻击不依赖系统漏洞，而是利用用户信任实现自我执行，防御关键在于避免从不可信来源复制终端命令并提高对社交工程攻击的警惕。

消息来源：

https://cybernews.com/security/macos-clickfix-infostealer/

**混合语音钓鱼绕过反垃圾邮件过滤机制**

最新研究显示，一种混合语音钓鱼攻击正在快速演变：攻击者先通过邮件或协作工具发送虚假账单、订阅通知等诱导信息，引导受害者主动拨打电话，从而规避运营商对诈骗电话的标记与拦截；同时，攻击者利用Google Calendar、Zoom、Squarespace等可信平台发送钓鱼内容，这些信息因来自合法服务基础设施，能通过SPF、DKIM、DMARC验证，更容易进入收件箱并获得信任。该攻击的核心在于借用正规平台的信誉绕过安全检测，同时利用受害者主动联系降低其警惕性。对此，专家建议企业加强协作工具的安全监控，并提升员工识别异常邀请与可疑沟通内容的能力。

消息来源：

https://www.esecurityplanet.com/threats/hybrid-vishing-campaigns-abuse-online-services-to-evade-anti-spam-filters/

**Axios遭供应链攻击植入恶意程序**

流行的JavaScript库Axios遭遇严重供应链攻击：攻击者通过劫持维护者的npm账户，发布了被植入恶意代码的版本1.14.1和0.30.4，其中加入了一个伪装成正常依赖的恶意包“plain-crypto-js”。该依赖在安装过程中自动执行脚本，下载并部署可攻击Windows、macOS和Linux系统的远程访问木马，从而窃取API密钥、云凭证、GitHub令牌等敏感信息。由于Axios每周下载量高达上亿次，此次事件潜在影响范围极广。目前恶意版本已被移除，专家建议开发者立即检查依赖版本、回滚至安全版本，并更换所有相关凭证。

消息来源：

https://cybernews.com/security/axios-npm-critical-supply-chain-compromise/

**WhatsApp传播恶意脚本攻击**

一项新的攻击活动通过WhatsApp消息传播恶意VBS脚本文件，针对Windows用户发起入侵：攻击始于2026年2月，利用社交工程诱导用户运行附件，脚本执行后触发多阶段感染链，创建隐藏目录并将curl、bitsadmin等合法工具重命名以躲避检测；随后从AWS、Backblaze等可信云平台下载更多载荷，通过修改系统设置（如绕过UAC）实现权限提升与持久化控制，最终部署恶意MSI安装包建立远程访问后门。该攻击的关键在于结合社交工程、合法工具滥用（LOTL）与云基础设施隐藏流量，专家建议用户避免运行聊天软件中的不明文件，并加强终端防护与脚本执行限制。

消息来源：

https://thehackernews.com/2026/04/microsoft-warns-of-whatsapp-delivered.html

**RoadK1ll后门帮助攻击者横向渗透网络**

研究人员发现一种名为RoadK1ll的新型恶意程序，用于在已入侵网络中进行隐蔽横向移动。该工具是基于Node.js的轻量级植入程序，通过建立WebSocket出站连接与攻击者控制服务器通信，无需在受害主机开放端口以降低检测概率；其核心功能是将被感染设备转变为网络中继节点，使攻击者能够访问内部系统、服务和网络分段，从而放大入侵范围。RoadK1ll支持同时建立多个连接，通过CONNECT、DATA等简单指令转发流量，通信行为伪装成正常网络流量并具备自动重连能力，实现长期隐蔽访问。专家建议企业重点监控异常的WebSocket外联连接和可疑的Node.js进程，以防止此类攻击扩散。

消息来源：

https://www.bleepingcomputer.com/news/security/new-roadk1ll-websocket-implant-used-to-pivot-on-breached-networks/

**04.**

**热点漏洞**

**Moby授权插件绕过漏洞（CVE-2026-34040）**

Moby是一款开源的容器框架，提供授权插件和容器运行时功能。Moby存在授权插件绕过漏洞。该漏洞产生的原因是授权插件机制存在安全缺陷。攻击者可利用该漏洞，通过本地低权限用户身份绕过授权检查，从而获取容器系统的完全控制权限。

影响版本：

Moby<29.3.1

**Dolibarr本地文件包含漏洞（CVE-2026-34036）**

Dolibarr是一款企业资源规划和客户关系管理软件，提供AJAX端点和文件访问功能。Dolibarr存在本地文件包含漏洞。该漏洞产生的原因是/core/ajax/selectobject.php端点在处理objectdesc参数时存在访问控制缺陷。攻击者可利用该漏洞通过已认证用户身份读取服务器上的任意非PHP文件，对系统造成破坏。

影响版本：

dolibarr<=22.0.4

**SciTokens SQL注入漏洞（CVE-2026-32714）**

SciTokens是一款用于生成和使用科学令牌的参考库，提供KeyCache类和SQLite数据库存储功能。SciTokens存在SQL注入漏洞。该漏洞产生的原因是KeyCache类使用str.format()方法将用户提供的数据（如issuer和key\_id）直接拼接构造SQL查询。攻击者可利用该漏洞在未授权状态下执行任意SQL命令，从而控制本地SQLite数据库。

影响版本：

scitokens<1.9.6

**WordPress插件Everest Forms Pro远程代码执行漏洞（CVE-2026-3300）**

Everest Forms Pro是一款用于WordPress网站的表单构建插件，提供复杂计算功能和字段值处理。WordPress插件Everest Forms Pro存在远程代码执行漏洞。该漏洞产生的原因是Calculation Addon的process\_filter函数在将用户提交的表单字段值传递给eval()之前未进行适当转义，直接拼接成PHP代码字符串。攻击者可利用该漏洞在未授权状态下通过任何字符串类型表单字段提交恶意值，在服务器上执行任意PHP代码，对系统造成破坏。

影响版本：

Everest Forms Pro<=1.9.12

**PaperCut NG/MF跨站脚本漏洞（CVE-2026-4794）**

PaperCut NG/MF是一款打印管理软件，提供Web用户界面和管理员配置功能。PaperCut NG/MF存在跨站脚本漏洞。该漏洞产生的原因是多个UI字段未能对用户输入进行有效过滤。攻击者可利用该漏洞通过已认证管理员用户身份注入恶意脚本，从而在其他管理员会话中执行未授权操作，对系统造成破坏。

影响版本：

PaperCut NG/MF<25.0.10

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpOiaqdVjO0uYsdAOOhNg8SXGjd6IGlGV4HqbeSSqGY4iabOUqgsMicn2AE0ZIpHpDpEGBbQicV8nqtZicNhQku5YibPxBWJvCcfy56cM/640?wx_fmt=png&from=appmsg)

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