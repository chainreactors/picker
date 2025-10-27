---
title: 【技术原创】渗透技巧——远程访问Exchange Powershell
url: https://www.4hou.com/posts/zlj2
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-29
fetch_date: 2025-10-04T10:58:18.889224
---

# 【技术原创】渗透技巧——远程访问Exchange Powershell

【技术原创】渗透技巧——远程访问Exchange Powershell - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】渗透技巧——远程访问Exchange Powershell

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-03-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)131008

收藏

导语：Exchange Powershell基于PowerShell Remoting，通常需要在域内主机上访问Exchange Server的80端口，限制较多。本文介绍一种不依赖域内主机发起连接的实现方法，增加适用范围。

**0x00 前言**

Exchange Powershell基于PowerShell Remoting，通常需要在域内主机上访问Exchange Server的80端口，限制较多。本文介绍一种不依赖域内主机发起连接的实现方法，增加适用范围。

注：

该方法在CVE-2022–41040中被修复，修复位置：C:\Program Files\Microsoft\Exchange Server\V15\Bin\Microsoft.Exchange.HttpProxy.Common.dll中的RemoveExplicitLogonFromUrlAbsoluteUri(string absoluteUri, string explicitLogonAddress)，如下图

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869568202619.png "1669864599270275.png")

**0x01 简介**

本文将要介绍以下内容：

实现思路

实现细节

**0x02 实现思路**

常规用法下，使用Exchange Powershell需要注意以下问题：

所有域用户都可以连接Exchange PowerShell

需要在域内主机上发起连接

连接地址需要使用FQDN，不支持IP

常规用法无法在域外发起连接，而我们知道，通过ProxyShell可以从域外发起连接，利用SSRF执行Exchange Powershell

更进一步，在打了ProxyShell的补丁后，支持NTLM认证的SSRF没有取消，我们可以通过NTLM认证再次访问Exchange Powershell

**0x03 实现细节**

在代码实现上，我们可以加入NTLM认证传入凭据，示例代码：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869569586433.png "1669864717256342.png")

在执行Exchange Powershell命令时，我们可以选择pypsrp或者Flask，具体细节可参考之前的文章《ProxyShell利用分析2——CVE-2021-34523》和《ProxyShell利用分析3——添加用户和文件写入》

pypsrp或者Flask都是通过建立一个web代理，过滤修改通信数据实现命令执行

为了增加代码的适用范围，这里选择另外一种实现方法：模拟Exchange Powershell的正常通信数据，实现命令执行

可供参考的代码：https://gist.github.com/rskvp93/4e353e709c340cb18185f82dbec30e58

代码使用了Python2，实现了ProxyShell的利用

基于这个代码，改写成支持Python3，功能为通过NTLM认证访问Exchange Powershell执行命令，具体需要注意的细节如下：

**1.Python2和Python3在格式化字符存在差异**

(1)

Python2下可用的代码：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869570136018.png "1669864771155868.png")

以上代码在Python3下使用时，需要将Str转为bytes，并且为了避免不可见字符解析的问题，代码结构做了重新设计，Python3可用的代码：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869571877577.png "1669868450134905.png")

(2)

Python2下可用的代码：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869572542963.png "1669868511668190.png")以上代码在Python3下使用时，需要将Str转为bytes，Python3可用的示例代码：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869573111937.png "1669868551369177.png")

(3)

Python2下可用的代码：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869575129665.png "1669868670471728.png")![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869576805444.png "1669868682396213.png")

以上代码在Python3下使用时，需要将Str转为bytes，为了避免不可见字符解析的问题，这里不能使用.decode('utf-8')，改为使用.decode('ISO-8859-1')

Python3可用的示例代码：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869577513162.png "1669868728109333.png")

**2.支持Exchange Powershell命令的XML文件格式**

XML文件格式示例1：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869579143449.png "1669869067168657.png")

对应执行的命令为：Get-RoleGroupMember "Organization Management"

XML文件格式示例2：

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869580186354.png "1669869123241125.png")

对应执行的命令为：Get-Mailbox -Identity administrator

通过格式分析，可得出以下结论：

**(1)属性Cmd对应命令名称**

例如：

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869581550601.png "1669869180144518.png")

**(2)传入的命令参数需要注意格式**

如果只传入1个参数，对应的格式为：

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869582455256.png "1669869272271222.png")如果传入2个参数，对应的格式为：

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869582107371.png "1669869311678805.png")

如果传入4个参数，对应的格式为：

![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869583191987.png "1669869344963542.png")为此，我们可以使用以下代码实现参数填充：

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869584189294.png "1669869378116694.png")构造XML文件格式的实现代码：

![27.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869585595080.png "1669869427202314.png")![28.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869587807112.png "1669869498906193.png")![29.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869588172961.png "1669869515172373.png")结合以上细节后，我们可以得出最终的实现代码，代码执行结果如下图

![Unknown.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221201/1669869589464827.png "1669869551899304.png")

**0x04 小结**

本文介绍了远程访问Exchange Powershell的实现方法，优点是不依赖于域内主机上发起连接，该方法在CVE-2022–41040中被修复。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?TtswvhkD)

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

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)...