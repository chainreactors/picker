---
title: 每周高级威胁情报解读(2026.06.19~06.25)
url: https://mp.weixin.qq.com/s/oJllK4gZreQbmSZqKPM4EA
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:50:05.276753
---

# 每周高级威胁情报解读(2026.06.19~06.25)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqicCm1547HNNLOJGGrkia1LEu4tBEwyAaXGlZpc77psfkbPD3l1l7rmrMVznJIsLicXh71GGXrayhm52MFNRicKJl8ViaYns0vC6c2w/0?wx_fmt=jpeg)

# 每周高级威胁情报解读(2026.06.19~06.25)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026.06.19~06.25

**攻击团伙情报**

* Backdoor.Mistic后门与Woodgnat初始访问代理及勒索软件生态关联
* APT-C-36近期针对哥伦比亚境内的活动分析
* GhostShell（MB-0009）：瞄准乌克兰无人机作战和国防供应链
* Mastra供应链攻击活动与朝鲜BlueNoroff组织有关

**攻击行动或事件情报**

* npm 供应链大规模攻击：20 个 Leo 平台软件包遭到入侵
* 谨防冒充 Malwarebytes 的续订诈骗
* StrikeShark 活动通过 SharkLoader 投放 Cobalt Strike
* 攻击者利用 CVE-2026-33017 漏洞进行加密货币挖矿活动
* 两个互不相关的攻击者同时进行的并行活动

**恶意代码情报**

* StealC 和 Amadey：剖析信息窃取者及其背后的网络犯罪服务
* Payouts King初始访问代理部署Edgecution恶意Edge扩展
* 恶意软件攻击活动通过WhatsApp私信分发VBScript
* 新型加载器 OXLOADER 正通过恶意 Google 广告传播 CASTLESTEALER
* Gentlemen 的 EDR killer 框架内幕

**漏洞情报**

* Squidbleed（CVE-2026-47729）漏洞分析
* Zafran披露Dify AI平台DifyTap漏洞：跨租户静默窃听与数据泄露

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqibSmicbz4a9mRuBtKD2ygVGLBDwt0K68RRJUMTnFsaCx6quZlJByJXnYmWT7llR5YRkVteuX4XplIDkEurMyoQXrSwpNXBUWkB8/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq94tLVEDFugdTSVo9TaIqm2QcDSA7ZZ3BvichLIjtibBiaA8RH7jgcAuORq30jnnwAMibRFSXMQBqVRrQy9bjnG54AtaSicVrJXzRTw/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqicgY01WbMlIkdKvJtnbB3N34mtZrHPDj9rame5JneCDLzLtpUsJeAGk2hJWr7sezR7QFO0iaibUiaGIFTHDFNjGpu8uSh235xMibUw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq8IAcONYdUDVeA3EagNicjgsXic1mZ4MkzqPKRD8cPPbJbs2ricdI2Jam3ibojLd0PEuGeU1Vj5YVkSqltzibKmTDgThR8qLSoRaUJw/640?wx_fmt=gif&from=appmsg)

**01**

**Backdoor.Mistic后门与Woodgnat初始访问代理及勒索软件生态关联**

**披露时间：**2026年6月24日

**情报来源：**https://www.security.com/threat-intelligence/new-mistic-backdoor-modelorat

**相关信息：**

Symantec发现了一个名为Backdoor.Mistic的新型后门，自2026年4月起被用于网络犯罪入侵，可能关联初始访问代理团伙Woodgnat。Mistic通过DLL侧加载技术启动，在内存中执行远程载荷且不落地磁盘，具备文件上传下载、命令执行、自毁删除等隐蔽功能，部署目标涵盖保险、教育、IT和专业服务等多个行业，呈现机会主义特征。在一个入侵案例中，Mistic与Woodgnat的标志性工具ModeloRAT同时出现。Woodgnat是自2024年活跃的初始访问代理，通过ClickFix等社会工程技术诱使用户执行恶意PowerShell命令，并利用Microsoft Teams发送技术支持伪装信息，已在多起攻击中向Qilin、Interlock、Rhysida等勒索组织出售访问权限。其工具链包括WinPython、Node.exe、伪造Chrome扩展、多种加载器和大量Windows原生工具，通过多层持久化和多个C2备份保障访问弹性。

**02**

**APT-C-36近期针对哥伦比亚境内的活动分析**

**披露时间：**2026年6月25日

**情报来源：**https://mp.weixin.qq.com/s/jXkbq0oWxu4D5yH46TQybg

**相关信息：**

近期360高级威胁研究院监测发现，盲眼鹰组织在2026年4月份实施了新一轮攻击活动，在本轮活动中，攻击者在攻击过程中增加了使用JavaScript和Powershell编写的下载器，并延续了使用Hijackloader来加载恶意载荷的行为习惯，最终加载Remcos远控木马，实现对受害者计算机的控制。另外，该组织的代码中存在着明显的人工智能生成痕迹。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqiblWtcJ2B7ibcTWPykLPplaiaBMK3H7nrxvdzGxOT7Xs7ibGd9pksO0hXQoEtemnvzcmibmpRycBoNsicdXbywm9BU4Q9BgcF77LwYc/640?wx_fmt=png&from=appmsg)

