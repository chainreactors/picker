---
title: 【安全圈】安卓新增入侵日志功能，助力深度分析复杂间谍软件攻击
url: https://mp.weixin.qq.com/s/yXIJyDjEMxqggNx1t5vt2w
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:53.737735
---

# 【安全圈】安卓新增入侵日志功能，助力深度分析复杂间谍软件攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEqASa52UbjC7LDmea7rvxEWfAMwiaHtuQK5xj9u9FbzqDRHXMS2QOn5El7l7POYicxK7UrT64Dz4g3wTbIswyTDBsy9YV7mgicEA/0?wx_fmt=jpeg)

# 【安全圈】安卓新增入侵日志功能，助力深度分析复杂间谍软件攻击

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

日志

谷歌推出一项安卓新功能 “入侵日志”，该功能默认不开启，用于存储取证日志，以便更好地分析复杂的间谍软件攻击。

谷歌表示，“入侵日志” 作为 “高级保护模式” 的一部分，**可实现 “持久且保护隐私的取证日志记录，以便在设备疑似遭到入侵时进行调查”。**

谷歌补充称，该功能是与国际特赦组织（Amnesty International）和无国界记者组织（Reporters Without Borders）合作开发的。根据谷歌分享的一份帮助文档，它会每日记录设备和网络活动，包括设备行为信息以及运行在设备上的各类应用程序的相关信息。

以下是记录的活动类型：

* 应用活动（例如，应用进程何时启动）
* 应用安装、更新和卸载
* 网络连接情况，如 Wi-Fi、蓝牙的开启与关闭，DNS 查询以及 IP 地址
* 通过 USB 进行的设备文件传输
* 系统证书变更
* 设备锁定或解锁时间

谷歌还指出，日志数据由设备进行端到端加密，并存储在谷歌服务器上。加密密钥由谷歌账户密码和屏幕锁定凭证保护，这意味着除设备所有者外，包括谷歌自身在内的任何第三方都无法访问这些日志。

无国界记者组织表示：“通过将数据存储在安全服务器上，即便是安装在智能手机上的恶意软件也无法访问、删除或篡改数据。端到端加密还确保谷歌和国家行为者都无法访问这些数据。特别是入侵日志功能，即便面对极为复杂且以往难以察觉的攻击，也能实现检测和取证分析。”

加密日志存储期限为 12 个月，之后会自动清除。一旦开启入侵日志功能，用户在 12 个月期限届满前无法删除日志，即使关闭账户或关闭该功能也不行。如果用户希望长期保存日志，可以选择离线下载。

尽管如此，谷歌强调，日志下载和解密后，用户需自行负责其安全性。谷歌指出：“在某些法律或监管环境下，法律可能要求您提供对解密数据或安全凭证的访问权限。”

启用该功能时需要注意的另一点是，由于它在系统层面运行，不会区分浏览模式，因此也会记录 Chrome 隐身浏览期间生成的网络事件，如 DNS 查询和 IP 连接。换句话说，任何有权访问解密日志的人都能了解访问过哪些网站，但无法推断这些网站上的具体页面。

推出入侵日志功能的目的在于，高风险人群若怀疑自己因身份或从事的活动而成为高级监控工具的目标，可以将活动日志分享给可信的安全专家进行详细检查。

用户可通过依次点击 “设置” 应用程序、“安全与隐私” -> “高级保护” -> “入侵日志” -> “访问日志” 来下载日志。目前，该功能正面向所有运行安卓 16 十二月更新及更高版本的设备推出。

国际特赦组织安全实验室负责人唐查・奥・凯尔巴尔（Donncha Ó Cearbhaill）在一份声明中表示：“通过推出入侵日志功能，谷歌成为首个主动应对检测设备高级攻击这一挑战的主要厂商。通过为研究人员提供更多经用户同意的取证数据，我们可以加大攻击者的作案难度，并在民间团体的设备遭到间谍软件和移动数据提取工具非法攻击时，帮助他们追究相关方的责任。”

### 安卓即将推出的其他隐私与安全功能

