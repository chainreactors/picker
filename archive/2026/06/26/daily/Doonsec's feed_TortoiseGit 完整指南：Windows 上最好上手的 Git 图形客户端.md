---
title: TortoiseGit 完整指南：Windows 上最好上手的 Git 图形客户端
url: https://mp.weixin.qq.com/s/d7b6KJOSDKNpQJfeWSSFxA
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:45:45.756125
---

# TortoiseGit 完整指南：Windows 上最好上手的 Git 图形客户端

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/I4ibOKsL0MdAFhJcozyKDMzmlPNEKlyZk1ic4VHSPibN074Vfc4RpcJm7SFCOkYPiatATUJGQ4sBDLqC98JYQfKfXsibnaSsRYNVxA8a1ZomXxN8/0?wx_fmt=jpeg)

# TortoiseGit 完整指南：Windows 上最好上手的 Git 图形客户端

原创

AI和效率工具
AI和效率工具

AI和提效工具实验记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如果你在 Windows 上写代码，又不想一开始就被一堆 Git 命令劝退，TortoiseGit 是一个很值得上手的工具。

它俗称“小乌龟 Git”，和很多人熟悉的 TortoiseSVN 一样，直接集成到 Windows 资源管理器里。你不需要打开命令行，只要在项目文件夹里点右键，就能完成克隆、提交、拉取、推送、分支管理、查看日志和解决冲突。

这篇文章按实际开发顺序整理：先安装，再配置，最后进入日常使用。

## 一、TortoiseGit 是什么？

TortoiseGit 是一个 Windows 资源管理器集成式的 Git 可视化客户端，完全免费、开源。

它最大的特点是：把常用 Git 操作都做成了右键菜单和图形界面。

你可以把它理解为：

> Git 的底层能力 + Windows 右键菜单 + 中文图形界面。

它适合这些场景：

* • 不熟悉命令行，但需要使用 Git 管理代码；
* • 团队使用 GitHub、Gitee、GitLab 等代码平台；
* • 希望通过图形界面查看提交记录、文件差异和分支状态；
* • 需要在 Windows 资源管理器里直接看到文件状态。

TortoiseGit 的核心特点包括：

* • 文件图标实时标记状态，例如绿色对勾、红色感叹号、黄色冲突标记；
* • 支持中文界面，克隆、提交、拉取推送、分支、日志都能图形化操作；
* • 底层依赖 Git for Windows，所以必须先安装 Git，再安装 TortoiseGit；
* • 兼容 GitHub、Gitee、GitLab；
* • 支持 HTTPS 和 SSH 密钥两种仓库访问方式。

一句话总结：TortoiseGit 不是 Git 的替代品，而是 Git 在 Windows 上的一层好用图形界面。

## 二、安装步骤：顺序很重要

### 1. 先安装 Git for Windows

TortoiseGit 底层依赖 Git for Windows，所以第一步必须先安装 Git。

进入 Git for Windows 官网下载安装包，安装时一路默认即可。对大多数新手来说，默认选项已经足够日常开发使用。

安装完成后，TortoiseGit 才能正确识别 Git 命令路径。

### 2. 再安装 TortoiseGit 本体

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I4ibOKsL0MdBHibsLCCd5xLlQA2ToNNWhzE0GAfRPzdr6cuciaaiansiaGbe0CEAJNWTb6kPLqSOV6iccuuINmz83C2ia8VoKyG4x6SKzRvsDJiaQf8/640?wx_fmt=png&from=appmsg)

接着去 TortoiseGit 官网下载对应系统的安装包。

如果你使用的是 64 位 Windows，就选择 64bit 版本。

安装过程一般保持默认即可：

* • 安装路径可以自定义；
* • 组件保持默认勾选；
* • 一路点击 Next 完成安装。

安装完成后，建议重启一次资源管理器或重启电脑，这样右键菜单和文件图标状态会更稳定。

