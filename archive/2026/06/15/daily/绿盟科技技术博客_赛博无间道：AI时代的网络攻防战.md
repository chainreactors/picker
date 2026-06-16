---
title: 赛博无间道：AI时代的网络攻防战
url: https://blog.nsfocus.net/%e8%b5%9b%e5%8d%9a%e6%97%a0%e9%97%b4%e9%81%93%ef%bc%9aai%e6%97%b6%e4%bb%a3%e7%9a%84%e7%bd%91%e7%bb%9c%e6%94%bb%e9%98%b2%e6%88%98/
source: 绿盟科技技术博客
date: 2026-06-15
fetch_date: 2026-06-16T07:15:34.809186
---

# 赛博无间道：AI时代的网络攻防战

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 赛博无间道：AI时代的网络攻防战

### 赛博无间道：AI时代的网络攻防战

[2026-06-15](https://blog.nsfocus.net/%E8%B5%9B%E5%8D%9A%E6%97%A0%E9%97%B4%E9%81%93%EF%BC%9Aai%E6%97%B6%E4%BB%A3%E7%9A%84%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2%E6%88%98/ "赛博无间道：AI时代的网络攻防战")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 75

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/8df92549a92047658d266636a2c66cae~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=llftAKuraofMDKTAAkacpQDRPMg%3D)

你能想象，你每天玩的游戏背后的厂商，其实正被AI黑客虎视眈眈吗？

2026年4月，游戏行业又出了一件事。《侠盗猎车手》系列发行商Rockstar Games，这个坐拥数十亿美元IP的游戏巨头，又一次成了黑客的目标。攻击者利用AI云分析工具Anodot的一个漏洞，通过窃取的身份验证令牌，悄无声息地侵入了Rockstar的数据仓库。整个过程没有警报、没有异常流量，因为他们伪装成了合法的内部用户。

Rockstar不是个例。2025年12月，育碧确认内部系统遭到入侵，攻击者试图窃取高达900GB的数据。同一时间，《堡垒之夜》开发商Epic Games也遭遇了大规模数据泄露，包括用户信息在内的200GB的内部数据被窃取。

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/37e6dd8c498f46af960f78acaa1b9079~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=12GXNS1mZjtbPHVtJoARk86YP8Y%3D)

FairGuard发布的《2025年度游戏安全报告》显示，去年游戏行业累计检测到的安全风险同比激增90%，外挂样本达32306款，黑灰产被封禁的账号高达6.4亿。

游戏行业只是一个缩影。金融、医疗、制造、政务……几乎每一个依赖数字化运转的领域都在经历同样的风暴。

CrowdStrike数据显示，2025年，由AI赋能的攻击同比增长了89%。全球暴力破解事件平均每天1.85亿次，全年超过676亿次。勒索软件的受害者激增了近四倍。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/d7a9a13ae0f548d8b17d07296465a27b~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=%2BlUewX4n%2BqpT8ixKJQhK2jt9ZLA%3D)

为什么攻击突然变得这么多、这么快？为什么连Rockstar、育碧这样的大厂都防不住？AI时代，通用安全大模型能抵御一切攻击吗？

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/ce8fd73df0c44c85917b7d61b935d6b9~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=jlVzvcZe6DJ8kVU3hfwyOZkLHWU%3D)

在传统的认知里，黑客是什么样的？

极客、高手，能在行行代码中找到那个致命的漏洞。你需要懂网络协议、懂系统底层、懂编程语言，需要像大海捞针一样在数万行代码中找出那个微小的错误，门槛极高。但AI时代，这道门槛正在被技术跨越。开源大模型和自动化渗透工具的出现，让攻击门槛降到了前所未有的低点。

研究显示，2021年，完成一次完整的攻击链平均需要9天，2023年缩短到2天，到了2025年，这个数字变成了半个小时之内。甚至有新闻爆料，攻击链最快已经可以在22秒内完成。

同时，攻击手段已经开始千人千面般疯狂变异。针对个人的钓鱼邮件攻击正在工业化批量生产；恶意软件入侵后先观察环境，再实时改写自己的代码，每次攻击都可能是一个全新的变种。

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/fde927b0441544f78f29b9538ed1d210~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=gtaxDsc1%2B8rNM%2Fx6%2BmOo9CajOgo%3D)

