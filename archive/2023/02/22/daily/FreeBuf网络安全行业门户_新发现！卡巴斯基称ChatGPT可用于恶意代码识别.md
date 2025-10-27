---
title: 新发现！卡巴斯基称ChatGPT可用于恶意代码识别
url: https://www.freebuf.com/news/358273.html
source: FreeBuf网络安全行业门户
date: 2023-02-22
fetch_date: 2025-10-04T07:43:20.158363
---

# 新发现！卡巴斯基称ChatGPT可用于恶意代码识别

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

新发现！卡巴斯基称ChatGPT可用于恶意代码识别

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新发现！卡巴斯基称ChatGPT可用于恶意代码识别

2023-02-21 16:40:53

所属地 上海

随着近日大型语言模型 (LLM) ChatGPT的流行，许多网络安全工作者也开始实验它在抵御安全威胁方面的能力。目前已有多项实验表明，ChatGPT不仅能够对潜在的安全事件进行分类，还能从中发现代码的安全漏洞，即便它没有专门针对此类活动进行训练。

![](https://image.3001.net/images/20230221/1676972091_63f4903b0a1e24f70618a.png!small)

2月15日，卡巴斯基在一项实验中，将ChatGPT 作为事件响应工具的实用程序进行分析。他们模仿一般攻击者使用 Meterpreter 和 PowerShell Empire 代理感染了一个系统，用 ChatGPT 对受感染的进程进行识别。结果显示，ChatGPT在没有误报的情况下正确排除了137 个良性进程，识别出了2个恶意进程，并且还供了该服务应被归类为陷落标识（indicator of compromise）的原因结论。

最终，卡巴斯基分析师使用 ChatGPT 分析了测试系统上 3500 多个事件的元数据，发现了 74 个潜在的危害指标，其中 17 个是误报。该实验表明，ChatGPT 可用于为未运行端点检测和响应 (EDR) 系统、检测代码混淆或逆向工程代码二进制文件的公司收集取证信息。

这项实验是从向 ChatGPT 询问 Mimikatz 和 Fast Reverse Proxy 等几种黑客工具开始的。人工智能模型成功地描述了这些工具，但当被要求识别众所周知的哈希值和域时却失败了，例如， ChatGPT无法识别恶意软件WannaCry众所周知的哈希值。

但显而易见，卡巴斯基在识别主机上的恶意代码方面则较为成功，他们要求 ChatGPT 创建一个 PowerShell 脚本，以从系统中收集元数据和危害指标并提交。在手动改进代码后，安全人员在受感染的测试系统上使用了该脚本。

在此之前，其他安全公司也在研究如何通过此类模型来执行特定的防御相关任务。去年12月，数字取证公司Cado Security使用ChatGPT创建了一个事件中的JSON数据的妥协时间表，生成了一份“不完全准确但总体良好”的报告。

## 结果是否可用？

由此看出，ChatGPT得出的结果到底是否可用？安全咨询公司NCC集团尝试用ChatGPT作为寻找代码中的漏洞的方法，得到了“不总是准确”的结果。NCC集团首席科学家 Chris Anley 表示，安全分析师、开发人员和逆向工程师在使用如ChatGPT的大型语言模型时要小心行事，尤其是对于超出其能力范围的任务。

“我赞同专业开发人员和其他使用代码的人去探索 ChatGPT 和类似模型，但更多的是为了获得灵感，而不是为了获得绝对正确、真实的结果，“Chris Anley说道。”用ChatGPT进行安全代码审查不是我们的最佳选择，所以期望它第一次就做到完美是有点不公平。"

卡巴斯基事件响应团队负责人 Victor Sergeev也警告称，结果不准确是一个非常现实的问题，要注意这些这可能产生的误报和漏报，并称目前的ChatGPT”也只是另一个容易产生意外结果的统计神经网络“。

## 有待完善的隐私规则

目前，已经有公司开始对使用互联网上的信息创建数据集提出异议，NCC Group 的 Anley 表示，安全专家必须确定提交的入侵指标是否暴露了敏感数据，或者提交软件代码进行分析是否侵犯了公司的知识产权。“向ChatGPT提交代码是否是个好主意，很大程度上取决于具体情况。"很多代码是专有的，受到各种法律保护，所以我不建议人们提交代码给第三方，除非他们得到许可。” Anley说道。

Sergeev也发出了类似的警告。使用ChatGPT检测漏洞，必然会向系统发送敏感数据，这可能违反了公司政策，并可能带来商业风险。

> 参考来源：[https://www.darkreading.com/analytics/chatgpt-subs-security-analyst-hallucinates-occasionally](ChatGPT%20Subs%20In%20as%20Security%20Analyst%2C%20Hallucinates%20Only%20Occasionally)

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

结果是否可用？

有待完善的隐私规则

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)