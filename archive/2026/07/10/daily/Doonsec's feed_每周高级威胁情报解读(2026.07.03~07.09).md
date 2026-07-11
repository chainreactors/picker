---
title: 每周高级威胁情报解读(2026.07.03~07.09)
url: https://mp.weixin.qq.com/s/vZxba_6iuoHyaBZ2W5Nwdg
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:01:35.236944
---

# 每周高级威胁情报解读(2026.07.03~07.09)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOqicW8O5UicepibJQR5vHyO22pBOZkeXSmYBodUOLVATBg1enic9VBicCPtQ5Z9SajSNlEAGYBw74YxLbNpJRCia50rX5CibpzNViaJCCQw/0?wx_fmt=jpeg)

# 每周高级威胁情报解读(2026.07.03~07.09)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026.07.03~07.09

**攻击团伙情报**

* Armored Likho APT组织利用BusySnake Stealer实施间谍活动
* APT-C-36使用新加载器开展攻击活动
* Scattered Spider: 通过共享的战术、技术和程序定义网络犯罪团伙
* 从发票到 AnyDesk：揭露针对俄罗斯航空航天组织的网络钓鱼活动
* Kimsuky的CHM攻击技巧：多阶段执行和选择性有效载荷交付
* Cavern Manticore：揭露与伊朗有关的模块化C2框架

**攻击行动或事件情报**

* “Muck and Load”恶意活动伪装成DNS扫描工具的Go模块实施投毒
* 攻击者通过 Microsoft 网站发起的设备代码网络钓鱼攻击
* 网络钓鱼攻击伪装成知名品牌的招聘面试窃取谷歌账户
* Vidar 窃取者身份揭秘：代码签名滥用、Go 加载器和文件膨胀

**恶意代码情报**

* Linux 后门攻击 iKuai 路由器
* 新型ChocoPoC恶意软件通过木马化的PoC漏洞攻击研究人员
* 研究人员发现新型安卓恶意软件RedWing
* Avalon框架：从法律诱饵到CrownX勒索能力的AI辅助多阶段攻击链
* Jamf发现名为PamStealer的macOS信息窃取器

**漏洞情报**

* GitHub 的新 Agentic Workflows 中存在严重的提示注入漏洞 GitLost
* Linux 的新漏洞Januscape允许虚拟机在 Intel 和 AMD 设备上逃逸

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqib1FaVtSyvtKMBlZbPqCDsNI7Y6hopOxONo5hzWZCAibYJytHgxDfvBkbF61IW5J6n92fGSetsiaxK2eImCPVgfMKdufoXricvbGg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9q0ic3hkyPnVhibFVGuCujVuEJ7jftLgcZ5jL6lOYTYO410kTHsvlQ8icGichBeU9a64vDbbL3C66sstiaLNC48FLs68lkMIQRZwLk/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq972RqbVh4q1sCiaic073Hh57WC3ibaP7ooyce1N67XP4u1vIVjDpdvd1ldZZ7lYUP5fxKWvacTWiazGxHOMlmmR9ib4EnygWP0mKaE/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibdYPxQG4iajoSE6jJwlWlyOicJ3kFEf7iaMozibj1MmaWWGMOsibwa4gfdCs6ficVACOib0iauGPorm5FDMibBPPg8k0ZI3wU6iawOEfdpY/640?wx_fmt=gif&from=appmsg)

**01**

**Armored Likho APT组织利用BusySnake Stealer实施间谍活动**

**披露时间：**2026年7月3日

**情报来源：**https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/

**相关信息：**

