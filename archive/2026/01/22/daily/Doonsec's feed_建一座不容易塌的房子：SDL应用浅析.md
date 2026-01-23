---
title: 建一座不容易塌的房子：SDL应用浅析
url: https://mp.weixin.qq.com/s/LcBeiE18ncjP_Mqwe5evzg
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:31:19.111691
---

# 建一座不容易塌的房子：SDL应用浅析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/U6oY6Hu3lnk60icN7YDSlJUHAUjK9jwvB9jqmJdEicF8ibCQJJSudG4cibkHoAAkJkqDgA62icS9bGkIQFDHzfVeAfA/0?wx_fmt=jpeg)

# 建一座不容易塌的房子：SDL应用浅析

原创

catfishfighting
catfishfighting

透明魔方

![]()

在小说阅读器中沉浸阅读

又要去给开发团队做安全意识培训了。

借着马上要去培训的驱动力，我试着完成这篇文章。

## 一、我们总在建“漏雨的房子”

为什么我们总在建”漏雨的房子“呢？

今年参加了一个大型事业单位的漏洞分析工作，试着分析暴露出来的漏洞所产生的原因，帮助单位进一步排查现有系统的潜在漏洞。这些漏洞虽然五花八门，但最主要的漏洞还是鉴权不完善导致的很多”未授权访问“和”越权“问题。

甚至，很多漏洞是因为仅在客户端做了校验，而不是服务器端做的校验。

会上，年轻的开发工程师很委屈：“我们是按功能来开发的，这个也要看安全能力的，而且有些要求需求文档没写，最后测试也通过了。”

项目经理更委屈：“我们按进度交付业务功能，安全不是最后有渗透测试等三测吗？”

传统的软件开发流程，安全就像最后那道“质检工序”。代码写完了，功能测好了，才最后“看一看”有没有漏洞。这时候发现的漏洞，就像房子盖好了才发现承重墙有问题——要么推倒重来，要么打上难看的补丁。

况且，最后一关的渗透测试是否能全面找出漏洞？

当然是不太可能，毕竟你的系统上了公网，要对抗的是海量黑客。

而SDL（Security Development Lifecycle）说的是另一件事：**从一开始，就用安全的方式思考**。

## 二、安全开发规范——SDL

既然软件安全方面的问题究其根本在于软件本身存在安全漏洞（当然也面临了外部威胁），那我们就可以用比较好的软件开发模型来应对这个问题。

典型的软件安全开发模型有几种，如安全开发生命周期SDL，ISO/IEC27034、McGraw的7个接触点模型BSI、软件开发成熟度模型BSIMM、OWASP的CLASP3。我们今天介绍一个常用的模型，就是微软从安全角度提出的指导软件开发过程的管理模式——SDL。

![](https://mmbiz.qpic.cn/mmbiz_png/U6oY6Hu3lnk60icN7YDSlJUHAUjK9jwvBF92bia1cnG9bVabANibW4Bq1EnUWW7TOkKfTjA7pXmFlEPlYR4tPXwdw/640?wx_fmt=png&from=appmsg)

传统的软件开发流程，中心主要是围绕着产品功能，如瀑布模型，几乎没有安全方面的考虑。从需求分析分析——软件设计——软件编码——测试等环节均没考虑，如软件设计考虑的是如何有效正确的实现功能，会约定来自相关模块的数据是值得信赖的，可能只在最外围的数据模块接口处对用户数据加以校验，那么如果一个模块出现安全问题，整个软件系统就处于不设防的状态。

SDL的核心理念，就是将软件安全的考虑集成在软件开发的每一个阶段（需求分析、设计、编码、测试和维护）。也就是在传统软件开发生命周期的各个阶段增加一些必要的安全活动。

安全培训:是基础性的工作，要求开发人员必须了解基本的安全概念。安全培训也是贯穿SDL的一个东西，有需要就培训。

需求分析阶段: 要应用文档描述安全需求，从风险角度搞清楚开发和支持成本，识别系统的功能时，要执行安全风险评估并进行隐私影响分级。

设计阶段:采用威胁建模等来识别脆弱性。

实施阶段: 要遵循最佳实践。

验证发布阶段：要进行评审。

这里我就不详述了，毕竟SDL不是那么死板的，大家都可以运用这个理念打造适合自己的SDL。

三、安全开发规范——SDL实践

微软的实践证明，SDL能减少操作系统的安全漏洞。如Windows Server 2003是第一次大规模实施SDL（还不是全面实施），漏洞就比2000少了很多。自2004年起，微软将SDL作为全公司的强制政策。

![](https://mmbiz.qpic.cn/mmbiz_png/U6oY6Hu3lnk60icN7YDSlJUHAUjK9jwvBmibNtdoUxFVIZhZDYdfYOkia4EyzWZRXeNG2hYdTC1R9tpqpKmZTk6TQ/640?wx_fmt=png&from=appmsg)

全球各大企业也在以自己的理解及实际情况探索实现SDL安全体系，我们国内也有一些应用SDL的案例，比如工商银行2022年开始建立SDL体系，将其与DevSecOp结合，用平台系统（含流程、知识库、工具、安全组件、基线）支撑，赋能人员，提高了安全开发的效率。

![](https://mmbiz.qpic.cn/mmbiz_png/U6oY6Hu3lnk60icN7YDSlJUHAUjK9jwvBZw7ObUFhjH29vLHn3NbytthGwgxL5CWMpiaBmwJyVS8vpXE86XFZIuQ/640?wx_fmt=png&from=appmsg)

四、中小型企业如何开展SDL建设

中小型企业如果要全面应用SDL会面临安全人才匮乏、系统支撑不足导致的无法落地（如测试人员无法执行完整正确的安全用例测试）、自动化程度低主要靠人工、缺乏长期规划等困难。

如果中小企业探索SDL可以重点考虑一些工作：

首先就是引起高层重视，可以先从挖掘很多漏洞，暴露出很多安全隐患入手。高层重视了，

就可以：

1.定义清晰的长期规划，提供组织架构保障。

2.安全平台建设并与现有体系耦合（引入知识库和工具组件），实现自动化落地，提升执行效率和控制力，人员能力沉淀为企业资产。

THE END

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/U6oY6Hu3lnltCm5ZvL07Mm4DwTUefYEPXR7QRNQxXvc9xPEOz18ws0djQpfmVIQq9Js0TcSKH8tu1g1AyWMibBw/0?wx_fmt=png)

透明魔方

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/U6oY6Hu3lnltCm5ZvL07Mm4DwTUefYEPXR7QRNQxXvc9xPEOz18ws0djQpfmVIQq9Js0TcSKH8tu1g1AyWMibBw/0?wx_fmt=png)

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