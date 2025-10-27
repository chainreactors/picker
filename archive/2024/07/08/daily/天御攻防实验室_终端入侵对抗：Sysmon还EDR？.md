---
title: 终端入侵对抗：Sysmon还EDR？
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485883&idx=1&sn=6ca8d0bc5a6abd6d31f5575446292b69&chksm=fb04cad3cc7343c5434958338ac2a21a7b0eccc078f17b4c061ac0840e3fbfc3a04f22ba66e7&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2024-07-08
fetch_date: 2025-10-06T17:41:13.250435
---

# 终端入侵对抗：Sysmon还EDR？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBBhTrp7OQ4ktoDsBsJF6IQhnQjXUX6TX9t58anMof6kLdgq3LsAvA3qibHm2KOebwb2a21QE4Z9I3w/0?wx_fmt=jpeg)

# 终端入侵对抗：Sysmon还EDR？

原创

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBBhTrp7OQ4ktoDsBsJF6IQh0dvR0JffibbdTzeTHxYVlHmgfvOdmjstXLBshxXQQ9kwvdsHfVCYddQ/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/L3Qib0nCc28kiapaXx6yNO55P5HlE5K5KPeSAjibuQB36kIUdWs5ZVzic20R5FzeTKae8vbINVEw6wlcgKa6R3ZqJyzYfRb6Z531/640?wx_fmt=svg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**导语：**

![](https://mmbiz.qpic.cn/mmbiz_svg/L3Qib0nCc28kiapaXx6yNO55P5HlE5K5KPXIUDVn0iapYjG2yy97z0lLcM24iaxtvIURGVzAzErSBnM9ZAYQl7U12fvcpic6PLTwm/640?wx_fmt=svg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

我最近与来自完全不同行业/领域的几个客户开展了研讨会，Sysmon + SIEM（安全信息和事件管理）检测规则 VS 商业EDR到底如何选择？这是一个反复出现的话题。

# 01

不选Sysmon的理由

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBBhTrp7OQ4ktoDsBsJF6IQhobdbYfbkMAUw792Vy1BwyMwmibXfHiaXBRu8PLsfFqCQwJbyNvLzVFJA/640?wx_fmt=jpeg&from=appmsg)

首先，我在这里写的几乎所有内容都集中在或适用于企业环境、大规模部署和高预算。此处的观点不适用于家庭或学生实验室环境。它也不适用于被限制使用商业产品、主要依赖免费或开源软件的组织。

其次，它不适用于研究实验室或从业者用来体验Sysmon丰富日志信息的环境。

最后，我不是在讨论取证或任何事后使用案例（响应），而是在讨论如何利用Sysmon的日志信息来构建检测体系。

目标和视角

如果你要领导一个大企业的安全监控实践，拥有相对充足的资金和有限的人力资源，我相信更容易理解我的观点。

对于预算和合同都受限制的人来说，情况与拥有充足资金的大企业完全不同

那么在企业环境中，一切都与钱有关吗?是的，尤其是如果你也把时间看作是一种货币投资的话。

部署Sysmon是一项任务，维护该部署是另一项任务，而使用Sysmon的日志信息来构建检测机制又是另一个完全不同的挑战。

存储再丰富的日志数据，如果不被主动使用（检测），其检测价值也微乎其微。

因此，假设这里的目标是利用终端信号来检测威胁。

作为一名企业安全负责人，你需要考虑以下几点：

检测面：考虑到组织所面临的风险，你的团队需要尽可能多地覆盖攻击面。在本例中，我们讨论的是终端安全，主要是商业恶意软件，这是一个非常普遍的攻击载体，每天都会出现新的变种。

部署维护：除了能够将agent（代理）部署到尽可能多的终点之外，还需要快速完成。agent的故障排除或更新也应该是轻而易举的。

与现代EDR相比，Sysmon的开箱即用价值无法相提并论，这听起来不太公平，因为我们在比较一个免费产品和一个商业产品。

尽管如此，这种比较在今天是成立的，因此有了这篇文章。接下来，我们深入探讨使用EDR的优缺点。

# 02

Sysmon vs EDR

首先要强调的是，大多数EDR产品都提供多种功能，从丰富的日志信息、告警信号，到响应功能。

鉴于所有这些功能，这里的重点仅在于检测能力。

遥测（Telemetry）与检测（Detection）不同

这是一个看似显而易见、但实际上很多人尚未意识到的重要区别，即"告警事件"和"普通日志事件"是有本质不同的。

告警事件携带明确的告警信号，如"可疑的Tomcat子进程"。普通事件只是说"这里创建了一个新进程"。

简而言之，只有原始日志就像拥有原油而不是汽车燃料等副产品。

在你能够提炼它之前，它的用例非常有限。这意味着在你能够使用它之前，它没有价值。

现在，从原始终端日志中制作出好的检测有多难?

