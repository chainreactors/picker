---
title: 工程化开发skills : superpowers
url: https://mp.weixin.qq.com/s/_74brftyujY74e5mI9Lysw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:07:48.940833
---

# 工程化开发skills : superpowers

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/smrEGbtBXaXlia56rlOSoyTSicSPlOENGMe6c9mXyloK2D1MicJwQmia7gjicRcsNUb7gj804QmRT8T3fuxtTibia4EAmNFvg9UdUqjC0yiarIEXECw/0?wx_fmt=jpeg)

# 工程化开发skills : superpowers

原创

信安路漫漫
信安路漫漫

信安路漫漫

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 前言

在用AI做项目的过程中，发现前期用起来还行，随着项目越来越大会发现项目越来越乱，AI这里改一下哪里改一下，造成这个的原因就是AI没有规划，完全就是凭感觉去写。

而今天这个skills就是解决这个问题，在编写代码以前，先聊透需求然后再去写，这样写出来的代码更加容易维护。安装以后Claude Code 将自动走 Brainstorm → Planning → TDD → 执行 → Review 全流程，这样代码质量将有质的飞跃。

#

# 安装与配置

可以连外网的可以直接通过插件商城进行安装，

插件安装命令

```
# 1. 安装插件（官方市场）/plugin install superpowers@claude-plugins-official# 或者通过 Superpowers 市场（部分版本）/plugin marketplace add obra/superpowers-marketplace/plugin install superpowers@superpowers-marketplace
```

本次我通过自动下载进行安装。

https://github.com/obra/superpowers/tree/main/skills

从上面的链接中下载项目代码，然后将skils文件的目录中的内容放到你的项目目录skill下。例如我的项目目录path\.claude\skills

![0](https://mmbiz.qpic.cn/mmbiz_png/smrEGbtBXaWTbB1pju6uicj9wzCic8U6HdibHG2kdsK8yZURJm9UWc49jpCepX9pKkTecQOZgOp0wKJp1alA8pKOOofLWfHWdStN7fY18mP6RU/640?wx_fmt=png&from=appmsg)

# 核心技能

Superpowers并非单一的skills，它包含了多个skills，可以相互组合进行使用。如下图所示

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/smrEGbtBXaVSMogAwIdnUFwFk5iayjFXs906XibzNDgCthNSuMxOibUficTaExz6eicZPHlDcW56lsvdmep4bodDUPLpiaIZib611FlfASS7Pgf9UA/640?wx_fmt=png&from=appmsg)

目前使用较多的就是brainstorming，Write Plan，executing-plans，test-driven-development这几个

## 1）brainstorming 头脑风暴

该skill会促使Claude交互式澄清需求、生成用户故事、界面草图想法等，帮你把模糊需求变成清晰规格。

![0](https://mmbiz.qpic.cn/mmbiz_png/smrEGbtBXaVdq8UyKHsozVHzHF1jow0ha3IeJsyKzNgUwRiaMV9icBzPUGyGc8sJFTMVv2Ye8M2C3kJ1JTuAzUUPWHzA4OXYica1AQo0y0FwY8/640?wx_fmt=png&from=appmsg)

如下图，他会让你一步步选择你想要使用的方案等技术架构

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/smrEGbtBXaXibib1qp0icJ7GUPMEIgosya8j8FV1LWjeOj9AcdzIGeBlS2DutjHqEWH70TqalnopW1ssV7FicBVswDkyGqedEeRWHBgvrXbIZsY/640?wx_fmt=png&from=appmsg)

## 2）Write Plan 编写实施计划

将设计转化为极细粒度的任务（每个任务约 2-5 分钟），包含精确的文件路径、完整代码和验证命令，杜绝模糊的占位符。

## 3）executing-plans  执行计划

作为子代理模式的备选方案，支持按计划逐个执行任务，并在每个任务完成后设置检查点供人工确认。

## 4）subagent-driven-development（子代理驱动开发）

为每个计划任务派发独立的子代理执行，避免上下文污染。完成后强制进行“规格合规”与“代码质量”两阶段审查。

## 5）dispatching-parallel-agents（并行子代理）

当存在多个互不依赖的任务时，支持同时派发多个子代理并行处理，大幅提升开发效率。

## 6）requesting-code-review（请求代码审查）

自动获取当前分支的 git diff，逐文件进行审查，按严重程度报告问题，关键问题会阻止后续推进。

## 7）receiving-code-review（接收审查反馈）

提供技术性接收反馈的结构化流程，帮助 AI 理解每条审查意见、验证其合理性并逐条处理。

## 8）using-git-worktrees（Git 工作树）

创建独立的 Git Worktree 和新分支，实现开发环境与主分支的物理隔离，确保主代码库的安全与稳定。

## 9）finishing-a-development-branch（分支收尾）

在所有测试通过后，提供合并到主分支、创建 PR、保留分支或丢弃分支的选项，并自动清理临时工作区。

