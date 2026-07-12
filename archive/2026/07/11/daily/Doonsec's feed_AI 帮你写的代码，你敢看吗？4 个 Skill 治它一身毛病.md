---
title: AI 帮你写的代码，你敢看吗？4 个 Skill 治它一身毛病
url: https://mp.weixin.qq.com/s/AJ1E9qyCkDtwr04eIi2bpQ
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:08:52.411784
---

# AI 帮你写的代码，你敢看吗？4 个 Skill 治它一身毛病

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MGmpoYTX6rj3fIdIDlG2H5XDnAaOzc2lq9neTOrKJsIlQUy9QgoTl8w7LMkia5wUJZASUOzNATZVRrf6F8jzD1xxQko7R8jCyFrFqtiam1Afw/0?wx_fmt=jpeg)

# AI 帮你写的代码，你敢看吗？4 个 Skill 治它一身毛病

原创

AI安全工坊
AI安全工坊

AI安全工坊

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# AI 帮你写的代码，你敢看吗？4 个 Skill 治它一身毛病

我用 Claude Code 写了小半年，直到上周才反应过来一件事。

我一直在让一个能力很强、但没立过任何规矩的实习生，替我写生产代码。

它写得快，也写得多。多到有时候一个小需求，它能给我糊上三四百行。我看着那堆代码，说实话，好多我自己都没耐心读完。跑起来没报错，我就点了"同意"。

现在想想，有点后怕。

你是不是也这样。

这周我扒了一圈 GitHub，发现有个东西正在悄悄治这个病——**Skill**。而且这周好几个 skill 的星标跟坐了火箭似的往上蹿。我挑了 4 个最能打的，一个个跟你说清楚：它治啥病、怎么装、有啥坑。

不吹，也不藏。

## 一、先说清楚，Skill 到底是个啥

一句话：**Skill 就是给你的 AI 立规矩、补短板的一个小文件。**

你把它装上，AI 干活就照着里面写的来。不装，它就还是那个凭本能瞎写的实习生。

好在装它不费劲。现在有个通用法子，叫 Agent Skills，一行命令搞定：

```
npx skills add <仓库地址>
```

Claude Code 用户还能走插件市场，`/plugin install` 一下也行。这套东西现在通吃 70 多个 agent——Claude Code、Cursor、Codex、Copilot、Gemini CLI，你在用的基本都覆盖了。

那为啥这周突然火？我的理解是，大家慢慢想明白一件事：光换个更聪明的模型，越来越不解渴了。真正差的，是给这个聪明脑子配上"手艺"和"规矩"。skill 干的就是这个。

行，上货。

## 二、4 个当红 Skill，挨个盘

