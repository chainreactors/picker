---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（07/06-07/10）
url: https://mp.weixin.qq.com/s/JaSUQsvYe6d4b_Qqz0Ztnw
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:58:50.999233
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（07/06-07/10）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mxwq2AF6zpNZspvMEcZgtzkJfDM32Bp4y3n5kARkLtohHf1PuzoxibibE6s3IjFrFIq6luzXYg4qzy6765pkj8jx953WOFvCHia2gmn5SBDQVM/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（07/06-07/10）

盛邦安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件490起，环比上周上升23.12%。本周内贩卖数据总量共计389767.5万条；累计涉及7个主要地区及5种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpPx0s3ue4hmricMBjcE199WYNsKS2gubT1R6lGLLenxeia1azwPcrU1FPicXYWF1wA6ompzyfJFMCXaRM3VDhuKwyibW0d5PxhQpFY/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及金融、服务、贸易等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpMUGvB95YolIGiad53tyjlJq8DWWdLhw3oVRgejqicglDuzIDxOhZp6gGUqIlC4N5MYHeB21zlfibCOdomF4LQXiaLzPZchEGKibxtU/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期安全威胁以新型网络钓鱼攻击和AI技术武器化为主，并伴随恶意软件降低攻击门槛、僵尸网络代理化等风险持续扩散，本周内出现的安全漏洞中Topoteretes Cognee授权绕过漏洞和DataEase双重高危漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP8744条，主要涉及XPATH注入攻击、组件漏洞攻击等类型。

**01.**

**重点数据泄露事件**

**美国保险服务商AssuranceAmerica疑似数据泄露**

泄露时间：2026-07-08

泄露内容：攻击者通过入侵一名美国保险服务商AssuranceAmerica公司员工的账户获取了系统访问权限。泄露数据涉及约699万人，包含姓名、联系方式、驾驶执照号码，以及与汽车保险相关的保单和账户信息、驾驶员和车辆信息、客户索赔记录等。

泄露数据量：约699万

关联行业：金融

地区：美国

**以色列支付公司Nayax疑似数据泄露**

泄露时间：2026-07-07

泄露内容：攻击者声称已全面入侵以色列全球性金融科技和支付公司Nayax，窃取了超过100TB的数据。泄露数据包括超过10亿条数据记录、完整的预付卡数据、客户身份信息、交易历史记录、内部API密钥和凭证、基础设施架构图、源代码及财务记录。

泄露数据量：10亿

关联行业：金融

地区：以色列

**法国IT学校ESGI疑似数据泄露**

泄露时间：2026-07-08

泄露内容：威胁行为者在一个论坛上发布了一个据称属于法国IT学校ESGI的SQL数据库转储文件。ESGI是一所在法国多地设有校区的私立高等IT与数字技术专业院校。该转储文件包含来自一个用户表的26,451行数据，包括学生全名、电子邮件地址、手机号码、家庭住址、城市和邮政编码、国籍、班级和专业、入学状态和日期、Geschool ID以及学校Active Directory登录名。

泄露数据量：约2.6万

关联行业：教育

地区：法国

**墨西哥健康门户网站数据疑似泄露**

泄露时间：2026-07-07

泄露内容：攻击者声称入侵了墨西哥Culiacán市政府的官方数字健康系统Portal de Salud de Culiacán，并免费公开了窃取的数据，数据包含4,045份完整患者记录。泄露字段涵盖患者全名、CURP国家身份证号、出生日期、联系方式、家庭住址、就业/隶属关系数据，以及详尽的医疗病史，包括遗传性和病理性疾病、物质使用习惯等高度敏感信息。

泄露数据量：约4千

关联行业：医疗

地区：墨西哥

**法国医疗软件平台Follow.fr疑似数据泄露**

泄露时间：2026-07-09

泄露内容：威胁行为者声称获取了Follow.fr的数据库。Follow.fr是法国一款获得Ségur认证的医疗软件和患者记录平台，供专科医生和外科医生使用。获取的数据集包含2,052,123条患者记录，泄露的字段包括患者姓名、性别、出生日期、电子邮件和电话号码、法国INSEE国家身份证号、健康保险号码以及相关医生信息。

泄露数据量：约205万

关联行业：医疗