## 10）test-driven-development（测试驱动开发 TDD）

这是一项铁律技能，强制遵循 RED-GREEN-REFACTOR 循环。要求必须先写一个会失败的测试，再写最简代码使其通过，最后重构。如果先写了生产代码再补测试，AI 会强制删除代码重来。

## 11）systematic-debugging（系统化调试）

提供四阶段根因分析流程（根因调查 → 模式分析 → 假设与实验 → 实施修复），杜绝“随机试错”式的低效排查。

## 12）verification-before-completion（完成前验证）

强制要求在宣布“任务完成”或“Bug 已修复”之前，必须运行新鲜的验证命令并检查完整输出，防止 AI 过度自信导致的“假阳性”。

## 13）writing-skills（编写技能）

允许用户使用 TDD 的方式编写新的 Skill，将团队专属的工程规范或特定框架的最佳实践封装为可复用的技能，实现 AI 能力的自我进化。

## 14）using-superpowers（使用 Superpowers）

作为技能系统的入门引导，包含“1% 规则”，用于自动触发和调度方法论约束，确保 AI 始终遵循工程化规范。

# 开发实践案例

#### 1. 需求澄清（Brainstorming）你向 AI 输入 /superpowers:brainstorm 我想开发一个带有用户验证功能的待办事项小程序（或数学闯关游戏）。

AI 会化身架构师，通过“苏格拉底式提问”追问细节。例如它会问：“目标用户是个人还是企业？需要支持手机号验证还是邮箱验证？是否需要数据备份功能？”

经过几轮问答和设计确认后，AI 会生成一份包含功能范围、技术限制和验收标准的 PRD（产品需求文档）。在这个过程中，AI 甚至可能帮你想到你最初没考虑到的需求（例如：管理入口是否需要密码保护）。

#### 2. 创建隔离工作区（Using Git Worktrees）

需求确认后，AI 会自动创建一个独立的 Git Worktree（如 .worktrees/ 目录）。这相当于为本次开发建立了一个物理隔离的“沙盒”，无论后续怎么试错，都不会污染主线代码。

#### 3. 任务拆解（Writing Plans）

你输入 /superpowers:write-plan，AI 会将宏大的游戏目标拆解为极细粒度的微型任务。例如：

* 任务1：创建项目目录结构（路径：./math-game，验证标准：包含 src、config、test 文件夹）。
* 任务2：编写用户验证接口（路径：./src/api/auth.js，验证标准：可正常接收手机号+验证码，返回登录状态）。每个任务都明确标注了预计耗时（2-5分钟）、文件路径和验证步骤。你需要审阅并输入 APPROVED 后，AI 才会动手。

#### 4. 并行执行与子代理驱动（Subagent-Driven + Parallel Agents）计划确认后，AI 不会在一个长上下文中写完所有代码，而是为每个任务派发一个“干净的”子代理（Subagent）去独立执行。

如果存在互不依赖的任务（例如同时开发“前端用户管理页面”、“后端权限 API”和“单元测试”），AI 会触发 dispatching-parallel-agents，同时派发多个子代理并行处理。每个子代理在独立的工作树中编译和运行，最后由主代理合并，完美避免了多代理修改同一文件导致的“车祸现场”。

#### 5. 测试驱动开发（TDD）

在编写具体业务代码时，AI 会强制执行 RED-GREEN-REFACTOR 循环：

* RED：先写一个会失败的测试用例。
* GREEN：编写最少的代码让测试通过。
* REFACTOR：重构优化代码。如果 AI 试图先写业务代码再补测试，Superpowers 会强制它删掉重来。

#### 6. 两阶段代码审查（Requesting Code Review）

每个子代理完成任务后，必须经过两轮审查：

* 第一轮（规格合规审查）：审查代理会拿设计文档逐条对照，检查“做没做对”，逐行验证需求是否真的实现。
* 第二轮（代码质量审查）：检查命名、结构、复杂度等质量问题。只有两轮审查都通过，任务才会被标记为完成。

#### 7. 完成分支与收尾（Finishing a Development Branch）

当所有 12 个微型任务全部完成且通过测试后，AI 会验证所有测试通过，提供合并到主分支、创建 PR 或清理 Worktree 的选项，并自动完成代码的合并与清理工作。

最终产出：通过这套严密的流程，AI 最终能交付一个包含完整页面（如关卡地图、答题、结算、错题本、题库管理），支持多种题型和移动端适配的高质量代码文件。整个过程中，AI 产出的代码质量与有经验的工程师写的没有明显差距，且几乎没有返工。

# 参考链接

https://cloud.tencent.com/developer/article/2668308

https://github.com/squallopen/superpowers-zh-adapters

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Rzo6rPw2nBzeSE9F8n8h6enwOQRic7J3SE7afEypJIw6rfTP291hkrrVzeuGMOlj17RGwbv8wJibtdQnmamtGNmQ/0?wx_fmt=png)

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