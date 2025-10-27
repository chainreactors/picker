---
title: Cloudflare Worker Proxy 反向代理
url: https://blog.upx8.com/3662
source: 黑海洋 - WIKI
date: 2023-06-29
fetch_date: 2025-10-04T11:48:57.555943
---

# Cloudflare Worker Proxy 反向代理

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Cloudflare Worker Proxy 反向代理（jsdelivr加速）

发布时间:
2023-06-28

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
64286

# cloudflare-reverse-proxy

Cloudflare Worker Proxy 反向代理，可以把github、githubusercontent、jsdelivr等流量加速。

本项目是cloudflare反向代理。在cloudflare网站中新建worker，把worker.js文件中的内容复制进去即可使用。

**代码地址：**[https://github.com/hadis898/gh-proxy/blob/master/worker.js](https://blog.upx8.com/go/aHR0cHM6Ly9waWMuNzc2MS5jZi9odHRwczovL2dpdGh1Yi5jb20vaGFkaXM4OTgvZ2gtcHJveHkvYmxvYi9tYXN0ZXIvd29ya2VyLmpz)

使用方法为在任意url前面加上[https://你的域名/proxy/](https://blog.upx8.com/go/aHR0cHM6Ly94bi0tNnFxdjdpMnhkdDk1Yi9wcm94eS8) 即可使用cloudflare加速。

**使用方法示例：**https://pic.7761.cf/https://raw.githubusercontent.com/hadis898/Linux-tools/main/vps.sh

本人另外一个项目是基于[vercel](https://blog.upx8.com/go/aHR0cHM6Ly92ZXJjZWwuY29tLw)的反向代理，仓库地址[https://github.com/gaboolic/vercel-reverse-proxy](https://blog.upx8.com/go/aHR0cHM6Ly9waWMuNzc2MS5jZi9odHRwczovL2dpdGh1Yi5jb20vZ2Fib29saWMvdmVyY2VsLXJldmVyc2UtcHJveHk) 供大家参考

# 详细步骤

0 登录[https://www.cloudflare.com/](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuY2xvdWRmbGFyZS5jb20v)

1 创建应用程序 [![创建应用程序](https://pic.7761.cf/https://github.com/gaboolic/cloudflare-reverse-proxy/raw/main/img/1createapp.png)](https://pic.7761.cf/https%3A//github.com/gaboolic/cloudflare-reverse-proxy/blob/main/img/1createapp.png) 2 创建worker（pages也一样） [![创建worker](https://pic.7761.cf/https://github.com/gaboolic/cloudflare-reverse-proxy/raw/main/img/2createworker.png)](https://pic.7761.cf/https%3A//github.com/gaboolic/cloudflare-reverse-proxy/blob/main/img/2createworker.png) 3 点"部署"按钮 [![创建worker](https://pic.7761.cf/https://github.com/gaboolic/cloudflare-reverse-proxy/raw/main/img/3deploy.png)](https://pic.7761.cf/https%3A//github.com/gaboolic/cloudflare-reverse-proxy/blob/main/img/3deploy.png) 4 编辑代码 [![编辑代码](https://pic.7761.cf/https://github.com/gaboolic/cloudflare-reverse-proxy/raw/main/img/4update.png)](https://pic.7761.cf/https%3A//github.com/gaboolic/cloudflare-reverse-proxy/blob/main/img/4update.png) 4 编辑代码 [![编辑代码](https://pic.7761.cf/https://github.com/gaboolic/cloudflare-reverse-proxy/raw/main/img/4update.png)](https://pic.7761.cf/https%3A//github.com/gaboolic/cloudflare-reverse-proxy/blob/main/img/4update.png) 5 把worker.js文件中的内容复制进去，点"保存并部署" [![保存并部署](https://pic.7761.cf/https://github.com/gaboolic/cloudflare-reverse-proxy/raw/main/img/5save.png)](https://pic.7761.cf/https%3A//github.com/gaboolic/cloudflare-reverse-proxy/blob/main/img/5save.png) 6 (可选) 添加自定义域

绑定自己的域名。[CloudFlare Workers 设置使用自定义域名教程](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzU4NjA2ODM0L2FydGljbGUvZGV0YWlscy8xMjQ2NzAyMTg)

# 使用方法

在任意url前面加上[https://你的域名/proxy/](https://blog.upx8.com/go/aHR0cHM6Ly94bi0tNnFxdjdpMnhkdDk1Yi9wcm94eS8) 即可使用cloudflare加速。

1. **[解决cdn.jsdelivr.net无法访问（国内加速）](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudXB4OC5jb20vMzU0Nw)**

   2024-10-18 00:45:15

   [回复](https://blog.upx8.com/3662/comment-page-1?replyTo=30206#respond-post-3662)

   [...]使用案例：https://raw.githubusercontent.com/FongMi/CatVodSpider/main/json/config.json拼接成下面的样子https://cdn.jsdelivr.us/gh/FongMi/CatVodSpider@main/json/config.json那么这就简单了，只需要把网站文件中的所有“cdn.jsdelivr.net&[...]
2. **[jsdelivr cdn报错无法访问 - 偶遇你](https://blog.upx8.com/go/aHR0cHM6Ly9vdXl1Lm1lLzEy)**

   2024-08-07 21:12:49

   [回复](https://blog.upx8.com/3662/comment-page-1?replyTo=30031#respond-post-3662)

   [...]jsdelivr.b-cdn.net （台湾 CDN）使用案例：//cdn.jsdelivr.us/gh/LWingYan/仓库名@latest/xx.png拼接成下面的样子//jsdelivr.b-cdn.net/gh/LWingYan/仓库名@latest/xx.png那么这就简单了，只需要把网站文件中的所有cdn.jsdelivr.net都替换成上方的任意一个域名就可以了有财力又有能力的 最[...]
3. **[解决cdn.jsdelivr.net无法访问（国内加速）](https://blog.upx8.com/3547)**

   2023-12-25 18:33:01

   [回复](https://blog.upx8.com/3662/comment-page-1?replyTo=28196#respond-post-3662)

   [...]使用案例：https://raw.githubusercontent.com/FongMi/CatVodSpider/main/json/config.json拼接成下面的样子https://cdn.jsdelivr.us/gh/FongMi/CatVodSpider@main/json/config.json那么这就简单了，只需要把网站文件中的所有“cdn.jsdelivr.net&[...]
4. **[反代Github和jsdelivr进行加速](https://blog.upx8.com/3689)**

   2023-12-23 14:25:48

   [回复](https://blog.upx8.com/3662/comment-page-1?replyTo=28178#respond-post-3662)

   [...]使用方法在PHP安装“fileinfo”扩展，然后在网站目录新建一个名为gh.php的文件，将下面的代码复制粘贴进去。然后访问：你的域名/gh.php?url=你要代理的URL地址使用方法示例：https://wiki.upx8.com/pic.php?url=https://cdn.jsdelivr.net/gh/notetoday/img/usr/uploads/202[...]

[取消回复](https://blog.upx8.com/3662#respond-post-3662)

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