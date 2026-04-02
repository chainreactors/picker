---
title: 51万行代码\"裸奔\"！Anthropic又犯了同一个错误，这次细节更炸裂
url: https://mp.weixin.qq.com/s/2cV-7iDNiMEuvwJ4Q0-fTQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:33.509920
---

# 51万行代码\"裸奔\"！Anthropic又犯了同一个错误，这次细节更炸裂

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yJLbez93fl9cMibHQoWzMC42Jibk23e1IG2fxiaicHULOXBiaAibqTXP6ISHWaNI8OXK0RlGTqOkDuIDk6ZKcpluDxuBib2ccsIRPibc2yGiaSnVLqnA/0?wx_fmt=jpeg)

# 51万行代码"裸奔"！Anthropic又犯了同一个错误，这次细节更炸裂

原创

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器中沉浸阅读

> **文章类型**：安全事件解读 + 实操建议 **发布平台**：网络安全老宋（secure\_song） **字数**：约2800字 **预计阅读时间：**5分钟

---

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flicicZn66MUibtu6icv7PVQ21ibrOuS1ZAPqcxXgMpBr9G5ibdNAF6594Hx4cHySb7B6fyLpwwpaJKmwoibK0S5uIj2wlKiauC75apaZ3k/640?wx_fmt=png&from=appmsg)

2026年3月31日，一个配置错误，让 AI 行业最火的编程工具 Claude Code，把 **51万行核心源代码** 暴露在了全网面前。

更讽刺的是——

**这不是第一次。**

2025年2月，同样的错误，同样的路径，Anthropic 已经犯过一次。

时隔一年，**原样复发。**

---

### 一、事件经过

3月31日，安全研究员 Chaofan Shou 在 npm 注册表中发现了一个异常：

Anthropic 发布的 Claude Code CLI 包里，附带了一个 **59.8 MB 的 `.map` 文件。**

这个文件叫 `cli.js.map`——是构建工具生成的 source map 调试文件。

正常情况下，这种文件只用于本地开发调试，**绝不应该出现在对外发布的生产包里。**

但 Anthropic 的发布流程里，没有人拦住它。

消息迅速传开，有人把还原后的源码上传到了 GitHub 仓库 `claude-code-source：`

* 📁 **1,906 个文件**
* 📝 **51.2 万行 TypeScript 代码**
* ⭐ **5400+ Star，8800+ Fork**（几小时内）

全网开发者开始疯狂解读，安全圈也没闲着。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yJLbez93fl82w3zKw179cicNCLHvlPxOnqxGYqGDChwpwsayXIefsIpsVibhPjPibSibhTVcCrAViaNBnia83dl050miaJkTiaTwJJPka0w5EsCxEWI/640?wx_fmt=jpeg)

### 二、问题的根源：一个本不该犯的低级失误

先说清楚技术原因，不复杂：

**什么是 source map？**

前端/Node.js 项目在发布时通常会对代码进行压缩混淆，比如把一个有意义的变量名 `userPermission` 压缩成单个字母 `a，`让代码体积更小、也更难被反向阅读。

source map 文件的作用是建立"混淆代码 → 原始代码"的映射关系，方便开发者在报错时定位问题。

它就像一本"翻译字典"——

有了它，任何人都可以把压缩后的代码**完整还原成原始源代码。**

**正确做法：**发布 npm 包时，通过 `.npmignore` 或 `package.json` 的 `files` 字段，明确排除 `.map` 文件。

**Anthropic 的做法：**忘了。

而且这个"忘了"，已经是 **第二次** 了。

---

### 三、泄露了什么？安全影响有多大？

很多人问：泄露出来的代码，对我们普通用户有什么影响？

直接结论：

**a 用户的数据没有被直接泄露**（泄露的是客户端代码，不是服务端数据库）

**b 但安全影响并不小，尤其对企业用户和开发者**

具体来看：

#### 1. 两个高危漏洞被坐实

代码解析后，安全研究者发现了两个已知漏洞：

* **CVE-2025-59536**（远程代码执行）
* **CVE-2026-21852**（API密钥窃取）

以前这些漏洞"可能存在"，现在有了源码，攻击者可以精准定位到漏洞位置，**利用难度大幅降低。**

#### 2. 权限绕过漏洞细节曝光

源码中有一个安全 Bug：

PLAN 文件的权限检查使用了 `startsWith` 前缀匹配——

这是一个 **过宽匹配** 的逻辑漏洞。

举个例子：如果白名单里有 `/safe/path，`攻击者创建 `/safe/path-evil` 目录同样能通过检查。

这种漏洞在代码审计中属于典型的"信任边界模糊"问题，在渗透测试里是很常见的突破口。

#### 3. 内部员工标识逻辑泄露

源码中有这样一段逻辑：

if (process.env.USER\_TYPE === 'ant') {
   // 内部员工才能使用的额外工具权限
}

这意味着什么？

攻击者只需在环境变量中设置 `USER_TYPE=ant，`就能**尝试解锁内部权限。**

虽然服务端还有校验，但这无疑给了攻击者一个明确的攻击方向。

#### 4. 供应链攻击风险上升

最值得警惕的攻击路径：

1. 攻击者发布一个"分析 Claude Code 源码"的恶意 GitHub 仓库
2. 诱导开发者克隆并运行
3. 利用初始化钩子（`postinstall`）静默执行恶意代码
4. 窃取 API 密钥、Claude 会话 Token

