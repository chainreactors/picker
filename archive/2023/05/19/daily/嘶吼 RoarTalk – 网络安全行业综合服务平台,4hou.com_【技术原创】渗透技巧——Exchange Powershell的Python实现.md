---
title: 【技术原创】渗透技巧——Exchange Powershell的Python实现
url: https://www.4hou.com/posts/AO03
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-19
fetch_date: 2025-10-04T11:36:53.919985
---

# 【技术原创】渗透技巧——Exchange Powershell的Python实现

【技术原创】渗透技巧——Exchange Powershell的Python实现 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】渗透技巧——Exchange Powershell的Python实现

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-05-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)166573

收藏

导语：本文将要介绍通过Python实现远程执行Exchange Powershell命令的细节，分享使用Python实现TabShell利用的心得。

**0x00 前言**

远程执行Exchange Powershell命令可以通过Powershell建立powershell session 实现。而在渗透测试中，我们需要尽可能避免使用Powershell，而是通过程序去实现。本文将要介绍通过Python实现远程执行Exchange Powershell命令的细节，分享使用Python实现TabShell利用的心得。

**0x01 简介**

本文件将介绍以下内容：

执行 Exchange Powershell 命令的实际方法

开发细节

TabShell利用细节

**0x02 执行 Exchange Powershell 命令的实际方法**

**1.使用Powershell连接Exchange服务器，执行Exchange Powershell命令**

命令示例：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304892537957.png "1675304314189542.png")

需要注意以下问题：

需要域内主机上执行

需要fqdn，不支持IP

连接url可以选择http或者https

认证方式可以选择Basic或者Kerberos

**2.使用Python连接Exchange服务器，执行Exchange Powershell命令**

这里需要使用pypsrp

命令示例：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304893742036.png "1675304367193636.png")

**0x03 开发细节**

这里需要了解具体的通信格式，我采用的方法是使用pypsrp，打开调试信息，查看具体发送的数据格式

**1.启动调试信息**

将调试信息写到文件，代码如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304894141009.png "1675304420214417.png")

**2.增加调试输出内容**

修改文件pypsrp/wsman.py，在def send(self, message: bytes)中添加调试输出信息

具体代号位置：

https://github.com/jborean93/pypsrp/blob/master/src/pypsrp/wsman.py#L834，添加代码：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304894142308.png "1675304469122465.png")https://github.com/jborean93/pypsrp/blob/master/src/pypsrp/wsman.py#L841，添加代码：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304895128542.png "1675304516860752.png")输出结果显示如下图

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304896536726.png "1675304540131465.png")

**3.数据包数据结构**

可参考之前的文章《渗透技巧——远程访问Exchange Powershell》

经过对比分析，在编写程序上还需要注意以下细节：

(1)Kerberos认证的实际情况

示例代码：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304897136910.png "1675304586123320.png")

(2)通信数据格式

类型为POST

header需要包裹：'Accept-Encoding': 'identity'

(3)认证流程

需要先进行Kerberos认证，返回长度为0

再次发送数据，进行通信，返回正常内容

(4)数据编码

发送和接收的数据平均做了编码

发送过程序的代码显示示例代码：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304898146300.png "1675304625433949.png")

注：

hostname必须为小写字符

接收过程序的解码示例代码：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304898123015.png "1675304654193078.png")完整展示示例代码如下：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304899677610.png "1675304744802531.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304900119728.png "1675304755641532.png")完整代码的输出结果如下图

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304901114824.png "1675304785179170.png")

**0x04 TabShell利用细节**

TabShell的公开POC使用Powershell连接取接Exchange服务器，执行特殊构造的Exchange Powershell命令接触，为便于分析中间的通信数据，可以采用以下方法擦拭中间：

**1.通过Flask构建本地代理服务器**

方法可参考之前的文章《ProxyShell利用分析3——添加用户和文件写入》

**2.通过Flask实现SSRF**

SSRF漏洞可选择CVE-2022-41040或CVE-2022-41080

**3.在Flask中输出中间的通信数据**

关键字代码示例：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304902103020.png "1675304854112601.png")根据通信数据，我们可以很容易地写出TabShell的Python现代代码，完整代码的输出结果如下图

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675304903217111.png "1675304880180285.png")

**0x05 小结**

本文件介绍了通过 Python 实现远程执行 Exchange Powershell 命令的细节，分享使用 Python 实现 TabShell 使用的心得。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?wZaPzaJV)

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