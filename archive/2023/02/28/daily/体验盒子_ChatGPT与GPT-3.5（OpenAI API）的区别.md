---
title: ChatGPT与GPT-3.5（OpenAI API）的区别
url: https://www.uedbox.com/post/68774/
source: 体验盒子
date: 2023-02-28
fetch_date: 2025-10-04T08:15:05.950785
---

# ChatGPT与GPT-3.5（OpenAI API）的区别

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# ChatGPT与GPT-3.5（OpenAI API）的区别

* 发表于 2023年02月27日
* [人工智能](https://www.uedbox.com/ai/)

**网页版chatGPT**和**chatGPT API**区别还是挺大的，具体可从问答中明显感受出来。

* 在[OpenAI官方网页](https://openai.com/blog/chatgpt/)中，我们可以看到官方对ChatGPT的描述为“ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022. You can learn more about the 3.5 series [here](https://beta.openai.com/docs/model-index-for-researchers). ChatGPT and GPT 3.5 were trained on an Azure AI supercomputing infrastructure”，从而得知ChatGPT与GPT-3.5是两个不同产品
* 官方对GPT-3.5系列的[介绍](https://beta.openai.com/docs/model-index-for-researchers)里，
  `text-davinci-003`
  是其中的模型之一
* 我们再查阅官方对OpenAI API KEY的[介绍](https://beta.openai.com/docs/introduction/key-concepts)，其中有一句“The API is powered by a set of models with different capabilities and price points. Our base GPT-3 models are called Davinci, Curie, Babbage and Ada”，davinci赫然在列

目录表

Toggle

+ - [至此，我们可以得出结论：现在所有使用OpenAI API KEY的项目，都不是基于ChatGPT开发的项目，官方并未发布ChatGPT的API接口](#_%E8%87%B3%E6%AD%A4%EF%BC%8C%E6%88%91%E4%BB%AC%E5%8F%AF%E4%BB%A5%E5%BE%97%E5%87%BA%E7%BB%93%E8%AE%BA%EF%BC%9A%E7%8E%B0%E5%9C%A8%E6%89%80%E6%9C%89%E4%BD%BF%E7%94%A8OpenAI_API_KEY%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%8C%E9%83%BD%E4%B8%8D%E6%98%AF%E5%9F%BA%E4%BA%8EChatGPT%E5%BC%80%E5%8F%91%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%8C%E5%AE%98%E6%96%B9%E5%B9%B6%E6%9C%AA%E5%8F%91%E5%B8%83ChatGPT%E7%9A%84API%E6%8E%A5%E5%8F%A3)

* [其他AI相关网站推荐](#%E5%85%B6%E4%BB%96AI%E7%9B%B8%E5%85%B3%E7%BD%91%E7%AB%99%E6%8E%A8%E8%8D%90)
  + [一些好玩的神经网络工具。](#%E4%B8%80%E4%BA%9B%E5%A5%BD%E7%8E%A9%E7%9A%84%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%B7%A5%E5%85%B7%E3%80%82)

#### 至此，我们可以得出结论：现在所有使用OpenAI API KEY的项目， `都不是基于ChatGPT开发的项目` ，官方并未发布ChatGPT的API接口

* 事实上，ChatGPT最近发生过登录认证风波，想了解详细过程的可以查看这个[issue](https://github.com/acheong08/ChatGPT/issues/261)
* 如果你自己有分别使用过ChatGPT的官方chat和OpenAI的API接口chat，你会发现API接口chat比ChatGPT的官方chat“笨”得多

## 其他AI相关网站推荐

另外，提供一些AI网站给大家，收集分享一些AI工具（网站），持续更新

* Galileo AI (<https://www.usegalileo.ai/>) 用AI设计生成UI设计
* README 生成器 (<https://readme.rustc.cloud/zh>) 用AI生成完整的GitHub readme
* ChatGPT for StackOverflow (<https://stackoverflow.gg/>) 查看 ChatGPT 对 StackOverflow 上每个问题的回复，甚至是未回答的问题
* 周报生成器 (<https://weeklyreport.avemaria.fun/zh>) 简单描述工作内容，帮你生成完整周报
* email-helper (<https://email-helper.vercel.app/>) AI帮你写邮件
* animeai (<https://animeai.app/>) AI生成漫画风格图片
* autodraw (<https://www.autodraw.com/>) AI辅助绘画
* bearly (<https://bearly.ai/>) AI帮助你阅读、创作，撰写，提高你的工作效率
* poe (<https://quorablog.quora.com/Poe-1>) quora出品的对话式AI工具
* latentlabs (<https://www.latentlabs.art/>) 根据文本生成 360 度全景图
* invideo (<https://invideo.io/ai/>) 根据文本生成视频
* docuchat (<https://www.docuchat.io/>) 上传文档，AI回答对应的问题
* tweetmonk (<https://tweetmonk.com/>) AI帮你打理社交网络
* image-to-sound-fx (<https://huggingface.co/spaces/fffiloni/image-to-sound-fx>) 图片转换为相对应的声音内容
* murf (<https://murf.ai/>) AI生成真人演讲视频
* stockimg (<https://stockimg.ai/>) AI设计图标
* playgroudai (<https://playgroundai.com/>) 获取AI绘图提示词，帮助你编辑图片
* MetaVoice Studio (<https://studio.themetavoice.xyz/>) AI声音编辑平台
* campbell (<https://review.gobudapest.io/>) AI生成评语
* penlope (<https://penelopeai.com/>) AI辅助markdown编辑器
* ChatGPT Detector (<https://huggingface.co/spaces/Hello-SimpleAI/chatgpt-detector-single>) 判断文本是否是AI生成
* humata (<https://app.humata.ai/signin>) 利用AI来分析论文内容
* tosummary (<https://tosummary.com/>) 利用AI提取书籍、YouTube视频摘要

### 一些好玩的神经网络工具。

* <https://www.lalal.ai/> - 从任何音频和视频中提取人声、伴奏和各种乐器的AI。
* <https://tosummary.com/> - 一键式摘要器，对文章、书籍、甚至YouTube视频进行转述。
* <https://www.autoti.io/> - 创建热门Instagram帖子。
* <https://chatbotkit.com/> - 允许您创建聊天机器人。
* <https://colorize.cc/> - 给黑白照片上色。
* <https://aihelperbot.com/> - 构建任何需要的 SQL 查询。
* <https://nuclia.com/> - 聪明的搜索引擎。
* <https://murf.ai/> - 将文本转录成音频。
* <https://debuild.app/> - 帮助编写web应用程序。
* <https://tryellie.com/> - 模仿您的风格，帮您回复电邮。

点赞(9)

打赏

分享

标签：[ChatGPT](https://www.uedbox.com/post/tag/chatgpt/) , [OpenAI](https://www.uedbox.com/post/tag/openai/)  原文连接：**[ChatGPT与GPT-3.5（OpenAI API）的区别](https://www.uedbox.com/post/68774/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[Mac右键终端：快速打开当前目录的终端](https://www.uedbox.com/post/68767/ "Mac右键终端：快速打开当前目录的终端") [Flutter 二次封装Sqlite基类](https://www.uedbox.com/post/68785/ "Flutter 二次封装Sqlite基类")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![ChatGPT 是什么，有什么作用，跟搜索引擎有什么区别？](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT 是什么，有什么作用，跟搜索引擎有什么区别？](https://www.uedbox.com/post/68662/ "ChatGPT 是什么，有什么作用，跟搜索引擎有什么区别？")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT热，一大波 ChatGPT 开源项目诞生了！](https://www.uedbox.com/post/68725/ "ChatGPT热，一大波 ChatGPT 开源项目诞生了！")

[![你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/post/68792/ "你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议")

[![ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/post/68799/ "ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事")

[![ChatGPT 的 12 个主要用例](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT 的 12 个主要用例](https://www.uedbox.com/post/68804/ "ChatGPT 的 12 个主要用例")

[![ChatGPT推荐30岁女人必看的20部电影 ](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT推荐30岁女人必看的20部电影](https://www.uedbox.com/post/68807/ "ChatGPT推荐30岁女人必看的20部电影 ")

[![如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南](https://www.uedbox.com/post/68815/ "如何向 ChatGPT 提问以获得高质量答案：提示技巧工程完全指南")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

[![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/ "AutoGen Studio 容器化部署与维护指南")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

🔥 最新免费域名资源大全 | 永久免费域名获...