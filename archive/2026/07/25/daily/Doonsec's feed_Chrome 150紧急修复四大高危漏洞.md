---
title: Chrome 150紧急修复四大高危漏洞
url: https://mp.weixin.qq.com/s/vuQ5d_37WtyD0Gkf7-mdhg
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:21:47.927444
---

# Chrome 150紧急修复四大高危漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnvmV13vVL9Z0ica2iaa4C5zUjxkXbTPMiaWpK9ibd4fCquRbibI4KnptX7msWcFTr8ic02lrhBoF7hFBFJibqokrKUuETawLKEOcyARV8/0?wx_fmt=jpeg)

# Chrome 150紧急修复四大高危漏洞

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnsbNHdTaoH9InRichpcF71yopllWKichyohriaHDZ7WxWkafJnR2wS18v9GqFAicy4nOOtIEsxUY7M08IhKTbZibTibiald9wK7cWN7t0/640?wx_fmt=png&from=appmsg)

谷歌Chrome 150.0.7871.186版本已修复四个影响核心组件（Codecs、WebMCP、Blink及Input）的高危漏洞。

尽管谷歌未发现这些漏洞正被 actively exploited（主动利用）的证据，但公司限制了技术漏洞报告及相关信息的公开访问权限，直至大多数Chrome用户完成更新。此举是行业标准实践，旨在降低漏洞在广泛补丁部署前被武器化的风险。

Google Chrome 150 Update

最严重的漏洞为CVE-2026-16807，属于Chrome Codecs组件中的越界写入（out-of-bounds write）漏洞，由谷歌内部于2026年5月30日报告。此类漏洞发生时，软件会向内存缓冲区边界外写入数据。在浏览器环境中，此类内存破坏问题可能导致应用崩溃，并在特定条件下被攻击者利用，在浏览器进程中执行恶意代码。

Chrome 150.0.7871.186版本同时修复了三个释放后重用（use-after-free）漏洞：

CVE-2026-16806 影响WebMCP组件，谷歌于2026年6月10日报告；

CVE-2026-16805 位于浏览器渲染引擎Blink中，报告时间为6月12日；

CVE-2026-16804 涉及Input组件，报告时间为6月16日。

释放后重用漏洞源于软件在内存释放后仍继续访问该区域，攻击者可能借此篡改程序行为或触发内存破坏。Blink组件的漏洞尤为关键，因其负责处理网页内容并管理页面、脚本与渲染功能的交互。而媒体编解码器或输入处理功能的缺陷，则可能通过恶意构造的网页内容触发，具体取决于漏洞利用所需的代码路径与条件。目前谷歌尚未公开攻击向量、概念验证细节或可利用条件。

谷歌安全公告中未提及外部研究人员奖励，表明这些漏洞由内部发现。公司特别致谢其安全工程团队及自动化测试技术，包括AddressSanitizer、MemorySanitizer、UndefinedBehaviorSanitizer、控制流完整性（CFI）、libFuzzer和AFL。这些工具在Chrome开发与测试阶段可精准识别不安全内存操作、未定义行为及代码流缺陷。

可通过以下路径验证Chrome版本：点击浏览器菜单→帮助→关于Google Chrome。此操作将触发更新检查，并在必要时提示重启浏览器。处理敏感数据或处于高风险环境的系统应优先通过受管更新策略部署补丁。用户需注意：下载补丁后必须重启Chrome，否则修复程序无法生效。

Chrome 150.0.7871.186的完整更新日志可通过Chromium源代码仓库获取。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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