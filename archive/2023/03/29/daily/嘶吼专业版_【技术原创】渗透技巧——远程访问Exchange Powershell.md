---
title: 【技术原创】渗透技巧——远程访问Exchange Powershell
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247559326&idx=1&sn=2a66550f93fd815a9c13b6b785c8756e&chksm=e91438a4de63b1b26f0349e1ab630eac81ae1c67077e3500bb128163be2b325c60e314529caa&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-03-29
fetch_date: 2025-10-04T11:02:19.197628
---

# 【技术原创】渗透技巧——远程访问Exchange Powershell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvfEnUDnhS4XT2IwwkL6DXibdfGa3euqKeZjaw6lKVREVPKDNFIrw9nnA/0?wx_fmt=jpeg)

# 【技术原创】渗透技巧——远程访问Exchange Powershell

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)0x00 前言

Exchange Powershell基于PowerShell Remoting，通常需要在域内主机上访问Exchange Server的80端口，限制较多。本文介绍一种不依赖域内主机发起连接的实现方法，增加适用范围。

注：

该方法在CVE-2022–41040中被修复，修复位置：C:\Program Files\Microsoft\Exchange Server\V15\Bin\Microsoft.Exchange.HttpProxy.Common.dll中的RemoveExplicitLogonFromUrlAbsoluteUri(string absoluteUri, string explicitLogonAddress)，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvE4IqxmbQ8ghEHibwhfT1UIgIMZRm6Z4N5tRVBfsiakUAaGO4jwYv2l2g/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)0x01 简介

本文将要介绍以下内容：

实现思路

实现细节

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)0x02 实现思路

常规用法下，使用Exchange Powershell需要注意以下问题：

所有域用户都可以连接Exchange PowerShell

需要在域内主机上发起连接

连接地址需要使用FQDN，不支持IP

常规用法无法在域外发起连接，而我们知道，通过ProxyShell可以从域外发起连接，利用SSRF执行Exchange Powershell

更进一步，在打了ProxyShell的补丁后，支持NTLM认证的SSRF没有取消，我们可以通过NTLM认证再次访问Exchange Powershell

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)0x03 实现细节

在代码实现上，我们可以加入NTLM认证传入凭据，示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvpZuquO9PhLGEYeC2aV6D3nKpnG7a6j4LDcMnIMVXdSX43ZtCS3HTGA/640?wx_fmt=png)

在执行Exchange Powershell命令时，我们可以选择pypsrp或者Flask，具体细节可参考之前的文章《ProxyShell利用分析2——CVE-2021-34523》和《ProxyShell利用分析3——添加用户和文件写入》

pypsrp或者Flask都是通过建立一个web代理，过滤修改通信数据实现命令执行

为了增加代码的适用范围，这里选择另外一种实现方法：模拟Exchange Powershell的正常通信数据，实现命令执行

可供参考的代码：https://gist.github.com/rskvp93/4e353e709c340cb18185f82dbec30e58

代码使用了Python2，实现了ProxyShell的利用

基于这个代码，改写成支持Python3，功能为通过NTLM认证访问Exchange Powershell执行命令，具体需要注意的细节如下：

**1.Python2和Python3在格式化字符存在差异**

(1)

Python2下可用的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvcHWbTry2ppfXTxLYgal4MVicqaInlaxtmoibFOc0h16mMh1WCT6a9c8Q/640?wx_fmt=png)

以上代码在Python3下使用时，需要将Str转为bytes，并且为了避免不可见字符解析的问题，代码结构做了重新设计，Python3可用的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvOl1UD7p79TP4ibm6iawOVIiaNYUBVBicGeAJAr9mw0mt0xLCeRSLKIKQWQ/640?wx_fmt=png)

(2)

Python2下可用的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvyCvuI3xctEYMkqtJoPdwXJXBXqibCaSicNV06GlgJov0VZgNgia8ia4n2g/640?wx_fmt=png)

以上代码在Python3下使用时，需要将Str转为bytes，Python3可用的示例代码：

(3)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvw7ZxfumZBlIdwzq9GzHA4fBE2MzsuUyrZaXk4jDGUib8Qk8rQl4YHfA/640?wx_fmt=png)

