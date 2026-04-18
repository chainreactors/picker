---
title: Zack-AI-Scanner 新一代基于AI大模型的Web漏洞扫描器 (文末福利)
url: https://mp.weixin.qq.com/s/UcKuAyZow6QhEhCbpX4JDw
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:30:54.199836
---

# Zack-AI-Scanner 新一代基于AI大模型的Web漏洞扫描器 (文末福利)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/De3yb4u5JSrp4vfVv9shZicA2QwJvkP2ib9LOqw4VlFJYFgYPiciaJAwlsnE5dQEccricWoXEgLu84mUiatcu1g7VVcxkczdTyiccUyibpo01kHdrWw/0?wx_fmt=jpeg)

# Zack-AI-Scanner 新一代基于AI大模型的Web漏洞扫描器 (文末福利)

星悦安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于ZackSecurity
，作者ZackSecurity

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4hDldxzjdO3HAlbNBOdaIpnOicRR6vfAxiblGeg0XKQ3Lg/0)

**ZackSecurity**
.

本公众号不定期更新Web渗透、内网渗透、红蓝攻防、代码审计、IoT安全、APT研究、工具分享等内容。

## 0x00 前言

Zack-AI-Scanner 是一款依托大语言模型的自动化 Web 漏洞扫描工具，作为 Burp Suite 扩展插件运行。它采用 AI 深度学习技术，自动解析 HTTP 请求的特征，智能识别潜在的安全漏洞，动态创建有针对性的测试 Payload，并自动验证漏洞的真实性。

![image-20260413002103071](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSotffgeN2hr9Fr7ISYbDMicHa05QaLibkabtPaGSVVjfFUxpc21dDMia6wQfFAARwZKAegNcwlGLCPsbsVw9ymaGQKObkgduGicQC0/640?wx_fmt=png&from=appmsg)![image-20260413001605897](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSqaYzeEWtPKQKEapAvtEL96ktJAXXFvNhibFV5eIx5ybJ1icFBhAoVsWILjriaadVYJgCjtuXxDqBEicsZd0kDiayAYLTpmkF3SZjcg/640?wx_fmt=png&from=appmsg)

项目地址 : https://github.com/ZackSecurity/Zack-AI-Scanner

## **0x01 核心功能 & 技术栈**

## 核心功能

* **AI 智能扫描：通过内置的 Skills，利用大语言模型自动分析请求并制定测试策略。**

* **漏洞类型广泛支持：支持 17 种常见 Web 漏洞的检测。**

* **WAF 绕过能力：集成多种 WAF 绕过技术，50% 载荷为绕过载荷。**

* **实时验证：AI 二次验证确保漏洞的真实性，置信度阈值 ≥90%。**

* **报告格式多样：可导出 HTML 和 Markdown 格式的渗透测试报告。**

## 技术栈

| 组件 | 技术选型 |
| --- | --- |
| 开发语言 | Java 17 |
| 构建工具 | Maven (maven-shade-plugin) |
| 扩展框架 | Burp Extender API 2.3 |
| JSON 处理 | Gson 2.10.1 |
| HTTP 客户端 | OkHttp3 4.12.0 |
| GUI 框架 | Swing (Java 内置) |
| 配置存储 | JSON 文件 (~/.zackai\_config.json) |

## 支持的漏洞类型

| 漏洞类型 | 说明 |
| --- | --- |
| SQL\_INJECTION | SQL 注入 |
| XSS | 跨站脚本攻击 |
| COMMAND\_INJECTION | 命令注入 |
| FILE\_UPLOAD | 文件上传漏洞 |
| SSRF | 服务端请求伪造 |
| XXE | XML 外部实体注入 |
| FILE\_INCLUDE | 文件包含漏洞 |
| SSTI | 模板注入 |
| CSRF | 跨站请求伪造 |
| DESERIALIZATION | 反序列化漏洞 |
| AUTH\_BYPASS | 越权/认证绕过 |
| PATH\_TRAVERSAL | 路径遍历 |
| DIRECTORY\_TRAVERSAL | 目录穿越 |
| SENSITIVE\_DATA\_EXPOSURE | 敏感信息泄露 |
| LOGIC\_FLAW | 逻辑漏洞 |
| RACE\_CONDITION | 条件竞争 |
| TYPE\_CONFUSION | 类型混淆 |

