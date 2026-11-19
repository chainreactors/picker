---
title: 【安全速报】11月18日高危漏洞紧急预警
url: https://mp.weixin.qq.com/s/zgpPw5j363nLGtWYUscXUA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:51.467234
---

# 【安全速报】11月18日高危漏洞紧急预警

# 【安全速报】11月18日高危漏洞紧急预警

探知安全
探知安全

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 【安全速报】11月18日高危漏洞紧急预警

2026年11月18日  |  探知安全

今日焦点

本期六条串起来是同一件事——**"补丁时钟"已经彻底跑不过"攻击时钟"**。头条 **Java4Shell（CVE-2026-114938）** 把这件事量化到了具体数字：Oracle Java SE 与 GraalVM 的 **Base64 解码器**存在堆越界写，**64 个字母 A 加一个等号**就能让 JVM 把 64 字节写进只该放 2 字节的缓冲区、**62 字节落在数组之外**；发现方 **Calif.io** 的研究员 **Quang Luong** 用 OpenAI Codex **约 1 小时找到、2 小时写出可用利用、全部 token 成本不到 200 美元**，并在 **Keycloak、Jira、Confluence、Artifactory、Jenkins、PingFederate** 上确认了**未授权远程代码执行**。第二件必须看的是 **Perforce Puppet Enterprise（CVE-2026-115731）**，**11 月 17 日刚进 CISA KEV、联邦截止日 12 月 1 日**：报告处理代码里的反序列化让**任何一张 CA 签发的 agent 证书**都能在 Puppet Server 上以服务账号执行命令，而**开了 autosign 的部署等于把证书白送**——拿到的是 CA 私钥，**改一次就是整个机群的命令执行**。第三条是 **WP Duplicate 插件（CVE-2026-123751）**：**已在野利用、没有修复版、11 月 9 日被 WordPress.org 目录下架**，唯一处置是**删插件**。另外三条：**Oracle 11 月 CPU 一次放出 955 条 CVE、其中 6 条 10.0**；**DrayTek Vigor2960 一个文件里五个洞**；**LibreOffice 打开文档就能执行代码且 PoC 已公开**。**Google 威胁情报组 11 月 16 日的报告把背景讲透了**：攻击者已经在用名为 `exploit_agent` 的多智能体框架**读补丁、做差分、自动写利用并直接对真实站点开火，全程无人参与**——所以排查顺序应该是**先按"补丁到利用只差几小时"排公网 Java 与 Puppet，再按"根本没有补丁"排 WordPress 插件**。

## 漏洞详情

严重CVE-2026-114938CVSS 8.1

### Java4Shell：Java 运行时的 Base64 解码器堆越界写，未授权 RCE 已在六个企业级产品上验证（CVSS 8.1·Oracle 官方口径 / 9.2·CVSS 4.0 研究方口径·11/17 Oracle CPU435·CISA 当日发告警）

Oracle 在 **11 月 17 日**随 CPU435 一起修掉了 Java SE 的一条内存破坏漏洞，CVE 记录把它归在 **component: Compiler**，**CWE-122 堆缓冲区溢出**。机理不复杂但极精准：HotSpot 的 C2 编译器用 **AVX-512 intrinsic** 手写汇编来加速 Base64 解码，**处理补位尾部的那段汇编把输出长度算错了，得到 -1**，写掩码因此被完全打开——**该写 2 字节的地方写了 64 字节，其中 62 字节落在输出数组之外**。Java 随后会察觉输入非法并抛异常，**但写入已经发生**。触发载荷小得离谱：**64 个 A 加一个 =**（Java 17 上是 128 个 A 加一个 =），而且**解码器必须先被 JIT 编译过**，所以需要一点预热流量。