并且，影子代理类工具正在降低技术门槛。HexStrike AI、BruteForceAI等犯罪服务工具包正在暗网上明码标价。攻击者可以同时部署成百上千个AI智能体，自动寻找漏洞、自动破解密码、自动绕开防护。一个被发现，其他九十九个还在继续工作。

在AI出现之前，网络安全行业经过病毒时代、APT时代，已经形成了一套相对成熟的防御逻辑。安全研究员发现漏洞，写成规则，防火墙和入侵检测系统就能拦截。企业定期扫描，打补丁，修复。这套规则驱动的模式运行了几十年，清晰、可控、可预期。

**但AI时代到来之后，这套逻辑的前提开始崩塌。**

**一方面，规则更新跟不上漏洞产生的速度。**Anthropic的AI模型Mythos扫描了1000个开源项目，一周内发现了2.3万个漏洞，比全球每月新披露的漏洞总量还要多。AI挖漏洞的速度从月更变成了日更。

**另一方面，基于特征匹配的检测逻辑正在失效。**传统的检测方法是“找特征”。一段代码里有已知恶意代码的特定片段，就报警。但AI生成的恶意代码没有固定特征。每次运行都可能生成不同的变体，代码结构、函数命名、执行路径都不一样。传统的特征判断模式失效了。

当AI让攻击手段无限进化，行业纷纷研发通用大模型抵御变异的黑客。但大模型能防住一切吗？

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/21cd7645a999407d890606fb25eb1372~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=6eHE%2FuiNu3BIFNbqTM7fpPrIVv8%3D)

黑产无需考虑合规、稳定、兼容，只追求破防效率与隐蔽性，但防守端需要兼顾系统稳定、行业合规、多设备兼容，传统的网络安全方案已经防不胜防了。

顺着整个AI产业发展的规律看去，行业首先想到的就是押注大模型。AI攻击这么猛，防守当然要用更强大的AI。

**于是，互联网大厂在推出自己的安全大模型。**阿里的“天盾”、360的安全大模型……名字虽然不同，但底层逻辑相似，用海量数据和强大算力训练一个通用大模型，让它学习各种各样的攻击模式，然后部署到云上，为客户提供标准化的安全能力。

**头部网络安全企业也在升级。**奇安信、深信服、绿盟科技都推出了自己的AI安全方案，虽然各家在技术路径上有所差异，但“大模型”是共同的关键词。行业会议、技术白皮书、产品发布，几乎都在围绕大模型展开，甚至连甲方企业采购安全产品时，都会问一句：“你们的大模型有什么特点？”

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/0a1c7f5a12aa465ba5ecf6a96ad302bb~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=v%2B%2F%2FlDlMPeHmsZj0oYII5%2FriQ2k%3D)

这套主流叙事的逻辑其实很清晰：大模型能理解复杂的攻击语义，能处理海量的告警数据，能自动生成研判报告。大算力、全维度、云端通用似乎能解决安全运营中大部分让人头疼的问题。**但实际上，大模型在真实的网络安全攻守战中并非面面俱到。**

**一方面，大模型训练运维成本太高。**绿盟科技技术专家表示，每天自动化检测的上百万条告警里有99%以上都是正常业务流量，真正有威胁的攻击可能只占0.01%。用大模型去筛这99%的正常流量，就像用航母运快递，成本高且没必要。

**另一方面，大模型在网络安全场景速度比不上小模型。**参数量越大，计算量（FLOPs）和显存访问通常越高，导致单token生成延迟更大。但安全运营需要毫秒级的响应。一个攻击从发生到造成损失，可能只有几秒钟。等大模型分析完，数据大概率已经被窃取。

**并且，通用大模型偏向标准化、普惠化防护。**面对政企专网、私有机房等垂直行业的本地化、定制化安全需求，通用模型灵活性不足、适配性偏弱。

**因此，绿盟科技等头部网安厂商在训练通用大模型的同时，也在持续设计针对不同场景的小模型。**

小模型先冲在最前面，负责快速判断一个请求是不是正常的业务行为。一个数据库查询，正常，放行；一个API调用，符合日常模式，不惊动后端。只有那些拿不准的可疑流量才会被送到大模型面前。绿盟科技内部有多个经过产品化考验的小模型，它们把送往后端的数据量压缩了90%以上。没有它们挡在前面，大模型的算力会被无效流量耗尽。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/90371855d66f4b43b987df529d5ff910~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=KqFIaPjzRJoaC2RWdVFuy%2FVkmnE%3D)

