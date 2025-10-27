---
title: Windows VPS DD重装为 Linux 一键脚本
url: https://blog.upx8.com/3215
source: 黑海洋 - WIKI
date: 2023-02-12
fetch_date: 2025-10-04T06:26:12.104548
---

# Windows VPS DD重装为 Linux 一键脚本

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Windows VPS DD重装为 Linux 一键脚本

发布时间:
2023-02-11

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
11011

![](https://sunpma.com/usr/uploads/2021/06/2597889658.jpg)

# 介绍

**适用于将`Windows VPS`重装为`Linux`系统，无需`VNC`和`DHCP`支持；**
**对于一些深度精简过的`Windows`系统可能不支持；**

# 方法

需要用到的三个文件`win32loader.bat` `initrd.img` `vmlinuz`
下载地址：

**下载地址：[https://sunpma.lanzoui.com/iPo2xq07ycj](https://blog.upx8.com/go/aHR0cHM6Ly9zdW5wbWEubGFuem91aS5jb20vaVBvMnhxMDd5Y2o)**

将下载的三个文件上传到Windows服务器；
右键以管理员身份运行`win32loader.bat`文件；
然后根据提示输入`2`选择`[2] Local file`使用本地文件；
出现提示后将`initrd.img`和`vmlinuz`两个文件移动至`C:\win32-loader\`目录后继续回车确认；
再次回车确认就开始重装系统为Linux；
**预览**
[![](https://sunpma.com/usr/uploads/2021/06/673566456.png)](https://sunpma.com/usr/uploads/2021/06/673566456.png)
**说明：默认安装系统为Debian9；用户名：`root`密码：`MoeClub.org`**
**成功安装`Debian9`后就可以用网络重装脚本重新安装其它系统了；**
**Debian/Ubuntu/CentOS 网络重装一键脚本：<https://blog.upx8.com/3035>**

脚本来源：[https://moeclub.org](https://blog.upx8.com/go/aHR0cHM6Ly9tb2VjbHViLm9yZy8)

[取消回复](https://blog.upx8.com/3215#respond-post-3215)

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