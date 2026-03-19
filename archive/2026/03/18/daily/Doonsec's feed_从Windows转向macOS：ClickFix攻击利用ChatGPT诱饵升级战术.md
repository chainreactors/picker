---
title: 从Windows转向macOS：ClickFix攻击利用ChatGPT诱饵升级战术
url: https://mp.weixin.qq.com/s/1fmm5nCI0ZqojoJfPDrG7g
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:18:15.035519
---

# 从Windows转向macOS：ClickFix攻击利用ChatGPT诱饵升级战术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX15XFx2GU6o15bhVljdtsiaAGooOpKeFw6N5gX1tAV8ZGBNM78mn4zErHU4UOaiaOBSibgMxdnshUJKgQjbYrNdm44ekISwp6Licyk/0?wx_fmt=jpeg)

# 从Windows转向macOS：ClickFix攻击利用ChatGPT诱饵升级战术

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1flLw6euHnJmPsBDKQsxEibOnn2mN1HdwMNSatC2Kk5echzddOYaQLvRRmCGQaDmztPgSlonicbBicyiakkg8TBAQHT24DvjFHfQg/640?wx_fmt=png&from=appmsg)

##

## Sophos研究人员发现，ClickFix这种诱导用户手动执行恶意命令以绕过传统防护措施的社会工程技术正在演变。该技术最初主要针对Windows系统，如今正越来越多地影响macOS平台，近期攻击活动中部署了AMOS和MacSync等信息窃取程序。研究人员指出，这种战术演变可能源于防御措施升级和更广泛的技术趋势。

##

**Part01**

## ****第一阶段：基础但有效的终端命令欺诈****

Sophos研究人员分析了三个针对macOS用户的ClickFix攻击活动，均部署了MacSync信息窃取程序。2025年11月，攻击者采用相对"经典"的ClickFix技术：受害者搜索ChatGPT相关工具时，会通过谷歌赞助的恶意链接被诱导至伪造的OpenAI/ChatGPT页面。这些页面指示用户复制并执行经过混淆处理的终端命令，最终下载并运行MacSync信息窃取程序。这种方法虽然简单，但依赖用户信任和欺骗手段而十分有效。

Sophos报告指出："注意上方的终端命令，经过去混淆处理后，会从攻击者控制的网站下载并执行Bash脚本。该脚本会要求用户输入密码，随后获取并以用户权限运行恶意的MachO二进制文件（即MacSync信息窃取程序）。"

**Part02**

## ****第二阶段：利用ChatGPT对话提升可信度****

到2025年12月，攻击活动的传播和规避战术明显升级。攻击者不再直接将用户重定向至虚假下载站点，而是利用合法的ChatGPT共享对话建立可信度。这些页面随后跳转至模仿合法安装流程的GitHub主题虚假界面，诱使用户运行恶意命令。该技术成功绕过了macOS的Gatekeeper和XProtect等防护机制。

报告进一步说明："ChatGPT对话看似提供'如何清理Mac'或安装工具等实用指南，实则将受害者重定向至恶意GitHub主题着陆页，再通过伪造的GitHub安装界面诱骗用户运行恶意终端命令（即攻击链中的ClickFix环节）。这能有效规避macOS的Gatekeeper和XProtect等安全控制措施。"

![image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0HUwG3OFxMKjfe6xwScH17VewkXD4RFWYeOO2IIIAcu09yVQAVyt9ghpsoRqss22AFicoQXTA722NaJn9f4017C9mpQkqySk6o/640?wx_fmt=jpeg&from=appmsg)

同时，攻击者引入了复杂的追踪基础设施，包括基于JavaScript的分析工具、IP和地理位置记录，以及通过Telegram机器人实现的实时报告功能。这使得他们能够监控攻击效果——多个域名的用户交互量已达数万次。

**Part03**

## ****第三阶段：模块化服务与内存攻击****

到2026年2月，该攻击行动已演变为更高级、更隐蔽的威胁。虽然初始阶段仍依赖用户交互，但有效载荷投递已转变为多阶段的"加载器即服务"模式。恶意软件不再使用简单的二进制文件，而是采用混淆的shell脚本、API密钥保护的C2基础设施，以及在内存中执行的动态AppleScript有效载荷。这些改进显著提升了对抗静态和行为检测的能力。

最新版MacSync可窃取浏览器数据、凭证、文件、SSH密钥、云配置和加密货币钱包等广泛数据。它还具有分块数据外传、持久化机制和反分析技术等高级功能。值得注意的是，它能通过注入恶意代码篡改Ledger钱包应用，窃取助记词，使攻击者可直接盗取加密货币资产。

**Part04**

## ****攻击模式全面升级****

总体而言，这些攻击活动展现出从相对简单的社会工程攻击向高度模块化、隐蔽且以数据为中心的运营模式转变，既反映了对防御措施的适应，也体现了攻击者技术的日益成熟。

报告总结道："这三个攻击活动展示了多种战术，以及对传统ClickFix模式的改进。虽然都利用了生成式AI相关诱饵，但从冒充知名企业的恶意网站转向共享ChatGPT对话，标志着社会工程技术的重大转变。攻击者成功利用了两大优势：在可信域名托管恶意内容（首轮攻击也已采用），以及利用ChatGPT对话的相对新颖性。"

**参考来源：**

From Windows to macOS: ClickFix attacks shift tactics with ChatGPT-based lures

https://securityaffairs.com/189542/cyber-crime/from-windows-to-macos-clickfix-attacks-shift-tactics-with-chatgpt-based-lures.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

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