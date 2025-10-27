---
title: 【技术原创】Java利用技巧——Jetty Filter型内存马
url: https://www.4hou.com/posts/XVEg
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-06
fetch_date: 2025-10-04T11:29:56.999945
---

# 【技术原创】Java利用技巧——Jetty Filter型内存马

【技术原创】Java利用技巧——Jetty Filter型内存马 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 【技术原创】Java利用技巧——Jetty Filter型内存马

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-04-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)107739

收藏

导语：本文介绍了Jetty Filter型内存马的实现思路和细节，给出了可供测试的代码，分享了Zimbra环境的利用方法。

**0x00 前言**

关于Tomcat Filter型内存马的介绍资料有很多，但是Jetty Filter型内存马的资料很少，本文将要参照Tomcat Filter型内存马的设计思路，介绍Jetty Filter型内存马的实现思路和细节。

**0x01 简介**

本文将要介绍以下内容：

Jetty调试环境搭建

实现思路

实现代码

Zimbra环境下的Filter型内存马

**0x02 Jetty调试环境搭建**

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672718186182502.png "1672716500101267.png")

**0x03 实现思路**

相关参考资料：

https://github.com/feihong-cs/memShell/blob/master/src/main/java/com/memshell/jetty/FilterBasedWithoutRequest.java
https://blog.csdn.net/xdeclearn/article/details/125969653

参考资料1是通过JmxMBeanServer获得webappclassloaer，进而通过反射调用相关方法添加一个Filter

参考资料2是通过Thread获得webappclassloaer，进而通过反射调用相关方法添加Servlet型内存马的方法

我在实际测试过程中，发现通过JmxMBeanServer获得webappclassloaer的方法不够通用，尤其是无法在Zimbra环境下使用

因此，最终改为使用Thread获得webappclassloaer，进而通过反射调用相关方法添加Filter型内存马。

**0x04 实现代码**

**1.添加Filter**

Jetty下可用的完整代码如下：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672718188206717.png "1672716647105961.png")

**2.枚举Filter**

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672718197202572.png "1672717082184320.png")![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672718198170920.png "1672717976233133.png")(2)通过Thread获得webappclassloaer，通过反射读取\_filters属性来枚举Filter

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672718199169679.png "1672718060409764.png")**0x05 Zimbra环境下的Filter型内存马**

在Zimbra环境下，思路同样为使用Thread获得webappclassloaer，进而通过反射调用相关方法添加Filter型内存马

但是由于Zimbra存在多个名为WebAppClassLoader的线程，所以在添加Filter时需要修改判断条件，避免提前退出，在实例代码的基础上直接修改即可

**0x06 利用思路**

Filter型内存马的优点是不需要写入文件，但是会在服务重启时失效

**0x07 小结**

本文介绍了Jetty Filter型内存马的实现思路和细节，给出了可供测试的代码，分享了Zimbra环境的利用方法。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KlcabNCp)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/83af13989dee96c0471f.jpg)

# [3gstudent](https://www.4hou.com/member/bmZO)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bmZO)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)