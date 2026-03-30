---
title: 5200万次下载，三个高危漏洞：你的AI应用正在\"裸奔\"吗？
url: https://mp.weixin.qq.com/s/m0LjAX6cVyPs10fQ0BFxgQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:15.630320
---

# 5200万次下载，三个高危漏洞：你的AI应用正在\"裸奔\"吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fTugLXvN07CqtdYyFbOww6txaPYkIrdEoFyMvtPPesF9aHKE3omPuFN446b6GYrKEsouKBcqUYXBn5kG1L08lRLp2OKyYTRhZzFdzBwkYek/0?wx_fmt=jpeg)

# 5200万次下载，三个高危漏洞：你的AI应用正在"裸奔"吗？

原创

小安
小安

信息安全动态

![]()

在小说阅读器中沉浸阅读

![LangChain安全漏洞](https://mmbiz.qpic.cn/mmbiz_jpg/fTugLXvN07Dv6mJXX4v3VZJVrg9bG02eDCbcicF83R8jR3UVoB5puu7piaY0MiaCMQmXuv9PTmpSpARO2QTKl04SAYWn9ydxzxDj7FtqBonyM0/640?wx_fmt=jpeg "LangChain安全漏洞")

5200万次——这是LangChain上周在PyPI上的下载量。

当你的团队用它快速构建AI应用时，可能没想到：三个高危漏洞正潜伏其中，能读取服务器文件、窃取API密钥、甚至访问用户的完整对话记录。

## 事件概述

2026年3月27日，安全研究机构Cyera披露了影响LangChain和LangGraph框架的三个安全漏洞。这两个框架是目前全球最流行的LLM应用开发工具——仅上周，LangChain、LangChain-Core和LangGraph在PyPI上的下载量就分别达到5200万、2300万和900万次。

这意味着，**全球数以万计的企业AI应用可能正处于风险之中**。

## 三大漏洞详解

### 漏洞一：路径遍历（CVE-2026-34070，CVSS 7.5）

**攻击方式**：通过prompt模板加载API，攻击者可以构造特殊输入，绕过验证读取服务器上的任意文件。

**危害**：可能泄露Docker配置、密钥文件、系统敏感信息等。

**影响组件**：`langchain_core/prompts/loading.py`

### 漏洞二：反序列化漏洞（CVE-2025-68664，CVSS 9.3）⚠️ 最严重

**攻击方式**：攻击者传入特殊数据结构，欺骗应用将其解释为已序列化的LangChain对象，而非普通用户数据。

**危害**：直接泄露API密钥和环境变量中的敏感信息。

**注意**：该漏洞此前已被Cyera命名为"LangGrinch"，在2025年12月就已披露。

### 漏洞三：SQL注入（CVE-2025-67644，CVSS 7.3）

**攻击方式**：通过LangGraph的SQLite检查点实现，攻击者可操纵元数据过滤键执行任意SQL查询。

**危害**：访问敏感工作流相关的对话历史记录。

## 修复版本

官方已发布补丁版本：

| 漏洞编号 | 修复版本 |
| --- | --- |
| CVE-2026-34070 | langchain-core >= 1.2.22 |
| CVE-2025-68664 | langchain-core 0.3.81 或 1.2.5 |
| CVE-2025-67644 | langgraph-checkpoint-sqlite >= 3.0.1 |

**升级命令**：

```
pip install --upgrade langchain-core langgraph-checkpoint-sqlite
```

## 为什么这件事值得重视？

### 1. 影响范围巨大

"LangChain不是孤立存在的。它处于AI栈庞大依赖网络的中心。数百个库封装、扩展或依赖它。"——Cyera研究员指出。

当LangChain核心存在漏洞时，**影响会通过每个下游库、每个封装器、每个集成向外扩散**。

### 2. AI应用安全意识薄弱

很多团队在追求AI功能落地时，往往忽视了底层框架的安全风险。这些漏洞再次证明：**AI基础设施并不免疫经典的安全漏洞**——路径遍历、反序列化、SQL注入，这些都是老朋友了。

### 3. 攻击者反应迅速

就在几天前，Langflow的一个关键漏洞（CVE-2026-33017）在公开披露后**仅20小时就被攻击者利用**。威胁行动者正变得越来越快，留给我们的窗口期越来越短。

## 企业应对建议

### 立即行动

1. **检查依赖版本**：确认项目使用的LangChain、LangGraph版本
2. **升级到安全版本**：立即执行pip升级
3. **审计敏感数据暴露**：检查是否有密钥、配置文件被非预期访问

### 长期措施

1. **建立AI组件安全审计机制**：定期扫描AI框架依赖的安全公告
2. **环境密钥隔离**：避免将敏感密钥硬编码在环境变量中
3. **最小权限原则**：AI应用不应拥有读取任意文件的权限

## 写在最后

LangChain让AI开发变得简单——几行代码就能调用GPT-4，接入向量数据库，构建智能Agent。但便利的背后，是巨大的攻击面。

**5200万次下载，意味着5200万次潜在的风险入口。**

当你的团队在享受AI框架带来的效率提升时，请问自己一个问题：如果明天某个核心依赖爆出高危漏洞，你知道该升级哪个版本吗？

如果不确定，今天就去检查吧。

---

推荐阅读：

* [紧急！你的Chrome可能正在"裸奔"](https://mp.weixin.qq.com/s?__biz=Mzg4NDc0Njk1MQ==&mid=2247488086&idx=1&sn=63ac5ef813f01a53883269415cf8fce2&scene=21#wechat_redirect)
* [SIEM不是万能药：为什么90%的企业都在"假装"做安全运营](https://mp.weixin.qq.com/s?__biz=Mzg4NDc0Njk1MQ==&mid=2247488068&idx=2&sn=ccac2562e424a35a609d412dcee63583&scene=21#wechat_redirect)
* [企业信息安全框架选择：ISO 27001、NIST还是CIS？三大主流框架深度对比](https://mp.weixin.qq.com/s?__biz=Mzg4NDc0Njk1MQ==&mid=2247488064&idx=1&sn=f23ce47d0e4afdc1e4140975dc8a9972&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HPjboWok4teVOic0O8dM4CYg3a98MY5sfRJ2uicwq2VcVNH56GGxoWYpH4g3bq1tqhHOFxtfv0ryDt9vSne5JgnQ/0?wx_fmt=png)

信息安全动态

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HPjboWok4teVOic0O8dM4CYg3a98MY5sfRJ2uicwq2VcVNH56GGxoWYpH4g3bq1tqhHOFxtfv0ryDt9vSne5JgnQ/0?wx_fmt=png)

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