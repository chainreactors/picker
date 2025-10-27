---
title: 一款OutLook信息收集工具 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17129145.html
source: 博客园 - 渗透测试中心
date: 2023-02-18
fetch_date: 2025-10-04T07:23:02.796951
---

# 一款OutLook信息收集工具 - 渗透测试中心

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

# [一款OutLook信息收集工具](https://www.cnblogs.com/backlion/p/17129145.html "发布于 2023-02-17 09:58")

### 0x01 前言

这是一款burp插件，用于Outlook用户信息收集，在已登录Outlook账号后，可以使用该

插件自动爬取所有联系人的信息

### 0x02 安装

在burp扩展面板加载jar即可

### 0x03  功能介绍

#### 1.All Users

加载插件后，进入Outlook联系人面板，点击All Users

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095754648-934138006.jpg)

在burp中 Proxy -> HTTP history 筛选api接口

```
/owa/service.svc?action=FindPeople&app=People
```

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095755615-1407529720.jpg)

选中该请求，右键菜单 Extensions -> OutLook information collection -> Do OoutLook Email scan

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095756527-258145748.png)

会在 Extender -> Extensions -> OutLook information collection -> Output 中显示扫描进度

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095757297-634296044.png)

插件会自动爬取所有数据包并生成目录树，可以查看每一个请求响应包

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095758096-92972468.jpg)

右击该请求会弹出右键菜单，选择获取所有用户邮箱，即可获得所有的邮箱

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095758848-1201452255.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095759742-1384183711.jpg)

#### 2.注意

该Api会有大量相同url，不同的Post提交参数，如果选错了Api接口，会有弹窗提示

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095800733-584994050.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095801761-820625906.jpg)

#### 3.联系人信息

必须在加载 All Users的所有数据包才能正常使用，联系人信息基于All Users数据包信息，如果未进行第一步操作会有弹窗提醒

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095802597-563015457.jpg)

在burp中 Proxy -> HTTP history 筛选api接口

```
/owa/service.svc?action=GetPersona&app=People
```

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095803597-1431839783.jpg)

选中该请求，右键菜单 Extensions -> OutLook information collection -> Do OoutLook Email scan

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095804404-1030562578.png)

会在 Extender -> Extensions -> OutLook information collection -> Output 中显示扫描进度

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095805256-542719959.jpg)

插件会自动爬取所有数据包并生成目录树，可以查看每一个请求响应包

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095806159-1229654401.jpg)

右击该请求会弹出右键菜单，选择获取 All User个人信息，可获取所有联系人信息

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095807230-1070577141.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230217095808001-189242314.jpg)

**工具获取：公众号回复关键字“OutLook”**

posted @
2023-02-17 09:58
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(275)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025