---
title: Linux全天不间断直播工具（带面板）
url: https://blog.upx8.com/3289
source: 黑海洋 - WIKI
date: 2023-03-19
fetch_date: 2025-10-04T10:02:54.042487
---

# Linux全天不间断直播工具（带面板）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux全天不间断直播工具（带面板）

发布时间:
2023-03-18

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
10280

这个项目是：**Ant-Media-Server**

GitHub 地址：[https://github.com/ant-media/Ant-Media-Server](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FudC1tZWRpYS9BbnQtTWVkaWEtU2VydmVy)

提供了 web 界面的直播工具，可以直接上传多个视频，然后开启直播频道轮播，填上对应的 rtmp 推流地址，推流到 b 站直播、斗鱼、youtube 、twitch 等等。

部署方式很简单，直接 docker 部署

```
docker run --name ams -d --net=host nibrev/ant-media-server:latest
```

然后访问 http://你的 ip:5080 就可以了，点开这个界面上传视频 ![pic](https://i.v2ex.co/m9k1LgmD.png)

然后新增直播，选择 playlist ![pic](https://i.v2ex.co/Ova1rQm8.png)

填上你上传的视频的链接 ![pic](https://i.v2ex.co/lcq60M47.png)

然后填上直播平台 rtmp 推流地址，开启直播就行了 ![pic](https://i.v2ex.co/W53O6o2W.png)

8m 出口带宽，现在540p 的画质同时向 b 站、斗鱼两个平台推送直播，不会卡，而且带宽占用如下：稳定下来，大概占用 3m 左右的出口带宽.
![pic](https://i.v2ex.co/wu15p87p.png)

相关项目：https://github.com/bytelang/kplayer-go

[取消回复](https://blog.upx8.com/3289#respond-post-3289)

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