---
title: 超强AI对话系统ChatGPT不完全案例指南
url: https://www.uedbox.com/post/68659/
source: 体验盒子
date: 2022-12-07
fetch_date: 2025-10-04T00:41:12.141303
---

# 超强AI对话系统ChatGPT不完全案例指南

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

# 超强AI对话系统ChatGPT不完全案例指南

* 发表于 2022年12月06日
* [人工智能](https://www.uedbox.com/ai/)

12月1日OpenAI官宣了其目前最强的AI对话系统之后，大家发现这个强大的系统能做的事情远超过大家的想象。我们也在第一时间发布了相关的博客：<https://datalearner.com/blog/1051669904657253> 。由于这个系统实在是太过强大，大家发现的能力越来越强。连Musk也在几个小时之前感叹这个系统是so much better at bullshit than they are！在这篇博客中，我们将收集关于这个系统目前的使用案例，给大家一个更加全面的展示结果。

* [一、官方对ChatGPT系统的介绍](https://www.datalearner.com/blog/1051670116244987#%E4%B8%80%E3%80%81%E5%AE%98%E6%96%B9%E5%AF%B9ChatGPT%E7%B3%BB%E7%BB%9F%E7%9A%84%E4%BB%8B%E7%BB%8D)
* [二、ChatGPT的使用案例](https://www.datalearner.com/blog/1051670116244987#%E4%BA%8C%E3%80%81ChatGPT%E7%9A%84%E4%BD%BF%E7%94%A8%E6%A1%88%E4%BE%8B)
* [三、ChatGPT更多的技术细节](https://www.datalearner.com/blog/1051670116244987#%E4%B8%89%E3%80%81ChatGPT%E6%9B%B4%E5%A4%9A%E7%9A%84%E6%8A%80%E6%9C%AF%E7%BB%86%E8%8A%82)

目录表

Toggle

* [官方对ChatGPT系统的介绍](#%E5%AE%98%E6%96%B9%E5%AF%B9ChatGPT%E7%B3%BB%E7%BB%9F%E7%9A%84%E4%BB%8B%E7%BB%8D)
* [ChatGPT的使用案例](#ChatGPT%E7%9A%84%E4%BD%BF%E7%94%A8%E6%A1%88%E4%BE%8B)
* [ChatGPT更多的技术细节](#ChatGPT%E6%9B%B4%E5%A4%9A%E7%9A%84%E6%8A%80%E6%9C%AF%E7%BB%86%E8%8A%82)

## 官方对ChatGPT系统的介绍

官方博客中介绍到，ChatGPT是基于GPT-3.5（模型card：<https://datalearner.com/ai-resources/pretrained-models/gpt-3-5> ）微调的结果。ChatGPT是InstructGPT的兄弟模型（InstructGPT是官方训练的一个比GPT-3更好的遵循用户意图的语言模型，是基于OpenAI的alignment research技术研发的，比GPT-3更强的语言模型）。

ChatGPT的训练使用了基于人类反馈的强化学习（ Reinforcement Learning from Human Feedback，RLHF）。这点与InstructGPT一样，但是在数据收集方面有差异。OpenAI使用监督下的微调训练了一个初始模型：人类人工智能trainer提供对话，他们在对话中扮演双方—用户和人工智能助理。这可以让训练者接触到模型编写的建议，以帮助他们组成他们的回应。

![超强AI对话系统ChatGPT不完全案例指南](https://www.uedbox.com/wp-content/uploads/2022/12/b28f8ffe-1ddd-42dc-8c53-446490a98b91.jpeg)

## ChatGPT的使用案例

尽管官方对于ChatGPT的能力描述很简单，但是从实际大家使用的期刊来看，这个系统可以做的事情远超大家想象。这里我们会列举目前收集的ChatGPT的使用案例，供大家参考。

| 案例序号 | 案例名称 | 案例来源 |
| --- | --- | --- |
| 1 | 生成AI Prompt | <https://twitter.com/GuyP/status/1598020781065527296> |
| 2 | 编写iOS SwiftUI APP | <https://twitter.com/avielgr/status/1598895550392197121> |
| 3 | 学习技术 | <https://twitter.com/HamelHusain/status/1598834924848836609> |
| 4 | 写出一个可以生成小鸟图片的Python脚本 | <https://twitter.com/bgavran3/status/1598857248536956928> |
| 5 | 写Javascript脚本 | <https://twitter.com/vertinski/status/1599099368472137729> |
| 6 | 参与SAT考试 | <https://twitter.com/davidtsong/status/1598767389390573569> |
| 7 | 自然语言转成Latex | <https://twitter.com/jdjkelly/status/1598021488795586561> |
| 8 | 解释代码 | <https://twitter.com/goodside/status/1598129631609380864> |
| 9 | 改写故事 | <https://twitter.com/raphaelmilliere/status/1598469100535259136> |
| 10 | debugging代码 | <https://twitter.com/amasad/status/1598042665375105024> |
| 11 | 写计算机网络家庭作业 | <https://twitter.com/abhnvx/status/1598258353196929024> |
| 12 | 替代搜索引擎 | <https://twitter.com/RajJohri2019/status/1598492953764315137> |
| 13 | 创作短剧 | <https://twitter.com/rgodfrey/status/1598162900140445697> |
| 14 | 创作食谱 | <https://twitter.com/stephsmithio/status/1598920887029628928> |
| 15 | 反编译汇编代码 | <https://twitter.com/mahal0z/status/1598536939942006784> |
| 16 | 代写办公邮件 | <https://twitter.com/CubicleApril/status/1598753388895797282> |
| 17 | 写年度总结报告 | <https://twitter.com/shanselman/status/1599073011050872832> |
| 18 | 闲聊 | <https://twitter.com/t3dotgg/status/1598954493680713729> |
| 19 | 撰写技术博客 | <https://twitter.com/goodside/status/1598235521675038722> |
| 20 | 逻辑推理问题 | <https://twitter.com/Robdeprop/status/1598285166971351040> |

以上就是我们收集的关于ChatGPT的一些应用案例，很多内容都是重复的。不过从案例收集的结果来看。ChatGPT在编码上有很好的水平，同时在艺术创作、技术创作、办公、逻辑算术等方面都有很不错的表现。需要注意的是，ChatGPT是支持多轮对话的，它可以和你一起进行多次对话来修补回答。在写app和函数的案例中，如果你对答案不满意，可以要求怎么去修改它。这些案例让很多人认为这就是一个通用型人工智能的雏形，也是GPT-4的结果。

已经有人将ChatGPT的功能集成到一些小工具上变成一个AI助理了。不过由于ChatGPT没有开放的API，所以这种工具可能无法获得发展。

## ChatGPT更多的技术细节

官方没有放出ChatGPT的论文，只描述了一些基本概念。而知乎上已经有这样的问题，还有训练过ChatGPT的童鞋做了回答：<https://www.zhihu.com/question/570189639>

官方博客：<https://openai.com/blog/chatgpt/>
ChatGPT的其它细节我们会跟进。

ChatGPT目前是不联网的状态，所以回答的内容也是2021年之前的。

点赞(1)

打赏

分享

标签：[AI](https://www.uedbox.com/post/tag/ai/) , [ChatGPT](https://www.uedbox.com/post/tag/chatgpt/) , [OpenAI](https://www.uedbox.com/post/tag/openai/)  原文连接：**[超强AI对话系统ChatGPT不完全案例指南](https://www.uedbox.com/post/68659/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[微信小程序抓包方法汇总](https://www.uedbox.com/post/68649/ "微信小程序抓包方法汇总") [ChatGPT 是什么，有什么作用，跟搜索引擎有什么区别？](https://www.uedbox.com/post/68662/ "ChatGPT 是什么，有什么作用，跟搜索引擎有什么区别？")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![免费在线AI图片放大工具推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

免费在线AI图片放大工具推荐](https://www.uedbox.com/post/68787/ "免费在线AI图片放大工具推荐")

[![Mistral 发布首个面向代码开发的大模型](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Mistral 发布首个面向代码开发的大模型](https://www.uedbox.com/post/69627/ "Mistral 发布首个面向代码开发的大模型")

[![你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议](https://www.uedbox.com/post/68792/ "你用错了 ChatGPT！以下是如何领先于 99% 的 ChatGPT 用户的建议")

[![cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

cursor, 一款基于 vscode 的 AI IDE](https://www.uedbox.com/post/69717/ "cursor, 一款基于 vscode 的 AI IDE")

[![ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事](https://www.uedbox.com/post/68799/ "ChatGPT它会接管未来吗？使用 ChatGPT 可以做的 20 件事")

[![两个生成式AI 平台推荐，生产力亲测](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

两个生成式AI 平台推荐，生产力亲测](https://www.uedbox.com/post/69909/ "两个生成式AI 平台推荐，生产力亲测")

[![ChatGPT 的 12 个主要用例](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

ChatGPT 的 12 个主要用例](https://www.uedbox.com/post/68804/ "ChatGPT 的 12 个主要用例")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](https://www.uedbox.com/post/119346/ "Cursor agent ask manual区别")

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

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/them...