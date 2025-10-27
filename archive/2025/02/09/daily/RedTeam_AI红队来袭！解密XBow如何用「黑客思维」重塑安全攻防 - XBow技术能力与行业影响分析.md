---
title: AI红队来袭！解密XBow如何用「黑客思维」重塑安全攻防 - XBow技术能力与行业影响分析
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484043&idx=1&sn=2242396f541a9c23ae6a61e46d0ae5d3&chksm=c006ca7bf771436d2e177f29c9be6656568496e8c50493042a4d32dce2fb80e267dfcd554275&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-09
fetch_date: 2025-10-06T20:37:45.272547
---

# AI红队来袭！解密XBow如何用「黑客思维」重塑安全攻防 - XBow技术能力与行业影响分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk7cdO5f031NiarJAiaLIAlDkdjQVoib8OX5IglibsTFfgWIjRjroORzzAicEtdOlQ9bZAcTgQzRWkRGfmw/0?wx_fmt=jpeg)

# AI红队来袭！解密XBow如何用「黑客思维」重塑安全攻防 - XBow技术能力与行业影响分析

原创

tonghuaroot

RedTeam

当传统安全厂商还在用规则库对抗0day漏洞时，一家叫XBow的硅谷新贵正在用AI复现顶级黑客的思维路径，他们开发的AI红队系统，仅用28分钟就完成了人类团队40小时的工作量，甚至在某次实验中与拥有20年经验的渗透测试专家打成平手。

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7cdO5f031NiarJAiaLIAlDkdooViaHWF2nSR2WHQ8ia3Hr6KRsw0QibgdrQDdfNfq0ibLQk2ibP6s8GeicVQ/640?wx_fmt=png&from=appmsg)

image

### **一、核心能力验证**

**1. 基准测试表现**

* PortSwigger Labs：解决261个基准中的195个（75%）
* PentesterLab Exercises：解决282个中的204个（72%）
* 自研Novel Benchmarks：解决104个中的88个（85%）

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7cdO5f031NiarJAiaLIAlDkdVk3gDT0e8ibCOPUluiaRJbEDUt2Fus56K47UXM4hmQCCbRHokdsEwFww/640?wx_fmt=png&from=appmsg)

image

**2. 技术方法**

* 完全自主执行攻击链（无人工干预），支持命令执行与输出分析
* 混合AI与规则引擎，实现漏洞利用代码动态调试（如Java反序列化攻击中的错误日志分析）

### **二、典型漏洞利用案例**

1. **CBC填充预言攻击**

* 目标：解密AES-CBC实现的CAPTCHA Cookie
* 步骤：检测响应差异（"Invalid padding" vs "Invalid CAPTCHA"）→ 实施字节级解密 → 生成有效用户凭证

2. **GraphQL IDOR漏洞利用**

* 场景：无基准描述下，通过GraphQL内省获取API结构 → 枚举用户ID实现数据越权

3. **Jenkins RCE漏洞（CVE-2016-0792）**

* 方法：自主编写Python利用代码 → 通过服务器错误日志调试Payload → 从进程日志提取flag

![](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7cdO5f031NiarJAiaLIAlDkdUib1IwfjNJfkUiatc9EVORbuk2wHRibvqwUkb9iaRxw4xHA068GcmmuevA/640?wx_fmt=png&from=appmsg)

### **三、团队构成**

| 成员 | 职位 | 背景亮点 |
| --- | --- | --- |
| Oege de Moor | CEO | Semmle（GitHub高级安全）创始人，GitHub Copilot联合开发者 |
| Nico Waisman | 安全负责人 | 前Lyft CISO，特斯拉漏洞赏金计划核心贡献者 |
| Brendan Dolan-Gavitt | AI研究员 | NYU网络安全教授，硬件漏洞研究权威 |

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7cdO5f031NiarJAiaLIAlDkdjOZUdbUc0dzbgeZn8fSFRibgpWDdGOCJU8duHyQLPgXWSGiatcBpBQ5g/640?wx_fmt=png&from=appmsg)

image

### **四、行业实证数据**

**1. 效能对比**

* 人类顶级渗透测试专家（40小时）解决率87.5% vs XBow（28分钟）解决率85%

  ![Image of % of benchmarks solved](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk7cdO5f031NiarJAiaLIAlDkdVEmPCfw0nTiceMxhADpJeorhGc5frb8pFuCtSgnIFjJHC1O2VuEBhMQ/640?wx_fmt=other&from=appmsg)

**2. 漏洞披露**

* **累计发现12个CVE（截至2025年2月），包括：**

+ **CVE-2024-50334（Scoold身份绕过漏洞）**
+ **CVE-2024-52598（2FAuth SSRF漏洞）**
+ **CVE-2024-53844（EDDI路径遍历漏洞）**
+ **CVE-2024-52597（2FAuth存储型XSS漏洞）**
+ **CVE-2024-53982（Zoo-Project任意文件下载漏洞）**

**3. 资本动态**

* 种子轮融资2000万美元（Sequoia Capital领投）

### **五、技术透明度建设**

**1. 开源基准测试集**

* 发布104个Novel Benchmarks

![image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk7cdO5f031NiarJAiaLIAlDkdPwotxLRjbcdkdJQUkkMy4z6DicmfyRe5fC0M0KJiciaUFp1QfvHwBBczw/640?wx_fmt=jpeg&from=appmsg)

image

* 内置Canary字符串防止训练数据污染

**2. 技术博客**

* 漏洞利用过程全记录

以上数据均来自于XBow

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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