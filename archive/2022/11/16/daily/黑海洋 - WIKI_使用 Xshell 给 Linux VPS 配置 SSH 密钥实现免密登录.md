---
title: 使用 Xshell 给 Linux VPS 配置 SSH 密钥实现免密登录
url: https://blog.upx8.com/3091
source: 黑海洋 - WIKI
date: 2022-11-16
fetch_date: 2025-10-03T22:53:17.124327
---

# 使用 Xshell 给 Linux VPS 配置 SSH 密钥实现免密登录

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 使用 Xshell 给 Linux VPS 配置 SSH 密钥实现免密登录

发布时间:
2022-11-15

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
23534

## 前言

SSH 提供两种认证方式，密码认证和密钥认证，一般我们买来的 VPS 都是密码认证。密码的缺点是很容易被暴力破解，而且密码需要记忆，使用起来麻烦。密钥的好处是，你只需要一对密钥文件：公钥和私钥，公钥相当于门锁，装在 VPS 上，私钥相当于钥匙，放在本地计算机上，登录的过程就像是用钥匙去开锁，有钥匙的人才能打得开，不仅安全，而且方便。此外，公钥可以复制到其它主机和账户，这就像是你装了很多同样门锁。

## 获取密钥

就像门锁，先得有，才能装。你可以使用 Xshell 生成密钥，也可以通过其他方式生成密钥，再导入到 Xshell 中进行管理。关于导入和管理的方法可参考《[使用 Xshell 管理 SSH 密钥](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2FyY2hpdmVzL21hbmFnZS1zc2gta2V5cy13aXRoLXhzaGVsbC5odG1s)》这篇文章，这里不做赘述。

在 Xshell 中点开**工具**菜单，选择**用户密钥管理者** ( Alt+T+U )。

[![](https://imgcdn.p3terx.com/post/20190827144831.png)](https://imgcdn.p3terx.com/post/20190827144831.png)

在**用户密钥**窗口中点击**生成**按钮。

[![](https://imgcdn.p3terx.com/post/20190827161003.png)](https://imgcdn.p3terx.com/post/20190827161003.png)

在**新建用户密钥生成向导**中会让你选择密钥类型，一般默认即可，点击**下一步**。

[![](https://imgcdn.p3terx.com/post/20190827151824.png)](https://imgcdn.p3terx.com/post/20190827151824.png)

然后会要求你填写密钥名称和密码，免密登录密码留空即可，然后点**完成**。

[![](https://imgcdn.p3terx.com/post/20190827155946.png)](https://imgcdn.p3terx.com/post/20190827155946.png)

之后会有下面这个提示，选择**是**即可。

[![](https://imgcdn.p3terx.com/post/20190827150235.png)](https://imgcdn.p3terx.com/post/20190827150235.png)

当完成密钥生成的操作后密钥会出现在**用户密钥**的窗口中。

## 配置密钥

给 VPS 配置密钥简单来说就是把公钥内容写入到 `~/.ssh/authorized_keys` 中的过程。

首先使用 Xshell 登录到 VPS，这里需要注意需要配置密钥的用户，不要弄错。

执行下面的命令创建 SSH 认证文件并打开文本编辑器。

```
mkdir -p ~/.ssh && nano ~/.ssh/authorized_keys
```

然后在 Xshell 中点开**工具**菜单，选择**用户密钥管理者** ( Alt+T+U )。

[![](https://imgcdn.p3terx.com/post/20190827144831.png)](https://imgcdn.p3terx.com/post/20190827144831.png)

在**用户密钥**窗口中双击密钥进入密钥属性。

[![](https://imgcdn.p3terx.com/post/20190827161005.png)](https://imgcdn.p3terx.com/post/20190827161005.png)

在属性窗口中选择**公钥**标签，复制公钥。

[![](https://imgcdn.p3terx.com/post/20190827162147.png)](https://imgcdn.p3terx.com/post/20190827162147.png)

把复制的公钥粘贴到终端的文本编辑器中，最后保存退出。

[![](https://imgcdn.p3terx.com/post/20190827162918.png)](https://imgcdn.p3terx.com/post/20190827162918.png)

为了能正常登陆，需要给文件设置相应的权限。

```
chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
```

## 使用密钥登录 VPS

这里以新建会话为例子，已有会话可以通过右键属性进入到这个窗口。

[![](https://imgcdn.p3terx.com/post/20190827150240.png)](https://imgcdn.p3terx.com/post/20190827150240.png)

进入**用户身份验证**设置选项，按照下面的图片操作即可。

[![](https://imgcdn.p3terx.com/post/20190827200530.png)](https://imgcdn.p3terx.com/post/20190827200530.png)

## 禁用密码登录

在确认使用密钥能正常登录后，为了提高 VPS 的安全性建议禁用密码登录。

执行以下命令，对 sshd 配置文件 (`/etc/ssh/sshd_config`) 进行修改。

```
sudo sed -i '/PasswordAuthentication /c\PasswordAuthentication no' /etc/ssh/sshd_config
```

最后重启 sshd 服务，使配置生效。

```
sudo service sshd restart
```

1. ![Carlosdup](https://gravatar.loli.net/avatar/avatar/12ca8d4413f173c708e6933dfdbf9647?s=32&r=&d=)

   **Carlosdup**

   2024-12-22 00:46:37

   [回复](https://blog.upx8.com/3091/comment-page-1?replyTo=30368#respond-post-3091)

   коридори дизайн

[取消回复](https://blog.upx8.com/3091#respond-post-3091)

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