---
title: Chrome紧急发布安全更新，修复多个高危远程代码执行漏洞
url: https://mp.weixin.qq.com/s/avzLG4iOHfRN-f1IF1UpvA
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:04:57.322734
---

# Chrome紧急发布安全更新，修复多个高危远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnuedjrQfa4baXicxgD4jG85mhHSYvF1S7XW6TJl8ic5tqnxnopOia4cxZCCRwSojRmyS1No8BYLicDALA2mKRKmcRYReKdVZnicOfdI/0?wx_fmt=jpeg)

# Chrome紧急发布安全更新，修复多个高危远程代码执行漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnvdRsaSuSbZMrdjzes3IM0BWNvNEBEYOJIT12mMv2PtJkQgoPWe5wERSnJ7WK0hMLXCFO4Dbmt7C9YA1mchhhWJkO4op4XQEyk/640?wx_fmt=jpeg&from=appmsg)

Google已向Windows、Mac和Linux系统的稳定版Chrome发布Chrome 145更新，修复了11个安全漏洞，这些漏洞可能允许攻击者在受影响系统上执行恶意代码。

该更新于2026年2月10日宣布，将在未来几天和几周内逐步推出。

**关键安全修复**

此次更新修复了多个高严重性漏洞，对用户构成重大风险。

最严重的漏洞是CVE-2026-2313，这是一个CSS中的使用后释放(use-after-free)漏洞，为研究人员赢得了8,000美元奖励。

此类漏洞允许攻击者通过访问已释放内存执行任意代码。

Google内部安全团队还识别出另外两个高严重性问题。

CVE-2026-2314涉及编解码器(Codecs)中的堆缓冲区溢出，而CVE-2026-2315则解决了WebGPU中的不当实现问题。

| CVE ID | 严重程度 | 漏洞类型 | 报告者 |
| --- | --- | --- | --- |
| CVE-2026-2313 | 高 | 使用后释放 | Han Zheng (HexHive), Wenhao Fang (University of St. Andrews), Qinying Wang (HexHive) |
| CVE-2026-2314 | 高 | 堆缓冲区溢出 | Google |
| CVE-2026-2315 | 高 | 不当实现 | Google |
| CVE-2026-2316 | 中 | 策略执行不足 | Luan Herrera (@lbherrera\_) |
| CVE-2026-2317 | 中 | 不当实现 | Brendan Draper |
| CVE-2026-2318 | 中 | 不当实现 | Shaheen Fazim |
| CVE-2026-2319 | 中 | 竞态条件 | Anonymous |
| CVE-2026-2320 | 中 | 不当实现 | Alesandro Ortiz |
| CVE-2026-2321 | 中 | 使用后释放 | Google |
| CVE-2026-2322 | 低 | 不当实现 | Robbe Van Roey (PinkDraconian) |
| CVE-2026-2323 | 低 | 不当实现 | Hafiizh |

如果成功利用，这两个漏洞都可能导致远程代码执行。

此次更新还解决了影响Chrome各个组件的六个中等严重性漏洞。

CVE-2026-2316由安全研究员Luan Herrera发现，解决了Frames中的策略执行不足问题，并获得了5,000美元奖励。

其他中等严重性修复针对Animation、PictureInPicture、DevTools、File input和Ozone组件中的问题。

还修复了两个影响File input和Downloads的低严重性漏洞(CVE-2026-2322和CVE-2026-2323)，研究人员分别获得了1,000美元和500美元奖励。

Linux用户现在可使用Chrome 145.0.7632.45，而Windows和Mac用户将收到145.0.7632.45或145.0.7632.46版本。

此次更新包含多项功能改进和修复，完整变更日志可通过Chromium仓库获取。

公司对详细漏洞信息实施严格访问控制，直至大多数用户完成更新。

用户应立即通过导航至设置 > 关于Chrome来更新Chrome，浏览器将自动检查并安装最新版本。

鉴于修复漏洞的严重性，特别是允许代码执行的漏洞，及时更新对维护系统安全至关重要。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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