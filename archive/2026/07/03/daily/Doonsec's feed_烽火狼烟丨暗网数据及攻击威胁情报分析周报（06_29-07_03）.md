---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（06/29-07/03）
url: https://mp.weixin.qq.com/s/ib1kNgal88ur1NVVRXFvjQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:40:49.626083
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（06/29-07/03）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mxwq2AF6zpOp01C3X1YKxSQ6fg9Zu4q6ZJNsOEZcWPibibyNMFpHXghd5ib5pb4X8jO1f6A1YcWMLB1iczIKPvPYGc4zvllNY8bic2FKNRoDiaiajI/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（06/29-07/03）

盛邦安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件398起，环比上周下降24.91%。本周内贩卖数据总量共计93171.9万条；累计涉及6个主要地区及6种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpNNPbmgWcxL4TV8BSZPibTKibrUGLl0Zibeq7Tsr9iajiaVknSZurYsuNHzLqrZSS4loSKqFZvIwMTVzOzMszOH1GH7iaqMFrjWEG6Vs/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及金融、政府、社交等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpNC047E3A5ep3o1rPib4L0MA7EzVKyAfqEB04icZYRrP1eZibYWzeq3FLVZ1OicxyibUMptiaGxXQXJlMwP8xaG7amX4HSfw15icMP50o/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期安全威胁以AI供应链攻击和身份认证绕过为主，并伴随开源生态投毒与恶意软件隐匿化演进风险，本周内出现的安全漏洞中Oracle Payments远程代码执行和Linux内核DirtyClone提权漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP8535条，主要涉及命令注入攻击、组件漏洞攻击等类型。

**01.**

**重点数据泄露事件**

**利比亚民航局疑似数据泄露**

泄露时间：2026-07-02

泄露内容：威胁行为者声称利比亚民航局Libyan Civil Aviation Authority泄露了约300GB的数据集。该数据集覆盖了民航局的核心业务领域，包括飞行员、工程师和空中交通管制员的执照信息；飞机注册、适航认证及维护日志；空中交通与空域管理数据；安全事故调查报告及调查文件；行政与财务数据以及电子服务门户数据等。

泄露数据量：未涉及

关联行业：航空

地区：利比亚

**法国旅行社Pachatours疑似数据泄露**

泄露时间：2026-06-30

泄露内容：攻击者声称窃取了法国旅行社Pachatours的完整数据库，数据量约2GB、超过220万行记录，涉及约3.1万名独立个人。泄露数据包含明文护照号码、航空公司PNR预订编码、B2B旅行社登录凭证、支付交易记录、邮件系统凭证、超过34.9万条会计记录，以及公司完整的产品与定价目录。

泄露数据量：220万

关联行业：旅游

地区：法国

**美国移动核影像公司VIP Imaging疑似数据泄露**

泄露时间：2026-06-29

泄露内容：威胁行为者声称窃取了美国移动核影像公司VIP Imaging约8.67GB的公司数据。VIP Imaging是南加州最大的移动核影像公司，专门为心脏病专家提供心脏PET/CT和SPECT检查服务。泄露的数据极可能涵盖患者的全名、出生日期、联系方式、社会保险号等个人身份信息，以及与心脏PET/CT和SPECT检查相关的详细医疗影像数据、诊断报告、临床病史和医嘱等高度敏感的受保护健康信息。

泄露数据量：未涉及

关联行业：医疗

地区：美国

**德国公民医疗服务数据疑似泄露**

泄露时间：2026-07-02

泄露内容：威胁行为者声称泄露了与德国石勒苏益格-弗伦斯堡地区官方政府网站相关的公民医疗服务数据集，涉及约16.7万条记录。泄露数据涵盖公民医疗服务记录、患者姓名、出生日期、地址和邮政编码、保险相关信息、急诊医生信息、任务日期和任务编号、救援站/位置信息、目的地信息，以及协议和签名认证信息等。

泄露数据量：16.7万

关联行业：医疗

地区：德国

**医疗设备制造商Medtronic疑似数据泄露**

泄露时间：2026-06-30