**现在这个时间节点，已经有人在这么做了。**

---

### 四、顺手扒出的"未公开功能"

这次泄露还有个意外收获——

源码里藏着几个 **尚未上线的功能原型：**

| 功能代号 | 描述 |
| --- | --- |
| `PROACTIVE` | 主动模式：AI 会在你不问的情况下主动给建议 |
| `KAIROS` | 时序决策：AI 能感知当前时机决定是否介入 |
| `DAEMON` | 后台运行：AI 在后台持续监控，随时待命 |

这些功能意味着：**未来的 AI 工具将从"被动响应"走向"主动行为"。**

从安全角度看，这是一个重要信号——

当 AI 开始主动行动，我们的终端权限管理、进程监控策略，都需要同步升级。

---

### 五、对普通用户和企业用户的实操建议

不废话，直接说要做什么：

#### 立即要做（今天）

**1. 升级 Claude Code 版本**

npm update -g @anthropic-ai/claude-code

升级到 **2.0.65+，**Anthropic 已修复已知安全 Bug。

**2. 检查并轮换 API 密钥**

如果你在用 Claude API，登录 Anthropic 控制台，**立即轮换 API Key。**

这不是多此一举——一旦你的 Key 被泄露，对方可以无限消耗你的额度或用你的身份发起请求。

**3. 审查本机环境变量**

# 检查是否有可疑的环境变量设置

```
env | grep -i claudeenv | grep -i antenv | grep -i api_key
```

---

#### ToDo 近期要做（本周内）

**4. 检查 npm 全局包来源**

```
npm list -g --depth=0
```

重点审查近期安装的、来源不明的包，特别是名字里带 `claude、``anthropic、``ai-tool` 等关键词的仿冒包。

**5. 对企业用户：审查 AI 工具的网络访问权限**

Claude Code 的正常运行只需访问 `api.anthropic.com，`如果你的终端检测到它在向其他地址发起请求，**立即告警。**

**6. 警惕近期出现的"源码分析工具"类仓库**

供应链攻击的高发期就是现在。

对任何声称"帮你分析 Claude Code 源码"的仓库，在运行前必须：

# 先检查 package.json 有没有可疑的 scripts

```
cat package.json | grep -A5 '"scripts"'
```

# 检查 postinstall 钩子

```
cat package.json | grep "postinstall"
```

有 `postinstall` 脚本的陌生仓库，**不要随便跑。**

---

#### ToDo 长期来看（这件事背后的普遍教训）

**对开发团队：**

发布流程里必须加入 **source map 检查：**

# 发布前用这个命令预览会发布什么内容

```
npm pack --dry-run
```

# 确认输出列表里没有 .map 文件

简单一行命令，能拦住这次价值无法估量的泄露。

**对安全团队：**

AI 工具现在已经是企业常用工具了，它的安全管理不能空白。

至少要做到：

* 限制 AI CLI 工具的网络出口
* 监控 AI 工具对敏感目录（`~/.ssh、``~/.aws`）的访问
* API 密钥统一用密钥管理服务（KMS）管理，禁止硬编码在代码里

---

### 六、最后说一句

有人说这次事件没啥大不了的——源码都出来了，说明 Anthropic 没有太多黑魔法。

这话没错。

但作为安全从业者，我更关注的是：

**一家顶级 AI 公司，连续两年在同一个地方摔跟头。**

这不是技术能力问题，这是流程问题、文化问题。

当我们在追问 AI 安全、数据安全的时候，首先得问：**做 AI 工具的人，自己的安全意识够不够？**

这次泄露，是一个很直接的答案。

---

**如果你觉得这篇有用，转给你们技术团队的同事看看。**

**用 Claude Code 的开发者朋友，真的建议今天就去转一下 API Key。**

---

## 附件：本文核心要点速览

| 问题 | 答案 |
| --- | --- |
| 泄露原因 | npm 包中遗留 source map 文件 |
| 泄露规模 | 1906个文件，51.2万行代码 |
| 是否影响用户数据 | 不直接影响 |
| 主要安全风险 | API 密钥窃取、供应链攻击、权限绕过 |
| 用户立即要做什么 | 升级版本 + 轮换 API Key |
| 企业要做什么 | 限制 AI 工具网络出口 + 监控敏感目录访问 |

---

### 往期精彩

[开机自动显示电脑IP地址？这个小技巧让桌面“开口说话”！](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485519&idx=1&sn=8dad7ce2164b6c4abe63af016ec9148e&scene=21#wechat_redirect)

[红队视角下的暴露面攻防：如何从一个弱点撕开企业防线？](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485563&idx=1&sn=7d1d12904a8d700714b52aef2f4262f1&scene=21#wechat_redirect)

[实战视角下的云平台安全：从攻击路径到防御体系的全景解析](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485552&idx=1&sn=5160d3927b73bbb4006d965bddc73159&scene=21#wechat_redirect)

[终端攻防全链路解析：红队如何从一台电脑拿下整个内网？](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485454&idx=1&sn=6fe621fb3b423279921144cf24eb73c0&scene=21#wechat_redirect)

[三行神秘命令，一键优化 Windows？真相在这里！](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485246&idx=1&sn=dcc27fd9fda5ac8fa27311185563e5c9&scene=21#wechat_redirect)

如果你感觉有用，帮忙点个免费的关注转发，你的支持是我更新的动力

关注我的人，顺风顺水顺财神，朝朝暮暮有人疼！无一例外！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

网络安全老宋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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