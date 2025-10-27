---
title: 微软：VMware身份验证绕过漏洞正在被勒索团伙利用
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545166&idx=2&sn=0d296f18234549aff828cf1a6d89e7a6&chksm=c1e9bd1ff69e3409a31cb034d2641cd10c071a6ef133fe9deb7d3c3e451adaacb51387df9c49&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-01
fetch_date: 2025-10-06T18:04:58.579629
---

# 微软：VMware身份验证绕过漏洞正在被勒索团伙利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogu2R67necpnyIv2DiacMA7VXlEyvNrBJ13SfCK4y3xzALXhXpaichHSgFhLiaYeicJ9wnWBWB4k3Dicnpw/0?wx_fmt=jpeg)

# 微软：VMware身份验证绕过漏洞正在被勒索团伙利用

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogu2R67necpnyIv2DiacMA7VXFh5icVKia045nPUsmViaO6mUjP8Z3O4UGesU04IYaZkcmYDQazd1uG56A/640?wx_fmt=png&from=appmsg)

7月29日，微软发出警告指出勒索软件的犯罪团伙正在利用VMware ESXi中的一个身份验证绕过漏洞来进行攻击。该安全漏洞被追踪为CVE-2024-37085。

目前漏洞已被Storm-0506、Storm-1175、Octo Tempest和Manatee Tempest的勒索软件操作者在攻击中利用。

**1、VMware安全漏洞**

CVE-2024-37085漏洞是一个中等严重程度的安全漏洞，由微软的安全研究人员Edan Zwick、Danielle Kuznets Nohi和Meitar Pinto发现，并在6月25日发布的ESXi 8.0 U3中得到了修复。

攻击者可以利用这个漏洞将新用户添加到他们创建的“ESX管理员”组中，它允许未经授权的人获得对系统的高度控制权。

“具有足够Active Directory（AD）权限的恶意行为者可以通过在从AD中删除配置的AD管理员后重新创建配置的AD组，获得对ESXi主机的完全访问权。几个防毒墙高级设置的默认值在默认情况下是不安全的。当一台ESX主机加入Active Directory域时，AD组“ESX Admins”将自动获得Vim Admin角色。”

——Broadcom公司解释

**2、在勒索软件中被利用**

尽管发动一次攻击，需要攻击者对目标设备有较高的权限，并且需要用户的交互。但微软公司指出，一些勒索软件团伙利用这种攻击手段，来提升自己在已经加入到域的虚拟机管理程序上的权限，达到完全管理员级别。

到目前为止，该漏洞已被追踪为Storm-0506、Storm-1175、Octo Tempest和Manatee Tempest的勒索软件操作者在攻击中利用，导致Akira和Black Basta勒索软件被部署。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6xRu3pPXqugWD0pcl3vmAJoR55axcs0ozTQ46iav1GAuSYV6QJ3eeibErWtz51gJ1HKic1qS3CMYYVcA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Storm-0506恶意攻击链（微软）

例如，Storm-0506通过利用CVE-2024-37085漏洞提升权限后，在一家北美工程公司的虚拟机监控程序上部署了Black Basta勒索软件。

微软已经确定了至少三种可用于利用CVE-2024-37085漏洞的策略，包括：

1、将“ESX Admins”组添加到域并添加用户。

2、将域中的任何组重命名为“ESX Admins”，并将用户添加到该组或使用现有的组成员。

3、ESX虚拟机管理程序权限刷新（为其他组分配管理员权限不会将其从“ESX Admins”组中删除）。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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