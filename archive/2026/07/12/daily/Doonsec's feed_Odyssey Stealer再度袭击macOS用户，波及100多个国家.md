---
title: Odyssey Stealer再度袭击macOS用户，波及100多个国家
url: https://mp.weixin.qq.com/s/yhyhO6Hb6PdapM5eEemeWQ
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:27:12.541211
---

# Odyssey Stealer再度袭击macOS用户，波及100多个国家

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0jfgE6Lt54wdeSPOfThbOkvjQglDdlbKsAAib9k5Rn056Egl0xW2oia7sCWtg6XML0A7km8JaiaDAWtialVQiaerg87Rpib9XfwLjaE/0?wx_fmt=jpeg)

# Odyssey Stealer再度袭击macOS用户，波及100多个国家

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX0ibYibZGZlKuKE6MQA47jFpPx6osAZGYX5dhylJEfTCeheRBBWzibPMS2sZrB8Qa98cUiaPHHp3utco6opUwN2G7icbJsA6J0Kt6js/640?wx_fmt=gif)

![Odyssey Stealer再度袭击macOS用户](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2MFN2MvAA9vUConVcYZJMibMiaCxbpLsvicvaJF46COFoxxg7chTRlghlrZiaCF8EIoIC3KDMficvPL0Dtx2duuJXMeaVQ6WTm0Ufc/640?wx_fmt=jpeg)

Odyssey Stealer再次将目标对准macOS用户，近期攻击活动激增，已波及100多个国家的受害者。这款信息窃取恶意软件专门收集凭证、浏览数据、加密货币资产及其他敏感文件，可迅速暴露个人及企业账户。

该攻击活动通过欺骗性软件和更新提示传播，包括ClickFix式社会工程学诱饵，诱导用户运行恶意命令。一旦启动，恶意软件会静默搜索设备中的有价值信息，并将其发送至攻击者控制的基础设施。

这些诱饵利用用户的常规操作习惯，而非利用新披露的macOS漏洞。一个看似可信的提示就能将正常的下载或故障排查步骤转变为感染过程。因此，即使保持操作系统更新，用户也必须仔细核实来源。

Moonlock Lab在分享给Cyber Security News（CSN）的报告中指出，这一广泛攻击面可能影响个人用户、投资者及企业Mac用户。Moonlock Lab的分析人员识别了此次最新活动，并报告称该恶意软件拥有比一般以浏览器为目标的窃密程序更广泛的窃取能力。

Part01

针对浏览器和密码的全面窃取

研究人员发现，Odyssey能够从主流浏览器中收集密码、Cookie和自动填充数据，包括Chrome、Brave、Edge、Vivaldi、Opera、Arc、Firefox和Waterfox。

其影响不仅限于浏览器登录信息。通过窃取钱包数据、云平台和开发者凭证、即时通讯应用信息以及本地系统记录，攻击者可利用多个途径盗取资金、接管账户或深入侵入受影响环境。

自动填充信息还会暴露姓名、地址、支付详情及其他为便利而保存的数据。对于开发人员、管理员和远程工作者而言，SSH密钥以及AWS、Google Cloud、Azure和Docker的配置数据被盗尤为危险。被盗的FileZilla登录凭证、Keychain数据库数据、Telegram和Discord信息、shell历史记录以及本地可检索的密码，都可能在初始入侵后进一步扩大危害。

Part02

加密货币用户面临严重风险

加密货币用户在此次Odyssey Stealer版本中面临尤为广泛的威胁。Moonlock Lab表示，该恶意软件瞄准约300个加密货币钱包扩展的ID，这种方法让攻击者能够搜索大量基于浏览器的钱包，而非依赖某一种流行服务。

恶意软件还会搜索与16款桌面加密货币应用程序相关联的钱包文件。目标应用包括Electrum、Exodus、Ledger Live、Trezor Suite、Bitcoin Core、Litecoin Core、Dash Core和Monero，这使得软件钱包用户以及通过配套应用管理硬件钱包的用户均面临风险。

窃取流程不仅限于钱包。Odyssey可获取浏览器密码和会话Cookie，攻击者可能因此无需立即知道密码就能访问账户。自动填充信息还会暴露姓名、地址、支付详情及其他为便利而保存的数据。对于开发人员、管理员和远程工作者而言，SSH密钥以及AWS、Google Cloud、Azure和Docker的配置数据被盗尤为危险。被盗的FileZilla登录凭证、Keychain数据库数据、Telegram和Discord信息、shell历史记录以及本地可检索的密码，都可能在初始入侵后进一步扩大危害。

Part03

持久化机制提升威胁等级

该恶意软件试图通过在Mac上安装持久化的LaunchDaemon来驻留系统。LaunchDaemon是一种系统组件，可自动启动程序。这使Odyssey在重启后有更大机会重新运行，继续其数据收集活动，且无需受害者重新打开原始诱饵。

Moonlock Lab还观察到，攻击操作会替换Ledger、Trezor和Exodus应用程序，替换为旨在盗取钱包的木马版本。受害者可能认为自己正在使用可信的钱包程序，但实际上替换后的应用被设计为重定向或窃取加密货币交易。

攻击者使用一个主C2服务器和备用域名，即使一条连接路径中断，恶意软件也能接收指令并传输窃取的数据。该攻击活动还使用了第二阶段的木马钱包载荷，表明感染可能在首次窃取数据阶段之后进一步升级。

用户应始终在安装软件前验证来源。仅从官方供应商网站或Mac App Store下载软件，对意外的更新提示保持警惕，并在输入恢复信息前检查钱包应用，可降低风险暴露。

企业应留意可疑的LaunchDaemon、异常的对外连接以及钱包应用的意外变化。任何怀疑遭受感染的用户应立即断开Mac与网络的连接，从另一台可信设备更改凭证，检查加密货币账户，并在恢复正常访问前寻求事件响应支持。

攻击指标（IoCs）：

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3lDzJ2VgHe3SteYuOrQbHVxGACzY6M75a2kMAVkUZADiaRkJBXx6p0sFFf5VKMiauu67lecDvOhaxvMg4za882fX93sIaMFMCkM/640?wx_fmt=png&from=appmsg)

注意：IP地址和域名已进行脱敏处理（如[.]），以防止意外解析或超链接。仅在受控威胁情报平台（如MISP、VirusTotal或您的SIEM）中恢复原始格式。

参考来源：

Odyssey Stealer Hits macOS Users in 100+ Countries, Targets 300 Crypto Wallet Extensions

https://cybersecuritynews.com/odyssey-stealer-hits-macos-users/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

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