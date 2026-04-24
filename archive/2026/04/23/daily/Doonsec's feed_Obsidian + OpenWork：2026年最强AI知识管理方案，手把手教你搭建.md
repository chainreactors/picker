---
title: Obsidian + OpenWork：2026年最强AI知识管理方案，手把手教你搭建
url: https://mp.weixin.qq.com/s/WNh7BLGZWz9pdu3vaRHQEg
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:50:00.033953
---

# Obsidian + OpenWork：2026年最强AI知识管理方案，手把手教你搭建

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BowImrBK4tKS7aDO9PSZAtYs3SABiazzAAHiaGBeEkOPCeiaTrSIuTmPuvZUoibhUGHmbkhnUwkleibziaZ8jCe8yJJkaa3OMukLVOz8Vzo02jqOY/0?wx_fmt=jpeg)

# Obsidian + OpenWork：2026年最强AI知识管理方案，手把手教你搭建

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你是否也有过这样的困惑？

笔记软件用了不少，Obsidian、Notion、飞书文档……每个都很好，但用起来总是“差点意思”。灵感来了用 flomo 记一下，事后还要手动整理到 Obsidian；文章发布了，数据收集还要自己手动填表；多个知识库之间互相隔离，想跨库搜索比登天还难。

这些问题困扰了我很久，直到我遇到了 **OpenWork**——一个开源的 AI 桌面助手。配合 Obsidian，我终于跑通了 AI 知识管理的完整闭环。

今天，手把手教你搭建这套系统。

---

## 一、为什么需要 Obsidian + OpenWork？

在说怎么搭建之前，先聊聊为什么是这两个工具。

### Obsidian 的优势

* • **本地存储**：所有数据都在本地，不用担心云服务跑路
* • **双向链接**：让笔记之间形成知识网络，而非孤岛
* • **插件生态**：极其丰富，几乎没有它做不到的

### Obsidian 的痛点

* • 手机端同步麻烦
* • 多个知识库之间互相隔离
* • 很多操作依然需要手动完成

### OpenWork 的能力

**OpenWork** 是开源版的 Claude Cowork，主打“本地优先、隐私可控、执行高效”。它不只是一个聊天机器人，而是有“手足”的 AI 助手：

* • 能真正操纵你的电脑——读写文件、操作浏览器
* • 支持 MCP（Multi-Cloud Platform），能连接 Notion、Google Drive 等
* • 支持 Agent Skills，可以自动化处理各种日常任务
* • 有图形化界面，对非技术用户非常友好

**两者结合的价值**：OpenWork 充当“智能枢纽”，连接 Obsidian 和外部世界。你只需要发一条消息，它就能帮你把想法整理到 Obsidian、帮你收集数据、帮你管理知识库。

这就是 AI 时代知识管理的样子：**不是人找工具，而是工具为人服务**。

---

## 二、方案架构：二个组件，各司其职

这套工作流由二个核心组件构成：

| 组件 | 作用 | 说明 |
| --- | --- | --- |
| **Obsidian** | 知识库存储 | 本地 Markdown，双向链接，知识网络 |
| **OpenWork** | AI 大脑 + 执行手 | 理解意图，操作电脑，自动完成任务 |

**工作流程是这样的**：

```
你发消息 → OpenWork 理解意图 → 读写 Obsidian / 操作浏览器 / 调用 MCP → 返回结果
```

你不需要在各个应用之间跳来跳去，只需要对一个“助手”发号施令，它会帮你搞定一切。

---

## 三、手把手搭建指南

### 第一步：安装 OpenWork

1. 1. 访问 GitHub OpenWork 仓库（different-ai/openwork）
2. 2. 下载适配自己操作系统的安装文件
3. 3. 双击安装，打开后选择你的日常办公文件夹

**系统要求**：支持 Windows、Mac、Linux

### 第二步：配置模型

OpenWork 内置有模型提供，若是需要自己的自定义模型，则需要编辑

~/.config/opencode/opencode.json 内容，模版类似于：

```
{  "$schema": "https://opencode.ai/config.json",  "provider": {    "yidongyun": {      "npm": "@ai-sdk/openai-compatible",      "name": "yidongyun",      "options": {        "baseURL": "https://zhenze-huhehaote.cmecloud.cn/api/coding/v1",        "apiKey": ""      },      "models": {        "Minimax-M2.5": {          "name": "Minimax-M2.5"        }      }    }  },  "model": "yidongyun/Minimax-M2.5"}
```

### 第三步：连接 Obsidian

在使用 OpenWork 操作 Obsidian 之前，需要先完成以下步骤：

**确保 Obsidian 版本为 1.12.7 或更高**

**启用 CLI**

* 打开 Obsidian，进入 **Settings → General**
* 启用 **Command line interface**
* 按照提示完成注册
* **验证安装**

1. ```
   obsidian version
   ```

---

## 四、OpenWork 操作 Obsidian 的方式

通过 Obsidian CLI 与 vault 交互，执行各种命令操作。

```
常用命令示例：# 列出所有 vaultobsidian vaults# 列出文件obsidian files# 搜索笔记obsidian search query="关键词"# 读取当前文件obsidian read# 创建新笔记obsidian create name="笔记名称" content="内容"# 列出所有标签obsidian tags counts# 列出任务obsidian tasks todo# 读取今日日记obsidian daily:read# 追加内容到日记obsidian daily:append content="- [ ] 新任务"# 获取 vault 信息obsidian vault info=name
```

## 四、这些场景特别有用

### 场景一：搜索笔记

> “在 vault 中搜索包含 "OpenClaw" 的文章”

### 场景二：读取笔记内容

> “读取某个笔记的完整内容”

### 场景三：创建笔记

> 使用 OpenWork 可以生成结构化笔记：
>
> 1. 定义笔记模板
> 2. 使用 `create`命令批量创建
> 3. 自动添加属性（tags、aliases 等）

---

## 五、为什么不用 Notion 或飞书？

很多人会问：Notion AI 不香吗？飞书文档不香吗？

**关键区别：本地 vs 云端**

Obsidian 的底层是本地 Markdown 文件，OpenWork 可以直接读写，**不需要 API 调用，响应更快、更便宜**。

而 Notion、飞书的数据在云端，每次 AI 操作都要走 API，**慢、贵、有限制**。

更重要的是，**数据完全可控**。你的笔记存在你自己的电脑上，没有隐私泄露风险。

---

## 六、总结

Obsidian + OpenWork 这套组合，本质上是把**信息输入 → 智能处理 → 知识沉淀**这三个环节打通了。你不需要在各个软件之间跳来跳去，只需要对一个“助手”发消息，它会帮你搞定一切。

如果你也想体验“第二大脑”的感觉，不妨从今天开始，动手搭建这套系统。

**你不需要成为技术专家，只需要愿意尝试的心。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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