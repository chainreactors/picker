---
title: 全网最强AI黑客技能库诞生！一个标题党不够用，我试了十个
url: https://mp.weixin.qq.com/s/aJKkD-8wE475kEI8juxvkg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:47:19.383008
---

# 全网最强AI黑客技能库诞生！一个标题党不够用，我试了十个

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0UoFk1R1aSLfEGw2MYdDeVibOjDf97JTvsF9DwHd8LOdLicevQ7He0iavyZQeZLHrswmmTPPL4oe9OvQb4ibMjdyd3x0iaHD7jYIUur8/0?wx_fmt=jpeg)

# 全网最强AI黑客技能库诞生！一个标题党不够用，我试了十个

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

声明：本文仅供技术研究与学习，使用本项目技能前请确保已获得合法授权。未经授权的渗透测试属于违法行为。

---

你知道吗？OpenAI的GPT-4、Anthropic的Claude、谷歌的Gemini……这些顶级大模型在真实漏洞挖掘场景中的成功率竟然**不到30%**。

原因很简单：通用大模型缺乏结构化的安全知识库支撑，面对真实攻防场景时往往"一本正经地胡说八道"。

而今天要介绍的**hack-skills**，正是为解决这一痛点而生——一个专为AI Agent打造的安全技能军火库。

