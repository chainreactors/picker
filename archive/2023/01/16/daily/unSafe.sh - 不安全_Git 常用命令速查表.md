---
title: Git 常用命令速查表
url: https://buaq.net/go-145614.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:48.318601
---

# Git 常用命令速查表

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

![](https://8aqnet.cdn.bcebos.com/344da3b2db277636e2c4abc207dddb36.jpg)

Git 常用命令速查表

创建版本库$ git clone <url> #克隆远程版本库$ git init
*2023-1-15 14:38:0
Author: [blog.upx8.com(查看原文)](/jump-145614.htm)
阅读量:28
收藏*

---

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

文章来源: https://blog.upx8.com/3185
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)