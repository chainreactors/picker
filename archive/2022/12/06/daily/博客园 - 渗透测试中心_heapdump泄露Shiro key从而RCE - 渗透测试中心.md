---
title: heapdump泄露Shiro key从而RCE - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16951510.html
source: 博客园 - 渗透测试中心
date: 2022-12-06
fetch_date: 2025-10-04T00:34:53.499472
---

# heapdump泄露Shiro key从而RCE - 渗透测试中心

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

# [heapdump泄露Shiro key从而RCE](https://www.cnblogs.com/backlion/p/16951510.html "发布于 2022-12-05 09:42")

## 1. 简介

我搭建了一个Spring heapdump泄露shiro key从而RCE的漏洞环境，Github地址：<https://github.com/P4r4d1se/heapdump_shiro_vuln>
漏洞利用条件：

* Spring Shiro环境
* 存在heapdump文件泄露
* 存在可利用链

## 2. 漏洞原理

Shiro相关的漏洞原理和调试分析已经有很多大佬分享过了，这里不再赘述，这里主要针对这个漏洞环境进行说明：
（1）Spring其实是有自己默认安全框架的，叫Spring Security，但可能有的开发用Shiro用习惯了，将Spring Securiy替换成了Shiro，这种情况并不少见，比如若依就是Spring shiro。

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094141235-716240315.jpg)

（2）在有key的情况下，即使是最新版的Shiro也一样存在漏洞，而且在很多时候都会因为开发、部署等问题导致shiro key的泄露。
（3）Shiro大于1.2.4的版本中，在没有开发人员人工干预的情况下key改为了随机生成，这个随机生成是在每次启动Web环境的时候，重启前这个key不会改变，可以在JVM虚拟机内存里找到。

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094142103-2055517121.jpg)

（4）Spring的heapdump文件就是从JVM虚拟机内存导出的。
综上所述导致了这个组合漏洞的产生。

## 3. 漏洞演示

加载漏洞环境后，可以看到Shiro版本为1.8.0：

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094143073-114670788.jpg)

访问8080端口的/actuator/heapdump获取heapdump文件：

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094143969-554120927.jpg)

[获取其中的shiro key，我常用的有两种方式：
（1）JDumpSpider：](https://xzfile.aliyuncs.com/media/upload/picture/20221130172927-7c76e054-7091-1.png)<https://github.com/whwlsfb/JDumpSpider>
这个小工具可以自动爬取heapdump中的变量信息，比较方便，坏处是可能会漏掉没在爬取列表中的信息。
直接运行:java -jar JDumpSpider.jar heapdump即可自动获取变量信息，这里获取到ShiroKey：

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094144681-379271828.jpg)

（2）jvisualvm.exe：Java自带的工具，默认路径为：JDK目录/bin/jvisualvm.exe
这个工具需要手动去找想要的信息，在过滤里输入org.apache.shiro.web.mgt.CookieRememberMeManager，圈出来的16个字节的值就是key：

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094145426-680950609.jpg)

用一个Python小脚本转成base64编码后的Shiro key：

用一个Python小脚本转成base64编码后的Shiro key：

```
import base64
import struct

print(base64.b64encode(struct.pack('<bbbbbbbbbbbbbbbb', 109,-96,12,-115,33,59,24,112,44,124,56,110,-15,59,1,-41)))
```

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094146189-419865832.jpg)

使用获得的key进行利用成功：

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094147320-612137025.jpg)

重新启动服务器再次获取shiro key，可以看到key改变了，验证了漏洞原理的第3点，每次启动生成一个随机key：

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094148077-2083177773.png)

改用新的key仍然可进行利用：

![](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221205094148947-1689724177.jpg)

转自原文链接[：](https://xzfile.aliyuncs.com/media/upload/picture/20221130172927-7c76e054-7091-1.png)<https://xz.aliyun.com/t/11908>

posted @
2022-12-05 09:42
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(1756)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025