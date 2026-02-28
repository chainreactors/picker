---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（02/23-02/27）
url: https://mp.weixin.qq.com/s/NsRQ7lanRIbuSKdZbjKSjQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:50:46.689402
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（02/23-02/27）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mxwq2AF6zpOpdkn5tDpaKyIruCGU5WcxibnJ1duMzFyHIrcJ8licbha1Qn6t6DUJhZKbbcCvqZNUicUS7zq7c9LywsPj7hFfias2ExBCKk4VCibA/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（02/23-02/27）

盛邦安全应急响应中心

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件284起，同比上周增加13.60%。本周内贩卖数据总量共计51408.2万条；累计涉及7个主要地区及7种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpPuaAz1zTiaaHmmmxia8KiaHsXwzVopAia7eia3c33lgYPlyG2hVCibHibzpibcdvoThmbDWKj9KF1cymia0IGXGpp0nD3sBGUrrtwV8ytg/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及贸易、金融、个人信息等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpPtbpBtAmdicHm8HDujLzQsPteC9oP4Woics7YBiaklHKUFxO5ibodibyJptxpGoeaicvlj5TduFxzaPXMhXgUpvvSNc7MsTUa0zMHaU/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期主要威胁来自软件恶意软件、AI工具及网站攻击，需加强关注；本周内出现的安全漏洞以fast-xml-parser XML构建器栈溢出拒绝服务漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP7779条，主要涉及webshell攻击、敏感信息泄露攻击等类型。

**01.**

**重点数据泄露事件**

**Wendy数据库遭泄露**

泄露时间：2026-02-23

泄露内容：一名攻击者声称全球大型快餐连锁品牌Wendy的数据库遭到泄露。泄露的数据集包含特许经营相关信息，如名称、地址、电子邮件账户、系统使用详情及其他运营元数据。该攻击者还声称与API相关的凭据和其他技术配置元素也被一并泄露。

泄露数据量：未涉及

关联行业：餐饮

地区：美国

**Elastic NV公司信息泄露**

泄露时间：2026-02-23

泄露内容：据报道Elastic NV的三个可公开访问且配置错误的Elasticsearch实例泄露了高度敏感数据。Elastic NV是一家技术公司，也是开源搜索与分析引擎Elasticsearch的开发者。泄露的数据库包含超过4300万条记录，其中包括500多万条有效登录凭证、数千张信用卡信息，以及大量个人身份信息和商业交易数据。

泄露数据量：4300万

关联行业：IT

地区：荷兰

**CarGurus账户记录遭泄露**

泄露时间：2026-02-25

泄露内容：黑客团伙公布了1240万CarGurus账户持有人的个人记录，CarGurus是一家在线汽车市场和电商平台公司。泄露数据包括：电子邮件地址、IP地址、姓名、电话号码、物理地址。

泄露数据量：1240万

关联行业：电商

地区：美国

**Odido用户信息泄露**

泄露时间：2026-02-24

泄露内容：黑客声称掌握了荷兰最大的移动电话公司Odido约2100万条用户记录。这些数据可能包括用户的全名、实际住址、电子邮件地址、电话号码、明文密码、IBAN 银行账户详情、护照号码、驾驶执照编号以及企业相关信息。

泄露数据量：2100万

关联行业：通信

地区：荷兰

**法国银行信息泄露**

泄露时间：2026-02-23

泄露内容：据称攻击者利用从一名公务员处窃取的凭证，获取了信息共享平台的访问权限。这些凭证允许攻击者进入FICOBA数据库的部分区域，从而能够查看敏感的账户元数据。泄露的信息可能包括银行账户标识符（如RIB和IBAN）、账户持有人姓名、实际地址，以及在某些情况下的纳税人识别号码。

泄露数据量：未涉及

关联行业：金融

地区：法国

**02.**

**热点资讯**

**广告技术公司Optimizely调查语音钓鱼事件**

