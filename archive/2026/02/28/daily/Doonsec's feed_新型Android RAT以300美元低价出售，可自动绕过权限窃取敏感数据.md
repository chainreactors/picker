---
title: 新型Android RAT以300美元低价出售，可自动绕过权限窃取敏感数据
url: https://mp.weixin.qq.com/s/xmZkbMsa6VouKrDQThwnfQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:16:44.829556
---

# 新型Android RAT以300美元低价出售，可自动绕过权限窃取敏感数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3VXZPO7ibfpwzyQ6yucDyhwxicYpuO1Mib4Mzl1Zfx6904Swiaq4UgS7Ymy7ibz2eGSfYr2H8LwXMG3vAJk3INBBzZCVVj2xUPug1Y/0?wx_fmt=jpeg)

# 新型Android RAT以300美元低价出售，可自动绕过权限窃取敏感数据

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1DflXytTJ8A3xv2nuhvgjiaEf2Fib7YPBgy1XY1rld4coyrGteLicrmnYpUVTpHv4Kg19yP6IibUxVgtWR541ic93ajw2M5bUWYgiaw/640?wx_fmt=jpeg&from=appmsg)

##

一款名为Oblivion的新型Android远程访问木马（RAT）正在引发移动安全界的严重担忧。该恶意软件在公开黑客论坛上以每月仅300美元的价格出售，能够在受害者毫无察觉的情况下悄然控制Android设备。

##

**Part01**

## ****多合一攻击工具包****

Oblivion与其他地下RAT的不同之处在于它将多种危险功能整合到一个易于部署的套件中。该木马针对Android 8至16版本，覆盖了当前几乎所有活跃使用的Android设备。攻击者无需高级编码技能——该工具包含一个点击式构建器，可处理从制作虚假应用到在受害者设备上部署的整个过程。

Certo安全分析师在审查黑客论坛上公开的卖家帖子和视频演示后确认了这一威胁。他们的审查证实，该恶意软件在公开发布前已在真实环境中测试超过四个月，在此期间未记录到任何行为检测。

这种发布前的准备程度在地下工具中并不常见，表明开发者采取了更为慎重的开发策略。

**Part02**

## ****订阅制商业模式****

该恶意软件采用订阅模式，价格从一个月300美元到终身访问2200美元不等。买家无法获得源代码，控制权牢牢掌握在卖家手中。一旦Oblivion感染设备，攻击者可以拦截包含双重认证码的短信、读取银行应用的推送通知、记录每次按键、管理文件、远程启动或卸载应用，并使用捕获的PIN自动解锁手机。这种访问级别使攻击者几乎完全掌控受感染设备。

**Part03**

## ****隐蔽远程控制：****

## ****Oblivion如何隐形运作****

Oblivion最具技术意义的功能是其隐藏VNC（HVNC）能力——一种完全在受害者视线之外运行的隐蔽远程会话。标准VNC允许远程查看和控制设备，但HVNC完全隐藏此会话，在受害者屏幕上不留任何可见痕迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2KbFia773rYv00xxx9sII2bYNzEIIEdQYgrNTNhVGbd67NbTTyf5Huxwn8yGibIby04AiavhaQlf3NaicMkUoYJnZnhUkzAqqnVqg/640?wx_fmt=jpeg&from=appmsg)

当受害者屏幕显示逼真的"系统更新中..."动画时，攻击者在其背后运行的隐藏环境中拥有设备的完全交互控制权。这个覆盖层完全可定制，可以模仿HyperOS更新、杀毒软件扫描或任何不会引起怀疑的常规加载屏幕。

**Part04**

## ****自动化感染流程****

恶意软件通过Dropper Builder生成的虚假Google Play更新提示感染设备。该工具允许攻击者自定义虚假应用名称、图标和交付屏幕。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2hh6g8HEB71icRerdwYfB6mmDYutJaiaiaEVu2k3hdp051K8hYIHthsceab1270x0HfNEyb9LtKqpITkSpsBfmd7BGXrpPYcVOjE/640?wx_fmt=jpeg&from=appmsg)

受害者会收到"需要更新"的通知，并被逐步引导启用"未知来源"安装——这种社会工程技术之所以有效，是因为它看起来完全符合常规操作。

**Part05**

## ****突破Android安全防护****

安装后，Oblivion会自动绕过Android的无障碍服务权限，无需受害者任何操作。这一功能在包括三星One UI、小米MIUI/HyperOS、OPPO ColorOS、荣耀MagicOS和一加OxygenOS在内的主要定制Android界面上均有效。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0TTyDBDrwNicvfJxuRiawfZVAib7tb6g2kTtNIO28ictAEP9ShNlGCnhJ0L7KYSSTC7CRha6mPxXEuwO9ictNWPxCoWURZ6ZkQIYQM/640?wx_fmt=jpeg&from=appmsg)

Google多年来一直在加强各Android版本的无障碍服务限制，因此能够在Android 16上绕过这些保护的工具确实是一项重大突破。

Oblivion还包含屏幕阅读器模式，可突破银行应用和加密钱包用于阻止屏幕截取的黑屏保护——这直接削弱了金融应用中最依赖的安全措施之一。

**Part06**

## ****防护建议****

为降低感染风险，用户应仅通过Google Play商店安装应用，避免从任何外部来源侧载APK文件。任何要求从Play商店外部安装更新的意外弹窗都应立即引起怀疑，因为合法的Android更新永远不会通过这种方式提供。定期检查设置>无障碍功能并移除不熟悉应用的权限是每个人都应采取的实际步骤。如果在安装外部应用后设备意外卡在加载或系统更新屏幕上，立即关机并运行安全扫描是最安全的应对措施。

**参考来源：**

New $300 Android RAT With Automated Permission Bypass and Hidden Remote Control

https://cybersecuritynews.com/new-300-android-rat/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3tSDVhn4H8MfzIKxtt4We0D52fia93Y5a2TI7y0t4j0PpiclCRBqdQCZWYrwG4B4hpaT2593sVoic8GylJKxPrgP1gyC1304Y78I/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX16d9YFd8C2ZLm5AxSaONt9eF8xcnfW9nhy3jyhoyrY28GWAnNeXJ0ojss2bj9w5V2asdI31nwVv2SUldtdhLfWuCE2l8fCzT8/640?wx_fmt=png&from=appmsg)

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