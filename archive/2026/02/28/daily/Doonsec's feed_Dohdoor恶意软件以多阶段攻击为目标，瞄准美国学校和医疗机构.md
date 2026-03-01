---
title: Dohdoor恶意软件以多阶段攻击为目标，瞄准美国学校和医疗机构
url: https://mp.weixin.qq.com/s/jWzQd37AoUsAP68gjVHpfA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:21:25.735856
---

# Dohdoor恶意软件以多阶段攻击为目标，瞄准美国学校和医疗机构

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7ObbC0J4kHPJRXWNEYoHIdBZ09nPPjK4ZbHibrZzuhA3RSR4BNE5qfaHOwPfDiaRYle5ykcQfRgVFVjQY3wAmJiaMBiaXRfw6GHDGY/0?wx_fmt=jpeg)

# Dohdoor恶意软件以多阶段攻击为目标，瞄准美国学校和医疗机构

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一种名为 Dohdoor 的新型后门正在通过隐蔽的多阶段攻击链，积极攻击美国的学校和医疗保健机构。

UAT-10027 专注于美国的教育和医疗保健机构，这些行业处理高度敏感的个人和医疗数据，但通常安全预算有限且系统陈旧。

Cisco Talos 评估认为，UAT-10027 可能与朝鲜有关联，但置信度较低，因为其工具和技术与 Lazarus Group存在重叠。

攻击者的最终目标是利用 Dohdoor 建立持久的后门访问权限，然后投放后续有效载荷，很可能包括 Cobalt Strike 信标，以进行更深层次的网络入侵和横向移动。

思科 Talos追踪到的这场攻击活动编号为 UAT-10027 ，至少从 2025 年 12 月开始就一直在进行，它滥用 DNS-over-HTTPS (DoH) 和信誉良好的云基础设施来隐藏其命令和控制流量。

然而，受害者的特征与 Lazarus 通常关注的加密货币和防御策略并不完全吻合。重叠之处包括自定义解密逻辑、DLL 侧加载、进程空心化、基于 DoH 的 C2 通信以及 EDR 绕过例程，这些都曾在 Lazarus 早期的相关工具（例如 Lazarloader）中出现过。

## **Dohdoor恶意软件**

据信，初始访问依赖于社会工程，通过网络钓鱼电子邮件传递或触发 PowerShell 脚本，该脚本充当下载器。

遥测和开源情报显示，攻击者使用 PowerShell 调用 curl.exe 并传递编码后的 URL，从远程暂存服务器获取扩展名为“.bat”或“.cmd”的恶意批处理脚本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MEk40g2y1cly8uu1Y9hcGnEjvMmiaJ2azqIyQk3whV3Ds4veNPuqPFHZsjRibiarPfp5IXxg0lmrOZ2hfjicPPZPnDg8Q4qZvcZOs/640?wx_fmt=jpeg)

第二阶段是一个 Windows 批处理脚本，它会在 C:\ProgramData 或 C:\Users\Public 下准备一个隐藏的工作目录，然后通过特定的 URL 路径从 C2 下载一个恶意 DLL，并将其重命名以模仿合法的 Windows DLL，例如 propsys.dll 或 batmeter.dll。

然后，该脚本会将受信任的 Windows 二进制文件（例如 Fondue.exe、mblctr.exe 或 ScreenClippingHost.exe）复制到该文件夹中，并通过这些可执行文件侧载恶意 DLL，然后清除运行历史记录、清除剪贴板并删除自身以清除证据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NfXrxI1I2Fun0yWZ5hdwpZwVRH9sU9ruPQxMYrPaMYTVrq1YKGyO1DPCDqvHk1wlV0F5EVIq1yDt06O5RkBvIfuSaib1wjrnUk/640?wx_fmt=jpeg)

一旦 Dohdoor 加载完毕，它就会建立后门访问权限，并将下一阶段的有效载荷直接拉入内存，这很可能是一个Cobalt Strike Beacon 有效载荷，它会在合法的 Windows 进程中反射运行，以逃避传统的检测方法。

该恶意软件随后利用进程空洞技术攻击硬编码的 Windows 二进制文件（例如 OpenWith.exe、wksprt.exe、ImagingDevices.exe 和 wab.exe），以受信任进程的伪装来执行解密后的有效载荷。

Dohdoor 的突出特点是使用 DNS-over-HTTPS 来解析 C2 基础设施，同时融入正常的网络流量。

该恶意软件不会发送明文 DNS 查询，而是构造加密的 HTTPS 请求到 Cloudflare 的 DoH 服务（端口 443），使用 User-Agent: insomnia/11.3.0 和 Accept: application/dns-json 等标头，并通过查找“Answer”和“data”字段来解析 JSON 响应，从而提取 IP 地址。

解析 C2 IP 后，Dohdoor 使用 GET 请求建立 HTTPS 隧道，模拟 curl 流量（例如，User-Agent: curl/7.88 或 curl/7.83.1）和特定的 URL 路径来获取加密的有效负载。

UAT-10027 进一步将其基础设施隐藏在Cloudflare 边缘网络之后，并使用诸如“MswInSofTUpDloAd”和“DEEPinSPeCTioNsyStEM”之类的欺骗性子域名，这些子域名位于混合大小写的顶级域名（如“.OnLiNe”、“.DeSigN”和“.SoFTWARE”）上，以模仿更新或安全系统，并阻挠简单的基于字符串的阻止。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7M6Qk584wCxTJQFX4lbicaVHjbBicMMvric4Rc4ItV2ogW8RbMG5eV5Qqqj0XMEfgvWITdPJGNKtwqVp0KFQZLA4hwY8VkbJzzU9A/640?wx_fmt=jpeg)

这种解密方式，包括使用常量 0x26，与 Lazarloader 中记录的技术非常相似，进一步证实了与朝鲜操作员的联系。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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