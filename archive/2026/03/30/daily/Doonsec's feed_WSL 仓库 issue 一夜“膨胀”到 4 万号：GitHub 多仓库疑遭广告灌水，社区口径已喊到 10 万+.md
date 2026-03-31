---
title: WSL 仓库 issue 一夜“膨胀”到 4 万号：GitHub 多仓库疑遭广告灌水，社区口径已喊到 10 万+
url: https://mp.weixin.qq.com/s/vt0TKeKLn6oZoIZ4NdFZ8w
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:28.654997
---

# WSL 仓库 issue 一夜“膨胀”到 4 万号：GitHub 多仓库疑遭广告灌水，社区口径已喊到 10 万+

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ft77EUEUqosz9EsAglPXE11ZJr7ecCl8VkwJPUibdLvffsic6LqeXBPN4y8Z1b8e12ibMibIto2sWLG47Brseb50pCUfVOViaK4y4GFaoFu4y23A/0?wx_fmt=jpeg)

# WSL 仓库 issue 一夜“膨胀”到 4 万号：GitHub 多仓库疑遭广告灌水，社区口径已喊到 10 万+

原创

云梦DC
云梦DC

云梦安全

![]()

在小说阅读器中沉浸阅读

## 开场

很多开发者对 GitHub 的安全问题，第一反应往往是源码泄露、依赖投毒、账号接管。但这两天，一个看上去没那么“硬核”的问题，反而把不少开源维护者和围观者都看愣了:

**有人开始拿 GitHub Issues 当广告垃圾场，而且不是刷几条，而是把整个仓库的 issue 编号直接冲穿。**

最典型的案例，就是 `microsoft/WSL`。在 2026 年 3 月 29 日，WSL 维护者专门开了一个公告 issue，标题非常直白:

**[ANNOUNCEMENT] WSL Issue spam - We're on it!**

这不是普通意义上的“来了一波垃圾贴”。更准确地说，这是一次把 issue 体系本身当成攻击面使用的滥用行为。它的破坏力，不只在于广告内容本身，而在于它会制造：

* 巨量通知噪音
* 维护者处理队列堵塞
* 社区讨论区失真
* issue 编号永久膨胀
* 平台治理能力被公开拷问

## 先看 WSL 官方怎么说

从公开页面看，WSL 维护者 `benhillis` 在 **2026-03-29** 打开的公告 issue 里明确写道：仓库在过去一天收到了“**huge influx of spam issues**”，而且 GitHub 现有工具并不适合快速处理这类情况，所以他只能用脚本慢慢关。

这句话其实信息量很大。它至少说明了三件事：

1. 这不是用户误操作，而是明显的批量 spam。
2. 处理不是一键完成，平台端的批量治理工具并不顺手。
3. 维护者已经被迫从正常 triage，切换到“清场模式”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ft77EUEUqouDicAhqk3D4k9hwRLpUv8etKaF0RcCFwW73DhIv23wASwCE2ic64MqQMUy9uPfCFryL3PH3w4xwnLMugtVkhjJPKjtZJKg8YBMM/640?wx_fmt=png&from=appmsg)

## 真正值得警惕的，不只是广告，而是 issue 编号跳变

如果只是几十条广告贴，维护者顶多骂两句 GitHub 反垃圾做得差。但这次更夸张的地方在于，**issue 编号出现了极不正常的跳变**。

我直接用 GitHub API 抓了几个受影响仓库在 2026 年 3 月 30 日仍然能看到的结果，能得到下面这张表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ft77EUEUqoufSQ09Ojz2wusdBABpjczictQ4MicBRjyo97ic2hlicpxwYx91WNxgqICvhVtle2J8x19QicVMSLicA1zKS3cXbjMAJ2DvT1711icGAI/640?wx_fmt=png&from=appmsg)

从这张表里最值得注意的，是三个仓库的“前后编号差”：

