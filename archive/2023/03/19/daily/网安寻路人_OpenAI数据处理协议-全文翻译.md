---
title: OpenAI数据处理协议-全文翻译
url: https://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499306&idx=1&sn=e8ec9c1cef1e529b0c8b8d4fa243c4e4&chksm=97e943c0a09ecad670e23f6009a4c13f0548345fe92abf98c4964d8aeae2d980ba4c48893da7&scene=58&subscene=0#rd
source: 网安寻路人
date: 2023-03-19
fetch_date: 2025-10-04T10:03:03.447310
---

# OpenAI数据处理协议-全文翻译

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micOBTnNibZxvJ4NqjZxbgXLuibUeJ8H4vDJE5MVXzMO8Skb7LsAB9Vyib9ZzuvtNoHV5MFmpA26uNppQ/0?wx_fmt=jpeg)

# OpenAI数据处理协议-全文翻译

王新锐等

网安寻路人

**译者按**

关于LLMs（大型语言模型）的风险和监管，本公号发布过以下文章：

1. [ChatGPT是网络上的一个模糊的JPEG文件（外专观点）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499037&idx=1&sn=edf919c148180dbce5fab395d737cb90&chksm=97e940f7a09ec9e1e5f9c62de2ba580d3e35c5d5a5c093c07b7dea83425d4fa6aeee24ca3c0f&scene=21#wechat_redirect)
2. [ChatGPT是如何劫持民主进程（外专观点）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499047&idx=1&sn=d03eecb21b9ebc57280cb2f07fc467a3&chksm=97e940cda09ec9db66b84ad7178bd7e9a52a2e71cb238e3b91ae495eb55acc94aaafd311d95c&scene=21#wechat_redirect)
3. [ChatGPT：欧洲禁止Replika "虚拟伴侣"聊天机器人应用（外媒编译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499054&idx=1&sn=b53342145b2eaacdee56a017294201aa&chksm=97e940c4a09ec9d297cf8792919a347b9e119ab8e32c9fd89f2dd1083370f519faed22ce8c17&scene=21#wechat_redirect)
4. [ChatGPT背后的核心技术【好文转载】](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499104&idx=1&sn=c65ee739966ef5eaa307aa3d4fcad333&chksm=97e9408aa09ec99c49648d0e8cff4c10c4464ae52624c42d8a0631ffa4dd23ae33aeb2b2d626&scene=21#wechat_redirect)
5. [基辛格、施密特等：ChatGPT预示着一场智力革命（外媒编译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499227&idx=1&sn=2e6e03d91c0c0011b435bbd187f9407d&chksm=97e94031a09ec927c1d179c35810e4964ce622e472bf1ca40d27983b25520ade36597e408345&scene=21#wechat_redirect)

今天和大家分享的。译者为王新锐律师团队。

*—*

**译者序言**

OpenAI是一家2015年创立于旧金山的人工智能研究公司，ChatGPT（Chat
Generative Pre-trained Transformer）是OpenAI推出的一款人工智能聊天机器人产品，该款产品基于大语言模型算法，通过强化学习进行训练。根据OpenAI官方网站的介绍，“我们已经训练了一个叫做ChatGPT的模型，它以对话的方式进行互动。对话形式使ChatGPT能够回答后续问题、承认自己的错误、对不正确的前提进行挑战，并拒绝不适当的请求”。

鉴于ChatGPT在与用户交互过程中将涉及包含个人数据/个人信息在内的大量数据，就数据的处理与保护，我们找到了OpenAI《数据处理协议》，该协议旨在对OpenAI与API客户在数据处理活动中各自需要承担的义务、享有的权利进行规定。OpenAI《数据处理协议》从架构上看较为简略，但该协议对于人工智能语境下的数据保护具有较大的参考价值，该协议值得关注的条款主要包括：

1.OpenAI《数据处理协议》通过援引的方式明确其法律依据主要包括《加州消费者隐私法案》（“**CCPA**”）、欧盟《通用数据保护条例》（“**GDPR**”）以及实施前述法律所需适用的其他相关法律法规，同时规定《数据处理协议》双方，即OpenAI和API客户均需要遵守前述法律。OpenAI《数据处理协议》是在CCPA、GDPR语境下的协议。

2.一方面，OpenAI《数据处理协议》规定OpenAI可以为提供、支持和改进其服务的目的处理API客户提供的个人数据/个人信息。另一方面，在数据处理服务终止或在客户的要求下，OpenAI需要返还或删除个人数据/个人信息，但是OpenAI具有继续处理从个人数据/个人信息派生信息以改善其系统和服务的权利，因为该等信息已以无法识别到个人或客户的方式进行聚合。这意味着OpenAI可以使用API客户提供的数据来训练自己的机器学习算法，这可以保证ChatGPT可以持续获得学习资料，以使得ChatGPT越来越智能。

3.当OpenAI直接收到API客户的数据主体提出的关于行使数据主体权利的请求或投诉时，OpenAI将经过客户的事先书面授权才会对该等请求作出回应，这是客户作为数据控制者、OpenAI作为数据处理者的应有之义，同时也避免OpenAI承担其无需承担的责任、避免与数据主体的潜在争议。

我们于近日对OpenAI《数据处理协议》（2020年5月版本）进行了翻译，欢迎大家指正，并一起深入讨论。

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micOBTnNibZxvJ4NqjZxbgXLur5Tgrp9yl4Y445dY0z4FRXwhtGPVib2orSENPtF4WbUbmicINH43icamw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micOBTnNibZxvJ4NqjZxbgXLurKCf7ibY9uq2Mkb1uca2DlZKXIcDTRrNyFadbgU0Ejcjib0rKe8WwCZg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micOBTnNibZxvJ4NqjZxbgXLucCgyUyYMLY7V6OOYpUsWGedWaLX8qlpqFv0L6krYRqIx6FTiaXBkevQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micOBTnNibZxvJ4NqjZxbgXLu8P7XDyFRmkw7jmyawEtuzSBiaib2bsLDF7OtibfIAhM8gibMicNj5hZdu0w/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micOBTnNibZxvJ4NqjZxbgXLuztvib1qVU4GSAkZQbpMUSXyGGptHsR4xib6IGtGblMkP9a13ejxFIxeQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micOBTnNibZxvJ4NqjZxbgXLuMDboPmsHInA8Euj0kqUUR5SgWJNjqOuBG7QZL5uldjfEYBiag1EYkPw/640?wx_fmt=jpeg)

关于人工智能安全和监管，本公号发布过以下文章：

1. [《英国ICO人工智能与数据保护指引》选译 | 如何评估AI的安全性和数据最小化？](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247490369&idx=1&sn=7f628b0a227cc4ed5109aaf3b90883a9&chksm=97eaa6aba09d2fbd0a59bdf0376c067783a8b79a6d9e159641c4728f7cd4063ee80cd1158dc9&scene=21#wechat_redirect)
2. [英国ICO人工智能指导 | 数据分析工具包（全文翻译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247491455&idx=1&sn=0ab1756a63f56cae63936e3958587933&chksm=97eaa295a09d2b83e1c7440a22915ea671cab76bff47bb19fcd623fabf26bbdf54b603cd665d&scene=21#wechat_redirect)
3. [《英国ICO人工智能与数据保护指引》选译 | 如何保护人工智能系统中的个人权利？](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247490339&idx=1&sn=4ea2af025cdad3d46e7d92a24f76e860&chksm=97eaa6c9a09d2fdf6b2e37475479abbc4a9bc35e4ea9dc0ef29b1b0e727ccc82cd958ee50004&scene=21#wechat_redirect)
4. [人工智能 vs. 个人信息保护之“个人同意”](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247484571&idx=1&sn=41c9d5ec201e2e1f050dd77e856993ef&chksm=97eab971a09d30673d2513c98ca1a9d572ec1ed87e01fa09cd64ba3c41af6ca57e0d3b3c369e&scene=21#wechat_redirect)
5. [《以伦理为基础的设计：人工智能及自主系统以人类福祉为先的愿景（第一版）》](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247484264&idx=1&sn=dcb9e04c6f615a7c174c631ade2fa2aa&chksm=97eabe82a09d3794cb0a68a791d7a2ce009cd05c50ad423285003338c09575b6c8bd9519f812&scene=21#wechat_redirect)
6. [AI监管 | EDPB和EDPS对欧盟AI条例的联合意见书（全文翻译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492311&idx=1&sn=ea6f445d2fbd1389e2df697fe42539b6&chksm=97e95f3da09ed62bb16298981bd7fa2e46d53fdd97e490cd1bd2c5525a3d64796745ee65a9f1&scene=21#wechat_redirect)
7. [AI监管 | 对欧盟AI统一规则条例的详细分析](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492317&idx=1&sn=37fd2e9d5143edec9047e55776f91653&chksm=97e95f37a09ed6217aeb0ec31ec932b4111a108d4a8fd6d0826a8a8df4f5a5c1a712e05dad49&scene=21#wechat_redirect)
8. [AI监管 | 欧盟《AI统一规则条例（提案）》(全文翻译)](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492414&idx=1&sn=1c0addca9b35dfebe92c9537d5900f2a&chksm=97e95ed4a09ed7c26da4ccd52e2d8a74f114e8942ec94c7ceda2edcee403be41a2bb4ae466ee&scene=21#wechat_redirect)
9. [AI监管 | 意大利因骑手算法歧视问题对两个食物配送公司处于高额罚款](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492795&idx=1&sn=6196503c3e4306a682d220e9908cb9b1&chksm=97e95951a09ed047f5da7263e5dd9bf5426c5ebf906dfcb4bf10ff217154365d1963a4d7c850&scene=21#wechat_redirect)
10. [AI监管 | 用户数据用于AI模型训练场景的合规要点初探](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492865&idx=1&sn=813c0a010d8154c19a96b28e16504eb0&chksm=97e958eba09ed1fd26cc26fb2d8eb35fb380a386549c30b5919a6bf4602c15ba1bf270a7814b&scene=21#wechat_redirect)
11. [我国信息服务算法推荐管理 | 与个人信息保护的耦合和差异](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492942&idx=1&sn=bd14682c31904523d9ce5a60da168e3a&chksm=97e958a4a09ed1b2dbd302c0c1a8c8316da3038e783821eb7b3ef0e7efa6adbd311ae88b2cd9&scene=21#wechat_redirect)
12. [我国信息服务算法推荐管理 | 条文背后的技术逻辑“想象”](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492952&idx=1&sn=ebdb53b16ba58ab03d6b21b6557733ab&chksm=97e958b2a09ed1a431219e784dfe34c779568910bd6c5b739066ab435e3878191bc03521b8d1&scene=21#wechat_redirect)
13. [我国信息服务算法推荐管理 | 分类分级管理](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492957&idx=1&sn=30ec42429dd4a155cb491f573c711f6a&chksm=97e958b7a09ed1a17ed485076d4e7b4180523f8d7c752655a229a17424400242571eb608b90f&scene=21#wechat_redirect)
14. [我国信息服务算法推荐管理 | 合规的基础性工作：技术说明](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247492965&idx=1&sn=3f5be92414a67e4a1eef6dae021806b0&chksm=97e9588fa09ed199b0923b8f179362ef8932b7f03ab125a649a11bdfad90981be35c1426ff38&scene=21#wechat_redirect)
15. [中国个人信息保护中的自动化决策监管初探：基于与GDPR的比较](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247493567&idx=1&sn=e47cc742f4c2d1243e17be80478d0041&chksm=97e95a55a09ed343490132064ad60a1777c4bad8477dc590b00998a2646b981dc7e2618b5f42&scene=21#wechat_redirect)
16. [AI监管 | 全球人工智能的协调实际上是可以实现的吗？（外媒编译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247494365&idx=1&sn=2cded410ff7c053ae1b54a9e7cf8419f&chksm=97e95737a09ede21281773b8bc36bf5eedd74f0c3398fb71fc531919b98743b970e392da6e92&scene=21#wechat_redirect)
17. [《基于个人信息的自动化决策安全要求》标准制定项目的立项汇报](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247494424&idx=1&sn=4fc64514ca09561e7ca13f44847079e0&chksm=97e956f2a09edfe4d6d04dda28e14cfeca5cdc154224a2989551a585edb2db064bbb3f87232e&scene=21#wechat_redirect)
18. [AI监管 | 美国各州和地方开始以零敲碎打的方式推进AI监管（外媒编译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247494795&idx=1&sn=9ed4c19321436f486332abda861c4535&chksm=97e95161a09ed8770598d6d6767337fed70089bb25be2393378d9ce2dda47f7c746830ffe486&scene=21#wechat_redirect)
19. [欧盟《A...