## 支持的 AI 服务提供商

* OpenAI (GPT-4, GPT-3.5)
* Anthropic (Claude)
* Google Gemini
* Azure OpenAI
* 通义千问 (阿里云)
* 文心一言 (百度)
* 智谱 AI (GLM)
* Kimi (月之暗面)
* DeepSeek
* 讯飞星火
* 字节豆包
* 腾讯混元
* 百川智能
* MiniMax
* 零一万物
* 阶跃星辰

## **0x02 快速开始**

### 安装

1. 构建项目: `mvn clean package`
2. 在 Burp Suite 的 Extender 标签页加载生成的 JAR 文件

### 配置

1. 点击 "配置" 按钮打开配置中心
2. 选择 AI 服务提供商并输入 API Key
3. 点击 "获取模型" 按钮获取可用模型列表
4. 保存配置后即可开始使用

### 使用

1. 在 Burp Suite 的 Proxy 或其他模块中选择 HTTP 请求
2. 右键点击，选择 "Zack-AI-Scanner" 菜单
3. 选择扫描模式（AI 智能扫描或特定漏洞类型）
4. 在主面板查看扫描进度和结果
5. 导出漏洞报告

## 目录结构

```
src/main/java/com/zackai/├── AISentryExtender.java    # Burp 扩展主入口├── core/                    # 核心功能模块│   ├── AIEngine.java        # AI 扫描引擎│   └── ConfigManager.java   # 配置管理器（单例）├── model/                   # 数据模型│   ├── ScanTask.java        # 扫描任务模型│   ├── VulnResult.java      # 漏洞结果模型│   └── AIProvider.java      # AI 服务提供商模型├── ui/                      # UI 组件│   ├── MainPanel.java       # 主面板│   ├── TaskTablePanel.java  # 任务表格│   ├── TaskDetailPanel.java # 任务详情│   ├── LogPanel.java        # 日志面板│   ├── ConfigDialog.java    # 配置对话框│   ├── ExportDialog.java    # 导出对话框│   ├── EndpointManagerDialog.java  # 端点管理│   ├── PromptPanel.java     # 提示词管理│   └── HelpPanel.java       # 帮助面板└── util/                    # 工具类    └── ReportGenerator.java # 报告生成器
```

## 插件使用实例

配置大模型API Key信息：

## ![image-20260413001335537](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSpKOsyJHibjfVSRv3C6hicamZXG7sbyibCicBnCOAuV1YMKfpoe1Eus8S0jUXibywIf4WvNtiagCR4rKw0z15nacSWejEwiaoEFtg9wwQ/640?wx_fmt=png&from=appmsg)

右击请求包->拓展->Zack-AI-Scanner调用工具，可选择AI智能扫描和单漏洞扫描：

## ![image-20260413001605897](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSoyAQtU5ib8ibIICbsKOXl2HP59q6iaE59002icc9vMibK3uOQOiaEJmSVXXCHialML5LicMDD8icfzMvH3lJtQwqIiaTDic9OBbXun2l1Rng/640?wx_fmt=png&from=appmsg)

日志统计窗口可实时查看扫描信息：

## ![image-20260413002103071](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSoxVibeiaoPKpfvElgldicpWP71WbcQib0lpA0ia1vCjZxTwo0vmdQwPYgUSIrQtj5OrlcnjT7qJ23htj8DF4dUXGwhHXDDibADiahy1E/640?wx_fmt=png&from=appmsg)

请求与响应详情窗口可以查看实时的扫描流量：

![image-20260413002258241](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSrSaibiad8L7S7HZS6yV30nrnRBzNKJGPG4Yib5cgATpP9Pmk8NMYDhaibloZJibRichjjYPqJ8cgzupmia48rIyLuEkUynhQAoN4IlRA/640?wx_fmt=png&from=appmsg)