Optimizely正在调查一起语音钓鱼攻击事件。在此次事件中，攻击者通过社会工程学手段绕过了身份验证，未经授权访问了部分内部系统，导致有限的业务联系信息（如CRM和办公后台系统中的基本联系数据）被暴露。事件未对业务运营造成影响，也没有证据表明客户的敏感数据或个人可识别信息（PII）遭到泄露。该攻击利用了冒充可信人员的电话诱导，而非技术层面的漏洞，突显了组织在身份验证和访问管理方面存在的薄弱环节。为此，建议加强具有抗钓鱼能力的多因素认证（MFA），完善帮助后台的身份验证流程，遵循最小权限原则，实时监控异常行为，并通过员工培训和模拟演练进一步提升防范社交工程攻击的能力。

消息来源：

https://www.esecurityplanet.com/threats/ad-tech-firm-optimizely-investigates-vishing-incident/

**威胁组织借助AI实现了创纪录的加速攻击**

网络威胁组织正利用生成式AI技术，将攻击速度提升至前所未有的水平，进一步拉大了其与传统安全防护之间的差距。2025年，恶意入侵活动中的平均“突破时间”——即从初始侵入到横向移动至其他系统所需的时间，已缩短至约29分钟，较前一年加快了约65%。这一速度的提升在很大程度上归因于AI的应用。攻击者借助各种AI工具，自动化执行侦察、编写恶意脚本、窃取凭证乃至实施攻击任务，显著提升了攻击效率。报告还指出，许多攻击行动并未明显依赖传统恶意软件，而是通过向合法AI平台投放包含恶意提示的请求，利用“提示注入”（prompt injection）等方式获取敏感信息。

消息来源：

https://www.cybersecuritydive.com/news/threat-groups-record-speeds-ai-attacks/812965/

**密西西比大学医学中心遭勒索软件攻击**

密西西比大学医学中心（UMMC）因勒索软件攻击，被迫关闭全州所有诊所，并取消预约与择期手术。攻击影响了包括Epic电子病历在内的关键系统，迫使医院改用人工记录。联邦机构正协助调查，攻击者已提出勒索要求。急诊部门仍开放，诊所关闭可能持续数日。目前尚无数据泄露的官方确认，该事件凸显医疗行业面临的重大网络安全威胁。

消息来源：

https://www.esecurityplanet.com/threats/university-of-mississippi-medical-center-closes-clinics-after-ransomware-attack/

**Adelaide大学研发出无人机网络安全系统**

澳大利亚Adelaide大学开发了一种新型网络安全系统，旨在保护无人机免受网络攻击。该系统结合软件定义广域网络（SD-WAN）技术，使无人机能同时通过多条通信路径连接，并在遭遇干扰时自动切换；同时内置下一代防火墙，实时监控并拦截可疑活动；还引入恶意软件沙箱，用于隔离检测可疑文件。研究已在实际无人机上完成演示，未来将开展进一步实地测试，目标是推广至商业、应急和政府等领域。

消息来源：

https://www.cybersecurity-review.com/adelaide-university-new-system-designed-to-protect-drones-from-cyber-threats/

**Predator间谍软件可在iPhone上实现传感器监控**

研究人员发现，名为Predator的高级间谍软件能够绕过苹果iPhone的隐私指示灯（绿点为摄像头、橙点为麦克风），在用户毫无察觉的情况下秘密启动摄像头和麦克风进行监控和录音。该软件由Intellexa开发，利用已获得的内核级权限拦截并屏蔽了传感器状态更新的显示，从而阻止隐私指示灯亮起。这种隐蔽手法让用户无法察觉被监视，只能通过专业分析工具才能检测到感染痕迹。

消息来源：

https://www.cybersecurity-review.com/predator-spyware-allows-full-sensor-surveillance-on-iphones/

**03.**

**热点技术**

**恶意NPM包伪造成正常依赖包下载后控制系统**

