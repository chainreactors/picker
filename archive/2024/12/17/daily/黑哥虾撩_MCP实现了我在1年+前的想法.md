---
title: MCP实现了我在1年+前的想法
url: https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484304&idx=1&sn=112438c7fe43760bc25b7fd7a53cec35&chksm=c050c9e1f72740f71a71a8a1fc84c796c97e1e67d6dcb9e9324f85e6b2ee32f4ea5f85096866&scene=58&subscene=0#rd
source: 黑哥虾撩
date: 2024-12-17
fetch_date: 2025-10-06T19:40:18.857884
---

# MCP实现了我在1年+前的想法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcP820f5mCAUHy23B0qsuH5Ob9oIicBVAaPhDTLWQF0eic7T12e1hb43a7Q/0?wx_fmt=jpeg)

# MCP实现了我在1年+前的想法

原创

heige

黑哥虾撩

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcPXbkau5UNTJ7O2s6YI1AHonQhpl17eclWxrTa54mYjRkQ6hFprRa2BA/640?wx_fmt=png&from=appmsg)

在前不久Claude发布了“Computer Use”狂吹了一波进入[Agent 2.0时代](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484242&idx=1&sn=8c3ca9e7cc7175b192756f908109651f&scene=21#wechat_redirect)，我是万万没想到Claude猝不及防发布了一个MCP，当然这个应该快20天之前的事情了，这段时间因为入手了华为Mate70还有Mac mini M4，再加上我的CLaude账号被封，所以没有第一时间体验MCP，当然这段时间我也重新换了个号，折腾了下...

MCP是什么?

没了解的大家可以直接去MCP官网看看

```
https://modelcontextprotocol.io/introduction
```

第一次看官方介绍估计你可能也有点莫名其妙的搞了个啥子“协议”，所以我让ChatGPT给我介绍了下：

> 模型上下文协议（Model Context Protocol，MCP）是一个开放标准，旨在标准化应用程序与大型语言模型（LLM）之间的上下文提供方式。它类似于 AI 应用的 USB-C 接口，提供了一种标准化的方法，将 AI 模型与不同的数据源和工具连接起来。

> MCP 采用客户端-服务器架构，主机应用程序（如 Claude 桌面版、集成开发环境或 AI 工具）可以通过 MCP 连接到多个服务器，这些服务器可以安全地访问本地数据源（如计算机的文件、数据库和服务）以及通过互联网可用的远程服务（如 API）。通过 MCP，开发者可以构建在 LLM 之上的代理和复杂工作流程，实现与数据和工具的集成，并确保在基础设施内的数据安全。

这个基本就是翻译了下官方的那个介绍，于是我让它通俗点：

> MCP（模型上下文协议）可以理解为一种“桥梁”，它让应用程序和大语言模型（LLM）更方便地交流、协作。通过这个协议，应用程序可以更高效地告诉模型需要什么信息，或者提供上下文（比如文件、数据、工具等），从而让模型更聪明、更贴合实际需求。
>
> 举个例子，就像一个万能插头，MCP标准化了各种设备（模型和应用）的连接方式，不用开发者为不同的接口操心。它还能保证在使用过程中数据是安全的，非常适合需要用到本地数据或者工具的场景，比如开发AI助手、自动化工具或者复杂的数据分析工作。

其实我看到这个还是有点“莫名其妙”，实际体验一把后，其实就是Claude就是实现了一个ChatGPT的GPTs，也就是一套Agent开发调用的框架，当然MCP这个是开源的，在这之前Claude一直是没有推出官方类似于GPTs这种agent的平台服务的，跟大家之前熟悉的langchain、dify等，从最终的实现的效果来看其实是一样的，当然你在开发角度去理解肯定存在一些理念或者说侧重点不一样...

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcPqFuMzMBe4hSfFt4Ea5ajOd5nqiboedxN38xdF8EuCTNW70hrfCDibesw/640?wx_fmt=png&from=appmsg)

MCP实现了我在1年+前的想法

