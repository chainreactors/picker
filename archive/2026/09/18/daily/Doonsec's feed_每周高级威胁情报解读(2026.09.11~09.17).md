---
title: 每周高级威胁情报解读(2026.09.11~09.17)
url: https://mp.weixin.qq.com/s/_vui-lVPog4QSv-CuwQwRg
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:55:51.386660
---

# 每周高级威胁情报解读(2026.09.11~09.17)

# 每周高级威胁情报解读(2026.09.11~09.17)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026.09.11~09.17

**攻击团伙情报**

* APT36 发起 RapidRust 攻击，投放 RUSTYSHADE 等多组件恶意套件
* 夜鹰（NightEagle）团伙针对俄罗斯企业实施定向攻击
* 朝鲜 IT Worker 利用 Discord 群组招募中间人实施求职欺诈
* Cyclops Blink 新版本现身，增强嗅探与内网侦查能力
* PolinRider 供应链攻击：捕获朝鲜攻击者真人上机操作痕迹
* Kimsuky 组织利用伪装安装包植入远控木马的攻击链分析

**攻击行动或事件情报**

* 诈骗分子利用 AI 构建高度逼真的杀毒软件续费钓鱼页面
* Beast (GodDamn) 勒索团伙借助 RDP 攻击韩国医疗机构
* 批量扫描 Vite 开发服务器，利用漏洞窃取云凭证
* WordPress 插件供应链投毒，Admin Menu Editor Pro 恶意更新包植入 Web 后门
* 银狐云端“生死簿”：从“无条件返回”到“黑名单”机制

**恶意代码情报**

* Atomic macOS（AMOS）窃取木马攻击活动分析
* GhostCode 钓鱼套件：滥用 OAuth 设备代码流程窃取微软账号权限
* Lemmings 框架：支撑主动影响行动的俄罗斯规模化虚拟身份供给管理系统
* The banana stand：利用 MQTT 在亚洲地区代理交易与管控主机感染节点

**漏洞情报**

* 思科 FMC 管理平台高危漏洞被在野利用，攻击者可获取系统最高权限
* 微软发布紧急Windows更新以修复RDS故障

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibicZgkBX59SyglxPcjUTtQ5wp2ibQQq1jsqibicqWEgzc6b8Ehq72MoDnde4KyWrNvYHOhn0kec7atCGArrgPNJqJyNCFX7KsMnSs/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqib6JDcXiakQsZ9FHS1WMfjZjQzFUG489Gkp0sA8doYClCxEgth3jEBDDZGTfibJpI4ZHSkSYjaaCZZN4TIXgO1WyKYCM2sicv5Qbs/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9yib8DXe3SV9C08RnSSkurUQIWruiarF5yUznXkPDnLvg6ibiaWS4qBuYUkbqnEulibwhiaD2Ebw3o4eaguyicwv2Dhxu5pnwXBSCU7I/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibI2vyuNXpLtNaLduJU9ASjAbjiaugjP2HeXWsibDw5egJZlhGuFImHWYOqlH1uCzFGt3YW2K4aXowoMfarXuCenSWdiboClWf9icI/640?wx_fmt=gif&from=appmsg)

**01**

**APT36 发起 RapidRust 攻击，投放 RUSTYSHADE 等多组件恶意套件**

**披露时间：**2026年9月16日

**情报来源**：https://www.zscaler.com/blogs/security-research/operation-rapidrust-apt36-deploys-rustyshade-rustymove-psnatch-and

**相关信息：**

