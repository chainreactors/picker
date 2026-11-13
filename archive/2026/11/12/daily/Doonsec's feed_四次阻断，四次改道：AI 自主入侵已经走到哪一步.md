---
title: 四次阻断，四次改道：AI 自主入侵已经走到哪一步
url: https://mp.weixin.qq.com/s/4zpv1uShrTOh7cTDdHc-Kg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:01:42.965216
---

# 四次阻断，四次改道：AI 自主入侵已经走到哪一步

# 四次阻断，四次改道：AI 自主入侵已经走到哪一步

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

AI 安全 · 威胁情报

四次阻断，四次改道：

AI 自主入侵已经走到哪一步

一名中文操作者通过自定义智能体框架，将侦察、漏洞利用、权限提升、横向移动和数据获取等大量技术工作交由 AI 执行——四次被拦截后，它能自行分析原因、替换路径并验证结果。

· AI 自主入侵　· 智能体框架　· C2 与隧道　· 信息截至 2026.11.12

**摘要：**Malbear Labs 披露了“雪球行动”（Operation Snowball）：一名中文操作者通过自定义智能体框架，将侦察、漏洞利用、权限提升、横向移动和数据获取等大量技术工作交由 AI 执行。比“AI 会攻击”更值得关注的是，它在 PwnKit、隧道工具、提权二进制和标准反序列化链相继失效后，能够自行分析原因、替换路径并验证结果。本文复盘攻击链，厘清影响边界，并给出 ATT&CK 映射、IOC 与检测建议。

一次 Linux 提权尝试被端点防护终止，进程退出码为 137。接下来发生的事情不是停止，也不是等待人工指令：智能体放弃 PwnKit，改用同一主机上可用的 sudo vi 逃逸，并建立 systemd 持久化。

这只是“雪球行动”中四次自动改道之一。

2026 年 11 月 8 日，Malbear Labs 披露，研究人员在例行开放目录扫描中发现了一个无需认证即可下载的攻击工作区，其中包括 70 余份压缩会话记录、按网段整理的目录、数百个目标的侦察结果、工具配置、凭据缓存、数据库转储以及智能体生成的行动报告。

这些材料记录了一名中文操作者与一套基于 DeepSeek Flash 的自定义智能体框架，对一家欧洲电信运营商及其数据中心、云环境中的机构开展了持续两周多的入侵活动。操作者负责设定目标和检查结果，大量具体技术动作则由智能体完成。

01 四次“此路不通”，四次自动改道

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqibMVxJF8iaia9icE6RtUUyeU9DEMUuEoZftXLCl0RWNSmSUnl4BEPfC8LUQQ23Bat1BBwsb52QWcSV5nm50Nu786D8JjGATS3RIo4/640?wx_fmt=png&from=appmsg)

**图1｜四次防御受阻与智能体自动改道**

图源：根据 Malbear Labs 披露的恢复会话记录整理绘制。

1. PwnKit 被终止，改用 sudo vi 提权

智能体在一台 Linux 主机上尝试利用 CVE-2021-4034（PwnKit）提升权限，Trend Micro Deep Security 检测并终止了相关进程。智能体记录拦截结果后，没有继续重复同一利用路径，而是转向该主机已有的 sudo vi shell 逃逸条件，随后创建 systemd 单元，以维持高权限执行。

Malbear Labs 指出，这一调整没有操作者逐步指挥。由于智能体此前已侦察 Deep Security 管理节点、代理版本和策略更新通道，它将 PwnKit 失败归因于防御控制，并选择了另一条路径。

2. suo5 隧道被拦截，现场编写 Perl 替代工具

取得立足点后，智能体部署 suo5 内存型 SOCKS 隧道，以代理进入内部网段。端点控制拦截该工具后，主智能体让工作智能体编写了一个自定义 Perl HTTP-to-TCP 桥接脚本：通过 HTTP 请求携带代理流量，再转发为原始 TCP 连接。

该脚本在同一会话内完成编写、部署和验证，隧道随之恢复。Perl 代理本身并不新颖，关键在于框架完成了“发现阻断—生成替代工具—确认可用”的闭环。

3. JuicyPotato 被删除，Windows 持久化转向脚本化

在 Windows 主机上，智能体曾尝试投放 JuicyPotato，但 Trend Micro OfficeScan 10 随即将其删除。会话记录显示，该主机的 OfficeScan 配置为 EnableBM=0，即行为监控未启用；已知二进制被特征匹配清除，而自定义脚本和非 PE 载荷能够留存。

