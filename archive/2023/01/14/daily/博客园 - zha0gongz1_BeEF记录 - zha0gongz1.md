---
title: BeEF记录 - zha0gongz1
url: https://www.cnblogs.com/H4ck3R-XiX/p/17047431.html
source: 博客园 - zha0gongz1
date: 2023-01-14
fetch_date: 2025-10-04T03:49:54.934915
---

# BeEF记录 - zha0gongz1

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/zha0gongz1/)

# [zha0gongz1](https://www.cnblogs.com/zha0gongz1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/zha0gongz1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/zha0gongz1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [BeEF记录](https://www.cnblogs.com/zha0gongz1/p/17047431.html "发布于 2023-01-13 17:00")

## 前情提要

最近项目上常规手段遇阻，计划进行水坑钓鱼，一番搜索找到[近期SolarMarker组织的手法](https://www.esentire.com/blog/popular-info-stealing-malware-solarmarker-is-using-watering-hole-attacks-and-fake-chrome-browser-updates-to-infect-business-professionals-warns-esentire)，但是没有找到相关样本，于是就自己实现了一个类似的前端功能（水坑手法项目会持续记录学习，但目前不会放出，敬请谅解）。持续的检索收集，发现了沉睡已久的神器——BeEF，虽然此工具在当今实战环境中比较鸡肋，可用的功能不多，但秉着对该项目作者持续更新态度的尊敬，我认为应该抱着温故而知新的态度重新审视这个十年老工具，故而本文旨在探索记录使用过程。

## 老生常谈

网络上BeEF的使用方法很多，我在这里就不赘述了，简单记录下一些小技巧吧（后续有新发现会在这里记录）。

### 基础配置

根据个人情况及喜好修改默认配置，直接看图

![](https://img2023.cnblogs.com/blog/1449167/202301/1449167-20230113164517857-1207802470.jpg)

### 踩坑

在实际环境中，大多数网站都是https的，所以当你只是简单地开启BeEF服务时，浏览器不允许在https页面里嵌入http的请求，会出现以下错误：

![](https://img2023.cnblogs.com/blog/1449167/202301/1449167-20230113162822573-2029536281.jpg)

所以，我们此时要在BeEF的配置文件中，开启SSL证书，

![](https://img2023.cnblogs.com/blog/1449167/202301/1449167-20230113163255350-232164704.jpg)

并且修改 `./core/main/client/net.js` 文件中的通信协议
![](https://img2023.cnblogs.com/blog/1449167/202301/1449167-20230113170854619-804416201.jpg)

此处又存在一个问题，直接将js链接地址插入的话，会出现这种访问超时，但这实际上是开启SSL后未使用域名导致浏览器不信任证书，不能有效加载js，**需要配置合法域名**

![](https://img2023.cnblogs.com/blog/1449167/202301/1449167-20230113161514521-1985113999.png)

这里加载成功，是因为我手动信任了该链接地址，浏览器默认信任访问

![](https://img2023.cnblogs.com/blog/1449167/202301/1449167-20230113163843193-611608435.jpg)

不太重要的一点，修改类似以上配置后，记得重新启动BeEF服务。

## 完

附：
[js在线混淆工具](https://obfuscator.io/)
参考链接：
<https://stackoverflow.com/questions/60360151/how-to-run-beef-behind-an-nginx-reverse-proxy-with-ssl-correctly>

朋友可以背叛你，但技术和身材不会

posted @
2023-01-13 17:00
[zha0gongz1](https://www.cnblogs.com/zha0gongz1)
阅读(318)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025