Kaspersky Securelist披露新APT组织Armored Likho（又称Eagle Werewolf），该组织针对俄罗斯、巴西和哈萨克斯坦的政府机构和电力基础设施实施网络间谍活动，同时并行开展针对个人的财务动机攻击。攻击者通过钓鱼邮件发送伪装成心理测试或人道主义援助申请的恶意附件，利用EXE自解压包或LNK文件触发感染，其中LNK借助漏洞ZDI-CAN-25373隐藏命令行参数，进而执行PowerShell下载载荷。该组织大量使用AI生成第一阶段代码，代码中包含大量注释和表情符号，从而模糊归因。核心恶意软件BusySnake Stealer采用Python编写，通过PyArmor Pro混淆，运行时动态解密函数。功能包括剪贴板监控、系统文件遍历、提取64位十六进制密钥、窃取Chromium和Firefox浏览器密码及Cookie、通过浏览器扩展窃取Cookie、收集Telegram会话数据、截图以及建立反向SSH隧道实现远程持久访问。载荷从GitHub仓库拉取，通过计划任务每五分钟执行一次。新版本改用COM对象创建计划任务并引入任务状态跟踪机制，提升隐蔽性。该组织持续活跃，工具集不断演进。

**02**

**APT-C-36使用新加载器开展攻击活动**

**披露时间：**2026年7月7日

**情报来源：**https://mp.weixin.qq.com/s/7eMIvKmpK5h2GlkH5U83rg

**相关信息：**

360高级威胁研究院发现APT-C-36于2026年5月发起新一轮攻击，针对哥伦比亚及南美地区政府、金融和保险行业。攻击者通过银行主题钓鱼邮件投递诱饵，释放包含合法Scalar可执行文件和恶意libwinpthread-1.dll的“白加黑”组合。该加载器为QuirkyLoader变体，采用.NET AOT预编译技术生成本地机器码，提高了隐蔽性。加载器解密字符串和API名称，从.reloc节提取加密载荷，经凯撒密码替换和chacha20变体算法两步解密后，通过修改PEB的ImageBaseAddress将DcRAT远控木马注入AddInProcess32.exe进程，实现进程镂空。DcRAT为AsyncRAT增强版，支持反杀毒、进程终止、摄像头控制和信息窃取。攻击者还将文件拷贝至Roaming\ASUS App Service目录并通过开机自启动维持持久性。此次攻击使用的加载器属于MaaS类型，攻击者仅替换加密载荷即可复用。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqibwpKTXlreB75RLpNv876NqW6THT1bxR5rsjQGKI9iczNSljGHicib0vxVDNlRia65SD4XdlvS05XLYTgL9L5viaaIUX3Dvh304GRiao/640?wx_fmt=png&from=appmsg)

**03**

**Scattered Spider: 通过共享的战术、技术和程序定义网络犯罪团伙**

**披露时间：**2026年7月1日

**情报来源：**https://www.group-ib.com/blog/connecting-scattered-spider/

**相关信息：**

根据Group-IB的最新证据，Scattered Spider并非单一网络犯罪组织，而是一个由多个独立子集群组成的松散网络犯罪集体，各子集群共享TTPs和工具但互不统属，类似“匿名者”黑客运动的结构。该集体自2022年起活跃，曾制造Twilio、MGM、Caesars等重大攻击，并通过SIM卡交换、钓鱼页面、社会工程等手段实施入侵。目标涵盖营销服务、移动运营商、银行、企业和加密货币持有者，攻击常以中间组织为跳板，利用其内部通信工具分发恶意链接。子集群采用Okta、Microsoft、Google等假冒登录页面窃取凭证，结合vishing和smishing进行定向欺骗，并通过P1机器人、加密货币钱包耗尽工具和RAT实现最终获利。由于每个子集群规模仅数人且独立运作，逮捕个别成员无法遏制整体威胁。该集体的核心特点是英语母语、高度适应性和灵活的操作流程，使其防御难度极大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqibnxP1Xmz5Z3WrBibxJEopEVnibSialwU9YVj6onYP6Ciba3vHRRt2CiacyVDmNOCvfFA7479YadEzTlpDhY8aaJRPmhxxaWTOEanDo/640?wx_fmt=png&from=appmsg)

**04**

