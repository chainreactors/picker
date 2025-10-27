---
title: 网站访客统计PHP源码
url: https://blog.upx8.com/3220
source: 黑海洋 - WIKI
date: 2023-02-12
fetch_date: 2025-10-04T06:26:10.802890
---

# 网站访客统计PHP源码

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 网站访客统计PHP源码

发布时间:
2023-02-11

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
12912

## 前言

* 一个简单统计网站访客的`PHP`源码，实现前端网页显示访问量
* 采用`PV`统计方式，单个用户连续点击`N`篇文章，记录`N`次访问量
* 源码会自动生成`TXT`记录文档，记录的访问量可以自行修改

## 源码

在网站根目录新建一个名为`FKTJ.php`的文件，然后写入以下代码

```
<?php
$n=file_get_contents('FKTJ.txt');
$n++;
file_put_contents('FKTJ.txt',$n);
echo "document.write($n);";
?>
```

在需要显示的地方添加以下调用代码

```
你是第<script type=text/javascript src=FKTJ.php></script>位访问者
```

## 说明

加入调用代码后打开网页，会在后台生成一个名为`FKTJ.txt`的记录文件，编辑此文件可以实现修改访问量
如需统计次目录下的单页访问量，可以在次目录下新建`FKTJ.php`文件，然后添加调用代码即可

[取消回复](https://blog.upx8.com/3220#respond-post-3220)

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