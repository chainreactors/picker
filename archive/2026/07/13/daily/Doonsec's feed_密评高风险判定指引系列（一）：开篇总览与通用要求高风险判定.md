---
title: 密评高风险判定指引系列（一）：开篇总览与通用要求高风险判定
url: https://mp.weixin.qq.com/s/iwxZ8e1gYWDOPnUOKPgOMw
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:45:23.773755
---

# 密评高风险判定指引系列（一）：开篇总览与通用要求高风险判定

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dOibzgvR2iaibqFaPDRXDrQmvKwSn1CBpTaqiaKyvsjxQ2ZYsaLsS2VC6k4zeopVIEkRp5y9m9SlibYjoTDgylm27k47ibXhGbCKJ3P9QMMYXG0rM/0?wx_fmt=jpeg)

# 密评高风险判定指引系列（一）：开篇总览与通用要求高风险判定

北京路劲科技有限公司

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**密评高风险判定指引系列（一）：开篇总览与通用要求高风险判定**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dOibzgvR2iaibpWia8bcEbs58WF0CrQg8mE5D0DhPWmic4jzAV8G0axAGPm2XiccNOJXsut6SEXG1lc7lic6aiaohOvHJ2Ksiatg2nJXqO0EqaOzC8IU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/dOibzgvR2iaibo2Fu3wRg3lNJxwAGP7kyUq5LJEMlBN04IYhE4pYHQI6GNgqcalFTz53ZuuqUicY3WuusPoEflSnBxdicbm3hibJ3I7Vml7YSceibk/640?wx_fmt=png&from=appmsg)

商用密码应用安全性评估（密评）中，高风险判定是决定测评结果是否"一票否决"的关键。本文带你读懂《信息系统密码应用高风险判定指引》的整体框架和通用要求中的高风险项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dOibzgvR2iaiboBiaR3cssMznNBMcVkp4Y1TfBfwv0OJeAXKfMajn2ib1VQ5tNMjhLTCibXeJ498bT5FkEFmLMmGswUsUW1ALlPRsYYxHic7Av3lqM/640?wx_fmt=png&from=appmsg)

**01**｜**为什么要关注高风险判定？**

在密评中，**高风险判定**是悬在每个信息系统头上的"达摩克利斯之剑"。根据《信息系统密码应用高风险判定指引》，一旦被判定存在高风险安全问题，无论其他指标完成得再好，整个系统的密评结果都将受到严重影响。

本指引由中国密码学会密评联委会于2021年12月发布，适用于指导、规范信息系统密码应用的规划、建设、运行及测评。

**聚力同行  勇往直前**

