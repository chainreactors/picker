---
title: 更新 GitHub 上 fork 的项目
url: https://blog.upx8.com/3186
source: 黑海洋 - WIKI
date: 2023-01-16
fetch_date: 2025-10-04T03:59:50.132726
---

# 更新 GitHub 上 fork 的项目

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 更新 GitHub 上 fork 的项目

发布时间:
2023-01-15

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
14210

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

[同步一个 fork](https://blog.upx8.com/go/aHR0cHM6Ly9nYW9oYW95YW5nLmdpdGh1Yi5pby8yMDE1LzA0LzEyL1N5bmNpbmctYS1mb3JrLw)

[取消回复](https://blog.upx8.com/3186#respond-post-3186)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")