**从发票到 AnyDesk：揭露针对俄罗斯航空航天组织的网络钓鱼活动**

**披露时间：**2026年7月7日

**情报来源：**https://www.seqrite.com/blog/from-invoice-to-anydesk-uncovering-a-phishing-campaign-targeting-russian-aerospace-organizations/

**相关信息：**

Seqrite发现一起针对俄罗斯航空航天组织的定向钓鱼活动，冒充俄罗斯VNIIR研究所发送发票主题邮件，内含密码保护压缩包。受害者解压执行后，释放合法AnyDesk远程桌面、Blat SMTP客户端和Tray Minimizer等工具，通过批处理脚本自动配置AnyDesk无人值守访问并设置密码，创建计划任务实现持久化，同时利用Tray Minimizer隐藏界面避免用户察觉。之后脚本将包含AnyDesk配置和标识信息的压缩包通过Blat经SMTP外传至攻击者邮箱，使攻击者可随时远程重连。该活动利用口令保护附件和echo命令逐步构建执行链，部署后清理临时文件减少痕迹，全程使用合法工具实现无文件落地，属典型离地生存手法。结合此前公开报告，攻击手法、工具链和针对俄航空航天领域的策略与Rare Werewolf组织高度吻合，且过去数月多个相关样本采用相同流程，表明该活动仍在持续。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqicdmhzGA4DHe5sWLU7s3KJv1iaXDOGwB4aflF4hZyKGVcORibJtexNl1vBRB6m9Tnlv8aws7dHJaXiay9E7us8mTgF6hb598aXx3s/640?wx_fmt=png&from=appmsg)

**05**

**Kimsuky的CHM攻击技巧：多阶段执行和选择性有效载荷交付**

**披露时间：**2026年6月29日

**情报来源：**https://blog.synapticsystems.de/inside-kimsukys-chm-tradecraft-multi-stage-execution-and-selective-payload-delivery/

**相关信息：**

Kimsuky组织利用恶意CHM文件实施多阶段攻击，通过HTML帮助组件中的ActiveX对象启动隐藏PowerShell，写入Base64数据后由certutil解码，再以wscript执行VBScript载荷。该载荷从C2获取侦察脚本，收集计算机名、操作系统、处理器、用户目录和进程列表等信息，上传至finalservice.php，并创建名为Edge Updater的计划任务实现持久化，每小时执行一次后续脚本。持久化脚本以随机间隔再次请求C2，返回的VBScript将任务转交PowerShell，通过Invoke-RestMethod和Invoke-Expression直接执行服务器响应。最终端点checkservice.php在分析环境中返回空响应，表明存在选择性载荷投递机制。整个攻击链不向磁盘写入可执行文件，主要依赖系统内置工具。C2域名解析至韩国IP，归属ucloud，且网站包含Kimsuky常见的欢迎信息和favicon，结合朝鲜语诱饵，归因可靠。

**06**

**Cavern Manticore：揭露与伊朗有关的模块化C2框架**

**披露时间：**2026年7月6日

**情报来源：**https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/

**相关信息：**

