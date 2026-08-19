---
title: 金融行业网络安全监测月报(202607)
url: https://blog.netlab.360.com/jin-rong-xing-ye-wang-luo-an-quan-jian-ce-yue-bao-202607/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2026-08-18
fetch_date: 2026-08-19T02:56:29.708098
---

# 金融行业网络安全监测月报(202607)

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

# 金融行业网络安全监测月报(202607)

* [![NOTOn1y](/content/images/size/w100/2026/08/2f35bd757c0c0fcb537ee47e8fa31171.jpg)](/author/on1y/)

#### [NOTOn1y](/author/on1y/)

18 Aug 2026
• 13 min read

[Share](#/share)

**报告编号：**360-TIC-202607-FIN01

## 一、报告概述

### 范围说明

基于360威胁情报中心对全球网络安全态势的持续监测与深度研判，本报告结合客户需求，整理了金融行业安全威胁情报，报告重点内容涵盖：

· **重大安全威胁事件分析：**聚焦REF6045银行欺诈活动，分析利用ClickFix投递SCMBANKER，并借助会话监控、剪贴板劫持及远程控制实施欺诈的链路与风险。

· **恶意软件威胁分析：**关注GoldPickaxe安卓银行木马窃取设备解锁凭证、生物识别材料和移动金融数据的风险。

· **加密资产与区块链安全态势分析：**剖析Injective官方SDK遭供应链投毒后，在运行时窃取助记词和私钥的攻击方式。

· **新兴技术安全趋势：**关注AI辅助恶意代码开发、AI智能体参与攻击以及间接提示注入带来的新风险。

· **多维度威胁数据支持：**综合Elastic、Zimperium、JFrog、Zscaler和Hunt.io等机构的公开研究成果。

────────────────────────────────────

## 二、重大安全威胁事件分析

**事件名称：**REF6045利用SCMBANKER实施银行欺诈活动

**发布日期：**2026-07-08

**发布机构：**Elastic Security Labs

**威胁概述：**

2026年7月，Elastic Security Labs披露REF6045银行欺诈活动。攻击者通过仿冒验证码页面实施ClickFix社会工程，诱导受害者在Windows“运行”窗口执行恶意命令，下载SCMBANKER PowerShell工具包。该工具包使用BITS任务下载组件，并通过注册表Run键和启动文件夹实现持久化。运行后可监控银行会话、截取屏幕、记录键盘输入、替换剪贴板中的账户号码，还能展示虚假银行警告、将浏览器重定向至钓鱼页面，或按需安装Remote Utilities接管主机。该活动重点针对墨西哥银行、金融科技、支付处理、加密货币交易和投资平台。Elastic认为，相关脚本存在明显的大模型辅助编写痕迹，但实际欺诈仍由人工操作员主导。

**受影响行业：**金融、科技

**攻击手法（MITRE ATT&CK映射）：**

· **ClickFix钓鱼与用户执行(T1566.002/T1204.001)：**通过虚假验证码页面将恶意命令写入剪贴板，诱导受害者在Windows“运行”窗口执行。

· **命令与脚本执行(T1059.003/T1059.001)：**利用批处理脚本和PowerShell分阶段部署SCMBANKER，并以虚假Windows更新界面掩盖后台执行过程。

· **BITS任务与工具传输(T1197/T1105)：**使用bitsadmin等系统工具下载主控脚本、功能模块和远程访问组件。

· **启动项持久化(T1547.001)：**将run.vbs写入注册表Run键和启动文件夹，强制重启后由启动项触发执行。

· **信息收集与欺诈操控(T1010/T1113/T1115)：**监控银行窗口、截取屏幕，并替换剪贴板中的银行账户或银行卡号，帮助操作员识别并优先处理高价值目标。

· **远程访问与资金盗取(T1219/T1657)：**按需安装Remote Utilities取得主机远程控制权，并结合语音钓鱼、浏览器重定向等方式实施金融欺诈。

**IOC指标：**

· **Domain：**ratonvaquero2026.online, monteviral2026.duckdns.org, osogransd.online, negratomasa2026.online, gestionmontelavaria2026.online, ssinvestigaciones.com, bancaporinternetbbmx.online

· **IP：**68.211.161.46, 216.250.112.100, 185.242.246.169

· **SHA256：**b30cb0aa977aacdab94d2ef503186c8f0b2fc10d7cf0d7c7c0ada70c127dc7e8, 554f1aefeb698995501751328c2f9fe93f02a680679fba3dd15f1ed93d46bf1b, ff3555154e91e42490cc722b6c7f3c4c91654b7ef53a35d0719ffb89accf1b27, 526287a40aad1b218228cdd1f459ad3b93f858585048347644d597c6ab19515a, 685d29ce8a550feb3a9e1d1c5926ec5e927615cf34aab62c108a812a1eb6737c, 8c87ea94401fa97d3743a87604e088d1a29c7b06cf9673623941a42da68452a6, 30ff24faad80184bb43660a8bd317df99a8d09d31bae3b446aaa876543f2620f, 32d981b3e7c36aa7030cfd9ee412bff742e00b36c39c80634b2681f89de4a487

· **URL：**http://68.211.161.46/validation.txt, http://216.250.112.100/validation.txt, https://negratomasa2026.online/dashboard2/recData.php, https://negratomasa2026.online/dashboard2/imagenes.php, https://negratomasa2026.online/dashboard2/avisos2.php, https://negratomasa2026.online/dashboard2/logs.php, http://68.211.161.46/driver.html?off

**报告链接：**

https://www.elastic.co/security-labs/mexican-banking-fraud-scmbanker-ref6045

────────────────────────────────────

## 三、恶意软件威胁分析

**事件名称：**GoldPickaxe安卓银行木马窃取生物识别数据

**发布日期：**2026-07-09

**发布机构：**Zimperium zLabs

**威胁概述：**

Zimperium zLabs披露GoldPickaxe移动银行木马的新变种，并将其归因于活跃在亚太地区的GoldFactory团伙。攻击者利用仿冒“快播”视频平台的网站诱导用户安装Dropper APK，再滥用Android SessionInstaller API部署第二阶段载荷，并通过AES加密和动态代码加载隐藏核心功能。该变种可窃取设备解锁凭证，读取短信、联系人和通话记录，还能进行键盘记录、屏幕覆盖、屏幕共享和手势模拟。恶意程序还会诱导受害者上传身份证件并录制人脸视频，这些材料可能被用于绕过电子身份核验和活体认证。Zimperium共发现19个在野样本，影响5个国家；其中一个样本内置118个印度尼西亚金融应用目标。

**受影响行业：**金融、个人用户

**攻击手法（MITRE ATT&CK Mobile映射）：**

· **钓鱼分发(T1660)：**通过仿冒视频平台网站诱导用户下载并安装恶意Dropper APK。

· **动态代码加载(T1406)：**将核心恶意逻辑封装在AES加密的payload\_dex.bin中，在运行时解密并加载，以规避静态扫描。

· **隐藏应用图标(T1628.001)：**省略MAIN和LAUNCHER入口，使恶意应用不在主屏幕显示，增加用户发现和卸载的难度。

· **图形界面输入捕获(T1417.002)：**通过伪造锁屏和金融应用界面，窃取PIN、图案、密码及其他登录信息。

· **无障碍功能与屏幕捕获(T1453/T1513)：**滥用无障碍服务读取屏幕元素，并通过Media Projection API开启实时屏幕共享。

· **视频采集与C2外泄(T1512/T1646)：**诱导受害者录制人脸视频、上传身份证件，并通过加密C2通道外传相关生物识别和金融数据。

**报告链接：**

https://zimperium.com/blog/goldpickaxe-returns-when-your-biometric-information-is-as-important-as-your-money

────────────────────────────────────

## 四、加密资产与区块链安全态势分析

**事件名称：**Injective官方SDK供应链投毒窃取钱包密钥

**发布日期：**2026-07-12

**发布机构：**JFrog Security Research（IOC补充来源：SlowMist）

**威胁概述：**

JFrog Security Research披露，Injective Labs官方TypeScript SDK软件包@injectivelabs/sdk-ts@1.20.21被植入钱包密钥窃取代码。该攻击不依赖安装脚本，而是在应用调用钱包密钥功能时触发。恶意代码以“密钥派生遥测”伪装正常功能，可在PrivateKey.fromMnemonic()、PrivateKey.fromHex()及部分交易广播和钱包封装流程中截获助记词或私钥，并将数据Base64编码后写入X-Request-Id请求头，以gRPC-Web POST请求外传。只有sdk-ts包直接包含恶意代码，其他同版本组件因依赖关系受到间接影响。修复版本为1.20.23。使用受影响版本处理过的钱包密钥应按已泄露处置，尽快升级、轮换密钥并迁移资产。

**受影响行业：**金融、区块链、科技

**攻击手法（MITRE ATT&CK映射）：**

· **软件供应链入侵(T1195.002)：**攻击者篡改官方npm软件包发布链，将窃密逻辑植入受信任的Injective SDK版本。

· **私钥与凭证窃取(T1552.004)：**在钱包生成、导入、签名和交易广播相关调用路径中截获助记词和私钥。

· **应用层协议伪装(T1071.001)：**将外传请求伪装成Injective相关的HTTPS gRPC-Web流量。

· **C2通道数据外泄(T1041)：**将密钥数据经Base64编码后写入高熵X-Request-Id请求头，并通过空请求体POST请求外传。

**IOC指标：**

· **Domain：**testnet.archival.chain.grpc-web.injective.network

· **IP：**15.235.87.88

· **MD5：**d72bdb86962a4bb673619945175f6378, 9b37a86aad8a5e191c1b8c3397848503, 06c9394afab853bcbca15f354ef0d72a

· **SHA1：**9233c753a5a4b0f89d1ae0f4ecf6a74fd8d9eff1, 4bfbe6c80d0fb9983c21288fdfaa23c1cc8744e4, e9bf2a19038b34e9cc6239a4849b3d5a9bd98aef

· **SHA256：**624ac118eb5e66d6d313424d375021298bf8a809925a7c642300a41fd672a05d, 103c4e6181151c1bcfedc41506cd1815458c38375d08a8fcd9981dbe0b965ce0, 9a59eb454f3ca3fe91214136ee5edd417cc47a80e6f169b52099d6561944baf9

· **URL：**https://testnet.archival.chain.grpc-web.injective.network/

**报告链接：**

https://research.jfrog.com/post/injective-sdk-supply-chain-attack/

────────────────────────────────────

## 五、威胁技术发展趋势

AI智能体参与攻击与间接提示注入风险上升

**趋势说明：**

2026年7月披露的多起事件显示，AI已被用于恶意脚本编写、攻击任务执行和自动化编排。同时，具备联网、检索和工具调用能力的AI智能体，也可能受到恶意内容诱导。Elastic在REF6045活动中发现，部分PowerShell模块存在大模型辅助编写痕迹，但具体欺诈操作仍由人工控制。总体来看，AI正在降低恶意工具的开发和使用门槛，并给金融机构带来新的安全风险。

**典型案例包括：**

Hunt.io于2026年7月23日披露，针对泰国财政部的攻击活动中发现Hermes AI智能体和Hades跨平台Go后门。相关日志显示，Hermes以无人值守模式执行了主机信息收集、文件遍历和LinPEAS结果分析等操作。由于攻击者如何取得初始访问权限尚不明确，目前只能确认AI参与了后续渗透和任务执行，不能认定整起入侵由AI独立完成。

同期，Zscaler ThreatLabz发现，攻击者利用SEO投毒、隐藏网页内容和JSON-LD结构化数据，对AI智能体实施间接提示注入，诱导其采信虚假API文档，甚至执行异常的加密资产操作。金融机构在使用AI智能体时，应重点限制其联网检索、工具调用和支付权限，并加强对外部内容的校验。

**报告链接：**

https://www.elastic.co/security-labs/mexican-banking-fraud-scmbanker-ref6045

https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent

https://threatlabz.zscaler.com/blogs/security-research/indirect-prompt-injection-web-content-targets-ai-agents

────────────────────────────────────

## 六、防御建议与落地措施

### （一）终端防护建议

**ClickFix与脚本执行阻断：**重点检测浏览器页面诱导用户打开Windows“运行”窗口、向剪贴板写入长命令、curl下载内容直接传入cmd.exe，以及PowerShell、VBS和bitsadmin异常组合调用等行为；同时限制普通用户创建注册表Run启动项和启动文件夹脚本。

**移动金融终端反欺诈加固：**在移动银行和钱包应用中加强运行时保护，识别无障碍服务滥用、Media Projection屏幕共享、覆盖层注入、用户手势模拟和应用图标隐藏等异常行为；对人脸视频采集、证件上传及异常设备环境增加二次活体检测和人工复核。

### （二）网络防护措施

**恶意基础设施与异常外联监测：**将本月IOC同步至DNS、代理、防火墙和EDR策略，重点监测终端访问ClickFix投递页面、SCMBANKER控制面板及Injective恶意gRPC-Web端点的行为；结合进程上下文识别浏览器、脚本解释器和远程访问软件的异常外联。

**高熵请求头与AI访问流量审计：**排查application/grpc-web+proto空请求体中出现高熵X-Request-Id的情况；对AI智能体的联网检索、网页抓取、代码仓库访问和工具调用流量进行内容过滤与来源校验，识别包含隐藏指令或异常JSON-LD内容的网页，并限制未经批准的支付跳转。

### （三）资产与数据管控

**软件依赖与钱包密钥应急处置：**全面检查package-lock.json、yarn.lock、pnpm-lock.yaml及制品缓存中是否存在@injectivelabs/\* 1.20.21，并升级至1.20.23或更高版本；凡曾由受影响版本生成、导入或调用过的助记词和私钥，均应立即轮换，并将资产迁移至新钱包。

**AI智能体最小权限与人工审批：**将联网检索、代码执行、凭据访问、文件写入和资金支付权限分层隔离，禁止默认开启无人值守的高权限模式；涉及转账、密钥操作、生产配置变更和外部脚本执行时，应增加策略校验和人工确认，并保留完整的工具调用日志。

────────────────────────────────────

## 七、报告总结与交流

经过对本月相关事件的综合分析，金融行业安全风险呈现以下特点：

**金融欺诈链条进一步延伸：**REF6045活动将ClickFix诱导、脚本投递、终端监控和远程控制串联起来。攻击者取得主机控制后，可持续观察银行会话并根据交易状态实施干预，传统仅针对钓鱼入口的防护难以及时发现后续欺诈行为。

...