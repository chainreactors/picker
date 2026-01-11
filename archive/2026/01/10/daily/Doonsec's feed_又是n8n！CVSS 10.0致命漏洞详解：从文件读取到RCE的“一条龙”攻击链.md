---
title: 又是n8n！CVSS 10.0致命漏洞详解：从文件读取到RCE的“一条龙”攻击链
url: https://mp.weixin.qq.com/s/jjUdwk5w2P7vAFHWZ3wPdg
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:46.134647
---

# 又是n8n！CVSS 10.0致命漏洞详解：从文件读取到RCE的“一条龙”攻击链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wWBwsDOJT49vicQyWqPD1sGniaIt5y1ibic3yZX4DB9pbUKChbWFOfrgtqBlNQh4wVVcy4yxQahFMXnx96BhV8QicIg/0?wx_fmt=jpeg)

# 又是n8n！CVSS 10.0致命漏洞详解：从文件读取到RCE的“一条龙”攻击链

原创

Hankzheng

技术修道场

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wWBwsDOJT49vicQyWqPD1sGniaIt5y1ibic306Mk7CCWT9Ev70lCnHJ7qpZZkIoE1ibHG53MkajlfhYQiaxXAWgFrPKA/640?wx_fmt=png&from=appmsg)

大家好，作为一名同时也负责IT运维的“老司机”，看到 **n8n** 和 **CVSS 10.0** 这两个关键词组合在一起，你猜我心情如何？

n8n 是我们很多团队都在用的自动化神器，因为它太方便了，但也正因为它连接了太多的API密钥、数据库和敏感服务，一旦被攻破，后果就是“火烧连营”。

---

兄弟们，如果你正在公司内部跑着 **n8n** 做自动化流程，请尽快检查一下你的版本号。

这几天被一个代号为 "Ni8mare"（噩梦）的漏洞刷屏了。

🔴 漏洞速览 (CVE-2026-21858)

* **危险等级：**

  CVSS 10.0 (满分)
* **攻击条件：**

  无需登录 (Unauthenticated)
* **后果：**

  任意文件读取 -> 远程代码执行 (RCE)

这可不是那种“理论上存在风险”的小打小闹。这意味着攻击者**不需要任何账号密码**，不需要和你进行任何复杂的交互，就能远程接管你的 n8n 实例，顺便把你存放在里面的 API Key、数据库密码打包带走。

作为一名同样在用 n8n 串联业务的运维老兵，我看完漏洞细节后的第一反应是：**这个逻辑漏洞，简直太“经典”了。**

今天我们就来扒一扒，这个满分漏洞到底是怎么绕过防御的。

## 🚨 为什么这次的漏洞是“满分”？

最近 n8n 确实有点“水逆”。过去两周，官方连续披露了 4 个高危漏洞。但请注意，之前的几个漏洞（比如 CVE-2025-68613），虽然评分也高达 9.9，但它们都有一个前提：**攻击者需要有登录权限**。也就是说，黑客得先搞到你某个员工的账号，才能搞事情。

但这次的 **Ni8mare** 不同：

* **无需登录**

* **无需交互**

* **全权接管：**

  从读取文件到执行任意命令（RCE）。

简单说，只要你的 n8n 暴露在公网且版本受影响，在黑客眼里，它就是一只待宰的肥羊。

## 🛠️ 技术拆解：当 Content-Type 成为“骗子”

这个漏洞的核心，出在 n8n 处理 **Webhooks** 和 **文件上传** 的机制上。

我们知道，Webhooks 是 n8n 的灵魂。在 n8n 的底层代码中，有一个关键函数 `parseRequestBody()`，它的职责是根据请求头里的 `Content-Type` 来决定怎么处理数据：

1. 如果是 `multipart/form-data`：说明是表单上传，调用 `parseFormData()`，把解析出的文件信息存到 `req.body.files` 变量里。
2. 如果是其他类型（比如 JSON）：调用普通解析器，把数据存到 `req.body` 里。

**问题就出在这里！**

Cyera 的安全研究员发现，在处理表单提交的函数 `formWebhook()` 中，代码逻辑出现了一个致命的疏忽：

> 它直接调用了文件处理函数去处理 req.body.files，却没有再次校验当前的 Content-Type 是否真的是 multipart/form-data。

