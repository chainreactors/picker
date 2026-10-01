---
title: AgentTeams Dashboard v1.2.5：68 个 commit，把「自己更新自己」做进去了
url: https://mp.weixin.qq.com/s/oGpGUp0hBF6cC50108IpwQ
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:57:06.774029
---

# AgentTeams Dashboard v1.2.5：68 个 commit，把「自己更新自己」做进去了

# AgentTeams Dashboard v1.2.5：68 个 commit，把「自己更新自己」做进去了

原创

Nil2024
Nil2024

鸿渐在路上

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本期导读：v1.2.5 已于 2026-09-30 发布。从 v1.2.4.9 到 v1.2.5 共合入 **68 个 commit、触及 167 个文件**，其中 **21 个功能与修复、6 个重构、5 个测试与 CI、17 篇文档、13 项工程与依赖治理**。本文按这五类逐条展开，所有条目均取自 GitHub Compare API 与官方 CHANGELOG，未做删减与推测。

如果你在用 AgentTeams Dashboard，大概遇到过这些场景：想升级版本却只能改 compose 文件重新 `docker pull`；多实例部署时页面提示「有新版本」，刷新、无痕、清缓存都不管用；`npm audit` 挂着 8 个高危不敢动。

v1.2.5 把这三件事一次处理完，并且顺手把 README 的定位语改成了 **Mission Control**。

AgentTeams Dashboard 是 AgentTeams 的 **Mission Control**——基于 Next.js 16 + React 19 的操作台，让操作者实时督导多智能体团队：集群拓扑、带人工干预的任务看板、具备运行时感知渲染的 Matrix 聊天、RBAC 与审计治理，以及 AI 诊断助手。

项目地址：github.com/agentteams-group/agentteams-dashboard

## 一、版本速览

| 项目 | 内容 |
| --- | --- |
| 发布版本 | v1.2.5（2026-09-30） |
| 容器镜像 | higress-registry.cn-hangzhou.cr.aliyuncs.com/agentteams/agentteams-dashboard:v1.2.5 |
| 变更规模 | 68 个 commit / 167 个文件（自 v1.2.4.9） |
| 预发迭代 | v1.2.5-beta.1 → beta.5，五轮全部在 09-30 当天 |
| 依赖治理 | 生产依赖高危漏洞 8 → 0 |
| 运行时 | Node 20 → Node 22 LTS |
| 主要贡献者 | @nillikechatchat（66）、@shiyiyue1102（2） |
| 许可归属 | higress-group |

### 68 个 commit 的分布

| 类型 | 数量 | 说明 |
| --- | --- | --- |
| feat / fix | 21 | 功能与修复，本次主角 |
| docs | 17 | 含 4 篇新增规范文档 |
| chore | 13 | 依赖、运行时、lint、4 次发版 |
| refactor | 6 | 五个大组件拆分 + 清除 any |
| 无前缀 | 6 | 3 个 Merge 与 3 条 README 图片调整 |
| test / ci | 5 | 测试覆盖与 CI 门禁 |

### 167 个文件改在哪

| 目录 | 文件数 |
| --- | --- |
| src/components | 65 |
| src/lib | 23 |
| src/app | 21 |
| .monkeycode（规格与任务清单） | 10 |
| .github（工作流） | 6 |
| src/plugins | 5 |
| src/hooks | 4 |
| deploy / install | 4 |

**超过六成改动落在组件层**——这不是一次「加功能」的版本，是一次「让程序能自己更新自己」的版本。

## 二、21 个功能与修复

### 1. 应用内热补丁（本次最重）

**完整链路**（`src/app/api/self-update/route.ts` + `src/lib/hotfix.ts`）：

`` ` `` POST /api/self-update → 从最新正式 Release 下载 dashboard-hotfix-\*.tar.gz → sha256 校验 → tar 解包完整性检查（server.js / BUILD\_ID） → 原子热替换应用目录（旧版本保留于 app.prev） → 进程三级强杀（SIGTERM → SIGKILL → exit） → 容器监管方拉起 `` ` ``

**三个设计约束**：

* **无 docker socket、无旁路容器**

  ——`docker restart` 策略与 `k8s restartPolicy` 行为一致
* 页面轮询服务器版本号变化后自动刷新（5 分钟超时）
* 安装器部署默认 `--restart unless-stopped`，保证进程退出后被拉起

**这里有个值得记的演进**。commit 历史里能看到一条完整的路线：

`` ` `` feat(dashboard): container self-update via watchtower sidecar   ← 先用 watchtower feat(dashboard): in-app hot patch replaces watchtower sidecar    ← 自己的热补丁取代它 `` ` ``

**先用现成方案跑通，再换成自研。** watchtower 那一版被完整替换掉了。

### 2. 按钮式更新