Python2下可用的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvKqWWzZfLFjxjmlib0ibXoI7l9PdaNhsb8vQ8R64yDh1ofDD6icDYCjK9A/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvNhOh5UboWeZ3WlaWDk4Ecnmdgic2xYmneXcOHYUoYLcvkYic8icKBKfRA/640?wx_fmt=png "1669868682396213.png")

以上代码在Python3下使用时，需要将Str转为bytes，为了避免不可见字符解析的问题，这里不能使用.decode('utf-8')，改为使用.decode('ISO-8859-1')

Python3可用的示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvTHxxosMsiao3wB8UEdM9ED4t7jiaPuCfDSvIaBgXJuaDmfWBQ8JAfWIA/640?wx_fmt=png)

**2.支持Exchange Powershell命令的XML文件格式**

XML文件格式示例1：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvoXru2uInIVUxwGBGNHCLKlsvNcly1kWoUvz02g0Skv1got1PDIRxnQ/640?wx_fmt=png)

对应执行的命令为：Get-RoleGroupMember "Organization Management"

XML文件格式示例2：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvCbkDJCVicjhMez7jj7CCA4V17ct4RWgg4HdctENYXV1yWibUlT26KRibg/640?wx_fmt=png)

对应执行的命令为：Get-Mailbox -Identity administrator

通过格式分析，可得出以下结论：

**(1)属性Cmd对应命令名称**

例如：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvicOC0PanPQicKwFN4WQibvH0YZSHNh0ia6BHBL3KPmElOPLYVtgrvTD06Q/640?wx_fmt=png)

**(2)传入的命令参数需要注意格式**

如果只传入1个参数，对应的格式为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvuBlYFjmfiaoCmHk66fxcTDX9DCxk8kVuiaOeoGQWKbe8Tmial1K5nxqAA/640?wx_fmt=png)

如果只传入2个参数，对应的格式为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvw1ujpEA5ia1kiaCRWp1ZChalic6yPUegpmHcV591kJyIK5syk2MdaJWpw/640?wx_fmt=png)

如果传入4个参数，对应的格式为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvkqIRlPMPibuZszVOxpF33WLJZslhCgfmceOQ6ZLs8UbHIkicYVWMp5Rw/640?wx_fmt=png)

为此，我们可以使用以下代码实现参数填充：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvSVWel1P5EQNhYFrGR86QlpjzRxjg50bGNcpF0LAW4gJCsdsUfffdow/640?wx_fmt=png)

构造XML文件格式的实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv8MPN1JOmPYBqQzzGul6W75ooo4fnfQ0OEjU8fwz6aYH29ia145UdAyA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvTHkGict1eGuAajMicXia9CDrS4I9lqoG7nrHAkfp2KWYjrPmI8IFeCG6A/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvUSqiczz9Dawtm2IOPd7MyEJRicBWlkNhibpN3er5LHaR7pqiaTWLhm0sWQ/640?wx_fmt=png)

结合以上细节后，我们可以得出最终的实现代码，代码执行结果如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvYPVoiaGLqkrqW9NXBbwbmIdnHNPXWCRoMOic9uWP3VSAoFZeV6JeibK6Q/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)0x04 小结

本文介绍了远程访问Exchange Powershell的实现方法，优点是不依赖于域内主机上发起连接，该方法在CVE-2022–41040中被修复。

相关阅读：

[【技术原创】渗透技巧——从VMware ESXI横向移动到Windows虚拟机](http://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247550739&idx=1&sn=15440c91b391911a2a5771f3c05b6e80&chksm=e915d729de625e3f789159d490cf9693f5decd7e3f0fb785f864b8f82913463042c918f5c462&scene=21#wechat_redirect)

[【技术原创】渗透技巧——通过WSUS进行横向移动](http://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556226&idx=1&sn=0b1bda048a3ea962ed756319e96ff939&chksm=e915ccb8de6245aeb73f4e56702d49d5047b9075dc27c2cdf058bed176a582a0b0528c4ff64f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvJmGFdyUibsJopeo2ZRcYqYic0sicaHqrZukuRugoJ087N3yPRXFG5vclw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvOibzWMJ2wJbtvvGOosfkYWgJaYJSU6dYCJahY9lUemYzc0dQ1lhGKuw/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过