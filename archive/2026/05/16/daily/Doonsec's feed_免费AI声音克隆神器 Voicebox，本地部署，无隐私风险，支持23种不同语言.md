---
title: 免费AI声音克隆神器 Voicebox，本地部署，无隐私风险，支持23种不同语言
url: https://mp.weixin.qq.com/s/aBX46ulFlPg6Hpjy6xuj4w
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:09.331791
---

# 免费AI声音克隆神器 Voicebox，本地部署，无隐私风险，支持23种不同语言

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjWiaeNGN6ibXOVNjteXxPk2XMtPslicsfveuKpE4pygsNuDE6CUnvpTVaHAEWNMjRw3I9ad88d0xpQ4wa5WUQF9qVibCzDRelibhm9Q/0?wx_fmt=jpeg)

# 免费AI声音克隆神器 Voicebox，本地部署，无隐私风险，支持23种不同语言

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Voicebox 是一款**以本地化为核心的 AI 语音工作室，它是一款免费开源的应用程序，可以替代**ElevenLabs**和**WisprFlow**。只需从几秒钟的音频中就可克隆语音，使用 7 个 TTS 引擎生成 23 种语言的语音，通过全局热键在任何文本字段中进行语音输入，并为任何支持 MCP 的 AI 代理赋予选择的声音。**

**两大云端语音处理服务商分别位于语音输入/输出回路的两端——ElevenLabs 负责输出，WisprFlow 负责输入。Voicebox 则兼顾两者，并通过捆绑的本地 LLM 实现语音精细化和个性化设置，所有功能都在本地计算机上运行。**

**优势：**

* **完全隐私：模型、语音数据和采集内容不会离开本地设备，不会上传到云端。**
* **7款 TTS 引擎：Qwen3-TTS、Qwen CustomVoice、LuxTTS、Chatterbox Multilingual、Chatterbox Turbo、HumeAI TADA 和 Kokoro。**
* **支持23种语言：从英语到阿拉伯语、日语、印地语、斯瓦希里语等等，包括中文。基本上主流的语言它都支持。**
* **长度不限：没有长度的限制，但要生成的越长，点设备所要的配置就越高。脚本、文章和章节自动分段并带有淡入淡出效果。**
* **语音输入：全局听写快捷键，支持按键说话和切换模式；macOS 系统下支持辅助功能验证的自动粘贴功能；每个文本字段都内置麦克风；支持基于 Whisper 的语音转文本功能。**
* **API优先：REST API加上内置的MCP服务器，可将语音I/O集成到自己的应用程序和代理中。**
* **支持多平台运行：macOS（MLX/Metal）、Windows（CUDA）、Linux、Docker。**
* **......**

**声明：**

**本文基于开源项目 Voicebox（GitHub：jamiepine/voicebox）进行整理与实践记录，仅用于技术学习与交流用途，不涉及任何商业用途。**

需要特别说明的是，Voicebox 虽然提供了声音克隆与语音生成能力，但这类技术本身具有一定敏感性。

在实际使用过程中，请务必遵守基本的法律与伦理规范：

* 不得在未获得授权的情况下，克隆或模拟他人的声音用于商业用途或对外传播
* 不得利用声音克隆技术冒充他人身份，或用于误导、欺骗性场景
* 不得生成涉及侵权、违法或不当用途的语音内容
* 建议仅使用本人声音或已获得明确授权的音频数据进行测试与创作

AI 语音技术本质上是一种工具，它的价值取决于使用方式。
在合理、合规的前提下，它可以极大提升创作效率；但如果越过边界，也可能带来不必要的风险。

本文仅作为技术学习与工具体验记录，不鼓励任何违规或不当使用行为。

**项目地址：**

```
https://github.com/jamiepine/voicebox
```

**记得给作者点个 Star。**

**安装方法很简单，我的电脑是Windows系统。根据自己的电脑设备来对应下载安装包。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjU1m1nbOIrzZaLX6ePITCBB8GiaZ0KhgkL3nKLNnXgVJYEI8F7NicNibx8ICP13kj0NBPiaBW6iadlcO1xGXcV2Nic4NiaZgcSknR8HoY/640?wx_fmt=png&from=appmsg)

**安装过程只需一路下一步就行，中间唯一需要改的就是安装路径，这个按需修改就行。**

**安装完成之后运行软件。进入这个软件的时间不同电脑配置时间上就不同，配置好点进入软件就快，配置不怎么好，就会进入慢点。**

首先刚进入，也就是左边第一个标签页。这个页面就是我们要克隆的声音源。后边我们创建声音源和生成克隆声音，就是在这里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXuI5NDOfSO8gAZJ8aSnXcicU68EZvk2Ae7HgP5q5Im1UbAQPxZibG7YFuwuuEpoZyRkVQsxr4yGwY44xLWuNNjn2wMiaq2fX6N68/640?wx_fmt=png&from=appmsg)

