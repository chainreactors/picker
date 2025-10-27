---
title: JS(JavaScript)简单的判断城市跳转劫持代码
url: https://blog.upx8.com/3247
source: 黑海洋 - WIKI
date: 2023-03-01
fetch_date: 2025-10-04T08:20:22.111990
---

# JS(JavaScript)简单的判断城市跳转劫持代码

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# JS(JavaScript)简单的判断城市跳转劫持代码

发布时间:
2023-02-28

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
12517

最近在工作中有一个需求根据不同的地区，跳转不同页面，考虑到PHP的效率问题最后使用js来实现，接下来编程为大家介绍一下js判断用户当前地区，有需要的小伙伴可以参考一下：

### 1、IP获取代码：

```
    <script src="https://pv.sohu.com/cityjson?ie=utf8"></script>
```

### 2、souhu接口各项参数：

```
{
    "cip": "192.168.115.178",  //用户IP
    "cid": "CN",  // 英文缩写
    "cname": "CHINA"
}
```

### 3、根据地区显示跳转不同页面：

```
  var city = returnCitySN.cname; //获取城市信息
  //判断是否是上海，然后做不同的判断
  if (city.indexOf('上海') != -1) {
    window.location.href = '/1.html';
  }else{
    window.location.href = '/2.html';
  }
```

[取消回复](https://blog.upx8.com/3247#respond-post-3247)

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