这给了黑客一个搞事情的机会：

1️⃣ **攻击者发送一个普通的 JSON 请求**，而不是文件上传请求。
2️⃣ 在 JSON 的 Body 里，攻击者手动构造一个名为 `files` 的对象，并伪造 `filepath` 参数。
3️⃣ 因为不是 multipart 类型，n8n 的文件解析器不会运行，`req.body.files` 本该是空的。
4️⃣ **但是！** 此时 `req.body` 已经被 JSON 解析器填充了，而攻击者构造的 JSON 数据正好覆盖了 `req.body.files`。
5️⃣ 后续代码傻傻地以为这是用户上传的文件，直接读取了攻击者指定的 filepath（比如服务器上的敏感文件）。

这就是经典的 **“类型混淆”（Type Confusion）**。代码以为它在处理上传的临时文件，实际上它在读取你服务器上的 `/etc/passwd` 或者 n8n 的配置文件。

## ⛓️ 攻击链：从“偷看”到“夺权”

你可能会问：“只能读文件而已，离控制服务器还远吧？”

天真了。n8n 作为一个高度集成的系统，**任意文件读取** 加上 n8n 的架构特性，足以构建出一条完美的 **RCE（远程代码执行）** 攻击链：

**第一步：窃取数据库**
攻击者利用漏洞读取 `/home/node/.n8n/database.sqlite`。这可是 n8n 的心脏，里面存着所有用户的信息。

**第二步：提取管理员哈希**
从数据库里，黑客轻松拿到了管理员的 User ID、邮箱和密码哈希。

**第三步：拿到加密秘钥**
光有哈希还不够，黑客继续利用漏洞读取 `/home/node/.n8n/config` 配置文件，拿到了系统的 **Encryption Secret Key**。

**第四步：伪造 Session**
有了用户 ID 和加密秘钥，黑客就可以自己在本地伪造一个合法的 Session Cookie。

**第五步：RCE 降临**
带着伪造的 Cookie，黑客以管理员身份登录后台。接下来就简单了：**新建一个工作流 -> 拖入一个 "Execute Command" 节点 -> 输入任何想执行的系统命令。**

至此，你的服务器彻底易主。

## 🛡️ 你的 n8n 安全吗？

**❌ 受影响版本：**
所有低于（包含）**1.65.0** 的版本。
(注意：中间有些版本可能也有风险，请以官方公告为准)

**✅ 已修复版本：**
**1.121.0** （2025年11月18日发布）
目前最新版本包括 1.123.10, 2.1.5, 2.2.4, 2.3.0 等。

如果你也是 Censys 上那 26,000 多个暴露在公网的 n8n 用户之一，请务必执行以下操作：

1. **立刻升级！立刻升级！立刻升级！** 这是最彻底的解决办法。

2. **网络隔离：** 如果不是业务必须，千万不要把 n8n 的管理面板直接暴露在公网。套一层 VPN 或者加一个 Basic Auth 的 Nginx 反代。

3. **强化表单验证：** 对所有的 Form 表单开启身份验证。

## ✍️ 碎碎念

n8n 的强大在于它连接了一切，但这也意味着它是企业的 **“单点故障”** 所在。

想象一下，你的 n8n 里配置了 AWS 的 Access Key，连接了生产环境的数据库，还绑定了 Slack 的机器人 Token。黑客攻破了 n8n，就等于拿到了你整个云端架构的万能钥匙。

这次的 CVE-2026-21858 给我们所有 IT 人敲了个警钟：**低代码和自动化虽然爽，但安全基线不能丢。**

不多说了，我要去检查我的 Docker 镜像了。各位，好运！👊

如果你觉得这篇文章对你有帮助
欢迎 **点赞、在看、转发**
让更多的技术兄弟看到！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/wWBwsDOJT48jXhr3LrlFvFZoevRic7DnQnTT7l1Xh2vwQZFg0EVXZj8AfvVs3uBFwDRS7JsuQ7NXlaCW0Iq6feA/0?wx_fmt=png)

技术修道场

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/wWBwsDOJT48jXhr3LrlFvFZoevRic7DnQnTT7l1Xh2vwQZFg0EVXZj8AfvVs3uBFwDRS7JsuQ7NXlaCW0Iq6feA/0?wx_fmt=png)

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