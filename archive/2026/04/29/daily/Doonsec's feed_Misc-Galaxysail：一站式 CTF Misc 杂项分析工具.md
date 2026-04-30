---
title: Misc-Galaxysail：一站式 CTF Misc 杂项分析工具
url: https://mp.weixin.qq.com/s/3bFWifwmXZaF_jwDkJNbQA
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:24:27.528549
---

# Misc-Galaxysail：一站式 CTF Misc 杂项分析工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicIibiaIb7gBibTERHibuMhE6BBx3okQdReldRZ6E0s9phgtmTZdPJtHJcBianiaS9rqqSmH11unVdOUkc93AxHYibN6NdBTRKJEjWoiakU/0?wx_fmt=jpeg)

# Misc-Galaxysail：一站式 CTF Misc 杂项分析工具

原创

Galaxysailll
Galaxysailll

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[CialloVOL 1.2：便捷好用的轻量化内存取证分析平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487188&idx=1&sn=e79b9644800b6e2a27241243fad4f56f&scene=21#wechat_redirect)

·[近期你还有这些CTF比赛可以参加](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487155&idx=1&sn=8dbf634d2c54d83eb5baa5fcb781b98a&scene=21#wechat_redirect)

·[USB抓包工具：Bus Hound](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487129&idx=1&sn=c837679e94cfa86982879523fcde61ed&scene=21#wechat_redirect)

·[Attack\_login：基于Golang开发的Web批量连接测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487109&idx=1&sn=8d8c299835fd86f8fafa547010f98cd4&scene=21#wechat_redirect)

·[PyGlimmer：Python逆向集成工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487068&idx=1&sn=c7e31db8644a1a56beb932b40ef5cd95&scene=21#wechat_redirect)

·[ClarityJS：一款轻量级JavaScript解混淆工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487053&idx=1&sn=1eba92a83267ab8c8a2ef8db834a4586&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicLjmgNmtVFfKdKBWJmmXUpI4ibSMYp2vZe0PGgfYlpD4oKr3TIto938b74yPS9qibe6571E8uyu3gzVvZ0ZNboz9RO4bsbzkle4o/640?wx_fmt=jpeg&from=appmsg)

    Misc-Galaxysail 是一款面向 CTF 竞赛 MISC 方向的集成解题工具平台，专为隐写分析、编码解码、压缩包加密分析三大核心领域设计。工具以单文件 exe 形式分发，无需安装 Python 或任何运行环境依赖，解压即可使用，开箱即用。

    GalaxySail 围绕三大核心模块构建一站式 CTF 杂项分析平台：图片隐写（6 步流水线：元数据/文件分离/LSB/GIF/宽高修复/盲水印）、字母编码（20+ 编码 + 7 种古典密码 + Magic 自动识别 + 十六进制编辑器）、ZIP 加密（伪加密修复 / CRC32 碰撞 / 字典掩码爆破 / 结构修复）。

    容错性强：支持损坏图片、不完整压缩包的分析与修复  简写为一段技术特色：完全离线运行（本地分析，不上传文件）；单文件 exe 分发，无 Python 依赖；设备绑定授权，一机一码；现代化 Web UI，操作直观；结果持久化为 JSON，支持搜索/导出/统计看板；批量处理 ZIP 字典/掩码破解，流式反馈进度；容错性强，支持损坏图片与不完整压缩包的分析修复。

    本工具处于持续开发阶段，将根据 CTF 赛事趋势和用户反馈不断新增功能模块与分析能力，敬请关注后续更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**使用说明**

获得压缩包后解压得到以下文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIp9cvWpf6x2a5hFgjlicP20ibbIOEWSnIkm35Uc3URZvwZeUzicmQCWEWh4ghI6mbF6ffaKmKssXAXTSDnOXvXdLKX1BmGMraK0I/640?wx_fmt=png&from=appmsg)

    双击打开Misc-Galaxysail.exe文件即可启动工具，并且会在此目录下生成instance、results、temp、uploads文件夹：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLZPZicibs4tcqmw2V6w33RfyEsQH8D0ibmNsEeThPx4uNWtC7pmlEsnw635ELo3VaWUaO4nRF1pibFNX6MGLQfx3siaerAPbfB3UtQ/640?wx_fmt=png&from=appmsg)

    同时工具自动在默认浏览器中打开激活页面，若浏览器未自动打开，请手动访问 http://127.0.0.1:7890。

    请按照使用说明.md中的指导完成授权码的获取并输入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJws5G9aDoaGGvkwSP0CBHqefkLlQgcCQXJHVj6e7mOEKn11BzOM4XpMiar2sXVjJeKL8zS0qriaZhIbuUU4H64DQmF2SF1qpmKE/640?wx_fmt=png&from=appmsg)

    然后便可以进入使用了：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJBia6rUP6fCHavP6EicfmDyaRSpaIFBNsVF1xLubXj9mWUEbtY5DJ6WaqTEOKy96bkibhOPj8udT0D1hPBpN0rzkCfk93QNofNTs/640?wx_fmt=png&from=appmsg)

工具界面是目前三大模块的展示，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicILY18husvxqKTSaicECXIj9Pdtj8KFfXSm4PBqp4PtSMRoFCJldd4TSmGk04unbwZzvAqXGmUFRwtITPIF8MYunicia74eT5aMsw/640?wx_fmt=png&from=appmsg)

