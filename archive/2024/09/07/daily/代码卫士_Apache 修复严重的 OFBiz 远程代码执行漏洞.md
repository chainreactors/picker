---
title: Apache 修复严重的 OFBiz 远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520714&idx=2&sn=a3784b5b2245f1449edaefa3064d676f&chksm=ea94a0a0dde329b6ca2b17012b7eb003867fd983c6abcc5e7fde821968dec1ea86592860496c&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-07
fetch_date: 2025-10-06T18:28:28.303026
---

# Apache 修复严重的 OFBiz 远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRZ9z4nZmPRJKEtGUFf6J7BFPLcyWDRQbUdfiaDiafyzbdNswKhicr7BnhhIABlj2PeB3nIkIdC5NXgw/0?wx_fmt=jpeg)

# Apache 修复严重的 OFBiz 远程代码执行漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Apache 修复了 OFBiz 软件中的一个严重漏洞，可导致攻击者在易受攻击的 Linux 和 Windows 服务器上执行任意代码。**

OFBiz 是一款客户关系管理 (CRM) 和企业资源规划 (ERP) 商业应用套件，可被用于开发 web 应用的基于Java 的web 框架。该漏洞的编号是CVE-2024-45159，由 Rapid7 安全研究员发现，是由一个强制浏览弱点造成的远程代码执行漏洞，该弱点可将受限制的路径暴露于未认证直接请求攻击。

安全研究员 Ryan Emmons 在本周四的一份报告中提到，“无有效凭据的攻击者可利用 web 应用中缺失的视图授权检查，在服务器上执行任意代码。”Apache 安全团队在18.12.16版本中增加了授权检查，从而修复了该漏洞。建议 OFBiz 用户尽快升级安装以拦截潜在攻击活动。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRZ9z4nZmPRJKEtGUFf6J7BhAHuGJ1p4F863ksrNf7hWBq1iaUhet1upUiadosQkmm8oFjibue6t65Wg/640?wx_fmt=gif&from=appmsg)

**此前的安全补丁遭绕过**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRZ9z4nZmPRJKEtGUFf6J7B9u7E96jxFebfB3OukiahyzibXkkw7dQp6rsJQpSfibqOntlxQB9hPIVZg/640?wx_fmt=png&from=appmsg)

正如 Emmons 今天进一步解释的那样，CVE-2024-45159是对其它三个 OFBiz 漏洞补丁的绕过，这三个漏洞早在今年年初就已修复，它们是CVE-2024-32113、CVE-2024-36104和CVE-2024-38856。

Emmons 表示，“从分析来看，三个漏洞实际上是由同一个根原因引发的同样的漏洞。”所有这三个漏洞都是由控制器-视图映射分段问题造成的，该问题可导致攻击者执行代码或SQL查询，并在未认证的前提下实现远程代码执行。

8月初，CISA提醒称，5月修复的CVE-2024-32113正在遭利用，而距离 SonicWall 研究员发布CVE-2024-38856预认证RCE漏洞的详情才过去几天。CISA还将另外两个漏洞纳入必修清单，要求联邦机构在三周内按照2021年11月发布的BOD22-01指令将其修复。尽管BOD22-01仅适用于联邦民事行政部门(FCEB)，但CISA 督促所有组织机构优先修复这些漏洞，以阻止针对其网络的攻击。12月，攻击者开始利用另外一个OFBiz 预认证RCE漏洞CVE-2023-49070来查找易受攻击的 Confluence 服务器。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[【已复现】Apache OFBiz 授权不当致代码执行漏洞(CVE-2024-38856)安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=2&sn=db306ee3ac03c2a6708b7ae1cc72beaf&chksm=ea94a124dde32832c4479a4e205381dc87f02c98b62b21ceb6a18b70624d029f055e06ba57b2&scene=21#wechat_redirect)

[Apache 修复 Apache HTTP Server 中的源代码泄露漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520009&idx=1&sn=b958a0460ffa3e890f8c189660f04487&chksm=ea94be63dde337752a7dace28761adae32e92abbff78ddbb4dba723691c1d4eb489dd3e5deb2&scene=21#wechat_redirect)

[【已复现】Apache OFBiz 路径遍历漏洞(CVE-2024-36104)安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519685&idx=5&sn=cd7840386d236e97bc419b0a943f9d25&chksm=ea94bcafdde335b99fff79a2689e78cb78922997a12f87792bff03a1861af54f7ec49cf32f44&scene=21#wechat_redirect)

[Apache 项目中存在依赖混淆漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519338&idx=2&sn=c65a447c216d55afbb9483c48c34f453&chksm=ea94bd00dde334161df74aa1e15e2b728e866bddfe2a1e21bfb5e44dfcf65213634e19fe8ad7&scene=21#wechat_redirect)

[【已复现】Apache OFBiz 远程代码执行漏洞(CVE-2023-51467)安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518558&idx=1&sn=f0c9d4e2fed90fb991a8eb33bf83c83d&chksm=ea94b834dde331220ccaaf9b38a24400569f89b94484b4d335ad53352d52be4580d114ba1276&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/apache-fixes-critical-ofbiz-remote-code-execution-vulnerability/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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