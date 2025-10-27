---
title: Ubuntu 22.04.1 LTS 启动docker镜像失败.解决方法
url: https://blog.upx8.com/3429
source: 黑海洋 - WIKI
date: 2023-04-20
fetch_date: 2025-10-04T11:34:37.199665
---

# Ubuntu 22.04.1 LTS 启动docker镜像失败.解决方法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Ubuntu 22.04.1 LTS 启动docker镜像失败.解决方法

发布时间:
2023-04-19

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
19229

在 Ubuntu 22.04 LTS 上安装 Docker 的步骤如下：

1. 更新操作系统：

```
sudo apt update
sudo apt upgrade
```

2. 安装所需的依赖包：

```
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

3. 添加 Docker 官方 GPG 密钥：

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

4. 添加 Docker 官方存储库：

```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

5. 安装 Docker：

```
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```

6. 启动 Docker 服务：

```
sudo systemctl start docker
```

这就是在 Ubuntu 22.04 LTS 上安装 Docker 的详细步骤。

[取消回复](https://blog.upx8.com/3429#respond-post-3429)

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