---
title: BT最新版一处RCE&后门&登录漏洞 - sevck
url: https://www.cnblogs.com/sevck/p/17466884.html
source: 博客园 - sevck
date: 2023-06-09
fetch_date: 2025-10-04T11:44:45.093455
---

# BT最新版一处RCE&后门&登录漏洞 - sevck

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/sevck/)

# [Sevck's Blog](https://www.cnblogs.com/sevck)

## 关注互联网安全，软件开发，这里记录着我的渗透心得、开发文摘、随笔心情(Linux,Windows,Python,Java.Lua,JS,C++在学习)。JAVA安全网:https://www.javasec.cn

* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [BT最新版一处RCE&后门&登录漏洞](https://www.cnblogs.com/sevck/p/17466884.html "发布于 2023-06-08 16:24")

审计搞了宝塔好几个版本，花了也不算短时间，屯了3个洞

1.一个命令执行 （有一定利用条件，最开始不能回显，配合DNSLOG完成回显）

2.一个不死后门（非官方，自留后门,用来持续维持权限）

　　适用

　　　　Linux/windows

　　　　测试版本：

* + linux 7.9.8
  + Windows 6.7.0
  + Windows. 7.8.0

　　更新日志：

　　　　2022年12月17日 增加无账号登录、日志清理

　　　　2023年03月20日增加linux/windows后门注入

　　　　2023年03月21日 增加命令执行,面板防止修复

　　　　2023年04月04日 兼容windows7.8.0版本

　　　　2023年04月07日 增加拒绝宝塔云扫描webshell

3.一个登录利用

还是需要一定利用条件，需要组合，如果无限制RCE那就无敌了。如果有个任意文件下载，

测试自己服务器、办案目标站点都没问题，linux root权限，windows system权限

![](https://img2023.cnblogs.com/blog/737185/202306/737185-20230608161031021-1181189332.png)

![](https://img2023.cnblogs.com/blog/737185/202306/737185-20230608161700083-462522817.png)

![](https://img2023.cnblogs.com/blog/737185/202306/737185-20230608161745013-584087583.png)

【版权所有@Sevck 博客地址http://www.cnblogs.com/sevck】 可以转载，注明出处.

posted @
2023-06-08 16:24
[sevck](https://www.cnblogs.com/sevck)
阅读(2534)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)