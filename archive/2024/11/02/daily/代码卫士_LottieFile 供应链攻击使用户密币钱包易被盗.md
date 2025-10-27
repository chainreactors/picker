---
title: LottieFile 供应链攻击使用户密币钱包易被盗
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521357&idx=1&sn=59e85c17b04d58d9bf269db28b3f7104&chksm=ea94a527dde32c3125fd93f22805ff0add4099ed03bd0dcfc4fda8b64a482bd578f73c461d26&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-02
fetch_date: 2025-10-06T19:17:37.153967
---

# LottieFile 供应链攻击使用户密币钱包易被盗

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQZGhzRE4MsrALm3RE0JXrMmicoQNWqYmOd8EhcVe3wlaBcfS6V0tUReolSxyyzvJib6iabeRLzK0sKQ/0?wx_fmt=jpeg)

# LottieFile 供应链攻击使用户密币钱包易被盗

Connor Jones

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQZGhzRE4MsrALm3RE0JXrMnBc53DTf0q3FYf5KOlFLIibNnMPPVgJZsXKjfZQTnR3suLUnib5xicdibg/640?wx_fmt=gif&from=appmsg)

**LottieFiles 的一个开发者账户遭攻陷，被用于洗劫用户的密币钱包。**

LottieFiles 的热门网站动画插件 LittiePlayer 最为人所知，其联合创始人兼首席信息官 Nattu Adnan 在本周四证实称，攻击者利用被盗会话令牌访问了一个高权限开发者的账户并将恶意代码推送给用户。他提到，该代码旨在让 LottieFiles 用户将密币钱包连接到攻击者的基础设施，从而清空他们的资产。

论坛用户在访问依赖于 LottiePlayer 动画功能的站点时讨论了这一异常发现。访问站点时，用户收到连接钱包的提醒。攻击者在一个小时的时间内想 npmjs 包管理器推送了LottiePlayer 的三个版本（2.0.5、2.0.6、2.0.7），这是该项目在两个月内发布的第一批变更。

其中很多网站被配置为使用 LottiePlayer 的最新版本，而非手动选择版本，因此导致恶意版本自动推送给用户。Adnan 在该项目的 GitHub 页面上提到，“在协调世界时10月30日的下午6:20左右，LottieFiles 收到通知称，web 播放器 @lottiefiles/lottie-player的热门开源 npm 包，未经授权推送了含有恶意代码的新版本。dotlottie 播放器和/或 SaaS 服务并不受影响。之后我们启动了事件响应计划，为您造成的不便，我们深表歉意。我们致力于保护用户、客户及其终端用户、开发者和员工的安全。”

他补充道，他们聘请了外部安全专家，击退了攻击者，并发布了安全版本 2.0.8，该问题已解决。网站管理员如无法更新至该版本（2024年3月份发布的版本2.0.4的复制版），则建议与客户非常清晰地沟通，告知他们不应在收到提示时，连接自己的钱包。他提到，“我们已确认，其它开源库、开源代码、GitHub 仓库和 SaaS 服务并不受影响。”

Adnan 并未就受该事件影响的用户数量置评，不过 LottiePlayer 非常流行，每周的下载量为9.4万次，自首次发布起已经下载了400多万次。再次重申，该项目并未发布官方确认，不过 Web3 安全平台 Scam Sniffer 发现一起交易，一名受害者因该攻击被盗10个比特币（约合722508美元）。

该事件只是一年来发生的值得注意的钱包洗劫攻击事件之一。上个月，一款恶意安卓 app 盗取了受害者约合7万美元的密币资产。不管是通过app、像 LottiePlayer 遭受的供应链攻击，还是利用智能合约部署操作码的机制，网络犯罪分子一直都在伺机赚快钱。

大概近一年前的这个时候，密币交易所 Poloniex 的用户资产丢失1.2亿美元，而就在几天前，门罗币项目被盗近100万美元。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Python、npm和开源生态系统中的入口点可用于发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&chksm=ea94a22fdde32b396a0c379623e7d047d6762947c21f033e10a0d1e0f8567a584c4d74c12e27&scene=21#wechat_redirect)

[MLOps 平台存在20多个供应链漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520605&idx=2&sn=6bd044882cfd8e5f96140c71e26498f4&chksm=ea94a037dde32921016d3ccc578f09450825636f654da7d674940fccba2dbb77ba63a80dd774&scene=21#wechat_redirect)

[在线阅读版：《2024中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&chksm=ea94a18edde328988758d00a0c6c91218ef60546d92e98647d91c44e557d14c15596b8aff06c&scene=21#wechat_redirect)

[JFrog Artifactory 缺陷导致软件供应链易受缓存投毒攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520385&idx=2&sn=af4a594c3080780ffef2c03ee32f72d5&chksm=ea94a1ebdde328fdfc828f63fc0ecbd0128261440aeba197b83f1d8e451ce4507c42bfa4878a&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/10/31/lottiefiles\_supply\_chain\_attack/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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