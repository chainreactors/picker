---
title: 从开源爆款到 OpenAI 收编：OpenClaw 体验、架构与 Prompt 全解析
url: https://mp.weixin.qq.com/s/H1DzmanO_Pxwudb8eEH9QA
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:13:13.851017
---

# 从开源爆款到 OpenAI 收编：OpenClaw 体验、架构与 Prompt 全解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2QnR8sFGoyicVmu5uGywDVNVfzcPVUIF7Yn3gRS5OZsES3kAA2fZWfR4UGYCeakIytvXaeqSLtkJKQPwQibu0UEtJl8tCo0sV2QUTgpAA3B10/0?wx_fmt=jpeg)

# 从开源爆款到 OpenAI 收编：OpenClaw 体验、架构与 Prompt 全解析

原创

yzddMr6
yzddMr6

网络安全回收站

![]()

在小说阅读器中沉浸阅读

# 前言

OpenClaw 最近很火，非常出圈。作为一个自托管的个人 AI 助手平台，它让你可以通过飞书、Telegram、WhatsApp 等 IM 渠道随时随地跟 AI 对话，数据完全掌握在自己手里。

安装了很久，一直没时间认真测。终于抽出时间，做了一次完整的体验测评，顺便让 Claude Code 把它的架构扒了个底朝天，还抓了一份它的 prompt 流量包做了个解剖。

省流：作为个人助手聊聊天、查资料还行，复杂任务容易卡住或者死循环。但架构设计确实有想法，prompt 工程也值得学习——这是第一个出圈的个人助手类项目，后面肯定还会有更多。

## 一、体验篇：从安装到翻车

### 安装：比想象中麻烦

OpenClaw 的安装并不是一键搞定的事。好在有 Claude Code 帮忙，直接让它帮我装。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoy9aQwZ9EpPhozWa77ic6TeJrHu9R8tqgTVHG0nKNurpI0JpDgundTQARPUadOWWmKsDCkI1M0rCicV5zjCzUGu9eopP4Za6ia0n7E/640?wx_fmt=png&from=appmsg)

装好之后，因为要放在内网小主机上，需要改监听网段。默认绑定的是 loopback，局域网其他设备访问不了。继续让 Claude Code 帮忙修改。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoyib9xpMfRDpRG4YhokicSLQf5Sa3ws3KVeo8I2tBGSuOxgNicf35SicCNaBEnF4zrz28ic8DtdYsbb7HlzaO2agqic1sexbN3vgJkxzE/640?wx_fmt=png&from=appmsg)

然后遇到第一个坑：默认的 Antigravity 认证插件不支持最新的 Claude Opus 4.6 模型。没关系，改成我们反代出来的 Antigravity Manager 的 OpenAI 兼容格式接口就行。

第二个坑：直接从局域网连接会报错，提示非安全上下文。继续让Claude Code帮我解决。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy8xTSEI6yBY5f3gDFESSET1QJ159x5UiaJ9TuMjW0ZjEWjOrMdNBJV7Iia1uGiaQiaWdl4XG1M1H0hkPqhickC6F6rR3BRicC1RTQ6EQ/640?wx_fmt=png&from=appmsg)

### 连接飞书

接着通过申请飞书的 bot 机器人，打通了对话通道。日志显示 WebSocket 连接建立成功，飞书 channel 已经跑起来了。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoy9qN1uZVGK4sIQAWhfaiapJA4YoVHf86ZicBtDRM4KcNx1gpLSySAhytvNXjb685GdAhYrxJypgawC4x3vfq3pqlLq4dj0EPFnTg/640?wx_fmt=png&from=appmsg)

发出第一条消息——"你好"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyibvvcj22hUSBgC37mVibRasYUEWCqfXrpBfsUO8xEuNLjDvjMicd77eCYj4yYMOWDEfnh2U3PJNKPxEic7fBN8YM6tkFhcasodbEs/640?wx_fmt=png&from=appmsg)

机器人回复："你好！我刚刚上线。我是谁？你是谁？"

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoyibCibsxruAqVg6SGKxOR8fxzfT1fdcs0QUibZfmj3Lzf10QQXDCaxzrnFn11w9iad0k2yWwr3DxZZAMicYojgIS4ic3ofPO51retu3o/640?wx_fmt=png&from=appmsg)

告诉它我是它的主人之后，它开始自我介绍，还挺像模像样的。到这一步，基本的对话通道算是打通了。

### 任务一：让它分析自己

第一个正经任务：让 OpenClaw 利用自带的 skills 功能，用 repo-analyzer 技能分析自己的代码仓库。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy8e9BJZI0NmI78GIibS6aFcc69OnaR29S1OrdEgJRc4j4TposDlu3yBLnJXws6OzEO0GgfdXsKg8ZO8DQZyWQj5AFE5MPsCL33M/640?wx_fmt=png&from=appmsg)

