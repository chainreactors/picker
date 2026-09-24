---
title: 微软SharePoint曝出高危RCE漏洞，低权限账号即可远程拿下服务器
url: https://mp.weixin.qq.com/s/VmErImAG1RuOcK-Rg5hLcw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:22.261324
---

# 微软SharePoint曝出高危RCE漏洞，低权限账号即可远程拿下服务器

# 微软SharePoint曝出高危RCE漏洞，低权限账号即可远程拿下服务器

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX1Bic0Ge9gkA3ebXczksf1XCSJEJ4Wrn1JvfmTGs3MWDTdkPd74h0eoB5ibOicjZPFTm1cdQ483oMgQDoBVhErs6iavu1VyefNaT8I/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3Y7fzO6BhZ2ibeV1FKkrJTEXyiaLDu08bTPJFdrOdeeALx5K21xvOnUeDLTH3JoXpmTaKGBa8DfW1gJtibY74aN4IP1kSnoYbJoY/640?wx_fmt=png)

Part01

高危RCE漏洞影响多版SharePoint

微软已确认本地部署版SharePoint Server存在一处高危远程代码执行漏洞。经过身份认证的低权限攻击者无需用户交互，就可以通过网络在目标系统上执行任意代码。

该漏洞为代码注入类型（CVE-2026-65660），CVSS评分为8.8，影响范围包括SharePoint Server 2016、SharePoint Server 2019以及SharePoint Server订阅版。

SharePoint服务器通常存储敏感文档，且服务账号权限较高。攻击者一旦成功利用漏洞，就能在目标环境中建立据点，进而窃取凭证、横向移动、渗出数据并维持长期访问权限。

Part02

漏洞源于校验逻辑缺陷

Viettel Cyber Security的研究人员Dinh Ho Anh Khoa发现了这一漏洞。他指出，这是又一起针对SharePoint SafeControls防护机制的绕过案例。

SafeControls是SharePoint的内置防护机制，会在系统解析页面和Web部件标记时，阻止不受信任的服务端类被实例化。漏洞出在ToolPane组件处理攻击者可控的Register指令环节，这类指令的作用是将标记前缀映射到ASP.NET控件。

Viettel Cyber Security发布的技术分析显示，ToolPane的处理流程分为两步：首先将Register指令与控件标记分离，校验指令中的类型名称；随后重构这些指令，将属性值放入双引号中。

由于系统没有对嵌入的引号做安全转义，攻击者构造的恶意值可以篡改重构后的指令，原理类似注入漏洞。恶意指令会绕过已完成的安全检查，在ASP.NET解析控件之前插入额外的指令。

这种校验顺序的漏洞，让攻击者可以注册原本被拦截的危险.NET类，触发代码执行gadget。Khoa演示了一条完整利用链，涉及XamlServices.Parse()方法、ExpandedWrapper泛型、ObjectDataProvider类以及LosFormatter反序列化。

这种利用方式不会向磁盘写入传统webshell，而是直接创建内存webshell。这类攻击能减少明显的文件系统痕迹，大幅提升事件响应的难度。目前公开的研究资料中包含可直接运行的利用标记代码，大幅降低了漏洞复现的门槛。

微软表示，攻击者默认需要先通过身份认证才能利用该漏洞，且仅需低权限账号就可以完成操作。但研究人员证实，如果SharePoint部署配置允许匿名访问特定页面，攻击者可以将CVE-2026-65660与ToolPane组件的另一个认证缺陷组合利用，实现预认证RCE。

微软在2026年6月9日的更新中已经修复了这条匿名利用路径，已安装该补丁的系统不会暴露上述预认证利用链。

Part03

微软已发布官方修复补丁

微软在2026年8月11日正式发布漏洞修复补丁。各版本对应的修复后构建号分别为：SharePoint 2016是16.0.5565.1001，SharePoint 2019是16.0.10417.20198，SharePoint Server订阅版是16.0.19725.20522。

微软在安全公告中提醒用户，企业必须安装所有适用的更新包，SharePoint 2016的管理员可能需要安装公告中列出的两个更新包。

研究人员还指出，这种利用方式的底层原理同样适用于SharePoint 2013。该版本已于2023年4月停止支持，因此微软官方的受影响产品列表没有将其纳入。

因此，仍在使用SharePoint 2013的企业应当尽快完成迁移或隔离，不要等待几乎不可能发布的安全更新。

在公告发布时，微软称CVE-2026-65660尚未被公开披露，也未出现在野利用，漏洞被利用的概率较低。但随着详细技术资料公开，这一评估结论已经需要重新考量。

管理员应当立即安装补丁，限制互联网访问和匿名访问权限。同时要审计低权限账号活动，排查携带异常Web部件标记或编码XAML内容的可疑POST请求。

应急响应团队还应当检查工作进程行为、异常子进程、可疑程序集以及易失性内存内容。内存植入物几乎不会在磁盘上留下webshell文件，很难通过常规文件检测发现。

在调查过程中，如果需要重启受感染的SharePoint服务器，响应团队必须先留存IIS日志、ULS日志、Windows事件日志、PowerShell日志以及端点遥测数据。

参考来源：

Microsoft SharePoint Flaw Lets Attackers Execute Code Remotely With Low Privileges

https://cybersecuritynews.com/microsoft-sharepoint-rce-flaw/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0XsTyO4SuMuGUvEh6HBoZLXPa9xnn1UsveAZRjUSfAKwT77dFfrwAPbRgSe6l66sYOBiaFSfWMn3DL4IfDrDmexoxCYLftaleo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651346509&idx=1&sn=71e02ef8b6a2ed67fdc94aa19b152171&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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