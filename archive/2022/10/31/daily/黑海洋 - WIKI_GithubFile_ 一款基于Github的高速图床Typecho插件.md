---
title: GithubFile: 一款基于Github的高速图床Typecho插件
url: https://blog.upx8.com/3060
source: 黑海洋 - WIKI
date: 2022-10-31
fetch_date: 2025-10-03T21:21:14.873871
---

# GithubFile: 一款基于Github的高速图床Typecho插件

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# GithubFile: 一款基于Github的高速图床Typecho插件

发布时间:
2022-10-30

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
12721

## 推荐运行环境

PHP Version：7.2 及其以上

PHP Need Support：Curl or Socket

## 安装插件

1. 下载插件：[点击下载](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01saUtpb3dhL0dpdGh1YkZpbGUvYXJjaGl2ZS9yZWZzL2hlYWRzL21haW4uemlw)
2. 上传到压缩包到博客插件目录：`/usr/plugins/`
3. 右键解压上传的插件压缩包，将解压出来的文件夹名称改为**`GithubFile`**，不然不能正常启用插件。

## 获取token

进入github网站，登录自己的账号，点击[新建token](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NldHRpbmdzL3Rva2Vucy9uZXc)，如图所示填入自己想填的名称和进行选择权限后拉到最下面点击**`Generate token`**后会出现ghp\_开头的一串字符，这就是你的token，复制下来后面要用。（注意：这个token只会显示一次！）
[![2022-10-18T11:34:50.png](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092891.png "2022-10-18T11:34:50.png")](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092891.png "2022-10-18T11:34:50.png")
[![2022-10-18T11:36:17.png](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092978.png "2022-10-18T11:36:17.png")](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092978.png "2022-10-18T11:36:17.png")
[![2022-10-18T11:38:33.png](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666093114.png "2022-10-18T11:38:33.png")](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666093114.png "2022-10-18T11:38:33.png")

## 启用插件

1. 进入博客的管理后台，找到插件选项点击进入插件管理，点击设置填入你自己的相关参数后点击保存即可。

[![2022-10-18T11:24:24.png](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092266.png "2022-10-18T11:24:24.png")](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092266.png "2022-10-18T11:24:24.png")
[![2022-10-18T11:28:48.png](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092529.png "2022-10-18T11:28:48.png")](https://fastly.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/18/1666092529.png "2022-10-18T11:28:48.png")

## 项目地址

如果喜欢这个插件的话给作者点个star，给他一些动力。

[GithubFile](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01saUtpb3dhL0dpdGh1YkZpbGU)

[76](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01saUtpb3dhL0dpdGh1YkZpbGUvc3RhcmdhemVycw)[24](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01saUtpb3dhL0dpdGh1YkZpbGUvbmV0d29yay9tZW1iZXJz)

基于Github的Typecho图床插件—[Read More](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01saUtpb3dhL0dpdGh1YkZpbGUjcmVhZG1l)
[https://nanaeo.cn](https://blog.upx8.com/go/aHR0cHM6Ly9uYW5hZW8uY24v)

[Download as zip](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL01saUtpb3dhL0dpdGh1YkZpbGUvemlwYmFsbC9tYXN0ZXI "Get an archive of this repository")

## 常见问题

如果不能正常上传的话参考这篇文章进行修改设置

# 记Typecho博客上传附件不成功，提示Operation timed out after 3000 milliseconds with 0 bytes received的解决记录

由于博客经常要用到图片，但是上传到服务器又太占地方了，于是想到安装GithubFile插件把图片和附件上传到Github作为图床使用，但是在上传到时候就出现由于文件太大上传失败

## 修改nginx配置

`client_max_body_size 100m;`

## 修改PHP配置

`post_max_size = 100M`，`upload_max_filesize = 100M`把文件上限改为100M，`max_execution_time = 0`把超时时间改为0为不限制时间

## 修改Typecho文件

进入`/var/Typecho/Http/`目录，打开`Client.php`修改`private $timeout = 3;`这是程序本身代码写的限制超过3秒就会超时，所以把代码改为`private $timeout = 1800;`也就是超时时间改为30分钟，再次进行上传就没有出现任何问题了。

[取消回复](https://blog.upx8.com/3060#respond-post-3060)

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