Agent这个方向我觉得是大模型生态中最开始卷的一个方向，而且也是最被看好的一个方向，这个是大模型能大规模实际应用的必然。在1年+前我看到了第一个安全领域里的应用，之前我在朋友圈及ppt里有提到过 “AI安全助手” ：

```
https://github.com/opensec-cn/opensec-cn.github.io/issues/2
```

 在当时还是非常不错的尝试的，非常有开创性的，我记得当时还没有GPTs

我当时看到这个项目就联系了作者wolf，他当时实现的是B/S模式，这个其实跟GPTs的方式一样他把对应的插件（Call Function/Tool）放在他的服务器上跑，这种模式有着天然的缺陷，而且存在各种安全隐患，我当时还测试发现了好几个安全问题，比如浏览器调用的插件可以直接访问服务器本地文件这种，其实这也是Agent应用场景下很常见的漏洞模型，当然还有一些就是隐私的顾虑，还有就是扩展性问题，于是我建议他应该出一个客户端版本，插件可以放在本地使用的文件操作、命令操作、网络操作都是在用户本地环境中，这种可以扩展的场景会非常多～

大概1-2个月后wolf就上线了客户端版本，可惜他使用了Docker，也就是把一个一个插件放在容器中跑，其实这个还是局限安全场景下，另外插件也没有实现进一步的类似于“工作流/链”的调用，当时我比较期待的还有一个就是客户端与服务端分离的设计，也就是我可以把这种agent框架跑在任意的环境下（包括服务器、移动设备等），然后通过插件平台分发对应的插件，这样可以扩展的场景就不仅仅局限在“纯安全”应用场景下了 ...

MCP这个设计很接近当时我跟wolf提到的那些设计了，不过在客户端与服务端分离的这个问题上可能还没有很好的实现实际例子，看官方的介绍有Server-Sent Events (SSE)

```
https://modelcontextprotocol.io/docs/concepts/transports#transports
```

 这种方式是不是可以实现，就看后面的各种应用场景优化了，当然你也可以直接通过本机写个MCP server去操作（比如ssh）服务器的曲线路子实现这个目的，也是可以的。

MCP的核心

我们要解决大模型应用的问题，核心就在于处理数据与大模型“沟通”的问题，在这个角度上去理解MCP官方的定义介绍可能就非常好理解了，所以在本地运行环境可能更接近用户数据源，所以GPTs这种在局限在官方的运行的环境下，接近用户数据的也就是通过API的方式调用了，当然Agent的还有一个就是数据源处理后的动作执行判断，这个执行动作也是在GPTs或者Docker这种环境里很多场景下还是非常受限制的。

所以Claude把MCP定义为一种协议，是非常能体现出他们的核心理解。

MCP的应用

在MCP发布的时候，发布了多个官方的开发的Model Context Protocol servers

```
https://github.com/modelcontextprotocol/servers
```

 当然也吸引了不少开发者的响应，在上面github页面里可以看到很多社区的MCP server的Third-Party项目，设置已经出现了“应用市场”：

```
https://mcp.so/
```

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcP88UcqlnAWPUDDMv5CpHBZPgP1wDoJWKCbRBNXNxd5t1aRbHlfozKfQ/640?wx_fmt=png&from=appmsg)

到目前为止已经看到了343个MCP Servers了，里面还是有很多很有意思的项目

当然这个MCP也不局限在官方的那几个Claude客户端的调用，也可以通过开发第三方客户端调用，比如：

```
https://github.com/chrishayuk/mcp-cli
```

 这个项目，就实现了：

> Support for multiple providers and models:
>
> Providers: OpenAI, Ollama.
>
> Default models: gpt-4o-mini for OpenAI, qwen2.5-coder for Ollama.

还有Gui的项目，比如：

```
https://github.com/daodao97/chatmcp
```

 目前实现了“OpenAI LLM Model”调用

不过在我的实际测试mcp-cli项目时发现，我使用本地Ollama的的调用效果跟Claude客户端是没有办法比的，核心可能在于大模型本身的能力，还有第三方开发调用及对应MCP Server涉及到的“提示词”工程还是有很大的关系，所以如果想要进行私有化的落地还是得针对性根据模型进行优化～

MCP Server开发

