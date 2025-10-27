---
title: 黑客攻击利用Microsoft服务逃避检测并分发恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492397&idx=1&sn=f400943848445bec8918963d7406cc5a&chksm=e90dc907de7a40119c3af319323eb613d24b94e267a657b2fbae6156887fa45507759172dc52&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-08
fetch_date: 2025-10-06T19:20:47.079204
---

# 黑客攻击利用Microsoft服务逃避检测并分发恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 黑客攻击利用Microsoft服务逃避检测并分发恶意软件

BaizeSec

白泽安全实验室

网络安全厂商Hunters’ Team AXON安全研究团队最近揭露了一个名为“VEILDrive”的持续性网络攻击活动，该活动利用微软的SaaS服务套件，特别是Teams、SharePoint、Quick Assist和OneDrive，来执行其攻击战术。VEILDrive通过在已被攻陷的主机环境上，部署定制恶意软件。同时在恶意软件中嵌入OneDrive基础的命令与控制（C&C）方法，展示了他们其独特的攻击技术。研究人员的分析表明，这场活动可能源自俄罗斯，并向微软和受影响的组织报告了这些发现，以协助关闭攻击者的基础架构。

VEILDrive攻击活动始于2024年8月，研究人员在对一个关键基础设施实体遭受攻击的事件响应中首次发现了这一独特的攻击活动。VEILDrive的攻击技术与典型的攻击行为明显不同，攻击者严重依赖微软的SaaS基础设施来分发鱼叉式网络钓鱼活动和存储恶意软件，这种基于云的策略使得攻击者能够避开传统监控系统的检测。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIMWjJCiav8SdZJ6VLHIKxL0RuCNV292iaemey0ZNapvlUpQqMuzibSh9xpxX4iaghf72PBomP2FBNC0Kw/640?wx_fmt=png&from=appmsg)图 1 攻击流程图

**攻击过程分析：**

**1.初始访问：**

* 攻击者利用微软Teams向目标组织中的四名员工发送消息，冒充IT团队成员，并通过Quick Assist远程工具工具请求访问员工的设备。
* 通过社会工程手段，攻击者成功诱使一名员工接受其访问请求，从而获得了对受害者计算机的初始访问权限。

**2.恶意软件部署：**

* 攻击者通过SharePoint分享了一个下载链接，该链接指向另一个组织（称为“Org B”）的SharePoint中托管的恶意文件。
* 这些文件包括一个密码保护的.zip文件，内含多个文件，其中包括一个额外的远程监控管理工具。

**3.持久性与隐藏：**

* 攻击者通过创建计划任务来尝试维持访问权限，这些任务被设置为重复执行攻击者下载的文件之一——一个名为LiteManager的远程监控管理工具。

**4.恶意软件执行：**

* 攻击者手动下载并执行了另一个.zip文件，该文件包含了主要的.jar恶意软件以及整个Java开发工具包，用于执行.jar恶意软件。

**5.网络活动：**

* 恶意.jar文件执行了多个网络活动和命令执行，包括对特定域的DNS请求和执行本地枚举命令，如获取系统信息、机器时间信息和机器的UUID。

**6.OneDrive作为C&C：**

* VEILDrive恶意软件中一个独特的部分是利用OneDrive作为C&C通道。
* 攻击者使用硬编码的凭据通过“on-behalf”身份验证访问Entra ID，从而访问特定Entra ID用户的OneDrive，滥用此访问权限进行C2通信。

**结论：**

VEILDrive攻击活动展示了攻击者如何结合简单技术和复杂的战术，以及如何利用微软服务作为攻击基础设施。这种攻击手法不仅增加了检测难度，也突显了当前检测策略的局限性，强调了对非传统攻击方法保持警惕的必要性。随着网络威胁技术的不断演变，保持对最新威胁情报的了解和采取适当的安全措施变得至关重要。

参考链接：

https://www.hunters.security/en/blog/veildrive-microsoft-services-malware-c2

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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