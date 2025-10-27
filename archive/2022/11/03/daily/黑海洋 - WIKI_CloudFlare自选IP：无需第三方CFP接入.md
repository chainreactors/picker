---
title: CloudFlare自选IP：无需第三方CFP接入
url: https://blog.upx8.com/3068
source: 黑海洋 - WIKI
date: 2022-11-03
fetch_date: 2025-10-03T21:40:02.995749
---

# CloudFlare自选IP：无需第三方CFP接入

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CloudFlare自选IP：无需第三方CFP接入

发布时间:
2022-11-02

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
16540

# 第一步：注册CF并导入域名

官方版本即可，具体操作自行查阅相关域名

# 第二步：用脚本获取优秀的自选IP

脚本地址：https://github.com/BlueSkyXN/CloudFlareNB

原作者不详，有知道的可以告诉我一声

有两种方法，

一种是一键脚本（bat）

个人感觉不准，不推荐

另一种是半自动

先运行：1-自动查找100个丢包最少的IP

后会得到一个IP表

然后运行：2-对100个丢包最少的IP测速

会生成一个temp文件夹，里面是空白文件

但是文件名是ip，大小也不同，是第二步在相等条件下生成的下载测试

理论上文件越大，速度越快

然后：3-单IP测速

输入IP来测试，一般试2-3个快的即可

# 第三步：修改本地Host

直接txt修改太麻烦了，用工具吧

https://oldj.github.io/SwitchHosts/#cn

这里有个很方便的切host工具，有中文，界面简洁无广告

而且有便携版（免安装）和安装版，支持多种系统

Host 怎么写，就是ip+域名，域名就是你网站的域名

如果不想修改host，修改某客户端的配置文件中的address为新ip即可（配置中host为指向的域名来识别）

最后别忘记把小云朵点亮

注意，cf不是万能的，毕竟还是163，你想起飞，不是那么容易，但是至少，能让垃圾们活过来

[取消回复](https://blog.upx8.com/3068#respond-post-3068)

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