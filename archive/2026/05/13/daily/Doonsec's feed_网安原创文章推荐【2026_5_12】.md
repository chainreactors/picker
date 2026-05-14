---
title: 网安原创文章推荐【2026/5/12】
url: https://mp.weixin.qq.com/s/TQ7SQeH8SyEo4Vg1c7sXEQ
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:45:05.868069
---

# 网安原创文章推荐【2026/5/12】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJABCdvWpwT0fgmyiaic1aApicBGQMXAic7KFGUNI7LS7ePpaNlr2ljIsMZ5IG28MfKEMzwsAJ7mNAZhtNBZqM18iaZ6Nnge6C9c0glXc/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/5/12】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-05-12 微信公众号精选安全技术文章总览

> 洞见网安 2026-05-12

---

### 0x1 [Grav CMS 组合拳漏洞| CVE-2026-42613&CVE-2026-42607复现&研究](https://mp.weixin.qq.com/s?__biz=MzE5ODMzOTgwMg==&mid=2247484548&idx=1&sn=ca90da6ec1332e0ba8f3dd98d904ae38&scene=21#wechat_redirect "Grav CMS 组合拳漏洞| CVE-2026-42613&CVE-2026-42607复现&研究")

> 404号浪漫 2026-05-12 22:14:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/eefCd8vibaic2yiaa5BDhv7SezcKcBsjT2RBxE2jFHrD4ZMpH4jZcBAP8GEltmB58Jkc68KGBpX8Wymnk7UjVAibO5Hwu7utoxiaCYM8kHMEX1ic4/640?wx_fmt=jpeg)

Grav是一个基于文件的Web平台，在2.0.0-beta.2之前的版本中存在两个高危漏洞，可导致组合利用。第一个漏洞是权限提升漏洞（CVE-2026-42613），由于Login插件在处理用户注册请求时未对请求数据中的groups/access字段进行服务端校验，攻击者可以通过构造带有恶意参数的注册请求，直接创建拥有超级管理员权限的账户，实现未授权权限提升。第二个漏洞是远程代码执行漏洞（CVE-2026-42607），由于Grav管理后台的“直接安装”功能在解压用户上传的ZIP插件包时未进行任何安全检查，攻击者可以上传包含恶意PHP代码的合法结构插件ZIP包，其中的PHP文件会随Grav的插件初始化事件自动执行，从而在服务器上写入Webshell或执行任意系统命令，最终获得服务器控制权。文章详细分析了漏洞的原理，包括架构与模块定位、关键路径锁定、逻辑缺陷等，并提供了修复建议，包括升级到最新版本、临时防护措施等。

---

### 0x2 [空密码后台 → SQLite 落地 Webshell → 内核 CVE-2026-31431 root](https://mp.weixin.qq.com/s?__biz=MzYzNjgwNDg3Mg==&mid=2247483815&idx=1&sn=f718b476026be9106fad60fdb971bbf0&scene=21#wechat_redirect "空密码后台 → SQLite 落地 Webshell → 内核 CVE-2026-31431 root")

> YMs0ra的安全漫路 2026-05-12 21:53:05

![](https://mmbiz.qpic.cn/mmbiz_jpg/SPfHPOgCrHrJOhO0IoWPrct1Pib0CsZkvs5ghiaW6J9Newl3dic27FOfLEoicnRUFJQv0Gyb8EQsjCsojnFEdwva6Ihmz4SqjHiaeaO4Ns2QrFfo/640?wx_fmt=jpeg)

该文章描述了一个基于Docker的Web应用程序，其中包含一个SQLite数据库和Apache服务器。应用程序使用PHP进行后端处理，并通过Rewrite规则将大部分请求重定向到main.php。审计发现，该应用程序存在一个管理界面，可以通过传递参数/mange?p=来访问，而无需密码验证。这是因为管理密码被硬编码为空。该管理界面允许用户在CONFIG表中插入、删除和更新记录。通过在CONFIG表中插入PHP代码，攻击者可以执行远程代码执行（RCE）。虽然PHP环境受到限制，但可以通过挂载服务器目录来绕过这些限制。此外，应用程序中的Go程序存在一个漏洞，可以通过触发panic来重启服务，这可能导致提权。提权阶段，由于PR\_SET\_NO\_NEW\_PRIVS的限制，直接su提权不可行。攻击者需要利用内核漏洞（如CVE-2026-31431）来进行提权。

---

### 0x3 [蚁剑最新高危漏洞分析：为什么一个“终端输出”最后变成了客户端 RCE？](https://mp.weixin.qq.com/s?__biz=MzI5NDg0ODkwMQ==&mid=2247487801&idx=1&sn=04de9283bdbd00f8045a22fab9eec0a1&scene=21#wechat_redirect "蚁剑最新高危漏洞分析：为什么一个“终端输出”最后变成了客户端 RCE？")

> 六边形攻防安全 2026-05-12 20:33:50

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FaZFJ7xrqJbibibkHV7uJF1PQMl1LjWeT7IPknjjePLFDtm6lhIdh5XPLSGGGDaJEbzrffQ1jwjIYSjicjxEEOa76ZdUe3X18ROx6wsM3Nsyeo/640?wx_fmt=jpeg)

