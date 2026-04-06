---
title: 【红队】一个高性能、准确的命令行指纹识别工具
url: https://mp.weixin.qq.com/s/DMLrjxI3cn_cEGQ-TM7Klg
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:39:18.509170
---

# 【红队】一个高性能、准确的命令行指纹识别工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k2PJfskYECnRBwWbzWibyia6ibSrGNPcF4IErc464R5bkwUsP1ojbFqn9sB5bNzhoNicnakP7hZyUFylicoEPRkhMRPTKyqhNuKhkvd74oImI7kw/0?wx_fmt=jpeg)

# 【红队】一个高性能、准确的命令行指纹识别工具

HackAllSec
HackAllSec

贝雷帽SEC

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**免责声明**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/HVNK6rZ71oofHnCicjcYq2y5pSeBUgibJg8K4djZgn6iaWb6NGmqxIhX2oPlRmGe6Yk0xBODwnibFF8XCjxhEV3K7w/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic)

本公众号所提供的文字和信息仅供学习和研究使用，请读者自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具介绍**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**hfinger** 是一个**高性能**、**准确**的命令行指纹识别工具，用于红队打点时快速准确识别指定目标的 Web 框架、CDN 和 CMS 等信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k2PJfskYECk0EicDP28Bjxia1IG1v6nzaeMX6vMV5LmY7p0sX2eugC34S6ZIetkia8Kt6NaxdmDLQagEsuKygKX0k97xLIQcAySRvSgWJ59cE8/640?wx_fmt=png&from=appmsg)

特性

* 高性能、精准的识别目标
* 支持同一目标匹配多个框架指纹识别
* 支持主动模式和被动模式
* 支持根据错误页识别
* 根据响应 Header、body 和 title 与 finger.json 中定义的指纹进行匹配
* finger.json支持自定义匹配逻辑
* 支持随机UA头
* 支持多线程，线程数可通过 -t 参数调整
* 支持代理，通过 -p 参数指定代理
* 实时输出匹配结果，匹配到则使用绿色输出，未匹配到则使用白色输出
* 支持 JSON、XML 和 XLSX 格式的输出
* 支持HTTP/2和HTTP/1
* 支持标准HTTPS和国密HTTPS
* 由于Fofa的部分icon\_hash和Mmh3Hash32的计算结果不一致，新增了icon\_hash计算工具

指纹库

* 收录的产品、Web框架和CMS总数（根据不同cms的值统计，名称相同的指纹只记1次）：**1177**
* 指纹总数量（数量小的原因是已将指纹进行优化和合并，对同一资产的指纹进行合并）：**1412**
* 指纹库中的规则区分大小写，自定义添加指纹是需要注意

兵在精而不在多，指纹数量也一样，看数量意义不大，关键看可以识别的产品、Web框架和CMS数量。

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具使用**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
git clone https://github.com/HackAllSec/hfinger.gitcd hfingergo build
```

```
 █████         ██████   ███▒▒███         ███▒▒███ ▒▒▒ ▒███████    ▒███ ▒▒▒  ████  ████████    ███████  ██████  ████████ ▒███▒▒███  ███████   ▒▒███ ▒▒███▒▒███  ███▒▒███ ███▒▒███▒▒███▒▒███ ▒███ ▒███ ▒▒▒███▒     ▒███  ▒███ ▒███ ▒███ ▒███▒███████  ▒███ ▒▒▒ ▒███ ▒███   ▒███      ▒███  ▒███ ▒███ ▒███ ▒███▒███▒▒▒   ▒███ ████ █████  █████     █████ ████ █████▒▒███████▒▒██████  █████▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒███ ▒▒▒▒▒▒  ▒▒▒▒▒                                        ███ ▒███                                       ▒▒██████                                        ▒▒▒▒▒▒                     By:Hack All Sec
A high-performance command-line tool for web framework and CMS fingerprinting
Usage:  hfinger [flags]
Flags:  -f, --file string          Read assets from local files for fingerprint recognition, with one target per line  -h, --help                 help for hfinger  -l, --listen string        Using a proxy resource collector to retrieve targets, example: 127.0.0.1:6789  -j, --output-json string   Output all results to a JSON file  -s, --output-xlsx string   Output all results to a Excel file  -x, --output-xml string    Output all results to a XML file  -p, --proxy string         Specify the proxy for accessing the target, supporting HTTP and SOCKS, example: http://127.0.0.1:8080  -t, --thread int           Number of fingerprint recognition threads (default 100)      --update               Update fingerprint database      --upgrade              Upgrade to the latest version  -u, --url string           Specify the recognized target,example: https://www.example.com  -v, --version              Display the current version of the tool
```

```
单个 URL 识别:hfinger -u https://www.hackall.cn从文件中读取目标并识别（每行一个url，需要添加协议，如http或https）:hfinger -f targets.txt指定代理:hfinger -u https://www.hackall.cn -p http://127.0.0.1:8080输出为 JSON 格式:hfinger -u https://www.hackall.cn -j output.json输出为 XML 格式:hfinger -u https://www.hackall.cn -x output.xml输出为 XLSX 格式:hfinger -u https://www.hackall.cn -s output.xlsx
```

**下载链接**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
项目地址：https://github.com/HackAllSec/hfinger
```

End

“点赞、在看与分享都是莫大的支持”

**工具精选**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

[【红队】一款安全测试工具集——Onyx](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494121&idx=1&sn=8675cf1677352620a57d68ff9f0b0686&scene=21#wechat_redirect)

[【红队】一款 AI 原生安全测试平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494139&idx=1&sn=5d8a98e0d0cb700c124aeaecae595d4c&scene=21#wechat_redirect)

[【红队】Webshell 管理与后渗透平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494098&idx=1&sn=cb7bc8f3cc7f59e6f80f4b56e7d4c1f9&scene=21#wechat_redirect)

[【红队】BProxy - 多级 SOCKS5 代理工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494084&idx=1&sn=dbc658a17e6ddc0dcd7c7857c841478a&scene=21#wechat_redirect)

[【红队】攻击面管理平台 (ASM)](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494076&idx=1&sn=e9c2ff60ccd065dc223c71042515268d&scene=21#wechat_redirect)

[【红队】ParrotOS 7.0 正式发布 代号：Echo](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494038&idx=1&sn=243e1105a439eb986fdc34534e6a8d19&scene=21#wechat_redirect)

[【红队】一款专为红队打造的主动资产指纹识别工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493898&idx=1&sn=3e395ade15061739c89f5d0a13645af4&scene=21#wechat_redirect)

[【蓝队】SamWaf开源轻量级网站防火墙](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493939&idx=1&sn=e56702a24dcae461024668aaea6aced3&scene=21#wechat_redirect)

[[蓝队] FastMonitor - 网络流量监控与威胁检测工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493925&idx=1&sn=a952c400c3ee63c8401ff57692745dd1&scene=21#wechat_redirect)

[【蓝队】漏洞全生命周期管理平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493803&idx=1&sn=10daa12b5a3523bf4a1ecc665890f917&scene=21#wechat_redirect)

[【蓝队】蓝队Ark神器 OpenArk v1.5.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493788&idx=1&sn=91a31e2d507cb9e0111c19dac98b315e&scene=21#wechat_redirect)

[【红队】矛·盾 武器库 v3.2](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493701&idx=2&sn=9cf7e304fee21328bac6d9bd97b81183&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/pM2klgicgT5dylTzXyrXBmex6dlAsZ0QJOQdzqcw2HpC49rnL0dTHNsWsOze4QmRYN7fPRoLdVK5MXs0DXtOvZw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

贝雷帽SEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

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