在这段时间里其实我也折腾了下MCP Server的开发，官方提供了Python SDK 、TypeScript SDK 相比之我比较熟悉Python点，当然其实我Python也是非常有限的，不过在大模型时代，已经实现了开发自由了很多时候交给大模型开发就行了！是的，这个时候就轮到之前给大家吹嘘安利过无数次的Cursor上场了，因为MCP这个是个全新的玩意，在使用Cursor的时候，还是非常被动的，如果你不说明清楚，很可能就串台到啥“工控”啥的上面去了，所以对于这些比较新的概念，你得先让大模型学习下对应的知识，还好Cursor等都已经考虑到这种文档类的东西了，所以直接在Cursor 对话框里 @https://modelcontextprotocol.io/introduction 让他学习下是MCP当然，这个官方的文档其实写的比较简陋的，测试几次感觉直接写效果不太行，于是我想着能不能让他先学习下官方给出的来源代码：

```
https://github.com/modelcontextprotocol/servers
```

直接git clone下来后，用Cursor打开src这个目录项目，然后让他学习下time这个MCP server的代码，然后他就会写了，直接在Composer生成你想要的项目就行了，比如直接生成一个计算md5hash的 MCP server直接一次性生成好好了，可惜当时的Cursor Chat记录被我删除了，没办法给你们代码生成的图，直接看下Claude客户端调用的效果图吧

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcP7uFWxaTbLQTKkX4lLLibFlVPP8026LScnIK1tvjsAia4BhdQnFqVlzJw/640?wx_fmt=png&from=appmsg)

在这里我想要吐槽下的就是MacOS下的Python开发环境的配置环境变量的配置真是一言难尽，尤其是对我这种开发萌新选手来说，简直是噩梦！而且我还结合了大模型给的建议，好几次大模型都懵逼了！比如我当时在测试claude客户端配置调用具体的MCP server时，用uv可以，但是用python -m 调用是否不行，折腾了好久才发现Claude.app可能是硬编码python了

```
sudo ln -s $(pyenv which python) /usr/local/bin/python
```

尝试这个ln才搞定，当然其实在配置文件里写python的完整路径也是可以的。所以在这里建议如果你是跟我一样是开发小白，在可以选开发语言或者环境的时候，尽量别选python，那都是坑！

其实你调试通了后，开发就很简单了Cursor就直接帮你搞定了，比如我开发个ZoomEye-MCP-Server、还有我们创宇智脑GAC的Gac--MCP-Server，你就只需要告诉Cursor对应的api调用文档或者Curl包给他就行了，效果大体如下：

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcP3n2kMib6OmLgeRdxAqYvAGMOh9iaWMryOCTywJWTyWlib6nbDmsibtXRpA/640?wx_fmt=png&from=appmsg)

这里有个细节点，我提示词是ZoomEye搜索，然后Claude客户端自动关联了到了ZoomEye MCP Server的search\_host 及 Gac MCP Server的ip\_analysls的两个工具的Calling

需要注意的是在API调用的时候如果数据量大，建议在API输出后在MCP-Server进行处理后提交给LLM，要不然可能会处理不过来！

我也在使用上面提到的mcp-cli测试了下Ollama的效果使用的模型为llama3.1 测试的效果肯定是不如Claude客户端的：

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcPkW92jzQCOyVw5ia17qHvdpFO7yEVp0f424ZxGVnTjSbEA7Yz9dHkZiaQ/640?wx_fmt=png&from=appmsg)

按原始设计Tool Call输入IP时，应该启用ZoomEye的语法词IP过滤器也就是ip:185.215.113.9 才对，当然这个不怎么影响结果。

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcPa9n5ltY76wuznqvjqxg1malvbEFzfwzETRkzOFWAmlibBqTLBdhRDjw/640?wx_fmt=png&from=appmsg)

这个是Tool Call search\_host 触发ZoomEye API请求后的数据，提交给大模型进行推理，大体的整体效果也需要再通过提示词工程优化。

