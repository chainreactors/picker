---
title: 基于AI的自主渗透测试平台 | AI-Powered Autonomous Penetration Testing Platform
url: https://mp.weixin.qq.com/s/HGqJ5lnHgRwYk2axpZn1Nw
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:38:47.292066
---

# 基于AI的自主渗透测试平台 | AI-Powered Autonomous Penetration Testing Platform

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AXRefkPRWsEA4crQxmWRA0uDyxuibHqxTU7dr34GYGNxFB06lfI45WOj9y3hicXJMyu7J14UjfBDGmvpROibQ98Iw/0?wx_fmt=jpeg)

# 基于AI的自主渗透测试平台 | AI-Powered Autonomous Penetration Testing Platform

原创

0xSecDebug
0xSecDebug

0xSecDebug

![]()

在小说阅读器中沉浸阅读

# KaliGPT-Attack Platform (beta v0.2)🛡️

>     请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**。

## 📖 项目简介

    KaliGPT-Attack Platform 是一个创新的AI驱动的自主渗透测试工具，采用独特的**三模块架构**（推理、生成、解析），有效解决了传统LLM在长时间渗透测试过程中的上下文丢失问题。该工具支持Web UI和MCP-stdio两种工作模式，能够自主决策、执行渗透测试任务，并实时反馈结果。

### ✨ 核心特性

* 🧠 **三模块AI架构** - 推理模块（Lead Tester）、生成模块（Junior Tester）、解析模块，分工明确，有效缓解上下文丢失
* 🌲 **PTT任务树** - Penetration Testing Task Tree，清晰维护任务层级和执行状态
* 🔄 **双模式支持** - Web UI（可视化界面）+ MCP-stdio（命令行集成）
* ⚡ **实时流式输出** - SSE技术实现AI推理和工具执行的实时反馈
* 🤖 **自主执行** - AI自动决策下一步操作，无需人工干预
* 🔍 **智能漏洞分析** - 自动提取、分类和报告发现的安全漏洞
* 🛠️ **丰富的工具集成** - 支持Nmap、SQLMap、Nikto、Gobuster、Hydra等主流渗透测试工具
* 🎨 **现代化UI** - 基于React + TailwindCSS + Framer Motion的精美界面，支持深色/浅色主题

  ![image](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEA4crQxmWRA0uDyxuibHqxTTMOz9JBuJaJyTXP6ibvSCxPc4sTuvZADL97ibDID6g03gcYPB6az1wXg/640?wx_fmt=png&from=appmsg)

  ![image](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsEA4crQxmWRA0uDyxuibHqxTQmTia16uiamXOyadnJKCiaq8012SXc4V6T5ibicTUJOdXNQKq7CK3X2IIqA/640?wx_fmt=png&from=appmsg)

---

### 三模块架构详解

#### 1️⃣ 推理模块 (Reasoning Module - Lead Tester)

* **职责**：维护PTT任务树，决策下一步任务
* **输入**：用户目标、工具执行结果、当前PTT状态
* **输出**：下一步任务建议、优先级排序
* 关键功能：

+ PTT初始化和动态更新
+ 任务可行性评估
+ 攻击路径规划
+ 风险评估

#### 2️⃣ 生成模块 (Generation Module - Junior Tester)

* **职责**：将抽象任务转换为具体可执行命令
* **输入**：推理模块的子任务描述
* **输出**：具体的工具调用命令和参数
* 关键功能：

+ 任务扩展（Chain of Thought）
+ 命令生成和参数优化
+ 工具选择和组合
+ 执行策略制定

#### 3️⃣ 解析模块 (Parsing Module)

* **职责**：提取和分析工具输出信息
* **输入**：工具输出、源代码、HTTP响应等
* **输出**：结构化的发现、漏洞报告
* 关键功能：

+ 工具输出智能解析
+ 漏洞识别和分类
+ 信息提取和关联
+ 结果去重和聚合

---

## 🚀 快速开始

### 前置要求

* **Go** 1.21 或更高版本
* **Node.js** 16+ 和 npm/yarn
* **Kali Linux** 或安装了渗透测试工具的系统
* **OpenAI兼容的API** (OpenAI、DeepSeek、SiliconFlow等)

#### 运行

**Web模式（推荐）：**

```
./kaligpt-attack -mode web -addr :8080
```

然后访问 `http://localhost:8080`

**MCP-stdio模式：**

```
./kaligpt-attack -mode mcp-stdio
```

---

## 💻 使用指南

### Web UI 模式

1. **启动服务**

   ```
   ./kaligpt-attack -mode web
   ```
2. **访问界面**

* 打开浏览器访问 `http://localhost:8080`
* 首次使用需要在"系统设置"中配置API Key

3. **开始渗透测试**

* 进入"LLM助手"页面
* 输入目标和测试需求，例如：

  ```
  请对目标网站 http://example.com 进行全面的安全测试
  ```
* AI将自动规划任务树并执行测试

4. **查看结果**

* 实时查看AI推理过程
* 查看工具执行输出
* 查看攻击链可视化
* 导出测试报告

### MCP-stdio 模式

适合集成到其他工具（如Claude Desktop、Cursor等）：

```
# 在MCP配置文件中添加
{
  "mcpServers": {
    "kaligpt": {
      "command": "/path/to/kaligpt-attack",
      "args": ["-mode", "mcp-stdio"],
      "env": {
        "KALIGPT_API_KEY": "your-api-key"
      }
    }
  }
}
```

## 🛠️ 支持的工具

| 工具 | 类别 | 描述 | 状态 |
| --- | --- | --- | --- |
| **Nmap** | 扫描 | 网络映射和端口扫描 | ✅ |
| **Masscan** | 扫描 | 超快速端口扫描 | ✅ |
| **HTTPx** | Web | HTTP探测和指纹识别 | ✅ |
| **SQLMap** | Web | SQL注入检测和利用 | ✅ |
| **Nikto** | Web | Web服务器漏洞扫描 | ✅ |
| **Gobuster** | Web | 目录/文件暴力破解 | ✅ |
| **WPScan** | Web | WordPress安全扫描 | ✅ |
| **Hydra** | 暴力破解 | 网络登录暴力破解 | ✅ |

更多工具持续集成中...

---

## 🎯 使用场景

### 1. 自动化渗透测试

```
用户输入：对 http://testsite.com 进行完整的安全评估

AI执行流程：
1. 推理模块：规划测试任务树（信息收集 → 漏洞扫描 → 漏洞利用）
2. 生成模块：生成具体命令（nmap、nikto、sqlmap等）
3. 解析模块：分析结果，提取漏洞信息
4. 推理模块：根据发现调整任务树，继续深入测试
```

### 2. 漏洞验证

```
用户输入：验证 http://example.com/login.php 是否存在SQL注入

AI执行流程：
1. 生成模块：生成SQLMap测试命令
2. 执行器：运行SQLMap
3. 解析模块：分析输出，确认漏洞
4. 推理模块：生成详细报告
```

### 3. 安全培训

* 观察AI的渗透测试思路
* 学习工具使用方法
* 理解攻击链构建过程

## 📖 项目地址

```
https://github.com/kk12-30/KaliGPT
```

## 💻 威胁情报推送群

>   如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

![图片](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsFtSkiayt0qhnGMdQLOiaibqxvgibgaWjhuM9B25NW9yrlU1ga4MrHFSor63U27nUWveeCDvpRvT0TXdg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

0xSecDebug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

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