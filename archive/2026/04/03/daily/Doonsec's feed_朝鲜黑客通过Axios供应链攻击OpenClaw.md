---
title: 朝鲜黑客通过Axios供应链攻击OpenClaw
url: https://mp.weixin.qq.com/s/LUSwo9AFR4PDMUjyFE_-WA
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:10:51.190718
---

# 朝鲜黑客通过Axios供应链攻击OpenClaw

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTvYAvEK8VztLBL2T2qZnmr1PeJ9FEaKAGG4mZU7PUXvouJ89Cg48XyqDjNdZqqJLoj30SBRNIHyQUVb3vulXtp11NogiasXeag/0?wx_fmt=jpeg)

# 朝鲜黑客通过Axios供应链攻击OpenClaw

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器中沉浸阅读

近日，国外安全媒体披露，一支与朝鲜相关的黑客组织 UNC1069，通过社会工程手段攻陷了 Axios 维护者 Jason Saayman 的 npm 账号，并成功发布了两个被篡改的 Axios 版本（1.14.1 和 0.30.4）。

值得注意的是，这次攻击并没有修改Axios的核心源码，而是通过引入一个名为 plain-crypto-js的恶意依赖，实现了隐蔽投毒。

这意味着——

开发者即使审核了 Axios 本身代码，也很难发现异常。

## npm、Node.js、Axios 到底是什么？

要理解这次攻击的威胁，需要先搞清楚三个关键组件：

### 1. npm：软件供应链的“高速公路”

npm（Node Package Manager）是 Node.js 的官方包管理工具，全球数百万开发者通过它下载和发布开源组件。

●  类似“应用市场”

●  任何人都可以发布包

●  项目依赖通过 package.json 自动拉取

👉 风险本质：信任链极长，一处被污染，全链路受影响

### 2. Node.js：现代应用的底层运行时

Node.js 是一个基于 JavaScript 的服务器运行环境，被广泛用于：

●  Web 后端开发

●  API 服务

●  自动化工具

●  AI Agent（如 OpenClaw）

👉 特点：依赖生态极其丰富（也意味着攻击面巨大）

### 3. Axios：最常用的 HTTP 请求库之一

Axios 是一个基于 Promise 的 HTTP 客户端，支持：

●  GET / POST 请求

●  请求拦截器

●  自动 JSON 转换

●  跨浏览器与 Node.js 使用

👉 现实情况：几乎所有 Node.js 项目都会用到

## 攻击过程拆解：一次“隐形执行”的供应链攻击

这次攻击的核心，不在“代码修改”，而在“依赖劫持”。

### 攻击路径如下：

#### 1️⃣ 社会工程攻击

黑客通过钓鱼或欺骗手段获取 Axios 维护者 npm 账号权限。

👉 本质：人是最薄弱的一环

#### 2️⃣ 发布带毒版本

上传两个版本：

●  Axios 1.14.1

●  Axios 0.30.4

但核心变化是：

"dependencies": {

  "plain-crypto-js": "x.x.x"

}

👉 关键点：恶意代码不在 Axios，而在依赖中

#### 3️⃣ 利用 postinstall 自动执行

在 plain-crypto-js 的 package.json 中：

"scripts": {

  "postinstall": "node setup.js"

}

👉 一旦开发者执行：

npm install

恶意代码自动在后台执行，无需任何用户交互。

#### 4️⃣ 多平台恶意载荷投放（SILKBELL）

setup.js 会根据系统下载不同 payload：

●  Windows → PowerShell 木马

●  macOS → Mach-O 二进制

●  Linux → Python 后门

👉 实现真正的“跨平台攻击”

#### 5️⃣ 清理痕迹（极具隐蔽性）

攻击完成后：

●  删除自身

●  替换 package.json

●  移除 postinstall

👉 开发者事后几乎无法察觉

#### 6️⃣ 后门能力（WAVESHAPER.V2）

最终植入后门具备以下能力：

●  kill：自毁

●  rundir：枚举文件系统

●  runscript：执行命令（PowerShell / Shell / AppleScript）

●  peinject：加载并执行二进制

并且：

👉 每 60 秒向 C2 服务器通信一次（心跳机制）

## 四、为什么 OpenClaw 受到直接影响？

这里是这次事件最关键的一点。

OpenClaw 本质是一个基于 Node.js 的 AI 智能体系统，其核心特征包括：

●  大量依赖 npm 生态

●  广泛使用 HTTP 请求（调用 API / LLM）

●  自动化执行任务（高权限运行）

👉 而 Axios 正是 OpenClaw 这类系统的“基础组件”。

### 风险传导路径：

Axios 被污染

      ↓

Node.js 项目依赖更新

      ↓

OpenClaw 安装或构建

      ↓

恶意代码执行

      ↓

Agent 被控制

### 对 OpenClaw 的具体影响：

#### 1️⃣ 智能体被远程控制

攻击者可以通过后门：

●  执行任意命令

●  操控任务执行逻辑

●  窃取数据

👉 相当于“劫持 AI 助手”

#### 2️⃣ 敏感数据泄露

OpenClaw通常会访问：

●  API Key

●  内部系统接口

●  用户数据

👉 一旦被控，等同于“数据中枢失守”

#### 3️⃣ 横向移动风险

