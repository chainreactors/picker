---
title: 从零开始学 Git 的基础操作
url: https://buaq.net/go-145618.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:50.791559
---

# 从零开始学 Git 的基础操作

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

从零开始学 Git 的基础操作

创建本地仓库初始化本地仓库（git init）切换路径到目标目录，执行 git init 命令行。cd /home/Git/test/ #进入一个
*2023-1-15 14:30:0
Author: [blog.upx8.com(查看原文)](/jump-145618.htm)
阅读量:24
收藏*

---

## 创建本地仓库

### 初始化本地仓库（`git init`）

切换路径到目标目录，执行 `git init` 命令行。

```
cd /home/Git/test/    #进入一个文件夹
git init              #初始化一个Git仓库
```

或者执行 `git init test` ，就会直接创建一个以 `test` 名来命名的文件夹

### 克隆远程仓库到本地（`git clone`）

也可以克隆远程仓库到本地，使用 `git clone` 后面跟仓库地址

```
git clone https://github.com/P3TERX/ServerStatus-V.git
```

如果是要克隆某个分支，使用 `git clone -b` 加分支名，后面再跟仓库地址

```
git clone -b server https://github.com/P3TERX/ServerStatus-V.git
```

## 管理本地仓库

在 Git 中文件有三种状态：已修改（`modified`）、已暂存（`staged`）、已提交（`committed`）。

用 Git 管理文件也可以简单的理解为**三个步骤：修改文件、跟踪文件、提交文件。**

### 修改文件

修改文件即是对文件的添加、编辑、删除等等，和普通修改文件的方法一致。

### 跟踪文件（`git add`）

创建文件和修改文件后需要把文件添加到仓库，即对文件进行跟踪。

添加一个文件时直接在终端输入 `git add` 后面空一格输入完整的文件名（包含后缀，如.txt）:

```
git add README.md
```

添加多个文件也类似， `git add` 后面空格输入完整的文件名，文件名之间用空格分隔：

```
git add README.md learn_git.txt
```

添加当前仓库里的所有文件时直接在终端输入 `git add .` ，注意此处末尾的 `.` 不要遗漏。

### 提交文件（`git commit`）

用 `git commit -m` 命令把文件提交到仓库，一次性会提交所有你已经添加的文件后面引号中的内容是你的提交说明，以便清楚地了解做了什么修改。

```
$ git commit -m "Modify function"
[master 77f3e3d] Modify function
 1 file changed, 26 insertions(+), 27 deletions(-)
```

> `$` 符号是使用终端时自动输入的，用户并不需要输入此符号。

### 查看文件状态（`git status`）

使用 `git status` 命令查看文件状态。

* **已修改（modified）** ———— 表示修改了文件，但还没保存到数据库中
* **已暂存（staged）** ———— 表示对一个已修改文件的当前版本做了追踪，使之包含在下次提交的快照中
* **已提交（committed）**———— 表示数据已经安全的保存在本地数据库中

## 管理远程仓库

### 添加远程仓库（`git remote add`）

使用 `git remote add [remote-name] [url]` 命令。

```
$ git remote add origin [email protected]:P3TERX/SSH-Key-Installer.git
```

`remote-name` 是给远程仓库气的别名，一般是 `origin` ，用户可以根据自己的需求自定义。

用 `git remote -v` 命令来查看当前添加的远程仓库地址

```
$ git remote -v
origin  [email protected]:P3TERX/SSH-Key-Installer.git (fetch)
origin  [email protected]:P3TERX/SSH-Key-Installer.git (push)
```

### 推送数据到远程仓库（`git push`）

使用 `git push [remote-name] [branch-name]` 可以将本地仓库中的数据推送到远程仓库

```
git push -u origin master
```

`-u` 参数的狭义理解：当加入 `-u` 参数之后，以后就可直接输入 `git push` 来推送数据。

不带任何参数的 `git push` ，默认只推送当前分支。

### 重命名远程仓库（`git remote rename`）

可以用 git re­mote re­name 命令修改某个远程仓库在本地的简称，比如想把 `learn-git` 改成 `origin`，可以这么运行：

```
git remote rename learn-git origin
```

### 解除远程仓库关联（`git remote rm`）

比如要解除和远程仓库「ori­gin」的关联，运行：

```
git remote rm origin
```

> 注意，此命令是解除了本地仓库和远程仓库的关联，并不是删除了远程仓库的数据。

### 修改远程仓库地址（`git remote set-url`）

修改远程仓库地址的方法有 3 种

1. 直接使用命令修改

```
git remote set-url origin [url]
```

1. 先解除关联再添加

```
git remote rm origin
git remote add origin [url]
```

1. 直接修改 `config` 文件

文章来源: https://blog.upx8.com/3181
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)