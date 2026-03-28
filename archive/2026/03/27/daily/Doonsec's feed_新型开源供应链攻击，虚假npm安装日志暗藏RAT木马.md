---
title: 新型开源供应链攻击，虚假npm安装日志暗藏RAT木马
url: https://mp.weixin.qq.com/s/kAi3ueHFGINskU24SXMZEA
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:10.537851
---

# 新型开源供应链攻击，虚假npm安装日志暗藏RAT木马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3icLg5tAmetHbJQNjibjge8hyNRJOhsswbEK6GAG9lqmwbBKUwZ8F5YOpOTwlbANXZOQ2puTCRlhTM4ibhhaNRrcLjbjO3kexJ2Y/0?wx_fmt=jpeg)

# 新型开源供应链攻击，虚假npm安装日志暗藏RAT木马

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3kuQUXmyQYmcAm8X3q9t0Iq9NCxKLEBCBIXVK47Q2oanzqfuZOTbgVXU7NyOgGYicHykhUQng8l4hjv4Blyb5mlYXEuFDia7eoE/640?wx_fmt=jpeg&from=appmsg)

##

**Part01**

## ****攻击概述****

安全研究人员发现一场精心策划的新型软件供应链攻击正通过 npm 包注册表针对开发者，攻击者利用虚假安装日志掩盖恶意活动。这项被命名为"幽灵行动"（Ghost campaign）的攻击始于 2026 年 2 月初，攻击者构建了一系列 npm 包诱骗开发者提交系统凭证，同时在受害者机器上秘密部署远程访问木马（RAT）。

**Part02**

## ****攻击流程剖析****

当开发者安装恶意包时，攻击即刻启动。这些包会模拟正常的 npm 安装过程——输出日志信息、显示进度条并插入随机延迟以增强真实性。实际上，屏幕上显示的待下载包名均来自硬编码列表，所有声称要安装的依赖均不存在。这种欺骗手段使得即使经验丰富的开发者都难以察觉异常。

ReversingLabs 分析师在 2026 年 2 月初识别出该恶意活动，溯源发现 7 个相关包均由名为"mikilanjillo"的 npm 用户发布，包括：

* react-performance-suite
* react-state-optimizer-core
* react-fast-utilsa
* ai-fast-auto-trader
* pkgnewfefame1
* carbon-mac-copy-cloner
* coinbase-desktop-sdk

**Part03**

## ****技术突破与后续扩散****

研究人员指出，使用虚假安装日志掩盖恶意行为属于新型攻击技术，标志着威胁行为体在开源生态系统中规避检测的手段出现显著演变。攻击最终阶段会投放专门窃取加密货币钱包、收集敏感数据并接收攻击者服务器指令的 RAT。

该活动的影响范围超出最初发现的 7 个包。2026 年 3 月，JFrog 记录了名为 GhostClaw 的相关攻击集群，其技术与基础设施与 ReversingLabs 发现的样本高度相似。Jamf Threat Labs 分析进一步显示，攻击还通过伪装成交易机器人和 SDK 等合法开发工具的 GitHub 仓库传播。这些仓库先植入无害代码并长期保持静默以建立信任，随后才引入恶意组件。

**Part04**

## ****核心欺骗机制：虚假日志与 sudo 钓鱼****

攻击最具迷惑性的环节是诱骗开发者提交 sudo 密码。在虚假安装过程中，包会输出错误提示，声称由于缺少对/usr/local/lib/node\_modules（Linux/macOS 系统标准全局包目录）的写入权限而无法安装依赖，继而诱导开发者输入 root 密码以"解决问题"。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3pBfoQmBD35tGA95z9Xjo5JlCJMwNvrLcM1ZJ5gwNaAgLyUsVz2blDl6hb83vTybiac9XiapT4QF1VqIfkmdFQ9icvj8cCn4GT7U/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1RTuCqXgSXM7gtJ51XZkerFTbeCu1jFIEvPRWxKMyvYeZQqI7mPWv3TiciaGEPw17NxF6qllUK9Ec5379sz4MBLWgViaCTwPTvXw/640?wx_fmt=jpeg&from=appmsg)

密码确认后，恶意下载器便在虚假日志的掩护下静默运行。下载器会从 Telegram 频道获取最终载荷 URL 和解密密钥，在某些案例中这些信息被隐藏在 teletype.in 上伪装成区块链文档的 Web3 帖子中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cMshrMmlKDQSF8rzPX20pTNSOCicd8UmQ5n4a0icjHmFkgTFIKeq42PmcNQzpbyzu4iasCh5icZj79eCDAicNCUSOJ0yUoict9sd5c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2aaKkmDL2wsFrnunSP5BbMmxRS24obBbwQTib2Uqkic91cOBXicSNPdImc8nOAv2spm5B0kl9uoMicnoISn9fQ2fU0vezb6DF2TqE/640?wx_fmt=png&from=appmsg)

**Part05**

## ****防护建议****

开发者应特别注意：

* 安装过程中绝不应 npm 包要求输入 sudo 或 root 密码，合法包在此阶段无需系统级访问权限
* 安装前务必验证包作者及仓库历史记录
* 使用自动化安全扫描工具检测可疑脚本 企业应实施严格的依赖项审查流程，并将软件安装过程中的任何密码提示视为重大危险信号。

**Part06**

## ****攻击指标（IoC）****

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0CupicBmdtvOdiceQbRIBV6mIjgtrUtxIPNKJJlzvowa0Aaaa2ibO3l5jd1HBM7NYlte1kU7RGgiakRBsxFgsfIqh3RAibJYUP4EHE/640?wx_fmt=png&from=appmsg)

**参考来源：**

Fake npm Install Messages Hide RAT Malware in New Open Source Supply Chain Campaign

https://cybersecuritynews.com/fake-npm-install-messages-hide-rat-malware/

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