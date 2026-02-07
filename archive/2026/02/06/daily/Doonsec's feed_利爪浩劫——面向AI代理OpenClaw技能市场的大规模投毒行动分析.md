---
title: 利爪浩劫——面向AI代理OpenClaw技能市场的大规模投毒行动分析
url: https://mp.weixin.qq.com/s/Rj0uk1AXdPW1PnuaRfxA1A
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:05:21.805256
---

# 利爪浩劫——面向AI代理OpenClaw技能市场的大规模投毒行动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/krU5D4C1q6QUXiczt4s7htOO9sPYsXExuzPA9AvUhLAm5z26ekBKprrmaEf8GH1r4fSMS5Q6SNEb7Ysx0HrT8Dw/0?wx_fmt=jpeg)

# 利爪浩劫——面向AI代理OpenClaw技能市场的大规模投毒行动分析

安天CERT
安天CERT

安天集团

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

**0****1**

**概述**

2026年初，伴随着OpenClaw爆火，叠加由于多次更名带来的认知混乱，其生态系统成为供应链攻击的新目标。OpenClaw作为开源个人AI代理，提供了灵活的Skills（技能插件）扩展接口，也开放了官方技能市场ClawHub，已经形成了一个新型的AI产业生态。而攻击者正是通过注册为ClawHub的开发者，之后开发并批量上传伪装成合法技能插件的恶意“Skills”，**通过“ClickFix”模式的社工攻击技巧，诱导用户下载安装，在用户系统中植入运行恶意代码**。构成了一起严重的面向AI生态的供应链投毒攻击事件。[安天安全研究与应急处理中心（安天CERT）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650208789&idx=2&sn=00b7643e03b81ed7c151388153fce778&scene=21#wechat_redirect)对本事件进行了持续跟踪，并进行了相关样本分析和研判。安天AVL SDK反病毒引擎已经具备相关恶意Skills样本的查杀能力。使用安天AVL SDK反病毒引擎的主机安全产品升级后均可检测拦截相关恶意Skills文件样本，及其关联下载的样本。

OpenClaw（曾用名ClawdBot、Moltbot），是近期被全球关注的现象级开源AI智能体，以“跨平台数字生产力工具”为核心定位，在短时间内获得极高关注度。其Skills模块作为生态扩展，支持深度接入数十个办公及社交平台，用户可通过相关平台便捷获取与安装。目前已衍生出数千种各类Skills，涵盖自动化办公、加密货币工具、社交媒体辅助等多个场景，初步形成了自组织、快速演化的开源生态。

ClawHub是作为OpenClaw的核心Skills分发渠道，已经形成了由一定粘性的开发者群体。2026年2月1日，国际安全团队Koi Security在ClawHub平台上发现大量恶意Skills集中植入，并将相关攻击称之为“ClawHavoc”攻击行动[1]，我们尊重Koi率先发现者对事件的命名权，将攻击事件中文名译为“利爪浩劫”，同时根据投毒样本的形态特点，将相关批次样本命名为*Trojan/OpenClaw.PolySkill*。

ClawHub运营者已经进行了响应处理，部分恶意Skills已无法搜索到，但仍有“漏网之鱼”，在规模性下架恶意Skills后，截止到本报告发布时点，ClawHub平台中共包含3498个Skills。根据安天CERT统计，历史ClawHub至少出现过1184个恶意Skills。其中ID为hightower6eu的作者上传恶意包最多，达677个。

随着基于技能的生态规模快速扩张，Skills市场投毒成为了OpenClaw生态最突出、最紧迫的安全挑战，也使扩展插件的供应链污染对AI生态的新威胁。恶意Skills通过伪装隐蔽、诱导传播等方式可窃取用户敏感数据、接管系统权限、篡改系统数据、破坏系统运行、自动横向渗透攻击。相关风险如果不能有效遏止，也会制约OpenClaw开源生态的健康与可持续发展。并影响用户对整个AI代理类工具和产品的信心。同样，这一事件对国内AI生态的建设与发展也将带来重大的警示作用。其与近期开始陆续出现的基于大模型平台编写的恶意代码，无不提醒我们，**所谓人工智能安全不应窄化为人工智能本身机理型的算法、模型风险及数据投毒，AI所推动的网络攻击自动化与AI应用带来导致的暴露面与新的攻击通道已经处于加速运动之中，才是我们当下需要最迫切投入资源应对的现实威胁**。

**0****2**

**“利爪浩劫”事件与样本分析**

###

OpenClaw作为支持功能扩展的AI代理框架，其Skills扩展包可通过ClawHub市场便捷安装，而Skills本质上是一组“以结构化文件组织起来的插件/能力包”，具体内容包括配置、代码、资源、元数据。基于安天所提出的执行体治理视角，其是一类新型的脚本格式的新型执行体。攻击者利用Skills的开放扩展机制，制作伪装成正常功能的恶意技能包并上架ClawHub，诱导用户下载安装；这类恶意技能包通常会在SKILL.md说明文件或配套脚本中，植入要求用户执行终端命令、下载运行未知二进制文件的“虚假安装步骤”，借助社会工程学手段骗取用户信任并执行高危操作，一旦用户照做，恶意代码将凭借技能包的系统访问权限直接侵入主机，最终实现对用户系统的控制、数据窃取或恶意程序植入，形成完整的攻击链路。

## 2.1 **典型恶意Skill样本分析**

目前捕获到的样本虽然数量很多，但整体上主要是三类恶意功能：诱导下载并执行恶意代码（ClickFix）、反弹连接Shell（RAT）、信息窃取（steal）。其中**部分并不是传统意义上的恶意代码，而是一个带有URL的社工内容**。按照安天恶意代码分类命名规范分类前缀/环境前缀.家族命名的格式，安天CERT将这批样本统一命名为*Trojan/OpenClaw.PolySkill*，将其分类为特洛伊木马；并首次在命名库中增加OpenClaw前缀；与此同时，基于Skill包是一个代码、数据、配置、元数据等的聚合物（Poly），其风险恰恰在于**Poly同时具备对OpenClaw操控和对使用者欺骗的能力**，因此我们用Poly（聚合体）与Skill组合，作为其命名。对恶意Skill诱导下载的二进制木马，我们会在后续报告中专门分析。本篇聚焦于恶意Skill投毒。对于其诱导下载的木马，我们依然采取原同源性家族命名。

1、诱骗下载并执行恶意代码典型样本：skill内容对应的是zip压缩包文件，文件内容包含：一个json和一个SKILL.md文件，恶意下载链接或恶意下载命令被嵌入至SKILL.md文件中。

对应样本在文档中提供虚假信息，冒充需要用户手动安装openclaw-core组件才能使用，依托操作指南文档，对用户进行社工欺骗，诱导用户下载安装恶意代码。其中针对Windows系统则从github下载恶意加密压缩包并解压执行恶意软件，通过工程师对github的信任感提高诱骗成功率。macOS系统则执行base64解码后的命令，从攻击者的服务器下载二制载荷执行。

**表****2****-****1****SKILL****.m****d****样本标签**

|  |  |
| --- | --- |
| **病毒名称** | Trojan/OpenClaw.PolySkill |
| **原始文件名** | SKILL.md |
| **MD5** | 5e4428176aeb8cfc7f0391654d683a2a |
| **文件大小** | 5.36 KB (5,493 字节) |
| **文件格式** | Text/ISO\_IEC.UTF8[:No bom] |
| **SKILL****包名** | google-k53 |
| **版本** | 1.0.0 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHk9wCKep8coWZFuYnRPyZL18D77DfMst7sCQEwFmFdgZ7TnGkFwiadjyhOP85L9iaEY9ibn9sURWnEO9Hic3w8Vp8or982Qlw7lpG7w/640?wx_fmt=png&from=appmsg)

 图**2****-****1****诱导下载压缩包或执行恶意命令**

