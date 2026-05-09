---
title: (2)漏洞复现-Tomcat-upload \"幽灵比特位\"
url: https://mp.weixin.qq.com/s/Hq3bBSJrBVHPqS6Zj-D1QA
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:04:58.993023
---

# (2)漏洞复现-Tomcat-upload \"幽灵比特位\"

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AVZW8rmhibiaLDs2axmxwBBIggxBJsibfV0liabbSccmPibAdYKR68yRGUL8q95Zozt8n0uL4nnOM2rrWVZSP2yO5YialSAYY8Nic4WGw9MbjS5MCw/0?wx_fmt=jpeg)

# (2)漏洞复现-Tomcat-upload "幽灵比特位"

原创

FengXS0ne
FengXS0ne

Feng随心而安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**本文章仅供学习交流使用，文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途以及盈利等目的，否则后果自行承担。请尊重原创，相互学习。**

0x01: 介绍

前段时间爆出来java 的幽灵比特位（Ghost Bit）感觉挺有意思，刚好，阅读了一些公众号文章提到Tomcat 在文件上传中也存在这样的问题，但似乎都没有明显的复现，就去跟了一下，特此记录一下复现的过程。

0x02: 正文

前面的文章跟过Tomcat 在文件上传中一些手法，其中最核心的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AVZW8rmhibiaLa2Xh2mwTbaiaChRELdVQd4ibMkb21C4Uz6297topYtp6tiarrpYx0tiapY3MN7ztcGfE0kuibQ2y6AkseHk6r5cAQE9qTmRtnTxzs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AVZW8rmhibiaLn3oLKz3sFHqIAhnmByCkLCI5ErewF1c9ibll2Khk58QLGbicDG5ibuBJ3Dxibc4px5PIib9FeUUOewE2vYF4eQ8Y1PfVDNw1A3nQI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AVZW8rmhibiaL41Fe63NwUIKLU9GLerELl6PicibhvbMLbpiaMgucmn4SZ4XUJMKGSe21qn408PviaQTayQVIYeadsOH7CNsl8raanyGOgicWWxUa4/640?wx_fmt=png&from=appmsg)

其中继续跟进发现出现幽灵比特位的就是这个fromHex这里出现的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AVZW8rmhibiaLdXfgpBjEqCD3RMup1odjNFsy3S5yF4ia202CdKWgsFYpv6lWsRkGZicJeDdIAjJ96Ah69PWY0EktTJtb6FuXVmeokKmH9bIbV4/640?wx_fmt=png&from=appmsg)

欧克，在以前的那个编写一个jar工具吧，测试环境 Tomcat 9.0.56

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AVZW8rmhibiaJxdo72mJZnKHHtcSQNZCp7UqzicxuOwEzWbmcfVNJMsJI3hbO4ia72s4czxYHWLMbqXE75yPic1UVB6vShNTgiabS6ZmwibVzY59rM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AVZW8rmhibiaKWcIib0FwWbMSVFezjeGM2uPqwTVTcfn6qoF4R6DrTtDb6pSwrtvHibFDCd45r9EmGUL5FomXBIbmRRyb3tib9URr0LkDUZV7mM8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AVZW8rmhibiaJnW1uhuQ1gKAyFgBq3ZhWQs65weLQicO2ialJwUQpxGSibcniazLkXyXDSfKwdfwLEnsSrDILTp9gQccsWAB1DOoyqTNu17DoICQM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AVZW8rmhibiaKVicUJS1pF2Jd8fyqs5kXjAT31FjibbeCF9RgswSItcu9ntFRjUEQlib7B7q1W2yuUrictY7abLoMXfy2snIEbicutUZP4wWr8tmqA/640?wx_fmt=png&from=appmsg)

当然有一个小彩蛋，自己去研究吧，挺好玩的。就是我们基于这个特性始终去走out.write((byte) c)这个逻辑，mimeCharset

0x03: 结语

    挺好，学到了很多。又到emo的时候了： 静，轻似青，青争，轻争方为静。上善若水，水善利万物而不争，故几于道。

**本文章仅供学习交流使用，文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途以及盈利等目的，否则后果自行承担。请尊重原创，相互学习。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/CK4vLU3q0r7cbrhJYia5mceH4syD1oAkMibdJWRYiaZwE8SNxYRkwtlAibeegXnllww8DqCEaia9ceuZAdyeUWPnaVg/0?wx_fmt=png)

Feng随心而安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CK4vLU3q0r7cbrhJYia5mceH4syD1oAkMibdJWRYiaZwE8SNxYRkwtlAibeegXnllww8DqCEaia9ceuZAdyeUWPnaVg/0?wx_fmt=png)

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