**03**

**GhostShell（MB-0009）：瞄准乌克兰无人机作战和国防供应链**

**披露时间：**2026年6月22日

**情报来源：**https://blog.synapticsystems.de/ghostshell-mb-0009-targeting-ukraines-uav-operations-and-defense-supply-chain/

**相关信息：**

Synaptic Systems披露了名为GhostShell的新威胁行为者，自2026年2月起针对乌克兰无人机操作和国防供应链发起攻击。初始载体为一个利用CVE漏洞的RAR压缩包，解压后将VBS脚本复制到Windows启动文件夹以实现持久化，同时附带伪装成乌克兰无人机制造商Besomar公司商业提案的诱饵PDF文档，内容涉及充电站、无人机配置等军事技术细节，表明攻击目标涵盖军方、技术人员和采购人员。VBS脚本解码后从cloudaxis.cc下载多个载荷，其中122.exe为加载器，通过XOR解密嵌入的加密覆盖层并提取mTLS客户端证书，证书颁发者为“GhostShell Implant CA”，该植入物与cdnexpress.cc建立HTTPS通信，支持屏幕截图、命令执行、注册表持久化和主机指纹收集。update.exe则从Telegram频道获取C2地址，执行反沙箱检查、AMSI和ETW补丁绕过，并加载Metasploit风格的HTTPS stager。另一载荷22.exe使用Xray代理隧道传输Vidar信息窃取软件。

**04**

**Mastra供应链攻击活动与朝鲜BlueNoroff组织有关**

**披露时间：**2026年6月17日

**情报来源：**https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/

**相关信息：**

Microsoft于2026年6月17日披露，导致140多个Mastra相关npm包受损的供应链攻击归因于朝鲜相关组织Sapphire Sleet，该组织也被称为BlueNoroff。已披露信息显示，攻击者入侵npm维护者账户ehindero，该账户拥有Mastra包环境发布权限，随后在@mastra作用域内发布超过140个软件包的恶意更新，并注入名为easy-day-js的恶意依赖项。该依赖项伪装成dayjs库的拼写相近包，安装后会触发脚本，关闭TLS证书验证，连接攻击者控制的C2基础设施，下载第二阶段载荷并以隐藏进程执行。第二阶段载荷为跨平台信息窃取程序，可收集主机信息、浏览器历史、应用和进程信息，并检查166个加密货币钱包浏览器扩展。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9JtPkHucg2WVl3ZWKc7mUrYlMI4icQWRaW5DFuHcicEia8ibZHnTJzmmNchqrYE55ZSEIJibbgcD84TxjBn99cN2zsPmDJYo6LjMVU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibb9NeibjscLfwUMYTcQl7Us2XI5cIxepXlcwLcs0eXXicNicn3icG7aiaBy7tRH4KiauqP8EYTpPseYwcphMYzh4xibAoNH3l2NfEbps/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibicEH7Eic6ibtgt4ia0dWDibvVkKibunb3zkCxVFP9zia29YgQNJkL3JpJz4GHViarQYLUajpEibVdvx7I7j6TzUB6ufmFiaSCN0HPMVaSA/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqicRJZKQaz6vQh3ta4PKkEURF6iae3ibqWXPSthtrb7VWzDJqaZ162HmJd2WzictCliaMULbibGChBYpfo9CLRkKzo9Sg8rBSIstYkqA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqic2IaqXD2KMbsNyAAA8AAtibsjUznxd8UaF2IDbyDlI8SftU5VeicMAZ1BVyPMum2u5yWvJqVbjusNSD5rohduttOnAQJWTeePHs/640?wx_fmt=gif&from=appmsg)

**01**

**npm 供应链大规模攻击：20 个 Leo 平台软件包遭到入侵**

**披露时间：**2026年6月25日

**情报来源：**https://www.stepsecurity.io/blog/mass-npm-supply-chain-attack-20-leo-platform-packages-compromised

**相关信息：**

2026年6月24日，攻击者在不到三秒的时间内，以协同攻击的方式发布了20个属于Leo平台生态系统的恶意npm软件包。这20个软件包都携带相同的CI/CD攻击工具包，该工具包会从GitHub Actions运行器、云凭证存储、软件包注册表和密码管理器中窃取密钥，然后通过受害者的GitHub令牌将其泄露。这些软件包每周的下载量约为13,600次。

**02**

**谨防冒充 Malwarebytes 的续订诈骗**

**披露时间：**2026年6月24日

**情报来源：**https://www.malwarebytes.com/blog/scams/2026/06/watch-out-for-renewal-scams-pretending-to-be-malwarebytes

**相关信息：**