针对MacOS系统恶意代码分析，其执行base64解码后得到一个URL并下载二进制载荷，该载荷详细信息参见安天病毒百科[3]。

**表****2****-****2****MacOS二进制样本标签**

|  |  |
| --- | --- |
| **病毒名称** | Trojan/MacOS.Amos |
| **原始文件名** | sujwb2nsdn93d79q |
| **MD5** | be24b44d4895c6bc14e3f98a9687a399 |
| **处理器架构** | X86\_64、ARM64 |
| **文件大小** | 509 KB (521,440 字节) |
| **文件格式** | Mach-O |
| **编译语言** | C/C++ |
| **VT首次上传时间** | 2026-02-03 15:48:21 UTC |
| **VT检测结果** | 26/65 |

其二进制载荷中存在大量加密静态数据，仅在运行时进行解密，以此规避检测。

![](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHkib1BCmpB9iaiaBYgQ9TwpA18VwmiaWicjM1ATTQrcHlYDia7DKfQvOSuAQSXPxvKHGibzpBR05UGm1icX9iatdu9F17gMJjo0bup1Ll5x4/640?wx_fmt=jpeg&from=appmsg)

**图****2****-****2****加密数据及对应的解密代码**

根据其算法对多个不同样本data段中的配置信息进行解密，其配置中均有“jhzhhfomng”、“https://socifiapp[.]com”字符串以及对话框提示文本，主要是窃取文件类型的范围有所不同。

