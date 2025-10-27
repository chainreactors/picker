---
title: Spokenly macOS 上的语音转文字工具
url: https://blog.einverne.info/post/2025/05/spokenly-voice-dictation-on-device-whisper.html
source: Verne in GitHub
date: 2025-05-19
fetch_date: 2025-10-06T22:23:19.722944
---

# Spokenly macOS 上的语音转文字工具

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# Spokenly macOS 上的语音转文字工具

Posted on 05/18/2025
, Last modified on 05/18/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-05-18-spokenly-voice-dictation-on-device-whisper.md)

前几天我介绍了一款 macOS 下的语音转文字应用 [Aqua Voice](https://blog.einverne.info/post/2025/05/aqua-voice-voice-to-text.html) 用语音的方式提升输入效率，但是 Aqua Voice 它有使用的限制，但是今天我很[偶然](https://www.reddit.com/r/macapps/comments/1kfffhc/spokenly_tiny_29mb_voice_dictation_with_ondevice/)地发现了一款完全免费的，并且可以直接离线使用的语音转文字工具 [[Spokenly]]。

Spokenly 来自一个独立开发者 Vadim Akhmerov，在 macOS 下应用只有 3.3 MB 大小，作者直接利用了本地集成的 Whisper 模型来提升识别准确度和效率，如果用户想使用 GPT-4o 的模型，也可以自己输入 API Key 来使用联网的模型。

## Spokenly 是什么

[Spokenly](https://spokenly.app) 是一个本地的语音转文字应用，可以口述任何的文字，代码，笔记等等。

![nQD3LqMD69](https://pic.einverne.info/images/nQD3LqMD69.png)

## 特性

* 注重隐私，音频不会离开 Mac，调用本地 Whisper 模型
* 可以选择调用 GPT-4o 进行转写
* 内置标点符号和语音控制
* 可以语音打开应用，链接，快捷方式等
* 文件转录，支持 mp3, m4a, wav, flac 以及 mp4, mov 等等格式
* 完全免费，无需登录，本地模型永久免费
* 语音快捷指令，可以设置语音触发调用 macOS 自带的快捷指令

## 使用

初次使用需要设置好权限。

![Pv2g](https://photo.einverne.info/images/2025/05/19/Pv2g.png)
然后可以根据自己的习惯设置触发的快捷键，以及选择适当的模型。我推荐，如果想要使用云端的转录，可以直接用默认的 GPT-4o mini Transcribe 模型。

![PMbw](https://photo.einverne.info/images/2025/05/19/PMbw.png)

如果不想使用在线的模型，可以直接下载本地的 Whisper Large V3 Turbo(Quantized) 模型，这个兼顾了识别速度和准确度。

![PyVc](https://photo.einverne.info/images/2025/05/19/PyVc.png)

Spokenly 使用起来非常简单，通过快捷键触发录制音频，松开快捷键就可以进行转录。

## related

* [[Voicenotes]]
* [[Aqua Voice]]
* [[superwhisper]]
* [[VoiceInk]]
* [[Willow Voice]]
* [[Voice Type]]

## Related Posts

* [Whispering 开源离线的语音转文字应用](/post/2025/08/whispering-open-source-offline-speech-text.html) - 08/20/2025
* [Spokenly macOS 上的语音转文字工具](/post/2025/05/spokenly-voice-dictation-on-device-whisper.html) - 05/18/2025
* [Aqua Voice 利用语音转文字提升产出效率](/post/2025/05/aqua-voice-voice-to-text.html) - 05/11/2025
* [OpenAI 的 Whisper 以及相关模型和项目](/post/2024/09/whisper-and-related.html) - 09/05/2024

---

* [← Previous（前一篇）](/post/2025/05/fider.html "Fider 用户反馈收集投票系统")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/05/namecrane-business-email-provider.html "NameCrane 邮件托管服务体验：超大存储空间的终身邮箱解决方案")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/05/spokenly-voice-dictation-on-device-whisper.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [voice-to-text 3](/tags.html#voice-to-text)
* [tts 5](/tags.html#tts)
* [whisper 6](/tags.html#whisper)
* [mac-whisper 2](/tags.html#mac-whisper)
* [faster-whisper 2](/tags.html#faster-whisper)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").