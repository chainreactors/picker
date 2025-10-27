---
title: 如何更改Azure的静态IP为动态IP地址
url: https://blog.upx8.com/3055
source: 黑海洋 - WIKI
date: 2022-10-23
fetch_date: 2025-10-03T20:41:28.615675
---

# 如何更改Azure的静态IP为动态IP地址

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 如何更改Azure的静态IP为动态IP地址

发布时间:
2022-10-22

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
42329

最近开了一个AZ学生的订阅，B1S 免费机 Stop 实例的时候不再提醒是否需要保留此 IP ，停止后再开机还是原先 IP 。查询Azure的更新文档发现：

***2022.8.30更新：创建新的虚拟机默认静态IP且不可变更为动态IP。***

因此需要在创建时就配置好动态IP：将基础配置→实例详细里的可用性选项选为无需基础结构冗余，在网络配置→公用IP 新建一个公共IP地址，SKU为基本，分配为动态，确定后创建虚拟机即可。

![](https://cnboy.org/wp-content/uploads/c4ca4238a0b9238-6.jpg "如何更改Azure的静态IP为动态IP地址第1张-CNBoy 四海部落")

但是很多人踩坑，创建时并未选择动态IP，后期想更换IP了，怎么办呢？

下面就来讲讲如何只有静态一个默认选项的情况下，怎么修改为动态IP地址。

### 操作步骤流程

1、打开与虚拟机绑定的位于同一资源组的IP地址资源，点击取消关联。

![](https://cnboy.org/wp-content/uploads/c81e728d9d4c2f6-5.jpg "如何更改Azure的静态IP为动态IP地址第2张-CNBoy 四海部落")

2、点击资源—配置，在分配那里选择动态，点击保存。

![](https://cnboy.org/wp-content/uploads/eccbc87e4b5ce2f-5.jpg "如何更改Azure的静态IP为动态IP地址第3张-CNBoy 四海部落")

3、再点击概述，点击关联，资源类型选择网络接口，网络接口则选择对应的即可，重新关联到原来的虚拟机上。

![](https://cnboy.org/wp-content/uploads/a87ff679a2f3e71-4.jpg "如何更改Azure的静态IP为动态IP地址第4张-CNBoy 四海部落")

至此，修改成功。

我们可以回到对应的虚拟机页面，点击 Stop 按钮，就会发现是否需要保留此 IP 的提示出现了。

![](https://cnboy.org/wp-content/uploads/e4da3b7fbbce234-3.jpg "如何更改Azure的静态IP为动态IP地址第5张-CNBoy 四海部落")

使用动态IP的机器，只要不人为重启机器，一般他的IP地址是不会改变的。

### 补充说明：为什么要将静态IP更换为动态IP？

静态IP需要收费。1,500 小时的动态公共 IP 地址，才是Azure12个月的免费产品。

![](https://cnboy.org/wp-content/uploads/1679091c5a880fa-9.png "如何更改Azure的静态IP为动态IP地址第6张-CNBoy 四海部落")

1. ![machow](//q2.qlogo.cn/headimg_dl?dst_uin=137639650&spec=100)

   **machow**

   2023-01-29 21:57:28

   [回复](https://blog.upx8.com/3055/comment-page-1?replyTo=26871#respond-post-3055)

   站长麻烦帮忙更新下图片好嘛，光看文字没有找到地方

   1. ![chen](//q2.qlogo.cn/headimg_dl?dst_uin=21432432&spec=100)

      **chen**

      2023-05-03 23:48:13

      [回复](https://blog.upx8.com/3055/comment-page-1?replyTo=27126#respond-post-3055)

      SKU改为基本就行了。
2. ![bacon](//q2.qlogo.cn/headimg_dl?dst_uin=648558021&spec=100)

   **bacon**

   2023-01-17 17:55:17

   [回复](https://blog.upx8.com/3055/comment-page-1?replyTo=26851#respond-post-3055)

   老哥，ip配置那里改不了

   1. ![chen](//q2.qlogo.cn/headimg_dl?dst_uin=21432432&spec=100)

      **chen**

      2023-05-03 23:46:15

      [回复](https://blog.upx8.com/3055/comment-page-1?replyTo=27125#respond-post-3055)

      SKU改为基本就行了。

[取消回复](https://blog.upx8.com/3055#respond-post-3055)

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