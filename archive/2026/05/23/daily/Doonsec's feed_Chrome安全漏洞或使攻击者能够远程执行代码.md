---
title: Chrome安全漏洞或使攻击者能够远程执行代码
url: https://mp.weixin.qq.com/s/z4wthxePisDjY6eYFtHmZg
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:23.589869
---

# Chrome安全漏洞或使攻击者能够远程执行代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnuK84c9GmRoolfhwmG5mPOquplSCNp6Wtxl6jz1Lb76pNU6756iaWsrvCv2nicXFpxm4wzO9FbZkaktGiaPpG2gDRtcib9ib6Qrv8To/0?wx_fmt=jpeg)

# Chrome安全漏洞或使攻击者能够远程执行代码

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnsHPZRVEPRx7vmoeYcd8arFLzPicsby7A49EcIcDZT660bP1X1BibUicl3HYUUt7sShYEjb04Ir3kflYOoh3un0hVyOKxKsFBI9zo/640?wx_fmt=png&from=appmsg)

Google已为其Chrome浏览器发布关键安全更新，修复了多个可能允许攻击者在受影响系统上执行任意代码的安全漏洞。

此次更新现已面向全球用户推送，将Chrome升级至Windows和macOS平台的148.0.7778.178/179版本，以及Linux平台的148.0.7778.178版本。

根据官方Chrome Releases博客，本次更新共修复16个安全漏洞，包括多个高危及关键级别漏洞。

Google Chrome Security Flaws
两个最需警惕的漏洞CVE-2026-9111和CVE-2026-9110被评定为关键级别，可能被用于远程代码执行（RCE）。

最严重的漏洞CVE-2026-9111是WebRTC组件中的释放后重用（use-after-free）漏洞，该组件负责浏览器的实时通信功能。

释放后重用问题源于内存处理不当，攻击者可通过操作已释放的内存执行恶意代码。

另一关键漏洞CVE-2026-9110涉及浏览器用户界面（UI）的不当实现。尽管技术细节暂未公开，此类漏洞常可与其他漏洞组合以绕过安全防护。

这些漏洞的危险性在于，仅需诱导用户访问恶意网站或交互 crafted 网页内容即可远程触发。

Multiple High-Severity Bugs Identified
除关键漏洞外，Google还修复了多个影响核心组件的高危漏洞：

CVE-2026-9112: GPU中的释放后重用漏洞
CVE-2026-9113: GPU中的越界读取漏洞
CVE-2026-9114: QUIC协议中的释放后重用漏洞
CVE-2026-9115 & CVE-2026-9116: Service Workers中的策略执行问题
CVE-2026-9117: 图形渲染（GFX）中的类型混淆漏洞
CVE-2026-9119 & CVE-2026-9120: WebRTC中的内存破坏漏洞

根据利用条件，这些漏洞可能导致内存破坏、数据泄露或沙箱逃逸。值得注意的是，由于GPU和WebRTC组件的复杂性及其对不可信输入的暴露，它们仍是高频攻击目标。

本次更新还修复了多个中危漏洞，包括堆缓冲区溢出、越界读取和输入验证不足问题。尽管单个风险较低，但这些漏洞仍可能在多阶段攻击中被利用。

例如，CVE-2026-9124揭示了对不可信输入验证不足的问题，这是浏览器攻击链中的常见根本原因。

Google对发现这些漏洞的内部团队和外部研究人员予以致谢。高危漏洞的漏洞赏金最高达11,000美元，体现了社区对提升浏览器安全的持续参与。

该公司还指出，许多漏洞是通过AddressSanitizer、libFuzzer和控制流完整性（CFI）等高级模糊测试与内存安全工具检测出的。

Mitigation and User Recommendations
强烈建议用户立即更新Chrome至最新版本以降低潜在风险。更新正在逐步推送，但用户可通过以下路径手动检查：

Settings → About Chrome → Check for updates.

安全专家强调，延迟浏览器更新会增加遭受主动攻击的风险，尤其在补丁应用后漏洞细节公开时。

组织应确保终端设备及时完成补丁管理，并监控可能表明利用尝试的异常浏览器活动。

此次Chrome更新凸显了现代浏览器中内存安全漏洞的持续威胁。鉴于多个关键及高危漏洞可实现远程代码执行，无论是个人用户还是企业，快速修补仍是防御核心。

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