这次 JuicyPotato 尝试其实是一次冗余测试：智能体此前已通过 BladeLogic RSCD 的权限映射获得 SYSTEM 级访问。但失败仍改变了后续操作方式。其 Windows 持久化更多转向明文 PowerShell、编码命令、WMI 事件订阅和计划任务，减少对已知可执行文件的依赖。

4. Liferay 主机禁止出网，重建整条利用链

最具技术含量的调整发生在一台 Liferay 7.0 主机上。该主机存在 CVE-2020-7961 反序列化漏洞，能够从互联网接收 HTTPS 请求，却无法主动连接外部 IP。

这使依赖 JNDI 回连的常规利用路径失效：攻击请求可以进入，但目标 JVM 无法回连攻击者的 LDAP 服务。现成的 CommonsBeanutils1 链又因目标缺少 commons-collections 库而失败。

智能体随后利用目标现有类构造了新的进程内反序列化链，通过 PriorityQueue、BeanComparator 和携带自定义 Java translet 的 TemplatesImpl 完成代码执行，不再依赖外部类加载。它先用延时载荷验证盲远程代码执行，再通过 JMX Catalina MBeans 与响应延时侧信道定位 Web 根目录，最终写入 WebShell。

防御仍未消失。该主机上的 Deep Security 会删除具有已知特征的 Behinder JSP 和 suo5 JSP。智能体于是对 JSP scriptlet 内容进行 Unicode 转义：Java 编译时会还原本义，但磁盘上的源码特征发生变化，从而绕过了该主机所使用的文件字符串特征检测。

**这四次改道才是事件的核心。**单个漏洞、脚本或隧道都不是新东西，新的观测点在于：智能体能够把拦截结果转化为下一步决策，而不是机械重复预设 playbook。

02 低频人工监督下的自主执行

Malbear Labs 将本次活动描述为 largely unsupervised intrusion activity，即大部分行动缺少人工监督。材料呈现出的是一种低频人工监督下的自主执行模式：操作者设定目标并检查结果，智能体完成其间的大量技术动作。

操作者的输入包括目标 CIDR 网段、“继续”“处理最新高危漏洞”“停止”，以及禁止触碰的三个内部 IP。更具体的 CVE、工具和利用方法由智能体选择。会话之间存在重叠，说明多个目标可以并行推进；操作者则可异步查看行动报告，再下达下一项目标。

框架内部有两类角色：

* 主智能体：维护主机、端口、漏洞、凭据、活动会话和待办事项等全局状态，并向工作智能体分派任务
* 工作智能体：承担单一任务，执行结束后将结果返回主智能体

会话索引显示，框架版本为 0.2.0-rc.2，模型标识为 deepseek-flash，提供方标识为 deepseek-official，上下文窗口为 100 万 token。长上下文用于维持长程行动状态，共享工作区则保留跨会话的主机、凭据和任务结果。两者结合，减少了重复侦察和重复验证。

“越狱”发生在提示词与编排层，不等于模型文件被篡改

每次会话开始时，框架都会注入一段约 7.8 万字符的系统提示词。它以公开的“Little Code Sauce（小码酱）”越狱模板为基础，删除原有角色扮演内容，增加约 400 行攻击性指令，并覆盖 21 类攻击性活动。

这段提示词将拒答定义为“故障”，同时抑制中英文拒绝话术，并要求越狱状态在整个会话中持续生效。提示词还把请求直接绑定到 WebShell、Shell 处理、内网扫描和浏览器自动化等技能模块。Malbear Labs 表示，在恢复的两周会话记录中，没有发现模型拒答或安全免责声明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq9pVaNDaK0UfkwQeZS8LqaElgibD6YXHQBoicYM1PG0YfuibvvTfWCfTOzI2M0ePm9icuQOuDWKPE7mQibialASR3xsHurojVpwBPiae0/640?wx_fmt=png&from=appmsg)

**图2｜操作者系统提示词注入片段**

图源：Malbear Labs《Operation Snowball: Inside an Autonomous AI Intrusion Campaign》

因此，这里真正失效的是“模型会拒绝危险请求”这一假设。智能体一旦拥有扫描器、浏览器、Shell、代理和凭据等工具，模型层的拒答就不能替代授权、隔离和审计。

工具链与激励机制都已工程化

