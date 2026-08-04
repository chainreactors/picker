---
title: 一个假“公安一网通办”App，扯出了一整条安卓远控黑产生态链
url: https://mp.weixin.qq.com/s/sBWZZM6rNpACtSeuPb05dw
source: Doonsec's feed
date: 2026-08-03
fetch_date: 2026-08-04T04:59:17.352751
---

# 一个假“公安一网通办”App，扯出了一整条安卓远控黑产生态链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GuWrHvI4xlaOzwyDg3aiaU4TWHN2lEqR7XNQXcsYDibS3vl9aC4Oa3ibHtiaHcq2U1S30veGTSIypbP2iaQ1McKAlboz2S9cpFe2Oo/0?wx_fmt=jpeg)

# 一个假“公安一网通办”App，扯出了一整条安卓远控黑产生态链

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

主要发现攻击者通过其控制的域名分发的虚假公安局应用程序是攻击的入口点。2026 年 6 月，我国官方媒体发布公告，警告公民提防伪装成官方政府服务的欺诈性应用程序，证实了这一点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0HSTXgJrFDbr1GAwVpzXA6oibCPTcrxFd5mzn9O65xAMvNVFqzw0yTAJWg0YONWFNDibHatYU39JZATXlPtB61DWQ0mtDKdiauNbM/640?wx_fmt=png&from=appmsg)

2026年2月5日，一个Telegram频道发出一张聊天截图。截图中，有人声称已经拿到了飞鹰相关客户服务器的访问权限，并开始谈条件。

同一天，这个频道开始售卖“修复版”飞鹰，价格2000 USDT，同时附上“发现后门全额退款”的承诺。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HEMZvwwlbannotWIiavK08BTKZwCaNSMQAcMe2c05A0d2tY3cbzAtibuGbgT1Sb8deWbhic8pfvokeFJ9r55AEbYkZg8dAllYUOE/640?wx_fmt=png&from=appmsg)

源码泄露的真正影响，往往不在泄露本身，而在泄露之后发生的事情。

**入口与工具本身**

公开调查显示，攻击入口是一款伪装成公共服务的安卓应用。对该应用的分析指向一个未公开的安卓应用构建器与设备控制框架，名为飞鹰（Flying Eagle）。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GJ1wpaWOk1pnN8ry4SeqZLW9jqLJF0Kjf7Md2bjVXDgm2MR8QH1ldDdYl9F1tED1MHzFf2oZKT57J5b2wMk64E3p7sL0flpiaA/640?wx_fmt=png&from=appmsg)

说明：飞鹰登陆页面

飞鹰把APK生成和完整的C2设备管理功能集成在同一个面板里。操作者可以自定义应用名称、图标、诱饵文字和回连地址，然后用内置模板生成已签名的APK。

构建过程会做多项处理：把默认包名替换成看起来合法的随机名称，把核心功能类名改成8到14位随机字符串，把C2地址用AES-128-CBC加密后硬编码进样本，并在assets目录注入2.8至3.5MB的结构化填充数据，降低文件熵值，减少被静态检测命中的概率。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HicNcTyXrZOpiamcjicteFuMwL4tZvvSbgibdGAUADVibMSr4DEXsNI6tUcW5vmkD3RFZV0iaiboiabpI7QlWBGia6Do8GHeBicNmQFL57c/640?wx_fmt=png&from=appmsg)

说明：ApkBuilder.php 脚本片段，展示了命名模式和 URL 加密。

生成的样本在沙箱中被归类为具备远程控制能力的安卓木马，核心行为包括无障碍服务滥用、手势注入、屏幕截图、键盘记录以及针对支付类应用的叠加层。

**源码泄露后的裂变**

2026年初，飞鹰的源代码连同近200个客户数据库一起被盗。泄露发生后，至少两个Telegram频道开始接手这套代码。

某SQ\*\*CE0频道更早出现。它先放出早期打包文件，随后持续发布补丁，修复域名连通性、WebSocket稳定性和防卸载等问题，并推出收费的“完全修复版”。

2026年6月23日，该频道进一步发布了名为“夜龙”的独立平台，宣称兼容更多设备，支持金融应用密码截取、黑屏假更新、安装后自动隐藏图标，并强调代码不含后门，发现即退款。调查期间，与夜龙相关的登录面板数量仍较少，第二代版本已在开发中。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EXTsZ72gCXCCGBUTBxicWa6xCgW3svkwhufeTo55icjb8UZA375EDwkntnBpRpXhqpVexiat0z8nJiaXUez2NtEDWT4QBn4fgkxQc/640?wx_fmt=png&from=appmsg)

说明：夜龙功能和设备控制接口

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HME3EBq4SjnxAlcEialm3W3BWpzyicczcMQd514Ms3xAzZhYWaopOp0icUKicOaQ1nA5uypLIxicnXejcumwIicrFXMMQkIvSicOzwAI/640?wx_fmt=png&from=appmsg)

说明：后台设备管理面板，显示可能有 29 台受害设备

