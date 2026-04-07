---
title: Claude Code代码泄露引发武器化攻击潮
url: https://mp.weixin.qq.com/s/Y4rMP8W9T1MRBMkMFTIygQ
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:12.019307
---

# Claude Code代码泄露引发武器化攻击潮

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1hsTJhxDShaZcHI8zibXz9rytY1lpfibSMhWaSvQ7Gs108AeywkMoQncc62umMT7Ayib9Fjg0M55zlbZ1icI4dop5ibqosWVuU5kT0/0?wx_fmt=jpeg)

# Claude Code代码泄露引发武器化攻击潮

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0W15c2vqqt2EhkXIHfBiaJrDUWWOP5pv0CDFvRNd5auYhcNEvTRZHGhlHzRqiaQcEXZKujoYlrhHjhTLJkicAd4JnOnyLD6f6XVc/640?wx_fmt=png&from=appmsg)

##

Anthropic 出现大规模源代码泄露事件后，网络安全界已处于高度警戒状态。2026 年 3 月 31 日，该公司意外泄露了其旗舰级终端编程助手 Claude Code 的完整源代码。

此次泄露源于一个公开 npm 安装包的打包错误，该安装包不慎包含了一个 JavaScript 源码映射文件，其中存有超过 50 万行未做混淆处理的 TypeScript 代码。尽管泄露的数据不包含模型权重和用户数据，但仍暴露了高度敏感的内部运行机制。

安全研究员 Chaofan Shou 在社交媒体上公开披露此事后，该代码库几乎立刻被镜像到 GitHub 平台，并被复刻了数万次。

![Google search results for leaked Claude Code on GitHub returning a malicious repository (Source: Zscaler)](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0jianLNUOibP56QtonJyLZ31UQYvyTibcv9CA6ic6PSX4Kb8DHLvrR0zhzRFWCxHq7FhGEortDkm3alB52JxrH2KfNY2LCBPY5kUg/640?wx_fmt=png&from=appmsg)

谷歌搜索 “GitHub 上泄露的 Claude Code” 时，结果中出现了恶意代码仓库（来源：Zscaler）

这些专有代码的大范围扩散，形成了一个巨大的供应链攻击面。网络犯罪分子正积极将这一事件武器化，制作恶意复刻版本，用以攻陷开发者的工作设备。

Zscaler 威胁实验室的研究人员近期发现了一场极具欺骗性的攻击活动：攻击者以此次代码泄露为社会工程诱饵，专门针对试图获取该源代码的开发者下手。

![Malicious GitHub repository using the leaked Claude Code source as a lure (Source: Zscaler)](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0MwQbicwWbJAyrvFyFAuQs48keLjlQDSrUcIgScpGEY5lWw519joskuJuYrvP6Kn8gsKsGQgWP6iaqVvqria0xpAL9O3wtrvSyQM/640?wx_fmt=png&from=appmsg)

以泄露的 Claude Code 源码为诱饵的恶意 GitHub 仓库（来源：Zscaler）

**Part01**

## ****投放 Vidar 与 GhostSocks 恶意软件****

##

在此次新发现的攻击活动中，攻击者搭建了伪装成正版泄露源码的恶意 GitHub 仓库。

其中一个由恶意用户 idbzoomh 发布的显眼页面，目前在用户搜索相关文件时，排名接近搜索引擎前列。

![Malicious GitHub repository using the leaked Claude Code source as a lure (Source: Zscaler)](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sMRawSnngXTbicw7WpvExOzVBvmVrg0z8v0GbpkSATibb4UmjNrtcEtCmhehphLMfiaReZ6SgZ4pnmKTH2GV4yNa0mZ6aI46k4I/640?wx_fmt=png&from=appmsg)

该代码仓库声称提供无使用限制的企业版解锁软件，但压缩包内并非合法代码，而是一个基于 Rust 语言编写的加载器程序。

该加载器运行后，会部署 Vidar 信息窃密木马以窃取敏感凭证，同时部署 GhostSocks 代理工具转发网络流量。

此次 GhostSocks 的投放方式，与此前观察到的攻击活动高度相似：攻击者均通过伪造软件安装器，同步分发网络代理工具与数据窃密类恶意软件。

![ Additional GitHub repository hosting the same Claude Code leak lure with a “Download ZIP” button. (Source: Zscaler)](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0VDJBmkxibSlIJyEB4nJ8zmEIb0q2vbn3Zs9wBBEiaoZx6ibAkInQkm0Ahy9cSwwjIh5kXc5Vpdpxpk8W4jJ7xJr9UQ8zTHeZXiaU/640?wx_fmt=png&from=appmsg)

另一个同样以 Claude Code 泄露源码为诱饵、带有 “下载 ZIP” 按钮的 GitHub 仓库（来源：Zscaler）

这些内部组件的暴露带来的严重风险，远不止简单的社会工程诱骗。泄露文件揭示了复杂的调度逻辑、权限执行层级、持久化内存系统，以及数十个隐藏的内部功能开关。

由于原始代码库具备本地 Shell 执行、脚本自动运行等高级能力，掌握完整源码的攻击者可以轻松构造精准的利用程序。

攻击者只需诱骗开发者克隆不可信仓库，或打开特制的项目文件，就有可能实现对设备的静默控制或凭证窃取。

**Part02**

## ****缓解措施与防御策略****

##

企业必须立即部署防御措施，保护开发环境免受此类投机性攻击。

安全团队应强烈建议所有开发者，不要下载、编译或运行任何声称是 Anthropic 泄露源码的程序。严格通过官方渠道和已签名二进制文件获取软件，是保障程序完整性的关键。

此外，部署零信任架构并对关键应用进行访问隔离，有助于在开发者设备沦陷后缩小攻击影响范围。

监控异常出站网络连接、扫描本地环境中可疑的 npm 安装包，是发现早期感染迹象的关键步骤。

##

**参考来源：**

Hackers Weaponize Claude Code Leak to Spread Vidar and GhostSocks Malware

https://cybersecuritynews.com/claude-code-leak-to-spread-vidar-and-ghostsocks-malware/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1df9O3S7TcqYQ5TtfibKYusLhstH06qHkXsM712er2kqnjI8bykhu6xWMFStgejUxm8xOIKU6ibAmY2cojOAEcd3IawxVWR9UcM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651336627&idx=1&sn=980bb90fbcbc3a4df630ccd700eefbcf&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

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