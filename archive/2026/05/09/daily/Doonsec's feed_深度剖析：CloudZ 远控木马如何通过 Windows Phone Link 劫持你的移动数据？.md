---
title: 深度剖析：CloudZ 远控木马如何通过 Windows Phone Link 劫持你的移动数据？
url: https://mp.weixin.qq.com/s/vVXx1ZRNWgH5mRl3DNU8NA
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:35:03.631817
---

# 深度剖析：CloudZ 远控木马如何通过 Windows Phone Link 劫持你的移动数据？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bHeteOibsicdgrXibeMRoia6DLHCSh599Vr0rHUxGMJx5Lic2jyvV6zmUf5bcUJN4AnJdypuR7c7fbNpThuOopgkdniaq6atpeuzFMat2oYgsEvicw/0?wx_fmt=jpeg)

# 深度剖析：CloudZ 远控木马如何通过 Windows Phone Link 劫持你的移动数据？

原创

Kit Chung
Kit Chung

安全圈动向

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bHeteOibsicdhtkS5KAmA476deicKsetPXkwC6DDOLoTWKiczWEucBDMegKk4k40h9iaLgVtRtBsVhG1wq41XOegFHMKs2xN6VibeTqhpRmiaicuX5k/640?wx_fmt=png&from=appmsg)

大家好，平时为了办公方便，咱们不少人都会用 Windows 自带的 **“手机连接”（Phone Link）** 功能吧？电脑上直接回短信、接电话、看通知，确实爽歪歪。但就在最近，安全圈曝出了一个相当“阴损”的新招数：黑客盯上这条跨设备同步的桥梁了！

Cisco Talos 的安全研究员最近披露了一个名为 **CloudZ** 的远程访问木马（RAT），它配合一个此前从未露面的插件 **Pheno**，正在精准“打劫”用户的凭据和短信验证码（OTP）。最骚的操作是：**你的手机压根没中毒，黑客只要搞定你的电脑，就能远程同步读取你的所有短信。**

今天我就带大家深入扒一扒这个攻击链路，看看这帮家伙是怎么在 Windows 系统里“隔山打牛”的。

---

## 一、 核心原理：为什么攻击 Windows 就能拿到手机短信？

咱们搞技术的都知道，Phone Link 的本质是 PC 和手机之间建立了一个受信任的数据通道。为了实现实时同步，Windows 会把手机端的短信、通知、甚至通话记录，存储在本地的一个 **SQLite 数据库** 中。

黑客的逻辑非常直接：与其费劲巴拉去攻破防护越来越严的 iOS 或架构碎片化的 Android 手机，不如直接去翻你电脑里的数据库。只要你的电脑开了 Phone Link，你的 2FA 验证码在黑客面前就是全透明的。

---

## 二、 攻击全链路解析：从伪装到持久化

这次攻击的手段非常老辣，整个流程环环相扣，咱们来看下它的技术路径：

### 1. 初始入侵与“李代桃僵”

攻击者首先会抛出一个伪装成 `ConnectWise ScreenConnect`（一款合法的远程桌面工具）的可执行文件。这招走的是社会工程学路线，专门坑那些对远程维护工具习以为常的运维或技术人员。

### 2. .NET Loader 的环境检测

初级 Dropper 运行后，会下载并运行一个 **.NET 加载器**。这个加载器非常鸡贼，它不会直接释放木马，而是先做一轮**硬件和环境检查**，确认自己没跑在安全专家的虚拟机或沙箱里。一旦确认环境“安全”，它就会通过嵌入的 PowerShell 脚本设置一个**计划任务（Scheduled Task）**，实现持久化驻留。即使你重启电脑，它也会自动复活。

### 3. 模块化的 CloudZ 远控主体

CloudZ 是一款用 C# 编写的模块化木马。它通过加密的 Socket 连接与 C2 服务器通信，所有指令都经过了 **Base64 编码**。它的设计非常灵活，可以根据黑客的需要，随时加载或卸载不同的插件模块。

---

## 三、 技术戏肉：Pheno 插件如何“劫持”Phone Link？

整场攻击最核心的环节就在这个名为 **Pheno** 的插件上。它是专门为 Windows Phone Link 量身定制的“数据提取器”。

> **实现流程：**
>
> 1. **侦察：** 扫描系统进程，确认 `PhoneExperienceHost.exe` 是否正在运行。
> 2. **定位与读取：** 寻找存储同步数据的 SQLite 数据库文件路径。
> 3. **暂存：** 将提取到的短信、联系人和 Recon 日志写入到特定的本地暂存文件夹（例如 `C:\ProgramData\Microsoft\whealth\`）。
> 4. **外泄：** CloudZ 主体读取该文件夹下的内容，打包回传给 C2 服务器。

这意味着，黑客可以实时监控你的短信验证码，从而轻松绕过你账号的二次验证（2FA）。

---

## 四、 CloudZ RAT 指令集一览

为了让大家更直观地感受这个木马的功能，我整理了它支持的部分核心指令：

| 指令 | 功能描述 |
| --- | --- |
| `GetWidgetLog` | **重头戏：** 提取 Phone Link 的侦察日志和同步数据。 |
| `RunShell` | 执行任意 Shell 命令，完全控制你的终端。 |
| `BrowserSearch` | 窃取浏览器存储的敏感数据和搜索历史。 |
| `savePlugin` | 将新插件保存到 `\whealth\` 目录，实现功能无限扩展。 |
| `rec` | 开启屏幕录制，你的一举一动都在黑客眼里。 |

---

## 五、 避坑指南：IT 人该如何防范？

看完这个案例，我最大的感触是：**便捷性往往是安全的第一杀手。** 这种“不碰手机却能偷手机数据”的思路，防御起来确实头疼。我有几点建议：

* **权限最小化：**

  如果不是极其依赖电脑发短信，建议在 Windows 设置里关闭“手机连接”的短信同步功能。
* **关注异常目录：**

  盯紧 `C:\ProgramData\` 下的奇怪文件夹，特别是像 `whealth` 这种起个正经名字却存放加密文件的。
* **防御 .NET 威胁：**

  现在的黑客越来越爱用 .NET，因为它能完美调用 Windows 系统 API 且易于混淆。公司内部需要加强对未授权 .NET 程序运行的审计。

最后，大家对这种“跨端劫持”的思路怎么看？你在实际工作中还见过哪些奇葩的 2FA 绕过方式？咱们评论区聊聊！

#WindowsPhoneLink漏洞  #CloudZRAT  #Pheno插件  #验证码窃取  #2FA绕过  #网络安全  #远程访问工具

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cGfIHiaxhOAibibTsJVcHDbhtFv0ag2IA9b81ZpnotG5eND55SagiagYFdpes4L0YOekWuhScYdKGVGky9M9m9qP4g/0?wx_fmt=png)

安全圈动向

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cGfIHiaxhOAibibTsJVcHDbhtFv0ag2IA9b81ZpnotG5eND55SagiagYFdpes4L0YOekWuhScYdKGVGky9M9m9qP4g/0?wx_fmt=png)

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