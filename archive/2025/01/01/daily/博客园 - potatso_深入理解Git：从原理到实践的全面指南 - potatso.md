---
title: 深入理解Git：从原理到实践的全面指南 - potatso
url: https://www.cnblogs.com/potatso/p/18644042
source: 博客园 - potatso
date: 2025-01-01
fetch_date: 2025-10-06T20:06:17.612458
---

# 深入理解Git：从原理到实践的全面指南 - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [深入理解Git：从原理到实践的全面指南](https://www.cnblogs.com/potatso/p/18644042 "发布于 2024-12-31 15:07")

# Hello World

# 深入理解Git：从原理到实践的全面指南

> 本文深入剖析Git的核心概念和底层实现原理，包括对象模型、分支管理、合并策略等关键特性。通过理解Git的数据结构和工作机制，帮助开发者更好地处理版本控制中的各种复杂场景，从基础使用者进阶为Git专家。

在日常开发中，很多开发者在使用Git时往往只是停留在基本操作层面，特别是在遇到复杂的合并冲突时，常常感到无所适从。要想真正掌握Git，成为Git专家，关键在于深入理解其底层原理。本文将帮助你：

* 深入理解Git的核心概念和工作原理
* 学会分析和解决各类合并冲突
* 掌握Git的高级特性和最佳实践

通过本文的学习，你将能够在日常工作中更加自如地使用Git，处理各种复杂场景。

# 1. 基础概念 git的三种基本对象

## 1.1 Blob

Blob对象是Git中最基础的存储单元。它的工作原理是：

1. 将文件内容进行SHA-1哈希计算，得到一个唯一的哈希值作为文件名
2. 使用zlib压缩算法压缩文件内容，生成blob对象

这种设计的巧妙之处在于利用了哈希算法的"雪崩效应"：即使文件内容只改变一个字符，产生的哈希值也会完全不同。这样，Git只需要比较文件的哈希值，就能立即知道文件是否被修改，而不需要逐字节地比较文件内容，大大提高了效率。

## 1.2 Tree

Tree对象相当于Git中的目录结构，用于组织和管理文件。它的工作原理是：

1. 记录目录下所有内容的信息：
   * 文件对应的blob对象
   * 子目录对应的tree对象
2. 为每个目录生成一个唯一的哈希值，这样任何目录结构的变化都能被追踪

这种层级结构让Git能够高效地管理从单个文件到整个项目的所有内容变化。

## 1.3 Commit

保存每次提交的信息。

![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150200612-208705082.png)

## 1.4 分支

分支其实就是一个指向commit的指针（文件内容是commit的hash值）。当你提交新的更改时，这个指针会自动指向新的commit。这就是为什么我们能轻松地在不同版本之间切换：本质上就是在移动这个指针。

![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150214209-61969469.png)

# 2. 完整的一次提交过程

在这里我们模拟解释一次git add/ commit的过程，来了解git的工作原理。

## 2.1 git add 文件

假设我们修改了readme.md文件，执行`git add`时会发生以下操作：

1. Git读取readme.md的内容
2. 将内容用zlib算法压缩，创建一个blob对象
3. 用SHA1算法计算这个blob对象的哈希值
4. 用这个哈希值作为文件名，将blob对象保存到Git仓库中

这样，每个文件版本都会有一个唯一的标识（哈希值），Git可以精确地追踪文件的每次变化。

## 2.2 git commit

执行`git commit`时，Git会按以下步骤创建新的提交：

1. 创建新的Tree对象：

   * 读取当前仓库的Tree对象（保存了所有文件的目录结构）
   * 将`git add`创建的新Blob对象更新到Tree中
   * 为这个新的目录结构创建一个新的Tree对象
2. 创建新的Commit对象：

   * 记录新Tree对象的哈希值
   * 记录父Commit的哈希值
   * 保存提交信息（commit message）
   * 保存提交者信息和时间戳
3. 更新分支指针：

   * 将当前分支指向这个新的Commit对象

