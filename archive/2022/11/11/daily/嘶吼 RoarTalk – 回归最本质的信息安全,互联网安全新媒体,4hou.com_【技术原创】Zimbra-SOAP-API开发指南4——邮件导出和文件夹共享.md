---
title: 【技术原创】Zimbra-SOAP-API开发指南4——邮件导出和文件夹共享
url: https://www.4hou.com/posts/LBwW
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-11
fetch_date: 2025-10-03T22:21:23.130465
---

# 【技术原创】Zimbra-SOAP-API开发指南4——邮件导出和文件夹共享

【技术原创】Zimbra-SOAP-API开发指南4——邮件导出和文件夹共享 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】Zimbra-SOAP-API开发指南4——邮件导出和文件夹共享

3gstudent
[技术](https://www.4hou.com/category/technology)
2022-11-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)210560

收藏

导语：本文将要继续扩充开源代码Zimbra\_SOAP\_API\_Manage的功能，实现邮件导出和文件夹共享，分享开发细节。

**0x00 前言**

本文将要继续扩充开源代码Zimbra\_SOAP\_API\_Manage的功能，实现邮件导出和文件夹共享，分享开发细节。

**0x01 简介**

本文将要介绍以下内容：

邮件导出

文件夹共享

开源代码

**0x02 邮件导出**

Zimbra支持导出当前邮箱的所有邮件，通过Web界面的操作方法如下：

登录邮箱后，依次选择Preferences->Import/Export，如下图

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665218998208715.png "1665216681213169.png")

接下来，通过抓包的方式分析实现流程，进而使用程序实现这部分功能

**1.默认配置导出邮件**

默认配置下，会导出所有邮件，以压缩包的形式保存

访问URL示例：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665218998185816.png "1665216792209354.png")

参数解析：

admin%40test.com为邮箱用户，可以用~替代

filename=All-2022-07-27-181056为存在记录时保存的文件名，2022-07-27-181056对应的时间格式为年-月-日-时分秒，时间为带时区的时间，需要计算时差

emptyname=No+Data+to+Export为空记录时保存的文件名

在程序实现上，需要同Web操作的格式保持一致，代码细节：

(1)构造保存的文件名

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665218999582309.png "1665216861140158.png")

(2)保存文件

保存文件时使用binary写入

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219000387217.png "1665216914104688.png")

实现代码示例：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219001104494.png "1665218065155369.png")

**2.加入筛选条件导出邮件**

高级选项下，可以添加筛选条件，导出特定的邮件

访问URL示例：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219002874854.png "1665218116190059.png")

参数解析，新增加了以下参数：

start=1658818800000为筛选的起始时间，格式为unix时间戳，没有额外计算时差

end=1658991600000为筛选的结束时间，格式为unix时间戳，没有额外计算时差

query=content%3Apassword为筛选的关键词，作用是查询正文中带有password关键词的邮件

筛选条件的语法可参考：https://wiki.zimbra.com/wiki/Zimbra\_Web\_Client\_Search\_Tips

代码实现细节：

(1)时间格式转换的示例代码

时间转换成秒：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219003114616.png "1665218174183063.png")秒转换成时间：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219003847777.png "1665218247154563.png")

实现代码示例：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219004888464.png "1665218389199681.png")![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219005148858.png "1665218401213996.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219006213266.png "1665218412142321.png")

**0x03 文件夹共享**

**1.流程分析**

Zimbra支持将当前邮箱的文件夹共享至其他用户，通过Web界面的操作方法如下：

登录邮箱后，依次选择Preferences->Sharing，如下图

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219008425822.png "1665218469213069.png")

文件夹共享可选择以下三个文件夹：

Inbox

Sent

Junk

如下图

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219009697239.png "1665218523115104.png")

设置共享属性如下图

需要区别以下设置：

(1)Role

Viewer只能查看邮件

Manager可以修改邮件

(2)Message

Send stanard message，在设置后会向目的邮箱发送一份确认邮件

Do not send mail about this share，不发送确认邮件

这里可以通过抓包分析每项设置对应的具体数值

示例数据包1：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219009122573.png "1665218621269037.png")

格式分析：

(1)

id="2"表示Inbox

Sent对应id="5"

Junk对应id="4"

通过测试，还可以指定Drafts，对应id="6"

(2)

d="test1@test.com"表示可访问共享的邮箱

perm="r"表示权限为可读，对应Viewer

Manager对应的配置为perm="rwidx"，表示权限为读、写、添加和删除

如果设置了Send stanard message，在设置后会向目的邮箱(例如test1@test.com)发送一份确认邮件，数据包格式示例：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219010116653.png "1665218697300869.png")

邮箱test1@test.com会收到一份邮件，确认是否接受文件夹共享

**2.代码实现**

(1)添加文件共享

需要指定目标邮箱和共享文件夹

添加文件共享成功的响应中返回共享文件夹对应的zid

实现代码示例：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219011190182.png "1665218800207166.png")![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219012944427.png "1665218812131684.png")![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219013199312.png "1665218822588262.png")

(2)发送文件共享请求

需要指定目标邮箱

实现代码示例：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219014170823.png "1665218890102508.png")![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219015926953.png "1665218902103166.png")

这里需要注意，只有在添加文件共享后，发送文件共享请求才能成功返回200，否则返回500，提示invalid request: no matching grant

(3)删除文件共享

需要指定目标邮箱对应的zid和共享文件夹，zid可在添加文件共享成功的响应中获得

实现代码示例：

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219016541161.png "1665218972101917.png")![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665219017781853.png "1665218982355691.png")

**0x04 开源代码**

新的代码已上传至github，地址如下：

https://github.com/3gstudent/Homework-of-Python/blob/master/Zimbra\_SOAP\_API\_Manage.py

添加以下五个功能：

AddShare：添加文件夹共享，默认权限为rwidx

ExportMail：导出带有搜索条件的邮件，可指定日期和关键词

ExportMailAll：导出所有邮件

RemoveShare：删除当前邮箱的文件夹共享

SendShareNotification：在添加文件夹共享后，向目标邮箱发送一封确认邮件

**0x05 小结**

本文扩充了Zimbra SOAP API的调用方法，添加五个实用功能，实现方法和思路还可在XSS漏洞上进行测试。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ghedK364)

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
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www....