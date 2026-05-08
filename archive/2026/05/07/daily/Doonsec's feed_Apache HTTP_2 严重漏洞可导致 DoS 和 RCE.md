---
title: Apache HTTP/2 严重漏洞可导致 DoS 和 RCE
url: https://mp.weixin.qq.com/s/L3-qQ9PyEz094ffMSVN1Hw
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:53:33.555519
---

# Apache HTTP/2 严重漏洞可导致 DoS 和 RCE

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfVxibmFWvP5K4xQW1fLkL6EeuZL0vHdkkxa3cmw97A27o3ld1C4FIibn8wZO92W98XYwTcFBfqacB7cBoqdbhS7icqCAwuZkgwFiac/0?wx_fmt=jpeg)

# Apache HTTP/2 严重漏洞可导致 DoS 和 RCE

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Apache****软件基金会 (ASF) 发布安全更新，修复了位于 HTTP Server 中的多个漏洞，其中一个严重漏洞（CVE-2026-23918，CVSS 8.8）可能导致远程代码执行 (RCE) 后果。**

该漏洞是位于 HTTP/2 协议处理中的“双重释放且可能是RCE” 的漏洞，影响 Apache HTTP Server 2.4.66版本，已在2.4.67中修复。Striga.ai 公司的联合创始人 Bartlomiej Dmitruk 和 ISEC.pl 公司的研究员 Stanislaw Strzalkowski 发现并报送了该漏洞。

Dmitruk 评论称，该漏洞可用于实现拒绝服务 (DoS) 和 RCE，属于严重级别。他还详细解释称，“CVE-2026-23918是 Apache httpd 2.4.66 中 mod\_http2 模块的一个双重释放漏洞，具体位于 h2\_mplx.c 的流清理路径中。当客户端在复用器尚未注册该流的情况下，向同一个 HTTP/2 流发送一个 HEADERS 帧，并紧接着发送一个带有非零错误码的 RST\_STREAM 帧时，便会触发该漏洞。此时，两个 nghttp2 回调函数会依次触发：首先是处理 RST 帧的 on\_frame\_recv\_cb，然后是处理关闭事件的 on\_stream\_close\_cb。这两个回调最终都会调用 h2\_mplx\_c1\_client\_rst –> m\_stream\_cleanup，导致同一个 h2\_stream 指针被两次加入到 spurge 清理数组中。随后，当 c1\_purge\_streams 遍历 spurge 并对每个条目调用 h2\_stream\_destroy  –> apr\_pool\_destroy 时，第二次调用的内存区域已经被释放，从而引发双重释放。”

Dmitruk 补充道，DoS 攻击非常容易实现，适用于任何默认部署了 mod\_http2 且使用多线程 MPM 的服务器；而 RCE 路径要求 Apache 可移植运行时（APR）使用 mmap 分配器，这在基于 Debian 的系统以及官方 httpd Docker 镜像中是默认配置。

Dmitruk进一步解释称：第一种后果是拒绝服务，手段非常简单：只需一个 TCP 连接、两个帧，无需认证、无需特殊头部、无需特定 URL，工作进程就会崩溃。Apache 会重启该进程，但在崩溃工作进程上的所有请求都会丢失，只要攻击者持续发送数据包，这种模式就可以一直维持下去。第二种后果是远程代码执行（RCE），且研究员已经在 x86\_64 架构上构建了一个可用的概念验证（PoC）。利用链通过 mmap 复用方式在已释放的虚拟地址上放置一个伪造的 h2\_stream 结构体，将其内存池清理函数指向 system()，并利用 Apache 的记分板内存作为伪造结构体和命令字符串的稳定容器。

记分板在服务器的整个生命周期内位于固定地址，即使启用了 ASLR 也是如此，这正是 RCE 利用路径具备可行性的原因。通常的注意事项依然适用：实际利用需要信息泄露来获取 system() 的地址以及记分板的偏移量，并且堆喷射具有概率性，但在实验室条件下，数分钟内即可实现代码执行。

Dmitruk 还指出，MPM prefork 模式不受该漏洞影响。不过，他警告称漏洞的攻击面很大，因为 mod\_http2 包含在默认构建中，且 HTTP/2 在生产环境中被广泛启用。鉴于该漏洞的严重性，建议用户应用最新修复补丁以获得最佳防护措施。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Apache Tomcat 紧急修复多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525768&idx=1&sn=1c34f092d86b657532a27c79a93f83a3&scene=21#wechat_redirect)

[已存在13年的Apache ActiveMQ 严重漏洞可用于远程执行命令](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525686&idx=1&sn=51e7e391e06000c6fad494187241de39&scene=21#wechat_redirect)

[Apache Syncope 漏洞可用于劫持用户会话](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525048&idx=2&sn=58b797888d5027994282725ccb9f23de&scene=21#wechat_redirect)

[Apache Struts 2 严重 XXE 漏洞可用于窃取敏感数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524857&idx=1&sn=7d98b989a61c9b25103ccef5b0524560&scene=21#wechat_redirect)

[Apache StreamPipes 严重漏洞可用于获取管理员权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524778&idx=2&sn=17e6675d731950fb6f61f841bb161ef5&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/05/critical-apache-http2-flaw-cve-2026.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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