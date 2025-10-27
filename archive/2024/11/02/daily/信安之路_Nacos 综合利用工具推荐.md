---
title: Nacos 综合利用工具推荐
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247499648&idx=1&sn=e6b64c5c0789c719e6a3b6b78f7af344&chksm=ec1dcfa8db6a46be99de77e2ff41fc59ca5f1d882b5a50fe6eb2d23763e759aabd85d179b1af&scene=58&subscene=0#rd
source: 信安之路
date: 2024-11-02
fetch_date: 2025-10-06T19:17:32.369377
---

# Nacos 综合利用工具推荐

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfelgSEN5mSsibtoBZXTUuh0lzy0eeiccVLJkM2ld8GmaNm9fQFQOnRhptOeZUIPJH6wuvZP48HEMrzA/0?wx_fmt=jpeg)

# Nacos 综合利用工具推荐

xazlsec

信安之路

Nacos `/nɑ:kəʊs/` 是 Dynamic Naming and Configuration Service的首字母简称，一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台。

Nacos 致力于帮助您发现、配置和管理微服务。Nacos 提供了一组简单易用的特性集，帮助您快速实现动态服务发现、服务配置、服务元数据及流量管理。

Nacos 帮助您更敏捷和容易地构建、交付和管理微服务平台。 Nacos 是构建以“服务”为中心的现代应用架构 (例如微服务范式、云原生范式) 的服务基础设施。

指纹识别方式：`title="NACOS" && body="nacos-logo.png"`

Nacos 综合检测利用工具推荐：NacosExploit

下载地址：https://github.com/h0ny/NacosExploit

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelgSEN5mSsibtoBZXTUuh0lZadqh8ZZI529Pz8bpJ6Z2gia4tGRZ9NLQTgoaZb51V0QSQXIYWZDUeg/640?wx_fmt=png&from=appmsg)

支持检测的漏洞列表：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelgSEN5mSsibtoBZXTUuh0lwIph1Gxvq55JuzYUZTtnURsM40bujOicvSWpdwzIfqNcTsrYNibe676w/640?wx_fmt=png&from=appmsg)

可以基于认证绕过漏洞导出配置文件，其中包含很多敏感信息，比如数据库的链接地址和账号密码，如图：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelgSEN5mSsibtoBZXTUuh0lzEQiacYKpiaoBa4v4Jrb4Hg454g4fGfkHMYlOpbhl3FV5FzQkAXptiafw/640?wx_fmt=png&from=appmsg)

如果存在反序列化漏洞或者未授权 SQL 语句执行，那么可以利用该漏洞直接打入内存马，从而接管整个服务器：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelgSEN5mSsibtoBZXTUuh0l68wSibY3LI3dRCara6fr6cJC7xcV1cufPibrkicdiaQbicU3cdZhpKSd8Tw/640?wx_fmt=png&from=appmsg)

### 安全建议

1、加强系统和网络的访问控制，修改防火墙策略，不将非必要服务暴露于公网；

2、升级系统到最新版，以防历史漏洞造成不必要的损失

### 一键检测 Nacos 历史漏洞

信安之路 POC 系统配套工具 xazlscan 可以一键识别系统类型，并自动适配 POC 进行漏洞检测，只需要输入目标，就能获得漏洞列表，傻瓜式、一键化实现漏洞发现：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfelgSEN5mSsibtoBZXTUuh0lfFYxkIgVT3Sm5ryjTSCdj9ZlYMic7NnPE2ss03Q15BoDubvEaVb89XA/640?wx_fmt=png&from=appmsg)

下载地址：https://github.com/myh0st/xazlscan

每个 POC 都有对应的文库地址，无需搜索相关资料，一步直达漏洞详情。

### 信安之路

成长平台：帮助小白入门信息安全

内部文库：自学安全更加体系化

POC系统：历史漏洞检测更高效智能

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfc1ibbG6mEdqV5Xpw0yu9UxtIoLlhiazxU4NakInEiam1mOnHHYw4pVq3nrrCc8tpnn5ictdhmNLUaHuA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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