本文详细分析了AntSword v2.1.15版本中的一个高危漏洞，该漏洞最终导致客户端本地命令执行（RCE）。漏洞源于终端模块对服务端返回内容进行二次解析时，过滤函数未完全过滤特殊格式，使得攻击者可以通过构造特定的恶意内容，在客户端执行本地系统命令。该漏洞的关键在于Electron环境下的XSS攻击可以转化为本地RCE。文章还提到了恶意服务端反向攻击客户端的可能性，以及恶意WebShell可能利用此漏洞进行攻击。此外，文章强调了类似问题在Markdown渲染、富文本编辑器、聊天系统等场景中的普遍性，并指出Electron、富文本和Node.js权限组合本身具有潜在的高危性。尽管该漏洞已修复，但它暴露出的安全问题值得深入学习和关注。

Web安全

漏洞分析

客户端安全

漏洞修复

安全漏洞

恶意代码

安全工具

编程语言安全

---

### 0x4 [链锁裂变｜TeamPCP 供应链攻击劫持 guardrails-ai，七模块凭据收割全景分析](https://mp.weixin.qq.com/s?__biz=MzI5ODk3OTM1Ng==&mid=2247511898&idx=1&sn=55cf5a7445b1796c68e2649152e4d592&scene=21#wechat_redirect "链锁裂变｜TeamPCP 供应链攻击劫持 guardrails-ai，七模块凭据收割全景分析")

> 腾讯安全威胁情报中心 2026-05-12 20:18:36

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jHUbrwW0VwWSZbOzFqfPJTI0agSQzI3VZibnw7er6pgREJCYseibd8b4ib7UOwTpeGUbHZKXCZjF70JRdNo6AWw4jSTa5IQ9V3b90NZiaD8UG3w/640?wx_fmt=jpeg)

2026年5月12日，腾讯安全威胁情报中心发现知名LLM防护框架guardrails-ai的异常版本更新，确认为TeamPCP组织的供应链攻击。攻击者在合法包入口文件末尾追加14行代码，静默下载并执行23KB的Python zipapp载荷。载荷内含7个并发凭据收割模块，覆盖AWS、Azure、GCP、Kubernetes、HashiCorp Vault、密码管理器及90个敏感文件路径，同时具备条件性系统擦除与systemd持久化能力。该攻击利用PyPI平台发布恶意版本，通过伪装合法服务和沙箱规避技术，窃取大量敏感凭据并可能对系统进行破坏。攻击者还利用GitHub平台进行数据回传，并针对特定地理位置的系统触发条件性擦除。建议开发者和企业安全团队检查受影响版本，轮换凭据，并加强供应链安全防护。

---

### 0x5 [【免杀神器】morphkatz](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485430&idx=1&sn=471a6e92b7dafc9a5e8f413cbea1d8ad&scene=21#wechat_redirect "【免杀神器】morphkatz")

> 安全天书 2026-05-12 19:59:29

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQVhu1sib1M6teZGbXkHqcE1xEfz6ga4wmd3KJU4Ome6LukbrsoZicwWMAdGL4CUcfBtDXFLevfQcLibm6DZvbTFgwicFm4icibaoOdsU/640?wx_fmt=jpeg)