结果界面存放了所有的分析结果，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKuMFrqKmQACBRzZmicdyA5skYTjARmqxwIqsu2SebXj4MlEjb4nVzUT7JU1xa9l5bKUicibQ2PITy3pf429L2xKgyGkFvqEYkzh0/640?wx_fmt=png&from=appmsg)

文档界面展示了工具简介和简单的使用说明，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIaJ9pY1uy19JRHHg6NznpibXqI2nFibad3M6ChLDicng8YbvXEEuvUkg8CAQZA62J6jOVbcDF24xS2SAIia8g0t5yicLlVdMia33cNs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**功能介绍＋演示**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**一.图片隐写**

首页点击图片模块下的”进入“即可进入到图片隐写分析界面：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLtRGyNjK8hxfOFnqfLmlXUWREicWhI7NmfrA4oefouPKMGuLhYFbr9TsmHclESD4gvT9rGHncuNrMgZleoP3Uwpz1MMs8ksibpA/640?wx_fmt=png&from=appmsg)

    支持格式：PNG、JPG/JPEG、BMP、GIF、ICO、WebP、TIFF

    单文件上限：100MB

    上传图片后，可手动选择 6 个分析模块逐一执行分析，每个模块独立查看结果。

1.元数据与文本块分析

    读取图片元数据与文件格式信息，对图片的基本信息，EXIF信息，PNG文本块，文件尾部数据信息进行检测和分析：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJNiaDAF8vychptJ4trQBq1f7cfv1OOjKVhqyfdKWEcDibeaU9FHa1PCW1wiagQX0UbF20H4B1W3VaO16MFlXXEq3BKyektujvgibk/640?wx_fmt=png&from=appmsg)

2.文件合并/分离检测

    识别图片尾部拼接的其他文件，包括：Magic 签名检测，文件提取，偏移量定位

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicK3q2HMem8kSJEFJG1My1RHbQ0ibqv90z3vxrLQOZMk1VeuxOic90H4iaCXnfkicFG179qXOYXrZ04JtQQt3FqJrJ17KNibpO6o0I4c/640?wx_fmt=png&from=appmsg)

    可以看到检测并提取出了图片中隐藏的zip文件并保存到了本地

3.LSB 位平面分析

    执行 LSB（最低有效位）隐写检测，进行**54 种组合扫描，拥有**三种视图模式，**正则搜索和**匹配导航进行定位，同时也可以将组合获取得到的特殊文件，比如图片或者zip文件自动提取出********

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIrBNvNktobIIk6D8Qc7UeLLbTFfWE2dWQaGea6pPTQA26LdJBRa1eeUAS2icpkyhJ6Gac2EIvGXJUicZymsiaBjeAkia3NKXic93mM/640?wx_fmt=png&from=appmsg)

