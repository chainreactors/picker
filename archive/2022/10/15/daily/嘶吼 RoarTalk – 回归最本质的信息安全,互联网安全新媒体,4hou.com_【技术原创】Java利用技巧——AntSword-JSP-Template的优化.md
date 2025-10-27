---
title: 【技术原创】Java利用技巧——AntSword-JSP-Template的优化
url: https://www.4hou.com/posts/XVVW
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-15
fetch_date: 2025-10-03T19:55:14.193827
---

# 【技术原创】Java利用技巧——AntSword-JSP-Template的优化

【技术原创】Java利用技巧——AntSword-JSP-Template的优化 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】Java利用技巧——AntSword-JSP-Template的优化

3gstudent
[技术](https://www.4hou.com/category/technology)
2022-10-14 11:33:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138962

收藏

导语：本文分享了一种不额外生成.class文件的实现方法，对于开源的代码test4.jsp，还可以应用到Java文件的编写中。

**0x00 前言**

在之前的文章[《Java利用技巧——通过反射实现webshell编译文件的自删除》](https://www.4hou.com/posts/rVr2)曾介绍了通过反射实现AntSword-JSP-Template的方法。对于AntSword-JSP-Template中的shell.jsp，访问后会额外生成文件shell\_jsp$U.class。《Java利用技巧——通过反射实现webshell编译文件的自删除》中的方法，访问后会额外生成文件shell\_jsp$1.class。

在某些特殊环境下，需要避免额外生成.class文件。本文将以Zimbra环境为例，介绍实现方法，开源代码，记录细节。

**0x01 简介**

本文将要介绍以下内容：

**·** 实现思路

**·**实现代码

**0x02 实现思路**

基于[《Java利用技巧——通过反射实现webshell编译文件的自删除》](https://www.4hou.com/posts/rVr2)中的方法，访问后会额外生成文件shell\_jsp$1.class，这里可以通过构造器避免额外生成.class文件。

在具体使用过程中，需要注意如下问题：

**(1)反射机制中的构造器**

正常调用的代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661328796136651.png "1661328550166594.png")

通过反射实现的代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661328796182238.png "1661328561116025.png")

**(2)选择合适的defineClass()方法**

在ClassLoader类中，defineClass()方法有多个重载，可以选择一个可用的重载。

本文选择defineClass(byte[] b, int off, int len)

**(3)SecureClassLoader**

使用构造器时，应使用SecureClassLoader，而不是ClassLoader

示例代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661328797213950.png "1661328596152548.png")

**0x03 实现代码**

为了方便比较，这里给出每种实现方法的代码:

**(1)test1.jsp**

来自AntSword-JSP-Template中的shell.jsp，代码如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661328797469453.png "1661328622106759.png")

保存在Zimbra的web目录：/opt/zimbra/jetty\_base/webapps/zimbra/

通过Web访问后在目录/opt/zimbra/jetty\_base/work/zimbra/jsp/org/apache/jsp/生成以下文件：

**·** \_test1\_jsp.java

**·**\_test1\_jsp.class

**·**\_test1\_jsp$U.class

**(2)test2.jsp**

来自[《Java利用技巧——通过反射实现webshell编译文件的自删除》](https://www.4hou.com/posts/rVr2)中通过反射实现AntSword-JSP-Template的方法，代码如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661328797254387.png "1661328723132675.png")

通过Web访问后生成以下文件：

**·** \_test2\_jsp.java

**·**\_test2\_jsp.class

**·**\_test2\_jsp$1.class

**(3)test3.jsp**

基于test2.jsp，通过构造器实现，代码如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661328798393361.png "1661328760142358.png")

通过Web访问后生成以下文件：

**·**\_test3\_jsp.java

**·** \_test3\_jsp.class

**(4)test4.jsp**

基于test3.jsp，不使用base64Decode()，代码如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661328796176623.png "1661328796176623.png")

通过Web访问后生成以下文件：

**·** \_test4\_jsp.java

**·** \_test4\_jsp.class

在代码实现上需要注意Java语言中数组必须先初始化，然后才可以使用。

**0x04 小结**

本文分享了一种不额外生成.class文件的实现方法，对于开源的代码test4.jsp，还可以应用到Java文件的编写中。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uuafbWeS)

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