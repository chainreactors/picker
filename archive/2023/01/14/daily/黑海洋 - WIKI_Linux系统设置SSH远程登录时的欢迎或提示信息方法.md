---
title: Linux系统设置SSH远程登录时的欢迎或提示信息方法
url: https://blog.upx8.com/3177
source: 黑海洋 - WIKI
date: 2023-01-14
fetch_date: 2025-10-04T03:53:17.509112
---

# Linux系统设置SSH远程登录时的欢迎或提示信息方法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux系统设置SSH远程登录时的欢迎或提示信息方法

发布时间:
2023-01-13

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
13957

[![](https://blog.tag.gg/d/file/p/2023/01-07/698239dfea37125f08410e86df46d8e2.jpg)](https://blog.tag.gg/d/file/p/2023/01-07/698239dfea37125f08410e86df46d8e2.jpg)

前言：在Linux系统SSH远程登录时我们想显示自己的提示信息或设置固定的欢迎信息,可以参考这篇文章操作实现,方法很简单。
设置方法：
1、执行如下命令打开/etc/motd文件编辑。

> vi /etc/motd

2、将提示信息或欢迎信息写入到/etc/motd文件中即可,例如本次演示写入如下信息：

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
>
>                    \_ooOoo\_
>                   o8888888o
>                   88" . "88
>                   (| -\_- |)
>                   O\  =  /O
>                \_\_\_\_/`---'\\_\_\_\_
>              .'  \\|     |//  `.
>             /  \\|||  :  |||//  \
>            /  \_||||| -:- |||||-  \
>            |   | \\\  -  /// |   |
>            | \\_|  ''\---/''  |   |
>            \  .-\\_\_  `-`  \_\_\_/-. /
>          \_\_\_`. .'  /--.--\  `. . \_\_
>       ."" '<  `.\_\_\_\\_<|>\_/\_\_\_.'  >'"".
>      | | :  `- \`.;`\ \_ /`;.`/ - ` : | |
>      \  \ `-.   \\_ \_\_\ /\_\_ \_/   .-` /  /
> ======`-.\_\_\_\_`-.\_\_\_\\_\_\_\_\_/\_\_\_.-`\_\_\_\_.-'======
>                    `=---='
> ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设置后关闭ssh重新登录则会显示

[取消回复](https://blog.upx8.com/3177#respond-post-3177)

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