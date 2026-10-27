---
title: Node.js、Python、Bun全中招：一个压缩库的内存漏洞，让半个互联网"裸奔"
url: https://www.anquanke.com/post/id/316355
source: 安全客-有思想的安全新媒体
date: 2026-10-26
fetch_date: 2026-10-27T07:04:16.855625
---

# Node.js、Python、Bun全中招：一个压缩库的内存漏洞，让半个互联网"裸奔"

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Node.js、Python、Bun全中招：一个压缩库的内存漏洞，让半个互联网"裸奔"

阅读量**74137**

发布时间 : 2026-10-26 14:54:01

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

Google Brotli解码器曝出严重内存损坏漏洞，影响Node.js、Python、Bun、Envoy等主流软件，Imperva已证明可在Node.js上远程代码执行，你的应用可能正在解压恶意数据。

你以为压缩库能有什么安全问题？不就是解压个文件吗？

醒醒。一个压缩库的漏洞，能让你的Node.js服务器被远程控制，能让Python应用崩溃，能让Envoy代理变成攻击者的跳板。

这不是危言耸听。这是2026年10月21日，Google Brotli解码器漏洞（CVE-2026-111497）披露后，安全圈的真实反应。

# **一、Brotli是什么？为什么这个漏洞影响这么大**

先科普一下。Brotli是Google开发的一种压缩格式，主要用于Web压缩。你在浏览器里看到的网页、图片、API响应，很多都是Brotli压缩后传输的。目的是减少带宽、加快加载速度。

现在，全球绝大多数Web服务器、CDN、代理都在用Brotli。Node.js内置了Brotli解码器，Python有brotli和brotlicffi包，Bun（新一代JavaScript运行时）内置了Brotli，Envoy（流行的云原生代理）也内置了Brotli。

问题来了：这些软件都是各自内置了一份Brotli解码器的代码。现在这份代码出了漏洞，意味着所有内置了这份代码的软件，都受影响。

这不是”一个软件有漏洞”，而是”一个库有漏洞，一堆软件跟着遭殃”。

漏洞编号CVE-2026-111497，类型是”越界写”（Out-of-Bounds Write）。什么意思？攻击者构造一个恶意的Brotli压缩数据，解码器在处理这个数据时，会写入超出缓冲区边界的数据，覆盖相邻的内存区域。

后果是什么？三种可能：

1. **程序崩溃**（拒绝服务，DoS）
2. **内存泄漏**（敏感信息暴露）
3. **执行攻击者控制的代码**（远程代码执行，RCE）

第三种，是最致命的。

# **二、Node2Shell：Imperva证明可在Node.js上远程代码执行**

漏洞披露后，安全公司Imperva的研究人员做了一个实验：能不能用这个Brotli漏洞，在Node.js上实现远程代码执行？

答案是：能。

他们把这个利用方式叫做”Node2Shell”。具体来说，他们在官方发布的Node.js 24.22.0版本（Linux arm64架构）上，通过喂入精心构造的Brotli数据，成功执行了攻击者提供的代码。

注意，这不是什么魔改版、调试版的Node.js，是官方发布的正式版本。没有修改任何代码，没有加任何调试器，就是原汁原味的Node.js。

Imperva的研究人员也承认，这个利用不是每次都能成功，在他们的Linux arm64环境下，需要尝试几次才能成功执行代码。而且这个结果只覆盖了这一个构建和应用设置，其他架构（比如x64）和其他版本线（22.x和26.x）没有测试。

但即便如此，这已经足够吓人了。因为：

1. 之前公开的PoC（概念验证）只能在故意削弱的测试构建上实现代码执行
2. 这次是在标准构建上实现了代码执行
3. 这证明漏洞是真实可利用的，不是理论上的风险

更关键的是，Imperva在修复后的版本24.22.1上测试了同样的数据，结果被拒绝，没有执行任何代码。这说明补丁是有效的。

问题是：你的Node.js升级了吗？