### 3. 安装中文语言包

首次启动 TortoiseGit 时，会进入初始化向导。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I4ibOKsL0MdCkE62FDg0uyJskj7Tq4ZbSpVNrfMWvlia3rUI0S4XnjPiabuAqKGY19nicb7Z6ngRdRAfeDcib4Em2LnhsxU2U3eYQqgS9rOjWPMo/640?wx_fmt=png&from=appmsg)

如果你希望使用中文界面，需要先安装中文语言包，然后在向导中点击 Refresh 刷新语言列表，选择「中文（简体）」。

后续也可以通过：

> 任意文件夹右键 → TortoiseGit → 设置 → 常规 → 语言

切换界面语言。

## 三、基础全局配置

安装完成后，先做一次全局配置。

![](https://mmbiz.qpic.cn/mmbiz_png/I4ibOKsL0MdDRR6o1ich1GQQgZR1HdtsQegRrEZPxgyic6ia0licPlTnO48A5PmF0FHMKVqSMazqmftPEbb1HEEnx4s9GOBbMxmT3dopppta2PM8/640?wx_fmt=png&from=appmsg)

操作路径：

> 任意文件夹右键 → TortoiseGit → 设置

### 1. 检查 Git 路径

在「常规」设置里，TortoiseGit 通常会自动识别 Git for Windows 的安装目录。

如果没有自动识别，就手动选择 Git 的安装路径。

### 2. 配置用户名和邮箱

进入：

> Git → 配置

填写用户名和 Email。

这两个信息会写入每一次提交记录里，用来标识是谁提交了代码。

建议这样填写：

* • 用户名：开发者姓名或常用昵称；
* • Email：注册 GitHub、Gitee 或 GitLab 时使用的邮箱。

对应的 Git 命令是：

```
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

### 3. 配置 SSH 密钥（推荐）

如果你希望后续克隆、拉取、推送代码时不用反复输入账号密码，建议使用 SSH 密钥。

TortoiseGit 常见做法是使用 Puttygen 生成 PPK 密钥，然后把公钥上传到 GitHub、Gitee 或 GitLab 的 SSH Key 设置里。

配置好以后，克隆仓库时选择 SSH 地址即可。

新手也可以先使用 HTTPS 地址，等熟悉流程后再切换到 SSH。

## 四、日常开发核心操作

下面是日常开发中最常用的几个操作。每个操作都附上对应的 Git 命令，方便你理解它背后的含义。

## 1. 克隆远程项目：Git Clone

当你要把远程仓库下载到本地时，使用 Clone。

操作方式：

> 空白文件夹右键 → Git Clone

在弹窗中填写：

* • URL：粘贴仓库地址；
* • Directory：选择本地存放路径。

仓库地址可以是 HTTPS，也可以是 SSH。

对新手来说，HTTPS 更容易开始；如果已经配置好 SSH 密钥，推荐使用 SSH。

等价命令：

```
git clone 仓库地址
```

克隆完成后，本地会得到一份完整项目代码，并且自动关联远程仓库。

## 2. 提交本地修改：Commit

当你修改了代码，需要把这次改动保存到本地 Git 仓库时，就要提交 Commit。

操作方式：

> 项目空白处右键 → Git Commit

提交时建议按这几步做：

* • 勾选本次要提交的变更文件；
* • 填写清晰的提交备注；
* • 点击 Commit。

好的提交备注应该能说明“这次改了什么”，例如：

* • 修复登录失败问题；
* • 新增首页样式；
* • 优化订单列表加载速度；
* • 调整接口错误提示。

等价命令：

```
git add .
git commit -m "提交备注"
```

如果刚提交完发现备注写错了，或者漏了一个小文件，可以在未推送前勾选 Amend Last Commit，修正上一次提交。

注意：Amend 更适合修改尚未推送到远程的提交。

## 3. 同步远程代码：Pull 和 Push

团队开发时，本地代码和远程仓库需要经常同步。

这里最常用的是 Pull 和 Push。

### Pull：拉取别人最新代码

操作方式：

> 右键 → TortoiseGit → Pull

Pull 会从远程仓库拉取最新代码，并尝试自动合并到当前分支。

等价命令：

```
git pull origin 分支名
```

建议每天开始开发前先 Pull 一次，避免本地代码和远程代码差太多。

### Push：推送自己的提交

当你本地 Commit 完成后，需要把提交上传到远程仓库。

操作方式：

> Commit 完成后点击 Push，选择本地分支和远程分支，确认推送

等价命令：

```
git push origin 分支名
```

### Git Sync：高频一键同步面板

TortoiseGit 还提供 Git Sync 面板，把 Pull、Push、查看未推送提交等能力集中在一起。

如果你已经熟悉基本流程，Git Sync 会是日常使用频率很高的入口。

## 4. 分支管理

分支是 Git 开发中的核心概念。

常见做法是：主分支保持稳定，功能开发在独立分支上进行，开发完成后再合并回主分支。

### 新建分支

操作方式：

> TortoiseGit → Create Branch

输入分支名称，并勾选创建后自动切换。

例如：

* • feature-login；
* • fix-order-bug；
* • release-2026-06。

### 切换分支

操作方式：

> TortoiseGit → Switch/Checkout

选择目标分支后确认即可。

### 合并分支

常见流程是：

1. 1. 先切回主分支，例如 main 或 master；
2. 2. 选择 Merge；
3. 3. 选择要合并进来的功能分支；
4. 4. 解决可能出现的冲突；
5. 5. 提交并推送。

### 删除分支

可以在日志或分支列表中右键删除本地分支，也可以删除远程分支。

删除远程分支前要确认团队已经不再使用，避免误删他人的工作分支。

## 5. 查看提交日志：Show Log

Show Log 是 TortoiseGit 里非常实用的功能。

操作方式：

> 右键 → Show Log

你可以在这里看到：

* • 所有提交记录；
* • 每次提交的作者、时间和备注；
* • 每次提交修改了哪些文件；
* • 文件前后差异 Diff；
* • 分支合并轨迹。

常用操作包括：

* • 双击文件查看代码差异；
* • 选中两次提交对比版本；
* • 回滚某次修改；
* • Cherry-pick 挑选某个提交应用到当前分支。

如果团队里出现“这个功能是谁改的”“这个 bug 是哪次引入的”，Show Log 往往是最快的溯源入口。

## 6. 冲突解决

多人同时修改同一个文件时，Pull 或 Merge 可能会出现冲突。

出现冲突后，文件通常会显示黄色冲突标记。

操作方式：

> 冲突文件右键 → TortoiseGit → Resolve

TortoiseGit 会打开三方对比工具，通常可以看到：

* • 本地版本；
* • 远程版本；
* • 合并后的结果。

你可以选择：

* • 保留本地版本；
* • 保留远程版本；
* • 手动合并两边代码。

解决完成后，需要标记为已解决，然后重新 Commit，再 Push。

冲突不可怕，关键是不要盲目覆盖。遇到不确定的业务逻辑，最好先和相关同事确认。

## 7. 常用进阶功能

### Stash：临时储藏

当你手上有未提交改动，但需要临时切换分支时，可以使用 Stash。

它会先把当前改动临时保存起来，等你切回分支后再恢复。

适合这种场景：

> 功能写到一半，突然需要切到另一个分支修紧急 bug。

### Revert：还原提交

Revert 用来撤销某次已经提交的修改。

它不会直接删除历史，而是生成一个新的提交来抵消之前的提交。

因此，已经推送到远程的提交，通常更推荐用 Revert。

### Reset：重置提交

Reset 可以把本地仓库回退到某个提交。

它能力很强，但也更危险，尤其是 hard reset。

如果提交已经推送到远程，不建议随意使用 hard reset，否则可能影响团队其他人的历史记录。

### Diff：查看文件差异

单个文件右键选择 Diff，可以查看当前文件和仓库中版本的差异。

这是提交前自查代码的好习惯。

## 五、文件图标状态说明

TortoiseGit 会直接在资源管理器里给文件和文件夹加状态图标。

常见图标含义如下：

| 图标状态 | 含义 |
| --- | --- |
| 绿色对勾 | 文件已提交，没有新的修改 |
| 红色感叹号 | 文件已修改，但还没有提交 |
| 蓝色加号 | 新增文件，尚未加入版本控制 |
| 黄色感叹号 | 文件存在冲突，需要解决 |
| 灰色减号 | 文件已删除，等待提交 |

这些图标能让你不打开任何工具，也能快速判断项目当前状态。

## 六、常见问题

### 1. 右键没有 TortoiseGit 菜单怎么办？

可以按顺序检查：

* • 是否安装了正确版本，64 位 Windows 建议安装 64bit 客户端；
* • 是否安装完成后没有重启资源管理器；
* • 是否需要重启电脑；
* • 是否在 TortoiseGit 设置里关闭了某些右键菜单项。

大多数情况下，重启资源管理器或重启电脑就能恢复。

### 2. SSH 克隆时一直报密码或认证错误怎么办？

优先检查这几项：

* • 是否已经用 Puttygen 生成 PPK 密钥；
* • 是否把公钥上传到 GitHub、Gitee 或 GitLab；
* • TortoiseGit 设置里是否指定了正确的 SSH 客户端；
* • 克隆地址是否使用 SSH 地址，而不是 HTTPS 地址。

如果你只是临时使用，也可以先换成 HTTPS 地址克隆。

### 3. Push 时提示冲突怎么办？

通常说明远程分支已经有别人提交的新代码，而你本地还没有同步。

处理方式：

1. 1. 先 Pull 拉取远程最新代码；
2. 2. 如果有冲突，先解决冲突；
3. 3. 重新 Commit；
4. 4. 再 Push。

不要在不了解原因的情况下强制推送。

### 4. Amend 修改提交后推送报错怎么办？

Amend 会改写上一次提交的历史。

如果这次提交已经推送到远程，再 Amend 后直接 Push 可能会失败。

所以建议记住：

* • 未推送的提交：可以用 Amend 修正；
* • 已推送的提交：尽量不要 Amend；
* • 团队协作中：慎用强制推送。

## 七、推荐新手使用流程

如果你刚开始用 TortoiseGit，可以先记住这一套最小闭环：

1. 1. Git Clone：把远程项目克隆到本地；
2. 2. Pull：每天开发前先拉取最新代码；
3. 3. 修改文件；
4. 4. Commit：把本地修改提交到本地仓库；
5. 5. Push：把本地提交推送到远程；
6. 6. Show Log：有问题时查看历史和差异；
7. 7. Resolve：遇到冲突时解决冲突后再提交。

掌握这套流程后，日常开发基本就够用了。

## 总结

TortoiseGit 的价值，不是让你完全不用理解 Git，而是把 Git 的常用操作变得更直观。

它特别适合 Windows 用户、Git 新手，以及习惯图形化操作的开发团队。

如果你能理解 Clone、Commit、Pull、Push、Branch、Merge、Log、Conflict 这几个核心动作，再配合 TortoiseGit 的右键菜单，日常协作开发就会顺很多。

先用图形界面跑通流程，再慢慢理解背后的 Git 命令，这是一条非常适合新手的学习路径。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/I4ibOKsL0MdDIqvp6vDcv2HqdekyL3JDHW2vQpW4iaSegBwCiasoHhXGbxhK7sicWhKszfYzXOdj2bjPaadHTzUBYTZzOuzbzntH5tMKAOY8DKM/0?wx_fmt=png)

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