针对不同客户的业务场景，小模型可以做定制化训练。比如，针对某家银行的交易系统，训练一个小模型来学习“什么是这家银行正常的数据访问模式”。大模型负责通用攻击识别，小模型负责告诉大模型：“等等，这个操作在这家客户那里是正常的。”两者配合，才能把误报降下来。

并且，很多企业的业务系统部署在本地机房、专网甚至工业现场，数据不能出内网，网络带宽有限，云端的大模型根本用不了。小模型可以直接部署在客户本地，在边缘侧完成实时判断和处置。

**简言之，大模型解决深度问题，小模型解决广度问题和场景问题。**由信息工程大学团队完成的TinySecGPT研究表明，经过专业微调的小模型在安全任务上对比14B大模型的胜率或平局率达到85%，最佳模型对比安全专用大模型SecGPT达到90%，同时训练时间减少53%，推理成本大幅降低。安全厂商Sophos也在实践中验证了这一路径，通过知识蒸馏等技术训练的小型AI模型在恶意网站分类等任务中准确度已可媲美传统大模型，甚至在某些资安情境下表现更优。

放在行业视角来看，大厂善于把控全域大势，老牌网安精于细分场景落地，未来的网络安全，大概率是平台、专业的协同作战。

不过，模型协同作战就能抵挡住一切黑客攻击了吗？网络安全领域，曾作为攻防核心的人是否真的可以隐居幕后？

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/93bbbdc74b1c4c80bdc05bc94c751a1b~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=AT%2BeWPaYCchmFw%2BCXBgM%2FvbPGn0%3D)

世人皆盼安全一劳永逸，但网安江湖从来没有修成圆满的那一天。回顾网络安全行业的发展历程，可以清晰地看到几次代际更替。

第一代是病毒时代。黑客编写病毒通过软盘传播，杀毒软件以特征码进行匹配。彼时攻防核心在于谁能更快获取样本、谁的特征库更全。第二代是网络攻击时代。蠕虫、木马、DDoS攻击开始泛滥，行业逻辑演变为规则驱动，彼时的攻防比拼的是知识库的完备程度。第三代是APT时代。攻击者是针对特定目标进行长期潜伏渗透。行业开始转向行为分析、威胁情报与态势感知。

三代更替，攻防双方在“信息—知识—智能”的轴线上反复拉锯，但始终没有脱离一个核心——人。人是每一次对抗的主角。黑客是人，安全研究员是人，写规则的是人，分析告警的也是人。

**如今，行业正在进入第四个时代：AI系统之间的攻防战。**

攻击者部署AI代理，自动扫描、挖洞、生成攻击代码；防守者祭出大模型、智能体、Skill、数字人，全副武装。一线对抗，变成了AI与AI之间的博弈。看上去，人似乎可以退场了。

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/5eeec72dffee4b64bb50ce0dfce932de~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=2026061511051993FDAB252B6EC8204505&x-expires=2147483647&x-signature=3%2BQQP9KkOvn0DZkliNSr7ichihk%3D)

**但绿盟科技专家的一段话提供了一个不同的观察角度：“我们花了三年时间，经过专家不断地调教，优化AI，才把AI运营系统的效率从刚上线时的水平提升到现在的80%多。”**

AI运营系统的核心是一套复杂的自动化流程。前端多个小模型做流量过滤，后端大模型做深度研判，中间还有智能体负责情报收集、漏洞分析、报告生成。分析研判的Skill、漏洞情报的Skill等智能体Skill上线运营……这看起来是一个完整的AI闭环：告警进来，AI自动研判、自动处置、自动生成报告，效率提升70%以上。

但这个闭环能够运转，前提是有人一直在修。因为一旦误判，代价是巨大的。

自动化脚本可以瞬间生成检测规则，但判断不了“这条规则会不会把客户的正常业务给拦了”。如果把正常业务当成攻击拦截，可能导致客户的业务中断、交易失败、用户无法访问。智能体可以二十四小时不间断工作，但分不清“这是攻击还是正常的业务高峰”，而把真正的攻击漏过去，可能导致数据泄露、系统被控、勒索软件加密。

在网络安全这个领域，无论是误报还是漏报，损失都不计其数。一个金融客户的核心交易系统被误拦一分钟，损失可能就是几百万；一个企业的用户数据被泄露，面临的可能就是千万级的罚单和无法估量的品牌损失。

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/2a7327c5494c47c1b64f9f61b9506a60~tplv-tt-shrink:...