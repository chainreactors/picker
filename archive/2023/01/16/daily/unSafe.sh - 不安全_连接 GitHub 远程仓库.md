---
title: 连接 GitHub 远程仓库
url: https://buaq.net/go-145615.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:49.941511
---

# 连接 GitHub 远程仓库

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

连接 GitHub 远程仓库

设置用户信息git 要求使用者必须提供自己的身份标识，为此我们需要在 git bash 中执行以下命令：git config --global user
*2023-1-15 14:35:0
Author: [blog.upx8.com(查看原文)](/jump-145615.htm)
阅读量:18
收藏*

---

## 设置用户信息

git 要求使用者必须提供自己的身份标识，为此我们需要在 git bash 中执行以下命令：

```
git config --global user.name "name" //填写你的用户名
git config --global user.email "[email protected]" //填写你的邮箱
```

## 生成密钥

```
ssh-keygen -t rsa -C "[email protected]" //填写你的邮箱
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]  // 推荐使用默认地址
Enter passphrase (empty for no passphrase):   //此处点击 Enter 键即可，也可以填写密码，填写密码后每次使用 SSH 方式推送代码时都会要求输入密码，由于这个 Key 也不是用于军事目的，所以也无需设置密码。
```

有任何提示，直接回车即可。

## 将公钥添加到Github

```
cat ~/.ssh/id_rsa.pub
```

复制文件中的内容，打开 <https://github.com/settings/ssh/new> ，并点击 `Add SSH key` ，将内容粘贴到 Key 中。

## 测试连接状态

```
ssh -T [email protected]
```

看到 `Hi XXXXXX! You've successfully authenticated, but GitHub does not provide shell access.` 说明连接成功了。

## 参考

[使用 git 连接到 Github](https://blog.csdn.net/furzoom/article/details/49734799)

[如何配置 SSH 公钥访问代码仓库](https://blog.csdn.net/mahoon411/article/details/125596729)

文章来源: https://blog.upx8.com/3182
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)