Malwarebytes发现近期有诈骗分子冒充该公司发送虚假订阅续费通知，利用用户对已使用品牌的信任实施欺诈。这类邮件通常采用以下手法：发件地址非官方域名，使用伪造的发票号和激活码，声称已扣取数百美元费用，金额设计为足以引起焦虑但不至于离谱，结尾附上钓鱼链接或电话号码诱导用户争议扣款。一旦用户拨打骗子提供的号码，便落入诈骗话术陷阱，可能被诱导提供支付信息、验证码或允许远程控制电脑，进而造成实际资金损失或个人信息泄露。部分变种还会冒充PayPal等支付服务商，将用户引导至假登录页面窃取银行凭据。

**03**

**StrikeShark 活动通过 SharkLoader 投放 Cobalt Strike**

**披露时间：**2026年6月24日

**情报来源：**https://securelist.com/strikeshark-campaign/120326/

**相关信息：**

卡巴斯基发现StrikeShark入侵活动，其SharkLoader加载器用于部署Cobalt Strike Beacon。攻击者利用Exchange、SharePoint、Openfire等公网漏洞，或伪装成合法软件的投放器入侵目标。SharkLoader采用DLL侧加载和“完美DLL劫持”技术，释放加载器锁后解密反射加载加密模块，安装大量API钩子实现父进程欺骗和执行流重定向，最终在内存中执行Beacon。后渗透使用FScan等开源工具进行网络扫描和凭证窃取，工具开发者具中文背景但归因置信度低。受害目标涵盖印尼、中国台湾等多地政府及软件企业，呈现定向与机会主义混合特征。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9U4mkIITdnCV8VevUaPEqnSzBicythO0DqB3JvopdOH7QJhf7xeWHbMlBfp9EAibwfgiaVeu9IBy47IBFaoAPibrE4WYk99R0ZXoo/640?wx_fmt=png&from=appmsg)

**04**

**攻击者利用 CVE-2026-33017 漏洞进行加密货币挖矿活动**

**披露时间：**2026年6月23日

**情报来源：**https://www.trendmicro.com/en\_us/research/26/f/from-langflow-to-monero-inside-cve-2026-33017-cryptominer.html

**相关信息：**

趋势科技披露了针对AI应用框架Langflow的CVE-2026-33017漏洞利用活动，攻击者通过未认证API端点向公共流程注入恶意Python代码，实现远程命令执行。初始载荷从C2下载isp.sh脚本，该脚本进一步下载名为lambsys的Go语言二进制木马并通过SSH密钥扩散横向传播。lambsys执行后首先提升文件描述符限制，通过进程名、端口和PID文件三重机制杀死竞争对手的挖矿进程，删除akay和vfinder后门账户，随后依次禁用AppArmor、SELinux、UFW防火墙、iptables以及阿里云安全代理，清理系统日志，解除竞争对手在cron和SSH目录上的不可变属性锁。它安装cron每五分钟和init\_rmount每分钟两个看守进程，实现自我恢复持久化，并锁定/tmp和/var/tmp目录防止删除。最终从C2下载MD5校验的XMRig定制矿工，连接矿池挖掘门罗币。

**05**

**两个互不相关的攻击者同时进行的并行活动**

**披露时间：**2026年6月22日

**情报来源：**https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/

**相关信息：**

微软DART团队在调查一起勒索软件入侵时发现，实际有两组互不相关的威胁组织在同一客户环境中平行活动，使单一攻击演变为多组织、多流派的复杂安全事件。其中Storm-2603自2025年中针对SharePoint服务器进行漏洞探测和利用，之后部署Velociraptor进行环境侦查，安装Cloudflare隧道、Zoho Assist和Visual Studio Code建立多种远程访问及C2通道，通过创建管理员账户维持权限，并加载NSecKrnl.sys脆弱驱动实现内核级EDR绕过。与此同时，调查人员在相同环境内发现了DLL侧加载和自定义后门等不属于Storm-2603技战术的额外痕迹，经微软威胁情报证实为第二个独立组织的活动，且两组攻击系平行而非顺序进行，相互掩盖导致单一视角难以发现全貌。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9Ibs4PB6g88ZBlnDg7cfSVfq4KM37Bib9LxTZv54uYsVaKG3ct8WicmXr0Tq0aZqDPVycFbvDh7Vo1ibIyiaicdh744k1icLhovFyib0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8tVBpuNS6EOicribxJf5rdqgW9RZJ8ukj38YUN4iaIwjHibn3DKPCozfuZUSlicib19xrWtpR4d7rbjibxUiaHZ7D78ibicJbI6cGOJCCpY/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9aPNMMVnKcVSYcMiakcXoKUoPOPCrvNpgo4YtyS5t0nPTAv3xOIpjhAaB6rBRwibIz7oUgH6QIuxv9dD2Y6SDYQxUv37QWHoSAc/640?wx_fmt=gif&from=appmsg)

**恶意代码情报**

![](https...