极具挑战性!

我曾帮助一个团队维护和进一步开发了一个基于EDR原始日志的告警框架，包含400多个自定义检测/指标。

相信我，这很有挑战性。

下面是一个例子，展示了可以用原始终端日志做什么:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBBhTrp7OQ4ktoDsBsJF6IQhdM32oz2bh7YsDqqmXGPw23OxVJnfUASrwHKPjP8VT74HXDkCYiaqPKA/640?wx_fmt=jpeg&from=appmsg)

**全球指标反映了过去30天内所有受监控端点上每个指标的发生情况。**

| 设备时间 | 指标 | 全球趋势 | 全球端点数 | 评分 |
| --- | --- | --- | --- | --- |
| 4月1日 04:54 | 观察到潜在未跟踪的RAT（远程访问工具）痕迹 |  | 3 | 10.00 |
| 4月1日 04:52 | 潜在已知的RAT网络活动 |  | 7 | 7.00 |
| 4月1日 04:50 | 从非浏览器访问非HTTP/S端口的稀有外部域名 <rustdesk.com> |  | 6 | 6.00 |
| 4月1日 04:50 | 观察到潜在已知的RAT痕迹 |  | 5 | 5.50 |
| 4月1日 04:48 | 从临时压缩文件运行的可执行文件或脚本 |  | 4 | 5.50 |
| 4月1日 04:56 | 文件下载匹配显著扩展名 |  | 3 | 5.00 |
| 4月1日 04:56 | 从Google Docs下载显著文件 | - | - | 5.00 |
| 4月1日 04:54 | 新进程执行外部连接至高UDP端口 | - | - | 4.50 |
| 4月1日 04:52 | 新进程执行外部连接至非常见TCP Web端口 | - | - | 4.00 |
| 4月1日 04:50 | LOLBin: <certutil.exe> 联系高频外部域名 <digicert.com> |  | 2 | 3.00 |
| 4月1日 04:48 | 从临时位置执行的可执行文件 |  | 3 | 3.00 |
| 4月1日 04:56 | 基线中未发现的新哈希 |  | 2 | 2.50 |
| 4月1日 04:54 | 基线中未发现的Packer工具 |  | 1 | 2.00 |
| 4月1日 04:52 | 管理员：通过consent.exe请求的管理权限 |  | 1 | 1.50 |
| 4月1日 04:50 | 在命令行中找到URL |  | 1 | 1.00 |
| 4月1日 04:48 | 压缩文件操作 |  | 1 | 0.50 |

```
**全球指标反映了过去30天内所有受监控端点上每个指标的发生情况。**
| 设备时间 | 指标 | 全球趋势 | 全球端点数 | 评分 ||----------|------|----------|-----------|------|| 4月1日 04:54 | 观察到潜在未跟踪的RAT（远程访问工具）痕迹 | ![趋势](https://via.placeholder.com/100x20) | 3 | 10.00 || 4月1日 04:52 | 潜在已知的RAT网络活动 | ![趋势](https://via.placeholder.com/100x20) | 7 | 7.00 || 4月1日 04:50 | 从非浏览器访问非HTTP/S端口的稀有外部域名 <rustdesk.com> | ![趋势](https://via.placeholder.com/100x20) | 6 | 6.00 || 4月1日 04:50 | 观察到潜在已知的RAT痕迹 | ![趋势](https://via.placeholder.com/100x20) | 5 | 5.50 || 4月1日 04:48 | 从临时压缩文件运行的可执行文件或脚本 | ![趋势](https://via.placeholder.com/100x20) | 4 | 5.50 || 4月1日 04:56 | 文件下载匹配显著扩展名 | ![趋势](https://via.placeholder.com/100x20) | 3 | 5.00 || 4月1日 04:56 | 从Google Docs下载显著文件 | - | - | 5.00 || 4月1日 04:54 | 新进程执行外部连接至高UDP端口 | - | - | 4.50 || 4月1日 04:52 | 新进程执行外部连接至非常见TCP Web端口 | - | - | 4.00 || 4月1日 04:50 | LOLBin: <certutil.exe> 联系高频外部域名 <digicert.com> | ![趋势](https://via.placeholder.com/100x20) | 2 | 3.00 || 4月1日 04:48 | 从临时位置执行的可执行文件 | ![趋势](https://via.placeholder.com/100x20) | 3 | 3.00 || 4月1日 04:56 | 基线中未发现的新哈希 | ![趋势](https://via.placeholder.com/100x20) | 2 | 2.50 || 4月1日 04:54 | 基线中未发现的Packer工具 | ![趋势](https://via.placeholder.com/100x20) | 1 | 2.00 || 4月1日 04:52 | 管理员：通过consent.exe请求的管理权限 | ![趋势](https://via.placeholder.com/100x20) | 1 | 1.50 || 4月1日 04:50 | 在命令行中找到URL | ![趋势](https://via.placeholder.com/100x20) | 1 | 1.00 || 4月1日 04:48 | 压缩文件操作 | ![趋势](https://via.placeholder.com/100x20) | 1 | 0.50 |
```