这样就完成了一次完整的提交，保存了项目的一个新版本。
![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150229416-311831287.png)

相当于，我们每次提交，都会完整的把项目中每个文件通过zlib压缩，完整地保存下来。而对于没有修改的文件，git会通过类似于快捷方式，或者软链接等方式，直接指向上一次提交的版本。

Commit对象包含以下重要信息：

1. tree：指向项目根目录的Tree对象
2. parent：指向一个或多个父Commit
   * 常规提交只有一个父Commit
   * 合并提交会有多个父Commit，记录了所有被合并的分支
3. author/committer：提交者信息
4. message：提交信息

这种设计让Git能够完整记录项目的历史，并支持复杂的分支合并操作。

在git commit时，会获取git add创建的blob对象。为了优化设计，git在某处地方存放了一个列表，里面写满了

# 3. 常见概念以及命令解析

## 3.1 暂存区（Stage/Index）

暂存区是Git中的一个重要概念，它是一个临时的Tree对象，默认与仓库的HEAD指针指向的Tree对象相同，内容也相同。如果有文件提交，那么临时Tree对象只修改对应的blob，指向新的blob。现在不理解不要紧，下面在使用git底层命令模拟提交的时候会通过例子去详细解释：

1. 当执行`git add`时：

   * 创建新的Blob对象
   * 更新暂存区的Tree对象，指向这些新的Blob
2. 默认情况下：

   * 暂存区的Tree对象与最近一次提交的Tree对象结构相同
   * 只有执行`git add`后，相应的文件引用才会更新
3. 特殊操作：

   * 执行`git reset --soft`时，只移动HEAD指针，暂存区保持不变

## 3.2 使用git底层命令模拟commit

既然git add是创建新的Blob对象，那么我们理论上也可以用git提供的底层命令去完成这个操作。

```
MS-7B23:~/repo$ git hash-object -w -t blob hello.txt
ce013625030ba8dba906f756967f9e9ca394464a
```

在这里，我们可以看到git hash-object命令的输出，它生成了一个新的Blob对象，并且返回了这个对象的哈希值。我们直接使用zlib命令，在.git文件夹中找到这个blob文件并解压。

```
zlib-flate -uncompress < .git/objects/ce/013625030ba8dba906f756967f9e9c
a394464a
blob 6hello
```

接下来，我们需要将这个新创建的blob对象添加到暂存区的tree对象中。这个过程包含两步：

1. 获取当前的tree对象并创建副本
   注意

   1. 如果你此时仓库为空，例如刚初始化，git中没有任何东西。那你并不需要获取当前的tree对象。跳到第二步即可
   2. 但是如果你此时仓库中已经被初始化，那就需要获取当前的tree对象。需要使用`git read-tree HEAD # 读取当前HEAD的树到暂存区`
2. 在新的tree对象中更新hello.txt的引用，指向我们刚创建的blob对象

```
git update-index --add --cacheinfo 100644 ce013625030ba8dba906f756967f9e9ca394464a hello.txt
```

然后再把这个新的tree也保存到文件，我们需要执行`git write-tree`,这个命令会返回这个tree的哈希值。

```
git write-tree
aaa96ced2d9a1c8e72c56b253a0e2fe78393feb7
```

到这里，我们已经创建了文件的blob对象和目录结构的tree对象。最后一步是创建commit对象，它将包含：

* 这个tree对象的引用
* 提交信息
* 提交者信息
* 时间戳
  当然默认git会读取git config中的user.name和user.email，但是也可以在`git commit中`自己指定

这个临时的树，就是git中大名鼎鼎的暂存区。你可以使用git ls-tree $tree\_sha1来查看它的内容（ls-tree可以查看任意tree对象的内容），也可以使用git diff $tree\_sha1来查看它的变化。

我们现在提交这个树到仓库，并包含commit信息。

```
echo "Project structure" |  git commit-tree aaa96ced2d9a1c8e72c56b253a0e2fe78393feb7
f2d4b8622737f02c226f16594f32c423b2c39c5c
```