在任务列表窗口可以查看所有扫描任务和状态，扫描结束导出漏洞报告，支持 HTML 和 Markdown 格式：

![image-20260413002603746](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSqzM58tmynYBHgIQibKRXNicgnB8P6caQJg8o3wPrXNufLs8CXevD4m0lFzleWfltTbLwvSR93uMnn5lExoLXc4UUjck4ZOPDC8s/640?wx_fmt=png&from=appmsg)![image-20260413002646611](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSojjU5agayqvUMzvqaCsdvBTP7zHickE4ArvYFibseNhNgGicVw5Pyb7WCRRmANKCicBWhsafGu1y8icja4xCuHaibH4AksIgice5pjP4/640?wx_fmt=png&from=appmsg)

HTML 和 Markdown 格式报告内容：

![image-20260413003256031](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSqRPIFvMSOJyBEdlSGhrvBORJfWic9QrghRz0ELTeRia2eicRSxw0eby7CEqxMjjvq9vlf6xk6QGibYQhtIs9NtAcW16A4ib2xqRS9M/640?wx_fmt=png&from=appmsg)

![image-20260413003211829](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSrY093n3rpTlGNEUKDYAb26yvsHdNtE6CianT9Ru8vsWw8x8gh7n7szWVS7KNtMblNM410ZpZeq1DLeedaxxfVMFIcDlyStoCe8/640?wx_fmt=png&from=appmsg)

## 免责声明

本工具仅供教育和授权测试使用！旨在帮助安全研究人员、渗透测试人员和IT专业人员在**获得明确授权**的情况下进行安全评估和漏洞研究。

**使用本工具即表示您同意：**

* 仅在您拥有明确书面授权的系统上使用此工具
* 遵守所有适用的法律法规和道德准则
* 对任何未经授权的使用或滥用行为承担全部责任
* 不会将本工具用于任何非法或恶意目的

## 0x03 星悦AI中转站

而想要高速率使用国外顶级AI模型，如ChatGPT 5.4 / Claude-Opus 4.6 那就需要找到一个好用的中转站.

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSoFenib0R0YIxlIRRib0gA9JguDib2rQG80LfhqET1QXPsoNDreXA2W4TsUG0iajV1LBTkiaRacdibQ4E39bPHbtlQe6ibrc4vGtp6Udk/640?wx_fmt=png&from=appmsg)

我这里为大家能舒适使用，给大家构建了一个中转站，主营Openai / Claude ，后期会上线别的模型，而且是最快速 最安全的，不像某些所谓的公益站会往你的电脑里塞入后门.

中转站地址 : https://xyusec.com/

现在注册送10$额度，能随便用 GPT5.4 和 Claude-Opus-4.6（限前60名，后面的注册送5$）

目前模型列表:

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSq0CPicY6xzMTp4EPnVXHGd5njEyAOAibWMGV3gcUiaM6lKMrYVVe82hWO0fkb19XicX4HJP5hdjKE4snTJ3unk5ibytbPQQle1UscM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSpxPRNBm6wHufRtPoQmLyPzAxVFHreeFcIDR08NPlorPyxvRZOdXlj0fkhXOJSD1yWpxDK5dibMVpm7ibYfiaDo6RR00puUA3YIq8/640?wx_fmt=png&from=appmsg)

## **0x04 20$兑换码获取**

****标签:代码审计，0day，渗透测试，系统，通用，0day，闲鱼，交易所****

******5个20$兑换码，发送 260417 获取(先到先得).******

******免责声明:****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由读者承担全部法律及连带责任，文章作者和本公众号不承担任何法律及连带责任，望周知！！!******

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicic8KPZnD5dyHp8uiasNyNWQgSUlzVSibCfnv5HjhSB9o1zibZnicxGGalykSuiaux0iaMneticVbzcGFRxbLP5kaSg1A/0?wx_fmt=png)

星悦安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicic8KPZnD5dyHp8uiasNyNWQgSUlzVSibCfnv5HjhSB9o1zibZnicxGGalykSuiaux0iaMneticVbzcGFRxbLP5kaSg1A/0?wx_fmt=png)

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