设置面板新增「更新」tab（`src/components/dashboard/settings/update-tab.tsx`）：

| 功能 | 说明 |
| --- | --- |
| 版本信息 | 展示版本号 / 构建号 / 构建时间 |
| 检查更新 | 一键比对服务器与上游 Release |
| 立即更新 | 整页刷新携带 `?_b=` 时间戳查询参数，穿透反向代理缓存 |

配套：

* `GET /api/dashboard-build`

  只读构建身份接口（buildId + version + builtAt，`Cache-Control: no-store`，免认证）
* **chunk 加载失败自愈**

  ——懒加载 chunk 被新部署清除时，会话内自动整页刷新一次
* `feat(update): distinguish same-version rebuilds from real new versions`

  ——**版本号一致但构建号不同时，提示改为「同版本新构建，建议刷新同步」**，只有真实版本差异才显示「发现新版本」

### 3. 任务看板切换修复

**现象**：从 chat 首次点击「任务看板」无响应，要点第二次。

**根因**（commit `410018a`）：

useActiveSection() 初始解析 effect 随组件挂载重复执行，同 commit 同步挂载路径下把 store 回滚为旧 hash 值。

**修法**：改为模块级 `once` 标记，并附「remount 不回滚」回归测试。

**顺带修的**：`chat 会话侧栏拖拽中途切换区块时 pointermove / pointerup 监听器泄漏`——处理器入 ref，卸载统一移除。

### 4. Worker 环境编辑与网关校验

* `feat: edit worker environment and verify saved gateway access`

  （**出现两次**，一次在 PR 合并前、一次在合并后）
* `test(workers): gateway-probe route e2e cases`

  ——补了端到端用例

**验证从 UI 一直做到路由层。**

### 5. MCP 可信目录

* `feat(mcp): expose catalog servers + trusted-name helper`

  （B7 21.1 groundwork）
* `feat(mcp): trusted-catalog default pre-check for new workers`

**新建 Worker 前先做可信目录预检**——这是一个安全边界的收紧。

### 6. 会话回放

`feat(replay): shareable sanitized session replays`（D3 MVP）

**可分享的、经过脱敏的会话回放。** 与 v1.2.4.9 的「Matrix 聊天运行时感知渲染」是同一条线。

### 7. 存储回归测试与凭据回退

`feat(storage): regression suite + installer RUSTFS_* credential fallback`

安装器支持 `RUSTFS_*` 凭据回退——**对象存储从 MinIO 向 RUSTFS 迁移的配套**。

### 8. 运行时一致性清扫

`feat(dashboard): runtime consistency sweep - cards, KB gating, capability doc`（B2）

统一了卡片、知识库门控与能力文档。

### 9. 贡献者入口基线

`feat(dashboard): contributor entry baseline - templates, gallery, dead link`（D1）

模板、画廊与死链检查——**这是给外部贡献者铺路**。

### 10. 跨平台脚本

`feat(scripts): cross-platform dev/build/start wrappers`（A7）

### 11. 三条收尾修复

| commit | 内容 |
| --- | --- |
| `fix(test): await the readdir assertion in server-package.test` | CI 变绿 |
| `fix(scripts): mkdir -p hotfix bundle output dir` | 热补丁包输出目录 |
| `fix(config): drop duplicate readFileSync import` | next build 类型检查 |

## 三、五个 beta 修了什么

**这一节比功能列表更有信息量**——它记录的是「热更新」这个功能自身被反复打磨的过程。

| 版本 | 修的是什么 |
| --- | --- |
| **beta.1** | 热更新首次交付；任务看板修复；chunk 失效自愈；发布规范 docs/RELEASE.md |
| **beta.2** | 检查更新语义修正；`/api/dashboard-build` 新增 version 字段 |
| **beta.3** | **热更新核心缺陷** ：热替换成功后进程退出可能被路由执行上下文吞掉（主进程存活继续服务旧构建），导致「API 报新构建号、页面一直旧构建号」且刷新与无痕均无法收敛。改为三级终止 |
| **beta.4** | 缓存层问题：跳转追加时间戳强制反代/CDN 回源；构建号接口 no-store |
| **beta.5** | **彻底修复「页面构建号与服务器构建号不一致」** |

### beta.5 的根因值得单说

同一次构建内 **Turbopack 的 client / server worker 各自加载 next.config**，时间戳构建号被求值两次——页面内联 A、服务端文件 B，**永久分裂**。

**修法是构建号确定化**（`src/lib/build-id.ts`），三级回退：

`` ` `` DASHBOARD\_BUILD\_ID env  →  git short sha  →  .next/.build-id-lock（10 分钟锁文件） `` ` ``

CI 镜像经 `--build-arg DASHBOARD_BUILD_ID=${VERSION}` 注入，**镜像构建号即版本号**。