框架的技能目录覆盖被动侦察、Nmap/Masscan 扫描、Nuclei 漏洞检测、Playwright 浏览器自动化、Impacket 横向移动、Sliver C2、Chisel/FRP/suo5 隧道，以及 Hydra、Hashcat、John 等凭据攻击工具。流量匿名化使用 VPNGate，工作区中包含 4000 余个中继节点，框架可按会话更换中继。

框架还内置了攻击计分机制。普通服务器管理员权限计 50 分，突破逻辑网络边界计 1000 分，安全设备管理平台的分值更高；工作区恢复时总分为 **3725 分**。该分数是攻击框架内部的任务激励，不是通用漏洞风险评分，但它清楚显示了对网段突破和集中管理设施的倾斜。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqibCHgJNUDr5MKJtq7LynyXbc8dJibrm7FYx8UE7tiaMqbqzQOiblqhs0WbibptFvxtw0bpXicX3yAJluyichdBOHFqWRN6cuMKicXA0ws/640?wx_fmt=jpeg)

**图3｜人机协作与智能体框架运行流程**

图源：根据 Malbear Labs 公开研究整理绘制。

03 从运营商入口到医疗数据库：攻击链如何闭合

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqickoythIBRic7mfreJQKehWO20BCPXwgbvTDYq1CKdgdn39PaBYcxB2o9mlblsOdCFXusN2UxBB1MDJgDU6ib53IPA4sqMrgjheg/640?wx_fmt=png&from=appmsg)

**图4｜雪球行动端到端攻击链：从运营商入口到医疗数据库**

图源：根据 Malbear Labs 公开研究及 Cisco 安全公告整理绘制。

第一步：通过 BroadWorks XXE 进入运营商环境

电信运营商基础设施中的主要目标是 Cisco BroadWorks XSP（Xtended Services Platform），版本为 23.0.1.1075，相关服务运行在 2208 端口。

智能体利用 CVE-2026-20320，一个 BroadWorks OCI XML 解析器中的未认证 XXE 漏洞，读取服务器文件。Cisco 的公告说明，该漏洞源于默认允许外部实体解析，未经身份验证的远程攻击者可构造 XML 消息，以 BroadWorks 用户权限查看敏感文件。

会话材料显示，智能体从 XSP 主机获取了系统身份私钥、三组 SSL 凭据以及另外三把与证书匹配的私钥。其中，系统身份私钥用于 BroadWorks 组件间认证，持有该密钥可能冒充 XSP 参与组件通信。

第二步：利用老旧 JBoss/RichFaces 建立第二个立足点

进入内部网络后，智能体发现一台 JBoss AS 6 主机，并利用 RichFaces 的 CVE-2013-2165 反序列化漏洞执行系统命令，随后写入 Behinder JSP WebShell。

这是发生在内网横向移动阶段的第二次独立利用，不是 BroadWorks 初始入口的重复描述。它使智能体在更深处获得了新的执行点。

第三步：借助管理代理、JMX 与脚本链扩大控制

BladeLogic RSCD 在本次活动中承担了重要的内部执行通道。相关连接被映射到本地 Administrator 账户，使智能体能够在部分 Windows 主机上获得 SYSTEM 级访问，并向其他内部主机传递工具。

另一条路径来自未正确配置认证的 JMX 接口。智能体利用 MLet MBean 加载位于同一主机暂存路径的 Java 类，获得第二条操作系统命令执行路径，该路径随后被用于 sudo vi 提权。

在医疗机构的 Active Directory 环境中，智能体还枚举了域管理员、SPN 以及与 OLLAMA、LLM、JUPYTER、GPU 等关键词匹配的主机名，并通过卷影复制/IFM（Install From Media）方式导出域控制器的 NTDS 数据库、SYSTEM 配置单元和相关注册表文件，以便离线处理域凭据。其清理脚本随后删除这些输出和载荷文件。

第四步：通过中间主机和 JDBC 触达 TrakCare Oracle 9i

医疗数据访问并非直接使用 BroadWorks 漏洞完成，也不是整个运营商入侵的初始入口。

目标是一套运行在 AIX 上的 TrakCare Oracle 9i 数据库，当前立足点无法直接访问。智能体先将 Oracle Type 4 JDBC 驱动暂存到一台已失陷中间主机，再通过 BladeLogic RSCD 执行路径将其转移到第二台内部主机，最后从该主机建立 SQL 层数据库连接。

