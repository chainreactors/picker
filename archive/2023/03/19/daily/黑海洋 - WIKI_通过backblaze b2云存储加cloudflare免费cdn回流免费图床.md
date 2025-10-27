---
title: 通过backblaze b2云存储加cloudflare免费cdn回流免费图床
url: https://blog.upx8.com/3278-1
source: 黑海洋 - WIKI
date: 2023-03-19
fetch_date: 2025-10-04T10:02:54.568746
---

# 通过backblaze b2云存储加cloudflare免费cdn回流免费图床

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 通过backblaze b2云存储加cloudflare免费cdn回流免费图床

发布时间:
2023-03-18

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
8541

# 准备工作

---

首先准备一个完全自主的域名，一个邮箱

## 1.在[cloudflare](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuY2xvdWRmbGFyZS5jb20v)注册并将你的域名加入，这个很简单，cloudflare现在大部份都中文了

## 2.在[backblaze](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuYmFja2JsYXplLmNvbS9iMi9jbG91ZC1zdG9yYWdlLmh0bWw)注册一个账号，并新建一个bucket，这步也简单，

记得Files in Bucket are:这里选public就好，就是公开桶。

#### 对接回流：

## 1.打开backblaze 点Upload/Download 随便上传一个文件，然后点上传文件，弹出文件信息

![](https://i0.wp.com/cdn.skyimg.de/up/2025/1/5/xnurah.webp)

图中红色箭头的链接复制，一会在cloudflare要用到。

## 2.转到cloudflare控制页面，找到dns记录 设置如下图填写添加一个记录

[![](https://f004.backblazeb2.com/file/momog-cn/images/cloudflaresetdns.png)](https://f004.backblazeb2.com/file/momog-cn/images/cloudflaresetdns.png)

现在将backblaze链接里面的域名<https://f004.backblazeb2.com/file/momog-cn/images/cloudflaresetdns.png>
替换成你自己刚设置的域名，如我的是<https://assets.momog.cn/file/momog-cn/images/cloudflaresetdns.png>
能访问就成功了，基本到这也就可以了，下面再说一下我的缓存时间设置及域名简化规则

## 3. 缓存时间设置（这个也可以在backblaze设置,百度有教程） ,我这里是在cloudflare操作的

看图
[![](https://f004.backblazeb2.com/file/momog-cn/images/cloudflaresetcache.png)](https://f004.backblazeb2.com/file/momog-cn/images/cloudflaresetcache.png)

## 4. 域名简化规则，就是将backblaze默认的 /file/桶名 重写简化

由原来的<https://assets.momog.cn/file/momog-cn/images/cloudflaresetdns.png>
变成这样<https://assets.momog.cn/images/cloudflaresetdns.png>
看图
[![](https://f004.backblazeb2.com/file/momog-cn/images/cloudflaresetrule.png)](https://f004.backblazeb2.com/file/momog-cn/images/cloudflaresetrule.png)

```
`concat("/file/momog-cn",http.request.uri.path)` 这里的/file/后面改成你自己的桶名
```

#### 扩展工具

假如你是用的typecho，还可以使用我的上传插件实现自动上传，无需登录backblaze：
typecho - b2file 插件地址：[https://github.com/qq80284445/Typecho-B2File](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3FxODAyODQ0NDUvVHlwZWNoby1CMkZpbGU)
另：backblaze支持s3 ，所以你用Picgo等软件上传的话，只需要添加个s3插件就可以了

使用方法：(插件文件夹改成：B2File，不然无法激活)
第一步：下载本插件，放在 usr/plugins/ 目录中；
第二步：进入后台 插件管理 激活插件；
第三步：填写空间名称、keyID、applicationKey、域名 等配置；
第四步：B2配合cloudflare免费回流cdn白嫖10G图床。

相关链接：[https://blog.xiaoz.org/archives/17544](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnhpYW96Lm9yZy9hcmNoaXZlcy8xNzU0NA)

相关：[https://zhuanlan.zhihu.com/p/604285576](https://blog.upx8.com/go/aHR0cHM6Ly96aHVhbmxhbi56aGlodS5jb20vcC82MDQyODU1NzY)

# [Backblaze(B2)套CloudFlare可用于静态文件存储](https://blog.upx8.com/go/aHR0cHM6Ly9tcC53ZWl4aW4ucXEuY29tL3M_X19iaXo9TXpJME1ERTVPVGd5TWc9PSZtaWQ9MjY0OTY0Mjk5NyZpZHg9MSZzbj04ZWZlYTEzY2MyZjhhZGY3Mjk3Zjg1NzYzODRlNmI3NiZjaGtzbT1mMTA0ODYxNGM2NzMwZjAyN2Q0N2QzNDU4MzEyMjYyMzQ2MDIxMzI0MWZjNDlkMDZmMjJjMDBkODY4MjE3MjU2NTg4YmY2MTNiODQ5JnNjZW5lPTI3)

[取消回复](https://blog.upx8.com/3278-1#respond-post-3280)

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