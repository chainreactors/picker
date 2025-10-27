---
title: sql盲注快速出数据之超级注入工具 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17074602.html
source: 博客园 - 渗透测试中心
date: 2023-01-31
fetch_date: 2025-10-04T05:14:24.630020
---

# sql盲注快速出数据之超级注入工具 - 渗透测试中心

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

# [sql盲注快速出数据之超级注入工具](https://www.cnblogs.com/backlion/p/17074602.html "发布于 2023-01-30 10:10")

一些朋友在群里经常遇到sql注入的问题，有时候有waf、有时候是盲注、有时候不知道如何下手? 今天分享一款工具，名字是超级注入工具

下载地址： https://github.com/shack2/SuperSQLInjectionV1

案例1:  带waf的盲注

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101107212-90175087.png)

如下图，单引号报错，而且有报错回显，这种情况利用就是典型的布尔盲注，只要我们能在后面构造一个 and 1=1 或者 or 1=1这种语句，就能出数据

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101131425-356375614.png)

这里是mysql的数据库，通常借助if函数来布尔注入，waf通常不拦单个if()，但会拦if(1,1,1)这种，如果拦了，可以把1替换成11-10，2替换成12-10这种

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101204863-503051983.png)

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101222813-968703287.png)

然后，超级注入工具一把梭就行了，

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101307542-1419344949.png)

绕过waf正则就下面这种，比较简单

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101344123-592448871.png)

案例2:

  案例1构造的and是为了超级注入工具去识别页面返回的内容，去判断出 1=1正确的页面字段和1=2错误页面的字段，正常工具是识别不到注入点的，所以你要指定字段，给工具一个布尔注入的依据！

再来看一个例子，希望你能理解我的意思，，

如下图，还是mysql，成功构造出一个if

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101406519-1710661959.png)

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101416464-592041923.png)

报文贴入超级注入工具，这款工具测试盲注只会测试1=1和1=2,所以，在if的第一个位置设置payload，看右下角的框，已经识别到正确页面的回显值，那后面，数据就出来了！

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101428882-828580557.png)

案例3:

这里提供一个mssql类型的，

也就是Sql-server，站点存在waf,测试oR 1=1 和 1=2这种不拦截，利用1=1这里构造下数据包，sql注入工具就能识别到布尔值了，

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101444979-720843412.png)

后面就无脑出数据了，

![](https://img2023.cnblogs.com/blog/1049983/202301/1049983-20230130101457121-71717272.png)

原文连接：https://mp.weixin.qq.com/s/jrv1ZLjZ3IbtloRCXWDo-Q

posted @
2023-01-30 10:10
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(1489)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025