---
title: 第三节｜Windows认证+权限系统设计模型（收尾篇）
url: https://mp.weixin.qq.com/s/ZcFZVh3bwpM-8OouLqyUGA
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:20.554249
---

# 第三节｜Windows认证+权限系统设计模型（收尾篇）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3PxWhY8513b26mGkzhcs93NXria3vwFxhwdH15pbHiaiaGvLu5t99jMueNAnhey0ibpOU7M5y9MetssAQRn92k4fMSbLDzAWdsqErhmqibL6srYo/0?wx_fmt=jpeg)

# 第三节｜Windows认证+权限系统设计模型（收尾篇）

原创

皮皮宋
皮皮宋

皮皮宋渗透笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

身份认证系列来到最后一节啦！前两节给大家讲了基础认证（多因子、SSO、JWT）和企业级认证（OAuth、SAML、SCRAM），覆盖了通用场景和企业场景。

今天这一节，聚焦两个核心重点：一是Windows系统专属的身份认证机制（本地认证、Kerberos、NTLM），二是通用的权限系统设计模型，收尾整个身份认证系列，帮大家构建完整的知识体系，不管是开发、运维还是网安，都能直接套用。

![](https://mmbiz.qpic.cn/mmbiz_png/3PxWhY8513aEmJeXCu05wsDLWicShfv0HPyAmgdM5s6DUrcicGJibh7VtX2Jib4AicYjAXIma3ODvaMn68YmqrdaNyTosBP3yPVqr71lschuZLiak/640?wx_fmt=png&from=appmsg)

# 一、Windows系统身份认证机制

## 7.1 本地用户认证（核心流程）

Windows本地登录认证，核心是“密码哈希比对”，整个流程由两个关键进程协作完成，步骤清晰：

用户在登录界面输入账号密码，由winlogon.exe进程接收输入（winlogon.exe的作用：用户注销、重启、锁屏后，显示登录界面，接收用户凭证）；

winlogon.exe将用户输入的凭证，传递给lsass.exe进程（本地安全授权服务）；

lsass.exe将用户输入的明文密码，通过算法转换为NTLM Hash，与系统中SAM数据库保存的Hash值进行对比；

对比一致，认证成功，允许用户登录；对比失败，提示“密码错误”。

## 7.2 SAM：Windows密码存储核心

SAM（Security Accounts Manager，安全帐户管理器），是Windows操作系统管理用户帐户安全的核心机制，本质是一个存储用户密码哈希的数据库文件。

关键细节（必记）：

存储位置：SAM文件保存于 %SystemRoot%\system32\config\sam，同时在注册表中保存于 HKEY\_LOCAL\_MACHINE\SAM\SAM 和 HKEY\_LOCAL\_MACHINE\SECURITY\SAM；

存储内容：不存储明文密码，只存储明文密码经过算法处理后的Hash值，主要分为LM Hash和NTLM Hash（后续详解）；

访问权限：正常情况下，SAM文件处于锁定状态，不可直接访问、复制、移动，仅system用户有权限读写。

## 7.3 密码破解（常见方式）

攻击者破解Windows密码，核心是获取SAM文件中的Hash值，再通过暴力破解、彩虹表等方式还原明文密码，常见获取方式有4种：

物理接触主机：启动其他操作系统（如PE系统），访问Windows分区，获取 %SystemRoot%\system32\config\sam 文件；

获取备份文件：找到 %SystemRoot%\repair\sam.\_ 文件（系统备份的SAM文件），提取Hash值；

注册表导出：使用工具（如mimikatz）从注册表中导出SAM散列值；

网络嗅探：在网络中嗅探分析SMB报文，从中获取密码Hash（如Net-NTLM Hash）。

## 7.4 SPNEGO：Windows扩展认证协议

SPNEGO（Simple and Protected GSS-API Negotiation），是微软提供的一种基于GSS-API认证机制的安全协议，核心作用是“使Web服务器共享Windows凭证”，扩展了Kerberos协议，常用于Windows域环境中的Web应用认证。

# 二、Kerberos协议（Windows域环境默认认证）

## 8.1 简介

Kerberos协议起源于美国麻省理工学院Athena项目，基于公私钥加密体制，核心作用是为分布式环境提供双向验证，是Windows域环境中的默认身份验证协议，也是企业级域环境中最核心的认证方式。

简单来说，Kerberos实现了“单点登录（SSO）”：用户只需登录一次，就能访问域内所有授权的服务器（如文件服务器、打印服务器、邮件服务器），无需反复输入密码。

Kerberos系统中，核心角色有4个（简化为3个核心）：认证服务器（AS）、票据授予服务（TGS）、客户端（Client）、普通服务器（Server）。

## 8.2 核心概念（必记）

Principal（安全个体）：被认证的对象（用户、服务器），有唯一的名字和口令；

KDC（Key Distribution Center，密钥分发中心）：提供票据和临时会话密钥的网络服务，包含AS和TGS；

Ticket（票据）：用户向服务器证明身份的核心凭证，包含用户标识、会话密钥、时间戳等信息，用服务器密钥加密；

Authenticator（认证器）：辅助验证票据的凭证，包含时间戳、校验码等，用会话密钥加密；

TGT（票据授予票据）：由AS发放，用户用于向TGS申请访问其他服务器的票据；

ST（会话票据）：由TGS发放，用户用于访问普通服务器的票据。

## 8.3 简化认证过程（核心5步）

跳过复杂的TGS交互，简化后的Kerberos认证流程，核心是“票据的申请与验证”：

客户端向AS发起请求，提交自己和目标服务器的Principal；

AS生成会话密钥（Kc,s），并生成两个票据：① 用客户端密码加密的票据（包含会话密钥、服务器Principal）；② 用服务器密码加密的票据（包含会话密钥、客户端Principal），返回给客户端；

客户端用自己的密码解开票据，获取会话密钥（Kc,s），生成Authenticator（用Kc,s加密），将Authenticator和给服务器的票据发给服务器；

服务器用自己的密码解开票据，获取会话密钥（Kc,s），用Kc,s解开Authenticator，验证时间戳（是否在5分钟内、是否首次出现，防止重放攻击）和校验码；

验证通过，客户端完成认证，服务器可返回加密的时间戳，完成双向认证。

## 8.5 优缺点

## 优点

密码不直接在网络中传输，不易被窃听；

密码猜测难度高，安全性强；

票据被盗后难以复用，需配合Authenticator使用；

支持双向认证，同时验证客户端和服务器身份。

## 缺点

缺乏票据撤销机制，票据有效期内被盗，仍可能被滥用；

密钥管理复杂，需维护大量Principal的密钥；

依赖时钟同步，客户端与服务器时间差超过5分钟，认证失败；

伸缩性受限，不适合超大规模分布式环境。

# 三、NTLM身份验证（Windows早期标准协议）

## 9.1 NTLM认证（核心流程）

NTLM（NT LAN Manager），是基于“挑战/应答”的身份验证协议，是Windows NT早期版本中的标准安全协议，目前仍在部分旧系统、非域环境中使用。

NTLM通用流程（6步）：

客户端在本地将用户密码加密为密码Hash；

客户端向服务器明文发送用户名；

服务器生成一个16位随机数字（Challenge，挑战码），发送给客户端；

客户端用密码Hash加密Challenge，生成Response（应答码），返回给服务器；

服务器将用户名、Challenge、Response发送给域控制器；

域控制器用用户名查询SAM数据库，获取对应的密码Hash，用该Hash加密Challenge，与客户端的Response对比，一致则认证成功。

NTLM有两个版本，核心区别在于Challenge长度和加密方式：

Net-NTLMv1：Challenge为8位，加密方式较脆弱，可通过彩虹表爆破；

Net-NTLMv2：自Windows Vista起默认使用，Challenge为16位，加密强度更高，安全性优于v1。

## 9.2 Hash详解（LM Hash vs NTLM Hash）

## 1. LM Hash

Windows最早使用的密码Hash算法，由IBM设计，存在诸多安全缺陷，目前已被NTLM Hash替代。

计算方式：

将用户密码转换为大写，截断为14字节；

不足14字节则用0×00补足；

将14字节分为两段7字节数据；

以“KGS!@#$%”为密钥，对两段数据分别进行DES加密，得到16字节Hash；

拼接两段Hash，得到最终的LM Hash。

核心缺陷：密码不区分大小写、最长14字节、DES算法强度低、分组加密降低复杂度。

## 2. NTLM Hash

微软为解决LM Hash的缺陷，于1993年在Windows NT 3.1中引入，目前是Windows系统的主流密码Hash算法。

计算方式：

将密码转换为16进制，进行Unicode编码；

基于MD4算法计算哈希值，得到最终的NTLM Hash。

注意：Windows 2000/XP/2003中，密码≤14位用LM Hash，密码>14位用NTLM Hash；Windows Vista及以后版本，默认禁用LM Hash，仅使用NTLM Hash。

## 9.3 常见攻击方式

Pass The Hash（PtH，哈希传递）：攻击者捕获用户密码Hash后，无需还原明文，直接复用Hash进行认证，是NTLM最常见的攻击方式；

Pass The Key（密钥传递）：在禁用NTLM的环境下，用工具（如mimikatz）直接获取密码密钥，进行认证；

NTLM Relay（NTLM中继）：中间人攻击，攻击者伪装为认证服务器和客户端，中继认证请求，获取权限。

# 四、权限系统设计模型（通用）

身份认证的最终目的，是“控制用户访问权限”——确保合法用户只能访问自己有权限的资源，因此权限系统设计至关重要。常见的权限设计模型有4种，各有适用场景：

## 核心概念（必记）

用户：发起操作的主体（如登录系统的人）；

对象：被操作的客体（如文件、接口、页面）；

权限：对某对象的操作许可（如读取、修改、删除）；

ACL（权限控制表）：描述用户与权限之间关系的数据表；

权限控制矩阵：抽象的安全模型，描述每个用户对每个对象的权限。

## 4种核心权限模型

## 1. 自主访问控制（DAC）

核心逻辑：基于ACL控制，用户可自主分配自己拥有的权限（如用户A可将自己的文件读取权限分配给用户B），灵活性高。

适用场景：普通办公系统、小型应用，对权限控制要求不严格的场景。

缺点：权限分散，难以统一管理，易出现权限泄露。

## 2. 强制访问控制（MAC）

核心逻辑：每个用户和对象都有固定的权限标识（如“绝密”“机密”“公开”），用户能否操作对象，取决于双方权限标识的关系（如“绝密”用户可访问“机密”对象，反之不可）。

适用场景：高安全等级场景（如军事、政务系统），权限控制严格，不允许自主分配权限。

缺点：灵活性差，无法灵活适配业务需求。

## 3. 基于角色的访问控制（RBAC）

目前最普及的权限设计模型，核心逻辑：引入“角色”概念，用户关联角色，角色关联权限，通过角色分配权限，实现权限的统一管理。

举例：“管理员”角色关联“用户管理、文件删除、系统配置”权限，给用户分配“管理员”角色，用户即可获得该角色的所有权限。

适用场景：绝大多数企业应用、网站、APP，灵活适配业务需求，便于权限管理。

## 4. 基于属性的权限验证（ABAC）

核心逻辑：不依赖角色，基于“属性”动态判断权限，属性分为4类：用户属性（如用户等级）、环境属性（如登录时间、IP地址）、操作属性（如操作类型）、对象属性（如文件类型）。

举例：仅允许“VIP用户”在“工作日9:00-18:00”，从“公司内网IP”访问“机密文件”。

适用场景：复杂业务场景、动态权限控制（如电商、金融系统）。

## 系列总结

到这里，身份认证系列就全部收尾啦！从基础的多因子认证、SSO、JWT，到企业级的OAuth、SAML、SCRAM，再到Windows专属的Kerberos、NTLM，最后到通用的权限系统设计模型，完整覆盖了身份认证的核心知识点。

不管是开发时设计认证系统，还是渗透测试时挖掘认证漏洞，或是运维时保障系统安全，这些知识点都能直接用到，帮大家快速避坑，记得关注哦～

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/CrpWk11pwIicrkmF1ZAbZl48vjGQFt5MKRmdXeAcNxicBjVnQqx3DYUqGd2UhqveP86KHpS0CYUoSia6QAF01kVhw/0?wx_fmt=png)

皮皮宋渗透笔记

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CrpWk11pwIicrkmF1ZAbZl48vjGQFt5MKRmdXeAcNxicBjVnQqx3DYUqGd2UhqveP86KHpS0CYUoSia6QAF01kVhw/0?wx_fmt=png)

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