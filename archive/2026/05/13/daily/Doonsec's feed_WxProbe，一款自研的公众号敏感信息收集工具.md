---
title: WxProbe，一款自研的公众号敏感信息收集工具
url: https://mp.weixin.qq.com/s/PmGYqI4rbRwbPGOWq7cCsw
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:01.904052
---

# WxProbe，一款自研的公众号敏感信息收集工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1E8ULvdwpfOClCCjJicH24E2SGrdaR5ibibE9ng7s5xc62TopVxmZeic9K2K0tcPxwPG3myKYgxyic1ElUZRibJyloHwjdSVS7H3Pr5FfkaP6VtB4/0?wx_fmt=jpeg)

# WxProbe，一款自研的公众号敏感信息收集工具

原创

仙草里没有草噜丶
仙草里没有草噜丶

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

此工具的灵感主要是源于一次北京红队金融项目，在公众号这块的信息收集实验比较少，要手动一个一个公众号去翻，特意写的一个工具

这个工具主要用于敏感信息收集工具，专注于微信公众号文章批量获取与 AI 智能分析。

通过 Token 登录微信公众平台，**批量抓取指定公众号发布的历史文章，利用 DeepSeek AI 识别手机号、身份证、邮箱、车牌号、密码等等敏感信息。**以及**公司关联信息，公司注册资金、统一信用代码，法定代表人，股东结构**等等信息（AI生成的结果，仅供参考）

> 白小羽
>
> 注：此工具仅限于学习使用，请勿用于非法用途，若造成不良后果，与工具开发者以及泷羽Sec安全团队无关，请自行承担相应的法律责任，此工具禁止逆向源码，一旦发现，后果自负，若需要源码二开，可以自行联系工具作者一次性买断（白菜价）。

## 技术架构

```
WxProbe
├── WeChatLogin          # Token + Cookie 登录管理
├── ArticleFetcher       # 文章列表获取 + 正文抓取
│   ├── scrapling        # headless 隐身模式（反爬）
│   └── requests         # 保底方案
├── SensitiveInfoAnalyzer
│   ├── _regex_scan      # 正则快速扫描（手机号/身份证/邮箱/IP等）
│   └── analyze_single   # DeepSeek AI 深度分析
├── WechatSogouAPI       # 搜狗微信搜索（可选）
└── ShadowEyeApp (UI)
    ├── 公众号情报 Tab
    ├── 搜狗搜索 Tab
    ├── URL 抓取 Tab
    └── 设置 / 导出
```

| 模块 | 功能 |
| --- | --- |
| 🔐 **公众号情报** | Token 一键登录 → 搜索公众号 → 多页爬取文章 → AI 分析 → 导出报告 |
| 🔎 **搜狗搜索** | 无需登录，直接搜索微信文章 → 一键抓取 → AI 分析敏感信息 |
| 📎 **URL 抓取** | 粘贴微信文章链接（单条/批量），抓取正文并用 AI 分析 |
| 🤖 **AI 分析** | DeepSeek + 正则双引擎：手机号、身份证、邮箱、IP、银行卡、密钥等 |

### 使用教程

打开微信公众平台扫码登录

![image-20260509143934747](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfN85bibZc3GDuNt0icCKvvP1VlGldE7JpVKeehZZEia3iauDYhtnvwm6xt0bQZ8GCSciaEKv0J8amQs9M4Fg7uLaMspntewRswCDicIM/640?wx_fmt=other&from=appmsg)

image-20260509143934747

登录后复制token

![image-20260509182545104](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPicRjYQoGOZ7H79v9NSOvdcuRwpiaQDwRV8iaBXsDNztCoa6gep77EicuQibYOBNV5O2dg0IVq4jbR19hLhu3YDTITISYIzT5MrdjE/640?wx_fmt=other&from=appmsg)

image-20260509182545104

复制cookie

![image-20260509180735598](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfN7vv9rH9SSuPQCmGw8icg26xrjEFnu7mw8aRE5wZG9WpHsiclHyEI3l5BPjSYmuZCSrUrtBkGgmadSnhgeOsVuW4R6sM3YFXuRs/640?wx_fmt=other&from=appmsg)

image-20260509180735598

复制到这上面来

![image-20260509182431402](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfNOzFvYjnKwkLy9x7LaC8FibiayRqxw0GiaAEWSuSJdHsM5UNTp6G99dGN218twqN6QrNW1hrZKXqqWWeThOvG6D6a5HiaHVc5AQ78/640?wx_fmt=other&from=appmsg)

