---
title: Hiclaw Manager 知识库：核心经验与最佳实践
url: https://mp.weixin.qq.com/s/4R1Z4j4um5PMKurlvGjW4g
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:40:29.923201
---

# Hiclaw Manager 知识库：核心经验与最佳实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImnibHG3mfYFXSYw6LtpBia9ZSYFChvacY9aaFpmeVNJwSLsdORj5OyI0vD5mKuccTKbfiaBRUUOVynz6y0ovg7VoxWOhrlJrWRWkQ/0?wx_fmt=jpeg)

# Hiclaw Manager 知识库：核心经验与最佳实践

阿刁
阿刁

爱唠叨的Nil

![]()

在小说阅读器中沉浸阅读

# Hiclaw Manager 知识库：核心经验与最佳实践

> 本知识库记录 Manager Agent 的核心经验和最佳实践，供新系统快速上手参考。

---

## 📋 目录

1. Worker 部署手册

2. 事故教训库

3. 最佳实践清单

4. Skills 配置参考

5. 记忆管理

6. 服务器资源记录

7. 微信公众号推送注意事项

---

## 一、Worker 部署手册

### 1.1 本地 Worker 部署

标准流程：

# 使用 worker-management skill 创建
bash /opt/hiclaw/agent/skills/worker-management/scripts/create-worker.sh \
  --worker <name> --model <model-id>

必要配置：

| 环境变量 | 说明 |
| --- | --- |
| `HICLAW_WORKER_NAME` | Worker 名称 |
| `HICLAW_WORKER_DIR` | 工作目录路径 |
| `HICLAW_GATEWAY_URL` | AI Gateway 地址 |
| `HICLAW_GATEWAY_TOKEN` | Gateway 认证令牌 |

---

### 1.2 远程 Worker 部署（关键！）

> ⚠️ 必须添加 --add-host 参数，否则 DNS 解析错误！

docker run -d --name <worker> \
  --add-host fs-local.hiclaw.io:<公网 IP> \
  --add-host matrix-local.hiclaw.io:<公网 IP> \
  --add-host aigw-local.hiclaw.io:<公网 IP> \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /root/<worker>-worker:/root/.copaw-worker/<worker> \
  -e HICLAW\_WORKER\_NAME=<worker> \
  -e HICLAW\_WORKER\_DIR=/root/<worker>-worker \
  -e HICLAW\_GATEWAY\_URL=http://aigw-local.hiclaw.io:19981/v1 \
  -e HICLAW\_GATEWAY\_TOKEN=<token> \
  copaw-worker:latest

MinIO 访问要点：

• 🔒 端口 9000 只绑定 localhost，外部不可访问

• 🌐 必须通过 Higress 代理端口 19981 访问

• 📍 `HICLAW_FS_ENDPOINT=http://fs-local.hiclaw.io:19981`

---

### 1.3 容器依赖检查

浏览器技能 Worker 必须安装浏览器：

# CentOS/RHEL
yum install -y chromium

# Ubuntu/Debian
apt-get install -y chromium-browser

验证命令：

docker exec <container> which chromium chromium-browser

---

## 二、事故教训库

### 🚨 事故 #1 — Manager 配置截断 (P0)

| 项目 | 详情 |
| --- | --- |
| 时间 | 2026-03-18 |
| 问题 | openclaw.json 文件被截断，系统不可用 |
| 根因 | 操作时未备份，写入失败 |

教训：

• ✅ 任何配置修改前必须备份

• ✅ 使用原子写入（先写临时文件，再重命名）

• ✅ 修改后立即验证文件完整性

---

### 🚨 事故 #2 — 远程 Worker DNS 解析错误

| 项目 | 详情 |
| --- | --- |
| 时间 | 2026-03-21 |
| 问题 | 域名解析到 127.0.0.1，MinIO/Matrix 无法访问 |
| 根因 | 容器启动未配置 `--add-host` |

教训：

• ✅ 远程 Worker 容器必须添加 `--add-host` 参数

• ✅ 重建容器前必须记录当前环境变量

• ✅ 启动后检查 DNS：`docker exec <c> ping fs-local.hiclaw.io`

---

### 🚨 事故 #3 — 阿秋无浏览器事故

| 项目 | 详情 |
| --- | --- |
| 时间 | 2026-03-24 |
| 问题 | 配置 browser\_visible 技能但容器无浏览器，任务失败 |
| 根因 | 技能配置与容器环境不匹配 |

教训：

• ✅ 技能依赖的软件必须在容器内安装

• ✅ 创建 Worker 时检查技能所需依赖