除入侵日志功能外，谷歌还宣布了一系列隐私和安全改进措施，包括 “已验证金融通话”，这是一项新的电话诈骗防护功能，旨在应对诈骗分子冒充银行诱骗用户泄露敏感数据或转账的攻击。

当用户接到看似来自合作银行的电话时，安卓系统会要求已安装的网上银行应用程序确认银行是否真的在尝试联系客户。如果应用程序确认并未拨打该电话，系统将自动挂断。

谷歌表示：“您的银行或金融机构也可以将号码指定为仅用于呼入，即他们从不使用这些号码致电客户。来自这些号码的来电将直接被挂断。” 该功能预计未来几周内在搭载 Revolut、伊塔乌银行（Itaú）和努班克银行（Nubank）的安卓 11 + 设备上启用，今年晚些时候会扩展到更多银行。

其他值得关注的变化如下：

* 扩大 “实时威胁检测” 范围，针对可疑的应用行为发出警告，包括短信转发和无障碍服务覆盖，安卓银行木马通常利用这些手段窃取凭证。
* 当开启 “安全浏览” 功能时，在安卓版 Chrome 浏览器下载的 APK 文件安装前，对其进行已知恶意软件评估。
* 从所有未标记为无障碍工具的应用程序中移除对无障碍服务 API 的访问权限。
* 禁用设备间解锁和 Chrome WebGPU 支持。
* 为聊天通知添加诈骗检测功能。
* 增强 “查找中心” 的 “标记为丢失” 功能，可通过生物识别认证锁定手机，若设备被标记为丢失，可阻止小偷关闭设备追踪功能。触发 “标记为丢失” 还会开启额外保护，如隐藏 “快速设置” 并禁用新的 Wi-Fi 和蓝牙连接。
* 减少能够物理接触设备的第三方猜测 PIN 码或密码的次数，并在尝试失败后设置更长的等待时间。
* 改进设备恢复功能，在运行安卓 12 或更高版本的设备上，可通过锁屏界面访问设备的 IMEI 号码。
* 提供更好的隐私控制，允许用户在特定应用打开时，为特定任务临时分享精确位置，并向第三方应用提供特定联系人的访问权限，而非分享整个通讯录。
* 推出结合 pKVM 的 AISeal，用于对人工智能（AI）相关数据处理进行硬件支持的设备端隔离。
* 扩大安卓系统的 “二进制透明度”，通过验证官方版本以及为正版谷歌应用和基础 GMS API 提供公共分类账，确保系统完整性。
* 对大多数应用隐藏短信一次性密码（OTP）长达三小时，以防止被授予短信权限的恶意应用窃取 OTP。
* 让运营商能够默认禁用 2G 网络，保护客户免受传统技术漏洞的威胁。
* 引入后量子密码学强化数据保护，防范未来威胁。
* 引入明确的用户控制，可选择开启或关闭整个功能、安全防护措施，以及在安卓上使用 Gemini 时提供透明度。

安卓安全与隐私总监尤金・利德曼（Eugene Liderman）表示：“通过加强对银行诈骗的防护，并扩展如实时威胁检测和安卓高级保护等强大功能，我们确保安卓始终是最安全的平台。”

***END***

阅读推荐

[【安全圈】苹果修复 macOS 和 iOS 系统数十个漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=1&sn=28c320ab902f356686e31c217bcd9b65&scene=21#wechat_redirect)

[【安全圈】Windows 11遭新型BitUnlocker降级攻击：5分钟内可解密加密磁盘](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=2&sn=8bef02564b19d5593d920a9e226b38ed&scene=21#wechat_redirect)

[【安全圈】Exim 新 BDAT 漏洞致 GnuTLS 构建面临代码执行风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=3&sn=4a801e88018faba5f0fdb72a80373270&scene=21#wechat_redirect)

[【安全圈】警惕！你的蓝牙可能正被监听 改一个设置就能有效防护](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=1&sn=80e79d8ca786f2b8a4f2a23fe7d5bad4&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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