我们直接解压这个commit对象，可以看到它的内容。

```
zlib-flate -uncompress < .git/objects/f2/d4b8622737f02c226f16594f32c423b2c39c5c
commit 212tree aaa96ced2d9a1c8e72c56b253a0e2fe78393feb7
author lll <abc@mail.com> 1735620034 +0800
committer lll <abc@mail.com> 1735620034 +0800

Project structure
```

到这里还不算完，还需要更新HEAD指针，才算一次真正的提交

```
git update-ref refs/heads/master f2d4b8622737f02c226f16594f32c423b2c39c5c
```

这样，我们就完成了一次完整的提交，保存了项目的一个新版本。使用git log命令，可以查看本次提交的记录

```
git log
commit f2d4b8622737f02c226f16594f32c423b2c39c5c (HEAD -> master)
Author: lll <abc@mail.com>
Date:   Tue Dec 31 12:40:34 2024 +0800

    Project structure
```

完整图例

![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150314919-227489282.png)

## 3.3 git soft三种模式的区分

通过前面的学习，我们已经了解到HEAD和暂存区实际上都是指向特定Git对象的指针。默认暂存区指针与HEAD指针指向同一Tree对象。
现在，让我们通过一个具体的例子来深入理解`git reset`的三种模式（--soft、--mixed、--hard）的区别。

假设我们有一个项目，已经进行了三次提交，我们将以这个场景为例：
![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150328315-595647928.png)

### 3.3.1 git reset --soft

如果我们执行`git reset --soft HEAD^1`, 那么Git会做以下操作:
更新HEAD指针，指向上一次提交的commit对象， 暂存区指针不动，依旧指向本次commit提交的tree对象

![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150341693-105525396.png)

这种状态下，如果我们执行新的提交，会产生一个有趣的效果：

1. 暂存区保留了最新的文件状态（指向最新的Tree对象）
2. HEAD指向了上一个commit
3. 当我们提交时，会用暂存区的内容创建一个新的commit

这就是为什么它被称为"soft"（软）重置：

* 只移动HEAD指针，不改变任何文件内容
* 保留了暂存区的所有改动
* 常用场景：
  1. 修改最近一次的提交信息
  2. 将多个提交合并为一个提交
  3. 在不丢失任何改动的情况下重新组织提交

我们可以使用Git底层命令来模拟`git reset --soft`的效果。首先使用`git rev-parse HEAD`获取当前commit的引用，然后通过`git rev-parse HEAD^1`获取父commit的hash值，最后使用`git update-ref refs/heads/master HEAD^1`来更新分支指针。这样就实现了只移动HEAD指针而保持暂存区不变的效果。

### 3.3.2 git reset --mixed

如果我们执行`git reset --mixed HEAD^1`, 那么Git会做以下操作:
更新HEAD指针，指向上一次提交的commit对象， 暂存区同时也更新，指向上一次提交的tree对象。但是工作区不动。工作区就是你当前在磁盘系统上的项目文件。

![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150401390-902682970.png)

这种模式的一个典型应用场景是：当你不小心提交了一些不应该提交的文件，或者不该提交的代码，但又不想丢失工作区的修改时。通过`git reset --mixed`，你可以重置暂存区到上一个状态，重新选择要提交的文件，同时保留工作区的所有改动。这就是为什么它被称为"mixed"（混合）重置 —— 它在保留工作区的同时，让你能重新组织暂存区的内容。

通过上面的描述，我们可以使用git read-tree 命令来模拟git reset --soft的效果。核心要点在于修改HEAD和暂存区指针，但不改变工作区的内容。

### 3.3.3 git reset --hard

如果我们执行`git reset --hard HEAD^1`, 那么Git会做以下操作:
更新HEAD指针，指向上一次提交的commit对象， 暂存区同时也更新，指向上一次提交的tree对象，同时把Tree对象中的文件，解压覆盖工作区。
![](https://img2024.cnblogs.com/blog/1916047/202412/1916047-20241231150412530-794903669.png)

## 3.4 git...