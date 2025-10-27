---
title: 日常SRC中xss小tips - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16951930.html
source: 博客园 - 渗透测试中心
date: 2022-12-06
fetch_date: 2025-10-04T00:34:53.389782
---

# 日常SRC中xss小tips - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [日常SRC中xss小tips](https://www.cnblogs.com/backlion/p/16951930.html "发布于 2022-12-05 12:01")

## 0x00  前言

关于众测、专属中如何去捡漏xss洞，水文，水文，水文！！！

## 0x01  日常测试

日常无聊测站点，当你在渗透测试时候，发现有某个html标签调用服务器内图片的，并且是那种加入服务器ip地址的，可以尝试通过修改host头来fuzz一下，探测下是否存在xss。

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205120118289-2003703296.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205120119178-982184139.jpg)

看到这种情况我们可以大概猜想一下，其中的后段代码可能是以下样子：

<img src="<?php echo "http://{$\_SERVER['HTTP\_HOST']}/"?>xxx/aaa.png" />

这样看来就很简单了，修改一下请求包中的host就能造成xss咯。

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205120119915-1550751559.jpg)

成功弹窗

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205120120690-217287024.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205120121286-2038736915.jpg)

捡破烂小tips完结。

转自原来链接：

https://blog.csdn.net/Guapichen/article/details/124040935?spm=1001.2014.3001.5501

posted @
2022-12-05 12:01
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(233)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025