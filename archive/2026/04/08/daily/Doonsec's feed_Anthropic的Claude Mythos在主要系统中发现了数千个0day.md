---
title: Anthropic的Claude Mythos在主要系统中发现了数千个0day
url: https://mp.weixin.qq.com/s/4SbRrtlHO_k9z6m9fe9RLg
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:27:49.135403
---

# Anthropic的Claude Mythos在主要系统中发现了数千个0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs9yagSqpic9PQ5UKcDmShmCTjVhrFc54PsBZria7fVnoFEMvzUs0bkRInV9APKf51ZG08MicstkFjiaYic5VicA5SRr9CUc92FGXZk0M/0?wx_fmt=jpeg)

# Anthropic的Claude Mythos在主要系统中发现了数千个0day

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oPZcPicUADsics31du9gy3vYAFhj8cV0MeTHYFjicd1NwP9alUMiak8TbDSFhAjGwzvPlqbuTvdQLkoq2WdmkWnzha3viaiacZj8V0dFXibxmgzY4Q/640?wx_fmt=png&from=appmsg)

人工智能（AI）公司Anthropic宣布了一项名为Project ；Glasswing ；的新网络安全计划，该计划将使用其新前沿模型Claude Mythos  ；的预览版来发现和解决安全漏洞。

该模型将被一小部分组织使用，包括亚马逊网络服务、苹果、博通、思科、CrowdStrike、摩根大通、Linux基金会、微软、英伟达和Palo alto Networks，以及Anthropic，以确保关键软件的安全。

该公司表示，它正在形成这一倡议，以回应在其通用前沿模型中观察到的能力，该模型显示出“编码能力水平，在发现和利用软件漏洞方面，它们可以超越除最熟练的人类之外的所有人”。“由于其网络安全能力和担心这些能力可能被滥用，Anthropic选择不让该模型普遍可用。”

Anthropic ；声称，已经在每个主要操作系统和web浏览器中发现了数千个高度严重的零日漏洞。其中一些漏洞包括OpenBSD中一个已有27年历史的漏洞，FFmpeg中一个已有16年历史的漏洞，以及一个内存安全虚拟机监视器中的内存破坏漏洞。

在该公司强调的一个例子中，据说神话预览自动出现了一个web浏览器漏洞，该漏洞将四个漏洞链接在一起，以逃避渲染器和操作系统沙箱。anthropic还在预览版的系统卡中指出，该模型解决了一次企业网络攻击模拟，而人类专家要花10个多小时才能解决。

这可能是最令人惊讶的发现之一，Mythos Preview成功地遵循了一名进行评估的研究人员的指示，从一台安全的“沙盒”计算机中逃脱，这表明它具有“潜在的危险能力”，可以绕过自己的保护措施。

模型并没有就此停止。它进一步执行了一系列额外的行动，包括设计一个多步骤的漏洞，从沙箱系统获得广泛的互联网访问权限，并向正在公园里吃三明治的研究人员发送电子邮件。

此外，“anthropicp”表示，为了证明自己的成功，该公司在多个难以找到但技术上面向公众的网站上发布了有关其漏洞利用的详细信息，这令人担忧，也是未经请求的。

该公司指出，“玻璃翼”项目是在敌对行为者采用前沿模型能力之前，为防御目的而采用这些能力的“紧急尝试”。它还承诺为Mythos预览版提供高达1亿美元的使用额度，并向开源安全组织直接捐赠400万美元。

Anthropic说：“我们并没有明确地训练Mythos Preview具备这些能力。”相反，它们是作为代码、推理和自主性普遍改进的下游结果而出现的。使模型在修补漏洞方面更加有效的改进，也使其在利用漏洞方面更加有效。

上个月，由于人为失误，该模型的细节被无意中存储在一个可公开访问的数据缓存中，有关神话的消息被泄露。草案材料将其描述为迄今为止最强大、最有能力的人工智能模型。几天后，Anthropic遭遇了第二次安全漏洞，在大约三个小时的时间里，意外地暴露了近2000个源代码文件和超过50万行与Claude code相关的代码。

这次泄漏还导致发现了一个安全问题，当向AI编码代理提供由50多个子命令组成的命令时，该问题会绕过某些防护措施。这个问题已经由Anthropic在上周发布的Claude ；Code 2.1.90版本中正式解决。

人工智能安全公司Adversa表示，“Claude Code”是Anthropic的旗舰人工智能编码代理，可以在开发人员的机器上执行shell命令，当命令包含超过50个子命令时，它会忽略用户配置的安全拒绝规则。配置‘never run rm’的开发人员在单独运行时将看到rm被阻塞，但是如果前面有50条无害语句，则相同的‘rm’可以不受限制地运行。安全策略默默地消失了。

证券分析花费token。Anthropic的工程师遇到了一个性能问题：检查每个子命令都会冻结ui并烧毁计算。他们的解决办法是：50岁以后不要再查看手机。他们以安全换取速度。他们以“安全”换取“成本”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

HackSee安全生活

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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