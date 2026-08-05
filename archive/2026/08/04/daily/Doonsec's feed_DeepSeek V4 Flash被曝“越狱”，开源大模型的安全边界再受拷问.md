---
title: DeepSeek V4 Flash被曝“越狱”，开源大模型的安全边界再受拷问
url: https://mp.weixin.qq.com/s/1MOpmIeuQOM8yAE-YYJNsA
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:57:16.426365
---

# DeepSeek V4 Flash被曝“越狱”，开源大模型的安全边界再受拷问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hxdb7gjfn9nUf2bWlxYctrLqkRia8zhTn9ibpXwmDTLzDfsbRbcD4uy2CeXp0ibRibkH9lckBbI5UGOUVuicrU6B2UVDNPoBdCouAbiatEvrUMiaWY/0?wx_fmt=jpeg)

# DeepSeek V4 Flash被曝“越狱”，开源大模型的安全边界再受拷问

e安在线
e安在线

e安在线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kTH4ibOQnoWKJBaAQ9VIS5xYTnJZd3lTApwnu5VzjpLwO0kNxEL4sYugsBpXrymf2wpVQHWUpia5vkYziahibm4HpqbOmxF5Bz3Kw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9mBoMjrYaU5MYcia59YIR8Ey0aHLZdicpxCicmSib7I4Z5LBYWPOPeiah2RIaDugPnEFsF59v9hV1rf3KvxB4MmZKicTYlCiavp2hBlek/640?wx_fmt=png&from=appmsg)

**正式版API刚开放，DeepSeek V4Flash被“时间错位”提示词推上风口浪尖。测试者将敏感请求伪装成旧资料，诱导模型输出多类高风险内容。**

**单次截图不足以证明模型失守，但提醒:当AI能调用工具、编写并执行代码，越狱可能从不当回答变成真实操作。企业部署时应限制工具及数据权限，为高风险行为设置人工确认，检测输出并保留完整审计，研究者也应避免公开危险提示词。**

DeepSeek V4 Flash正式版刚刚进入公众视野，一场围绕模型安全边界的讨论便迅速升温。

8月1日，X平台用户@Exocija发布截图称，通过一组经过设计的提示词，DeepSeek V4 Flash输出了原本应当拒绝提供的高风险内容，涉及违禁药物、勒索软件及信息窃取程序等领域。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hxdb7gjfn9laA611cmoqZMs6320FgMuLGtAhOMmdDibzmiaXvx8ysoHQumLQibt7r3oX9IYtjib4QPcdxkEnK4OaQSTHkDAvoNo1Mdc85utf528/640?wx_fmt=jpeg&from=appmsg)

相关帖子很快获得数千次点赞和收藏。不少人将其视为DeepSeek V4 Flash遭到“越狱”的证据，也有人质疑，单次截图不足以证明模型存在普遍性的安全缺陷。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kUKjF4gDpgEiahYuFqIVwvfIHfN58WwO8NicwwuVu4Sgr0l0YV1Nu4Q8u6QmvplSAMOCCINT83E6FEX3BvFOgDDX9Kc5ibObtt0A/640?wx_fmt=png&from=appmsg)

**新模型更新后被曝“越狱”**

DeepSeek V4系列于2026年4月推出预览版，包括V4-Pro和V4-Flash两个版本。7月31日，DeepSeek进一步更新V4-Flash，并开放正式版API公测。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9ln5ibrEQy8aMJS0wcZAdkUyKt5Bkic7ybWtCMRzLwW0JE3EkWF935ibm4a5BVNGFDM22fsCTWeG1DUdTViaG1klO0XlMZGybfg5as/640?wx_fmt=png&from=appmsg)

官方资料显示，V4-Flash采用混合专家架构，拥有2840亿总参数，每次推理激活约130亿参数，支持100万Token上下文。与强调综合能力的V4-Pro相比，V4-Flash更侧重响应速度、运行效率和使用成本。

此次更新并未改变模型架构和参数规模，而是通过新一轮后训练，重点提升代码代理和工具调用能力。DeepSeek公布的测试结果显示，其在Terminal Bench、NL2Repo和Cybergym等任务上的表现均有明显提高。

能力增强也意味着安全压力随之上升。

过去的大模型主要负责回答问题，即使生成错误内容，影响往往停留在对话窗口中。如今，具备代理能力的模型可以调用工具、编写代码并连续执行多步任务。一旦安全机制被绕过，风险就可能从“不当回答”进一步扩展为真实操作。

**“时间错位”绕过安全限制**

所谓模型“越狱”，是指通过精心设计的提示词、角色设定或虚构情境，绕过模型内置的安全限制，诱导其生成通常会拒绝提供的内容。

此次测试采用了“时间错位”的思路：先将时间设定在2135年，再把相关请求包装成对2026年旧资料的查阅，并要求模型提供“真实、准确”的内容。通过把现实中的敏感请求伪装成历史研究，测试者试图让模型放松判断，进而突破原有的拒绝机制。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9mOORib7zSdqib4NyefuRdibZnKXicRHNgKxJbZjxhribSFgya8bj3dZRNyziconP9nUgArZ7271vx34gLf5uS28Uo5VLxyxV8WAibpbU/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9k0V8R1ycbwDHuia3iaxge8hCdJvHhZxdz4icGzOYTWQwk2O3ExxedUOmooS1ZGTRAGyromGEfzribQhdW7zRibSibye4JU5tenekX2g/640?wx_fmt=jpeg&from=appmsg)