**写出去的字节是固定的**——攻击者能选**写在哪里**，不能选**写什么**。Calif 的做法是借用 JavaScript 引擎挖掘里的经典堆布局技巧：**先用固定写覆盖邻近数组的长度字段**，得到一个能接受任意字节的写入器，**再做一次同样的操作得到读取器**；**写入器加读取器 = Heartbleed 式堆信息泄露 = 通往代码执行的路**。这解释了为什么早期实验室复现只看到"崩溃"、甚至有研究者据此认为 RCE 无法证明：**他们缺的是堆布局，不是漏洞**。Calif 最终在默认配置的 **Keycloak、Atlassian Jira、Atlassian Confluence、JFrog Artifactory、Jenkins、PingFederate** 上确认了**未授权（pre-auth）RCE**，在 **Kafka Broker、Solr、Elasticsearch、Gerrit、Spinnaker** 上确认了需登录的 RCE，并说 Struts 与 Spring Boot 的示例应用同样成立。

**受影响范围比"Java 应用"这个说法窄得多，也宽得多**：Oracle 官方列出的受影响版本是 **Oracle Java SE 8u511b33-perf、17.0.21.0.3、21.0.13.0.3、25.0.5.0.3、27.0.1.0.3**，**GraalVM for JDK 17.0.21.0.3 与 21.0.13.0.3**，**GraalVM Enterprise Edition 21.3.20.0.3**。**但真正的判定条件是硬件**：漏洞代码只在 **x86-64 且支持 AVX-512 VBMI 的 CPU** 上执行（Intel Ice Lake、Sapphire Rapids、Emerald Rapids、Granite Rapids，AMD Zen 4 及以后），**ARM64 不受影响**，**Java 11 与标准版 Java 8 不受影响**（**Oracle 只把 Java 8 的性能版 8u511b33-perf 列为受影响**）。所有下游发行版都继承同一份代码：**Amazon Corretto、Eclipse Temurin、Microsoft Build of OpenJDK、Azul Zulu、BellSoft Liberica、SAP SapMachine、Red Hat OpenJDK、Oracle OpenJDK / Java SE、Oracle GraalVM for JDK**——**11 月 17 日 20:00 UTC 时 Temurin、Corretto、Zulu 的修复构建仍未到位**。Calif 说这套运行时覆盖**约 90% 的财富 500 强**。

**CVSS 口径要写清分歧**：Oracle 给的是 **CVSS 3.1 8.1**（`AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`，**`AC:H` 是关键——Oracle 认定它"难以利用"**），研究方 Calif 给的是 **CVSS 4.0 9.2**。**分歧点就在利用复杂度这一项**：Oracle 认为需要苛刻条件，研究方在六个企业级产品的默认配置上直接拿到了未授权 RCE。**防守按后者理解更安全**。**本条未进 KEV，无在野利用报告**。

时间线值得逐分钟看：**11 月 12 日** Oracle 的预发布通告列出 11 条 Java SE 修复、全部可远程未认证利用、最高 8.1，**当时还没有 CVE 编号**；**11 月 17 日上午 10:22** 讨论内容已在 X 上泄漏，**17:44 UTC** OpenJDK 通告列出 CVE-2026-114938，**17:53 UTC** CISA 放出的 KEV 目录里**还没有它**，**20:00 UTC** 有实验室公开复现溢出但称 RCE 未获证明，**21:00 UTC** Calif 发布完整技术报告并放出多产品 RCE 演示。**CISA 同日发出紧急告警并给出 5 条 IOC 条目**（由加拿大网络安全中心共同署名），明确要求**优先处理面向互联网的系统**，同时点出一句要命的话：**JDK 与 Java 运行时可能根本不会作为独立条目出现在你的软件清单里**。

影响范围

Oracle Java SE **8u511b33-perf、17.0.21.0.3、21.0.13.0.3、25.0.5.0.3、27.0.1.0.3**；Oracle GraalVM for JDK **17.0.21.0.3、21.0.13.0.3**；Oracle GraalVM Enterprise Edition **21.3.20.0.3**。**判定必须同时满足版本与硬件**：x86-64 且 CPU flags 同时具备 `avx512f`、`avx512bw`、`avx512vbmi`、`bmi2`（Intel Ice Lake / Sapphire Rapids / Emerald Rapids / Granite Rapids、AMD Zen 4+）；**ARM64 不受影响，Java 11 与标准 Java 8 不受影响**。所有基于 OpenJDK 的下游发行版均在范围内。

