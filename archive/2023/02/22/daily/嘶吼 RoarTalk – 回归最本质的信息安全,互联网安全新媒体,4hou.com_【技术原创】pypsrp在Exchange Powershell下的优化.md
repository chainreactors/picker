---
title: 【技术原创】pypsrp在Exchange Powershell下的优化
url: https://www.4hou.com/posts/ykgR
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-22
fetch_date: 2025-10-04T07:41:12.158638
---

# 【技术原创】pypsrp在Exchange Powershell下的优化

【技术原创】pypsrp在Exchange Powershell下的优化 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】pypsrp在Exchange Powershell下的优化

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-02-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124947

收藏

导语：pypsrp是用于PowerShell远程协议(PSRP)服务的Python客户端。我在研究过程中，发现在Exchange Powershell下存在一些输出的问题，本文将要介绍研究过程，给出解决方法。

**0x00 前言**

pypsrp是用于PowerShell远程协议(PSRP)服务的Python客户端。我在研究过程中，发现在Exchange Powershell下存在一些输出的问题，本文将要介绍研究过程，给出解决方法。

**0x01 简介**

Exchange PowerShell Remoting

pypsrp的使用

pypsrp存在的输出问题

解决方法

**0x02 Exchange PowerShell Remoting**

参考资料：

https://docs.microsoft.com/en-us/powershell/module/exchange/?view=exchange-ps

默认设置下，需要注意以下问题：

所有域用户都可以连接Exchange PowerShell

需要在域内主机上发起连接

连接地址需要使用FQDN，不支持IP

通过Powershell连接Exchange PowerShell的命令示例：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864415101637.png "1669862796110917.png")

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864416210278.png "1669862838218584.png")如果想要加入调试信息，可以添加以下代码：

![WX20221201-104743@2x.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864417737515.png "1669862875202761.png")

**0x03 pypsrp存在的输出问题**

我们在Exchange PowerShell下执行命令的完整返回结果如下图

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864417864294.png "1669862959142379.png")但是通过pypsrp连接Exchange PowerShell执行命令时，输出结果不完整，无法获得命令的完整信息，如下图

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864418210096.png "1669863021768918.png")

**0x04 解决方法**

1.定位问题

通过查看源码，定位到代码位置：https://github.com/jborean93/pypsrp/blob/704f6cc49c8334f71b12ce10673964f037656782/src/pypsrp/messages.py#L207

我们可以在这里添加输出message\_data的代码，代码示例：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864418716014.png "1669863113163687.png")返回结果：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864421597913.png "1669863266189727.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864423209350.png "1669863278169261.png")![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864425357342.png "1669863294836089.png")![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864427807163.png "1669863308135421.png")在调用serializer.deserialize(message\_data)提取输出结果时，这里只提取到了一组数据，忽略了完整的结果

经过简单的分析，发现标签内包含完整的输出结果，所以这里可先通过字符串截取提取出标签内的数据，示例代码：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864427167099.png "1669864228235221.png")进一步分析提取出来的数据，发现每个标签分别对应一项属性，为了提高效率，这里使用xml.dom.minidom解析成xml格式并提取元素，示例代码：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864429400992.png "1669864274181496.png")经测试，以上代码能够输出完整的结果

按照pypsrp的代码格式，得出优化pypsrp输出结果的代码：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864430117997.png "1669864312118430.png")使用修改过的pypsrp连接Exchange PowerShell执行命令时，能够返回完整的输出结果，如下图

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864431883166.png "1669864350854650.png")

经测试，在测试ProxyShell的过程中，使用修改过的pypsrp也能得到完整的输出结果

补充：

如果使用原始版本pypsrp测试ProxyShell，可通过解析代理的返回结果实现，其中需要注意的是在作Base64解密时，由于存在不可见字符，无法使用.decode('utf-8')解码，可以换用.decode('ISO-8859-1')，还需要考虑数据被分段的问题，实现的示例代码如下：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669864432213646.png "1669864386118305.png")**0x05 小结**

本文介绍了通过pypsrp连接Exchange PowerShell执行命令返回完整输出结果的解决方法。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?jfR5Mjcy)

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