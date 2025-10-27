---
title: PTZ摄像头曝严重零日漏洞，黑客利用漏洞发起攻击
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458580008&idx=2&sn=477b16b48e296bf88d2ad7ec6b81dfbf&chksm=b18dc4a286fa4db434ee0d7e082ead04be9d5fa649871858014538e187deedb7554777709cf8&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-02
fetch_date: 2025-10-06T19:17:34.959952
---

# PTZ摄像头曝严重零日漏洞，黑客利用漏洞发起攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GW3D0KDSQ7AJI7j4jAibbVHPH5JL8fuUMibv1cS6pfalmibblG71b3aYdzg8m4mle4FCBh5jIUMVE1g/0?wx_fmt=jpeg)

# PTZ摄像头曝严重零日漏洞，黑客利用漏洞发起攻击

看雪学苑

看雪学苑

近日，安全研究机构GreyNoise披露，PTZOptics品牌的PTZ摄像头存在两个严重的零日漏洞，编号为CVE-2024-8956和CVE-2024-8957，黑客正在积极利用这些漏洞发起网络攻击。**PTZ摄像头**因其集成的平移(Pan)、倾斜(Tilt)和变焦(Zoom)功能，**在工业、医疗保健、商务会议、政府和法庭等多种环境中被广泛使用。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GW3D0KDSQ7AJI7j4jAibbVHsWWfupaaMFX0JUxMYKGN19iaICOqOfbA6ZQMa4xBo0ywibibj8Ob0BkrQ/640?wx_fmt=png&from=appmsg)

**漏洞详情**

CVE-2024-8956是“lighthttpd”Web服务器中的一个弱身份验证问题，未经授权的用户可以在没有授权标头的情况下访问CGI API，这可能导致用户名、MD5密码哈希值和网络配置的泄露。CVE-2024-8957则是由“ntp.conf”中的输入清理不足引起的，攻击者可以通过特制的有效负载插入用于远程代码执行的命令，完全控制摄像头或导致视频源中断。

**影响与风险**

受影响的是基于Hisilicon Hi3516A V600 SoC V60、V61和V63的支持NDI的摄像头，运行早于6.3.40的VHD PTZ相机固件版本。这些漏洞可能导致摄像头被完全接管、机器人感染、转向连接在同一网络上的其他设备或视频源中断。

**修复与建议**

PTZOptics已于9月17日发布了安全更新，但部分型号如PT20X-NDI-G2和PT12X-NDI-G2因已达到使用寿命而未获得固件更新。对于这些型号的用户，建议尽快升级到最新的固件版本，并持续监控网络活动以检测任何异常，同时采取额外的安全措施，如更改默认凭据、限制远程访问和强化身份验证机制，以减少潜在的风险。

资讯来源：bleepingcomputer

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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