# **三、影响范围：Node.js只是冰山一角**

Node.js只是Brotli漏洞影响的软件之一。根据目前已知的信息，以下软件都受影响：

**Node.js**

* 22.x版本：低于22.23.4
* 24.x版本：低于24.22.1
* 26.x版本：低于26.12.1

**Python**

* brotli包（所有版本）
* brotlicffi包（所有版本）

**Bun**

* 所有内置Brotli解码器的版本

**Envoy**

* 所有配置为解压Brotli的版本

还有其他使用Google Brotli解码器的软件，都可能受影响。

为什么影响这么广？因为Brotli是Web标准的一部分。现代Web性能优化，离不开Brotli压缩。你在Nginx、Apache、Cloudflare、AWS CloudFront上配置的Brotli压缩，底层用的都是同一份Google的代码。

现在这份代码出了漏洞，意味着整个Web基础设施的底层，都出现了裂痕。

# **四、你的应用中招了吗？怎么排查和修复**

如果你的应用用到了Brotli解压，那很可能受影响。具体来说，以下情况需要警惕：

**Node.js应用**

* 代码中显式调用了`zlib.brotliDecompress()`、`zlib.brotliDecompressSync()`等接口
* 使用了接受Brotli压缩数据的HTTP服务器（比如Express、Koa等框架，配置了Brotli解压）
* 使用了第三方库，这些库内部调用了Brotli解压

**Python应用**

* 导入了`brotli`或`brotlicffi`包
* 代码中调用了`brotli.decompress()`等接口
* 使用了接受Brotli压缩数据的Web框架或中间件

**Bun应用**

* 所有Bun应用，因为Bun内置了Brotli解码器

**Envoy代理**

* 配置了解压Brotli的过滤器

怎么排查？

**Node.js**

```
node -v  # 查看版本
# 对比受影响版本：22.x < 22.23.4, 24.x < 24.22.1, 26.x < 26.12.1
```

**Python**

```
pip show brotli  # 查看brotli版本
pip show brotlicffi  # 查看brotlicffi版本
```

**Bun**

```
bun -v  # 查看版本
```

怎么修复？

**Node.js**

* 22.x升级到22.23.4或更高
* 24.x升级到24.22.1或更高
* 26.x升级到26.12.1或更高
* 升级后重启所有Node.js进程
* 使用容器或自带Node.js运行时的应用，需要更新镜像或应用内置运行时并重新部署

**Python**

* 等待brotli和brotlicffi官方发布修复版本
* 临时缓解：避免解压来自不可信来源的Brotli数据
* 如果必须解压，先对数据进行大小和格式校验

**Bun**

* 等待Bun官方发布修复版本
* 临时缓解：禁用Brotli解压功能，改用gzip/deflate

**Envoy**

* 等待Envoy官方发布修复版本
* 临时缓解：禁用Brotli解压过滤器，或限制解压数据的来源

阿里云开发者社区的文章也提醒：默认情况下Node.js不会直接进行Brotli解码，需要应用或依赖实际执行Brotli解压。但目前未见公开利用代码与在野利用报告。

注意，”未见在野利用”不代表”不会被利用”。Imperva的Node2Shell已经证明漏洞是可利用的。攻击者只是在等，等你的Node.js还没升级。

# **五、供应链安全的老问题：一个库漏洞，半个互联网遭殃**

Brotli漏洞再次暴露了软件供应链的老问题：一个底层库的漏洞，会沿着依赖链向上蔓延，最终影响成千上万的应用。

2021年的Log4Shell（Log4j漏洞），影响了几十万个Java应用。2024年的xz-utils后门，差点让全球Linux系统遭殃。现在的Brotli漏洞，影响了Node.js、Python、Bun、Envoy等主流软件。

共同的特征：

1. **底层库被广泛依赖**：Log4j、xz、Brotli，都是各自生态中的基础组件
2. **漏洞影响面极广**：一个库出问题，成千上万的应用跟着遭殃
3. **修复协调困难**：需要每个使用这个库的软件各自发布修复版本
4. **用户感知滞后**：很多应用开发者根本不知道自己的应用用了这个库

