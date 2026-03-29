---
title: 深澜计费管理系统day合集
url: https://mp.weixin.qq.com/s/wPyjgDeX8QbcISwMu_5WrA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:33:03.399814
---

# 深澜计费管理系统day合集

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6QSDNcWpMD0UoTWhux13P7a5uicCOTJLdia5e4bATV9RGqVjx65aUC1iaGIFH6avIEaa2toQkmriaGza2nib80mCwtQ6vJIfFBkzEe6QbTZCWBM0/0?wx_fmt=jpeg)

# 深澜计费管理系统day合集

小叶Sec

![]()

在小说阅读器中沉浸阅读

以下文章来源于paopao小白入安全
，作者paopao

![](http://wx.qlogo.cn/mmhead/kSiaeFj92SMzNTLAHmmJiczXokjsVIjrvFO9g6VWmrN8PvrQ13qOMs0A1ycibYDCZnhZ5R4wyN1BsA/0)

**paopao小白入安全**
.

一个初学网安的菜鸡，日常分享漏洞挖掘和自己的小小心得！！！感谢关注！！！ 学安全要练习就用好靶场

# 深澜计费管理系统day合集

```
免责声明： 本文章仅供分享，合法测试
若出现违法行为与本人无关，完全个人行为！
```

## 产品简介

* 杭州瀚洋科技有限公司（深澜软件）是全球领先且企业高端用户最多的认证计费技术厂商之一，总部位于中国的杭州。
* 目前全球超过2500家企业选择深澜软件作为其用户认证管理及计费方案；其中在中国Top100高校中有60%使用我们的产品。
* 作为全球认证计费解决方案的领导品牌。

## 资产测绘

fofa: "/js/xxxxxx/xx.js"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6QSDNcWpMD1E5zQibrU795MhjveAfGtbzibdgnBg5Y5jp04DQFf8xtMlTZsvkBs9GVlxicF1oiaP2YNs5t7ibjyNLYARaj8kpx38zXWoiaRNsbR6w/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/6QSDNcWpMD3zyNw7eFia7GA1ZicuRsibpTiaqeiaUJEEkhFA4qSC1wO7s68aBQpHuduUHkR2yEw7xqI1As0icT7IpGQWs5UPyqaTqllibASpB9icjd0/640?wx_fmt=png&from=appmsg)

### 弱口令

```
srun/123456
test123/123456
admin/admin
admin/Srun@4000
```

### 深澜计费管理系统多接口存在后台任意文件读取漏洞

#### 复现步骤（这里只复现其一）

```
/xxxx/xxxx/xxx/xxx?xxxx=/etc/passwd
```

![](https://mmbiz.qpic.cn/mmbiz_png/6QSDNcWpMD1zP7YuXGiau0HcAHEGhwdrhh61oAtoibW1tsM9H7d3Ratl8NXN6lpmQl9ZfvYmvdojha4WWJrygca65iaiab2wZPqicszjGM6GapCY/640?wx_fmt=png&from=appmsg)

### 用户信息泄露

#### 复现步骤

```
/xxxx/xxxx/xxxxx?type=2&page=2&per-page=10
```

![](https://mmbiz.qpic.cn/mmbiz_png/6QSDNcWpMD0GyEicWp25wqlr1LrajtuafgB9lM2WOL8JrqHZZJLIAxHqHpte5UxdlbQgYcmHjibVbySgoPjhYpCEYibFSdwovKicaicIJujN2voo/640?wx_fmt=png&from=appmsg)

### 存储型XSS

#### 复现步骤

##### 在登陆页面用户名处填入xss语句即可插入

![](https://mmbiz.qpic.cn/mmbiz_png/6QSDNcWpMD3xK7WELEL90ianeE1sX6cCkdqwNyqclBVQlDC4d9Dd3A2q5QJtkC7crQ8S1xWp1icLpWvRwehvdYU0R9DrRXh5dJBe7gYkGRibqc/640?wx_fmt=png&from=appmsg)

##### 但是需要站长点击日志管理-操作日志才能弹出XSS语句

![](https://mmbiz.qpic.cn/mmbiz_png/6QSDNcWpMD1arIrclkJoc4ic64JCbrTqyZstC5sxjMy1BYYInSFZgxhZ7IZ0Tnw56RtoNCt1JJd8V3qBHGichRrogKicbbiaBtsdOQ6t1ME7trY/640?wx_fmt=png&from=appmsg)

`目前本人复现了仅仅这些，如果想要完整的poc可以关注后私信回复：`

```
深澜计费管理系统poc
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6QSDNcWpMD3ptogGkRgLibO8o20qq0fHIRMBzWb5nueTWDMKm5ZWgnCfyGSp5UQ8Dx4NchwF1fOlTIm5f8mz7RAV6y5HzsBRicdSACniaJ4wNw/640?wx_fmt=png&from=appmsg)

`📌`

`免责声明本文仅用于网络安全技术学习、研究与防御交流，不针对任何特定目标。所有内容仅限合法授权环境下使用，严禁未经许可对任何系统进行测试、入侵、破坏或数据窃取。`

`读者因违规使用造成的一切法律责任与损失由使用者自行承担，本公众号不承担任何责任。`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

小叶Sec

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过