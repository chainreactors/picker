---
title: Windows开启sudo命令教程
url: https://blog.upx8.com/4376
source: 黑海洋 - WIKI
date: 2024-11-03
fetch_date: 2025-10-06T19:15:39.996335
---

# Windows开启sudo命令教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Windows开启sudo命令教程

发布时间:
2024-11-02

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
59302

#### windows 24h2 在开发者选项中可以直接开启sudo设置，开发者选项，启用sudo。

![](https://fastly.jsdelivr.net/gh/zsxwz/tuchuang2@latest/2024/11/02/e8b776f03a4cbc616200a6fc068002c6.png)

24h2 之前的版本，开启方法：

github：[https://github.com/microsoft/sudo](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21pY3Jvc29mdC9zdWRv)

26052 或以上的 Windows 可以直接使用，没有的话，自己下载一个也是一样的。

下载：[https://lanzoui.com/iJtqQ1ops6ej](https://blog.upx8.com/go/aHR0cHM6Ly9sYW56b3VpLmNvbS9pSnRxUTFvcHM2ZWo)

添加到系统环境变量目录：

win+r 打开目录：%SystemRoot%\System32\

把sudo.exe 移动进去就可以了。

设置权限：

以管理员身份打开powershell或者cmd：

```
sudo config --enable 启用模式
模式可选：forceNewWindow、disableInput、normal，“在新窗口中”、“禁用输入”、“内联”模式。

比如内联模式，就和linux终端一样。
sudo config --enable normal
```

使用：

打开没有管理员身份的powershell或者cmd，如果遇到需要管理员身份才能运行的命令，就可以直接在前面加sudo了

####

[取消回复](https://blog.upx8.com/4376#respond-post-4376)

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