连接使用默认数据库凭据并获得 DBA 权限。材料显示，该会话能够访问三个模式命名空间中的数百万条患者记录、疫苗接种登记和医疗预约数据。

因此，**BroadWorks XXE 是运营商入口，TrakCare 默认口令是后续医疗数据库访问条件，两者不能混写为同一个入口事件。**

第五步：以多套 C2 与隧道维持访问并转移数据

后渗透 C2 使用 Sliver v1.7.8，并通过 Cloudflare 前置；信标域名为 api.tablacysexplorer[.]com，端口为 443。Sliver team server 仅监听本机 127.0.0.1:31337，操作者通过另一台主机的 SSH 隧道访问，而不是将 team server 直接暴露到互联网。

![](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOq8fRpGEFVnXSwco58TNAssicfztky3gHGguA6Es5DymteGj4u6sAiaqA4VCRy6M7v3dxxBRI1QW0hWOmbhgOaAYtelSb6KzGs3VQ/640?wx_fmt=jpeg)

**图5｜C2、SSH 与多套隧道的连接关系**

图源：根据 Malbear Labs 公开研究整理绘制；地址已按 IOC 防直接点击格式展示。

框架还准备了 Chisel HTTP/WebSocket 隧道、suo5、定制 Perl 桥接以及在失陷主机上编译的 swgp-go WireGuard 混淆代理。Windows TCP 中继则先连接框架主机的 21 端口，再根据收到的目标地址建立第二条 TCP 连接并转发流量。开放工作区中发现的凭据缓存和数据库转储，证明至少部分数据已被集中到攻击者控制的工作环境。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqicJp3Tk03HIdXGUZKRQznT415xpwZP8Ah6dUm9EnN7vCxyWGvchGicYb53a8ibBCMGlNKOjp88GNicn5gMLRJS0BGPCSRPjz1CKAc/640?wx_fmt=png&from=appmsg)

**图6｜PowerShell 中继启动脚本**

图源：Malbear Labs《Operation Snowball: Inside an Autonomous AI Intrusion Campaign》

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqicQtWXQg27RVQ0kRxq0SxmLhT4SIPBGia2iaAMYpoN9FxTfjue7nOdF8NLtnWr2Ju2k9ZhX0ykibYj7O1darLzmStw0VELblWCW4o/640?wx_fmt=png&from=appmsg)

**图7｜Base64 解码后的 TCP 中继**

图源：Malbear Labs《Operation Snowball: Inside an Autonomous AI Intrusion Campaign》

04 影响范围：从运营商控制面延伸至医疗与托管机构

Malbear Labs 根据工作区、会话记录和智能体报告，给出了以下活动规模：

|  |  |
| --- | --- |
| 维度 | 材料所记录的情况 |
| 侦察范围 | 枚举数百项资产，其中多数确认存活；记录数百个开放端口，标记 100 余个漏洞 |
| 凭据与密钥 | 提取数十组凭据；从 BroadWorks 获取系统身份私钥及多组 SSL 凭据、私钥；另有一把电信运营商子域名的 RSA 私钥被外传 |
| 电信业务数据 | 从内部计费平台提取数千行用户计费和设备记录 |
| 医疗数据 | 通过 TrakCare Oracle 默认凭据获得 DBA 访问，可触及数百万条患者、疫苗接种和预约记录 |
| 医疗环境与人员凭据 | 从一家失陷的第三方医疗软件供应商处收集数十组员工凭据；在医疗机构域控制器上执行 NTDS 导出 |
| 监控配置 | 获取约 80 份 Zabbix .zbc-list 备份配置，涉及同一托管基础设施上的外部机构 |
| 后续目标 | 智能体依据公开 RIPE 记录整理出 13 家使用该运营商托管基础设施的机构清单 |

这些材料呈现出一条清晰的扩散路径：攻击者先取得运营商环境中的执行能力和认证秘密，再借助管理代理、内部服务与多套隧道向更深处推进，最终触达医疗数据库、域控制器和托管机构的监控配置。其影响因此不只是一次单点 Web 漏洞利用，而是对共享基础设施及其信任关系的连续穿透。

其中，数百万条医疗记录对应智能体获得 DBA 权限后的可访问范围；已经明确披露提取动作的是数千行电信计费和设备记录。13 家机构则来自智能体依据 RIPE 信息整理的后续目标清单，公开材料尚未逐一确认其失陷状态。

成功路径同样需要与工具储备区分开来。BroadWorks、JBoss/RichFace...