后面我追踪调试了下可能需要做进一步提示词的优化去理解返回及Call Tool的调用，因为我开发环境还是i9的iMac，所以我想着是不是可以调用我在最新的Mac mini M4上的大模型api，测试了Ollama及LM Studio 代码我就让cursor帮我改，不过最后测试发现在Call Tool环节一种都不能成功，目前估计还是跟提示词的理解有关系～

Agent 1.0/2.0

在开头我提到的那篇文章里关于“AI Agent 进入2.0时代”的文章里，实际上在后续的一些测试中发现还有一些问题，顺带在这里一起交代一下：

关于智谱的AutoGLM

智谱的AutoGLM 实际上还是在Agent 1.0的传统模式，基于事先“剧本”定义的模式，跟Claude computer-use这种“所见所得（推理）”的模式还是有本质上的差别的，在11月29日看到智谱发布会上介绍更加肯定了，而且当时他们介绍他们的所谓的“Agent 有 Emergent Ability” 也就是“涌现能力”，结果一看例子，还是提示词已经把操作流程“剧本”写进去了...

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusy2MEzWLZrZ5qW2kFyvCbcPzhtLNwpbibY6MnLrUFsJKxkicVrsaDnG40FfYiclhlV63aDXyPlFLkVOw/640?wx_fmt=png&from=appmsg)

非常有天朝特色的“小聪明”！当然目前这个也是主流方法，尤其是在手机端的AI布局竞争中，大家基本都是基于这种方式的调用，我其实一直都比较关注手机上的融合，因为国内iphone16限制使用的问题，所以入手了华为Mate70 Pro我核心也是为了手机端的大模型体验，整体感觉还是不错的，尤其是在调用大模型的方式上，鸿蒙next的方式非常多，可扩展的场景也非常多，可以看看我视频号上发的那些测试视频，不过这几天OpenAI挤牙膏发布会宣布iphone Siri深度融合了ChatGPT看一些测试视频效果来看确实要比之前很简单粗暴的融合要好很多，相比之下国内的手机上的调用最终还是大模型的推理能力上，目前这块还是OpenAI最强，尤其是这2天又发布了告你高级视频对话功能，还是非常惊艳的！（测试效果视频都可以看看我的视频号），其实这个视频功能跟Claude Computer Use是类似的“所见所得（推理）”的，之前就有人利用Claude Computer Use的做了个一个工地摄像头获取工地画面进行工地安全隐患的应用。

关于Agent 2.0安全问题

在前面我做了一个关于“[Claude Computer Use 提示词注入攻击演示](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484261&idx=1&sn=b5274b1e9c3502161d116f9817861fbb&scene=21#wechat_redirect)”，但是没有聊怎么防御的问题，实际上我感觉是确实是不太好防的，而且我觉得可能是影响广泛应用的"拦路虎"，因为改变了“输入”场景，攻击者可以通过“篡改”、“植入”的方式把“提示词”注入到具体的场景里，从而改变影响大模型的最终决策。在做“Claude Computer Use 提示词注入攻击演示”时候我一直在思考一个问题怎么识别出是不是大模型访问的问题，随后就看到了在Claude的黑客马拉松的比赛中，有人做了一个怎么防御“避免被 Claude Computer Use 破解验证码”的问题，因为在Claude Computer Use发布的时候已经有很多人就尝试过用来自动化破解验证码了（我在之前讲大模型安全应用的时候就提到了大模型来识别验证码的问题），还是非常有创意的，如果没有看过大家可以去看看：

```
https://weibo.com/5648162302/5098006686208067?comefrom=longpicweibo&pic_share_from=long_top
```

至于防御问题直接引用我朋友圈里发的内容：

> 这个挺有意思的方案，前面我还在想怎么识别AI操作还是人类操作，我在前面直播的时候也聊到怎么防御前面视频号演示的提示词注入的问题，可以考虑加入类似于“逆反馈”的COT机制去让模型接下来的动作是不是符合用户的原始诉求，应该是可以做到一定程度的缓解作用，在验证码这个维度他们这个设计确实还是非常有意思的，看起来我的“错别字”不仅仅是防伪标志了，而且还是是不AI的有效方案：比如我在问题中加入了错别字，如果AI的答案得到纠正，那...