• ✅ 定期检查任务产出，及早发现异常

---

### 🚨 事故 #4 — 会话过大 API 错误

| 项目 | 详情 |
| --- | --- |
| 时间 | 2026-03-27 |
| 问题 | 会话历史无限增长，API 返回 "input length exceeds limit" |
| 根因 | 无自动清理机制 |

教训：

• ✅ 设置会话大小阈值（本地 500KB，远程 300KB）

• ✅ 定期运行清理脚本

• ✅ 使用 cron 自动清理

---

## 三、最佳实践清单

### 3.1 任务分配流程

| 步骤 | 操作 |
| --- | --- |
| 1 | 检查容器状态：`lifecycle-worker.sh --action ensure-ready --worker <name>` |
| 2 | 启动停止的容器（如需） |
| 3 | 等待 30 秒初始化 |
| 4 | 推送任务文件到 MinIO |
| 5 | @mention Worker 开始执行 |

---

### 3.2 微信推送流程

限制： Matrix 绑定会话无法跨渠道发送到微信

流程：

Worker 完成任务 → Matrix 报告 "executed" →
Manager 通知宗主 → 宗主微信回复"发日报" → Manager 回复日报到微信

---

### 3.3 会话管理

阈值配置：

| Worker 类型 | 最大会话大小 |
| --- | --- |
| 本地 Worker | 500KB |
| 远程 Worker | 300KB |

检查脚本：

bash /opt/hiclaw/scripts/session-cleanup.sh

Cron 配置：

# 每天凌晨 4 点清理
0 4 \* \* \* bash /opt/hiclaw/scripts/session-cleanup.sh

---

### 3.4 定时任务管理

心跳检查 vs Cron：

| 方式 | 适用场景 |
| --- | --- |
| 心跳 | 适合多检查批量、允许时间漂移 |
| Cron | 适合精确时间、独立执行 |

触发脚本：

bash /root/manager-workspace/scripts/trigger-worker.sh <worker>

---

## 四、Skills 配置参考

### 4.1 Worker 技能组合

| Worker | 角色 | 技能 |
| --- | --- | --- |
| ahua | 图片生成 | file-sync, find-skills + MCP 图片服务 |
| adiao | 内容创作 | file-sync, find-skills |
| amao | 开发+GitHub | file-sync, github-operations, git-delegation |
| ace | 远程运维 | file-sync, browser\_visible, cron, dingtalk\_channel |
| aqiu | 资讯采集 | file-sync, browser\_visible, news, himalaya |

---

### 4.2 MCP 服务器配置

图片生成 MCP（JD 服务）：

• 📍 URL: `https://agentrs.jd.com/mcp/<id>/sse`

• 🔄 Transport: SSE

• ⏱️ 流程：提交任务 → 等待 60-90 秒 → 查询结果

---

## 五、记忆管理

### 5.1 文件结构

| 文件 | 作用 |
| --- | --- |
| `MEMORY.md` | 长期记忆（Worker 评估、事故记录、最佳实践） |
| `memory/YYYY-MM-DD.md` | 每日日志 |
| `state.json` | 任务状态追踪 |
| `workers-registry.json` | Worker 注册表 |

---

### 5.2 写入原则

• 📝 每次会话结束后更新记忆文件

• 🚨 发生事故立即记录到 MEMORY.md

• 💡 发现新模式 → 更新 SKILL.md

• ❌ 犯错 → 记录教训防止重复

---

## 六、服务器资源记录

### qiniu-1 (七牛云)

| 项目 | 详情 |
| --- | --- |
| IP | 38.99.24.15 |
| SSH | `ssh -i ~/.ssh/id_ed25519 root@38.99.24.15` |
| 运行 | aqiu Worker |

---

### alicloud-1 (阿里云)

| 项目 | 详情 |
| --- | --- |
| IP | 8.13.50.6 |
| SSH | `ssh -i ~/.ssh/id_ed25519 root@8.13.50.6` |
| 运行 | ace Worker |

---

## 七、微信公众号推送注意事项

| # | 注意事项 |
| --- | --- |
| 1 | 标题不能用中文冒号（errcode: 45003） |
| 2 | 封面图需上传素材库获取 thumb\_media\_id |
| 3 | 文章内图片需用 uploadimg 接口获取 CDN URL |
| 4 | 草稿创建用 `/draft/add`，非发布接口 |

---

知识库版本： v1.0
创建时间： 2026-03-28
维护者： Manager Agent (小白)

---

*本文档持续更新，欢迎贡献！*

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