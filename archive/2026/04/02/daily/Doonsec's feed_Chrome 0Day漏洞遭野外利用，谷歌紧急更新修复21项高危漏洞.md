---
title: Chrome 0Day漏洞遭野外利用，谷歌紧急更新修复21项高危漏洞
url: https://mp.weixin.qq.com/s/srC7Md79V2wmLMBg4Dj4CA
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:25:22.499835
---

# Chrome 0Day漏洞遭野外利用，谷歌紧急更新修复21项高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3LicgmWVOBnTo55TJR8MXkskVmvRrQ4RxibvUeVicypH4ZzpuBppU4NOiaJkk8jbZtTrmhGb8nhjcia8l7ecWrNYuXodP3m94xwrHg/0?wx_fmt=jpeg)

# Chrome 0Day漏洞遭野外利用，谷歌紧急更新修复21项高危漏洞

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0iaQQ5vLbdDK4y0ez3NapnjHfy8BVZFCeRTVgiapb32QDFIKE019ft8jp8t2JE0UHFDww4cHYhNW1TxNYRG7HjMbJib38Ioa9bv0/640?wx_fmt=png&from=appmsg)

##

谷歌已为其Chrome浏览器发布紧急安全更新，修复了一个正在被野外利用的0Day漏洞。Windows和Mac平台的稳定版已更新至146.0.7680.177/178版本，Linux平台更新至146.0.7680.177版本，预计未来数日或数周内将覆盖所有用户。

##

**Part01**

## ****漏洞技术细节****

该漏洞编号为（CVE-2026-5281），是Dawn Chrome跨平台GPU抽象层（用于实现WebGPU）中的释放后使用（use-after-free）漏洞。当程序持续引用已释放的内存时，攻击者可能借此执行任意代码或突破浏览器沙箱限制。谷歌官方确认该漏洞已被野外利用，表示"已知（CVE-2026-5281）的漏洞利用代码已在野外出现"。该漏洞由匿名研究员于2026年3月10日发现并报告。在大多数用户完成补丁更新前，漏洞技术细节将保持受限状态——这是谷歌限制漏洞复现的标准做法。

**Part02**

## ****21项安全修复补丁****

除0Day漏洞外，本次更新还包含21项安全修复，其中19项被评定为高危级别，涉及多个Chrome子系统。值得关注的已修复漏洞包括：

* （CVE-2026-5273）CSS中的释放后使用（3月18日报告）
* （CVE-2026-5272）GPU中的堆缓冲区溢出（3月11日报告）
* （CVE-2026-5274）编解码器中的整数溢出（3月1日报告）
* （CVE-2026-5275）ANGLE中的堆缓冲区溢出（3月4日报告）
* （CVE-2026-5276）WebUSB中的策略执行不足（3月4日报告）
* （CVE-2026-5278）Web MIDI中的释放后使用（3月6日报告）
* （CVE-2026-5279）V8中的对象损坏（3月8日报告）
* （CVE-2026-5280）WebCodecs中的释放后使用（3月11日报告）
* （CVE-2026-5284）Dawn中的释放后使用（3月12日报告）
* （CVE-2026-5285）WebGL中的释放后使用（3月13日报告）
* （CVE-2026-5287）PDF中的释放后使用（3月21日报告）
* （CVE-2026-5288）WebView中的释放后使用（谷歌内部报告，3月23日）
* （CVE-2026-5289）导航系统中的释放后使用（谷歌内部报告，3月25日）
* （CVE-2026-5290）合成系统中的释放后使用（谷歌内部报告，3月25日）

Dawn、WebGL、WebCodecs、Web MIDI、WebView、导航和合成系统中密集出现的释放后使用漏洞，凸显了浏览器渲染管线持续面临的内存安全问题。其中三个高危补丁由谷歌内部安全团队直接报告，表明部分漏洞是通过主动威胁狩猎而非外部披露发现的。

**Part03**

## ****更新建议****

所有运行低于146.0.7680.177（Linux）或146.0.7680.178（Windows/Mac）版本的Chrome用户均可能面临风险。鉴于（CVE-2026-5281）已确认被野外利用，企业用户和安全团队应将此更新视为关键优先级补丁。立即更新请前往菜单(⋮)→帮助→关于Google Chrome，浏览器将自动检查并应用最新更新后提示重启。通过策略管理Chrome部署的组织应即刻通过终端管理平台推送更新。

**参考来源：**

New Chrome Zero-Day Vulnerability Actively Exploited in Attacks — Patch Now

https://cybersecuritynews.com/chrome-zero-day-vulnerability-exploited/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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