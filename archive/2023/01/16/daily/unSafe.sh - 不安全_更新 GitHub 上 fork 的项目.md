---
title: 更新 GitHub 上 fork 的项目
url: https://buaq.net/go-145612.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:47.759985
---

# 更新 GitHub 上 fork 的项目

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

更新 GitHub 上 fork 的项目

为 fork 分配远程链接使用 git remote -v 查看远程状态。添加一个将被同步给 fork 远程的上游仓库。git remote ad
*2023-1-15 14:40:0
Author: [blog.upx8.com(查看原文)](/jump-145612.htm)
阅读量:25
收藏*

---

## 为 fork 分配远程链接

* 使用 `git remote -v` 查看远程状态。
* 添加一个将被同步给 fork 远程的上游仓库。

```
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

* 再次查看状态确认是否配置成功。

```
git remote -v
# origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
# origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

## 同步 fork

* 从上游仓库 fetch 分支和提交点，传送到本地，并会被存储在一个本地分支 `upstream/master`

```
git fetch upstream
```

* 切换到本地主分支（如果不在的话）

```
git checkout master
```

* 把 `upstream/master` 分支合并到本地 `master` 上，这样就完成了同步，并且不会丢掉本地修改的内容。

```
git merge upstream/master
```

如果想更新到 GitHub 的 fork 上，直接 `git push origin master` 就好了。

## 参考

[同步一个 fork](https://gaohaoyang.github.io/2015/04/12/Syncing-a-fork/)

文章来源: https://blog.upx8.com/3186
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)