* `microsoft/WSL`：从 **#14575** 跳到 **#40028**
* `isce-framework/isce2`：从 **#1023** 跳到 **#26663**
* `msgpack/msgpack-node`：从 **#60** 跳到 **#25685**

这意味着什么？

意味着即使中间大量 spam issue 最终被关闭、删除或者清理掉，**编号本身已经被永久消费掉了**。只要 GitHub 的 issue 编号分配机制还是按仓库自增，这种滥用就会留下非常明显、而且几乎不可逆的“污染痕迹”。

仅这三个仓库，直接可见的 issue 编号膨胀就已经达到：

**25,453 + 25,640 + 25,625 = 76,718**

也就是说，不用靠传闻，不用靠截图猜测，光是肉眼可核实的三例，已经足够证明这不是“小规模刷贴”，而是一次明显的批量滥用事件。

## WSL 不是孤例，另外两个仓库也能看到极端跳号

如果说 WSL 还可以理解为“大仓库本来 issue 就多”，那么另外两个仓库的情况就更有冲击力。

### 1. isce2：从 1023 硬生生跳到 26663

`isce-framework/isce2` 这个仓库的 issue 列表非常有代表性。在截图里你会看到，前两条就是和这次 spam 相关的处理/说明 issue，而紧接着往下翻，正常 issue 编号还停留在 **#1023**。

这说明中间凭空多出了两万五千多个 issue 编号位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ft77EUEUqotyfpup26DBCSPSNc1GTxMsrQt7ppKIkK33KYHhlFKf6N5SdSlI4HrP4U6PQCPlWME72I0lCXibVGybYt6d5sksE54lVshcRXfI/640?wx_fmt=png&from=appmsg)

### 2. msgpack-node：从 60 跳到 25685

更离谱的是 `msgpack/msgpack-node`。这个仓库原本 issue 数量就不高，但在 2026 年 3 月 29 日，它的列表顶部直接出现了一个 **#25685** 的“清理 spam” issue，而下面紧接着就是 **#60**。

这已经不是“异常”两个字能概括的了。它更像是有人拿自动化工具，直接对 issue 系统做了长时间、高频率、重复性的灌水。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ft77EUEUqovrEF3EwQKRLhAjO7DIM3uiapabg0BPvRcplMN1DjccNiaULF8OJhKHdaxasNxrAeM33EiaicbIRzZx3GogibYecPG44JAO6kcsQ6Ss/640?wx_fmt=png&from=appmsg)

## 社区为什么会喊出“累计 10 万+”

到这里，我们其实已经能理解为什么社区会迅速把这件事描述成“10 万+”级别了。

原因不是因为有人已经拿到了 GitHub 官方的总统计，而是因为：

1. 三个直接可核实仓库的小计就已经达到 **76,718**。
2. Reddit 社区在 **2026-03-29** 的讨论帖里明确提到，**WSL 和 many other repos** 同时遭遇重度 spam attack。
3. 同一帖里还有观察者提到，攻击样本里疑似存在 **100 个** 带相似痕迹的 bot 账号。
4. 社区还提到，攻击内容中夹杂中文博彩广告，以及看上去像面向生成式搜索/AI 抓取的 React 文本段落。

这里必须讲清楚：

* **“100 个 bot 账号”** 来自社区观察，不是 GitHub 官方确认。
* **“累计 10 万+”** 目前也更像社区推算，而不是平台披露数据。

但如果只从目前能直接验证的公开证据出发，说这是一次**至少 7 万级、很可能逼近 10 万级**的 issue 体系滥用事件，我认为是谨慎而不过分的表述。

## 这波攻击为什么比普通广告 spam 更值得写

很多人看到这里可能会说：不就是广告 issue 吗？关掉不就完了？

事情没有这么简单。

### 第一，它不是内容污染，而是工作流污染

GitHub Issues 对开源项目来说，不只是留言区。它本身就是项目管理、bug 跟踪、需求讨论和用户支持的工作入口。