Zscaler ThreatLabz于2026年8月发现巴基斯坦背景APT36针对印度和阿富汗政府国防实体发起Operation RapidRust行动。该组织部署四种新工具：RUSTYSHADE为Rust后门，利用攻击者控制的私有GitHub仓库作C2，硬编码PAT，采用AES-256-GCM加密通信，通过command.txt等文件交换指令与结果；RUSTYMOVE监控可移动媒体，将预置的RUSTYSHADE压缩包和恶意LNK复制到USB等外部驱动器根目录，以向气隙网络传播；PSNATCH和BASHNATCH分别针对Windows和Linux，递归扫描桌面、下载、文档及OneDrive等目录，窃取近120天内修改的多种文件并上传至以受感染主机命名的私有GitHub仓库。APT36还注册仿冒印度媒体theprints.org和indiatodays.org的域名托管恶意PowerShell脚本，并通过伪装成OneDrive和Edge更新任务的计划任务实现持久化，同时进行网络扫描、共享枚举和横向移动尝试。

**02**

**夜鹰（NightEagle）团伙针对俄罗斯企业实施定向攻击**

**披露时间：**2026年9月16日

**情报来源：**https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/

**相关信息：**

卡巴斯基发现NightEagle（APT-Q-95）组织针对俄罗斯企业的攻击活动。该组织自2023年活跃，原聚焦亚洲，现通过有效凭证接入企业VPN，来源包括Cloudflare WARP隧道和欧洲虚拟基础设施。攻击者在Exchange服务器部署GhostContainer后门，利用ViewState注入.NET程序集，实现代理转发并绕过AMSI和事件日志。随后通过RDP横向移动，从伪装成合法工具的GitHub压缩包下载adobe\_32.exe、AdobeSync.exe等，结合Microsoft dev tunnels和rdp2tcp建立隧道，并利用Impacket atexec创建计划任务及netsh端口转发。攻击者还利用BlueKeep漏洞创建管理员账户，请求Kerberos票据并尝试DCSync。

**03**

**朝鲜 IT Worker 利用 Discord 群组招募中间人实施求职欺诈**

**披露时间：**2026年9月14日

**情报来源：**https://www.silentpush.com/blog/nk-it-worker/

**相关信息：**

Silent Push披露朝鲜IT工作者通过Discord服务器“Mouse Review”发布虚假招聘广告，招募美国、欧盟及拉美国家人员充当代理。研究人员创建虚假身份，通过Telegram联系化名“Tec Guru”的招募者，中高置信度判断其为朝鲜IT工作者。该计划以身份与代理盗用为核心，让代理人以本人身份和摄像头通过面试，朝鲜操作者则通过Google Meet实时辅导、AnyDesk等远程控制软件完成技术测试，并借助AI工具填补知识缺口，收益按代理人35%、朝鲜方65%分成。交谈中，对方推荐朝鲜威胁行为者常用的Astrill VPN，并在听到“朝鲜”后立即关闭摄像头。

**04**

**Cyclops Blink 新版本现身，增强嗅探与内网侦查能力**

**披露时间：**2026年9月11日

**情报来源：**https://www.sophos.com/en-us/blog/-eye-spy-cyclops-blink-returns-with-extended-capabilities

**相关信息：**

Sophos披露俄罗斯关联的IRON VIKING组织（即Sandworm）使用升级版Cyclops Blink恶意软件攻击Cisco防火墙管理中心设备。该64位Linux植入物名为timezone\_check，采用父控制器加五个工作模块的模块化架构，通过IPC通信。模块分别负责主机侦察并可能读取密码哈希、文件传输与载荷执行、主动网络扫描、选择性数据包捕获及持久化。持久化通过SysV init实现，将自身复制到/lib/tz/timezone\_check并创建/etc/init.d脚本及rc2至rc5启动链接。C2服务器为89.34.96.56，使用TLS加密通信，每小时信标一次，并内置DNS-over-HTTPS解析器以规避本地DNS日志。与2022年针对WatchGuard的PowerPC版本相比，2026版转为x86-64架构，改用通用Linux持久化，新增网络扫描和数据包捕获模块，可扩展至其他Linux网络设备。报告建议将威胁狩猎范围扩大到兼容的Linux网络设备，并提供了相关文件路径、IP地址和用户代理等检测指标。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9Sx0B1EUeYhed9V1n1sqQuW6eEqksUs52vpemyTWtPicR6Nsj9gMzTaApBVxfIIsmZxnBcPqYzW8uLiasoGaJyOHOiaCA5pPcTok/640?wx_fmt=png&from=appmsg)