泄露内容：勒索软件组织声称窃取了医疗设备制造商Medtronic超过900万条记录，Medtronic是全球最大的医疗技术、服务和解决方案公司之一，业务遍及150多个国家。泄露数据涵盖患者及员工的姓名、联系方式、出生日期、社会安全号码等个人身份信息，以及医疗记录、治疗方案、设备数据等健康相关信息，同时还窃取了内部企业数据，涉及专有业务文件、内部通信、合作伙伴信息等。目前已知受影响患者分布：马萨诸塞州约6.4万人、德克萨斯州约29.7万人、佛蒙特州约8,700人。

泄露数据量：900万

关联行业：医疗

地区：美国

**02.**

**热点资讯**

**OpenMatter推出可验证信任层保障AI协作安全**

OpenMatter Network推出一套新的安全架构，旨在解决AI时代跨组织协作中的信任问题。该平台基于“不信任数据，只验证数据”的理念，通过密码学验证手段让企业能在无法完全掌控的环境中进行安全协作、执行敏感计算任务并部署AI系统。其核心技术包括“掩码计算”，可在不暴露底层数据的前提下实现跨组织验证执行；“量子守护”用于对跨系统运行的AI代理进行可验证策略管控；“数据观察者”则提供执行与AI活动的可视化验证。该技术可对跨系统运行的AI代理进行策略管控，同时提供执行过程的可视化验证，确保操作透明可追溯。这一思路被认为是应对AI时代数据主权与跨组织信任缺失问题的重要探索方向。

消息来源：

https://cybernews.com/press-releases/openmatter-network-introduces-verifiable-trust-layer-for-secure-collaboration-and-ai-agents/

**Azure CLI遭大规模密码喷洒攻击**

微软Azure命令行界面遭到了大规模持续密码喷洒攻击。攻击者发起了超过8100万次登录尝试，成功入侵了64个组织中的Microsoft账户。攻击的特殊之处在于，它利用了一个已被弃用的OAuth 2.0授权流程（ROPC），绕过了许多企业已启用的条件访问策略保护。即使部分企业已部署多因素认证，但由于策略配置未覆盖Azure CLI登录或仅针对特定应用和用户组，攻击者仍然能够得手。这些攻击基于此前泄露的旧用户名和密码组合，且不针对特定行业，完全取决于密码在泄露库中的普遍程度。

消息来源：

https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html

**超六成iOS AI应用泄露AI访问密钥**

研究人员检测444款iOS AI聊天应用发现，超六成存在API密钥、访问令牌泄露等安全问题。这些应用在网络传输中明文暴露密钥、使用永久长效令牌，或通过无校验服务器中转AI请求，攻击者只需抓取流量，即可盗用开发者账号免费调用OpenAI等大模型算力，产生的所有费用均由开发者承担，极端情况下单日损失最高可达4.6万美元。涵盖十余类AI服务商与十余种APP品类，多款数万、百万级用户体量的热门应用中招。业内表示，AI应用普遍存在客户端存密钥、权限校验缺失的开发陋习，叠加整改滞后问题，全网真实泄露风险远超统计数据。

消息来源：

https://thehackernews.com/2026/06/282-ios-apps-found-leaking-llm-api-keys.html

**十款热门开源AI代理存在命令过滤风险**

研究人员对11款热门开源AI编程代理进行安全测试后发现，其中10款存在命令过滤机制缺陷，攻击者可利用系统Shell与过滤逻辑之间的执行差异绕过安全限制，执行恶意操作。涉及工具包括Hermes、opencode、Goose、Cline、Roo-Code、Aider、Plandex、Open Interpreter、OpenHands和SWE-agent，合计拥有约54.8万GitHub星标，唯一免疫的是Continue。问题根源在于过滤机制检查的是原始命令文本，而系统Shell在执行前会对其进行参数扩展、引号剥离和命令替换等重写，导致看似安全的命令实际可能变为危险操作。在部分已设有人工确认机制的代理中，一旦切换到自动执行模式，恶意配置文件即可在无任何人为干预的情况下触发攻击。研究人员建议开发者对命令进行分词与规范化评估，而非简单依赖字符串匹配，以加强防护。

消息来源：