![](https://mmbiz.qpic.cn/mmbiz_png/dOibzgvR2iaibp223lST9lDIQLBYr7I0cucvOY7zicRRYrD2FAibzyKgUexIVJ4F3xADNOw1lUepSghRtIIpG5e7ib5fFOB5adTHomeMVZnNcgib9A/640?wx_fmt=png&from=appmsg)

**02**｜**高风险判定的五大构成要素**

每个高风险判定项都包含以下五个要素：

|  |  |
| --- | --- |
| 要素 | 说明 |
| \*\*指标要求\*\* | 源自GB/T 39786—2021的指标 |
| \*\*适用范围\*\* | 适用于哪一级别的信息系统 |
| \*\*安全问题\*\* | 具体的高风险安全问题描述 |
| \*\*可能的缓解措施\*\* | 能够降低风险等级的措施 |
| \*\*风险评价\*\* | 安全问题的风险等级判定 |

**聚力同行  勇往直前**

![](https://mmbiz.qpic.cn/mmbiz_png/dOibzgvR2iaibqspk0ibjEKOIosv9MaCt0qF3QheLHEUFQl2nKibbzABcNDB6x9tsho0nnZ6XheibFZfIsfDG0RS6OucE0kjfp0GWHLtmwjibbyiadk/640?wx_fmt=png&from=appmsg)

**03**｜**通用要求高风险判定**

通用要求覆盖**所有级别信息系统**，是所有后续章节的基础。**如果通用要求存在高风险，后续所有安全层面的判定都会受牵连**。

1

**密码算法高风险**

**指标要求：** 信息系统中使用的密码算法应符合法律法规和密码相关国家标准、行业标准。

**适用：** 所有级别信息系统

**两大高风险问题：**

**问题①：****使用不安全或强度不足的密码算法**

使用存在安全问题或安全强度不足的密码算法对重要数据进行保护，典型如：

• \*\*MD5\*\*（杂凑算法，已可碰撞）

• \*\*DES\*\*（对称加密，密钥太短）

• \*\*SHA‑1\*\*（杂凑算法，存在碰撞风险）

• \*\*RSA（不足2048比特）\*\*（非对称加密，密钥长度不够）

💡 **为什么是高风险？** 这些算法已被证明存在严重安全缺陷，攻击者可以轻易破解受其保护的数据。

**问题②：使用安全性未知的密码算法**

使用自行设计的密码算法、未经安全性论证的密码算法等。

💡 **为什么是高风险？** 未知即风险。没有经过公开论证和密码分析的算法，可能存在致命设计缺陷。

**缓解措施：**无

**风险评价：** 上述任一安全问题一旦被威胁利用，可能会导致信息系统面临高风险。

2

**密码技术高风险**

**指标要求：** 信息系统中使用的密码技术应遵循密码相关国家标准和行业标准。

**适用：** 所有级别信息系统

**两大高风险问题：**

**问题①：使用有缺陷或有安全警示的密码技术**

典型如：

• \*\*SSH 1.0\*\*（存在协议级漏洞）

• \*\*SSL 2.0 / SSL 3.0\*\*（已被彻底攻破）

• \*\*TLS 1.0\*\*（协议设计存在安全隐患）

**问题②：使用安全性未知的密码技术**

如自行设计的密码通信协议、未经安全性论证的密码通信协议等。

**缓解措施：无**

**风险评价：高风险**。

3

**密码产品和密码服务高风险**

**指标要求：** 信息系统中使用的密码产品、密码服务应符合法律法规相关要求。

适用： 所有级别信息系统

**五大高风险问题：**

|  |  |  |
| --- | --- | --- |
| 序号 | 安全问题 | 通俗理解 |
| 1 | 使用自实现且未提供安全性证据的密码产品 | “自己写的加密算法，没经过认证” |
| 2 | 使用的密码产品存在高危安全漏洞 | 如存在Heartbleed漏洞的OpenSSL |
| 3 | 密码产品使用不满足安全运行前提条件 | “没按说明书部署，安全策略没配” |
| 4 | 使用的密码服务提供商不具有相关资质 | “找了一家没牌照的加密服务商” |
| 5 | 存在密钥管理严重安全隐患 | 详见附录A（后续文章详解） |

**缓解措施：无**

**风险评价：高风险。**

**聚力同行  勇往直前**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dOibzgvR2iaiboHznQEiaoNePpuaTwOJ36OdpicPicMszF4Lg7nmK9hHREYIUwjKibY4vNJwnJQTtqXGtz6mXfZ5ZhDfwGT7qaRTzzAzrUTPjRrbiaE/640?wx_fmt=png&from=appmsg)

**04**｜**本章小结**

通用要求是密评高风险判定的"地基"。核心要点：

1. \*\*密码算法\*\*必须使用国家批准的算法（SM系列），杜绝MD5、DES、SHA‑1等

2. \*\*密码技术\*\*必须遵循国标行标，杜绝SSH 1.0、SSL 2.0/3.0等

3. \*\*密码产品\*\*必须合规、有资质、无漏洞

**一句话总结：算法合规、技术标准、产品认证，三者缺一不可！**

**聚力同行  勇往直前**

**关注路劲科技，关注网络安全！**

**END**

关于我们：

北京路劲科技有限公司(Beijing Lujin Technology Co. , Ltd.)成立于2019年1月4日，是一家提供全面系统集成与信息安全解决方案的专业IT技术服务公司。公司秉承“为网络安全保驾护航”的企业愿景及“提升国家整体安全”的使命，依据风险评估模型和等级保护标准，采用大数据等技术手段，开展网络安全相关业务。公司致力于为各个行业的业务信息化提供软件和通用解决方案、系统架构，系统管理和数据安全服务、以及IT咨询规划、系统集成与系统服务等专业化服务。公司立足北京，走向全国，始终坚持“换位、细节、感恩”的核心价值观，以“共赢、共享、共成长”的经营理念为出发点，集合了一批敢于创新、充满活力、热衷于为IT行业服务的优秀人才，致力于成为您身边的网络安全专家。

关注路劲科技，关注网络安全！

公司：北京路劲科技有限公司

地址：北京市昌平区南邵镇双营西路78号院2号楼5层504

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NtJr88ib7G289lzeU7zcuibiaE16ia3QnZNFaLUhC4G67CuiaOqicnfj2D8icshWLysP9N9UAx3n0rI3N70CltBPP1SXA/0?wx_fmt=png)

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