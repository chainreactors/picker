---
title: 黑客攻击导致至少16个Chrome浏览器扩展程序被入侵，影响超过60万用户
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492498&idx=1&sn=10ab1206b0915453dfe9f606e7ed2126&chksm=e90dc9b8de7a40ae78075d991e0d069ab9ce41bdf11b669d879a02a614885acc6d0d2a7941d9&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-01-03
fetch_date: 2025-10-06T20:10:31.928383
---

# 黑客攻击导致至少16个Chrome浏览器扩展程序被入侵，影响超过60万用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 黑客攻击导致至少16个Chrome浏览器扩展程序被入侵，影响超过60万用户

BaizeSec

白泽安全实验室

近期，一起重大的供应链攻击事件导致至少16个Chrome浏览器扩展程序被黑客入侵，暴露了超过60万用户的数据。攻击者通过钓鱼信息针对Chrome网上应用店的扩展程序发布者，一旦获得账户访问权限，便在扩展程序代码中植入恶意代码。

在这次复杂的攻击活动中，黑客通过精心设计的网络钓鱼邮件，冒充Chrome网上应用店官方通信，诱骗扩展程序开发人员授予恶意应用程序访问其账户的权限。这些邮件营造紧迫感，要求开发人员点击链接以接受政策许可，进而引导他们至一个伪造的Google登录页面，并要求授权名为“Privacy Policy Extension”的恶意OAuth应用，从而控制开发者账户。获取账户控制权后，攻击者向扩展程序注入名为“worker.js”和“content.js”的恶意文件，这些文件包含窃取Facebook账户数据的代码。这两个文件是恶意程序的关键组成部分，worker.js负责联系一个硬编码的命令与控制(C&C)服务器，下载配置并执行HTTP调用；而content.js则负责从目标网站收集用户数据，并将其泄露到C&C有效载荷中指定的恶意域名。

研究人员进一步调查了此次攻击，并发现其他Chrome浏览器扩展程序也受到了影响，包括但不限于：

* AI Assistant – ChatGPT和Gemini for Chrome
* Bard AI Chat
* GPT 4 Summary with OpenAI
* Search Copilot AI Assistant for Chrome
* TinaMInd AI Assistant
* Wayin AI
* VPNCity
* Internxt VPN
* Vindoz Flex Video Recorder
* VidHelper Video Downloader
* Bookmark Favicon Changer
* Castorus
* Uvoice
* Reader Mode
* Parrot Talks
* Primus
* Tackker
* AI Shop Buddy
* Sort by Oldest
* Rewards Search Automator
* ChatGPT Assistant – Smart Search
* Keyboard History Recorder
* Email Hunter
* Visual Effects for Google Meet
* Earny

此次攻击事件再次提醒用户和开发者，网络安全的重要性不容忽视。用户应保持警惕，定期更新和审查安装的扩展程序，而开发者则需加强安全措施，防止账户和代码被恶意攻击者利用。根据目前的初步研究，这是一次非针对性攻击，是针对Facebook广告用户的更广泛活动的一部分。

参考链接：

https://securityaffairs.com/172491/hacking/chrome-browser-extensions-compromise.html

https://secureannex.com/blog/cyberhaven-extension-compromise/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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