https://securityaffairs.com/194546/ai/guardfall-flaw-hits-10-of-11-popular-open-source-ai-agents.html

**WhatsApp新增用户名功能保护手机号隐私**

WhatsApp正式宣布全球开启用户名预约，该功能旨在保护平台超30亿用户的手机号隐私，作为可选功能，用户可自定义3至35位的唯一专属用户名，平台还配备用户名生成工具，企业、政府及公众人物的专属ID会被预留，普通用户无法注册；官方强调该功能主打隐私防护而非社交名片，无公开用户名浏览目录与账号推荐，他人必须掌握完整准确用户名才能发起首次联系，用户还可增设用户名密钥实现双重防护，对方需同时知晓用户名与密钥才能发起初次对话，密钥支持随时重置以阻断陌生新联络，内容创作者、商户与机构可直接认领自身在Instagram、Facebook的现有同名账号，统一跨平台线上标识，启用用户名后其他用户将无法查看你的绑定手机号，功能设置入口为设置-账户-用户名，此次更新弥补了WhatsApp此前仅依靠手机号建立联络带来的隐私漏洞。

消息来源：

https://thehackernews.com/2026/06/whatsapp-is-finally-getting-usernames.html

**03.**

**热点技术**

**SEO投毒活动利用DLL侧加载投递AsyncRAT**

SEO投毒活动，攻击者创建超90个仿冒OBS Studio、DNS Jumper等热门软件的仿冒域名，通过SEO优化将恶意站点推至搜索结果前列。恶意安装包捆绑合法签名的Microsoft install.exe与恶意install.res.1033.dll，利用DLL侧加载加载并部署ScreenConnect远程访问服务。随后创建PowerShell脚本配置Microsoft Defender排除项并禁用UAC提示，通过VBScript在C:\Users\Public释放五个载荷，cap.ps1读取secret\_bytes.txt解密AsyncRAT模块，利用进程镂空注入合法进程执行，连接C2域名mora1987.work.gd实现屏幕录制、数据窃取与远程控制。持久化通过计划任务每两分钟触发script.vbs。DLL侧加载绕过静态检测，进程镂空规避动态分析，Defender排除与UAC禁用实现权限维持。

消息来源：

https://thehackernews.com/2026/07/seo-poisoned-software-sites-abuse.html

**VeilDrop恶意链利用Blogger投递PureLogs窃密木马**

攻击者通过鱼叉式钓鱼或水坑攻击投放伪装为transcript.pdf.js等JavaScript文件，经Windows Script Host执行后启动PowerShell绕过执行策略，从Blogger平台htlwub00klocate.blogspot.com获取下一阶段载荷，利用Google可信基础设施绕过基于信誉的防御。加载器随后终止wscript.exe减少取证痕迹，删除初始JS文件消除执行证据，XOR解密内嵌载荷后进入最具规避性的阶段：每次执行动态构造独特的blogspot.com URL，在URL中插入随机数量的斜杠/绕过静态URL签名；解码后的脚本用随机字符串替换占位值，实现脚本签名和文件哈希的规避；重构后的脚本完全在内存中执行不落盘。核心恶意组件为.NET程序集，通过T1620反射式代码加载启动，若内存执行被阻止则回退至Microsoft签名的白名单二进制regsvcs.exe、installutil.exe、msbuild.exe、aspnet\_compiler.exe级联执行直至成功，最终投递PureLogs .NET信息窃密木马。

消息来源：

https://thehackernews.com/2026/07/veildrop-malware-chain-uses-blogger.html

**RustDuck采用Rust重构强化隐匿通信**

RustDuck恶意软件家族的核心模块正从C重写为Rust，新版本在密钥派生、流量隐匿及抗分析方面深度工程化。执行前运行风险评分检查，检测Wireshark、gdb等分析工具、调试器附加、蜜罐指纹及虚拟机硬件特征，超阈值自毁；其中一项检测访问IANA保留测试地址（应无响应），若收到回复则判定身处仿真网络并退出，另一项通过双时钟比对识别加速沙箱。通信使用ChaCha20-Poly1305握手加密、AES-GCM承载指令，密钥通过HKDF-SHA256与Curve25519交换派生，每十分钟轮换一次，伪装为普通加密Web流量。控制服务器依赖duckdns.org等免费动态DNS服务，通过弱口令及未修复漏洞感染路由器和IoT设备组建DDoS僵尸网络。