另一个频道于2026年4月创建。它早期内容直接涉及资金转移操作，并提供手续费在20%至50%之间的提现渠道，随后免费分发了体积约388MB的Docker完整部署包，还上传过其他远程控制工具的密码保护版本。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EN7x3w2DaHkwBiaicLIVlpJwNicOVRG27O8nZd3uFwfKqhm3JD5iaaAvT3qflIS9Z1kpbzMzXnBle9FibSybcc7jkx2TgyQZyoJbCY/640?wx_fmt=png&from=appmsg)

说明：本地测试实例中的 APK 生成页面

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0G8GHMRARunamkUnCVVR50qCBCn011BrRKMRMswVby9qtJSdicD6IVolY0qYOGDcH2w1ZGtJyL1sxDK5hKU6rmfJ4iaZYbnqw3xU/640?wx_fmt=png&from=appmsg)

说明：飞鹰测试登录页面。

这两个频道都不是原始开发者。它们做的是接手泄露代码、修复问题、降低使用门槛，并围绕工具建立运维与变现服务。

**基础设施如何被扩线到约170台**

公开安全通知最初只给出了两个IP地址。顺着这两个地址上的TLS证书继续查询，同一服务器在重叠时间段内托管了多个域名的证书，且证书几乎每月轮换。以其中一张证书的主题为枢纽，又发现了新的IP。

更有效的指纹来自登录面板本身：页面在加载自定义品牌前会短暂显示“AdminPro”标题，访问时固定返回302跳转到HTTPS，并带有严格的传输安全头。用这些特征组合查询，30天窗口内命中约158台服务器；再加上与默认证书相关的实例，总数达到约170台。

这些服务器高度集中在少数网络服务商，部分面板使用了自定义品牌名称。同一套代码库的痕迹也出现在一次开放目录中——相同的拼写错误环境变量、相同名称的PHP文件，以及Windows环境下的部署说明，进一步确认了不同实例之间的血缘关系。

**夜龙：功能与定位上的延续**

夜龙被宣传为独立开发，但调查发现它与飞鹰在托管偏好和面板行为上存在重叠。暴露的设备管理界面提供实时屏幕查看、短信与相册访问、录音、摄像头调用和文件管理，并针对主流移动支付与银行类应用提供快捷叠加层入口。

从飞鹰到夜龙，可以看到一条清晰的演进路径：源码泄露降低了获取成本，修改版和运维支持降低了使用门槛，新平台则在隐蔽性和功能完整性上继续迭代。

**对安全从业者的实际价值**

这组公开指标说明，当一套远程控制框架的源码已经扩散，单纯封禁原始版本往往不够。更有效的监测方向包括：

* 公开聊天平台上突然出现的“修复版”“无后门版”售卖与技术支持信息；
* 与已知面板模板高度相似的新实例（特定标题、固定跳转行为、默认证书特征）；
* 同一代码库在不同部署方式下的复用痕迹。

这些观察均来自已公开的技术报告与基础设施指纹，属于调查期间的快照结果，数字和活跃状态可能随时间变化。

源码被完整放出后，真正决定工具生命周期的，往往是谁愿意接手修复、谁提供后续服务、谁把技术产品嵌入完整的操作链条。飞鹰只是其中一个被记录下来的样本。类似的模式，在其他移动端远程控制工具中仍可能重复出现。

如果你也在跟踪这类框架的演进，欢迎在评论区分享你观察到的分发或迭代现象（请注意脱敏）。技术分析的价值，在于把公开碎片连成可验证的图景，而不是停留在单点事件上。

活动时间线：

* 2026年2月4日 SQ\*\*\*E0 Telegram 频道已创建；
* 2026年2月5日 SQ\*\*\*E0 发布消息，提及 Flying Eagle 源代码泄露并与开发人员聊天。
* 2026年2月5日 SQ\*\*\*E0宣布推出“修复版”飞鹰代币，售价为2000 USDT（约合1999美元）。
* 2026年3月7日至9日 SQ\*\*\*E0持续对源代码进行升级。
* 2026年3月13日 Attack Capture 首次发现 77.105.161[.]235:8000 处存在打开的目录，其中包含 Flying Eagle 和 BTMOB V4 的 Windows 安装说明。
* 2026年4月8日 YxT\*\*\*ology Telegram频道创建了包含欺诈操作指令的Telegram频道
* 2026年4月26日 YxT\*\*\*ology 分发中\*龙.zip（Flying Eagle Docker 版本）
* 2026年5月22日 YxT\*\*\*ology 上传了受密码保护的 BTMOB RAT v4.5.5
* 2026年5月23日 YxT\*\*\*ology提供带有管理后台的基础落地页，以及访客和下载量指标。
* 2026年6月4日 为 ls.j2x8a[.]top 颁发的 TLS 证书 --- 最近一次观察到的域名轮换
* 2026年6月18日 我国官方媒体发布关于“公安一网通办”恶意软件APP的安全公告
* 2026年6月23日 SQ\*\*\*E0 引入了夜龙
* 2026年7月12日     截止当前情报第二版还在积极开发中

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0E8ibRLxcqGXU1diakEcY4xEgMhl8baFVGha8y3QH18wXRqrquMlbZCvo9WEYGSf0C9PqwLMXnv1P1oadnuXMaLtauaxosoYBlibc/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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