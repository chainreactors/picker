---
title: App漏洞可远程解锁启动汽车，影响现代、捷尼赛思汽车
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247533101&idx=5&sn=9ba36bcd6e768076a0dda7474e9abc0f&chksm=c1e9ce7cf69e476a093b7f34c83e5bc04f50c296eb2b3080f5611264a9390779c8a2d5363641&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-12-06
fetch_date: 2025-10-04T00:35:13.326042
---

# App漏洞可远程解锁启动汽车，影响现代、捷尼赛思汽车

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtvgp07sL5Dib5vjUviapNhmicjOPGYJh9OgvFmIWbxfic2nUr7SicyBI5WzHOjicZHr7hOvKFN9gE8tz3g/0?wx_fmt=jpeg)

# App漏洞可远程解锁启动汽车，影响现代、捷尼赛思汽车

关键基础设施安全应急响应中心

汽车APP漏洞可远程解锁启动汽车，影响2012年之后部分型号汽车。

Yuga Labs安全研究人员发现了现代汽车APP中的安全漏洞，并在丰田、宏达、尼桑、英菲尼迪等汽车制造商使用的SiriusXM "smart vehicle"平台中发现了类似的攻击面。截止目前，安全研究人员尚未公开漏洞的技术细节，但在推特分享了相关的信息。

**现代汽车问题**

现代汽车和捷尼赛思汽车的移动APP名为MyHyundai和MyGenesis，允许认证用户启动、停止、锁定、解锁其汽车。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgnuMDpCdyfYInummcBvAr25o8ibKgeOthkBsnRTvc4DTv5f1uWictXzbQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 MyHyundai app接口

在拦截者2个APP生成的流量经过分析后，研究人员发现可以从中提取出API调用用于进一步分析。

研究人员发现，其所有者的验证是基于用户的电子邮件地址的，而电子邮件地址包含在POST请求的json中。

而且MyHyundai APP在注册时并不需要邮件确认，只使用用户注册时的邮件地址和额外的控制字符来创建账户。

最后，发送JSON token中包含欺骗地址、JSON body中包含受害者地址的HTTP请求到Hyundai终端，就可以成功绕过有效性验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgVpU0wrrj0hsgoEQrHqNrQNvoY1ibhrVJl1I4fOhnLpPaBdQK7k8QrDw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 伪造的HTTP请求的响应

为验证是否可以攻击汽车，研究人员尝试解锁了一辆现代汽车。几秒钟后，被攻击的汽车成功解锁了。

在现实攻击中需要多个步骤，研究人员将攻击过程封装进了一个Python脚本，只需输入目标邮件地址，就可以执行所有命令，并成功接管受害者汽车。

**SiriusXM问题**

SiriusXM 是一家车载服务提供商，有超过15个汽车厂商使用，有超过1200万连网汽车使用该服务。

Yuga Labs 安全研究人员发现宝马、本田、英菲尼迪、尼桑、丰田、雷克萨斯、路虎等都汽车厂商都使用SiriusXM 技术来实现远程车辆管理功能。

研究人员拦截了尼桑APP的网络流量，发现只需要知道目标车辆的ID（VID）就能发送伪造的HTTP请求到车辆。

对非授权的请求的响应中包含目标车辆名、手机号码、地址和车辆详细信息。

考虑到根据VIN很容易获取，比如在车上、卖车网站上都有。除了信息泄露外，这些请求也可以在其他汽车上执行命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29KPo3UHwFvEebMyQHZIicKgP6qppXcCWgSzvEiaF8Dib2u78TIYPVwNJZLxSUdumkI98TuZTOa4IXNQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 Python脚本输入VIN提取数据

BleepingComputer也联系了Hyundai和SiriusXM来确定漏洞是否被利用用于攻击现实用户。厂商回应称截止目前未发现有现实用户被攻击。

Yuga Labs研究人员已经通知了Hyundai和SiriusXM的漏洞和相关风险。目前，厂商也已经修复了相关的漏洞。

研究人员Sam Curry确认漏洞影响2015年之后使用SiriusXM的汽车品牌。攻击者利用该漏洞在只需要知道VIN号的请求下可以在SiriusXM平台上实现远程追踪、车辆锁定、解锁、启动、停止、开启车前灯。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/hyundai-app-bugs-allowed-hackers-to-remotely-unlock-start-cars/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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