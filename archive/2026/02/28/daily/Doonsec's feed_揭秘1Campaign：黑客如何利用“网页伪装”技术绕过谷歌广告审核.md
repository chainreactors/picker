---
title: 揭秘1Campaign：黑客如何利用“网页伪装”技术绕过谷歌广告审核
url: https://mp.weixin.qq.com/s/FmQM2yEpB1QzK5wk8lwdWQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:16:32.898962
---

# 揭秘1Campaign：黑客如何利用“网页伪装”技术绕过谷歌广告审核

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2uibKk5l4yQG2LOLicRuqicSuhgq3Khias037LQRprQhWkw2icmjesAossaGric5EAHUHHtDyzN3UffpMWrVDI1iaViakpszThdK6iayzU/0?wx_fmt=jpeg)

# 揭秘1Campaign：黑客如何利用“网页伪装”技术绕过谷歌广告审核

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

网络安全研究人员近期发现，一套名为“1Campaign”的黑客工具包正在被恶意利用，专门用于绕过谷歌的广告审核系统，向普通用户投放危险的诈骗广告。

伪装大师：同一网页，两种面孔

1Campaign的核心技术被称为“网页伪装”，这项技术能让同一个网址呈现出完全不同的两副面孔。当谷歌的审核人员或安全机器人访问时，页面展示的是无害的普通内容——可能是某个知名品牌的官方介绍或正规产品页面。但当普通用户点击同一则广告时，他们会被立即跳转到精心设计的诈骗网站，这些网站专门窃取加密货币钱包信息或用户的登录凭证。

这种“看人下菜碟”的技术让恶意广告能在谷歌平台上存活更长时间，大大增加了诈骗的成功率。

精准筛选：99.4%的“观众”被拒之门外

研究人员发现，1Campaign平台具备极其精准的访客识别能力。系统会给每个点击广告的访客打上0到100的“欺诈分数”，自动屏蔽来自科技公司（如微软、谷歌、腾讯）的访问，同时也会拦截使用VPN的用户。

在一项名为“Blockbyblockchain”、针对bitcoinhorizon.pro网站的攻击活动中，数据令人震惊：在1676名访客中，系统屏蔽了99.4%的访问者，最终只让10名“真正有价值”的潜在受害者通过。这种精准筛选意味着绝大多数安全检查都被成功规避，只有真实用户才会落入陷阱。

一站式诈骗平台

更令人担忧的是，1Campaign的开发者DuppyMeister将这个平台打造成了一个“一站式诈骗解决方案”。平台不仅提供网页伪装技术，还包括：

- 实时Telegram通知，让攻击者随时监控流量

- 机器人防护脚本生成器，保护诈骗页面不被下架

- 谷歌广告启动助手，帮助创建“黑帽”和“白帽”搜索广告

- 支持英语和俄语的多语言界面

- 专门的技术支持服务

特别值得一提的是那个广告启动助手，它让攻击者可以无视谷歌的政策限制，随意使用任何文字来创建广告，这大大方便了冒充知名品牌的诈骗行为。

根据研究人员的追踪，这些诈骗活动的触角已经延伸至全球多个国家和地区，包括英国、美国、荷兰、中国和德国。攻击者通常利用合法的广告位投放恶意广告，这种被称为“恶意广告”的手法让诈骗活动披上了合法的外衣。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0uxzAzQCv1k9auQicicAgLeZM2rbXOHFcyaOSVJRqn4RV5xcxCcrX9IdYBkxbFjCR3SseiaUaib3qAAoNyJq5ZSQ98iaiatrBe9UwbU/640?wx_fmt=png&from=appmsg)

当一个诈骗广告被人力举报而下架时，攻击者往往已经完成了足够多的诈骗，造成了可观的经济损失。这种“打一枪换一个地方”的模式让传统的黑名单式防御效果有限。

如何保护自己

面对日益复杂的网络诈骗手段，普通用户需要提高警惕。研究人员建议：

1. 对搜索结果中的推广链接保持怀疑态度，尤其是那些看起来好得不真实的优惠

2. 点击广告后，仔细核对网页地址，不要被看似熟悉的品牌名称迷惑

3. 输入任何个人信息或进行加密货币交易前，再三确认网站的真实性

4. 使用可靠的网络安全工具，帮助识别潜在的欺诈网站

网络诈骗工具的“平民化”正成为一个令人担忧的趋势。1Campaign这样的平台让没有专业技术背景的人也能轻松发起复杂的网络诈骗，这无疑加大了普通用户识别骗局的难度。在这场永不停息的网络安全攻防战中，保持警惕永远是我们最重要的防线。

资讯来源：本文基于Varonis Threat Labs的安全研究报告及Hackread.com的相关报道整理撰写

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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