****4.GIF 帧分析****

**对动图进行帧分析，逐帧拆解展示，并支持帧导出**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKyUHVFl5jrotJMz6lEycABzuSf75HDW5uVT95ia99l5csqBHlCL6Pv13HGYXDvRf9ibWJGVFNF9bFcN4PPZSpkIiavJSKLfxgiawc/640?wx_fmt=png&from=appmsg)

****5.宽高与 CRC 修复****

    检测 PNG/JPEG 图片的宽高异常，自动修复 CRC 并爆破正确宽高，进行异常检测和修复输出，展示修复好的图片并保存

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJlnR2jjvV9yB0kq7bw5F5LfSryrYtfcQqfhMzs7WBhicz43T6hfRb3CcASnwcYz6r6NQKVZmAPRib2qCwTovyjXUGSMMcPLAwkg/640?wx_fmt=png&from=appmsg)

6.盲水印/双图叠加分析

    支持单图和双图两种工作模式，单图时展示图片基本信息。双图分析在上传两张图片后启用，FFT 盲水印解码、像素运算，尝试多种盲水印提取策略并展示所有结果，支持在线预览提取结果，提供 PNG 格式下载

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIRS47ibmP9tst4hAIDiaiaadJnAt35CvJ9IwcA7O2Wu7yhXPeiawWvJQtQS1Eziaic68GmicZ7W0HcyHBvuMXusRCr6ibBcmwHSv6pW64/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**二、字母/文本分析**

首页点击字母模块下的”进入“即可进入到图片隐写分析界面：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJbUAtJNDZ3npok02LUWXMkayI8Yaoeib2MxmYLMrx0hrlHBrkGbEyib2wcvaemvKibKCaXH1KklxPKCvHC4Dm90KkPq1vabfjFco/640?wx_fmt=png&from=appmsg)

    支持上传 TXT/LOG/DATA/MD 文件，也支持直接粘贴文本内容进行分析。提供左右对比模式：原文在左，解码结果在右。

    除此之外，还提供单独的十六进制编辑器页面，支持对文件进行十六进制级别的查看和修改。

1.解码编码

    支持base64，base32，base58，**十六进制 (Hex)，**二进制，八进制，**URL 编码，**HTML 实体，**Unicode 转义，**凯撒密码，**ROT13，**ROT47，**Atbash，**栅栏密码，**摩斯密码，**培根密码的编码解码。************************

****同时包括**Magic 自动解码，**递归解码，**Flag 提取，**Base64 隐写提取等智能工具。************

******还有**字符串反转，**大小写转换，**去除空白字符，**正则提取等文本工具**************

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLGUV0oOUP8md8xibaV3Kv0YibSY6K9qIYWaQgVncaZjWQxLpDAibR2icSOibQztUia6gdzZL9tdy16uWNhCjHRqA3eJTFCZkMquDVxw/640?wx_fmt=png&from=appmsg)

****2.十六进制编辑器****

******提供完整的十六进制编辑功能，支持对上传的文件进行字节级别的查看和修改。支持文件加载，字节修改，全量写入以及另存文件的操作******

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLxsrkia6a0g9WYr60B1Z5dpwdCKp93jX2El7OrLKJkEibdicaIJnxhAw52rssrb86QyrZSoJDzruQJNcX950UvicGmuyJruGlT4bg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**三、zip分析**

首页点击字母模块下的”进入“即可进入到图片隐写分析界面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKAWMVdy9K7rDneLQ8WCpYg5D6LRcDZuSAlsS2S6Uobbia59n2tQYWJYjP4qcP3NJuxr8iaXXicMDoffuBfybwDVicVkicfVGxQVb3c/640?wx_fmt=png&from=appmsg)

    支持格式：ZIP、RAR、7Z、TAR 以及从其他文件（如图片）尾部提取的压缩包数据块

1.格式检测＋结构分析

自动检测：通过文件魔数自动识别 ZIP / RAR / 7Z / TAR 格式

容错识别：即使文件损坏或不完...