结果它说 git clone 卡住了，要改用 zip 下载。我说怎么能卡住呢，是不是网络问题，让它再试试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy8BuD8vcjehfx1SV4YibtBLURkicicq31Eg8uJtkKlq969nDhgKarP5MhHdU5T6f3cSJ5hMXwQ8hkjCkyh7jqXickeGvtv7zp8zTD4/640?wx_fmt=png&from=appmsg)

开始疯狂道歉，又说自己其实 clone 成功了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyibC7lpkOv7xRQRuEZGKj8upZHuENGrULI78qIGCUoGLgIvaFguTIoTEGJ1WPVB3ibKib5nlrzWsy8PCjuKcXCfibsjv83QibCl8Edw/640?wx_fmt=png&from=appmsg)

分析的时候又开始道歉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy8GFab7zjymkseGB3vJqMTl2FvDOEwibgRIYo7aoRianFrt5wZF2xYGZ9yjAY3zzKfRaClDLgEhogw6EZFibiaEG11omaccSGagHos/640?wx_fmt=png&from=appmsg)

我看了一下，其实根本没有 clone 成功，目录下一片空白。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoy8iapW6icgHxRibkJC2fkoWWLY875RORoz9VZ1oQnPxpaL32xH6569Xqqvu4EQBY4Q7dvXV1BYiawR0aTjGT8P0VpxccmLHa9MavDo/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoy9PcDvrV2Dfh5hc0ClmhiaqtkNeGSlib7PnjubAFmyic8mO0Aw42JUEAEfGAnXb9AKzwyoYic3GXia3XJ0O1V9xuIl00I5HSMp1oicHo/640?wx_fmt=png&from=appmsg)

让它确认一下。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoy9fcvVf2TE0hEvnXTt71ke5dFNrOX6BPcyvAtpDLD1dzvfs8CzL3GFcicBrZm5NXsmq7jVbw1ic5R4Ec9Kr7Z02qjiaMAebWfWyc4/640?wx_fmt=png&from=appmsg)

又开始道歉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy8qBYEm3pfkg8PKoDcQPgguvr5oaElA6fA9tFe25uKXpRO52v3mQ78y8WgxOAeroOroHJEZ5xAFfg2RUE8Qv8PDO5EMkqznowY/640?wx_fmt=png&from=appmsg)

感觉不对劲，问问 Claude Code："我部署的 OpenClaw 特别笨，很奇怪，它背后也是用的跟你一样的 Opus 模型，你看下是不是我哪里配置没配对。"

Claude Code 一查就找到了问题。这也太坑了，也没有告诉我要这么配置啊。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoyibzialdn2ByLbkH2TqVSJLnWHHSLxUhAouzEw0ZV6P5aqE5a630QGoce668NrcEQl2FSyu49J8AAF0sLzJxDlNRm7yic088gc2ks/640?wx_fmt=png&from=appmsg)

核心问题是 `maxTokens` 设置太低了（8192），thinking tokens 会占用这个额度，留给实际回答的空间就很小了。建议改到至少 16384，最好 32768。另外中间代理的 extended thinking 格式转换也可能有问题。

简直是 token 杀手，2个问题花了我快 2000 万 tokens。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoy8EXYz7lAf4Mpg1JVnKKUdvHUwKWpu6oDFWQgfXS1TQ76iaIz0zVTr2lKIRs25IT98FWdFtibxIxZa5CQMiaj4peHyXLN2DubLVEg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyicaibyZsSIRgFLR427lqkE47ibPkkAyfWEpE4dficJTj0P8em03icFbw6uxvOic8laJsZTHJSTRicdZWEHibS0KGksokr1sK0W9iauWWe4/640?wx_fmt=png&from=appmsg)

改完配置之后，OpenClaw 的表现确实好了不少。终于可以正常跑了。开始逐步分析自己的项目代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy8C99Nv1IBuYXakRWyChUeLPcw0BXFIIoU9yicSVdZtgib4fo9AuwBgqwtcWx664iaersj3A0JKslIhsL3kq5EKflO19BiaafMr54o/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyicKHQWLfibibxzWDqXP85gvtMM3hfXPL9P50YJ1IOPI3L7iahu8QPjwHlUzj7OWe7YZhBPuSPR9bX2WbnANPIsDbL3xryV4lUfia0A/640?wx_fmt=png&from=appmsg)

但是最后可能项目文件太大了，又又又卡住了。

监工Claude Code上线，看看咋回事。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyicDiaib1icfCBiciboznDsy0F7y9w5CuFSPybYAJ2QIZlibc0bwXvADe9YIL7LfwO1mgGwRIh0UictqICxiarCVKrpYmOe2k2darPh6TeA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy9ZGlLMI72ia4TG1dywTibUZUuneibZvRKKfKEy5hg6B361RXx95b7KwWHaLDNGu0yrsnacAtibIe5lPYoGI0TwmLvyB5ibZJ37JBK4/640?wx_fmt=png&from=appmsg)