本文介绍了一种名为MorphKatz的工具，该工具能够在PE可执行文件和原始shell代码中重写x86-64机器码，使其成为字节不同但语义相同的等价物，以此破坏字节模式检测，如YARA规则、Defender签名、弹性规则和Sigma检测内容，而不改变代码的实际功能。MorphKatz由Mohammed Abuhassan编写，是一个多面手的PE重写器，适用于Windows x64系统。文章中提供了MorphKatz的用法示例，包括比较、扫描和报告生成等操作。同时，文章也强调了该工具的使用仅限于安全测试和防御研究，禁止用于非法入侵或攻击他人系统。此外，文章还提到了一个专注于渗透测试、红蓝对抗、钓鱼手法思路、武器化以及红队工具二开与免杀的安全圈子，并介绍了该圈子的一些相关技术和工具。

网络安全工具

免杀技术

PE文件分析

安全测试

Windows安全

代码混淆

红队工具

免杀对抗

---

### 0x6 [针对 Windows 11 的新型 BitUnlocker 降级攻击可在 5 分钟内访问加密磁盘](https://mp.weixin.qq.com/s?__biz=Mzg4ODI5MzAzMw==&mid=2247486887&idx=1&sn=fb3423d9cef1cbb31b1b4d4799f8c3e7&scene=21#wechat_redirect "针对 Windows 11 的新型 BitUnlocker 降级攻击可在 5 分钟内访问加密磁盘")

> 安全圈的那点事儿 2026-05-12 19:22:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PA3Pem5ic2p85cFHl5zdDURyJPpU2d5wIEiatA2aFYAQ7VLub4LAaUiajzgEuOODwvfac1Y4gNnY9f2OXwPK8gpONBWnrPjrMmVk/640?wx_fmt=jpeg)

一款名为BitUnlocker的新工具揭示了针对微软BitLocker加密的降级攻击方法。攻击者利用CVE-2025-48804漏洞，在5分钟内通过物理访问解密已打补丁的Windows 11计算机上的加密卷。该漏洞存在于Windows恢复环境(WinRE)中的系统部署映像(SDI)文件机制。攻击依赖于未撤销的旧版Microsoft Windows PCA 2011证书，即使系统已安装补丁。攻击者只需物理访问目标计算机，使用USB或PXE启动，即可在未经用户交互的情况下解密BitLocker卷。微软建议采取的措施包括启用TPM+PIN预启动身份验证、部署KB5025885更新、验证启动管理器证书，以及删除WinRE恢复分区以减少攻击面。

Windows 11 安全漏洞

BitLocker 加密

物理安全攻击

零日漏洞

降级攻击

安全启动

证书管理

补丁管理

安全研究

安全漏洞利用

---

### 0x7 [PHP SOAP 扩展存在严重漏洞，可导致远程代码执行攻击](https://mp.weixin.qq.com/s?__biz=Mzg4ODI5MzAzMw==&mid=2247486886&idx=1&sn=251a6108872ea12d0d72361404bc89f0&scene=21#wechat_redirect "PHP SOAP 扩展存在严重漏洞，可导致远程代码执行攻击")

> 安全圈的那点事儿 2026-05-12 19:13:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PLVkGFBpVyv5h5BaqRAzNrM3FMGsxDJOrQXSZBwBW3DKKHpRSWtfKnFYyOwKIXH5yQmJQPIJDZ3S0Mhlc8lAYa6P6jiaP3grtk/640?wx_fmt=jpeg)

PHP SOAP 扩展被发现存在严重漏洞，编号 CVE-2026-6722，该漏洞允许未经身份验证的远程代码执行攻击。这个漏洞是由于扩展处理 XML 图中的对象去重方式不当，导致内存损坏。攻击者可以通过 Apache 映射机制利用这一缺陷，从而实现远程代码执行。此外，PHP 安全团队还修复了四个中等严重程度的漏洞，包括一个 SoapServer 的释放后使用问题，一个 Apache Map 节点解码过程中的空指针解引用漏洞，一个原生 urldecode() 函数的越界读取漏洞，以及一个 mbstring 扩展的全局缓冲区溢出漏洞。这些漏洞影响多个 PHP 版本，包括 PHP 8.2.31、8.3.31、8.4.21 和 8.5.6 之前的版本。建议管理员立即更新 PHP 环境，以避免安全风险。

