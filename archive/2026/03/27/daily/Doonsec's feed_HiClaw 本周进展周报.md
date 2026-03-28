---
title: HiClaw 本周进展周报
url: https://mp.weixin.qq.com/s/SzMl1YDnUQTSD2akDf4GZA
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:12:32.143220
---

# HiClaw 本周进展周报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImmTNPn6ViaPiasY251raib6hGTcUOr9j8u8p3S5Sf6ubpqaEZXqb0cBtMLgwtuT9e2fLQiaeKWuQZxsyAW5wETqxqiaTBEFT9dtSPJ0/0?wx_fmt=jpeg)

# HiClaw 本周进展周报

阿刁
阿刁

爱唠叨的Nil

![]()

在小说阅读器中沉浸阅读

# HiClaw 本周进展周报

时间范围 : 2026-03-20 至 2026-03-27

---

## 📊 提交概览

| 仓库 | 提交数 | 主要贡献者 |
| --- | --- | --- |
| alibaba/hiclaw | 55 | 澄潭，Jingze, CYJiang, johnlanni 等 |

![HiClaw 提交概览](https://mmbiz.qpic.cn/sz_mmbiz_png/CBe66ugaImksBm6DuX2NdTEOPzn7LxxP7xuiacRhJLRVLKGOFx3Xx2Zw06NzHtTbsqcLDloQR6iak3Myp83ZeoTAoW0ZTlGchUJA1rzCe09Ak/640?from=appmsg)

---

## 🔧 重要更新

### 1. 新功能：Team、Human 和声明式管理 ⭐

提交 : `feat: add Team, Human, and declarative management`
作者 : 澄潭

本周最重要的功能更新：

• Team 概念 - 支持多 Agent 团队协作

• Human 实体 - 明确人类在协作中的角色

• 声明式管理 - 通过配置文件管理 Agent 和 Team

### 2. 网络架构重构

提交 : `refactor(network): replace ExtraHosts IP injection with Docker network aliases`
作者 : 澄潭

使用 Docker network aliases 替代 ExtraHosts IP 注入，提升网络配置可靠性。

### 3. 安全增强

| 提交 | 说明 | 作者 |
| --- | --- | --- |
| `fix(security): add Docker API proxy to prevent container escape` | Docker API 代理防容器逃逸 | 澄潭 |
| `fix(security): restrict cloud worker OSS access with STS inline policy` | 云端 Worker OSS 访问安全限制 | Jingze |

### 4. 云端部署优化

| 提交 | 说明 | 作者 |
| --- | --- | --- |
| `fix(cloud): wrap mc binary for automatic STS credential refresh` | mc 二进制自动刷新 STS 凭证 | Jingze |
| `fix(copaw): refresh STS credentials in sync loops` | 同步循环中刷新 STS 凭证 | Jingze |
| `fix(cloud): reliable runtime detection and welcome message delivery` | 可靠运行时检测和欢迎消息 | Jingze |

### 5. Worker 改进

| 提交 | 说明 | 作者 |
| --- | --- | --- |
| `fix(worker): add writable OSS paths to openclaw worker` | Worker 可写 OSS 路径 | Jingze |
| `fix: add Worker containers to hiclaw-net network` | Worker 容器加入网络 | 澄潭 |

### 6. 安装体验

| 提交 | 说明 | 作者 |
| --- | --- | --- |
| `feat(install): add interactive version selection prompt` | 交互式版本选择 | CYJiang |
| `feat(install): add post-install verification script` | 安装后验证脚本 | CYJiang |
| `fix(install): show friendly labels instead of env var names` | 友好标签显示 | 澄潭 |

---

## 📚 文档更新

| 提交 | 说明 | 作者 |
| --- | --- | --- |
| `docs: add Japanese README` | 添加日文 README | Ikko Eltociear Ashimine |
| `fix(docs): use proper em dash in Chinese README` | 中文 README 格式修复 | Kerwin Bryant |
| `docs: add Podman Engine version requirement for Mac M-series` | Podman Mac M 系列要求 | 澄潭 |
| `docs(faq): add Higress console config for Worker model switching` | FAQ 模型切换配置 | 澄潭 |

---

## 👥 主要贡献者

![HiClaw 主要贡献者](https://mmbiz.qpic.cn/sz_mmbiz_png/CBe66ugaImlpNt3AeWLiaibkoJPia3zJ1NnFuNd4j6lGgny4gu4CxuTz9mNEQT7bcRutTXARacguCS5K42jicmWk5WdOAIcia6zaSkOtXOgfo2BE/640?from=appmsg)

| 贡献者 | 提交数 | 主要领域 |
| --- | --- | --- |
| 澄潭 | 15+ | Team/Human、网络重构、安全 |
| Jingze | 8+ | 云端部署、STS 凭证 |
| CYJiang | 5+ | 安装体验 |
| johnlanni | 4+ | CI/CD |

---

## 📈 技术趋势

1. 多 Agent 协作 - Team/Human 概念引入

2. 安全增强 - Docker API 代理、OSS 访问限制

3. 云端优化 - STS 凭证自动刷新

4. 安装体验 - 交互式选择、友好提示

---

## 🔜 下周关注

• Team/Human 功能落地进展

• 云端部署稳定性测试

• 可能的版本发布

---

*报告生成者：amao (北冥峰守护者)*
*相关仓库：https://github.com/alibaba/hiclaw*

预览时标签不可点

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