第二个标签页，这里主要是提供了一个简单的时间线编辑器，让你可以同时编辑多段的语音。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUBIh3ykc2MQx7BfpcpGUTmK0Q1ZB9vibdeEZRfTS8IOuyZtpC7pzDlTqu135GcbuxFeQ3Tqj3osUqZfQRiahtOwzMAs5wdwgZd4/640?wx_fmt=png&from=appmsg)

第三个标签页，这个主要是实时监听你的麦克风，然后自动转文字，你说话后，Qwen3大模型或者其它模型，会帮你优化文本，最终输出自然语言。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjV4WGJYlS6DsRFZg6szibfzdDz4ILXaXuzatzIoibd6Ad10nwBR7RBQatvfibzS8fShLsteI3IPJ877G1UbcaiaHrh8qDCQTziadA1A/640?wx_fmt=png&from=appmsg)

第四个标签页，这个页面与第一个页面功能上有点重复，这里主要就是存放你要克隆声音的源文件。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWTrofiabDWWSWgVqTKkadlibG8RkxaZ7xPWupnWhZWicicsOMTJlMkK0vHAXA7DkMLrKMDO23L73AVcV3Wq3BuYjMMdIzhBw0jCfU/640?wx_fmt=png&from=appmsg)

第五个标签页，这里主要是给声音加音效，比如上边写着 机器人、收音机、低沉嗓音等音效。基本上正常是用不到，但你想个声音加个特殊的处理，那么可以使用这个功能。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVtEDKoCRa24OvwYGcfF6ibwXDAcqSFFFsicc0LVy0R0TeEDR8mxHDIF9nyIYdK3R3ic8gCEP2jQGtDgjp1wFw51ssjIOKiaffVrYI/640?wx_fmt=png&from=appmsg)

第六个标签页，这里就是声音克隆的模型，要想克隆声音就要有一个大模型，第一次打开全部都是未下载的，选择一个去下载，建议选择 Qwen TTS 1.7B，这里1.7B是模型的数据集大小，参数越高，效果越好，但同时对硬件也越高。不同参数之间克隆出来的效果差距也是比较明显的。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVraVV1lz2JzXEBZhtueQ0Ht4vX9o9kmUAeo5kHWTDVjAYjgYGNG92vgtMUp7ktt33jibZicm5Eca7JGvPV3TJJaicRFFuvnvdzg8/640?wx_fmt=png&from=appmsg)

选择好要下载的模型，点击它，然后点击下载。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjV0NX3A27XJcLrk90IPuOabrMiawf9ibbFPdPklv5MuTMOgau92otdN3sXYJT7sjPBLaOh4r8cE9B7ZCoHg7F8CibzmbfYDaDNicrw/640?wx_fmt=png&from=appmsg)

下载好之后，它默认是下载到C盘，在上方可以看到存储位置，右侧可以更改存储位置，在别的磁盘创建好文件夹，更改存储位置迁移进去就行。

太方便了，打败了市面上百分之99的工具。

![](https://mmbiz.qpic.cn/mmbiz_jpg/LtibzcRx8GjUpzwkaD5EkMORYYqzqNFdqPqricGn70ha7N8qK5gIKp3E9QLEicKFwLvjtWicyRfPQpN4sgSJPBjnpCUTy0vgv7rbHl271eGqDyU/640?wx_fmt=jpeg&from=appmsg)

下方还有一个语音转录部分模型，这个主要是用于将你声音转文字。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWrLjskU214YcmbRLNe4pLibbibIic5icbq6wej1begibtCfboROImXXWGv2VIJeSZxJT1Xt5mzt2Hzb2kasHyTfq7c0rXxKWes1Ja0/640?wx_fmt=png&from=appmsg)

最后就是设置页面，可以看到常规设置里，它会在后台启动一个服务，后期可以自己写代码使用API去调用访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXN7RQRgPZ1xT7xQmcbDO4wgLc1P9FYHialsKmUaicniaibdmbVG7puJZqgnN4PMq1Xa8SZnN1tojzbFJ8tiavRt46zP5Lg3Gd4bH4w/640?wx_fmt=png&from=appmsg)

之后重点看 GPU 这个页面，因为我是Windows电脑，用的是NVIDIA显卡，它会自动识别我使用的操作系统，来推荐我下载对应的CUDA。

