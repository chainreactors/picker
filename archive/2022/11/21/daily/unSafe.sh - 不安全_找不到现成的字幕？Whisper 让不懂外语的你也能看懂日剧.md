---
title: 找不到现成的字幕？Whisper 让不懂外语的你也能看懂日剧
url: https://buaq.net/go-136473.html
source: unSafe.sh - 不安全
date: 2022-11-21
fetch_date: 2025-10-03T23:18:51.257608
---

# 找不到现成的字幕？Whisper 让不懂外语的你也能看懂日剧

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/bad9a1ce979b5f595634f90d1fad92f5.jpg)

找不到现成的字幕？Whisper 让不懂外语的你也能看懂日剧

找不到现成的字幕？Whisper 让不懂外语的你也能看懂日剧从大学开始，我看日剧十几年了，但日语毫无进步，只能听懂几句耳熟能详的句子，看国外电影全靠字幕组。曾经我想过学日语，报了暑期班，但成绩被七岁的
*2022-11-20 16:0:0
Author: [sspai.com(查看原文)](/jump-136473.htm)
阅读量:41
收藏*

---

找不到现成的字幕？Whisper 让不懂外语的你也能看懂日剧

从大学开始，我看日剧十几年了，但日语毫无进步，只能听懂几句耳熟能详的句子，看国外电影全靠字幕组。曾经我想过学日语，报了暑期班，但成绩被七岁的小妹妹同学吊打。然后，我就被自己的语言能力说服了，想着这辈子都离不开字幕组。这种情况一直持续着，直到我测试视频剪辑工具 AutoCut 时遇到了 Whisper。

Whisper 是今年 9 月被 OpenAI 开源的自动语音识别系统，除了可以用于语音识别，Whisper 还能实现多种语言的转录，以及将这些语言翻译成英语。「语言识别」「转录」听起来特别唬人，但 transcribe（转录）指将语音转为文字，Whisper 会为音视频生成带时间轴的字幕文件，是**支持 99 种语言 AI 字幕工具**。