消息来源：

https://thehackernews.com/2026/06/rustduck-botnet-rebuilds-in-rust-to.html

**NPM与Go包劫持VS Code投递窃密木马**

攻击者劫持了两个npm包（html-to-gutenberg、fetch-page-assets）及16个Go包。攻击链起点为隐藏在包内的VS Code任务配置文件.vscode/tasks.json，其中名为eslint-check的任务设置了runOn: folderOpen选项，当开发者将包含恶意包的目录作为工作区在VS Code或Cursor中打开并标记为可信时，任务自动触发执行。恶意命令将载荷伪装为字体文件public/fonts/fa-solid-400.woff2，实际包含加密JavaScript代码。该JS代码通过TronGrid区块链交易数据及Aptos备用机制获取下一阶段载荷，随后配置Socket.io后门实现远程控制，同时启动Python加载器从C2获取Python信息窃取器。最终窃密木马可窃取Chromium及Firefox浏览器凭证、密码管理器、加密货币钱包，以及Git凭证、GitHub CLI配置、VS Code全局存储等开发者专属数据，覆盖Windows Credential Manager、Linux Secret Service、macOS Keychain及各云盘元数据，窃取数据打包为ZIP上传至C2或Telegram机器人。该活动被追踪为Fake Font，是Contagious Interview攻击活动的变种。

消息来源：

https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html

**AI幻觉域名抢注用于钓鱼投毒**

新型攻击手法“幻觉域名抢注”是攻击者利用大语言模型的幻觉特性——当被问及某品牌官网或下载链接时模型会编造格式正确但实际不存在的域名，通过枚举品牌名与关键词提示批量诱导模型生成虚假域名，结合WHOIS查询过滤未注册候选并抢先注册。攻击依赖两个前提：不同模型对同一提示词倾向于生成高度一致的幻觉域名，使攻击者可预判并抢注；新注册域名无任何信誉记录，企业防火墙、威胁情报源和基于信誉的产品均无法在初期拦截。攻击者注册后部署三类载荷：钓鱼工具包在用户填写支付信息时实时转发表单数据至C2并克隆界面动态回显维持交互一致性；恶意Android应用向无障碍服务API注册监听器，钩取目标银行或支付类应用的Activity生命周期，覆盖合法登录界面窃取凭证；或利用该域名为后续恶意活动动态生成子域名逃避黑名单。该手法是“垃圾抢注”的域名版本——后者针对AI编码工具捏造的虚假软件包名，PhantomRaven活动已利用此手法在126个npm包中植入恶意代码，累计超86,000次安装。

消息来源：

https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html

**04.**

**热点漏洞**

**Oracle Payments远程代码执行漏洞（CVE-2026-46817）**

Oracle Payments是Oracle E-Business Suite中的支付处理模块，为企业提供支付事务管理和财务交易处理功能。Oracle Payments存在权限管理与身份验证不当漏洞，该漏洞产生的原因是File Transmission组件在处理特定请求时未进行充分的身份验证和权限校验。未经身份验证的远程攻击者可通过HTTP网络访问利用该漏洞，成功攻击可导致Oracle Payments被完全接管。

影响版本：

Oracle Payments <= 12.2.15

**libssh2越界写入漏洞（CVE-2026-55200）**

libssh2是一个开源的SSH2协议客户端C语言库，被curl、备份Agent、嵌入式设备等多种软件广泛使用。libssh2 1.11.1及更早版本存在越界写入漏洞，该漏洞产生的原因是ssh2\_transport\_read()函数在处理传入SSH数据包时，未能对攻击者可控的packet\_length字段强制执行上限检查。远程攻击者可发送带有超大packet\_length值的恶意SSH数据包，触发整数溢出导致堆内存损坏，从而实现远程代码执行。

影响版本：

libssh2 <= 1.11.1

**Microsoft SharePoint Server反序列化远程代码执行漏洞（CVE-2026-45659）**

Microsoft SharePoint Server是微软推出...