然而，大多数组织没有工程能力或技能来走这条路。此外，如果一开始没有考虑可扩展性来设计框架，维护起来也不容易。

在SIEM中，我们大多数时候专注于构建检测，而实际的检测在别处完成（在EDR中?）。

这是你战略中的一个重大决定，从这里我开始阐述为什么你应该把这些检测外包给EDR。

“吞吐量”：EDR厂商的产品研发团队 VS 企业内部安全团队

"吞吐量"在这里指的是单位时间内可以开发和交付的安全检测功能的数量和质量。专门的EDR产品团队在这方面具有明显的优势。

主要原因包括：

1. EDR厂商拥有专业的研发团队，聚焦产品功能开发，可以投入更多的人力资源。相比之下，企业内部团队往往人手有限，还要兼顾其他工作。

2. 开发检测能力是EDR厂商的核心业务，他们有更强的动力快速迭代、完善产品。而对企业而言，这只是众多安全管理任务之一。

3. EDR团队可以通过产品化实现检测能力的快速复制和交付，使众多客户受益。而企业内部团队的成果很难在组织外部共享。

因此，在检测能力的开发效率和覆盖范围方面，企业内部团队很难与专业的EDR厂商竞争。对于大多数企业来说，从成本效益的角度考虑，购买成熟的EDR产品是更经济的选择。

当然，这并不意味着企业完全不需要内部团队参与检测能力的开发。对于EDR未覆盖的特定场景，以及快速响应特定安全事件的需求，专业的内部团队还是可以发挥重要作用的。

然而，你的（小）内部团队需要让Sysmon保持运行，同时还要设计、测试和部署利用Sysmon日志的SIEM检测规则。

EDR产品的检测（和功能）将很容易超过你的团队使用原始日志+SIEM规则所能完成的。

作为企业安全负责人者，我最好调配这些资源，因为大多数团队除了检测工程之外，还在执行其他任务，如威胁情报/建模、事件响应等。

作为从业者，如果你真的喜欢这样做，可以考虑加入供应商，甚至开发自己的产品。这方面有很多成功的故事!

我一直在说:

如今，在企业环境中显著提高检测覆盖面的最有效措施，就是安装新的EDR agent。

从它激活的那一刻起，就有数百个场景被监控，没有任何SIEM规则集可以与之相提并论。

大多数时候，从数据收集的角度来看，只需将EDR告警接入SIEM就足够了，而不需要同时引入原始日志。

然而，当涉及确保不遗漏任何告警信号，并在尽可能多的端点（服务器和笔记本电脑）上安装agent时，SIEM仍然是王者。这只是其用例的几个例子。

# 03

支持Sysmon的看法

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBBhTrp7OQ4ktoDsBsJF6IQhZGxtMbCAWmw9lrszIeLe9ibufstaz8kkV7P1wq4BRtWGdjxq9ofx4rQ/640?wx_fmt=jpeg&from=appmsg)

**Sysmon是互补的**

这一点很容易达成一致，但我亲眼目睹了维持一个健康、大规模的Sysmon部署有多难。这需要时间，而这些时间本可以用于其他运维周期。

最重要的是，我不确定：

* EDR未覆盖的用例是什么。迟早，供应商将能够覆盖这一点，考虑到他们今天的开发速度。
* 这种用例的价值是否值得在一个端点维护多个agent+维护Sysmon的投入。

**EDR检测 = 黑盒**

对大多数产品来说确实如此。你无法看到清晰的检测列表，更不用说背后的代码或逻辑了。

然而，现代EDR将覆盖大量检测，因此真正的挑战变成了确定团队应该关注哪些告警信号的优先级。这就是SIEM分析发挥作用的地方!

每当发现明显的差距，你的团队就应该能够在EDR的开箱即用功能之上进行构建。

例如，大多数EDR不会将TeamViewer和其他合法的远程协助软件标记为可疑。

在这种情况下，你的EDR应该提供一种方法来创建自定义检测，可以轻松地部署到多个终端。

专业提示：如果你可以像在SIEM中一样制作EDR检测规则，会怎样?

我的意思是，使用相同的开发工作流，甚至可能使用相同的查询语言?

是的，微软和CrowdStrike在这方面有明显优势!

这是通过有选择地启用正确的EDR原始日志，然后通过SIEM中的检测规则捕获它来实现的。

或者更好的方法是，在EDR之上构建自定义检测规则，然后在SIEM中汇总这个告警信号。

参考资料：

https://detect.fyi/sysmon-a-viable-alternative-to-edr-44d4fbe5735a

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6...