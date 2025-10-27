---
title: 【技术原创】Zimbra-SOAP-API开发指南5——邮件转发
url: https://www.4hou.com/posts/PJAl
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-23
fetch_date: 2025-10-04T02:18:11.931036
---

# 【技术原创】Zimbra-SOAP-API开发指南5——邮件转发

【技术原创】Zimbra-SOAP-API开发指南5——邮件转发 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】Zimbra-SOAP-API开发指南5——邮件转发

3gstudent
[技术](https://www.4hou.com/category/technology)
2022-12-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125861

收藏

导语：本文将要继续扩充开源代码Zimbra\_SOAP\_API\_Manage的功能，通过Zimbra SOAP API修改配置实现邮件转发，分享开发细节。

本文将要继续扩充开源代码Zimbra\_SOAP\_API\_Manage的功能，通过Zimbra SOAP API修改配置实现邮件转发，分享开发细节。

**0x01 简介**

本文将要介绍以下内容：

添加邮件转发

查看邮件转发的配置

查看文件夹共享的配置

开源代码

**0x02 添加邮件转发**

Zimbra支持将收到的邮件额外转发至另一邮箱，通过Web界面的操作方法如下：

登录邮箱后，依次选择Preferences->Mail

设置转发邮箱后，点击Save

如果想要转发多个邮箱，可以使用,进行分割，同时转发至两个邮箱的示例：test1@test.com,test2@test.com

接下来，通过抓包的方式分析实现流程，进而使用程序实现这部分功能

抓包获得的soap格式示例：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281063519061.png "1665280560798274.png")

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281064172907.png "1665280642170329.png")

对于清除邮件转发的设置，只需要将邮箱地址设置为空即可

**0x03 查看邮件转发的配置**

在我们添加邮件转发前，通常需要先获得邮箱转发的配置

通过抓包发现，在访问Web主页面时，如果存在邮件转发的设置，那么返回数据会增加以下内容：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281065169527.png "1665280711776543.png")

如果不存在邮件转发的设置，返回数据不存在字符zimbraPrefMailForwardingAddress

在程序实现上，访问Web主页面需要添加Cookie，再通过正则表达式筛选出指定的内容即可

实现代码示例：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281066658576.png "1665280754403960.png")

**0x04 查看文件夹共享的配置**

在上篇文章《Zimbra-SOAP-API开发指南4——邮件导出和文件夹共享》缺少了查看文件夹共享配置的方法，本文作为补充

通过抓包进行分析

发送的url示例： https://

发送的内容示例：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281067204536.png "1665280820908108.png")返回的内容示例：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281068139091.png "1665280865132318.png")

从以上内容可以知道，相关的请求为GetFolderRequest

查看GetFolderRequest的用法：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/GetFolder.html

经过前期的积累，这里也可以通过Zimbra SOAP API实现，发送GetFolderRequest，对返回内容进行筛选即可

收件箱存在文件共享的数据内容示例：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281068170198.png "1665280911124037.png")

在程序实现上，如果返回结果中存在字符

实现代码示例：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281069208860.png "1665280980185946.png")![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281070481932.png "1665280992681145.png")返回结果示例：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665281071210123.png "1665281052419496.png")

在删除文件夹共享的操作时，需要填入zid和Inbox对应的数字2即可

**0x05 开源代码**

新的代码已上传至github，地址如下：

https://github.com/3gstudent/Homework-of-Python/blob/master/Zimbra\_SOAP\_API\_Manage.py

添加以下四个功能：

AddForward：添加邮件转发

GetForward：查看邮件转发

GetShare：查看文件夹共享

RemoveForward：清除邮件转发的设置

**0x06 小结**

本文扩充了Zimbra SOAP API的调用方法，添加四个实用功能，实现方法和思路也可在XSS漏洞上进行测试。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?W3xt4A3I)

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