---
title: web scraper：不用写代码的爬虫插件
url: https://zgao.top/web-scraper%ef%bc%9a%e4%b8%8d%e7%94%a8%e5%86%99%e4%bb%a3%e7%a0%81%e7%9a%84%e7%88%ac%e8%99%ab%e6%8f%92%e4%bb%b6/
source: Zgao's blog
date: 2023-01-13
fetch_date: 2025-10-04T03:43:04.875622
---

# web scraper：不用写代码的爬虫插件

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# web scraper：不用写代码的爬虫插件

* [首页](https://zgao.top)
* [web scraper：不用写代码的爬虫插件](https://zgao.top:443/web-scraper%EF%BC%9A%E4%B8%8D%E7%94%A8%E5%86%99%E4%BB%A3%E7%A0%81%E7%9A%84%E7%88%AC%E8%99%AB%E6%8F%92%E4%BB%B6/)

[1月 12, 2023](https://zgao.top/2023/01/)

### web scraper：不用写代码的爬虫插件

作者 [Zgao](https://zgao.top/author/zgao/)
在[[经验分享](https://zgao.top/category/%E7%BB%8F%E9%AA%8C%E5%88%86%E4%BA%AB/)](https://zgao.top/web-scraper%EF%BC%9A%E4%B8%8D%E7%94%A8%E5%86%99%E4%BB%A3%E7%A0%81%E7%9A%84%E7%88%AC%E8%99%AB%E6%8F%92%E4%BB%B6/)

最近帮小伙伴下载某学习网站的视频。需要对页面内的数据做一次性的抓取。对于是一次性的抓取需要，能不写代码就不写代码，就用web scraper这个浏览器插件进行链接抓取。

[](https://zgao.top/wp-content/uploads/2023/01/web-scraper抓取.mp4)

文章目录

[ ]

* [web scraper插件安装](#web_scraper%E6%8F%92%E4%BB%B6%E5%AE%89%E8%A3%85 "web scraper插件安装")
* [需求分析](#%E9%9C%80%E6%B1%82%E5%88%86%E6%9E%90 "需求分析")
* [web scraper 配置](#web_scraper_%E9%85%8D%E7%BD%AE "web scraper 配置")
* [开始抓取数据](#%E5%BC%80%E5%A7%8B%E6%8A%93%E5%8F%96%E6%95%B0%E6%8D%AE "开始抓取数据")
  + [遇到阻碍：referer检测](#%E9%81%87%E5%88%B0%E9%98%BB%E7%A2%8D%EF%BC%9Areferer%E6%A3%80%E6%B5%8B "遇到阻碍：referer检测")
  + [曲线救国：ModHeader 添加referer头](#%E6%9B%B2%E7%BA%BF%E6%95%91%E5%9B%BD%EF%BC%9AModHeader_%E6%B7%BB%E5%8A%A0referer%E5%A4%B4 "曲线救国：ModHeader 添加referer头")

## web scraper插件安装

![](https://zgao.top/wp-content/uploads/2023/01/image-7-1024x403.png)

下载链接：<https://chrome.google.com/webstore/detail/web-scraper-free-web-scra/jnhgnonknehpejjnehehllkliplmbmhn>

## 需求分析

需求很简单，要抓取两个页面。

![](https://zgao.top/wp-content/uploads/2023/01/image-8-1024x603.png)

先抓取课程页面中所有视频页面的链接。

![](https://zgao.top/wp-content/uploads/2023/01/image-9-1024x502.png)

然后在视频页面的中获取视频的真实链接，这里是用的阿里云的oss。

这么简单的抓取，写代码太浪费时间，手动复制又太麻烦。这种场景用插件抓取数据再合适不过了。

## web scraper 配置

F12打开控制台，新建一个sitemap。

![](https://zgao.top/wp-content/uploads/2023/01/image-10-1024x536.png)
![](https://zgao.top/wp-content/uploads/2023/01/image-11-1024x533.png)
![](https://zgao.top/wp-content/uploads/2023/01/image-12-1024x726.png)
![](https://zgao.top/wp-content/uploads/2023/01/image-13-1024x398.png)

保存后可以预览当前页面被选中的元素。

![](https://zgao.top/wp-content/uploads/2023/01/image-14-1024x550.png)

以及预览当前的抓取的链接。

获取到一级页面后，需要通过访问抓取的链接去获取视频url。

![](https://zgao.top/wp-content/uploads/2023/01/image-15-1024x492.png)
![](https://zgao.top/wp-content/uploads/2023/01/image-16-1024x553.png)

现在来到视频页面，因为input标签是不可见的，所以我们没法像刚才一样通过select去获取元素。

![](https://zgao.top/wp-content/uploads/2023/01/image-17-1024x603.png)

切换到元素tab，右键复制selector。

![](https://zgao.top/wp-content/uploads/2023/01/image-18-1024x613.png)

注意抓取的是标签属性，需要选择value。

![](https://zgao.top/wp-content/uploads/2023/01/image-19-1024x614.png)

![](https://zgao.top/wp-content/uploads/2023/01/image-20-1024x407.png)

这里可以看到我们爬虫selector的递进关系。

## 开始抓取数据

![](https://zgao.top/wp-content/uploads/2023/01/image-21-1024x475.png)

### 遇到阻碍：referer检测

![](https://zgao.top/wp-content/uploads/2023/01/image-22-1024x214.png)

打开第一个页面没有问题，抓取视频页面就会被检测。我搜了下网上的资料，没有解决的办法。

当然web scraper本身还不够强大，不支持自定义header。如果其他人遇到这种情况，估计就算了，不爬了。

但是我仔细想了想，既然web scraper的爬虫本身也是用Chrome进行抓取的，那么其他Chrome的插件也可以生效才对。所以我尝试用 [ModHeader](https://modheader.com/modheader) 插件手动给他加一个referer头上去。

### 曲线救国：ModHeader 添加referer头

![](https://zgao.top/wp-content/uploads/2023/01/image-23-1024x479.png)

果然奏效！

![](https://zgao.top/wp-content/uploads/2023/01/image-24-1024x523.png)

成功抓取到数据。

![](https://zgao.top/wp-content/uploads/2023/01/image-25-1024x485.png)

导出即可。

Post Views: 1,376

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/web-scraper%EF%BC%9A%E4%B8%8D%E7%94%A8%E5%86%99%E4%BB%A3%E7%A0%81%E7%9A%84%E7%88%AC%E8%99%AB%E6%8F%92%E4%BB%B6/#respond)

Δ

版权©2020 Author By : Zgao