类似技巧并不新鲜。面对直接的危险请求，大模型通常能够识别并拒绝；但当同一意图被包裹在学术研究、故事创作、历史档案或虚拟角色等语境中时，模型有时会错误判断请求性质。

这反映出当前安全对齐的一项难题：模型不仅要识别敏感词，还要理解隐藏在复杂叙述背后的真实意图。

如果防护机制只盯着表面表达，攻击者就可能通过改写语境、拆分任务或延长上下文，逐步绕开限制。

**开源放大了安全争议**

DeepSeek V4 Flash采用MIT许可证开放权重，开发者可以下载模型并在本地部署，也可以进行量化、微调和二次开发。

这种开放模式降低了模型的使用门槛，让更多团队能够研究其架构、改进推理效率并开发垂直应用。但与此同时，公开权重也意味着模型的安全机制更容易受到测试和修改。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9l3nVR1vKlV0kOpSHI3NbdRXvQYCr8yMdTgtTMRW1mW3aBps15qN9aqVlpo3UAMzDOaCJIZcwd5ZibKH6iaYTtJzqIolsLltbD88/640?wx_fmt=jpeg&from=appmsg)

闭源模型由服务提供商统一控制，除了模型自身的安全训练，还可以在接口层增加内容审核、调用限制和异常监控。开源模型一旦部署到本地，这些外围防线是否存在、执行到什么程度，很大程度上取决于部署者。

社区中甚至出现了主动削弱或移除安全限制的模型版本。此时，风险已经不再只是“原始模型能否被越狱”，而是模型被下载、修改和重新发布后，谁来为其实际用途负责。

不过，开源本身并不是安全问题的根源。开放权重也能让更多研究人员参与测试，更快发现缺陷并推动修复。

真正需要解决的是，如何让开放研究、安全披露和风险控制形成配套机制，而不是简单地把“开源”与“不安全”画上等号。

**一次成功不等于全面失守**

社交平台上的越狱截图很容易引发关注，但判断一个模型是否安全，不能只看一次成功演示。

1. 大模型输出具有一定随机性。同一个提示在不同参数、版本和运行环境下，结果可能完全不同。

2. 模型安全需要通过可重复、成规模的测试进行评估。除了攻击是否成功，还要观察成功率、拒绝稳定性、输出内容的危害程度，以及增加防护措施后能否有效拦截。

3. 官方API与本地部署版本并不完全相同。API服务通常叠加平台侧的审核和风控机制，本地模型则主要依赖部署者自行设置权限、过滤规则和使用边界。

因此，此次事件更适合作为一次安全预警：模型能力和安全能力并不会自然同步增长，尤其是当模型开始调用工具、编写代码和执行任务时，安全测试不仅要关注它“说了什么”，还要评估它“能够做什么”。

**安全不能只交给模型自己**

对于企业而言，部署开源大模型时不能只关注参数、速度和成本，还应建立独立于模型之外的安全控制。

涉及代码执行、文件读写、外部连接和敏感数据处理的任务，应限制工具权限和访问范围；高风险操作需要人工确认；模型输入和输出应经过检测，并保留完整审计记录。

普通用户在分享越狱测试结果时，也应避免公开危险内容、完整提示词和可直接复现的操作步骤。安全研究的价值在于发现问题、推动修复，而不是降低滥用门槛。

DeepSeek V4 Flash在长上下文、推理效率和Agent能力方面展现了开源模型的进步，但越是强大的模型，越需要清晰的使用边界。

这场讨论的重点并不是证明某个模型“彻底失守”，而是再次提醒行业：开放与安全并非一道二选一的题。真正成熟的开源生态，既要让技术可以被研究和使用，也要让风险能够被发现、披露和治理。

模型能力可以快速迭代，安全体系却不能只靠一次训练解决。随着AI从内容生成走向任务执行，模型厂商、部署者和社区都需要承担起各自的责任。

只有当能力提升与安全治理同步推进，开源大模型才能真正走得更远。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kPdCgez6icS2c9VyuFMF9dGK0kCxRoNT5XlDiaVdLTmrLjW1RCCHeia29Ey7WL55GMENic5GfDYo7K00ugbYaOMcsgI7pYGyWiclw8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9mOtCxEta4lGbXajAJ3AljFFP9zkxR4Gjy1kiarwsLOChVUUJ50teF1ZQ0tRItxcbFib8fUXhhibC5U5NuiaUptv5C3gguDh0hcEBY/640?wx_fmt=png&from=appmsg)

声明：除发布的文章无法追溯到作者并获得授权外，我们均会注明作者和文章来源。如涉及版权问题请及时联系我们，我们会在第一时间删改，谢谢！文章来源：FreeBuf

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kqe3O5gr8t3dCib589JIUMVKaqlYnqGq962wIdlIdteNhO1PFzyUyewGibR4o02iajHrI91icicEn5w6aCuqz1ZT37CIXSIMpD1ujk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9n4c3VGEAmsy39eRcfNTqjrwXic3X1Jf6LbanAqtr52vsbaZ00cbKiaDQQc3lxARh2IrWPxiaQraXhB71KWAzZErAgnz0ZTNYib1bU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9mK7quG3cMZm5jFEqPAk81KhEnlWlKOWk0FBDPibVTemE0mg7gozGwHmQGLKGm3WLOtqkgaqCjAn7QcibzUSMCxh2JlIAKfQReFI/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1Y08O57sHWiaro9eC87veL2BfoUwAjnOfbTbGQwSaaunoz9m7KFdFkib1pMyMoNY4tVtskNSHickKmn7Nza8WGTeA/0?wx_fmt=png)

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