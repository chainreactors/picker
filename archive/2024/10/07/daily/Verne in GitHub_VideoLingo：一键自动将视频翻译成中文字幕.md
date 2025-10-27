---
title: VideoLingo：一键自动将视频翻译成中文字幕
url: https://blog.einverne.info/post/2024/10/videolingo.html
source: Verne in GitHub
date: 2024-10-07
fetch_date: 2025-10-06T18:46:18.818996
---

# VideoLingo：一键自动将视频翻译成中文字幕

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

# VideoLingo：一键自动将视频翻译成中文字幕

Posted on 10/06/2024
, Last modified on 10/06/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-10-06-videolingo.md)

我之前的文章和视频中也介绍过好几款，或收费或开源的视频翻译工具，包括

* 收费的 [MemoAI](https://blog.einverne.info/post/2024/09/memo-ai-audio-transcript.html)
* 收费的 [YPlayer](https://blog.einverne.info/post/2024/08/yplayer-ai-transcript-player.html)
* macOS 下的客户端 [[MacWhisper]]
* 开源的 [pyVideoTrans](https://blog.einverne.info/post/2024/09/pyvideotrans-audio-to-text-to-audio.html)
* 以及许许多多 [Whisper 项目衍生](https://blog.einverne.info/post/2024/09/whisper-and-related.html)

今天再介绍另一款开源的视频字幕自动翻译项目—- VideoLingo。

[VideoLingo](https://github.com/Huanshere/VideoLingo) 是一款开源的视频自动翻译项目，可以将视频进行字幕切割，翻译，对齐，以及配音。

VideoLingo 可以接受 YouTube 链接或者本地视频，可以对视频进行自动转写，并且生成单词级别的转录文件，然后利用 LLM 对原始文本进行翻译，还可以利用 TTS 来生成配音

个人尝试了一下生成 Jensen Huang 的采访，因为使用了 Anthropic 的 AI，所以翻译质量非常高，并且达到了宣称的 Netflix 字幕标准，只有单行的长度，并且中文翻译非常信达雅。

![AJOB0r2lqP](https://pic.einverne.info/images/AJOB0r2lqP.png)

VideoLingo 还采用了多种 TTS 引擎，包括

* OpenAI
* Azure TTS
* [[GPT-SoVITS]]
* [[Fish Audio]] TTS

可以自行配置 API KEY 来生成中文配音，并自动合成到视频中。

## 相关的技术栈

* [[yt-dlp]] 实现 YouTube 视频下载
* [[WhisperX]] 语音转写，进行单词级时间轴字幕识别
* NLP 和 GPT 根据句意进行字幕分割
* GPT 总结提取术语知识库，上下文连贯翻译
* [[TTS]]
  + [[GPT-SoVITS]] 个性化配音，克隆声音并进行配音
* [[Streamlit]]

## 安装

```
# 获取源代码
git clone [email protected]:Huanshere/VideoLingo.git
cd VideoLingo
pyenv virtualenv 3.10.9 videolingo
pyenv local videolingo
pip install -r requirements.txt
python install.py
# 一键启动
streamlit run st.py
```

## 配置说明

### LLM 配置

LLM 配置中需要使用到 [[Anthropic]] 的 API，可以访问 https://gpt.einverne.info 获取 API KEY

### 转录和字幕设置

这里我选择了本地 WhisperX 方法。

### 配音设置

略过

## related

* [[Linly-Dubbing]]

## Related Posts

* [Aqua Voice 利用语音转文字提升产出效率](/post/2025/05/aqua-voice-voice-to-text.html) - 05/11/2025
* [Google Agent2Agent 协议](/post/2025/04/google-agent2agent.html) - 04/10/2025
* [Anthropic 开源 Model Context Protocol(MCP) 创建了 AI 和数据源的双向连接](/post/2024/12/anthropic-model-context-protocol.html) - 12/02/2024
* [JustRecap 将视频转成图文](/post/2024/10/justrecap.html) - 10/20/2024
* [VideoLingo：一键自动将视频翻译成中文字幕](/post/2024/10/videolingo.html) - 10/06/2024
* [EmotiVoice 网易开源的中英文 TTS 引擎](/post/2024/09/emotivoice.html) - 09/20/2024
* [使用 pyVideoTrans 自动进行视频翻译及配音](/post/2024/09/pyvideotrans-audio-to-text-to-audio.html) - 09/11/2024
* [MemoAI 一款跨平台的语音视频转文字工具](/post/2024/09/memo-ai-audio-transcript.html) - 09/03/2024
* [YPlayer 一款支持本地生成字幕的播放器](/post/2024/08/yplayer-ai-transcript-player.html) - 08/26/2024

---

* [← Previous（前一篇）](/post/2024/10/sanity.html "现代化的内容管理系统 Sanity 使用")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/10/screenpipe-your-personal-ai-assistant.html "Screenpipe 私人的 AI 助理 本地记录看到听到的一切")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/10/videolingo.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [videolingo 1](/tags.html#videolingo)
* [anthropic 7](/tags.html#anthropic)
* [openai 22](/tags.html#openai)
* [ai-transcript 6](/tags.html#ai-transcript)
* [audio-transcript 5](/tags.html#audio-transcript)
* [translate 1](/tags.html#translate)
* [video-translate 1](/tags.html#video-translate)
* [text-to-speech 2](/tags.html#text-to-speech)
* [tts 5](/tags.html#tts)
* [subtitle 8](/tags.html#subtitle)
* [subtitle-transcript 3](/tags.html#subtitle-transcript)
* [subtitle-translation 2](/tags.html#subtitle-translation)
* [memoai 3](/tags.html#memoai)
* [pyvideotrans 2](/tags.html#pyvideotrans)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").