这个功能主要是给 Voicebox 开启 NVIDIA CUDA 加速，因为 Whisper、TTS、声音克隆等，这些AI模型都非常吃算力，如果单靠CPU，那么就会出现：转录慢、生成慢、风扇狂转、延迟高等现象，但如果开启CUDA，启用GPU，速度就会直线提升多倍。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjX18wUzZpozfjcjEQnZGgp7AaSuPTGJ9lgGibWKcvribicLevyMJomBmibNLaLHAqIv1PCFpAzYr8ZITEia6u61icNZ6axoupX7pNXib8/640?wx_fmt=png&from=appmsg)

下载之前你先看看你电脑有没有NVIDIA 显卡，如果有你可以直接点击下载，这是必须的。如果你没有NVIDIA显卡，比如 AMD、Intel核显等，那就不用下载，因为 CUDA 只支持 NVIDIA，你就算下载了，也无法启用GPU，还是会使用CPU来跑模型。

你可以用下方步骤来确定有没有 NVIDIA 显卡👇适用于Windows，其它系统可自行百度。

最快方法，快捷键：

```
Ctrl + Shift + Esc
```

打开任务管理器。

然后：

## 性能 → GPU

如果看到：

* NVIDIA RTX
* NVIDIA GeForce

那就能用 CUDA。

Voicebox 这个设计其实很专业，它不是强制安装 CUDA。而是按需下载，因为CUDA Runtime 很大，很多AI软件安装包直接塞 5GB不等。非NVIDIA用户白白占空间，而Voicebox默认CPU，检测到NVIDIA再启用CUDA，这点Voicebox给我的感觉体验其实做的非常好。

安装完成之后就是这样：

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVq6p8tcPKTCuNpI9WLOB680fib0Wf2czyMCjDPG9tTiamTIuGQNibeFrWz2OUHsjAFjYDJyZwFFtUABDRQ8QtnI4l8TLuBIszLEY/640?wx_fmt=png&from=appmsg)

软件到这里就算是介绍完了，现在简单演示一下声音克隆的操作。

回到第一个页面，点击创建声音。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUqowvicc579ztsIib3ggBkzS98D1nReLHKyKz9D5OhVIPxTpt98AG1HPf4hzFVhzGEwy7wf6hxbUGPAAHV2gdrrptQuDXr6ib9AQ/640?wx_fmt=png&from=appmsg)

它这里可以上传音频，也可以通过麦克风去录制一段声音，系统音频就是录制当前电脑播放的声音。参考文本里建议输入语音的文本，这样更好识别。右侧名称、描述、人物设定按需填写。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjX9bs7ibiaBEkTPk5SKj5l69JjONBkScCCsdP7JZ9rENfEkSA3y1BYTQyetjC9dDRe82LnqPTGZbzribTe5UJokvnEWKaQuOyBuQ8/640?wx_fmt=png&from=appmsg)

重点是语言这里，一定要选择与语音同语言，你语音是中文，你选择的语言就必须是中文，不能是其它语言。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjXo2lSgkSQm0dKzufT5k1QsrhgHbONZlUA9ndWhFXIuexEzTtfyksmvImBHvOvhLBKHhDNqXjN8lGtxIKyKGjqh9O05BFHyFaI/640?wx_fmt=png&from=appmsg)

创建好之后，选择刚刚创建的声音，然后在下方输入你要克隆声音所要说的文本，然后可以选择语言，这里语言就是你克隆声音的语言。模型就选择你下载的模型。模型不同，克隆出来的效果也有所不同。之后点击右侧的类似星星的按钮生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWjs1TlTXrlPqc950UHpicLEzdoA035fDHIeKuLxUibR52ub4SgnoodjPfqsdzBPPOWtrjibGFvib0FX9B7nVTI0IwBicFsBEkFJa6M/640?wx_fmt=png&from=appmsg)

之后右侧就会出现生成的记录。现在的状态就是在加载模型，等Loading model...消失，会自动播放生成好的语音。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjU44v8fkGWnFwvUztfC9XT5IXNPDPkKbZv9fia3TeoT6z1lblicyI4uYTROW5rsoxVdiaEDKyJym1e0ekqHDtHwo6euC8kqFZjRxA/640?wx_fmt=png&from=appmsg)

看效果👇

我提供的声音素材也是AI生成声音，模型用的是Qwen3-TTS 0.6B。整体来说还是挺不错的。要想效果更好，需要上传：清晰，没有杂音，最好10秒，吐字清晰的音频，然后模型选择参数高的模型，才能达到更好的效果。

生成这点语音，就快把我GPU占满了，可见有多吃显卡了，我显卡就4G，这要是换成CPU，风扇不得起飞啊！！！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjV9VJk9dRLG7CXW39ibHjppfpCdIhAe3agnwGP4SUMTfMyVVX5tzWFh3pjFHd0utIzHBC1OnJBccdJXQoWjNhdUHhVSEN4OYfls/640?wx_fmt=png&from=appmsg)

本期内容到此结束。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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