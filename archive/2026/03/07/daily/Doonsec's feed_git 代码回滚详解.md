---
title: git 代码回滚详解
url: https://mp.weixin.qq.com/s/NnJnXFlt6CYH7hr_7NpBMg
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:36.060744
---

# git 代码回滚详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bCZqF8oBiayaiakNjcf8IqfZSdH6H9lZ1icDo7jlBQLV2ibvMS9mH3Oq3p4KxozvwV03icP7sIh2AGyy2zVUFLA4L1KZb9F8xZ8AwgZic8FMzicibCw/0?wx_fmt=jpeg)

# git 代码回滚详解

原创

静观云起
静观云起

码云精炼

![]()

在小说阅读器中沉浸阅读

在日常的软件开发过程中，团队成员通常会使用**Git**作为版本控制工具，来管理代码的变更、协作开发以及维护项目的稳定版本。

一 常见开发场景

✅多分支开发场景：

为了并行开发不同特性功能或修复不同bug，团队往往会从主干分支master,创建多个功能分支,如 `feature-A`、`feature-B，进行并行开发。`

`✅多分支合并场景：`

`当特性功能或修复bug开发完成后，开发者会将对应的分支feature-A、feature-B，合并到目标分支sit-test中，以集成代码、进行集成测试。`

`✅合并冲突场景：`

`在合并过程中，如果两个分支对同一部分代码做了不同的修改，就会发生冲突(conflict)，需要手动在线或本地解决冲突后才能完成合并。`

`二 需要回滚的场景`

**`✅`合并后出现问题**

1. 合并分支(如将 feature-A合并到sit-test)后，发现新代码引入了**Bug**或**功能异常**。
2. 合并后代码到sit-test后，无法正常编译、运行，或影响了系统的稳定性。

****`✅`**解决冲突后结果不如预期**

1. 在解决合并冲突时，可能选择了错误的代码版本，或者合并后的逻辑不符合预期。
2. 解决冲突后没有充分测试，导致线上或测试环境出现问题。

****`✅`**误合并或合并了错误的分支**

1. 可能误将某个**不应该合并的分支如feature-C**合并到了目标分支sit-test。
2. 或者合并的时机不对，比如尚未完成的功能被提前合并到集成测试分支sit-test。

****`✅`**影响团队协作**

1. 合并后的代码推送到了远程仓库(如GitHub)，可能影响其他团队成员拉取代码、继续开发或部署。
2. 为了保证团队后续工作基于正确的代码状态，需要将分支回滚到稳定或预期的版本

三 本地提交的回归

`在本地分支提交，未推送到远程分支，有2种方式回滚`

`方式一 git reset`

`回滚到指定版本，将当前分支的HEAD指针移动到指定的提交，并且可以选择是否保留工作目录和暂存区的更改。`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayZvBhO9gPDibJcSv4b22wNLsD5MaCgwnWrUTCiaNvJ3UkUq1NqiaBHHGqr80C9TRBVyR8AXyojZ3PAILVRXtzPkWPNgnE6OiaNuIJ0/640?wx_fmt=png&from=appmsg)

`✅ 回滚到指定提交并保留更改`

`回滚到某个提交，但保留工作目录和暂存区的更改，可以使用--soft`

```
git reset --soft <commit-hash>
```

`说明：<commit-hash>是你想要回滚到的提交的哈希值。执行该命令后，HEAD指针会移动到指定的提交，但工作目录和暂存区的文件不会发生变化。`

###### ****`✅`****回滚到指定提交并丢弃更改

回滚到某个提交，并且丢弃工作目录和暂存区的更改，可以使用`--hard`

```
git reset --hard <commit-hash>
```

`说明：执行该命令后，HEAD指针会移动到指定的提交，并且工作目录和暂存区的文件都会被重置到该提交的状态。`

`✅ 回滚到指定提交并保留工作目录的更改`

`回滚到某个提交，但保留工作目录的更改，可以使用--mixed`

```
git reset --mixed <commit-hash>
```

`说明：该命令后，HEAD指针会移动到指定的提交，工作目录的文件会保留，但暂存区的更改会被丢弃`

`方式二 git revert

git revert是另一种常用的回滚方式。与git reset不同，git revert不会移动HEAD指针，而是创建一个新的提交来撤销某次提交的更改。这种方式更适合在公共分支上使用，因为它不会改变提交历史。

![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayY0vJ3WVn2ia3ITAIwCGk2v2XRpCfBgEBKcjibwJP8SA4lGTgliaEp6IkicUGXytctc0ibFKPy1qkjV85vnoAYoQ1vlw2iaibykxRKQJM/640?wx_fmt=png&from=appmsg)

###### ✅ 撤销某次提交

要撤销某次提交，可以使用以下命令`

```
git revert <commit-hash>说明：这里的
```

`<commit-hash>是你想要撤销的提交的哈希值。执行该命令后，Git会创建一个新的提交，该提交会撤销指定提交的更改。`

###### **`✅ 撤销连续的多次提交`**

如果你需要撤销连续的多次提交，可以使用以下命令

```
git revert <oldest-commit-hash>^..<latest-commit-hash>
```

说明：该命令会撤销从`<oldest-commit-hash>`到`<latest-commit-hash>`之间的所有提交

四 远程仓库推送回滚

本地分支代码已推送到远程分支，有2种方式回滚

方式一 git reset

彻底删除远程仓库中的某些提交，可以使用git reset来回滚本地提交，然后使用git push --force强制推送到远程仓库。**注意：该操作会修改提交历史history，可能会影响其他开发者的代码，请谨慎使用.。**

**首先，使用`git log`找到你想要回滚到的提交的哈希值**

**<1> 回滚本地分支**

**然后执行以下命令**

```
git reset --hard <commit-hash>
```

说明：该命令会将HEAD指针移动到指定的提交，并丢弃之后的提交。

###### <2> 强制推送到远程分支

接下来，使用以下命令将回滚后的提交强制推送到远程分支

```
git push --force origin <branch-name>
```

`说明：执行该命令后，远程分支的提交历史将被修改，回滚之后的提交将被删除`

`方式二 git revert`

`首先，使用git log找到你想要撤销的提交的哈希值`

`<1> 回滚本地分支`

`然后执行以下命令`

```
git revert <commit-hash>
```

`说明：执行该命令后，Git会创建一个新的提交来撤销指定提交的更改`

`<2> 推送到远程分支`

`将新的提交推送到远程仓库`

```
git push origin <branch-name>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YFxLNg1Bibfnia4huCODlTdyh6PTbL1pic45RaY9PANbJVIia0XOz1gV28f9BHd4341P1lpqQwn0cRGBjHPbHYmYIQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

码云精炼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

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