近期在npm公共代码仓库中出现了一个名为“ambar-src”的恶意软件包，该包在短短几天内被开发者下载了近50,000次。由于它模仿了流行的JavaScript框架Ember.js的名称，很多人误以为这是一个正常的依赖包。该恶意包包含恶意代码，一旦通过npm install安装，就能在开发者的计算机上执行攻击载荷。安全专家指出，该恶意包不仅安装即可触发恶意动作，而且不需要开发者显式导入或运行它的代码，只是安装过程就会执行危害逻辑。一旦被植入，它会尝试获取系统控制、窃取数据并可能向远程服务器下载更复杂的恶意组件。GitHub发布安全通告提醒，任何安装了这个包的系统都应视为已被完全攻破，并立即采取措施（例如更换密钥、断网隔离并重建环境），因为删除包本身并不能保证清除所有恶意程序。

消息来源：

https://cybernews.com/security/malicious-npm-downloaded-by-thousands-of-developers/

**攻击者使用人工智能工具包入侵Fortinet防火墙**

近期网络安全研究显示，攻击者正利用商用生成式AI工具（如Claude）对全球范围内的Fortinet防火墙发起攻击。攻击者并未利用软件漏洞，而是通过扫描暴露在互联网上的管理接口，利用弱密码和缺乏多因素认证的单因素认证等安全缺陷进行访问。在此过程中，AI工具被用于自动化攻击链中的多个环节，包括生成攻击脚本、执行侦察、提取和分析受害设备的配置（如网络拓扑信息）以及运行各类攻击工具。此类AI增强的攻击手法显著降低了技术门槛，使得能力较弱的攻击者也能发动大规模、复杂的网络攻击。一旦成功入侵，攻击者便可获取设备配置、凭证和网络信息等敏感数据，并可能利用这些信息对受害组织展开更深层次的渗透。

消息来源：

https://cybernews.com/security/threat-actor-ai-tools-claude-fortinet-fortigate/

**黑客伪造Zoom更新页面安装监控软件**

近期发现了一个针对Windows用户的诈骗活动：攻击者伪装成Zoom视频会议邀请链接，引导受害者访问一个看起来非常逼真的伪造Zoom等候室页面。一旦用户进入页面，系统会假装出现“网络问题”和“可用更新”提示，强制触发自动下载所谓的Zoom更新安装文件。实际上，该下载的不是合法软件更新，而是预配置的Teramind监控软件安装程序（一种本用于企业监控员工活动的商业工具），它会在受害者系统上秘密安装并运行，不显示图标、不出现在程序列表，且安装后自动删除临时文件以降低被发现的可能性。由于攻击者使用的是合法商业软件并预配置成“隐形模式”，传统病毒扫描工具往往不会发现它。安全研究人员警告，这种社工式钓鱼和界面欺骗策略正越来越多地被滥用来安装间谍工具。

消息来源：

https://cybernews.com/security/hackers-fake-zoom-update-covertly-install-monitoring-tool/

**利用恶意OpenClaw插件传播Atomic macOS信息窃取器**

攻击者正在利用开源AI代理平台OpenClaw的插件生态，将恶意软件Atomic macOS Stealer(AMOS)推送到用户设备上。OpenClaw允许用户通过安装社区贡献的“技能”（类似插件）来扩展功能，攻击者将恶意指令伪装在看似正常的SKILL.md文件中。AI代理会按照这些说明提示用户安装一个命令行程序，引诱用户手动输入密码执行恶意安装步骤。被安装的AMOS变种不具备持久化机制，但能从macOS系统中窃取大量敏感数据，包括Apple与KeePass密钥串、浏览器访问凭证、各种文档、系统配置和用户文件等。虽然该攻击仍依赖社会工程学，但通过AI工具增强了欺骗效果，使得恶意软件能以用户认为“正常”的方式进入系统。因此用户在安装AI插件时，应对其来源和行为保持高度警惕，并避免执行未经验证的命令或工具。

消息来源：

https://www.trendmicro.com/en\_us/research/26/b/openclaw-skills-used-to-distribute-atomic-macos-stealer.html

**黑客针对欧洲金融机构发起钓鱼攻击**