地区：法国

**02.**

**热点资讯**

**欧美企业遭新型“幽灵网络钓鱼”大规模攻击**

一种名为“幽灵网络钓鱼”的新型攻击正对欧美企业构成严重威胁，安全研究人员每天都能检测到10至15个此类攻击活动。该攻击通过名为EvilTokens的钓鱼即服务平台实施，平台上线仅五周就导致超过340家企业账户被入侵。攻击者发送的钓鱼链接指向经过加密的恶意页面，能够轻松绕过传统的邮件安全检测，只有在受害者点击后才会在浏览器中解密并显示真正的钓鱼内容。攻击最终目标是Microsoft 365账户，利用微软合法的设备代码授权流程，诱骗受害者在官方登录页面输入攻击者生成的代码并完成多因素认证，从而在不窃取密码的情况下直接接管账户。据监测，咨询、金融服务、制造、科技和银行等行业是重灾区，暴露率均超过66%。

消息来源：

https://thehackernews.com/2026/07/new-ghost-phishing-wave-is-breaking.html

**RedWing安卓银行木马以订阅制在Telegram上出租**

新型安卓恶意软件RedWing正在Telegram上以“恶意软件即服务”的模式出租，即使是不懂技术的攻击者也能借此接管受害者手机、窃取银行账户凭证并拦截一次性验证码。该服务提供分档订阅、推荐折扣及操作教程，买家无需任何编程能力，通过Telegram机器人即可按需生成定制化的恶意应用。攻击始于钓鱼链接，受害者点击后会进入仿冒官方应用商店的页面，被诱导安装应用并授予权限。RedWing能利用虚假登录界面覆盖真实银行应用以窃取密码，读取短信和屏幕内容以获取验证码，甚至通过呼叫转移屏蔽银行的电话核实。此外，它还具备屏幕实时监控、键盘记录、摄像头与麦克风控制、文件读取及位置追踪等功能，同时可将感染手机组织起来对目标网站发起流量攻击。研究人员已统计到82家机构被列为攻击目标。

消息来源：

https://thehackernews.com/2026/07/redwing-maas-packages-android-bank.html

**新型APT组织利用AI生成恶意软件攻击多国政府与电网**

研究人员发现一个名为Armored Likho的黑客组织开始针对多国政府机构及电力基础设施发起间谍活动，同时也对普通个体实施经济犯罪。攻击通常始于鱼叉式钓鱼邮件，附件一旦被打开便会感染设备，窃取浏览器密码、加密货币私钥和通讯软件会话数据，同时为攻击者留下远程操控后门。研究人员发现，该组织所使用的恶意软件代码中包含大量人类风格注释和表情符号，这种特征在以往恶意软件中从未出现，强烈表明攻击者正在利用大语言模型生成恶意代码。该组织此前曾使用过其他恶意软件，新工具在结构上与之存在明显关联，表明这是一个持续演进的威胁团伙。

消息来源：

https://securityaffairs.com/194854/apt/ai-generated-malware-powers-new-armored-likho-apt-campaign.html

**假冒7-Zip安装程序将设备变为代理节点**

威胁组织运营的恶意住宅代理业务是通过仿冒知名软件和代理服务商来构建并变现庞大的代理网络。攻击者利用“7zip.com”等仿冒域名分发植入恶意代码的7-Zip安装程序，在用户毫无察觉的情况下将设备变为代理节点。受害者设备被秘密招募进一个代理僵尸网络，随后通过仿冒SmartProxy、IP Royal 等知名代理品牌的店面进行变现，同时运行虚假的独立评测网站来为欺诈店面引流。该组织还利用过期的域名来继承其信誉和合法性，并通过教程内容、搜索引擎诱导和仿冒域名来吸引受害者。除7-Zip外，同一基础设施还被用于分发假冒WhatsApp、TikTok和YouTube下载器以及WireVPN等工具的安装程序。

消息来源：

https://thehackernews.com/2026/07/fake-7-zip-installers-turn-devices-into.html

**SCMBANKER恶意软件针对金融用户发起攻击**