**修复建议：**升级到 **Oracle Java SE 8u513、17.0.21.1、21.0.13.1、25.0.5.1、27.0.1.1**（补丁可用性文档 **CPU435**），**Temurin / Corretto / Zulu / 发行版包要向各自厂商确认对应修复构建**。**发行版通过 apt/yum 装的 Java 会随发行版更新走，但容器镜像与厂商定制 JDK 不会自动更新，必须重建镜像并重新部署**。**不能立刻打补丁时**：JVM 启动参数加 **`-XX:-UseBASE64Intrinsics`** 可在所有受影响版本上止住溢出；`-XX:UseAVX=2` 也有效但会关掉全部 AVX-512 路径且**在 ARM 主机上启动失败**，只能用于 x86-64；**两者都需要重启 JVM**。**不要用 `-XX:DisableIntrinsic=_base64_decodeBlock` 走 `JAVA_TOOL_OPTIONS` 全网下发**——它必须配合 `-XX:+UnlockDiagnosticVMOptions` 才生效，缺一个就直接启动失败，**这是自己制造的停机**。**Oracle 自己给的通用变通方案是"阻断该攻击所需的网络协议"，但它同时警告本漏洞的协议是"Multiple"、阻断可能破坏业务功能**。**检测**：在 `Authorization` 头等位置找**长度不是 4 的倍数、以 = 结尾且长度不小于 32 的 Base64 字符集 token**；应用日志里每次尝试都会出现 `IllegalArgumentException: Input byte array has wrong 4-byte ending unit`；JVM 崩溃会留下 `hs_err_pid*.log` 与 SIGSEGV 集群。**回溯从 11 月 17 日之前开始查，别只查今天**。

满分CVE-2026-115731CVSS 9.9

### Puppet Server 报告反序列化：一张 CA 签发的证书就能拿下配置管理平面（CVSS 9.9·Oracle 官方 / 9.4·CVSS 4.0 厂商口径·CWE-94/CWE-502·11/17 入 KEV·联邦截止 12/01）

CISA 于 **11 月 17 日**把 **Perforce Puppet Enterprise** 的这条洞收进 KEV，**联邦强制整改截止日 12 月 1 日**，勒索软件使用情况标记为 Unknown。NVD 记录显示它 **11 月 3 日**就发布过、状态 Analyzed，**11 月 17 日**做了最后修订。机理在 Puppet Server 的**报告处理**环节：Agent 每跑完一次就往服务器发一份 JSON 报告，服务器用 **FromDataConverter** 把报告里的每个 event 还原成 Ruby 对象，而还原过程**认 `__ptype` 这个键**。攻击者只要在 `__ptype` 里塞进一整份 **Pcore 对象类型定义**，并在其中挂一个 **RubyMethod 注解**——该注解的 body 字符串会被**拼进一个动态生成的类体**、再交给 **`class_eval`** 执行。**Ruby 在类体定义时就会执行反引号里的命令**，所以服务器解析报告的那一刻，命令就已经以 **puppet 服务账号**的身份跑起来了。

**这条洞最狠的地方在它的"前置条件"其实常常不存在**。报告接口需要一张**由 Puppet CA 签发的 agent 证书**，向量因此是 `PR:L`。但 Neodyme（发现方）与 OpenVox 都指出：**大型 Puppet 部署普遍开着 autosign**——新 agent 自助注册、CA 自动签发、不做人工审批也不做强校验；Satellite 与 Ansible 这类开通工具更是依赖它。**在 autosign 配置下，任何能连到 8140 端口的人都能自己申请一张证书**，前置条件直接蒸发。Neodyme 的原话是大多数大公司都开着 autosign。**更严重的是后果的放大**：以 puppet 身份执行代码后**能读到 CA 私钥**，拿到私钥就能签发带 serverAuth 与 clientAuth 扩展用途的证书、**冒充任意节点**；而 Puppet 本身就是配置管理工具，**能向机群里每一台被管主机下发命令**——**一份精心构造的报告，等于一次全机群代码执行**。