Check Point发现伊朗关联组织Cavern Manticore自2026年起针对以色列政府和IT行业发起攻击，使用一套模块化C2框架，通过滥用目标已部署的远程管理软件实现初始入侵。该框架完全基于.NET，但各组件故意采用三种不同编译格式——纯.NET IL、混合模式C++/CLI和NativeAOT，迫使分析人员在多套工具链间切换，从而提升逆向难度。核心代理uxtheme.dll伪装成Windows主题库，通过DLL侧加载执行，创建独立AppDomain隔离运行各模块并在执行后卸载，实现反取证。通信模块n-HTCommp.dll处理HTTPS和WebSocket加密流量，载荷使用XOR 0x48加Base64编码。后渗透模块包括文件管理、DPAPI解密、SQL数据库操作、LDAP侦察、网络扫描和SOCKS5隧道代理等功能。该框架从早期Cav3rn演进而来，PDB路径和C2域名等痕迹指向同一开发者。归因依据包括针对以色列的战略目标、通过IT供应商供应链横向移动的手法，以及与伊朗MOIS关联组织Lyceum的TTP重叠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq9IlgBxHlt8d45tL5icmj7dnYz5KAPXvnwzJlcXbvSRibfRSz6hVoZCuibuS2iaASGibmiczLayFc12ZdlFEErBo7VA7MTUQMTKicUpYA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqicwHWyfsvwOcyfCJZJ1U4LnicTZS6WwMInNlYS2mHuvU2wROXvxxO2DAaoq02KbGZYjlxGicI7EZrABmZqaETE2NHdgEOQbtA0mw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqib00kNsqCXHXqFWh8396ItxRI7UjEiaERY9R3BF2Uh5ALvP4hrYLzZ7dkMv8icmpzRYlficCW6ZZEvNYFlIDIhvfPoy73ejpBJyB8/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqicQawNszQ8Wh082Eb7gn0ic5EQ6U4MYjox2bWpXCSc9vROe9lZESgOicktqT6XerEh4f2hXEItMHwMaExpvoW4BBdXbG2uP52QNY/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9NGmYUNCiaNkAicmEJhIuNwtSdb0eHickA9GScfXDU0QJVJiaz1odafnfS0quajotlqic1SDibzy7VsUycrlibsDrAnH8kgfVMiatPdrc/640?wx_fmt=gif&from=appmsg)

**01**

**“Muck and Load”恶意活动伪装成DNS扫描工具的Go模块实施投毒**

**披露时间：**2026年7月8日

**情报来源：**https://socket.dev/blog/malicious-go-module-exposes-github-malware-lure-network

**相关信息：**

Socket发现代号“Muck and Load”的恶意活动，攻击者通过伪造成DNS扫描工具的Go模块实施投毒，该模块嵌入隐藏的PowerShell命令，从muckcoding.com下载编码载荷并解密执行。后续多级PowerShell加载器利用公开死存储获取加密的载荷位置信息，解密后从GitHub下载带密码的Quixo.7z压缩包，解压至仿冒微软Photos路径并启动Microsoft.exe，最终部署AsyncRAT、Quasar、Remcos等远控木马和窃密软件。该行动还构建了由222个仓库、190个账户组成的GitHub诱饵网络，通过自动化工作流伪造提交活跃度，伪装成加密货币工具、游戏作弊器等热门项目。攻击者使用同一邮箱跨账户控制，部分仓库直接托管Vidar窃密软件和XMRig矿工。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9FriayAmnAvIvJBLknJ9QZ9lJYQDn09Cyia05ViaxdN7IChXgRnibGEPBWuzxS8aoOUBgrytgovUds4GtLHTKSA6jGNcsZnoZ3gEU/640?wx_fmt=png&from=appmsg)

**02**

**攻击者通过 Microsoft 网站发起的设备代码网络钓鱼攻击**

**披露时间：**2026年7月6日

**情报来源：**https://securelist.com/microsoft-device-code-phishing-attack/120350/

**相关信息：**

攻击者利用微软OAuth设备授权码流发起钓鱼攻击，绕过传统域名检查。用户收到的钓鱼邮件内含密码保护的PDF，打开后看到所谓“共享文件”，需点击链接获取一次性访问码。该链接实际指向攻击者预先从微软合法端点获取的device\_code和user\_code。点击后跳转至伪造页面显示该代码，再重定向至微软官方devicelogin页面。用户误以为在正常登录，输入代码并完成MFA后，攻击者即获得access\_token和refresh\_token，可读取邮件、OneDrive和Teams。攻击者还利用Cacoo.com等合法网站作为开放重定向跳板，增加可信度。后续变种针对巴西用户，移除PDF附件直接嵌入链接。由于整个过程使用微...