![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHkic6HUtibEuBzIWb5LrdWGbGIKoZ3CBf0kvoEHXGcbqtYVS0sK8sQSzOQACWrvMporYj69wAGmPFtPLqusz1MiavVUAn6Qr7mic2Tc/640?wx_fmt=png&from=appmsg)

 图**2****-****3****解密后的部分配置信息**

在运行后会显示预先配置好的伪装信息，让用户输入系统密码，以此获取更高权限实施恶意行动。根据相关提示信息、及代码分析关联可知样本为Atomic macOS Stealer（简称AMOS）窃密木马。AMOS窃密木马能够窃取文件、浏览器保存的密码、cookie、自动填充信息、系统Key串数据、Telegram会话和聊天记录、SSH 密钥和 bash/zsh 历史以及加密货币钱包资产等，然后压缩为ZIP发送至C2服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHkibLvGambwRCstqXnDpicwgmCZ7D1MPFqyTciaaf8jan56f71ic8xNmYicdKiaw3oqo0iau5ZDaKNTWgKg3eMibFmPSicux0g4RRk0smuhw/640?wx_fmt=png&from=appmsg)

**图****2****-****4****启动时弹出伪造的密码输入框**

2、反弹shell典型样本：skill对应的是zip压缩包文件，压缩包中包含：json文件、SKILL.md文件、scripts文件夹，该文件夹存在python脚本文件。

对应样本冒充加密货币监控工具获取加密货币平台的市场行情信息，但脚本文件代码中嵌入利用os.system函数执行恶意下载或反弹shell的命令。

**表****2****-****3****python代码****样本标签**

|  |  |
| --- | --- |
| **病毒名称** | Trojan/OpenClaw.PolySkill |
| **原始文件名** | polymarket.py |
| **MD5** | a3365c837ec2659c2aa04e7010a0db15 |
| **文件大小** | 13.6 KB (13,927 字节) |
| **文件格式** | Script/Python.PY |
| **SKILL****包名** | polymarket-all-in-one |
| **版本** | 1.0.0 |

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHk8qbUny5NehRzAxF2S4pxLLh8IaNMqnibSzF8wWsEcKqwxcgbph4ZRrjnLD9zFc51ZyTunujyMpyBtwOicnsfGWLTRvwFC8eEPX0/640?wx_fmt=png&from=appmsg)**

**图****2****-****5****下载具有反弹****shell****连接功能的远控木马**

3、窃密典型样本：skill对应的是zip压缩包文件，恶意代码在压缩包中的js文件中，利用js代码外传数据。

对应样本以“天气助手”功能为伪装，从开源天气网站open-meteo.com获取天气数据，并发送天气数据到用户信箱，但实际上窃取本地文件~/.clawdbot/.env。这个文件中存放正是付费的AI（Claude、OpenAI）等的可信配置源。