过一会又不动了。。。。问问 Claude Code 怎么修。

Claude Code看了下后给我加了个配置参数让我试试。修了一次后，不知道没过多久又挂了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy9foo0Yx5JL5zx6IFYk2TkCiccP7SJpuCgBHC5Dov4MPCZADtXpnGibric4pe9UWcVNM2EA6VPDHzaAIzDuzC4Kth9tgNXeb8dkTw/640?wx_fmt=png&from=appmsg)

麻了，已经不想再测了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyic01eQzh1juoywgyR92R66NJBF6C7XykusHuXuWQImcLCOve5E1NVmqhjUYuBmRtTPL4Ujc3qzke1rWdicBbyBYY1hQ4XOxr9pM/640?wx_fmt=png&from=appmsg)

### 任务二：查 Dify 最新更新

换个问题。背景是 Dify 当天发布了 1.13.0 的更新，看看它能不能帮我总结一下。

结果很离谱，还在回答上古时期的版本，并不是最新的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoy8WEpkp96ntKBntDuOIaJt1VIZWpun9bRRWR6lIH5UP8KvG2Cg7ugkD5mfko5rBMOWOZnFkfKmgBibnW8b4Nb1iaESiakD6IYZUYI/640?wx_fmt=png&from=appmsg)

看不下去了，一步步告诉它怎么查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyibklVZkejXflBt9uGCJ516GZ2oSkQZA8ibFicpic9bHyeVj67mw7pulgXMFV6Px4nT9osoMicwibiarlDnGEP6wrcTBdbJpDpTT0bib8Y/640?wx_fmt=png&from=appmsg)

让它查 1.13.0，结果查了 1.11.4 的内容出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyiciaD5YDAnYLkzKznhdk2uJgRIVXIicBOSellYFJpIv94yxfGth8YeolIdUjFibFRWBrj7WXicvmdcSpPlibZGIaKIkwPGCpS0r6Bys/640?wx_fmt=png&from=appmsg)

经过相当长时间的排查，最后发现是因为默认不支持 web 搜索，需要自己配 API key。

不是哥们，查不了你咋不直接说呢，在这胡说八道。

配上 API key 后，终于可以正常回答了。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoyicaY4ztJ5O6n3mEVxibBQJxsVmknwQz9cyhkvBUV2BrTKKo0EPFormxQAb7RwOicS8Eic5rzCV1ywARXAs4giaJF0kzsOiaKoZTAicIk/640?wx_fmt=png&from=appmsg)

### 任务三：帮我分析股票

最后一个任务，分析美股行情。

一开始直接给我拒绝了，说不能提供金融投资建议。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyibGPib2v28xKXtHAcftS2my0M2ysVkH9rS9TbtoXXYLR3KjOibjiawsyibnoZ80HBh4RFGict6fqnD0zBwX5onJZ1TibqxsbBb31WoeM/640?wx_fmt=png&from=appmsg)

经过一番"哄骗"，终于让它开始工作了。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoyicm8gUW0DxcESTmUibNxwe3rtnsgzxI6X6vvYSUX9ZzmoItM1av4fa2ZaavR5preicCyxeeP1vbbEDiaxIMOaQoCqpgjCfIwBA8Co/640?wx_fmt=png&from=appmsg)

但是查了第一家之后就卡住不动了。上午下发的任务，到晚上还没出结果，我就知道又出问题了。

![](https://mmbiz.qpic.cn/mmbiz_png/2QnR8sFGoy8XlRLQ5MrmoEL9nSZn9ZuZ5WXzRH5LD49PSHxibeicNAibcEnZ8e67llM35UjQJJicZ1iaGURAQDG9s61lA17NEHU4yK5jITr6RxwM/640?wx_fmt=png&from=appmsg)

还是让老演员 Claude Code 给我当监工。

发现果然又出问题了

Claude Code甚至问我要不要让他接手这个项目继续跑下去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2QnR8sFGoyibrdtRd2MibNR5ul3VEsLzx0ib5UzDNQ4DVb5JIUaYmfkick7icM1OmibESeic74Pxqq7iafUgbOfGTiaJZHlvBlUebDoia9I8ib4Odw7NPI/640?wx_fmt=png&from=appmsg)

### 体验小结

三个任务做下来，感受很明确：

简单对话和信息检索，OpenClaw 表现尚可。通过飞书随时随地跟 AI 聊天，确实比打开浏览器方便。

但复杂的多步骤任务，它很容易卡住或者死循环。git clone 卡住不报错、查不了网硬编答案、分析任务中途出错、股票分析做了一半就没动静。

同样是 Opus 4.6，准确度和可靠性相比 Claude Code 差的不是一点半点，以至于我还要引入 Claude Code 给它当监工。

整体感觉，OpenClaw 像一个非常努力但缺乏章法的莽夫。能力是有的，背后...