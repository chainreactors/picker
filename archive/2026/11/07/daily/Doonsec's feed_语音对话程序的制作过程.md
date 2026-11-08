---
title: 语音对话程序的制作过程
url: https://mp.weixin.qq.com/s/XutZyvGzZAcAFsCQftXdKQ
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:13:43.719968
---

# 语音对话程序的制作过程

# 语音对话程序的制作过程

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

目前大家应用多的语言对话程序有早期的小爱同学、天猫精灵到现在的豆包。包括衍生品豆包输入法、千问输入法。

这里面涉及到两块知识点，一个是语音转文字（输入法用的比较多），一个是文字转语音。

硅基流动上正好有用于实验的语音 API，可以用这些 API 构建一个语音对话程序 Demo 。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PepUeTKNN6WMTB6x5S5fibZ5pMd01AIq6JPRpoSZFfDibnibfcKpt7A7eY92o7zGlFXOffdSsZaREgTqeWdkGVEKvjC2UxVibnQGdA/640?wx_fmt=png&from=appmsg)

语音模型一般只有 0.5B 大小，和对话模型动辄671B无法比。构建一个语音对话程序需要三个模型，除了两个语音模型，还要有一个对话模型。

以硅基流动的 API 为例，将模型以及 API key 准备好，其中语音模型的 API url 格式为：

```
https://api.siliconflow.cn/v1/audio/speech
```

模型用的下面几个：

```
文字转语音：FunAudioLLM/CosyVoice2-0.5B语音转文字：FunAudioLLM/SenseVoiceSmall对话模型：deepseek-ai/DeepSeek-V4.1-Flash
```

语音 API 请求的 demo :

```
curl --request POST \  --url https://api.siliconflow.cn/v1/audio/speech \  -H "Authorization: Bearer YOUR_API_KEY" \  -H "Content-Type: application/json" \  -d '{    "model": "fnlp/MOSS-TTSD-v0.5",    "input": "你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦",    "voice": "fnlp/MOSS-TTSD-v0.5:alex",    "response_format": "mp3"  }' --output output.mp3
```

将这几个文件提供给你的代码编程助手，这里用 claude code 示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pf66Jblnuqw4Iib6Vr6BPg65X78Dh0IuuHRu8hvnSc7RXqgib6Ribqt4BKsWrNkWicq14y1m9fNWby658DGMwODLHTudKvHvVjJHMM/640?wx_fmt=png&from=appmsg)

让 claude code 写一个用于演示的 demo :

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PfVkUsZ5naJ20gD1yQu0EneHDex8dtYib9kPW2nRV2Ch6flBcGqEhJ8ia0fHH2r1KD064PBtZKkWvNmP6xMLjmaIXxANSudOSFCc/640?wx_fmt=png&from=appmsg)

因为只是做一个 demo ，不需要界面和自动判断对话是否结束，用回车触发每一轮对话。播放调用的是本地喇叭，输入需要用到麦克风，windows 和 mac 实现上会有一点点区别，和本机硬件相关。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PcWvxqQC8cyq01ZGgymxB0aQSHurSpsIibqBK3IfL54jlsz7lXYkE2KsgiafXqPaac9C5dZApjBVib2RrSDMiaNEv7N5HFLmpBrVKo/640?wx_fmt=png&from=appmsg)

最后效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PdFeQomY2TwZT6zOUu4P3A5A7nb7jVV9JlsCoUIibEpccPu0cXgIxceHAoaiazJ4tuWmgz1FsIsPloWCHevpyc4V1qdlfZBcqTib0/640?wx_fmt=png&from=appmsg)

大概进行了五六轮对话，花费如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PfJOS77zDrKlQiaWZkuTTkpbqG7gMlEW7A9M0ELZZIh72x6MaB0LMg5rWp8nj4gvoBYa2KjjY0VUe9z5llRNRqIQEKRYpEasJhc/640?wx_fmt=png&from=appmsg)

大概花了6分钱，对话只能基于模型自己的知识，无法调用外部工具。如果想做带语音的本地智能体，需要做成 skill 和 mcp 供 agent 调用。语音模块只作为技能，主体还是交给智能体。

这里是个独立的 demo 程序，不能被智能体调用。可以拆成多个模块，供本体调用。

demo 对话演示过程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PdibnPdFj7MoFOHXSMmGgWgJUFQXEJXgMxtDX89W0IFF92T5Qia9ibBIJlpUwv4yU4nPM01knu6ENOSZqEeDWic2197J7YXianLozuk/640?wx_fmt=png&from=appmsg)

语音和对话模型用到的 api 端点：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PcQeaSIAvIRoibYzhEmSzuJPavVcjoFNDgBUZPkAyoTPLe7RicOm9WyhrDQIGq3g95CbcwLCiauial5KXZSNYichykzTneejpCTqcsg/640?wx_fmt=png&from=appmsg)

基础的语音声音生成男声，后续还可以换音色、做成连续监听而不是按键触发。

如果想做编程助手中启用语音，则需要想好何时触发语音。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PcaIMqJaZdqUFy9Jzxp9GqBic7GJB84Kn0G9RURUToiaBHuUOHfRYVrz5KFibDDHGLVWnnAtEcTKBXicgGjcicVfrEtpZhl3u4CvVFY/640?wx_fmt=png&from=appmsg)

硅基流动会给新人16块钱新人券，硅基流动推荐链接如下：

```
https://cloud.siliconflow.cn/i/n6PPXPuJ
```

可以试试用送的 token 写一些大模型的应用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pc6W3uj3gQEBqTWoQpsolF5RRWdR6cjWfiavp1tve6n0QcOPw9mGRxEJFaAw3VLiaxfL6wHRaxyUkq45xaC7WkyK4j8zg6TzI3c0/640?wx_fmt=png&from=appmsg)

全文完。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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