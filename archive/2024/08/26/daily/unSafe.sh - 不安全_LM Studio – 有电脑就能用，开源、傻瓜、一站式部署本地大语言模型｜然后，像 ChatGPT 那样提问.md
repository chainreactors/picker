---
title: LM Studio – 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问
url: https://buaq.net/go-258100.html
source: unSafe.sh - 不安全
date: 2024-08-26
fetch_date: 2025-10-06T18:00:45.937638
---

# LM Studio – 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问

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

![](https://8aqnet.cdn.bcebos.com/9e7100d8454b77566178bb18559ad0fd.jpg)

LM Studio – 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问

HomeAILM Studio – 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问
*2024-8-25 22:57:1
Author: [www.appinn.com(查看原文)](/jump-258100.htm)
阅读量:49
收藏*

---

[Home](https://www.appinn.com)

[AI](https://www.appinn.com/category/ai/)

LM Studio – 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问

**LM Studio** 是一款将目前主流大模型 LLM 元素打包在一起​的工具，可以让你在自己的电脑上，“0门槛”运行本地大语言模型 LLM，并且用起来就像 ChatGPT 那样。支持 Windows、macOS、Linux。@[Appinn](https://www.appinn.com/lm-studio/)​

![LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问](https://www.appinn.com/wp-content/uploads/2024/08/Appinn-feature-images-2024-08-25T221457.341.jpg "LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 1")

傻瓜、一站式部署本地大语言模型，大概就是**打开电脑** > **双击运行程序** > **开始提问** > 获得 AI 回答这样三步走。

## LM Studio

我觉得 LM Studio 就是这样的软件，它长这样：

![LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 1](https://www.appinn.com/wp-content/uploads/2024/08/Appinn-2024-08-25-22.30.56@2x.avif "LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 2")

你唯一需要操心的事情，就是挑选模型，然后下载使用，就好了。

不过整个软件的难点也在这里，因为…目前的主流模型托管网站 [huggingface](https://huggingface.co/) 它不能访问 😂

于是，用镜像也不是不行。

## 下载模型

直接在目前可用的镜像网站 [HF-Mirror](https://hf-mirror.com/) 搜索你需要的模型，比如 `Meta-Llama-3.1-8B-Instruct-GGUF`，然后找到对应的 [Files](https://hf-mirror.com/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main) 页面，挑选你需要的模型，点击那个下载按钮

![LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 2](https://www.appinn.com/wp-content/uploads/2024/08/Appinn-2024-08-25-22.42.17@2x.avif "LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 3")

最终，你将得到一个类似 `Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` 的文件，很大，一般都好几个 GB。

## 安装模型

LM Studio 默认的模型保存路径在 `C:\Users\appinn.cache\lm-studio\models`，可以更换：

![LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 3](https://www.appinn.com/wp-content/uploads/2024/08/Appinn-2024-08-25-22.45.02@2x.avif "LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 4")

不过这里注意，你需要使用 `${Publisher}/${Repository}/${ModelFile}`这样的路径结构，如上图第二个红色框框，需要将手动下载的 .gguf 模型文件保存在路径的两级文件夹下才能正确识别。

然后，就能提问了。会自动使用你的 CPU、GPU…

## 本地 LLM 服务器

LM Studio 也支持 OpenAI 类的服务器，即可以在第三方服务器上使用这个 LLM，就像使用 OpenAI API 一样，只不过这里的 API 服务器是你自己的。

和 OpenAI 一样，使用过 `/v1/chat/completions` 、 `/v1/completions` 、 `/v1/embeddings` 即可。

![LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 4](https://www.appinn.com/wp-content/uploads/2024/08/Appinn-2024-08-25-22.50.35@2x.avif "LM Studio - 有电脑就能用，开源、傻瓜、一站式部署本地大语言模型｜然后，像 ChatGPT 那样提问 5")

## 获取

* [官网](https://lmstudio.ai/)

---

文章来源: https://www.appinn.com/lm-studio/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)