怎么解决？几个方向：

**第一，软件物料清单（SBOM）。** 每个应用都应该维护一份SBOM，列出所有直接和间接依赖的库及其版本。这样一旦出现底层库漏洞，可以快速排查影响范围。

**第二，依赖自动更新。** 使用Dependabot、Renovate等工具，自动监控依赖库的安全公告，及时创建更新PR。不要等漏洞被利用了才想起来升级。

**第三，最小化依赖。** 不要引入不需要的库。每多一个依赖，就多一个潜在的攻击面。定期审查依赖，移除不再使用的库。

**第四，纵深防御。** 不要假设底层库是安全的。应用层应该有输入校验、输出编码、异常处理等机制，即使底层库出问题，也能减少影响。

Brotli漏洞目前还没有在野利用，但Imperva的Node2Shell已经证明了漏洞的可利用性。攻击者只是在等，等你的系统还没升级。

不要等被打了才动。现在就去检查你的Node.js、Python、Bun、Envoy版本，该升级的升级，该打补丁的打补丁。

**更多AI知识，请扫码关注Aiker World社区公众号**

![]()

**Aiker World社区网址：https://aikerworld.com**

**Aiker World（AI世界）-聚焦AI人才与智能体工具的垂直专家社区。专家领航+人才汇聚+工具赋能，打通AI技术与产业落地断层，为AI从业者、开发者及企业提供一站式成长与协作平台。**

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/316355](/post/id/316355)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [供应链安全](/tag/%E4%BE%9B%E5%BA%94%E9%93%BE%E5%AE%89%E5%85%A8)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=184300)

[安全客](/member.html?memberId=184300)

这个人太懒了，签名都懒得写一个

* 文章
* **88**

* 粉丝
* **5**

### TA的文章

* ##### [Node.js、Python、Bun全中招：一个压缩库的内存漏洞，让半个互联网"裸奔"](/post/id/316355)

  2026-10-26 14:54:01
* ##### [凌晨收到GitLab安全公告，CVSS满分，我看了看自家版本号](/post/id/316350)

  2026-10-26 14:47:16
* ##### [AI自己写勒索脚本、自己挑目标、自己搞钱：俄罗斯黑客的Phantom框架，把勒索软件玩成了自动化流水线](/post/id/316346)

  2026-10-26 12:02:03
* ##### [你的对手不是人了：Claude+Grok组队，400家金融机构被AI全自动攻破](/post/id/316272)

  2026-10-22 15:57:59
* ##### [月下载9000万次的AI网关LiteLLM曝双漏洞：低权限账号就能偷走你所有API密钥](/post/id/316257)

  2026-10-20 19:06:20

### 相关文章

* ##### [2.45亿次下载的Rust crate被投毒：编译时恶意代码自动执行，朝鲜黑客又出手了](/post/id/316013)

  2026-08-24 14:12:38
* ##### [你的代码里，藏着黑客埋的"毒"：1300个 npm 包遭供应链投毒](/post/id/315949)

  2026-08-11 10:55:59
* ##### [Ghostcommit 攻击：恶意提示藏入图片，劫持Agent实施窃取](/post/id/315788)

  2026-07-13 15:14:37
* ##### [恶意Skills利用扫描规避技术攻击Claude Code和Codex](/post/id/315737)

  2026-07-07 16:59:30
* ##### [国务院令第834号已落地：软件供应链安全，企业欠缺的不是工具，是这三件事](/post/id/315352)

  2026-05-20 17:22:05
* ##### [喜报 | 悬镜安全中标海通证券SCA软件成分分析工具采购项目](/post/id/301926)

  2024-12-12 11:28:11
* ##### [发现针对 Telegram、AWS 和阿里云用户的供应链攻击](/post/id/290825)

  2023-10-18 11:22:29

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)