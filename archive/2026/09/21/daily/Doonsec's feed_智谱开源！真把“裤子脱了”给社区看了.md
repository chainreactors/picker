---
title: 智谱开源！真把“裤子脱了”给社区看了
url: https://mp.weixin.qq.com/s/ezOaJRnahCu5GZKUZFLllw
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:01:47.567257
---

# 智谱开源！真把“裤子脱了”给社区看了

# 智谱开源！真把“裤子脱了”给社区看了

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**前两天还在被骂“致歉日还在偷传代码”，**

**[致歉当日凌晨还在偷传！智谱ZCode被实锤：你的代码，正在流向新加坡？](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247557262&idx=1&sn=6598fee23676a360967fede15f243af0&scene=21#wechat_redirect)**

**今天（2026年9月21日）智谱直接放大招：****ZCode 开源了**，代码扔到 GitHub（zai-org/ZCode），Apache-2.0 协议，客户端、后端、Agent 运行时全摊开。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLEqCTGYQDJx2kWHichDdoMDiaUiaq8y4QCd9sLn9H3TmkFBAGNWsqGAFEwa1tFHSE8NAYCVaFGrgDicog6OgNA8960aczff3PwT7M/640?wx_fmt=jpeg)

这波操作，不像公关稿，像技术男被逼急了：“行，你们不是不信吗？自己看。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLvG04ibDfeYqOicQ5K7ObxmDgeyePUM9naEFsWy9SRI6ajj5kYTknIO8oVwhDg0dpmHpeib4HtOuxARpdEQvfxwF8FB6KPicNS28E/640?wx_fmt=jpeg)

**先认错，再把刀递给你**

智谱致歉说得很直白：社区反馈的产品安全问题，**已整改、已道歉**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKCVYKwTue7tM2m8UzVTpB8TNK64xF6LCVQfXaHrhrz29EFaria2I5AuNcQ9AaDb819kcfADxsf2GV4eaTsRxD1wQBm3WQma5SY/640?wx_fmt=jpeg)

但有网友分析了代码，评论

“开源看到更多不堪”

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJH1dnGf1VuicibDu0yP9GJ49pzuo1OAibXJodshM7jlLvzBpbs2TicGaTQj0bEh2txsUhzRLEDJwNezfWfbumF6GVVmvRXmPSCGnc/640?wx_fmt=jpeg)

最关键的 Repo Wiki 功能——就是那个被扒出会打本地仓库快照、关了开关还可能上传的玩意儿——**v3.14.0 里直接砍了**，快照生成和上传链路全切断。

以前是“我发声明你爱信不信”，现在是“代码挂网上，爱审不审”。

网友评论：

“至少态度上和行动上都是好的，没有抵赖，比其他公司的道歉声明诚恳务实很多。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJS4reRgn8x703JuuN2b00FHxHqg1haMczfs4MkFvPbU7ZtQy3ZMdxaAod7GQZDeBzThMXKBdm5RicZS2BI1Sac0d1XYIXVuOhY/640?wx_fmt=jpeg)

**两家机构背书：云端确实是空的了**

光自己说没用，智谱拉来中国信通院 + 绿盟科技：

* 信通院：zcode-prod 阿里云 OSS 存储桶，**云端零数据**；
* 绿盟：OSS 里数据对象和桶本身**都删了**，新客户端里找不到任何能触发快照/外发的路径。

  再加上那句“提及的代码数据无留存、从未用于模型训练”——到这儿，信任危机总算从“嘴硬”进入“可验证”阶段。

**开源不是终点，是接着挨锤的开始**

智谱还留了后手：建常态化安全漏洞机制，开发者找问题按严重程度给回报。

说白了，以后别再说“你暗箱”，你敢提 PR、敢发 CVE，我就敢改。

大厂 AI 编程工具走到“把底盘亮出来”，在国内真不多见。

**说人话总结**

ZCode 这波不算洗白，算“交投名状”：

以前信不过你，以后**代码、审计、漏洞赏金**三件套摆桌上。

国产 AI 要想让人敢把公司仓库接进去，就得这么玩——

**别等翻车才道歉，别等致歉还上传，别等开源才透明。**

要不要我顺手写个“开发者自查 ZCode 还安不安全”的极简清单，教读者看 GitHub 仓库、堵域名、查 `~/.zcode`？

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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