**05**

**PolinRider 供应链攻击：捕获朝鲜攻击者真人上机操作痕迹**

**披露时间：**2026年9月9日

**情报来源：**https://blog.deception.pro/blog/hok-dprk-polinrider-sep-2026

**相关信息：**

Deception.Pro在2026年8月底通过蜜罐诱饵工作站捕获朝鲜关联攻击者PolinRider的实时供应链入侵。攻击者约三小时内发现诱饵并入侵，持续约167小时。活动与Lazarus子集的Contagious Interview和Famous Chollima一致，并与APT37有重叠。攻击者以虚假招聘和编码测试为诱饵，诱导目标运行恶意PyPI包pybitjs，Node.js加载器回连23.27.13[.]135，通过cmd和curl从catbox下载SvcHostUpdate.py与SvcHostUpdate.js，利用GitLab原始README传递二次载荷。其访问lsass，部署XFiles和OmniStealer风格窃密程序，收集剪贴板、屏幕和主机数据，并以SYSTEM权限静默安装Python及requests、pyperclip、mss、Pillow等库。持久化分三层，全部伪装成MicrosoftCLROptimization，置于systemprofile路径，最后向150.251.113[.]223:8443上传数据并轮换用户代理。攻击还涉及以太坊RPC域名，意图窃取凭证、源代码和加密货币。防御应封锁C2和catbox、GitLab原始请求，狩猎systemprofile下的伪装持久化，扫描依赖并限制出站。

**06**

**Kimsuky 组织利用伪装安装包植入远控木马的攻击链分析**

**披露时间：**2026年9月10日

**情报来源：**https://mp.weixin.qq.com/s/9ilhH-WUqeNCStDfbrBsrw

**相关信息：**

360高级威胁研究院捕获了Kimsuky组织（APT-C-55）针对韩国的最新攻击活动。攻击者通过伪装成游戏安装包OrionQuests-Setup.exe投递恶意LNK文件，LNK从自身偏移读取数据并异或解密还原PowerShell脚本。脚本首先检测42种安全工具进程和虚拟机环境以规避分析，随后收集主机名、操作系统、进程列表等信息回传至C2服务器，并绕过InfinityFree免费主机的JavaScript反机器人验证机制下载后续载荷。第二阶段载荷test.bef\_fri将文件头伪装为RTF格式，在内存中修复解压缩后反射加载高度混淆的C#模块化后门，连接107.172.249.140:443，支持插件式扩展和AES加密通信。攻击者通过伪装为“Google Chrome更新”的计划任务实现持久化。报告通过载荷相似性、LNK解密手法和环境检测方式等特征，将活动归属为Kimsuky组织，并指出其工具链正朝着更隐蔽、更灵活的方向持续演进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqic5qmk8Cf1N5bz4PDkzaQs3meXAwR1zaENNSvtdiaBHMfFweKsRWziaEZXRzjI6500mo9s6aIN67P6NavCzyuibCYDZZKx3aBf0mE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq8FZp5XvPvwgniciaTHuoP2VqktiaPmJoGOlqBBJMeWUf3g9Tj464SWnCgplxsib10fHqpX7wfr05Hc3uVN3vqkIWzUzolDxAt3Eicc/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8tjyG6naFypLc9CKibGKxnRnvenNQpbbtIrGU1aGbNGe7SjhgGGqEgSLrkPbVO4PUqPo2micKzWbSfUfXfoWmQV9frg6ouEQEKI/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq8czb77c6cJx6LgpYQ6jjp5LA4p3bLUKE2QmmNNZUaLUn68Le2yMAMbMmMcFCh5AaPTPhMnicEDaTHaX6xaVpo1tXWltiaibC1OXc/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqibGz2mkkBpsXHy3LG0LuxhFeoZMHfiaCvAjNZias69useLXwpW4vSjz8w3DanBMwBQW4pVfcGibO7GJwbD1hTKia8qIOaFP6IyveSI/640?wx_fmt=gif&from=appmsg)

