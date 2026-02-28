---
title: 300美元买下你的手机控制权？这款新型安卓木马能在你眼皮底下“隐形操控”一切
url: https://mp.weixin.qq.com/s/1AhR8NAiWTZaOYfZIHLpAA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:54:04.144314
---

# 300美元买下你的手机控制权？这款新型安卓木马能在你眼皮底下“隐形操控”一切

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K15UkYqxeeJuV47ia7b6o8mMTiaojdu5eqk56zJchL7WvYFAPiblut5qIS4PwxxMwWETkAQ99mzRznKJX9hGpWpSPqE5ySt0Rb2Ts/0?wx_fmt=jpeg)

# 300美元买下你的手机控制权？这款新型安卓木马能在你眼皮底下“隐形操控”一切

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

> 如果你正在刷手机，屏幕突然弹出“系统更新”的提示，你的第一反应是什么？大概率会耐心等待它完成吧？安全研究人员发出警告：如果你看到这样的画面，手机可能已经被黑客完全接管了。

一款名为 Oblivion 的新型 Android 远程访问木马（RAT）正以每月 300 美元的低价在暗网论坛上出租。它的可怕之处在于，不仅能悄无声息地控制你的手机，甚至能在你亲眼看着屏幕的情况下，全程“隐形”操作一切。

传统远程控制软件，往往会让手机屏幕亮起，受害者一眼就能发现不对劲。但 Oblivion 使用了更阴险的技术——隐藏式虚拟网络计算（HVNC）。

简单来说，当木马被激活后，受害者的手机屏幕上只会显示一个看似正常的静态画面：比如“HyperOS 系统优化中，请稍候…”，或者是仿冒的杀毒软件扫描界面，进度条甚至还会慢慢走动，看起来完全无害。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0MF6M9XXZzt9J3klD9YH2vBZmJRK7WR2cMQt2t1z0ModV8hRpZcSr0RiaHs2gCCVHh4MNrdUUJOKAAxOmNw9ibnOJ6x9wgkhnB8/640?wx_fmt=png&from=appmsg)

但就在这个假界面的“掩护”下，黑客已经在另一个隐藏的虚拟空间中，对你的手机进行“实况操作”：翻看相册、读取短信验证码、打开银行 App 转账……而你，正眼睁睁看着那个假的更新界面，以为手机只是有点卡顿。

为什么它能突破 Android 15 的防线？

谷歌每年都在加强 Android 系统的安全性，尤其是在限制恶意软件获取“无障碍服务”权限方面。这个权限本是用来帮助视障人士操作手机的，却成了木马最爱的“后门”。

Oblivion 号称能绕过 Android 8 到 16 几乎所有版本的权限限制，甚至适配了主流的定制系统，如小米的 HyperOS、三星的 One UI、OPPO 的 ColorOS 等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K25tDiaG6egVJa0UicHlKDNiaUNz5pvzlQvYutP1vcicVLQXH5oVCibXsYu70ROQXfXXXTtsPN7r9UtyqYU2EGYEpRRAHlZ1APVT7zE/640?wx_fmt=png&from=appmsg)

一旦安装，它无需受害者点击确认，就能自动开启关键权限，实现以下“全套服务”：

* 拦截短信：包括 Google 验证码、银行转账确认码。
* 读取推送通知：即使是加密聊天软件或金融 App 的消息，也能被一览无余。
* 键盘记录：你输入的账号、密码、支付密码，都会被悄悄上传。
* 远程解锁：如果黑客拿到了你的锁屏 PIN 码，可以直接解锁手机，就像拿着自己的手机一样。
* 屏幕内容读取：它甚至能穿透银行和加密钱包 App 为防止截屏而设置的“黑屏保护”，通过所谓的“屏幕阅读器模式”实时读取屏幕上的敏感数字。

看似正规的“钓饵”：一个高仿的 Google Play

这款木马还附带一个“木马生成器”，攻击者可以像填表一样，轻松定制一个以假乱真的恶意 App。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1mSIfyAGgWg79twJXm1RDEj2Xm0RhoRZQTqlSQ2RC0KDZQicRDR3gBLtsZGiboK3Aq6BkVNU5kkrYkCrxFRb3NjoDoVNZ40qbtc/640?wx_fmt=png&from=appmsg)

从泄露的截图看，生成的界面与 Google Play 商店几乎一模一样。App 名称旁会显示“需要更新”的红色按钮，下方配有看似真实的下载量、评分和应用介绍，比如“性能改进”、“安全更新”等。

受害者以为自己在更新 Google Play 里的某个应用，实际上是在一步步被诱导允许“安装未知来源应用”，亲手把木马“请”进手机。

普通人该如何防范？

Oblivion 的出现，说明恶意软件正在变得更加隐蔽和专业化。对于普通用户，这几点值得留意：

1.  警惕任何“外部更新”提示：所有正规 App 的更新都应通过手机自带的应用商店完成。如果正在浏览网页或聊天时突然全屏弹窗要求更新系统或应用，最好直接关闭页面，不要点击任何按钮。

2.  检查“无障碍”列表：可以定期进入手机“设置” -> “辅助功能”（或“无障碍”），查看已下载的服务列表。如果发现有陌生或不认识的 App 被开启了权限，建议立即关闭并卸载该应用。

3.  留意手机异常：如果手机突然卡在某个看似系统更新的界面，且长时间没有变化，尝试强制重启。如果重启后恢复正常，可以马上运行安全软件进行扫描。

4. 坚持官方渠道：尽量避免通过第三方链接下载 APK 文件安装应用，这是木马进入手机最常见的途径。

手机里存着我们的照片、聊天记录、甚至银行账户，早已不只是通讯工具，更像是数字世界里的“家门”。当有人能用 300 美元就买到这把“万能钥匙”时，保持一份警惕，或许是最好的防线。

\*以上资讯改写自安全研究机构Certo发布的关于Oblivion Android木马的分析报告。本文内容已进行独立转述与整合，旨在向中文读者传递相关安全预警，如有侵权请联系删除。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

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