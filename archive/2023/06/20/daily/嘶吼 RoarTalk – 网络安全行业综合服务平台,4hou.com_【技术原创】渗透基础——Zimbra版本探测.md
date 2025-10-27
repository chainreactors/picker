---
title: 【技术原创】渗透基础——Zimbra版本探测
url: https://www.4hou.com/posts/vJNm
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-20
fetch_date: 2025-10-04T11:46:52.677374
---

# 【技术原创】渗透基础——Zimbra版本探测

【技术原创】渗透基础——Zimbra版本探测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】渗透基础——Zimbra版本探测

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-06-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)244163

收藏

导语：本文将要介绍Zimbra版本探测的多种方法，通过Python实现自动化，记录开发细节，开源代码。

**0x00 前言**

本文将要介绍Zimbra版本探测的多种方法，通过Python实现自动化，记录开发细节，开源代码。

**0x01 简介**

本文将要介绍以下内容：

实现思路

实现细节

开源代码

**0x02 实现思路**

查看Zimbra版本的方法有很多，各有优缺点，具体方法如下：

**1.通过Web管理页面**

通过浏览器访问7071管理页面，在主页面会显示当前Zimbra版本

例如我的测试环境显示为：

Zimbra Version: 9.0.0\_GA\_4273.NETWORK

通过该方法获得的版本为准确版本

**2.通过执行命令**

![微信截图_20230303155211.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830753132808.png "1677829891245433.png")

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830753106259.png "1677829951104583.png")

注：

Zimbra补丁更新可参考：

https://wiki.zimbra.com/wiki/Zimbra\_Releases/9.0.0/patch\_installation

**3.通过Zimbra SOAP API**

默认配置下，zimbraSoapExposeVersion属性为FLASE，查询命令：

![微信截图_20230303155456.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830754886086.png "1677830062134842.png")返回结果：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830754821014.png "1677830110101646.png")需要将zimbraSoapExposeVersion属性设置为TRUE后，可以通过Zimbra SOAP API获得版本，修改属性的命令为：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830754569183.png "1677830189600557.png")发送的SOAP格式示例：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830755438166.png "1677830221152790.png")默认配置下的返回结果：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830755745155.png "1677830287279808.png")

**4.通过imap协议**

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830756160246.png "1677830387939089.png")

**5.通过imap over ssl协议**

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830756286265.png "1677830428110338.png")

**6.通过特定url**

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830759167157.png "1677830477536560.png")

**0x03 实现细节**

综合以上探测方法，为了适应多种环境，在程序实现上选取了通过imap协议、通过imap over ssl协议和通过特定url三种方法实现

**1.通过imap协议**

完整示例代码：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830759167859.png "1677830555183719.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830760115016.png "1677830564204934.png")

**2.通过imap over ssl协议**

需要将ip转为hostname作为参数，示例代码:

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830760110692.png "1677830604118208.png")

完整示例代码：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830761166425.png "1677830659211324.png")![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830761190376.png "1677830671123096.png")

存在部分环境无法将ip转为hostname，导致报错：[Errno 11004] host not found，所以在程序判断逻辑上优先使用imap协议

**3.通过特定url**

完整示例代码：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830762179793.png "1677830733202663.png")![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677830763159907.png "1677830743114650.png")

**0x04 开源代码**

完整的实现代码已上传至github，地址如下：

https://github.com/3gstudent/Homework-of-Python/blob/master/Zimbra\_GetVersion.py

代码首先尝试通过特定url获得版本信息，再通过imap协议读取版本信息，如果失败，最后通过imap over ssl协议读取版本信息

**0x05 小结**

本文介绍了Zimbra版本探测的多种方法，比较优缺点，选取有效的方法并通过Python实现自动化，记录开发细节，开源代码，作为一个很好的学习示例。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?xZQVAl1i)

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