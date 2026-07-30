---
title: “系统正在维护” 影子资产实战思路
url: https://mp.weixin.qq.com/s/EL67pUvwu3c8fGvDIORb8g
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:50:00.840768
---

# “系统正在维护” 影子资产实战思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a3etiafIAYXGopOtacCKEDiaugjKlzZKI2Tx7Xu5bwc2WC8VC5x3gpBaNwQbem83l2nHmSctTyBAnuQq64QsutTnqqwWLrd5ibwGWkMOnagNuo/0?wx_fmt=jpeg)

# “系统正在维护” 影子资产实战思路

渗透安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于知攻善防实验室
，作者ChinaRan404

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7LSjun9LZLJQ4y8GvA9EhrnwUspbsrm1D1VQbcW4zL4A/0)

**知攻善防实验室**
.

红蓝对抗，Web渗透测试，红队攻击，蓝队防守，内网渗透，漏洞分析，漏洞原理，开源 工具，社工钓鱼，网络安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXFic1icjl3SFllfbGSN8YscgJgIrUaKxy1DNFUApKlCrlkXj6Q2f9TCamib36eIR3aP8paPW1xhzLGM3yrbibuFXuicOsibVARpWBIV4/640?wx_fmt=gif&from=appmsg)

前言

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXF3UlCPGRHeKeDEslHphS5TWE5faPtszPlk1XIm9quY2uOWwx2YH6UfW1IBM5Xia8CMH3NswXfMMELuNDpZDdyMicODNXeR9v9IQ/640?wx_fmt=gif&from=appmsg)

在渗透测试/攻防演练场景，我们经常遇到“系统正在维护”这种页面。

这种页面一般区分成两种

1.WAF映射

2.本机 nginx 配置

3.单网页

大致分为这两种

为什么我突然想发这篇文章呢？最近在做一些政务相关的渗透的时候发现的

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXGcKiar9U8UvRPibdwTU4z6S3qiaCBLYg4fHphHBOX1WGhtfgz3ibq6cuV3sQSSTm7mteK4XMOV3LE1EFThCatbphB6p1sVPubGFjA/640?wx_fmt=gif&from=appmsg)

WAF 映射

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXG7bmNl2bQQrclZohTbbmFjiaiaLtqgrCLYSTTjKM9eDwIoibYDsQNOIUL5JibYe4Pvt0Nq1LqLYqKrx0CwK8Vd282iciaiaaOedD2DAk/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/a3etiafIAYXE2ianFP6uEl8yyu8UTTOs9hHsIq79pnE1ibZBdKqR1KoldeNq2J3DlI3fc8KpkhlBRZLmgvub32gqX6RxH7bQQo52iap6LIBY9Zs/640?wx_fmt=png&from=appmsg)

这个也是我们这篇文章想讲的

流量先过 WAF，WAF 映射了一个页面，显示该系统正在维护，但是只是 302 跳转或者各种方式，总之，只有在前端看到系统正在维护，你正常通过 curl、http requests 还是可以正常使用业务接口的。

这个是非常重要的，也就意味着，这个系统停掉了，但是没有完全停掉，业务还是在的。

那么也就意味着一个新的攻击面/影子资产

“已关停业务”->"前端展示不了"->"原因是走 WAF 映射过来的页面"->"curl url"->"原业务"

除了前端展示不出来，剩下的渗透思路是一样的。

在我现在所在的这个省某一个大厂业务的 WAF 是存在这么个逻辑漏洞的。

实战思路就是：AI 直接打或者人工 curl 分析

实战思路：

在我以往的工作流中，比如一场攻防，我要人工筛选一下高价值目标，大概率就会把这种 title“系统正在维护”页面刷掉了，实际上可以打的空间非常多，后续可以专门打一下这种资产，看看成果率，如果是上述描述的那种情况的话，我觉得应该会好打很多。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXERtYG7YxpYeIakT1pmhhErqNprExXygbID1Vy9yq7OHqw8icEID3p56SeibNiccXWMcY6UNg8qhopV657efkWO7fPe1ica4dwibGlo/640?wx_fmt=gif&from=appmsg)

nginx 配置

![](https://mmbiz.qpic.cn/mmbiz_gif/a3etiafIAYXG727Yq4ibCRHjJXHklOpe0rZ5e6yibkyofQwFTiblzkM0NYUf7l78ToibPHSiaR1UoCw5KTeIY8uiaPfT4SSMRB1DLwg97RDJia5YL0A/640?wx_fmt=gif&from=appmsg)

 这个一般 nginx 配置了/\* 一般是绕过不了的，我也没有遇到过这个场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXE83N7bjXkiawHSl2BeXOSpJia8YVHyXSgIupRlb8EY8IVEHRH7SnaMwrGwia5KibpUKJ0kMwwreTdNFFtiblhJlJRTHG7q0VWE1Wqw/640?wx_fmt=gif&from=appmsg)

单网页

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/a3etiafIAYXGZu1pcRFzsjAvBNZyrqD0LzHYSgSHLAK7Fo6RBCuEeTJAFQ1dnoF37O5b8pbvpA3lraRMlOJfYcxeWdq5ERJRria4WvaqaCUC8/640?wx_fmt=gif&from=appmsg)

非 MVC 架构的，比如传统脚本 php、asp、jsp 这些访问，大多数都直接认 index 文件的，如果开发者仅仅是改了 index 文件，实际上通过目录扫描，其他的攻击面还是在的。

MVC 情况，没遇到过。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pPVXCo8Wd8DHexWkmfu2sWvFlJjB3HicIsbaxyHrHh7cLgaFw6hmxkNLW2C11PibcqnF4n1IRLxRLribqfmgFKtvQ/0?wx_fmt=png)

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