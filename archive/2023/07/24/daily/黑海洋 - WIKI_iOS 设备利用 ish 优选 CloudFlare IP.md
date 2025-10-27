---
title: iOS 设备利用 ish 优选 CloudFlare IP
url: https://blog.upx8.com/3705
source: 黑海洋 - WIKI
date: 2023-07-24
fetch_date: 2025-10-04T11:52:51.076030
---

# iOS 设备利用 ish 优选 CloudFlare IP

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# iOS 设备利用 ish 优选 CloudFlare IP

发布时间:
2023-07-23

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
25592

在之前的教程中，我介绍了两位开源大佬的优选工具。但是对于一些没有电脑的部分读者来说，优 cf 的 ip 的操作会变得有一些困难。这篇文章中，我来和大家介绍利用 ish 终端，使用犯罪高手这位开源大佬的优选工具来优选 cf 的 ip

## 准备材料

* iOS 设备

## 优选步骤

> 注意：请在开始优选前，断开所有的代理工具，否则会导致结果不准

1. 打开 ish，输入以下命令安装依赖

```
apk update && apk add -f wget curl bash
```

2. 输入以下命令，下载优选代码并运行

```
wget -N https://raw.githubusercontent.com/badafans/better-cloudflare-ip/master/shell/cf.sh
```

3. 如为移动用户，由于项目依赖地址可能被移动SNI阻断，请手动创建四个文件，分别为`colo.txt`、`ips-v4.txt`、`ips-v6.txt`和`url.txt`，内容在以下的链接内，其他运营商用户如无法下载可以使用本步骤

`colo.txt`：`wget https://www.baipiao.eu.org/cloudflare/colo -O colo.txt`

`ips-v4.txt`：`wget https://www.baipiao.eu.org/cloudflare/ips-v4 -O ips-v4.txt`

`ips-v6.txt`：`wget https://www.baipiao.eu.org/cloudflare/ips-v6 -O ips-v6.txt`

`url.txt`：`wget https://www.baipiao.eu.org/cloudflare/url -O url.txt`

4. 第一次执行的时候会下载依赖文件，如无特殊意外的话会来到主界面。根据自己的需要，选择对应的选项进行优选。输入设置的带宽值（不需要最低也不需要太高，适中即可）及测试线程数

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230718175945.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230718175945.png)

5. 等待一会之后，程序将会显示最优的 cf ip。

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230718180319.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230718180319.png)

1. ![哈哈哈哈](https://gravatar.loli.net/avatar/avatar/0c444f5f34d396c5721c406034bdcc37?s=32&r=&d=)

   **哈哈哈哈**

   2023-07-24 06:06:51

   [回复](https://blog.upx8.com/3705/comment-page-1?replyTo=27429#respond-post-3705)

   请问干嘛用的

[取消回复](https://blog.upx8.com/3705#respond-post-3705)

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