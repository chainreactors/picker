---
title: 瑞数VMP bypass
url: https://darkless.cn/2025/04/10/rsvmp-bypass
source: darkless
date: 2025-04-11
fetch_date: 2025-10-06T22:05:11.983273
---

# 瑞数VMP bypass

[![](/images/logo1.svg)](/)
[darkless](/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

瑞数VMP bypass

![](https://cdn.jsdelivr.net/gh/handbye/images@master/uPic/2025/04/7NTLKb.png)

![](/images/avatar.webp)

darkless

2025-04-10

2025-04-10

* [web安全](/categories/web%E5%AE%89%E5%85%A8/)
* [工具使用](/categories/web%E5%AE%89%E5%85%A8/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/)

* [瑞数VMP](/tags/%E7%91%9E%E6%95%B0vmp/)

在某项目渗透过程中遇到了瑞数vmp防护，具体表现为不能重放数据包，重放时会报400或者412错误。

关于如何识别瑞数vmp和其版本，可以看这里：<https://blog.csdn.net/weixin_43411585/article/details/138332923>

![image.png](/../post_images/3cdb7b44191acae743c15ed8c6f55e1e.png)

找了几个绕过的方法，大多数是利用js补环境来模拟真实请求从而获取到可以绕过的cookie。但我尝试了一些项目都失败了，原因未知，例如这个项目：

[link\_preview](https://github.com/pysunday/sdenv)

那是不是可以利用类似playwright的框架启动无头浏览器访问目标网站呢，这样就和真实访问目标网站没什么区别，于是我有了如下思路：

![image.png](/../post_images/e69e7f9f058af0bd6854804718e47e3f.png)

有了这个思路后我借助cursor完成了整个项目，结果证明是可行的。项目地址：

[link\_preview](https://github.com/handbye/RSVmpBypass)

里面保存了利用cursor编写过程中的详细文档。其实过程是很曲折的，主要表现为如何让AI正确理解我的需求，我的经验是可以先利用chatgpt进行头脑风暴，让他完全理解你的需求并写出需求文档，然后在发送给cursor编写。

瑞数VMP bypass

/2025/04/10/rsvmp-bypass

作者

darkless

发布于

2025-04-10 08:00

许可

* [瑞数VMP](/tags/%E7%91%9E%E6%95%B0vmp/)

[完全由cursor开发的基于任务驱动的打点和扫描工具发布了
上一篇](/2025/7/30/tscan-tool/ "完全由cursor开发的基于任务驱动的打点和扫描工具发布了")

[云原生安全学习小记
下一篇](/2025/01/10/cloud-native-security/ "云原生安全学习小记")

评论

评论插件加载失败
点击重新加载

正在加载评论插件

© 2019 - 2025
   [darkless](/)

由 [Hexo](https://hexo.io) 驱动 & 主题 [Keep](https://github.com/XPoet/hexo-theme-keep)

![]()