**同期还有一个必须一起修的洞**：**CVE-2026-115732（CVSS 4.0 9.0）**，位于执行 `auth.conf` 的 **trapperkeeper-authorization** 库，其**精确主机名规则被写成了前缀通配匹配**，导致 `evil.target.example.com` 的证书能通过为 `target.example.com` 写的规则。**两个洞在同一批版本修复，处置上按一个补丁对待**。

**必须点名一个版本号陷阱**：**Puppet 官方 What's New 页面把 8.x 的更新标为 8.22.1，但它链出去的 release notes 是 8.22.2 的**，而**真正列出 CVE-2026-115731 修复的是 8.22.2 这个构建**；NVD 把 8.22.2 之前的版本全列为受影响，**Red Hat 的缓解指引同样点名 8.22.2**。**照抄 8.22.1 会漏掉修复**。**还有一个"装完不生效"的坑**：漏洞代码位于**服务器本机安装的 agent 包里的 Ruby 报告处理器**——**只升级服务器上的 agent 包、或自己 restart puppetserver，旧代码仍然加载在内存里**。**这一条洞的发现方 Neodyme 是在准备红队演练时挖到的**，10 月报给 Perforce 与 OpenVox 项目，**修复于 11 月 3 日发布**，**公开 PoC 在进入 KEV 之前就已经流传**。

影响范围

**Puppet Enterprise 2023.8.0 至 2023.8.13 之前、2025.0.0 至 2025.12.1 之前、2026.0.0 至 2026.0.1 之前**；**Puppet Core 早于 9.1.3 与 8.22.2**；**OpenVox agent 早于 9.3.0 与 8.32.0，OpenVox Server 与 OpenVoxDB 早于 9.2.0 与 8.18.0**。**开源 Puppet 与 Puppet Server（包括 RubyGems 上 `puppet` gem 的全部版本至 8.10.0）不会得到修复**——Neodyme 在 **2021 年 7 月的 6.24.0** 上就确认了 RCE。**Red Hat Satellite 默认处理客户端报告，同样受影响**。

**修复建议：**升级到 **Puppet Enterprise 2023.8.13 / 2025.12.1 / 2026.0.1**，**Puppet Core 8.22.2 或 9.1.3**（**注意是 8.22.2，不是官方页面上写的 8.22.1**），**OpenVox Server 8.18.0 或 9.2.0，OpenVox agent 8.32.0 或 9.3.0**；**开源 Puppet 用户没有补丁，只能迁移到 OpenVox 或 Puppet Enterprise**。**升级完必须重启 puppetserver 服务**，否则旧版 Ruby 报告处理器仍在内存里跑。**在升级之前先做这一步**：查 `puppet config print autosign --section server`，若为 `true`（朴素自动签发，**CA 签所有请求**）或存在 `autosign.conf` 里的通配条目（如 `*.example.com`，**任何挑到一个未用匹配名的主机都能拿到证书**），**先关掉 autosign 或改成强校验的策略脚本**——**OpenVox 官方文档把 basic autosigning 直接称为"essentially insecure"**。**同时把 8140 端口与 `PUT /puppet/v3/report` 限制到已知 agent 网段**。**取证**：查 `/var/log/puppetlabs/puppetserver/puppetserver-access.log` 里带 `__ptype` 的异常 PUT 请求、**puppetserver 进程派生的 shell 或非常规子进程**、以及**你不认识的主机发起的证书签发请求**；**厂商未发布任何 IoC**，只能靠行为判断。**一旦确认被利用，按 CA 已失陷处理：重建 CA、重新签发全部 agent 证书**。

严重CVE-2026-123751CVSS 9.8

### WP Duplicate 未认证任意文件写入：已在野利用、无修复版、插件已下架（CVSS 9.8·CWE-434·WPScan 披露·WordPress.org 11/09 下架）

WPScan 作为 CNA 提交的记录写得直接：**"WP Duplicate"插件 1.1.11 及之前版本没有正确校验请求的认证值，也没有校验上传文件的路径或类型**，因此**未认证攻击者可以向服务器写入任意文件并实现远程代码执行...