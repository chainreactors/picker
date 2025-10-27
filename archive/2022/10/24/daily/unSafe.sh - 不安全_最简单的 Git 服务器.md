---
title: 最简单的 Git 服务器
url: https://buaq.net/go-132222.html
source: unSafe.sh - 不安全
date: 2022-10-24
fetch_date: 2025-10-03T20:43:00.295313
---

# 最简单的 Git 服务器

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

![](https://8aqnet.cdn.bcebos.com/888efba3687155f526bb8fd848a23067.jpg)

最简单的 Git 服务器

*2022-10-23 20:19:57
Author: [www.ruanyifeng.com(查看原文)](/jump-132222.htm)
阅读量:44
收藏*

---

程序员的代码仓库，总是需要托管一份在服务器，这样才保险，也方便使用。

今天就来谈谈 Git 服务器。

![](https://cdn.beekka.com/blogimg/asset/202210/bg2022102304.webp)

## 一、代码托管服务

一般情况下，都不建议自己搭建 Git 服务器，而要使用现成的服务，也就是代码托管服务。它们都是免费的。

> * [GitHub](https://github.com/)
> * [Gitlab](https://about.gitlab.com/)
> * [Bitbucket](https://bitbucket.org/)
> * [Codeberg](https://codeberg.org/)
> * [sourcehut](https://sr.ht/)
> * [Gitee](https://gitee.com/)

其中，除了最后一家 Gitee 是国内的服务，其他都是国外的服务。

这些外部服务，就不多做介绍了。本文的重点不是它们，而是想谈如果不得不自己搭建 Git 服务器，那该怎么做。

## 二、Git 服务器软件

自己搭建 Git 服务器的原因，无非就是不方便访问外网，不愿意代码放在别人的服务器，或者有一些定制化的需求。

这时，你可以选择开源的 Git 服务器软件。

> * [Gitlab CE](https://about.gitlab.com/install/ce-or-ee/)
> * [Gitea](https://gitea.io/zh-cn/)
> * [Gogs](https://gogs.io/)
> * [Onedev](https://github.com/theonedev/onedev)

这些软件里面，Gogs 的安装是最简单的，但是功能相对比较弱。功能越强的软件，安装越复杂。

如果你只是想远程保存一份代码，并不在意有没有 Web 界面，或者其他功能，那么根本不用安装上面这些软件，一行命令就够了。

## 三、Git 仓库的 SSH 传输

熟悉 Git 的同学可能知道，Git 默认支持两种传输协议：SSH 和 HTTP/HTTPS。

服务器一般都自带 SSH，这意味着，**我们可以什么都不安装，只通过 SSH 就把仓库推到远程服务器。**

所以，一条命令就够了。我们只要在远程服务器上，建立同名的 Git 仓库，服务器就搭建好了。

> ```
> $ git init --bare [仓库名].git
> ```

上面命令中，各个部分的含义如下。

（1）`git init`：初始化一个 Git 仓库。

（2）`--bare`：表示新仓库不需要工作目录，只建立 Git 数据目录。

（3）`[仓库名].git`：指定仓库名，比如仓库名是`example`，那么就要建立一个叫做`example.git`的 Git 数据目录。

执行这条命令以后，一个最简易的 Git 服务器就诞生了。后面，我们就可以通过 SSH 连接，把本地代码推送到这个远程 Git 仓库了。

## 四、操作演示

下面，我演示一下整个操作过程。

操作分成两部分，先在远程服务器操作，然后在本地计算机操作。

### 4.1 远程服务器操作

下面的操作都在远程服务器完成，假设你已经通过 SSH 登录上去了。不熟悉 SSH 的同学可以看参考这篇[《SSH 入门》](https://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)。

登录远程服务器的目的，主要是新建一个专门的用户，所有的 Git 操作都通过该用户完成。这一步其实不是必需的，但是这样后期操作比较灵活（比如仓库可以让多人共享）。

> ```
> $ sudo mkdir /home/git
> $ sudo useradd git
> $ sudo mkdir -m 700 /home/git/.ssh
> $ sudo cp ~/.ssh/authorized_keys /home/git/.ssh/
> ```

上面命令的含义如下。

（1）新建新用户的主目录`/home/git`。

（2）新建一个用户，用户名为`git`。

（3）新建新用户的 SSH 目录`/home/git/.ssh`。

（4）把当前用户的公钥拷贝给`git`用户，以便密钥登陆，详细解释可以参考[《SSH 密钥登录》](https://wangdoc.com/ssh/key.html)。

如果你只用密码登录，不使用密钥登录，那么上面第三步和第四步是不需要的，但是需要为`git`用户设定密码，命令如下。

> ```
> $ sudo passwd git
> ```

### 4.2 本机计算机操作

后面的操作都在本地计算机完成。

假定上一小节的远程服务器的 IP 地址是`192.168.1.25`，本地的 Git 仓库名为`example`。

> ```
> $ ssh [email protected] git init --bare example.git
> ```

上面命令中，`ssh [[email protected]](http://www.ruanyifeng.com/cdn-cgi/l/email-protection)`表示以`git`用户的身份，登录到远程服务器。后面的部分是 SSH 的一种语法，表示登录后在远程服务器执行的命令，即新建一个远程 Git 数据目录`example.git`。

这条命令运行完，就有了一个 Git 服务器了，然后就可以推送代码了。

> ```
> $ cd example
> $ git remote add myServer [email protected]:example.git
> $ git push myServer master
> ```

上面的命令先进入本地仓库，为远程服务器加一个别名，然后把代码推送过去。

## 五、另一种操作方法

上面的例子使用`git init --bare`命令，在远程服务器新建 Git 数据目录。其实，Git 数据目录就是一个普通目录，直接从本地计算机拷贝过去也可以。

> ```
> $ scp -r example/.git [email protected]:/home/git
> ```

上面的命令使用[`scp`工具](https://wangdoc.com/ssh/scp.html)将本地的 `example`仓库里面的`.git`子目录，拷贝到远程服务器的目录`example.git`。这样也能建立 Git 服务器。

## 六、参考链接

* [Host Git repositories on OpenBSD](https://rgz.ee/git.html)
* [Git on the Server](https://git-scm.com/book/en/v2/Git-on-the-Server-Getting-Git-on-a-Server)

（完）

文章来源: http://www.ruanyifeng.com/blog/2022/10/git-server.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)