---
title: 【技术原创】Zimbra-SOAP-API开发指南3——操作邮件
url: https://www.4hou.com/posts/RBBq
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-27
fetch_date: 2025-10-03T20:59:24.877108
---

# 【技术原创】Zimbra-SOAP-API开发指南3——操作邮件

【技术原创】Zimbra-SOAP-API开发指南3——操作邮件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】Zimbra-SOAP-API开发指南3——操作邮件

3gstudent
[技术](https://www.4hou.com/category/technology)
2022-10-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)179175

收藏

导语：本文扩充了Zimbra SOAP API的调用方法，添加三个实用功能：查看邮件、发送邮件和删除邮件，记录实现细节。

**0x00 前言**

在之前的文章《Zimbra SOAP API开发指南》和《Zimbra-SOAP-API开发指南2》介绍了Zimbra SOAP API的调用方法，开源代码Zimbra\_SOAP\_API\_Manage。 本文将要在此基础上扩充功能，添加邮件操作的相关功能。

**0x01 简介**

本文将要介绍以下内容：

查看邮件

发送邮件

删除邮件

**0x02 查看邮件**

Zimbra SOAP API说明文档：https://files.zimbra.com/docs/soap\_api/9.0.0/api-reference/index.html

结合Zimbra SOAP API说明文档和调试结果得出以下实现流程：

调用Search命令获得邮件对应的Item id，通过Item id作为邮件的识别标志。

获得Item id后可以对邮件做进一步操作，如查看邮件细节、移动邮件、删除邮件等。

**1.获得邮件对应的Item id**

需要使用Search命令。

说明文档：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/Search.html

需要用到以下参数：

(1)query

表示查看的位置，示例如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326054139274.png "1661325531848174.png")

(2)limit

表示返回的查询结果数量，示例如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326054211003.png "1661325558176160.png")

如果不指定该属性，默认为10

测试代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326055461293.png "1661325579132879.png")

返回内容示例：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326055188874.png "1661325598154496.png")

对以上格式分析，发现标签<c\*\*\*对应每个邮件的信息，提取数据如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326055389069.png "1661325617124360.png")

格式分析如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326056208642.png "1661325641100924.png")

时间格式转换的示例代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326056411872.png "1661325655174150.png")

综合以上内容，得出提取Item id、发件人、标题、正文内容和发送时间的实现代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326057131421.png "1661325688690691.png")

**2.查看邮件内容**

测试发现，查看邮件细节可以不依赖Zimbra SOAP API，访问固定url即可。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326057195495.png "1661325711332352.png")

通过这种方式可以获得完整的邮件内容，包括Base64编码的附件内容。

实现代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326057129090.png "1661325729154606.png")

**0x03 发送邮件**

在发送带有附件的邮件时，需要先上传附件，再发送。

**1.上传附件**

上传功能通过FileUploadServlet实现，对应代码位置：/opt/zimbra/lib/jars/zimbrastore.jar中/com.zimbra/cs/service/FileUploadServlet.class

上传细节可参考：https://github.com/Zimbra/zm-mailbox/blob/develop/store/docs/file-upload.txt

上传的url: https://

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326058172727.png "1661325773266042.png")

如果添加参数fmt=raw,extended，返回结果示例：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326058204976.png "1661325790453812.png")

经过比较，发现添加参数fmt=raw,extended能够额外获得文件类型，示例:"ct":"image/jpeg"

所以在上传时，使用url: https://<  url >/service/upload?fmt=raw,extended

综合以上内容，得出以下实现代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326058193655.png "1661325841170563.png")

**2.发送带有附件的邮件**

需要使用SendMsg命令。

说明文档：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/SendMsg.html

需要用到以下参数：

(1)e

表示发件人和收件人等相关信息，示例如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326059225092.png "1661325869196498.png")

(2)su

表示邮件标题，示例如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326059188330.png "1661325883767156.png")

(3)mp

表示正文内容，示例如下：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326059127116.png "1661325906122528.png")

(4)noSave

如果设置为1，表示邮件发送后，不在发件箱保存副本，示例代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326060630463.png "1661325923194743.png")

(5)attach

指定发送附件的aid，示例代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326060206232.png "1661325939102685.png")

综合以上内容，得出发送带有附件邮件的实现代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326060180006.png "1661325959749521.png")

**0x04 删除邮件**

需要使用ConvAction命令。

说明文档：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/ConvAction.html

需要用到以下参数：

(1)tcon

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326061214045.png "1661325995141916.png")

通过浏览器删除邮件的流程是先点击删除邮件，将邮件移动至垃圾箱，再从垃圾箱中点击删除邮件，完成邮件的彻底删除。

通过Zimbra-SOAP-API可以简化以上流程，直接删除邮件。

实现代码：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220824/1661326061831277.png "1661326023184169.png")

**0x05 开源代码**

新的代码已上传至github，地址如下：

https://github.com/3gstudent/Homework-of-Python/blob/master/Zimbra\_SOAP\_API\_Manage.py

优化了代码结构，增加了以下功能：

DeleteMail，删除指定邮件

SearchMail，获得邮箱信息，包括Item id、发件人、标题、正文内容和发送时间

SendTestMailToSelf，向当前邮箱发送一封带有附件的邮件

uploadattachment，上传附件

uploadattachmentraw，上传附件的另一种实现，用于特定条件

viewmail，查看邮件完整细节

**0x06 小结**

本文扩充了Zimbra SOAP API的调用方法，添加三个实用功能：查看邮件、发送邮件和删除邮件，记录实现细节。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Gw7bRt33)

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
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https:/...