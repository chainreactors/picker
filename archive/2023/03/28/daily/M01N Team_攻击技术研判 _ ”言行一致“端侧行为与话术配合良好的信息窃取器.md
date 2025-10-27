---
title: 攻击技术研判 | ”言行一致“端侧行为与话术配合良好的信息窃取器
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247491116&idx=1&sn=903090b6d787362268eb887ae7eeea91&chksm=c187de3df6f0572b205d4f8c8cb3fb6b7a8046f2e11b5fd710583c0a3c8d3007b8a636054923&scene=58&subscene=0#rd
source: M01N Team
date: 2023-03-28
fetch_date: 2025-10-04T10:53:34.721139
---

# 攻击技术研判 | ”言行一致“端侧行为与话术配合良好的信息窃取器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYSKT7e5OKt5ozRt570BMNu9TnSDFoialgXnIkjEw069F8B2mKgRy9giayuFpP0djicJ9wtDGbk9GCkg/0?wx_fmt=jpeg)

# 攻击技术研判 | ”言行一致“端侧行为与话术配合良好的信息窃取器

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2Q8vWhzC8icpu7MpBm1WibBJbwUr8MGIx2NEMIVJN34jKQPFWOYlSbsyQ/640?wx_fmt=gif)

**情报背景**

近期SerHack的研究人员发布了针对基于知名信息窃取工具Redline的恶意钓鱼攻击活动的分析，攻击者以伪造的具备NFT资金收益的游戏促销活动针对目标群体实施精准钓鱼打击，并在其后的攻击活动中伪造游戏合法流程以规避检测，最终实现敏感信息窃取的目的。名为Redline的商业化信息窃取程序通常在暗网论坛等区域以廉价的订阅价格销售，受到以窃取用户凭据、加密钱包信息等为目的的攻击者的青睐。

|  |  |
| --- | --- |
| **组织名称** | Redline |
| **战术标签** | 打击突破、防御规避、信息收集 |
| **技术标签** | 行为模拟、Binary Padding |
| **情报来源** | https://serhack.me/articles/analysis-redline-based-malware/ |

**01** 攻击技术分析

**要点：端侧行为与钓鱼话术的良好配合**

攻击者在初始的钓鱼邮件与站点内容中充分伪装为某个付费游戏的促销信息，号称通过该游戏可获得价值巨大的限量NFT资产。这种话术构造精准命中部分对该话题感兴趣的目标用户。

钓鱼站点与载荷投递服务等攻击基础设施均采用了与被模仿对象相近的域名，在其后多流程的攻击活动中也运用一系列对抗技术增强自身隐蔽性。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2RV33WUcuhBskNpD57ELHnPnSpqIoOmUoKcZVlvmgb98ngwbzNdRumw/640?wx_fmt=png)

图1 伪造为游戏促销活动的信息窃取器攻击流程

在载荷特征与端侧攻击活动中配合该话术实施伪装是本次攻击活动的一大特点，文件属性等尽可能贴近其所伪造的合法游戏启动器。

值得注意的是后续载荷释放执行的路径中也另有玄机：该路径与合法Steam客户端下载游戏数据的位置保持一致，使得后续载荷拉取执行更加符合游戏的正常执行流程。

```
特殊的文件释放路径（与合法版本游戏数据存储位置保持一致）：%APPDATA%\InternetCache\EOSOverlay\BrowserCache\blob_storage\72034298-6c55-4cae-bde5-b013ff6304f8
```

除此之外，攻击者利用端侧产品为了保证文件扫描与云端查杀效率而放弃大文件扫描与上传分析的特性，使用Binary Padding（T1027.001）的技术手段在尾部加入NULL字节，加大文件体积以规避静态检测与在线沙箱上传分析。

简单可行的静态扫描与沙箱查杀对抗效果也许是尽管简单粗暴的Padding手段无法给人工分析带来实际阻碍，却依然在多个Redline相关的攻击事件中被使用的原因。

**02**总结

自带基本的防御规避效果的Redline等商业信息窃取器的应用，使得攻击者能够专注于攻击流程的伪造设计，保证钓鱼话术构建、基础设施架设以及端侧行为伪装的一致性。不仅做到了静态特征的高度相似，还通过对“游戏数据下载”的合法行为的拟态，使自身在行为分析角度也更具迷惑性。

模拟合法程序操作的“障眼法”与简单可行的反分析手段组合的攻击思路，也比较符合其仿冒游戏客户端实施信息窃取的意图。从防御角度思考，以“Binary Padding”这类易检测的高频利用对抗技术实施检测是一个比较好的切入点。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2wTDVYsFf9FNJP56G8Cxl5B1GEktNtw5flkVst4cQECW1DM4Dqk3cvQ/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2T9Uic9MJSpUKBf2V4EHuAzOX21vpicPNNWIhpySUndTN7HacSTcT7Szg/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2PFZdcAdicuypxZ4VGTmDoCO811RQP0iaDz4rsIIfABCwicTS0U5ViamxPg/640?wx_fmt=png)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[攻击技术研判 | 借助OneNote笔记进行MoTW规避新姿势](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247491074&idx=1&sn=500ab115fc9e491ddaa0bdf74709b1ec&chksm=c187de13f6f05705f211f1cce11ba8908ab5c888bcfdf0d646233782340af308fb1aa223c915&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2RcZcXMxCpthffA7q9Ta0KxrKsQMRdXVQX6H5CZAFqh79vlZ07lP2Hw/640?wx_fmt=png)

[攻击技术研判 | 使用蜂鸣器对抗沙箱检测技术](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490989&idx=1&sn=22346fc6a4586c666c2eb23478d3cd83&chksm=c187ddbcf6f054aa17b85b2d007c2949b5a606a19423365c3992e302e44ef40a4de28196a447&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2RcZcXMxCpthffA7q9Ta0KxrKsQMRdXVQX6H5CZAFqh79vlZ07lP2Hw/640?wx_fmt=png)

[攻击技术研判 | Earth Kitsune滥用vcruntime140.dll和Chrome扩展等实现持久化](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490905&idx=1&sn=2c1426495bfdc73b5ca85a0dfba899c6&chksm=c187dd48f6f0545e04c5a10a2a04126f7ff9671068053f09eb8cf50e9401c5fc30597b6f86a3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZsFc0Py1QuaicTZH8y7VsG2RcZcXMxCpthffA7q9Ta0KxrKsQMRdXVQX6H5CZAFqh79vlZ07lP2Hw/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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