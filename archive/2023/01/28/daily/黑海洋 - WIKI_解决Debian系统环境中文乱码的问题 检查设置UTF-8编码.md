---
title: 解决Debian系统环境中文乱码的问题 检查设置UTF-8编码
url: https://blog.upx8.com/3202
source: 黑海洋 - WIKI
date: 2023-01-28
fetch_date: 2025-10-04T05:04:20.468075
---

# 解决Debian系统环境中文乱码的问题 检查设置UTF-8编码

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 解决Debian系统环境中文乱码的问题 检查设置UTF-8编码

发布时间:
2023-01-27

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
17976

晚上升级[mdserver-web](https://blog.upx8.com/3051)面板，出现了乱码，应该是开发者干掉debian编码设置影响的。此时，需要重新设置编码格式。

#如果在安装Debian时编码选择不正确，可能会导致终端输出的提示内容是乱码。

在终端输入命令：dpkg-reconfigure locales

这时候会弹出编码列表

![](//imgsrc.baidu.com/imgad/pic/item/3912b31bb051f819367c218c9fb44aed2f73e79f.jpg)

选中下面1项（光标移上去，空格选中）：**zh\_CN.UTF-8 UTF-8 ，**按tab键，切换到下面的确定按钮（确定按钮也可能是乱码，左边那个是），回车。

![](//imgsrc.baidu.com/imgad/pic/item/4f4a20a4462309f7713e8fd4370e0cf3d6cad6a7.jpg)

此时，让你选择默认的编码，选择**zh\_CN.UTF-8**。

回车后，成功后**重启**即可。

**推荐一键更改Linux语言 ：**

wget -N --no-check-certificate https://raw.githubusercontent.com/notetoday/LocaleCN/master/LocaleCN.sh && bash LocaleCN.sh

[取消回复](https://blog.upx8.com/3202#respond-post-3202)

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