**同时把升级语义从构建号门控切成版本号门控**——同版本不同构建号视为「已是最新」，只有真实版本差异才提示升级。

## 四、6 个重构：把五个大组件拆开

| 原文件 | 拆成 |
| --- | --- |
| knowledge-section.tsx | knowledge/ 模块 |
| **ChatRoom.tsx** | hooks + components |
| projects-section.tsx | projects/ 模块 |
| wen-tian/index.tsx | 聚焦模块 |
| knowledge-graph3d.tsx | knowledge-graph3d/ 模块 |

**每个拆分都配了一篇 wiki 同步**（docs 下 5 篇 `docs(wiki)` commit）——**拆完立刻把架构文档跟上，这是纪律**。

### 还有一条更硬的：清除 any

`` ` `` refactor(types): eliminate all explicit any from non-test source   (A6.2) chore(types): restore no-explicit-any as error, enable noImplicitAny (A6.3) `` ` ``

**把 `any` 从「允许」改回「报错」。** 对应 `chore(lint): clear the eslint baseline to zero warnings`（A6.1）——**告警基线清零**。

## 五、5 个测试与 CI 门禁

| commit | 内容 |
| --- | --- |
| `test(setup): fix refreshEffective mock leak via BackendProbeFn seam` | **引入 BackendProbeFn 测试缝** |
| `test(security): extend coverage to security-critical modules` | **安全关键模块补覆盖** |
| `test(workers): gateway-probe route e2e cases` | 网关探测端到端 |
| `ci(upstream): installer drift cron + contract baseline` | **上游漂移定时检查 + 契约基线** |
| `ci(alert): CI failure issue alert + blocked-task prerequisites` | **CI 失败自动开 issue** |

**`docs: ... add consistency gate to CI`（A4）把文档一致性检查也做成了 CI 门禁**——README 里的说法过时就会挂。

## 六、13 项工程与依赖治理

### 依赖高危 8 → 0

| 包 | 变更 | 漏洞 |
| --- | --- | --- |
| adm-zip | 0.6.0 → 0.6.1 | GHSA-vwc7-r8mq-g2x9 / GHSA-7q85-xj36-vmfc（插件 zip 解包路径） |
| sharp | overrides 收紧 ≥0.35.4 | GHSA-rgj7-g3m4-5g8c |
| nanoid | 新增 ^3.3.18 | GHSA-2v37-7h3g-55p8（v3 线内修复） |
| lodash-es | ≥4.18 | GHSA-r5fr-rjxr-66jc / GHSA-f23m-r3pf-42rh（mermaid→chevrotain 链三处嵌套 4.17.23） |
| baseline-browser-mapping | ≥2.11.0 | GHSA-w5vr-8v7q-w6rv |

**一批 caret-range 补丁升级**（A9）：

* three 0.185.1 → 0.186.1
* @a2ui 0.10 → 0.12（**含 API 迁移**）
* lucide-react 0.525.0 → **1.48.0**（跨大版本）
* recharts 3.8.1 → 3.10.1
* vitest **4.1 → 5.0.2**（含 coverage-v8、显式 vite 7）

### 两个明确不修的漏洞

| 包 | 漏洞 | 理由 |
| --- | --- | --- |
| minio@8.0.7 链 stream-json ≤3.4.0 | GHSA-528h-pc64-c93x | minio 依赖 ^1.8.0，无 1.x 修复版，3.x 为跨大版本 |
| 同链 decode-uri-component ≤0.4.2 | GHSA-vcc3-ghjq-m6fr | 修复版 0.5.0 为 ESM-only，与 query-string 7 的 CJS require 不兼容 |

官方对利用面的判断是「**二者仅解析自有可信 S3 后端响应，利用面受限**」，且 audit 建议的 minio@7.1.3 降级是破坏性变更、与对象存储迁移方向冲突，**不采纳**。

### 运行时与其他

| commit | 内容 |
| --- | --- |
| `chore(runtime): migrate Node 20 → 22 LTS` + 恢复 isomorphic-dompurify 4.x | 运行时升级 |
| `chore(release)` × 4 | beta.1 / beta.2 / beta.5 / v1.2.5 四次发版 |

## 七、17 篇文档：其中 4 篇是新增规范

| 新增文档 | 内容 |
| --- | --- |
| **docs/RELEASE.md** | 发版规范：版本三方一致（tag = package.json = 构建代码）、镜像发布链路、热补丁快速通道、构建号自检、已知坑清单 |
| **docs/INTERFACES.md** | 协议契约，含 **org.agentteams.run v1** 正式定义 + 回退测试 |
| **docs/runtime-capabilities.md** | 运行时能力说明 |
| **docs/external-runtime-integration-assessment.md** | 外部编码 agent 运行时集成评估（B6） |...