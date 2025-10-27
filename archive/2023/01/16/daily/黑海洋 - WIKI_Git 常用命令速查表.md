---
title: Git 常用命令速查表
url: https://blog.upx8.com/3185
source: 黑海洋 - WIKI
date: 2023-01-16
fetch_date: 2025-10-04T03:59:50.641734
---

# Git 常用命令速查表

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Git 常用命令速查表

发布时间:
2023-01-15

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
14383

[![常用Git流程图.png](https://imgcdn.p3terx.com/post/20181112070741.png)](https://imgcdn.p3terx.com/post/20181112070741.png)

## 创建版本库

```
$ git clone <url>                  #克隆远程版本库
$ git init                         #初始化本地版本库
```

## 修改和提交

```
$ git status                       #查看状态
$ git diff                         #查看变更内容
$ git add .                        #跟踪所有改动过的文件
$ git add <file>                   #跟踪指定的文件
$ git mv <old><new>                #文件改名
$ git rm<file>                     #删除文件
$ git rm --cached<file>            #停止跟踪文件但不删除
$ git commit -m "commit messages"  #提交所有更新过的文件
$ git commit --amend               #修改最后一次改动
```

## 查看提交历史

```
$ git log                    #查看提交历史
$ git log -p <file>          #查看指定文件的提交历史
$ git blame <file>           #以列表方式查看指定文件的提交历史
```

## 撤销

```
$ git reset --hard HEAD      #撤销工作目录中所有未提交文件的修改内容
$ git checkout HEAD <file>   #撤销指定的未提交文件的修改内容
$ git revert <commit>        #撤销指定的提交
$ git log --before="1 days"  #退回到之前1天的版本
```

## 分支与标签

```
$ git branch                   #显示所有本地分支
$ git checkout <branch/tag>    #切换到指定分支和标签
$ git branch <new-branch>      #创建新分支
$ git branch -d <branch>       #删除本地分支
$ git tag                      #列出所有本地标签
$ git tag <tagname>            #基于最新提交创建标签
$ git tag -d <tagname>         #删除标签
```

## 合并与衍合

```
$ git merge <branch>        #合并指定分支到当前分支
$ git rebase <branch>       #衍合指定分支到当前分支
```

## 远程操作

```
$ git remote -v                         #查看远程版本库信息
$ git remote show <remote>              #查看指定远程版本库信息
$ git remote add <remote> <url>         #添加远程版本库
$ git fetch <remote>                    #从远程库获取代码
$ git pull <remote> <branch>            #下载代码及快速合并
$ git push <remote> <branch>            #上传代码及快速合并
$ git push <remote> :<branch/tag-name>  #删除远程分支或标签
$ git push --tags                       #上传所有标签
```

[取消回复](https://blog.upx8.com/3185#respond-post-3185)

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