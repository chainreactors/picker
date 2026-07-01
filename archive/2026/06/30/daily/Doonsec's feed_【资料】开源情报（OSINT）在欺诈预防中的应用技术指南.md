---
title: 【资料】开源情报（OSINT）在欺诈预防中的应用技术指南
url: https://mp.weixin.qq.com/s/Tvc6QBzN6o_pjeUx2VHp0Q
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:19:51.609322
---

# 【资料】开源情报（OSINT）在欺诈预防中的应用技术指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/no8YFGgia2NEQL9diblRofOX238XYxUlicMqagtcibRxwicy1HtGTgtibnhqGdYYH2dxlnicYncXYMDXywWu0mjeR43uVKBibMXyWwPQZCKJNM491yw/0?wx_fmt=jpeg)

# 【资料】开源情报（OSINT）在欺诈预防中的应用技术指南

原创

丁爸
丁爸

丁爸 情报分析师的工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NFLKibkfeNia9Ku0kwJp2vmaRvwz8Zvef46CMM5NjibImsu7wzhSvYogxibbUdlsty2Ul8OWl9ZBibPnvJZ1hTdic3ZYMRz7GnEG2tF4/640?wx_fmt=png&from=appmsg)

这是SEON Technologies公司发布的一份关于**开源情报（OSINT）在欺诈预防中的应用技术**指南。以下是文章的主要内容：

---

## 一、OSINT的定义

开源情报（Open Source Intelligence, OSINT）是指从互联网、社交媒体、传统媒体（电视、广播、出版物）等公开渠道收集数据，用于评估案件或客户身份。正如CIA网站所言："信息不必是秘密的才有价值。"

**OSINT工作流程**：收集（Collection）→ 处理（Processing）→ 分析（Analysis）→ 知识提取（Knowledge Extraction）

---

## 二、OSINT的工作原理与数据来源

OSINT工具聚合来自多种公开来源的信息，包括：

* 博客、论坛、社交媒体
* 传统媒体（电视、广播、出版物）
* 研究论文、政府记录、学术期刊

在欺诈检测中，主要用于验证用户与持卡人是否为同一人，或分析可疑用户、关联方等（称为"关注对象"或POI）。

---

## 三、OSINT的应用领域

* 执法机构
* 风险与欺诈管理
* 人力资源
* 网络安全
* 军事行动

---

## 四、OSINT的重要性与优势

**重要性**：

* 识别数据泄露
* 客户尽职调查（CDD）
* 发现漏洞
* 支持决策过程
* 跟踪新闻动态

**优势**：

* 无需用户配合，不干扰用户体验
* 成本较低，许多工具免费
* 信息持续更新，因公开数据不断新增

---

## 五、OSINT的劣势

* **信息噪声大**：需从海量信息中筛选有效内容
* **缺乏即插即用工具**：分析信息需要大量人工验证
* **需验证信息来源**：否则容易分析虚假/无用信息

---

## 六、合法性

OSINT调查完全合法，因其使用的是公开生产和公开可得的数据，无需搜查令，也不涉及违法活动。但收集和存储的信息需合规处理。

---

## 七、OSINT技术方法

### 核心调查逻辑

从已知信息出发（"start with what you know/have"），通过以下维度展开：

* **电子邮件地址**：验证地址、搜索引擎查询、泄露数据库（Have I Been Pwned）、社交媒体关联
* **用户名**：关联潜在邮箱、搜索引擎、专门用户名搜索工具（Knowem、NameVine等）
* **真实姓名**：人员搜索引擎（Pipl、Spokeo等）、社交媒体、选民记录

### 关键技术

* **高级搜索运算符**：使用Google、DuckDuckGo、Bing、Yandex等搜索引擎的特殊语法
* **对抗算法**：不同搜索引擎结果排序不同，需交叉验证
* **专业数据库**：如泄露邮箱数据库、人员搜索引擎

---

## 八、OSINT调查员的工作流程

1. **信息收集**：从公开来源收集邮件、电话、用户名、地址等
2. **过滤筛选**：排除不匹配或无关信息
3. **信息分析**：采用自下而上逻辑（归纳推理），从数据构建理论，形成可操作洞察
4. **获取洞察**：提出处理建议，必要时引入另一位调查员复核

**OPSEC（行动安全）**：调查过程中需保持匿名，避免触发目标警觉（如通知提醒、IP暴露等），建议使用虚拟机。

---

## 九、OSINT在欺诈预防中的具体应用

### 典型场景

* 反欺诈系统规则不足以正确评估时的人工复核
* 跟踪欺诈分子动态（搜索卡农论坛、暗网趋势）

### 核心问题

* "你真的是你声称的那个人吗？"
* "这好得令人难以置信吗？"
* "此人是否符合我们的用户画像？"

### 欺诈对抗特点

* 欺诈分子会研究受害者，匹配交易细节
* 使用代理使地址距离看起来合理
* shady affiliate（可疑关联）会伪装成合法身份
* 可能利用身份盗窃或钱骡（money mule）

### 内外结合

* 将公开网络发现与内部系统关联用户/实体交叉验证
* 通过OSINT发现新关注点，再在内部系统中搜索关联

---

## 十、证据捕获与记录

* 使用archive.is或archive.org（时光机）保存网页
* 浏览器截图插件
* 行业标准工具：Hunchly扩展（年费制）

---

## 十一、OSINT工具推荐

### SEON自家产品

* **手动查询功能**：通过邮箱或电话号码快速收集用户数字足迹，支持35+网站，可作为Chrome扩展或API使用，内置于欺诈预防堆栈中自动应用风险评分

### 其他行业级工具

* **Maltego**：复杂调查工具，社区版免费但功能有限，许可证昂贵但转换功能强大
* **Skopenow**：现代OSINT套件，擅长查找人员、企业及其关联，将复杂案件简化
* **Netwatch**：自称在线和社交媒体情报首选，与广泛数据合作伙伴合作
* **Effect Group**：专为OSINT调查构建的 sleek 情报平台，按操作付费，快速低成本编制档案

### 预配置虚拟机

* 有现成的、专为OSINT设计的虚拟机可用

---

## 十二、结论

OSINT是分析师工具箱中的"瑞士军刀"。在欺诈预防中至关重要，因为网络犯罪分子专门攻克自动化安全系统。掌握OSINT的核心在于：

* 找到他人不想让你发现的信息
* 在适当情境中处理信息
* 得出正确结论并做出决策

虽然自动化工具众多，但最终**思维模式**才是关键。

相关资料已上传知识星球

长按识别下面的二维码可加入星球

里面已有万余篇资料可供下载

续费五折优惠

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5zKJ6IvDm7zH8uGKMLmpkqKYLbkAVHcDIy1pTdjbsOlqh0GOYj7RhhMsfCLtUtWfwEicsFibUicCMwnw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NGMPoQian3maxo6Kl0LWQEVtdXNzs9CYHneV8osV9BGysiaHHYSDL3yicrF6wLAgVH4FUlY1XXEiaIPAd6k9Ny2iaPSAwL0SIRficqr4/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFESZibsC7Dx12Z6vvEDg99uEsCAvGHwbf50FqMe83gZyVraKI9lPm2jOBuchjNKJPS16RBW7WeTJq8TrOaMe82iaScO3GaaKKaY/0?wx_fmt=png)

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