通过 Agent：

●  扫描内网

●  访问数据库

●  调用其他服务

👉 从一个组件 → 整个系统沦陷

#### 4️⃣ AI决策链污染

攻击者甚至可以：

●  篡改任务执行结果

●  注入恶意逻辑

●  影响业务流程

👉 从“系统安全问题”升级为“业务安全问题”

## 五、攻击思路总结：为什么这类攻击越来越多？

这次事件体现了当前最危险的攻击趋势之一：

### 👉 “不攻击你，而是攻击你信任的东西”

核心逻辑：

1.  不碰核心代码（降低暴露概率）

2.  利用依赖链（扩大攻击面）

3.  利用自动化机制（无感执行）

4.  清理痕迹（难以溯源）

## 六、供应链攻击的本质危害

### 1. 影响范围极大

一个 npm 包，可能影响：

●  数百万项目

●  全球开发者

### 2. 隐蔽性极强

●  不改源码

●  不触发告警

●  不留明显痕迹

### 3. 信任体系崩塌

开发者默认信任：

●  npm 官方仓库

●  开源社区

●  维护者

👉 一旦被攻破，信任链全面瓦解

### 4. 对 AI 系统打击更大

传统系统 vs AI系统：

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibQwjSWkeRjXYy83j8ng9quPO47ZjBbKtnZHDAnlhbuUYs33DMsOOQicSXU7v7lYSXDKePdmhb3dgOXzudWzGIHmq9ia7BZavbUP8/640?wx_fmt=png&from=appmsg)

👉 AI时代，供应链攻击 = “放大器”

## 七、总结：这是 AI 时代的一次“预警”

Axios 事件不是一次普通的 npm 投毒，而是一个信号：

当 AI 智能体开始接管执行权，供应链攻击将直接演变为“系统级控制攻击”。

对于 OpenClaw 这类 AI Agent 平台来说：

●  每一个 npm 依赖，都是潜在入口

●  每一次自动执行，都是风险放大

●  每一个 Agent，本质都是“高权限执行器”

## 八、给从业者的三点建议

1. 锁定依赖版本（避免自动升级）

2. 禁用 postinstall 或进行审计

3. 引入供应链安全检测（SBOM / SCA）

如果说过去网络安全的核心是“防漏洞”，

那么今天，真正的战场已经变成：防信任被利用。

而这，才是 OpenClaw 时代最值得警惕的地方。

END

推荐阅读

[OpenClaw七大安全风险曝光：你的AI，可能正在被“远程操控”](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492810&idx=1&sn=653a6bcd0c89ad74e760b19e238c4e24&scene=21#wechat_redirect)

2026-04-02

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSu9RMfSbatm1rt4vFZ12VuD6VIFrcbCK3jfSiaWymjlrUHnibsEWnxSorN3K9QU2weuLPcsUbkjlfJJzEgLaOuBBn3gyGunfFZc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492810&idx=1&sn=653a6bcd0c89ad74e760b19e238c4e24&scene=21#wechat_redirect)

[Check Point 《2026年网络安全报告》中文版发布！免费下载](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492788&idx=1&sn=e1d9273b400657bdddb2b92b5cd6cae5&scene=21#wechat_redirect)

2026-03-31

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibT1pvgrrorR1J2Yj9ySE8NMxJ5RXNHSVHXKF30icuv9T4BxE17OoRkbq5DcHtic17HhN3NNtG0faAoMEN55AhQf3wCdRwIsySaUo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492788&idx=1&sn=e1d9273b400657bdddb2b92b5cd6cae5&scene=21#wechat_redirect)

[养龙虾不安全，我装了个安全龙虾](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492802&idx=1&sn=861f7b9c4a46eb143700fc657594599e&scene=21#wechat_redirect)

2026-03-30

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibRTkDqj7xLh1aIfALCS4z68QNAFPqYkEMKDEIXjJjZdA3CB8K7XZ8nAzXuoXr5Zf5HdtRCc8dluKnoo8KpPEicprYmR92tpiaGAQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492802&idx=1&sn=861f7b9c4a46eb143700fc657594599e&scene=21#wechat_redirect)

[Manus被叫停背后：大模型出海，正在进入强监管时代](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492781&idx=1&sn=78c52fc9650e73e00c5ed9baf7f3c281&scene=21#wechat_redirect)

2026-03-28

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQvr7E5L3DYLgJSztPoAhgkttf8adswYHTdCiaymQylGE325Zf4OuokQgMDmvAe87hnuC3ykAcicsK5QHWMfUTEBbib4P2MMrTaIs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492781&idx=1&sn=78c52fc9650e73e00c5ed9baf7f3c281&scene=21#wechat_redirect)

[AI时代，为什么说Skills是未来？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492776&idx=1&sn=c45810dd9ab2f00844b5e3cd0d08a89a&scene=21#wechat_redirect)

2026-03-27

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQgEg9Jm9tOlibuqpWfStrOS326dCZiak9Xzib9sLep3Ulpus58z6W2Sshr3FNtsrxkVV4UZFa08tBCSMPQWAZA99bibTdHkGYZElA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492776&idx=1&sn=c45810dd9ab2f00844b5e3cd0d08a89a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

兰花豆说网络安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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