![HackSkills项目横幅](https://mmbiz.qpic.cn/mmbiz_jpg/x5l8unjI0UpSmuVIZZKzYZicBdoxxu7V2rHPy2CdpolAWtJzweVGJUhKoekz9OfD0kGEUB7H3QiaPFDgj2Noia6Pcwa6kSfVQmcoyG0iccetuOg/640?from=appmsg)

HackSkills项目横幅

## 重点导读项目概述

hack-skills是Yaklang团队开源的AI Agent渗透测试技能库，GitHub星标**1268**，Fork数**174**。项目覆盖Web安全、API安全、身份认证、操作系统提权、二进制漏洞利用、密码学攻击、智能合约审计等**14个安全领域**，包含**101个深度技能模块**。

项目采用标准化的目录结构：每个技能独占一个目录，统一使用`skills/{语义标识符}/SKILL.md`格式。这种设计确保AI Agent能够精准加载所需技能，而非被海量信息淹没。

## 重点导读技能层级

### PART 01入口架构

| 层级 | 角色 | 推荐暴露级别 |
| --- | --- | --- |
| 主入口 | 全局路由、测试时序、跨类目切换 | 优先暴露 |
| 类目入口 | 按攻击面路由到稳定技能族 | 优先暴露 |
| 深度专题 | 完整攻击手册与执行细节 | 按需加载 |

主入口`hack`负责全局路由，根据目标特征（Web/API/移动端/二进制）动态选择下一层技能路径。类目入口包括`recon-for-sec`（侦察）、`api-sec`（API安全）、`auth-sec`（身份认证）、`injection-checking`（注入检测）、`file-access-vuln`（文件访问）、`business-logic-vuln`（业务逻辑）。

### PART 02知识来源

项目从多个公开优质资源中提炼知识，包括：

* `swisskyrepo/PayloadsAllTheThings` — 64个漏洞类别的Payload家族与绕过技术
* `hacktricks` — 渗透测试百科全书，覆盖Linux/Windows/macOS提权、Active Directory、容器逃逸
* `ctf-wiki` — CTF竞赛知识库，含Pwn、Crypto、Reverse、Forensics
* 公开安全研究论文与CVE公告

项目明确禁止直接复制大型字典或完整Payload列表，优先提炼可路由、可组合、可审计的安全技能。

## 重点导读核心技能分类

### PART 03Web安全

#### 注入攻击

覆盖XSS、SQLi、SSRF、XXE、SSTI、CMDi、NoSQL注入等主流注入类型。

SQL注入技能（`sqli-sql-injection`）提供475行技术内容，含DB2/Cassandra/BigQuery/SQLite特定利用方法、SQLite RCE、WAF绕过矩阵、CTF技术（handler/prepare/innodb）。

SSTI技能（`ssti-server-side-template-injection`）覆盖**15+模板引擎**（Jinja2/Twig/Pug/Handlebars/EJS/Razor/EEx/Smarty），含盲SSTI、Flask PIN计算。

#### 反序列化

`deserialization-insecure`技能提供714行内容，覆盖Java/PHP/Python/Ruby .NET反序列化攻击链，含BinaryFormatter/ViewState/JSON.NET/Node.js node-serialize/funcster等框架的具体利用方法。

#### 请求走私

`request-smuggling`技能覆盖CL.TE/TE.CL/TE.TE三种走私类型，详解8种混淆变体、HTTP/2降级、客户端请求脱同步技术。

### PART 04API安全

#### 认证与授权

`jwt-oauth-token-attacks`技能（301行）详解JWT算法混淆、密钥混淆、Claim篡改、JWKS滥用。`idor-broken-object-authorization`技能（336行）提供8类系统性IDOR测试方法，含Django/Prisma/Ransack的ORM过滤链泄露。

#### GraphQL安全

`graphql-and-hidden-parameters`技能涵盖GraphQL内省、批处理攻击、隐藏参数发现。

### PART 05操作系统安全

#### Linux提权

`linux-privilege-escalation`技能覆盖SUID/SGID滥用、内核漏洞、Sudo配置错误、Cron任务、Linux Capabilities、写权限服务文件、NFS no\_root\_squash。配套`SUID_CAPABILITIES_TRICKS.md`提供GTFOBins Top 30 SUID二进制精确利用命令。

#### 容器与K8s

`container-escape-techniques`技能涵盖Docker Socket滥用、特权容器逃逸、cgroup突破、runc漏洞、敏感路径挂载。`kubernetes-pentesting`技能覆盖Pod安全策略绕过、RBAC滥用、ServiceAccount Token窃取、etcd访问、容器镜像后门。

#### Windows与AD

`active-directory-kerberos-attacks`技能详解Kerberoasting、AS-REP Roasting、Golden/Silver Ticket、委派滥用（无约束/约束/RBCD）、Diamond Ticket。`active-directory-certificate-services`技能覆盖ESC1–ESC8攻击模式、证书模板滥用、PKINIT利用、Shadow Credentials。

### PART 06二进制漏洞利用

#### 堆栈安全

`stack-overflow-and-rop`技能覆盖缓冲区溢出、ROP链构造、ret2libc、SROP、栈Pivot、one-gadget。`heap-exploitation`技能涵盖UAF、double free、tcache poisoning、fastbin attack、House of系列技术。

#### 内核利用

`kernel-exploitation`技能详解内核ROP、ret2usr、SMEP/SMAP/KPTI绕过、内核竞态条件、modprobe\_path覆写。

### PART 07密码学攻击

#### RSA攻击

`rsa-attack-techniques`技能覆盖Wiener攻击、Boneh-Durfee、Hastad广播攻击、共模攻击、Coppersmith小根、Franklin-Reiter、PKCS#1 v1.5填充预言机。

#### 对称密码与格密码

`symmetric-cipher-attacks`技能涵盖填充预言机、比特翻转、ECB剪切粘贴、中间相遇攻击。`lattice-crypto-attacks`技能覆盖LLL/BKZ格规约、Hidden Number Problem、NTRU攻击。

### PART 08区块链安全

#### 智能合约审计

`smart-contract-vulnerabilities`技能（314行）覆盖重入攻击（4种变体）、整数溢出、delegatecall存储冲突、签名重放、CREATE2利用、闪电贷模式。`defi-attack-patterns`技能（355行）详解闪电贷预言机操纵、MEV三明治/JIT/清算攻击、首存款人Vault攻击、治理闪电贷、桥接漏洞。

### PART 09AI安全

#### LLM安全

`llm-prompt-injection`技能（357行）覆盖直接/间接注入、RAG污染、工具/函数滥用、Markdown泄露、MCP安全风险、编码绕过。`ai-ml-security`技能（425行）涵盖模型文件Pickle RCE、对抗样本（FGSM/PGD/C&W）、训练数据投毒、模型提取、成员推断、Agent安全。

## 重点导读技能选择指南

| 场景 | 推荐入口 |
| --- | --- |
| 新目标、信息不足 | `recon-for-sec` |
| REST API、GraphQL | `api-sec` |
| 登录、密码重置、JWT | `auth-sec` |
| HTML/JS反射、模板表达式 | `injection-checking` |
| 文件路径、下载、上传 | `file-access-vuln` |
| 优惠券、支付、状态机 | `business-logic-vuln` |
| HTTP解析异常 | `request-smuggling` |
| Node.js `__proto__`可控 | `prototype-pollution` |
| PHP弱比较、0e哈希 | `type-juggling` |
| .git/.svn/.env可访问 | `insecure-source-code-management` |
| 内部包名、依赖混淆 | `dependency-confusion` |
| 智能合约、Solidity | `smart-contract-vulnerabilities` |
| LLM、聊天机器人 | `llm-prompt-injection` |
| WAF拦截Payload | `waf-bypass-techniques` |
| Linux主机、SUID/sudo | `linux-privilege-escalation` |
| Docker/Kubernetes | `container-escape-techniques` |
| Windows主机、本地管理员 | `windows-privilege-escalation` |
| Active Directory、域环境 | `active-directory-kerberos-attacks` |
| 二进制/ELF/PE利用 | `stack-overflow-and-rop` |
| CTF密码挑战(RSA) | `rsa-attack-techniques` |

## 重点导读设计原则

* 安全知识优先于花哨包装
* 内容可审计性优先于数量扩张
* 优先授权测试、合法研究、防守验证场景
* 目录名应一眼传达安全语义
* 无客户特定信息，全部为通用方法论

## 重点导读安装使用

```
bashnpx skills add yaklang/hack-skills
```

离线场景可下载AES-256加密ZIP包：

```
bashcurl -fsSLO https://oss-qn.yaklang.com/hack-skills/latest/hack-skills.zip
7z x -phack-skills hack-skills.zip
```

密码`hack-skills`公开可见，仅用于绕过AV/EDR内容扫描。

## 重点导读项目地址

本公众号非项目作者，仅做技术分享。

```
https://github.com/yaklang/hack-skills
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UpRWic9WFicla4NR1ibIo3ZtTVlnasVY4Apa0nCgibPeNEjwia7Y9VjklDic9r5O8yKPibQyTzEDjTsczOOZnibtlTdUVraJ8PIiczNCSMg/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoBCEgESF2HpJnGYT1pibS6UpFTkzYnPaCAIic5g9zQ7uqJLARibolfocP68EcjYib2hG79zbomcEDj2lrLss6z0A967vwViboU44a8/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过