一场针对金融体系的恶意软件活动正在持续蔓延，目标涵盖银行、金融科技公司、支付处理商和加密货币交易所。攻击者通过虚假的CAPTCHA验证页面诱导受害者运行恶意命令，受害者在完成验证后被指示将命令粘贴到Windows运行对话框中执行，恶意软件随即在后台下载完整工具集，并持续弹出提示诱使受害者授权更高权限。一旦感染成功，攻击者便可实时监控银行会话、截取屏幕、覆盖欺诈性警告信息、重定向浏览器，甚至替换剪贴板中的银行账号，同时还可部署远程控制工具实现设备完全接管，最终目的是窃取受害者资金。研究还发现，该工具包有很大一部分代码疑似借助大语言模型生成，这起事件再次凸显了虚假验证码作为初始攻击入口的广泛滥用趋势。

消息来源：

https://thehackernews.com/2026/07/scmbanker-malware-uses-clickfix-lures.html

**03.**

**热点技术**

**Cavern C2混合编译框架实现模块化后渗透**

Cavern模块化C2框架是基于.NET构建，攻击始于滥用SysAid软件更新进行DLL侧加载执行木马化uxtheme.dll，加载独立通信模块通过HTTPS或WebSocket连接C2动态拉取后渗透模块。该框架核心技术特征在于跨三种.NET编译格式的混合部署：纯.NET Framework模块负责文件操作、SQL枚举与AD侦察；Native AOT预编译模块负责通信、网络扫描与SOCKS5代理；主代理将托管.NET代码与原生C++混合编译于单一PE文件。Agent内嵌统一模块调度器，以n-前缀区分原生DLL通过LoadLibraryA加载，其余视为托管程序集通过AppDomain隔离机制加载。不同编译格式迫使逆向工程师切换多种工具集与元数据重建流程，按模块隔离的AppDomain作为反取证手段，每个模块在独立AppDomain中运行且卸载时保留内存区域造成残留效应。WebSocket隧道模块支持复用C2通道传输数据，模块间通过标准输入输出流交换JSON格式结构化数据实现解耦。

消息来源：

https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html

**Rogue Agent共享执行环境缺陷致跨Agent控制**

Google Dialogflow CX的Code Blocks功能允许开发者向聊天机器人对话流中添加自定义Python代码，代码运行在Google管理的Cloud Run环境中。该环境的核心技术问题在于同一Google Cloud项目下所有Agent共享同一个执行环境实例，且该环境中的包装文件code\_execution\_env.py为可写状态。该文件负责将开发者代码与内部设置代码拼接后传递给Python执行。具备dialogflow.playbooks.update权限的用户可在恶意Agent的Code Block中远程覆盖此共享包装文件，使修改后的版本应用于所有共享该环境的Agent。该环境具备无限制的出站互联网访问能力，内置urllib库可实现数据外传与远程指令接收；同时环境暴露Instance Metadata Service，可查询Google托管服务账户的凭证。覆盖操作发生在Google内部环境中客户无可见性，Cloud Logging几乎不记录相关日志。

消息来源：

https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html

**QuimaRAT实现跨平台多格式投递链与模块化设计**

QuimaRAT的Java-based RAT以MaaS模式运营是基于Apache Maven构建为模块化项目，配套完整的Builder、Loader与Dropper工具链支持JAR/EXE/APP/SH/BAT/VBS等多格式输出。Builder通过ProGuard混淆、Maven Shade重定位及字符串解密器处理生成初始载荷，Loader利用浏览器缓存投递payload，可生成HTA/LNK等格式的stager链接并绕过SmartScreen。执行后通过操作系统临时目录创建互斥锁文件确保单实例运行，内嵌配置解析进行环境验证。持久化机制因平台而异：Windows使用注册表Run键、计划任务及Startup文件夹；Linux使用.desktop自启动项和crontab重启任务；macOS使用LaunchAgent plist文件。通信支持TCP、WebSocket、TLS及HTTPS多协议，内置组件维持通道活性，连接丢失时自动重连，可选Pastebin-based C2热更新机制允许动态轮换C2地址而无需重新编译payload。内嵌Java Native Access原生库覆盖Windows、Linux、macOS多架构，通过C/C++代码直接调用底层OS API实现跨平台交互，支持远程命令执行、载荷下发、凭据窃取、剪贴板操作、摄像头监控及Windows主机无文件shellcode执行，模块化架构支持通过C2动态加载、卸载和更新加密插件以扩展功能。

