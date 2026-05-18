---
title: 用 Obsidian 管理飞书知识库？这个插件让双向同步成为现实
url: https://mp.weixin.qq.com/s/LpJgezEqkhDybS16_yvl2g
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:07:56.263651
---

# 用 Obsidian 管理飞书知识库？这个插件让双向同步成为现实

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImlDcibN1OiaUaPpSDvaqHnKdWBBicL7yokgy45TTK6Q5ia5YnXafS5dJhUKLu9AfktebdPVWbAxoBUxibicyuBKt0eib3TB5CQFMJTFiaE/0?wx_fmt=jpeg)

# 用 Obsidian 管理飞书知识库？这个插件让双向同步成为现实

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 你是否也在经历这样的痛苦：飞书文档越来越多，想用 Obsidian 整理却只能手动复制粘贴？改了这边忘改那边，版本混乱到怀疑人生？

今天给大家介绍一个开源 Obsidian 插件——**Feishu Sync**，它能让你的 Obsidian Vault 和飞书知识库真正实现双向同步。

---

## 🤔 为什么需要这个插件？

飞书文档协作方便，但深度编辑和知识管理体验远不如 Obsidian。很多知识工作者日常面临两难：

* **只飞书**：文档散落各处，缺乏双向链接和图谱，知识难以体系化
* **只 Obsidian**：团队协作不便，移动端访问受限，无法与同事共享
* **两边手动搬**：改一处要同步两处，迟早会遗漏，最终版本混乱

**Feishu Sync** 的出现，就是为了终结这个困境。

---

## ✨ 核心功能一览

### 🔄 真正的双向同步

不是简单的导入导出，而是**增量双向同步**：

* 在 Obsidian 新建/编辑的笔记 → 自动上传到飞书知识库
* 在飞书修改的文档 → 自动下载到 Obsidian Vault
* 只同步有变更的文件，不做无用功

支持三种同步方向，按需选择：

| 模式 | 适用场景 |
| --- | --- |
| 双向同步 | 日常使用，两边改动都能同步 |
| 仅下载（飞书→Obsidian） | 把飞书当内容源，Obsidian 只读 |
| 仅上传（Obsidian→飞书） | 用 Obsidian 写作，飞书做展示 |

### ⚔️ 智能冲突处理

当同一篇文档在飞书和 Obsidian 都做了修改，插件会自动检测冲突，并提供三种解决策略：

* **飞书优先**：以飞书版本为准，覆盖本地
* **本地优先**：保留 Obsidian 版本，不上传远端
* **创建冲突副本**：两份都保留，本地生成 `.conflict` 副本，由你决定取舍

### 📋 Frontmatter 元数据追踪

每篇同步的文档会自动注入飞书元数据：

```
---
feishu_node_token: "xxx"
feishu_obj_token: "xxx"
feishu_space_id: "xxx"
feishu_last_modified: "2026-05-17T..."
feishu_sync_version: 1
---
```

无需额外数据库，文件本身即映射关系，透明可控。

### 🔄 自动更新

基于 Gitee Releases 的插件自动更新机制，启动时自动检查新版本，一键升级，无需手动下载。

---

## 🚀 三步完成配置

插件的设置页面采用引导式设计，三步即可上手：

### Step 1：安装 lark-cli

lark-cli 是飞书官方命令行工具，插件通过它与飞书交互：

```
npm install -g @larksuite/cli
```

安装后点击「检查」，插件会自动检测是否安装成功。

### Step 2：配置凭据并登录

1. 前往飞书开放平台创建应用，获取 App ID 和 App Secret
2. 在插件设置中填入凭据，点击「配置并登录」
3. 浏览器自动弹出授权页面，扫码确认即可

整个 OAuth 设备授权流程内嵌在插件中，无需手动复制 token。

### Step 3：选择知识库并同步

填入飞书知识库的 Space ID（从知识库设置页面 URL 中获取），配置同步方向和冲突策略，点击侧边栏同步图标即可开始。

---

## 🎯 典型使用场景

### 场景一：个人知识管理

用 Obsidian 做深度笔记和知识图谱，同时自动同步到飞书知识库，手机上随时查阅。Obsidian 的双向链接、标签体系与飞书的协作能力完美互补。

### 场景二：团队文档协作

团队在飞书上协作编辑，你用 Obsidian 本地深度整理和加工，修改后自动同步回飞书。既享受 Obsidian 的编辑体验，又不脱离团队工作流。

### 场景三：文档备份与迁移

将飞书知识库全量同步到 Obsidian Vault，本地保留完整备份。从此不再担心平台数据丢失，随时可以迁移。

---

## 🛡️ 技术架构：为什么选择 lark-cli？

Feishu Sync 没有直接调用飞书 REST API，而是基于飞书官方的 lark-cli 命令行工具作为中间层。这个架构选择带来几个关键优势：

1. **认证统一管理**：OAuth 设备授权流程由 lark-cli 处理，插件无需自行管理 token 刷新
2. **API 变更无感**：飞书 API 升级时只需更新 lark-cli，插件代码无需改动
3. **可独立调试**：遇到问题可以直接在终端用 lark-cli 命令排查，定位问题更高效
4. **官方维护**：lark-cli 由飞书官方维护，API 兼容性有保障

---

## 💻 跨平台支持

插件特别针对 Windows 环境做了大量兼容处理：

* 自动查找系统 Node.js（支持 fnm、nvm 等版本管理器）
* 解析 npm `.cmd` 包装器，直接调用 node.exe 运行，绕过编码和 stdin 问题
* 临时文件存放在 Vault 目录内，不写入系统用户目录

macOS 和 Linux 同样支持，通过 login shell 执行确保 PATH 正确。

---

## 📦 安装方式

1. 前往 Gitee Release 页面下载 `main.js`、`manifest.json`、`styles.css` 三个文件
2. 在 Obsidian Vault 中创建 `.obsidian/plugins/feishu-sync/` 目录
3. 将三个文件复制到该目录
4. 重启 Obsidian，在设置中启用 Feishu Sync 插件

**Gitee 仓库**：https://gitee.com/hongjian\_Ai/feishu-sync

---

## 🗺️ 后续规划

* 支持选择性同步（按文件夹/标签过滤）
* 同步历史记录与回滚
* 飞书表格/多维表格支持
* 更多冲突解决策略（可视化 diff 对比）
* 移动端支持（通过 Obsidian Sync 中转）

---

## 🤝 参与贡献

Feishu Sync 是开源项目，欢迎提交 Issue 和 PR：

* **Gitee**：https://gitee.com/hongjian\_Ai/feishu-sync

如果你也在用 Obsidian + 飞书的组合，不妨试试这个插件，让知识真正流动起来。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImkIcetKf2R68VBM5icvTTX7zj1y7RekeFHal8mpPGDsncEwXDP7YP0eOQE5JPh9E3pYtiaC6AyFMgr2NrJyFeic5oDQmu1ZqZhVe4/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

爱唠叨的Nil

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

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