image-20260509182431402

输入之后就能登录成功

![image-20260509182617642](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfPJibiaRtOibV0HJiaHw0VX4OurbHUZSlQUDViaAUgAFEs8kSCFQvYXFHAhsyQQlxdWaE4ZH2q06OiakFZ9XNzGNuG7Ga7wZPl8sQnqk/640?wx_fmt=other&from=appmsg)

image-20260509182617642

尝试搜索公众号

![image-20260509182646331](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfO416h26LRTjFt9p9YlTV0Tu8OdsPTMgs8iaiajjJM3Kr19c2Uw2kBDDMAOWpJynSXlGlqvyMbiaZR3H04QfIekT6dykAyfrGMxUs/640?wx_fmt=other&from=appmsg)

image-20260509182646331

默认是五页选择自己要爬取的公众号后点击爬取

![image-20260509182719211](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfMRo6ILOu1GVwRdqxfvELYDDJaHvhMiaMybRTvDKGjbdlDHywJrUJzBMDRdEMoTnvY847Sian9Ogt1Nz4dlUMKMv7PXkALICGfOU/640?wx_fmt=other&from=appmsg)

image-20260509182719211

刚开始是没有敏感信息的，需要手动点击是否进行AI分析，这里使用的AI是deepseek

![image-20260509182835739](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfOicEsrHMBF4A605bgB4Ej26VcT5XQqwzSCz8wgnCUC4PzcGtPAZJrhRLMLGp0VTl1XnIiccKUQcOMricUfOtic2f5cg3kJlZk7Nqo/640?wx_fmt=other&from=appmsg)

image-20260509182835739

需要在系统设置，设置自己的apikey和模型名称

![image-20260513172540921](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfP2tKbbLwwZbFs2jsxDrp3fxbz3G8m0Ub7k6r6OUgsaEFiasx484yse8asqq7fnV36Qv7MYVVWDImyRARTT500SLBce5ziaNxNHY/640?wx_fmt=other&from=appmsg)

image-20260513172540921

AI分析完成后，可以在敏感信息中看到常见的**手机号、身份证号、姓名、邮箱、地址、IP地址、银行卡号、网站链接/域名、密码/密钥/Token、组织机构代码、车牌号、QQ/微信号、其他PII**等等，对于公司信息会调出企业工商信息，比如**（注册资金，实缴资本、统一社会信用代码、注册时间等等工商信息，以及公司结构）**这对于公众号这块的信息来讲是非常的有用的

![image-20260513194050156](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMxu6u0psK8kkms2Ts8XEh59tKapr525EHpevrZjk2NGSKqkicKLlGw1IP2UjVjGAPuicDVm1Z4rcMW0YRiaASC9ehYSpsh8sDQiaU/640?wx_fmt=other&from=appmsg)

image-20260513194050156

中国债卷尝试

![image-20260513194139812](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfPNxzKPnhFOgJ8icXffFHL2QCIIvmib5y9dHiaJPxibQ7UbSARAALp3T99TibExibvNvlh1f1VjBBdKr7SINWkv5sRkRz7KCicuBcp7HQ/640?wx_fmt=other&from=appmsg)

image-20260513194139812

![image-20260513194315066](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMqkiciad8VowbTC4a3lY8y5oPZ5DiaJZIuHtmiaTVF5Sv6VuBZPaTfD29TRpaCfKOlLYo2NKecc6Dfl1DjVDNyVm2dQdODRkvZ7og/640?wx_fmt=other&from=appmsg)

image-20260513194315066

若您对结果不满意，可以导出功能，自行对数据进行分析

![image-20260509183800370](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfMyxU7r0xfiaZsrlBcYOtGCdXtT2qNzFxhiajhqBMY6qHAZEibPH6yGpwjwk0BpxUicFSF2QG1TGffINpRPPQ5ibHMzqRdj3R5fjPVk/640?wx_fmt=other&from=appmsg)

image-20260509183800370

2、信息收集部分，本工具已绕过搜狗基础反爬功能，您可以通过搜狗搜索引擎，搜索到微信公众号相关文章，利用AI进行敏感信息分析，和前面一样比如邮箱、手机号等等信息，为了稳定请不要频繁点击某一个功能，耐心等待工具执行（若数据量较大可能要等待10分钟、一小时），在此期间可以双击某一个文章查看文章详情

> 白小羽
>
> 注意：对于搜狗搜索引擎，单个文章建议请抓取一次即可，不要重复抓取，否则极易促发反爬。

