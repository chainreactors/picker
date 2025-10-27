---
title: Windows与IOS设备局域网/内网传输文件方案推荐
url: https://blog.upx8.com/3066
source: 黑海洋 - WIKI
date: 2022-11-03
fetch_date: 2025-10-03T21:40:03.487489
---

# Windows与IOS设备局域网/内网传输文件方案推荐

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Windows与IOS设备局域网/内网传输文件方案推荐

发布时间:
2022-11-02

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
13715

# 前言

仅分享几个我测试过还可以接收的方案，本文不考虑公网传输。

可能并非最优解，还有很多可用的方法

# 支持上传、互传的IOS应用

比如 ES、Filebox、Alook等IOS应用，都支持监听本体端口，其他设备通过HTTP访问进行上传。

这种方法上传速度还算一般，但是比大多数家宽走公网快

# 数据线连接

比如爱思、iTunes等PC应用，这种方法对于线材和端口较差的设备比较麻烦，而且操作较为复制

# 网页Web RTC传输

[https://snapdrop.net/](https://blog.upx8.com/go/aHR0cHM6Ly9zbmFwZHJvcC5uZXQv)　需要设备支持webrtc，注意部分浏览器、插件、代理软件可能屏蔽webrtc，这个速度一般般，但是还算稳定。

# 发送端HTTP挂载分享

[https://www.voidtools.com/zh-cn/](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudm9pZHRvb2xzLmNvbS96aC1jbi8) （也就是Everything）在电脑用这个软件即可把整个电脑的全部硬盘映射到HTTP网页，其他设备直接进行HTTP访问即可，IOS设备请用ES进行下载视频，也可以直接用Filebox等软件播放视频。传输速度我个人还是比较满意的。

chfs 和这个差不多，我只用了Everything。

# 发送端SMB挂载分享

注意SMB极限速度就那样，不算很快，需要接收端支持SMB协议（比如Filebox和ES）

这个直接在电脑设置共享即可，请参考该文 [https://www.zhihu.com/question/20330664](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuemhpaHUuY29tL3F1ZXN0aW9uLzIwMzMwNjY0)

# 参考文档

[https://www.zhihu.com/question/20330664](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuemhpaHUuY29tL3F1ZXN0aW9uLzIwMzMwNjY0)

[https://geneliunx.com/2020/03/18/LAN-file-transfer/](https://blog.upx8.com/go/aHR0cHM6Ly9nZW5lbGl1bnguY29tLzIwMjAvMDMvMTgvTEFOLWZpbGUtdHJhbnNmZXIv)

[https://support.apple.com/zh-cn/guide/iphone/iphb14a056dd/16.0/ios/16.0](https://blog.upx8.com/go/aHR0cHM6Ly9zdXBwb3J0LmFwcGxlLmNvbS96aC1jbi9ndWlkZS9pcGhvbmUvaXBoYjE0YTA1NmRkLzE2LjAvaW9zLzE2LjA)

[https://www.zhihu.com/question/309005888](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuemhpaHUuY29tL3F1ZXN0aW9uLzMwOTAwNTg4OA)

[https://zhuanlan.zhihu.com/p/83983289](https://blog.upx8.com/go/aHR0cHM6Ly96aHVhbmxhbi56aGlodS5jb20vcC84Mzk4MzI4OQ)

[取消回复](https://blog.upx8.com/3066#respond-post-3066)

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