---
title: 连接 GitHub 远程仓库
url: https://blog.upx8.com/3182
source: 黑海洋 - WIKI
date: 2023-01-16
fetch_date: 2025-10-04T03:59:50.872514
---

# 连接 GitHub 远程仓库

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 连接 GitHub 远程仓库

发布时间:
2023-01-15

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
10661

## 设置用户信息

git 要求使用者必须提供自己的身份标识，为此我们需要在 git bash 中执行以下命令：

```
git config --global user.name "name" //填写你的用户名
git config --global user.email "name@email.com" //填写你的邮箱
```

## 生成密钥

```
ssh-keygen -t rsa -C "name@email.com" //填写你的邮箱
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]  // 推荐使用默认地址
Enter passphrase (empty for no passphrase):   //此处点击 Enter 键即可，也可以填写密码，填写密码后每次使用 SSH 方式推送代码时都会要求输入密码，由于这个 Key 也不是用于军事目的，所以也无需设置密码。
```

有任何提示，直接回车即可。

## 将公钥添加到Github

```
cat ~/.ssh/id_rsa.pub
```

复制文件中的内容，打开 [https://github.com/settings/ssh/new](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NldHRpbmdzL3NzaC9uZXc) ，并点击 `Add SSH key` ，将内容粘贴到 Key 中。

## 测试连接状态

```
ssh -T git@github.com
```

看到 `Hi XXXXXX! You've successfully authenticated, but GitHub does not provide shell access.` 说明连接成功了。

## 参考

[使用 git 连接到 Github](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1cnpvb20vYXJ0aWNsZS9kZXRhaWxzLzQ5NzM0Nzk5)

[如何配置 SSH 公钥访问代码仓库](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21haG9vbjQxMS9hcnRpY2xlL2RldGFpbHMvMTI1NTk2NzI5)

[取消回复](https://blog.upx8.com/3182#respond-post-3182)

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