消息来源：

https://thehackernews.com/2026/07/new-java-based-quimarat-maas-built-to.html

**AI编码代理行为模糊攻击检测边界**

Claude Code、Cursor、OpenAI Codex等AI编码代理的常规操作正频繁触发原本用于检测人类攻击者的行为告警。这些代理本身并非恶意，但其行为模式与攻击手法高度重叠。在统计的拦截事件中，凭据访问类占56.2%、执行类占28.8%，其中最大的触发源是代理调用Windows DPAPI解密浏览器存储的凭证，Claude Code的/browse技能通过PowerShell调用DPAPI解锁浏览器保存数据，另有实例中Cursor通过PowerShell向启动文件夹写入脚本实现持久化。在载荷获取方面，OpenAI Codex先用certutil从python.org下载Python安装包，被拦截后立即切换至bitsadmin重试，这种“被拦截后自动换手法”原本是区分活体攻击者与自动化脚本的关键行为特征，如今AI代理也具备了该能力。AI代理正在使浏览器凭据调用、LOLBin下载、启动目录写入等传统高置信度告警行为失去指向性，检测逻辑需要从静态行为匹配转向基于意图与上下文的判断。

消息来源：

https://thehackernews.com/2026/07/ai-coding-agents-found-triggering.html

**HalluSquatting利用AI幻觉与提示注入组建僵尸网络**

新型攻击手法HalluSquatting是利用AI编码助手的幻觉特性与间接提示注入，诱导AI自动安装恶意软件组建跨平台僵尸网络。攻击先追踪热门仓库或插件，反复向AI请求该资源并记录其最常虚构出的虚假名称；随后在GitHub或插件市场提前注册该名称并植入隐藏对抗指令；当真实用户请求AI获取该资源时，AI编造出相同虚假名称并拉取攻击者注册版本，其中的隐藏指令被AI视为用户指令的一部分，被劫持的AI使用自身内置的终端工具执行“安装僵尸程序”等命令。该攻击的技术核心在于AI虚构名称的高度一致性——在不同措辞和不同厂商模型间，AI在仓库请求中虚构出同一错误名称的概率高达85%，在技能安装场景中达到100%。与传统僵尸网络依赖弱口令或蠕虫传播不同，HalluSquatting无需任何网络漏洞利用，载荷以AI读取的文本形式到达，防火墙无法察觉。

消息来源：

https://thehackernews.com/2026/07/new-hallusquatting-attack-could-trick.html

**04.**

**热点漏洞**

**Topoteretes Cognee授权问题漏洞（CVE-2026-58473）**

Cognee是一款开源AI知识管理平台。Cognee存在权限控制不当漏洞，该漏洞源于/settings端点未执行管理员或超级用户检查。未经身份验证的远程攻击者可自行注册账户并调用设置端点，覆盖全局LLM提供商配置。攻击者可借此将实例范围内所有LLM操作重定向至其控制的端点，从而窃取所有用户的提示词、上传文档、提取的实体及知识图谱内容。

影响版本：

Topoteretes Cognee < 1.2.0

**DataEase SQL注入漏洞（CVE-2026-55635）**

DataEase是一款开源数据可视化与分析工具。DataEase存在SQL注入漏洞，该漏洞源于图表配额和Y轴过滤器在Quota2SQLObj.getYWheres()中直接将攻击者控制的过滤器值嵌入生成的SQL，而未像其他过滤路径那样进行SQL字面量验证和转义。已通过身份验证的远程攻击者（具备创建或修改图表定义权限，或可提交包含配额过滤器的图表数据请求）可向配置的数据源执行的查询中注入恶意SQL代码。成功利用可能导致敏感信息泄露、数据篡改或数据库服务器被完全控制。

影响版本：

DataEase < 2.10.24

**LocalAI服务器端请求伪造漏洞（CVE-2026-59707）**

LocalAI是一款开源本地大模型推理服务框架。LocalAI存在服务器端请求伪造漏洞，该漏洞源于POST /models/apply端点对请求体中的gallery URL字段未做内网地址校验，直接传入gallery.GetGalleryConfigFromURLWithContext而未进行适当验证。未...