![image-20260511215052744](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfPqkUqbSpEI04YGDmKCKXwkWeVOFAUxORTMxdLZ4ZEIsduFNOrqIEcLIzpDZr9C08ibMuI5JriaAwQNKaBCJTYZjhaKrpBbmibCZ4/640?wx_fmt=other&from=appmsg)

image-20260511215052744

![image-20260513152316128](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfOCnAvsBjGPDDEXeWb81yeicB7vibBSSJIFibkQTUicbJoibExC19caMvoclUIUJulQiap06AyOYfmAWiaibUVBSfNAnzZxelVbjOlqXwM/640?wx_fmt=other&from=appmsg)

image-20260513152316128

3、若您已经拥有了一定数量的公众号相关的URL，则可以使用URL抓取功能

![image-20260513152525644](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfNxO6GMTvlc1OB3XUg2LGsNI6HN4nBeVfO4cns9Ep7Viatw8BoKCIIXa3zKuBwUf9UzRo4J4BicNqKU2TQJWPicZvAarhSzzeIiaEU/640?wx_fmt=other&from=appmsg)

image-20260513152525644

例如

https://mp.weixin.qq.com/s/caVRY62bhNZm5Ri81oqUwg

https://mp.weixin.qq.com/s/hcB1m6tmDFfx9PA7rNzOZA

> 白小羽
>
> 注意：对于某号文章爬取，可全面绕过，稳定爬取，无需担心被拦截，但需要确保你已成功登录

![image-20260513154540630](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfN09Xc86EiaicTLrqM7kKWIDTu4nnnEic0cKS3hFFFF1x1PdH9ibskNFhqewKClHHVLf650uA7bkCXibf5Sg38EmpTfmPhaqicZ0Fveo/640?wx_fmt=other&from=appmsg)

image-20260513154540630

![image-20260513155756422](https://mmbiz.qpic.cn/mmbiz/1E8ULvdwpfM2Omt4xPOePd3ZBoXOiazvyLwdjCxdYOibqNFSWOdDzQftmMAZEWcfQXC1meZ1lWdnhsbKH9u9ImH3seicOkMRrv0ovqAutjdicm4/640?wx_fmt=other&from=appmsg)

image-20260513155756422

工具获取方式，扫描下方二维码加入freebuf知识大陆即可获取，券后仅需79

此时加入，可获取**香港免备案服务器**一个月使用权**（配置：4核心 4GB 硬盘：40G  带宽：10Mbps 峰值 流量：无流量限制）**，限时到**2026年6月1日之前**，之后不再赠送

[![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfPicAs0ar4ic22R4G7Xdlerm5QT3ibiaI4F5pkbcnnBkbFJmvmFsxiaewFK0PUVtqTIATstIS6Naef28NpomG52q6Nj1hj6GibeM1XkY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247502572&idx=1&sn=42a9853381a099fc7c074230c39824a3&scene=21#wechat_redirect)

> 白小羽
>
> 注：服务器使用需要实名，介意的话可以忽略赠品

![海报 (1)](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfN2rVibKNLec9tlBh8DFBkI62yYL1kSPWCWby96UrGQABQiaWcPM5MLYx5MvibKnw5OkucyUib5XhxODc6GvcuK4FNksLIianKV6GkM/640?wx_fmt=other&from=appmsg)

## 常见问题

**Q: 搜狗搜索提示验证码拦截？** 先执行一次搜索（让系统建立 session），搜索成功后 session 会缓存，后续抓取会复用该 session。

**Q: URL 抓取按钮一直"分析中"？** 需要先在「公众号情报」tab 完成登录。如果已登录仍卡住，可能是网络问题，2 分钟超时后会自动恢复。

**Q: 分析结果为空或"未获取到正文"？** scrapling 可能被反爬。程序会自动降级到 requests + BeautifulSoup 保底方案。如仍失败，检查文章链接是否有效。

github地址：https://github.com/baibaixiaoyu2024/WxProbe/

原文地址：https://longyusec.com/longyushoulu/1181/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWG2YeKibdOsJywysp4aTnLsvRodjpEhfhbPXvica7364Dn6VO7Ybtpma6IUaFciaiaZG8Sr9yJ2Dwuv1Q/0?wx_fmt=png)

泷羽Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWG2YeKibdOsJywysp4aTnLsvRodjpEhfhbPXvica7364Dn6VO7Ybtpma6IUaFciaiaZG8Sr9yJ2Dwuv1Q/0?wx_fmt=png)

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