一旦这里被灌爆，受影响的不只是页面观感，而是整个维护流程：

* 维护者要额外筛选真假 issue
* 邮件通知可能被刷爆
* 正常用户的 bug 报告更容易被埋掉
* 自动 triage 流程可能被拖慢
* 社区信任感会明显下降

### 第二，它会留下“永久编号疤痕”

比起删除广告内容，更麻烦的是 issue 编号已经被消耗。未来无论维护者还是用户，只要回看历史，都能看到这段异常膨胀。

这会带来两个副作用：

* 数据分析失真比如你想看仓库增长趋势、issue 活跃度、响应效率，都会被污染数据干扰。
* 运营和治理成本上升因为很多自动化工具默认把 issue 编号当成时间线近似代理，一旦编号膨胀，很多经验判断都会失灵。

### 第三，它暴露的是平台治理短板

WSL 维护者那句“GitHub does not have the best tools to do this”，其实已经点出核心矛盾了。今天的 GitHub 在代码托管、协作、CI/CD 上已经非常成熟，但在**大规模 issue spam 治理**这件事上，至少从公开表现看，仍然不够强硬、不够自动化，也不够让维护者省心。

## 一个容易被忽视的细节：这可能不只是“发广告”

Reddit 社区贴里有个观察很有意思：攻击内容不只是中文博彩广告，还混入了 React 之类的技术文本，有人怀疑这可能跟 **GEO（Generative Engine Optimization）** 或面向 AI 抓取系统的污染有关。

这一点目前没有 GitHub 官方确认，所以不能当成定论。但它至少提示了一个值得继续观察的方向：

**未来的垃圾内容，可能不只想骗真人点击，也想污染模型抓取、搜索索引和自动摘要。**

如果这个判断最终被更多证据支撑，那么这波事件的性质就会更复杂。它将不再只是“广告 spam”，而是“面向平台协作系统与 AI 抓取生态的双重污染”。

## 对 GitHub 和开源维护者，这次事件最现实的提醒是什么

我觉得有三点特别现实。

### 1. 平台需要更强的“非常态限流”能力

遇到这类突发滥用，维护者最需要的不是慢慢关 issue，而是：

* 临时冻结新 issue
* 按账号批量封禁
* 按模式批量删除
* 快速恢复通知秩序

如果这些能力要靠维护者自己写脚本，那说明平台工具链还有明显空缺。

### 2. 仓库治理不能只盯代码安全，也要盯协作入口安全

很多团队对仓库安全的关注点仍然集中在：

* 凭据泄露
* 依赖投毒
* PR 恶意代码

但 issue、discussion、wiki、release note 这些公开协作入口，同样可能成为滥用面。它们未必直接改代码，但能让仓库在运营和维护层面瘫掉。

### 3. 开源社区需要重新理解“垃圾内容攻击”

以前我们对垃圾内容的理解，更多停留在论坛、博客评论、邮件群发。现在看来，开源协作平台本身也已经成了目标。

因为对攻击者来说，这里有：

* 免费流量
* 高权重页面
* 搜索引擎与 AI 抓取入口
* 大量订阅通知用户
* 天然的公开传播性

这意味着“内容污染”与“协作系统滥用”未来可能会越来越交叉。

## 结尾

如果把这件事简单概括成“WSL 被刷广告了”，那就把问题看小了。更准确的说法应该是：

**GitHub 的 issue 体系，正在被人当成一个可批量利用、可制造噪音、可留下永久痕迹的攻击面。**

WSL 只是这次最显眼的一个名字。真正值得所有开源维护者警惕的，是这件事背后暴露出的趋势：

* 攻击目标不再只盯代码仓库本身
* 协作入口也会成为垃圾内容攻击面
* 平台治理效率会直接决定社区恢复速度
* 以后“仓库被污染”这件事，可能会越来越常见

如果 GitHub 不能更快补上这块治理短板，那么下一次被“冲号”的，未必还是 WSL。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

云梦安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

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