安全媒体报道称，黑客针对欧洲某金融机构发起了网络钓鱼攻击。在此次攻击中，攻击者伪造了“司法域名”，向目标人员发送带有恶意链接的钓鱼邮件，诱导其下载一个包含多层压缩文件的档案。最终解压出的可执行文件伪装成PDF文档，实为恶意程序。一旦运行，攻击链便会部署Remote Manipulator System（RMS）一款合法的远程控制软件。攻击者利用该软件获取受害系统的控制权限，实现远程桌面访问和文件传输功能，从而在受害者网络中维持隐秘访问。安全研究人员指出，这种“活用系统工具”的手法有助于攻击者保持隐蔽性，同时规避传统杀毒软件的检测。此类攻击凸显了高阶社会工程学攻击与远程访问恶意载荷相结合的趋势，也提醒业界注意，受攻击面已扩大至金融与政策领域的潜在风险。

消息来源：

https://thehackernews.com/2026/02/uac-0050-targets-european-financial.html

**04.**

**热点漏洞**

**Ajenti未授权远程代码执行漏洞（CVE-2026-27975）**

Ajenti是一款用于Linux和BSD系统的模块化服务器管理面板，提供服务器配置、应用管理和Web访问功能。Ajenti存在未授权远程代码执行漏洞。该漏洞产生的原因是系统未能对用户访问进行有效身份验证。攻击者可利用该漏洞在未授权状态下在服务器上执行任意代码，从而完全控制受影响的服务器。

影响版本：

Ajenti<2.2.13

**Langflow CSV Agent节点远程代码执行漏洞（CVE-2026-27966）**

Langflow是一款用于构建和部署AI智能体及工作流的开源工具，提供节点化编排、CSV数据处理和代码执行功能。Langflow存在CSV Agent节点远程代码执行漏洞。该漏洞产生的原因是CSV Agent节点硬编码allow\_dangerous\_code=True，导致LangChain的Python REPL工具自动暴露。攻击者可利用该漏洞在未授权状态下通过提示注入执行任意Python和操作系统命令从而实现远程代码执行，对系统造成破坏。

影响版本：

Langflow<1.8.0

**Agenta-API服务器端模板注入漏洞（CVE-2026-27961）**

Agenta是一款开源的LLMOps（大型语言模型运维）平台，提供模型评估、自定义代码执行和实验管理功能。Agenta-API存在服务器端模板注入漏洞。该漏洞产生的原因是API服务器评估器模板渲染功能未能对用户输入进行有效过滤。攻击者可利用该漏洞通过已认证用户身份注入恶意模板代码从而在服务器上执行任意代码，对系统造成破坏。

影响版本：

Agenta-API<0.86.8

**Copyparty反射型跨站脚本漏洞（CVE-2026-27948）**

Copyparty是一款便携式文件服务器，提供文件共享、上传下载和Web管理功能。Copyparty存在反射型跨站脚本漏洞。该漏洞产生的原因是URL参数setck未能对用户输入进行有效过滤。攻击者可利用该漏洞通过诱导用户访问特制链接在受害者浏览器中注入任意JavaScript脚本，从而窃取用户信息。

影响版本：

Copyparty<1.20.9

**fast-xml-parser XML构建器栈溢出拒绝服务漏洞（CVE-2026-27942）**

fast-xml-parser是一款用于XML文档验证、解析和构建的开源工具，提供无需C/C++库的纯JavaScript实现。fast-xml-parser存在XML构建器栈溢出拒绝服务漏洞。该漏洞产生的原因是当preserveOrder参数设置为true时，程序未能对输入数据进行有效处理。攻击者可利用该漏洞通过构造特制的XML数据触发栈溢出，从而导致应用程序崩溃。

影响版本：

fast-xml-parser<5.3.8

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpNKFfXhuuky9NGZuPggQOqNaEwQMAYYl5iauOKIf5p554icia5MxdATVMUSS9Lq0uxiarWlfP9YR2n9Vqqb4Hsuf4Wjl9zZHex7KPk/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNiabToHw1T09Myv7Q/0?wx_fmt=png)...