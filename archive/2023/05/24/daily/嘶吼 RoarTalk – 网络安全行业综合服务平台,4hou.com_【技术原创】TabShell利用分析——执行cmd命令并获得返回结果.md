---
title: 【技术原创】TabShell利用分析——执行cmd命令并获得返回结果
url: https://www.4hou.com/posts/DEmy
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-24
fetch_date: 2025-10-04T11:37:47.523197
---

# 【技术原创】TabShell利用分析——执行cmd命令并获得返回结果

【技术原创】TabShell利用分析——执行cmd命令并获得返回结果 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】TabShell利用分析——执行cmd命令并获得返回结果

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-05-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)148003

收藏

导语：本文将要介绍利用TabShell执行cmd命令并获得返回结果的方法，分享通过Python编写脚本的细节。

**0x00 前言**

利用TabShell可以使用普通用户逃避沙箱并在Exchange Powershell中执行任意cmd命令，本文将要介绍利用TabShell执行cmd命令并获得返回结果的方法，分享通过Python编写脚本的细节。

**0x01 简介**

本文将要介绍以下内容：

执行cmd命令并获得返回结果的方法

Python实现

**0x02 执行cmd命令并获得返回结果的方法**

testanull公开了一个利用的POC，地址如下：https://gist.github.com/testanull/518871a2e2057caa2bc9c6ae6634103e

为了能够支持更多的命令，POC需要做简单修改，细节如下：

某些命令无法执行，例如netstat -ano或者systeminfo

解决方法：

去掉命令：$ps.WaitForExit()

执行cmd命令并获得返回结果的方法有以下两种：

**1.使用Powershell连接Exchange服务器，实现TabShell**

Powershell命令示例：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308592834949.png "1675307764636700.png")

需要注意以下问题：

需要域内主机上执行

需要fqdn，不支持IP

连接url可以选择http或https

认证方式可以选择Basic或Kerberos

**2.通过SSRF漏洞调用Exchange Powershell，实现TabShell**

这里需要通过Flask建立本地代理服务器，方法可参考之前的文章《ProxyShell利用分析3——添加用户和文件写入》

Powershell命令示例：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308594108404.png "1675307854596723.png")![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308594147882.png "1675307863896901.png")

**0x03 Python实现**

这里需要考虑两部分，一种是通过SSRF漏洞调用Exchange Powershell实现TabShell的Python实现，另一种是通过Powershell Session实现TabShell的Python实现，后者比前者需要额外考虑通信数据的编码和解码，具体细节如下：

**1.通过SSRF漏洞调用Exchange Powershell实现TabShell的Python实现**

为了分析中间的通信数据，抓取明文数据的方法可参考上一篇文章《渗透技巧——Exchange Powershell的Python实现》中的0x04，在Flask中输出中间的通信数据

关键代码示例：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308595128705.png "1675308042588075.png")

通过分析中间的通信数据，我们可以总结出以下通信过程：

(1)creationXml

初始化，构造原始数据

(2)ReceiveData

循环多次执行，返回结果中包含"RunspaceState"作为结束符

(3)执行命令;../../../../Windows/Microsoft.NET/assembly/GAC\_MSIL/Microsoft.PowerShell.Commands.Utility/v4.0\_3.0.0.0\_\_31bf3856ad364e35/Microsoft.PowerShell.Commands.Utility.dll\Invoke-Expression

在返回数据中获得CommandId

(4)读取输出结果

通过CommandId读取命令执行结果

(5)执行命令$ExecutionContext.SessionState.LanguageMode='FullLanguage'

在返回数据中获得CommandId

(6)读取输出结果

通过CommandId读取命令执行结果

(7)执行命令并获得返回结果

依次执行以下命令：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308596253541.png "1675308108212939.png")在返回数据中获得CommandId，并通过CommandId读取命令执行结果，这些命令的格式相同，发送数据的格式如下：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308597212738.png "1675308307106128.png")![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308598441002.png "1675308317506076.png")![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308599149393.png "1675308327623113.png")![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308600186272.png "1675308339243418.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308601180683.png "1675308351135827.png")

(8)执行命令并获得最终返回结果

发送数据的格式同(7)一致，执行的命令为： $Out，在返回数据中获得CommandId，并通过CommandId读取最终的命令执行结果，提取执行结果的示例代码：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308602533297.png "1675308482905142.png")

**2.通过Powershell Session实现TabShell的Python实现**

这里可以借鉴上一篇文章《渗透技巧——Exchange Powershell的Python实现》得出的经验：两者通信过程一致，只是通过Powershell Session实现TabShell的Python实现需要额外考虑通信数据的编码和解码

通信数据的编码和解码可参考上一篇文章《渗透技巧——Exchange Powershell的Python实现》中的0x03

数据的编码和解码示例代码如下：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308603895957.png "1675308542196704.png")![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308604103634.png "1675308551137246.png")完整代码的输出结果如下图

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675308605301822.png "1675308581197950.png")

**0x04 小结**

本文介绍了利用TabShell执行cmd命令并获得返回结果的方法，改进POC，分享通过Python编写脚本的细节。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?HpkKjoBc)

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