虽然与 Stable Diffusion 同样归属 AI 工具，但 Whisper 安装非常简单，两行代码即可开箱使用。这部分我不多做赘述，具体可以看 [Whisper 官方文档](https://github.com/openai/whisper)。

```
pip install git+https://github.com/openai/whisper.git

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Scoop (https://scoop.sh/)

scoop install ffmpeg
```

接下来，我会分享如何使用 Whisper 为外语视频自动生成字幕，以日本综艺节目「中森明菜デビュー 40 周年 女神の熱唱！喝采は今も」为例。

## 音视频转录

在文件所在目录下打开终端，运行 `whisper jp.mp4` 即可执行音视频转录。测试视频名原本为日语，我改为「jp.mp4」，原因是我系统中只装了中英语言包，使用其他语言作为命令会出现 Invalid argument 报错，从而导致转录失败。Whisper 的媒体分析环节调用了 FFmpeg，所以主流音视频格式均被支持。

![boxcn775FSnn59GxsdubX641wWh](https://cdn.sspai.com/editor/u_/cdsigq5b34t9mjt23nl0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

视频时长 90 分钟，我使用 3080Ti 显卡转录，用时 10 分钟。转录过程中不要玩游戏，也不要进行直播等吃显存的行为，否则容易显存不足无法继续。Whisper 对设备要求不高，不过设备会决定转录时长和你能使用的转录模型。如果你使用 CPU 转录，时间会增加 5-10 倍。

转录完成后，Whisper 将生成原生字幕文件，日语视频会被转录为日语字幕，西班牙语视频会得到西班牙语字幕。

## 字幕翻译

通过 Whisper 获得原生字幕后，接着要将其翻译为中文。这一步需借助 SubtitleEdit Online，它支持免费在线翻译字幕，可使用 Google 和 Yandex 两种翻译引擎。1

1. 打开 [SubtitleEdit Online](https://www.nikse.dk/subtitleedit/online)，点击「Subtitle」>「Open...」，选择要导入的字幕文件。
2. 点击「Auto-translate」，选择翻译引擎，然后在弹出窗口中选择字幕要翻译的语言，并**将页面拖动到最下方**（非常重要），确定所有文字都被翻译后点击 OK 按钮。
3. 点击「Subtitle」>「Save/download...」，即可保存翻译好的字幕文件。

除了网页翻译字幕，本地端的神经机器翻译也是种好选择。macOS 用户推荐使用 [Argos Translate](https://github.com/argosopentech/argos-translate)，这是基于 OpenNMT 的开源神经机器翻译。如果你的动手能力较强，可以尝试 [Opus-MT](https://github.com/Helsinki-NLP/Opus-MT)。不管用哪种方式，都是将字幕以文本方式导出，复制到翻译引擎中翻译，即可得到不同于 Google Translate 的翻译结果。

## Whisper 进阶命令

### task

`--task` 分为 transcribe（语音转录）和 translate。Whisper 默认使用 `--task transcribe` 模式，将语音转录为对应的语言字幕。`--task translate` 是所有语言翻译为**英文**，目前尚未支持翻译为其他语言。

### language

`--language` 是设置语音转录的语种，支持语种范围查看 [tokenizer.py](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py)，比如指定日语 `--language japanese`。如果你没指定语种，Whisper 会截取音频的前 30 秒来判断语种。

如果指定语种与文件中的语种并不相同，Whisper 会强制翻译，但 10 分钟以上的音视频会出现大量的重复无意义字幕。2假设你把日语视频的转录语言设为汉语，前 8 分钟 Whisper 会正确转录到中文，但 8 分钟后的转录字幕会一直重复，并与实际片段无关。

### model

`--model` 指 Whisper 的转录模型，转录效果为 tiny < base < small < medium < large，默认使用 small。添加参数 `--model medium` 或 `--model large` 可以切换到更大的模型，但转录时间也会变长。如果你是对英文视频进行转录，则在模型参数上添加后缀 `.en`，能提升转录速度。

### 幻听参数

非英语视频的转录有时会出现**幻听**，即静默片段被识别出语音，或是转录结果与该片段无关。这些问题是由语气停顿参数引起的。幻听的解决方案是引入 [VAD](https://github.com/snakers4/silero-vad)，但 VAD 对动手能力要求较高。如果你的视频转录出现了严重幻听，建议先尝试调节参数阈值。

* `--no_speech_threshold` 无声识别的阈值，默认为 0.6。当 no\_speech\_threshold 高于阈值且 logprob\_threshold 低于预设时，该片段将被标记为静默。对于非英语长视频来说，建议将其调低，否则经常出现大段的重复识别。
* `--logprob_threshold` 转录频次的阈值，默认为 -1.0。当 logprob\_threshold 低于预设时，将不对该片段进行转录。建议修改为 None 或更低的值。
* `--compression_ratio_threshold` 压缩比的阈值，默认为 2.4。当 compression\_ratio\_threshold 高于预设时，将不对该片段进行转录。

`--no_speech_threshold 0.5 --logprob_threshold None --compression_ratio_threshold 2.2` 是我常用的参数，你可以按视频情况来调节。

## 转录成果

「夜のヒットスタジオ・スペシャル」：

「中森明菜デビュー 40 周年 女神の熱唱！喝采は今も」：

Whisper 对谈话片段识别不错，但歌曲转录与原意相差甚远。而我特别喜欢中森明菜的歌，所以在转录第二个视频后，特意花了几个小时重新比对歌词。

但视频发布后，B 站给我推送了明菜[歌迷会](https://www.bilibili.com/video/BV1x24y127ZZ)在一周前发布的带字幕视频。原本我有些沮丧，想着白花工夫了。但我看过对方专业的字幕视频后，心情立马变好了。歌迷会版本的字幕遣词造句都非常讲究，明显是日语精通级别，而我连五十音都没背全，用 10 分钟就能做出能看懂的字幕，质量也没相差巨大，我非常满足。之后，我也可以看没字幕的生肉节目了，不用再傻等字幕组的宠幸。

## 更多

除了用 Whisper 转录的字幕来看视频，还能将其用于管理音视频。[@PlatyHsu](https://sspai.com/u/platyhsu/updates) 分享的 [ATP Podcast Search](https://marcoshuerta.com/dash/atp_search/) 启发了我，ATP 用 Whisper 转录给一个做了十年的英文播客做了可搜索的索引。那是否有应用在本地端用字幕管理视频文件？

![boxcnJlPTSgPTXSAE6w14ks6BTb](https://cdn.sspai.com/editor/u_/cdsigqdb34t9mjt23nlg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

这个想法在技术上实现起来不难，甚至飞书妙记已经起到类似效果，但它是在线应用，不支持上传字幕，而且仅支持原生字幕搜索。换句话说，上传日语视频，你必须用日语搜索，即使妙记提供了中文翻译查看，你也不能中文搜索。

目前，我还没找到用字幕管理视频的应用，暂时只能记录下这个想法。笔记软件们继续卷起来，把字幕文件作为数据库索引，通过关键词搜索即可定位到音视频的时间戳，绝对是杀手级功能。

## 最后

今年是 AI 工具的爆发年，多个领域都出现优质的开源工具，极大地提升了我的生活、学习和工作效率。

在遇到 Whisper 前，我用 YouTube 的实时字幕看在线视频，但它是通过语言实时转录而非整句转录，导致效果远差于 Whisper。我使用飞书妙记管理本地视频，但飞书只支持中日英语，机器翻译较死板。Whisper 解决了两者存在的问题，转录效果更好，支持语言更多。

然而，与 Whisper 完美的英语转录效果相比，其对非英语视频的转录还有很大的提升空间，期待它的后续更新，也希望字幕组都使用上 Whisper，节省字幕转录时间，加快出片速度。

#### 关联阅读

* [从起因到争议，在 AI 生成艺术元年聊聊 AI](https://sspai.com/post/76277)
* [把 AI 作画引擎搬进家用电脑：Stable Diffusion 配置与使用指南](https://sspai.com/post/75544)

> 少数派请你做地图：城市声音收藏夹[火热征集中](https://sspai.com/post/76807)，期待你创作的城市之声 🎧

> 下载[少数派 2.0 客户端](https://sspai.com/page/client) 、关注[少数派公众号](https://sspai.com/s/J71e)，解锁全新阅读体验 📰

> 实用、好用的[正版软件](https://sspai.com/mall)，少数派为你呈现 🚀

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

[![清顺](https://cdn-static.sspai.com/ui/img-placeholder.png)](https://sspai.com/u/zqj05i4v/updates)

[清顺](https://sspai.com/u/zqj05i4v/updates) ![](https://cdn.sspai.com/ui/badge/matrix_zuozhe.png)

迷信新工具，热衷于研究开源软件、心理学理论，定期分享探索成果

文章来源: https://sspai.com/post/76899
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)