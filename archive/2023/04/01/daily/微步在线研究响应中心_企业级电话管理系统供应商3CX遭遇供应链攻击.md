---
title: 企业级电话管理系统供应商3CX遭遇供应链攻击
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247500859&idx=1&sn=d8ba3407a559c90c93bd9f34c2ba3511&chksm=cfcaa72ff8bd2e39654ac237eb33dd9eb0d8357d74c15a5a229037362f9acf1a0f58f17f0479&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2023-04-01
fetch_date: 2025-10-04T11:22:56.377751
---

# 企业级电话管理系统供应商3CX遭遇供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMabVVq7uDAACWlqSpaz550sRLVe5Rx4CKspIcxT8SB7tA080jU7CblMNA/0?wx_fmt=jpeg)

# 企业级电话管理系统供应商3CX遭遇供应链攻击

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMabggxYnpFRmPXP4YIicg335GmW5s2lb5jibiaEImQXzbHnA7icXL3Z8Skpwg/640?wx_fmt=png)

1

**摘要**

微步情报局监测发现，Win、macOS、Linux多平台上的一款常用工具“3CX DesktopApp”遭攻击者投毒， 3CX DesktopApp是一款流行的企业电话系统，它是一种开放式标准的软件IP电话交换机（PBX），可以在Windows、macOS或Linux上安装运行。官网介绍显示使用该产品的客户超过60万家企业，每日活跃用户超过1200万名用户，其客户包括来自金融、工业、能源、酒店、旅游、餐饮、教育等多种行业。

攻击者篡改了几个最近Windows和Mac版本的软件安装程序，以向用户计算机投递额外的信息窃取恶意软件。经过微步情报局关联分析，**相关木马特征符合Lazarus组织的特点**。

微步情报局秉承共建安全生态的原则，建议高度重视本次软件供应链投毒攻击，并根据附件IOC及时排查相关企业/部门内部是否存在相关网络威胁，保护自身安全。此次事件相关情报已自动下发，可用于威胁情报检测。

微步威胁感知平台TDP、本地威胁情报管理平台TIP、威胁情报云API、互联网安全接入服务OneDNS等均已支持对此次攻击事件和团伙的检测。**如需协助，请与我们联系：contactus@threatbook.cn**。

2

**事件概要**

|  |  |
| --- | --- |
| **攻击目标** | 全行业 |
| **攻击时间** | 2023年03月22日之前 |
| **攻击向量** | 供应链攻击 |
| **攻击复杂度** | 高 |
| **最终目的** | 窃密 |

3

**事件详情**

近日，微步情报局监测发现一款被广泛使用的语音和视频桌面客户端“3cx desktop”遭受供应链投毒事件，攻击者破坏修改程序的原始安装包，向受害者主机投递木马文件。

3CX DesktopApp在2023年3月30日发布通告，称Electron Windows应用程序的版本18.12.407和18.12.416，以及Electron Mac App的版本18.11.1213、18.12.402、18.12.407和18.12.416存在安全问题。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMablWMvaB7cBEHAf1kgibSCKyLUKLjODicicnxon6coPuKibLubdTmCZ5C4Kw/640?wx_fmt=png)

图 1 官方通报

通过微步X情报社区资产测绘平台可以发现，在互联网中多达24万公开暴露的3cx电话管理系统。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMabhKS7q8khWD3SZZN7WJxolQ9DZoPSYG1YibVqic6QrWb5EzMStutibnttQ/640?wx_fmt=png)

图 2 公开暴露的3cx管理系统

攻击者篡改了至少两个Windows版本（18.12.407和18.12.416）和两个Mac版本（18.11.1213和18.12.416）的3CX DesktopApp安装程序文件。这些安装程序文件包含了干净的应用程序和恶意的DLL文件。该应用程序被用于加载这些恶意DLL文件，然后在计算机上安装窃取信息的恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMabic9DcneYS0SnCibkhVZ3nchH5tB17DOdVgg4Se3y2wqpViaj1sCl3tVkg/640?wx_fmt=png)

图 3 Winodws端证书信息

在Windows中，攻击者在.msi文件中携带恶意代码，在代码执行后等待7天，然后从Github下载后续攻击载荷并与C2通信。.msi程序将释放文件ffmpeg.dll和d3dcompiler\_47.dll。

ffmpeg.dll文件通过查找数据FEEDFACE并使用 RC4 密钥 ( 3jB(2bsG#@c7 ) 进行解密，从d3dcompiler\_47.dll中提取后续攻击载荷，将提取出的攻击载荷加载到内存执行。在此处，攻击者所使用的加载器代码同样为APPJEUS加载器代码，而APPJEUS则疑似与朝鲜组织Lazarus相关联。完成后，设置7天定时器，在休眠7天后与C2连接下载后续载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMabPXyL34CUgIOqd56PoMRmcQFB9KGUtO0YzF0oRF7lG2Te9L4iawBwzZw/640?wx_fmt=png)

图 4 ffmpeg.dll加载d3dcompiler 47.dll

后续文件从Github下载，此存储库由 GitHub ID 120072117于 2022 年 12 月 8 日创建，最近更新于 2023 年 3 月 16 日。后续攻击载荷会获取主机信息、域、操作系统版本以及浏览器Brave、Chrome、Edge、Firefox的浏览历史记录，并将其发送回C2地址。目前该Github地址已被删除。

在macOS端，安装包以类似的方式遭到破坏，一个名为libffmpeg.dylib的文件遭到破坏修改，攻击者使用异或密钥0X7A解密Shellcode，并通过C2地址尝试下载后续攻击载荷，不过截至分析时，未能获取到后续载荷，从Windwos端来看，后续应为同样为信息窃取器。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMabpBYp0Dz8nvQldYA9QNUqDvv2O2u2ezfuq4v8yWab5m0RTxXN9IaIsA/640?wx_fmt=png)

图 5 解密

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKKIwzXUMSTRxJbmEAibibMabeicoEX8FZNQdYRPZy7lul4BtseKaYgGobmcHlib7VkibWI33iamG5Wv6wA/640?wx_fmt=png)

图 6 下载payload

4

**处置建议**

1.根据威胁情报，排查网络中安装有特定版本软件的主机，逐台清理。

2.微步在线云端已更新相关情报，建议更新TDP情报至最新版本，并全面覆盖贵单位网络区域。关注含有标签Lazarus的告警。

回复关键词“**3C**”获取相关IOC。

**---End---**
点击下方，关注我们
第一时间获取最新的威胁情报

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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