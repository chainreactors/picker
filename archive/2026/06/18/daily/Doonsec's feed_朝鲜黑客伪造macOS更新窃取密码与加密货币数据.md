---
title: 朝鲜黑客伪造macOS更新窃取密码与加密货币数据
url: https://mp.weixin.qq.com/s/KGIlleYIxkHmaduoZd8Bfg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:23.549620
---

# 朝鲜黑客伪造macOS更新窃取密码与加密货币数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2nZ0fxSSvxTATYDgwdAamGcCGaQoqA3fv2yiaTia4xCWIic6sQt0GZFEatvITXwq2pVxmq5WW5INJ1Z5EicCV7kVOicoPGUXE7gjBQ/0?wx_fmt=jpeg)

# 朝鲜黑客伪造macOS更新窃取密码与加密货币数据

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1FY81DGvSaHzlibaPRDLZ9BBVgg5iaicWtWp3WAIM5dxpT9yNTvG2uoQUx3pvYESR89D3rLuiawvprW55Bjibe0gVMZRibfZ7KofTPo/640?wx_fmt=gif)

![macOS钓鱼攻击示意图](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3DWPBgZBPEGiantgef9MVxl3WnBQKIG8b3uApov8bNXxfQbwtPm5GRqhJ9BGzLYYe7IkbrgOKfu1KRVAdrfDL7Jlj4szLGtWyI/640?wx_fmt=jpeg)

Part01

新型社交工程攻击威胁macOS安全

一场针对macOS用户的新型网络攻击活动正构成严重威胁，该攻击完全不依赖软件漏洞实施破坏。攻击者通过精心设计的社交工程手段，诱骗受害者主动交出密码与敏感数据，整个攻击过程看起来与正常操作无异。

这场攻击伪装成常规软件更新，实则是精心布置的陷阱。当受害者察觉异常时，往往为时已晚。经微软分析师确认，该活动始于2026年初，攻击者首次采用了针对macOS的新型攻击技术。

Part02

朝鲜背景的黑客组织Sapphire Sleet

此次攻击由朝鲜国家支持的黑客组织Sapphire Sleet（至少自2020年3月起活跃）发起。该组织专门针对加密货币、风险投资和区块链相关行业的从业人员，核心目标是窃取全球高价值个人与组织的数字资产和金融信息。

攻击完全通过社交工程实施：黑客首先在社交媒体或专业平台上冒充招聘人员接触目标，经过交流后诱导受害者下载伪装成Zoom SDK更新的文件。该文件通过macOS原生脚本编辑器执行，在后台悄无声息地加载恶意代码，受害者仅能看到看似正常的软件安装界面。

![从脚本编辑器触发的级联执行过程树](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX08wxWy1ia4DGUQLHqIZGSmC3Jlm5mibv8gKDjBRK2kch9IrzL7rEBRju5AvtEPOWlHDbkeTuBfwicicz0A3elTRj0PYAZUNnMoykw/640?wx_fmt=jpeg)

Part03

伪造系统更新窃取凭证

恶意脚本运行后，会在受害者设备上静默部署名为systemupdate.app的虚假应用。该应用会显示与macOS原生密码对话框完全一致的界面，提示用户输入密码以"完成软件更新"。大多数用户会不假思索地输入密码。

密码输入后，恶意软件会立即验证其有效性，并通过Telegram消息服务将凭证发送给攻击者。随后，另一个名为softwareupdate.app的虚假应用会显示"更新完成"的提示框消除受害者疑虑。与此同时，恶意软件开始窃取加密货币钱包文件、浏览器保存的密码、Telegram会话数据、SSH密钥、Apple Notes和浏览历史记录。

![伪造systemupdate.app显示的密码弹窗](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3cVMDTLpldzGbshGcj4aq0hPMPtu1zFrUw8VhCZyuSQwM8pUY32ibvzGlzqknxUF7icRD8WCmibljcqmgjhDEal8R76gV0JL8Xdw/640?wx_fmt=jpeg)

Part04

持久化后门与数据外泄

除窃取凭证外，Sapphire Sleet还部署了多个后门维持长期访问。其中com.apple.cli组件作为主机监控工具持续与攻击者服务器通信；更高级的icloudz后门直接将代码加载到内存中，几乎不在磁盘留下痕迹，极大增加了安全工具的检测难度。

恶意软件会安装启动守护进程，确保系统每次重启后自动恢复后门。所有窃取的数据经压缩后通过8443端口上传至攻击者控制的服务器，而凭证则通过Telegram Bot API单独发送。2026年6月，微软发现该组织开始使用Microsoft Teams主题的诱饵文件，采用新的载荷名称继续实施相同攻击链。

![带有诱饵内容和载荷执行的AppleScript诱饵](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3PbkXNGOpjs4X5So9XFy0KBBs0ID6BmVIshOibHFFicMGJr0MicfU41iaBtbs22FDzHBQpBSXibwU1opDDVHqA53Ax9CjIzHCmtBhA/640?wx_fmt=jpeg)

Part05

防御建议与妥协指标

微软建议用户切勿未经IT团队确认就运行通过聊天消息分享的脚本或终端命令。企业应阻止从互联网下载已编译的AppleScript文件，并监控macOS TCC数据库的未授权变更。管理加密货币资产的用户应使用硬件钱包并定期更换浏览器保存的凭证。

攻击指标(IoCs)：

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2wJYTmZH1FKWCTOjl6SlI7gOSoJnxVU8JNcHKxEGkPFc2AmIUM2EV8zWesllicUVzcN2f5bgsDxj7HPmCRRQMq3NbuDWOV6OXU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ibQXJ71weTHnQJ14myzpGhcmQhxFhbUGgRLeCLkSOZskRibzLYIlSa7PichWhBob2egdbjX33JrBehtpIKkN7PBhJ2DZTXIAXJs/640?wx_fmt=png&from=appmsg)

注：IP地址和域名已进行安全处理（如使用[.]），防止意外解析或超链接。仅在MISP、VirusTotal或SIEM等威胁情报平台中恢复原始格式。

参考来源：

Hackers Use Fake Software Update Prompts to Steal Passwords and Crypto Wallet Data From macOS Users

https://cybersecuritynews.com/hackers-use-fake-software-update-prompts/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2cVdntRnNdReFrEC9uicNrkrzxp72OgpNDz7srDyd0sPwPYZejHF5E9TqvpJWJ5qHkqqDtlREdb65n2YIfXD2jnNBFTqRI2LhM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1uQ9xLm3d4ZLoKboK1GHqPxkP2twtDHay11g4CqZnzXFyjmtib8WT7iaP1Libibnib4wCE0UreN6hUMgkYJ6NP9gD2ib8g2RNFTUAj8/640?wx_fmt=png)

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