![](https://mmbiz.qpic.cn/mmbiz_jpg/MGmpoYTX6ria0nM2RoYpGUkAyJXibs6NNQpjWXMzia0WWEWicdqmiaRAqUGNJIHyWCgvjyQEgaeW3iagEIo3o8VrQUXZ79oCmd7nibrxVhvhwMBsXQ/640?wx_fmt=jpeg&from=appmsg)

### ① ponytail：治它"话痨"，专写废代码

**77.4k 星。** 四个里我第一个装的就是它。

它的理念特别对我胃口，就一句——**最好的代码，是你压根不用写的代码。**

它给 AI 立了个规矩：动手前先自己盘问一遍。这功能真需要吗？代码库里是不是已经有了？标准库能不能干？非得自己造轮子？一路问下来，能不写就不写。

举它自己的例子：一个日期选择器，AI 原本吭哧吭哧引个第三方库、写四百多行。装上它之后，一行 `<input type="date">` 完事。

作者说平均能砍 54% 的代码量，个别任务砍到 94%。这数字——行吧，他自己报的，我没法替他背书。但"少写点"这个方向，我举双手赞成。

```
/plugin install ponytail@ponytail
```

装完 `/ponytail lite` 是轻度、`/ponytail full` 加码。**提醒一句：别一上来就拉满。** 管得太狠，它可能把你本该写的东西也给砍了，反而误事。先从 lite 试。

### ② agent-skills：给 AI 补上"工程纪律"

**72.7k 星，作者 Addy Osmani——谷歌 Chrome 团队的人。** 这背景，值得多看两眼。

如果 ponytail 治的是"写太多"，这个治的是"跳步骤"。AI 爱走捷径：需求没问清就写、测试不写、安全不管。这个包直接塞给它一整套流程，从怎么理需求、怎么拆任务，到怎么测、怎么审、怎么上线，24 个 skill 配齐。

最顺手的是那 8 个斜杠命令，跟点菜似的：

```
/spec   理需求
/plan   拆任务
/build  写
/test   测
/review 审
/ship   发
```

`/build auto` 甚至能自己把整条链跑完。你要是常一个人从头干到尾，这套能帮你少漏环节。

`npx skills add addyosmani/agent-skills` 装上。

**但说句实话，24 个 skill 有点重。** 你写个小脚本、糊个 demo，用不着这么大阵仗，反而碍事。它是给正经项目准备的。

### ③ taste-skill：治 AI 前端的"一股塑料味"

**60.4k 星。** 专门给做前端的。

你让 AI 生成个界面，是不是十次有八次给你整出那种一眼假、到处长一样的模板货？它管这叫 generic slop——没品的糊弄货。

taste-skill 给 AI 装了点"审美"。给你三个旋钮拧：布局要多敢玩、动效要多花、信息铺多密。想克制还是想张扬，自己调。

`npx skills add https://github.com/Leonxlnx/taste-skill`。

**丑话说前头：这玩意儿效果特别主观。** "审美"这东西没法量化，它调的是几个变量，不是保证你出来的东西一定好看。合不合你眼缘，得自己看。

### ④ graphify：让 AI 看懂你"整个"项目

**79.9k 星，四个里星最多的。**

AI 有个通病：一次只盯着几个文件，不懂你整个系统长啥样。你问它一个跨了好几个模块的问题，它经常抓瞎，甚至一本正经地瞎编。

graphify 把你的代码、数据库结构、配置全扒一遍，织成一张能查的关系图。谁调了谁、改这块牵动哪块，清清楚楚。而且它解析代码不靠 AI，用的本地工具，四十来种语言，快还准。

装法稍微特别点：

```
uv tool install graphifyy
graphify install
```

然后编辑器里 `/graphify .` 开跑，跑完给你一张可视化的图。

**不过丑话在前：项目小，它没啥用。** 就几个文件的东西，你自己扫一眼就完了，织图纯属杀鸡用牛刀。它是越大越乱的项目越香。

## 三、别急着全装，缺啥补啥

看到这儿你可能想：四个全装上，那不无敌了？

打住。这恰恰是我最想说的——**skill 这东西，缺啥补啥就行，别贪多。**

你想啊，给一个新来的实习生同时塞十本规章，他大概率一本都记不住，最后还是凭本能干。AI 也一样。规矩堆太多，互相打架，反而更乱。我自己就试过一口气装四个，结果它有时候前后矛盾，改起来更费劲。

所以，对着你自己最头疼的那个毛病来选：

![](https://mmbiz.qpic.cn/mmbiz_jpg/MGmpoYTX6riaWn0dKofBJib4ebfZkQQ5ibI7pv0WXMblVgGGLlpx6ZMLXqbibichDvUfZkJOB4aibjCY24ttfic3MogM3SoNJ9ZLwE9axmE5USc97k/640?wx_fmt=jpeg&from=appmsg)

* • 老嫌它写太多、太啰嗦 → 先上 **ponytail**。
* • 一个人干全套、老漏测试漏审查 → **agent-skills**。
* • 主要做前端、受不了那股模板味 → **taste-skill**。
* • 项目大、AI 老是不懂全局 → **graphify**。

先挑一个。今晚就装上，让它陪你写个把小时。合不合手，你比谁都清楚。

说到底，AI 再强，也就是个上手快的实习生。你得给它立规矩、补短板，它才慢慢变成那个靠得住的老手。这些 skill，就是你手里的教鞭。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8RWa5pyic1Xob8V1UxQjOHLAx5qbkPJ2gibKpIQpRw4ogjL6jE9xIxc26o12ZRTBvPaLQNjxXDAO5g/0?wx_fmt=png)

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