**01**

**诈骗分子利用 AI 构建高度逼真的杀毒软件续费钓鱼页面**

**披露时间：**2026年9月16日

**情报来源：**https://www.malwarebytes.com/blog/threat-intel/2026/09/ai-helps-scammers-build-convincing-antivirus-renewal-pages

**相关信息：**

Malwarebytes披露诈骗者利用AI生成逼真的杀毒软件续订钓鱼页面。诈骗以短信或消息称订阅已自动续费开始，引导用户点击取消链接，进入冒充Avast的假页面。该页面针对比利时用户，用法语显示已续费129.99欧元、覆盖五台设备等信息，并附绿色对勾和状态徽章，但订阅和扣费均不存在。页面要求填写姓名、邮箱和比利时手机号，不索取密码或卡号，以降低戒心，实际是为后续电话诈骗收集联系方式。代码中留有AI助手写给委托方的法语注释，说明表单尚未连接提交功能，还有未使用的样式和含糊文案，表明页面由AI生成且未完成，可能作为模板出售。文章指出，页面外观专业不再可靠，应直接检查银行账单或通过官方应用核实订阅，警惕仅索要电话号码的取消表单，后续来电才是真正危险，切勿安装远程访问软件。若已填表或安装软件，应断网、卸载、改密码并联系银行。

**02**

**Beast (GodDamn) 勒索团伙借助 RDP 攻击韩国医疗机构**

**披露时间：**2026年9月14日

**情报来源：**https://blog.alyac.co.kr/5779

**相关信息：**

韩国医疗机构近期遭受基于RDP的Beast（又称GodDamn）勒索软件攻击。攻击者通过RDP登录后，利用驱动器重定向功能（\tsclient\C...）将PCHunter、ProcessHacker等工具传入内网，先禁用安全产品，再执行勒索软件。Beast会检查系统语言和区域，若属独联体国家则直接退出，避免加密。其配置数据以ChaCha20加密存储，包含自复制、注册表持久化、删除卷影、停止数据库与备份服务、结束办公及安全进程、枚举网络共享、加密文件等功能。加密文件扩展名为“.[8位ID-8位ID].goddamn”，排除系统关键文件、可执行文件扩展名及系统目录。勒索信要求12小时内联系，否则泄露数据，并提供邮箱及TOX、Session匿名通讯ID。防御建议包括限制RDP访问和驱动器重定向、监控tsclient异常文件传输、隔离备份、及时隔离受感染系统。

**03**

**批量扫描 Vite 开发服务器，利用漏洞窃取云凭证**

**披露时间：**2026年9月11日

**情报来源：**https://www.f5.com/labs/articles/cloud-takeover-mass-scanning-for-exposed-vite-endpoints-cve-2026-39364

**相关信息：**

F5 Labs披露2026年8月针对暴露的Vite开发服务器的大规模扫描活动，利用CVE-2026-39364未认证文件读取漏洞，通过添加?raw等查询参数绕过server.fs.deny限制，读取.env、AWS凭据、Azure令牌、Terraform状态文件及/proc/self/environ等敏感信息。蜜网记录807个会话、约3.2万原始事件，较前三个月基线1732大幅增长。扫描器伪造Googlebot、ClaudeBot等User-Agent并注入X-Forwarded-For，源IP多来自Google Cloud，同时探测多个旧版Vite漏洞及Next.js绕过。目标集中于云凭证和基础设施状态文件，表明攻击者意图快速获取云环境访问权限。建议升级Vite至修复版本、确保开发端口不暴露公网、部署WAF阻断/@fs/路径、严格反向DNS验证爬虫、轮换可能泄露的密钥。

**04**

**WordPress 插件供应链投毒，Admin Menu Editor Pro 恶意更新包植入 Web 后门**

**披露时间：**2026年9月15日

**情报来源：**https://www.bleepingcomputer.com/news/security/malcious-admin-menu-editor-pro-plugin-b...