**表****2****-****4****js代码的样本标签**

|  |  |
| --- | --- |
| **病毒名称** | Trojan/OpenClaw.PolySkill |
| **原始文件名** | index.js |
| **MD5** | 2444b3ab5de42fcca22e6025cf018e3b |
| **文件大小** | 7.55 KB (7,734 字节) |
| **文件格式** | Script/Netscape.JS |
| **SKILL****包名** | rankaj |
| **版本** | 1.0.0 |

**![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHkicF9K301dX1rTLWdKj2CcNgfJcjIdzePfDw7JX0j9eaZQSTia0tpZq07YIt7Sc8j6wnzLdgSx2AJwQP6Cusdh3R95XJia2hoLh7E/640?wx_fmt=png&from=appmsg)**

**图****2****-****6****将窃取的数据发送至Webhook**

## 2.2 **攻防事件****时间线**

**➢ 2026年1月27日，首个恶意Skill，polymarket-traiding-bot v1.0.0发布，上传者为aslaep123；**

**➢ 2026年1月28日，恶意Skill，reddit-trends v1.0.0、base-agent v1.0.0发布；**

**➢ 2026年1月29日，恶意Skill，bybit-agent v1.0.0发布；**

**➢ 2026年1月31日，开始大规模发布恶意Skills，总计7名攻击者发布386个恶意Skills，其中包括主要攻击者hightower6eu的354个；**

**➢ 2026年2月1日，安全团队**Koi首次披露相关攻击活动，并将其命名为ClawHavoc；

**➢ 2026年2月1日，社区制作了一个基于AI用于自动检查Skills安全性的工具Clawdex；**

**➢ 2026年2月3日，社区在**GitHub发出安全提示，称已手动删除相关Skills，修复了多个安全问题，并提交两个拉取请求。

## 2.3 **恶意Skill样本统计**

2026年2月5日，截止至报告发布时，安天CERT发现ClawHub历史skills包中存在1184个恶意的，归属于12个作者ID，其中作者ID为hightower6eu的恶意包达677个。ClawHub平台正在进行清理。

**表****2****-****5 ClawHub恶意skills包统计**

|  |  |
| --- | --- |
| **Skills包作者** | **数量** |
| hightower6eu | 677 |
| sakaen736jih | 390 |
| moonshine-100rze | 60 |
| zaycv | 19 |
| aslaep123 | 14 |
| jordanprater | 10 |
| noreplyboter | 4 |
| rjnpage | 2 |
| gpaitai | 2 |
| lvy19811120-gif | 2 |
| danman60 | 2 |
| noypearl | 2 |

其中多数恶意Skill已经被清理下架，但还能访问并归属于moonshine-100rze上传者的Skills包地址如下，共计60个，对应下载量达14285次，请用户注意其风险。我们整理了URL清单，便于网络管理者加入黑名单，阻断风险。

![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHk8Egic4DVnJc8e2JYn7fKRuPenrLFlNmwgIFl50mbcZsXzCCrZonmic2ITMkNKmnA2YxKZMGZTXqSh0mocicMPWq7wQbc1vx2icDng/640?wx_fmt=png&from=appmsg)

**图****2****-****7****moonshine-100rze上传者的Skills包**

## 2.4 **攻击者的战术技巧分析**

攻击者针对Skill流行度和Skill使用群体进行了有针对性的设计，以提升攻击价值。

|  |  |  |  |
| --- | --- | --- | --- |
| **技能类别** | **代表性名称** | **目标受众** | **攻击意图** |
| **加密货币工具** | solana-wallet-tracker, polymarket-trader, binance-agent | 加密货币交易者、DeFi 用户 | 窃取钱包私钥、助记词、交易所API密钥 |
| **生产力增强** | google-workspace, gmail-integration, excel-helper | 企业员工、开发者 | 窃取企业文档、日历安排、邮件通信 |
| **社交媒体工具** | youtube-summarize-pro, x-trends-tracker, twitter-monitor | 内容创作者、营销人员 | 劫持社交账号、窃取会话 Cookies |
| **系统实用程序** ...