---
title: Deepseek是如何被黑掉的
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496994&idx=1&sn=d77c2e01b0dd8e2cb783fe7214e688c4&chksm=e8a5ff41dfd27657214d811c7635b0229bfd4e0dd9f949d59f1702d65efee83dd64fe76d58cb&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-02-01
fetch_date: 2025-10-06T20:38:10.624642
---

# Deepseek是如何被黑掉的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4XHD5Gz0ayY4l5aPwXoPUH1rpfhgqfTFC2zPzbicwymgUbdlCDUSe3TRiaypxYCgnrZe1C5c5jyWvQ/0?wx_fmt=jpeg)

# Deepseek是如何被黑掉的

Nagli

迪哥讲事

声明：文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任

## 正文

Deepseek的内部 ClickHouse数据库 泄露了,攻击者是怎么做到的,我们来看看:

1.从信息收集做起

```
subfinder -d deepseek.com
```

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4XHD5Gz0ayY4l5aPwXoPUHsjoP4drpGhiau6iapoPmkJCQocukibPRrdGCUHGTY9DgqKFBo5IaCIQibA/640?wx_fmt=png&from=appmsg)

如图所示,结果将有很多(这里仅仅只是展示,一般subfinder这个工具需要配置一些付费的api),我们需要从结果里面寻找到有效的子域名,这里的有效子域名是指具有IP地址的DNS记录，或者指向另一个资产的DNS记录

例如: sub1.example.com 的DNS记录是一个A记录，指向IP地址192.168.1.1。sub2.example.com 的DNS记录是一个CNAME记录，指向cdn.example.com，而cdn.example.com可能是一个CDN服务的域名。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4XHD5Gz0ayY4l5aPwXoPUHop60y9mFTTJeb2VJ4sMFOC2MS25pKaVbnQlqZRDYCagdSHwDuLbx4w/640?wx_fmt=png&from=appmsg)

通过DNS记录确认的子域名列表中，进一步筛选出那些“对外暴露且正在运行某种服务”的子域名

```
cat resolved | httpx -title -status-code -location -ip -cname -follow-redirects
```

通过之前的分析，已经得到了一个属于DeepSeek公司的公开可访问的HTTP服务器列表。这些服务器可以通过互联网访问，并且属于DeepSeek公司。

大多数服务器都是合法的，例如他们的聊天机器人（Chatbot）、API文档（API Docs）或状态网页服务器（status web server）。这些服务器提供了正常的服务，没有发现异常或可疑的情况。

有两个资产引起了注意:

http://oauth2callback.deepseek.com

http://dev.deepseek.com

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4XHD5Gz0ayY4l5aPwXoPUHWpEPMXVHPXibzlEFFWicOxSExI584BpZXxhd8cO6iaJcPYohyBH5jzSnQ/640?wx_fmt=png&from=appmsg)

使用nuclei在后台自动扫描已发现的服务器，检查是否存在HTTP和网络配置错误。工具会检查多种类型的配置问题和安全漏洞，验证方法准确，误报率低，且扫描过程无损，不会影响目标服务器的正常运行。这种自动化的扫描和配置检查有助于及时发现和修复潜在的安全问题，提高系统的安全性。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4XHD5Gz0ayY4l5aPwXoPUHjKuXxnaxbWMGaXVC3libRlWfTvTorBY3sEb3XYu4Y4fN1uNOtzLibxnw/640?wx_fmt=png&from=appmsg)

在访问目标服务器时，发现这些服务器正在运行ClickHouse数据库管理系统，这通常是一个内部使用的数据库系统。为了检查这些服务器是否存在安全问题，如未认证访问或配置错误，使用了Nuclei工具进行扫描。扫描结果显示，这些服务器确实对整个互联网公开，这意味着它们可能面临安全风险，因为ClickHouse通常不应该公开给外部访问。这种配置错误或未认证访问可能导致敏感数据泄露或被恶意利用。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4XHD5Gz0ayY4l5aPwXoPUHAibSTuRmD7qqKUos4OS2owSvBs9Mib37qfHum1cVEnXMpsCmic6tM7sDg/640?wx_fmt=png&from=appmsg)

在发现目标服务器运行ClickHouse数据库后，通过访问ClickHouse的HTTP API，我们能够直接查询MySQL数据库，发现数据泄露

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4XHD5Gz0ayY4l5aPwXoPUHZybIT0iakN9g4FmnVjx8y1UcV8ia11vBoesq891RVp6p3wo9hlNrAj0A/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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