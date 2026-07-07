---
title: CTFHub：第八十关——PHP——bypass iconv 2
url: https://mp.weixin.qq.com/s/b9uyXtDfuuvGMVmA5GBFtA
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:00:50.796293
---

# CTFHub：第八十关——PHP——bypass iconv 2

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TkbqemjbpIpgYl6T4SykK5VIxaNicROnVq5Tge2Dyh9Az8Fv0SZtiaS66qCHyXDKvxjVicPlRVe78icAWiburNHibbLlyTKg00iaic37fIPQJTiaFMKY/0?wx_fmt=jpeg)

# CTFHub：第八十关——PHP——bypass iconv 2

原创

君陌社区
君陌社区

君陌社区渗透安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTFHub网址:【https://www.ctfhub.com/#/index】

登录账号
点击技能树

选择“web进阶-PHP-Bypass disable\_function-bypass iconv 2”开启题目

漏洞原理: bypass iconv 2 与 1 的底层原理完全相同，通过 putenv() 劫持 GCONV\_PATH 环境变量，诱使 iconv() 函数加载攻击者构造的恶意 gconv 共享库（.so），从而在字符集转换过程中实现任意命令执行，绕过 disable\_functions 限制

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIpNV2xsKJwQhUtL4Yxl4iadMGA6gdNKr6LCXst5QHEdWLOo5VdaqAu4OqjdTpZ5xYq8ldicsiaeEMNFN7L0jYkyZj8df6Y4onr3zo/640?wx_fmt=png)

单击打开链接进入靶场实战练习环境，靶场中一件存在了一个一句话木马，可以直接连接

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrBOUJQdmibRPuWl46O0L4RXTTyULvg3JK0dk1YRjOVxg6kSxLwDRyPpB3Gabrn1cGeKOQLUdrX0SIR8aY977m0UmSdq5fy3j1k/640?wx_fmt=png)

打开中国蚁剑工具，测试链接，链接成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIrDWd1icMrbXD9BFHCgpgNm7jFRhwdLMCQQxAXicP5SmgCotTGmAicyZmwDibu6GEibhrrKapNxfbOicybJR4iaeibFDyWYwDN5TmM0GEc/640?wx_fmt=png)

右键打开虚拟终端，无法执行命令

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIqRgYsDukVaGj7Scb3wETgnM89QdVnicrHKvHdOicysBbH0Rj9ibLTR6wbg2KwWLM8eZUM2ccEkl8l2WWtibzKUPDoLk5tub6Naiczs/640?wx_fmt=png)

右键选择“加载插件” -> “绕过disable\_functions”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIpruR84u69fgjg139TSgQbhPJbVDYfvzOY95ItcncYAK0P6unKic6a0Xg8xFD1Jh0wibeNoOrnFBh1U6C3ibiclAuElOibLOibAEVjtw/640?wx_fmt=png)

在弹出的窗口中，模式选择iconv

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIrFPJaWDKeIBJeib6JwmL3EM0uxzcFMibvtKKDR8TCbzt6opvsmvmPWvDVPfJbiaY1X8ltiaB7g4LKuz2hHau3ISVqBjXUdZNuIGf0/640?wx_fmt=png)

点击“开始”按钮，插件会自动上传一个用于绕过的脚本

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrJicUpOc8ADkPmAF7dRMbCTD0pMF4HOnAcH5sRlyAvTjeVMrNMezyTaicXEo5z1ialKbTCv02CdeCyHrbqM9dLiaiakvDbtZnSibWSQ/640?wx_fmt=png)

插件执行成功后，会在当前目录生成一个新的 PHP 文件.antproxy.php

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrgxcqsYpYuPsUZJ8yEAcKrSfdZBBGyxksNuOzRDEKGvHHLdYRKVd5ovqOibc2Z8OycdsxXYL837ve6DCxcNyZLmeqDWicjWAaRk/640?wx_fmt=png)

连接这个文件，测试链接成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIo0wibqytjwdAUOYsymYWoR3SjQMotUJm7lN8gb4OYOsmtib8VS6gic0K4tahZu1Cia48zAw2GkYkFLAlCTLtibWEGHLoqMT6z1LojA/640?wx_fmt=png)

右键打开虚拟终端，执行

```
/readflag
```

命令，得到flag是数据

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIpS3cakmMtYA3GXjQ0tIZysPUtkhWMTZiahKcH9lVMDUp7cJKRWdzOJQiadWtgKuHLicGIm7kVBiaooJ1I1kZjYzqcQAOy786xf7xY/640?wx_fmt=png)

上传flag数据完成靶场实战练习

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TkbqemjbpIq8maYx7icXEusLbiaPLJaA3wdHNeYuc5QXe6e5ejibwSHTf6v53BjjR1ZNowZIj5UOqazaj7VAxvFuPJ3OW8zbRqIKzOZa2RWUZ0/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/csuE9m26HkI8taS28gIOWsc8KaibxmZ9HDovmlvGsicEnJuSw0Ricdq3KibbTUnRicEO0NohDyczWdgJBOe3RWF1tQw/0?wx_fmt=png)

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