远程代码执行 (RCE)

内存损坏漏洞

Web服务器安全

PHP安全

软件补丁

CVE编号

拒绝服务攻击 (DoS)

信息泄露

---

### 0x8 [Apache Tomcat Tribes EncryptInterceptor 加密绕过反序列化漏洞分析（CVE-2026-34486）](https://mp.weixin.qq.com/s?__biz=Mzg4NzE2MjM0OA==&mid=2247484624&idx=1&sn=12a258fbdc7c6ffddac46163e66d9631&scene=21#wechat_redirect "Apache Tomcat Tribes EncryptInterceptor 加密绕过反序列化漏洞分析（CVE-2026-34486）")

> ap0s 2026-05-12 17:16:34

![](https://mmbiz.qpic.cn/mmbiz_jpg/hYTcBbYGXIcCvAsVhicwzXwTbbZicmMNRicNANXrGJlCu2ibFCbum7gZz7cv6ibVgx599yPHpwJpdvrDKRZTrbXPze38eZcJkIaXdccnm85G6Rsc/640?wx_fmt=jpeg)

Apache Tomcat Tribes EncryptInterceptor 加密绕过反序列化漏洞（CVE-2026-34486）分析摘要：Apache Tomcat Tribes 是 Tomcat 内置的集群通信框架，用于多台服务器之间的可靠消息传递和节点发现。当启用 EncryptInterceptor 时，Tribes 之间的消息传输会通过 Java 序列化机制进行加密。该漏洞源于官方在修复 CVE-2026-29146 时引入的 Bug，导致即使解密失败，加密的消息也会被继续转发并反序列化。攻击者只需具备对 Tribes 接收端口（默认 4000）的网络访问权限，即可发送未加密的 Java 反序列化 payload，绕过 EncryptInterceptor 的保护，实现远程代码执行。影响版本包括 Apache Tomcat 9.0.116、10.1.53 和 11.0.20。利用条件包括 server.xml 中显式启用 Cluster、Channel 配置 EncryptInterceptor、Tribes 接收端口对攻击者可达以及 classpath 中存在可用的反序列化利用链。通信过程中，EncryptInterceptor 在解密失败后未终止处理流程，导致原始字节流被转发并反序列化。攻击者通过构造类似 Tribes 包的明文数据，包含恶意序列化数据，直接发送到目标端口即可利用该漏洞。

---

### 0x9 [注释写着\"需要认证\"，代码说\"不\"——CVE-2026-42864 未授权 SSRF 导致 AWS 凭据窃取](https://mp.weixin.qq.com/s?__biz=MzYyMTk5NjY2Ng==&mid=2247486961&idx=1&sn=8219c069042941bde418d5c1e5ca8e43&scene=21#wechat_redirect "注释写着\")

> CVE-SEC 2026-05-12 14:00:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/uibDXjFsesAO5mrqcm8gnbrpULSqsCgnIcE69uK22Sohicnaub8qPBqYEj7ZXiaa8cLiamy32yiaic6fLFufLcWu9LfUx01w8PUL7yvicKiboRvT4ibw/640?wx_fmt=jpeg)

CVE-2026-42864 是一个严重的云安全漏洞，源于开源事件管理应用 firefighter-incident 中的一个权限配置错误。该应用的文档注释表明需要 Bearer 令牌认证，但实际代码却配置了无需认证即可访问。此外，服务端对 attachments 字段中的 URL 没有进行任何校验，导致攻击者可以通过 SSRF（服务端请求伪造）攻击获取 AWS IAM 临时凭据。该漏洞在 AWS EC2/EKS 云环境中尤其危险，因为攻击者可以利用该漏洞获取 IAM 角色的高权限，从而对整个 AWS 账户的资源造成严重影响。官方已发布修复补丁，要求用户升级至 0.0.54 版本，并对云环境中的 IMDSv2 配置和 IAM 角色权限进行审查。

漏洞分析

SSRF漏洞

云安全

代码审计

云原生架构

认证与授权

安全测试

---

### 0xa [对Aut...