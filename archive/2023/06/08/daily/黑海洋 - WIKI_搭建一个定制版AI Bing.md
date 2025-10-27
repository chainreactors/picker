---
title: 搭建一个定制版AI Bing
url: https://blog.upx8.com/3625
source: 黑海洋 - WIKI
date: 2023-06-08
fetch_date: 2025-10-04T11:48:31.809780
---

# 搭建一个定制版AI Bing

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 搭建一个定制版AI Bing

发布时间:
2023-06-07

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
19115

# 项目介绍

demo：[https://bing.vcanbb.top/web/index.html#/](https://blog.upx8.com/go/aHR0cHM6Ly9iaW5nLnZjYW5iYi50b3Avd2ViL2luZGV4Lmh0bWwjLw)

项目地址：[https://github.com/adams549659584/go-proxy-bingai](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FkYW1zNTQ5NjU5NTg0L2dvLXByb3h5LWJpbmdhaQ)

![bing.png](https://iweec.com/usr/uploads/2023/06/130471354.png "bing.png")

引用项目简介：用 Vue3 和 Go 搭建的微软 New Bing 演示站点，拥有一致的 UI 体验，支持 ChatGPT 提示词，国内可用，国内可用，国内可用。

自己搭建不会出现使用中跳转到cn的情况，经过测试，无论是容器搭建还是vps上都比较稳定。

说起来，写此文本意是解答粉丝问题，希望大家在观看视频的时候，给个免费的赞。

# 优点

自建New Bing无需登陆就可以使用，也并不是必须要使用edge浏览器，登陆后可以使用绘图功能，登陆的方法就是获取到bing的cookie就行了。

![截屏2023-06-05 20.16.19.png](https://iweec.com/usr/uploads/2023/06/1732005653.png "截屏2023-06-05 20.16.19.png")

# 部署方法

项目作者想的很周到，给到了一些免费的容器部署方法和docker和compose，我这里就直接用几个方法来给大家演示一下：

**一、vps部署**

我不太建议用国内机器，原因是需要s5，新手朋友需要vps的看看：[https://bbs.csdn.net/topics/610404063](https://blog.upx8.com/go/aHR0cHM6Ly9iYnMuY3Nkbi5uZXQvdG9waWNzLzYxMDQwNDA2Mw)

首先是安装docker，然后直接使用命令：

```
docker run -d -p 8080:8080 --name go-proxy-bingai --restart=unless-stopped adams549659584/go-proxy-bingai
```

如果现在你访问ip:8080，网页显示并不是正常的。因为项目必须添加证书才能正常访问，所以我们需要一个域名，可用nginx或者caddy反向代理。

这里，我使用的是caddy，这里给出这几个步骤如下：

```
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

然后，编辑配置文件 /etc/caddy/Caddyfile

```
xx.com
encode gzip
reverse_proxy 127.0.0.1:8080
```

保存后重启一下caddy

```
systemctl restart caddy
```

现在用域名访问吧：

![截屏2023-06-05 20.12.12.png](https://iweec.com/usr/uploads/2023/06/3207226381.png "截屏2023-06-05 20.12.12.png")

**二、本地部署**

意思就是把这个new bing部署在自己的电脑上，目前仅支持windows和Linux。下载地址：[https://github.com/adams549659584/go-proxy-bingai/releases](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FkYW1zNTQ5NjU5NTg0L2dvLXByb3h5LWJpbmdhaS9yZWxlYXNlcw)

选择自己的系统，下载压缩包，执行go-proxy-bingai即可，它居然有windows arm64版本，使用MacOS PD虚拟机的也可以用了。

**三、容器部署**

支持Release，Railway，Vercel，Render等容器的部署，作者也贴心的给到了一键部署，我就不复制了，大家可以到项目主页看看吧。值得一提的就是如果容器域名被墙则不能访问，所以还是自己弄个域名好一些。

[取消回复](https://blog.upx8.com/3625#respond-post-3625)

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