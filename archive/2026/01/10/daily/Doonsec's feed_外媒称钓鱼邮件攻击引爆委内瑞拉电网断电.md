---
title: 外媒称钓鱼邮件攻击引爆委内瑞拉电网断电
url: https://mp.weixin.qq.com/s/6ke5ijmIY7AVmy_DPEhHaw
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:35:53.906371
---

# 外媒称钓鱼邮件攻击引爆委内瑞拉电网断电

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkopm4LoGpObW5EyiauvCADSDKjh5IhIvlUAOnrUpLicy0mJcrla9KMic2wStNkR29TQ2bYNkVB5AzywQ/0?wx_fmt=jpeg)

# 外媒称钓鱼邮件攻击引爆委内瑞拉电网断电

原创

黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

以下内容仅供参考，无需太过于当真。

前些天刷到了一篇关于特朗普暗示美国在马杜罗被捕期间参与了加拉加斯大停电事件的网络攻击的报道，由一个安全媒体cybersecuritynews发布，本以为过了两天会有其他人员跟进，发现没有，然后就发了一下吧。

https://cybersecuritynews.com/trump-signals-u-s-cyber-role-in-caracas-blackout/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkopm4LoGpObW5EyiauvCADSDqdOGmjjeKp0ibTE2DxzedjgNWCetZ7jxASAY0HHfTMsFRD4HMz8WFVw/640?wx_fmt=png&from=appmsg)

以下为原文翻译。

据信，美国网络司令部及其盟军部队已在委内瑞拉电力运营商内部部署了针对电网的恶意软件。

一旦触发，该代码会悄无声息地打开断路器，使控制系统失去同步，并切断现场设备与中央控制台之间的连接。

Politico 的分析人士后来确认该恶意软件是一种模块化的电网攻击工具，这与之前针对区域公用事业公司的攻击活动有着明显的联系。

他们对网络遥测和计时数据的审查表明，一个自定义加载器通过被入侵的 VPN 网关进入了控制网络。

恶意软件由此绘制出变电站控制器图，并标记了为加拉加斯市中心供电的优先馈线。

据区域电网工程师称，最初的故障迹象表现为监控屏幕上出现短暂的滚动式下降，而不是完全崩溃。

日志显示，多条230千伏线路出现突然但有序的跳闸，随后出现大量传感器错误值，导致当地操作人员困惑。备用柴油发电机组启动时，市中心已经一片漆黑。

感染链始于向国家公用事业公司的工程师发送的鱼叉式网络钓鱼电子邮件，邮件中隐藏着一份伪造的维护报告，其中包含一个已签名的远程访问工具。

一旦用户打开该文件，加载程序就会使用窃取的VPN凭据进入控制网络，然后在管理 SCADA 工作站和历史数据库的 Windows 服务器上投放第二阶段模块。

在受感染的服务器上，恶意软件运行一个紧密的循环，查询实时断路器状态，并且只有当电网负荷保持在安全范围内时才会将关闭命令加入队列。

这种设计有助于确保打击的精准性，减少对硬件的损坏，并减缓城市恢复供电后的审查速度。它也延误了响应人员的工作，因为他们需要面对干净的日志、虚假读数以及看似自行恢复的系统。

---

然而，黑鸟经过对多家主流媒体（如Politico、Axios、Dark Reading、Cybernews等）和相关报道的深入查证，尚未找到其他可靠来源支持 cybersecuritynews.com 文章中描述的那些高度具体攻击链路细节，如鱼叉式网络钓鱼邮件、窃取VPN凭证、在SCADA工作站加载第二阶段恶意模块、队列式断路器关闭命令、注入虚假传感器读数、日志清理等。

该文章将这些细节归因于“Politico分析师”和相关报道，但实际查阅Politico等多篇原报道后

如：

https://www.politico.com/news/2026/01/07/venezuela-us-cyber-warfare-00713507

，并无此类技术分析或披露。

这些具体内容很可能为文章作者的推测性补充或综合编造，目前无公开情报、泄露报告或独立验证支持。

因此上述情况仅供参考。

当然，论钓鱼，还得是某些黑客, 国外安全公司Darktrace近日发布的攻击活动分析报告指出，在马杜罗刚被捕几个小时之后(不排除修改了时间戳的缘故)，该黑客就写了一个关于委内瑞拉总统的钓鱼诱饵去进行钓鱼。

其中包含一个名为US now deciding what's next for Venezuela.zip(美国正在决定委内瑞拉的下一步行动.zip )的压缩文件。该文件包含一个名为马杜罗将被带到纽约.exe“Maduro to be taken to New York.exe”的可执行文件和一个动态链接库（DLL）“kugou.dll”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkopm4LoGpObW5EyiauvCADSDyeLhCq5EY3l5FfZQNa3OIrknkibUxiaTTIbFttxZKEsSEaOEF0mgMulw/640?wx_fmt=png&from=appmsg)

只是里面路径的360NB和酷狗白加黑确实有点难蚌了。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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