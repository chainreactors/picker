---
title: 【AI安全】核爆级！朝鲜黑客毒穿Axios攻击OpenClaw
url: https://mp.weixin.qq.com/s/g1AVmKM7OKRMR8gJ3It0xg
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:26:20.779232
---

# 【AI安全】核爆级！朝鲜黑客毒穿Axios攻击OpenClaw

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y05UtykogHR4l3RdyhG1EviavuiaHYSldO6nib6tETJr9QSQucic8RGOK8RmbmKibyXthBWopJhT2fjB76uX7c2jk6O78OnwMWudHJCyIzFGqsRY/0?wx_fmt=jpeg)

# 【AI安全】核爆级！朝鲜黑客毒穿Axios攻击OpenClaw

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器中沉浸阅读

# 一、1亿人信任的“基础设施”瞬间沦为黑客肉鸡！🌍

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！🚀

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

谁能想到，平时写代码闭着眼睛都会敲的 `npm install axios`，竟然成了一道“催命符”！😱

上周国外顶尖安全媒体投下一枚震撼弹：大名鼎鼎、每周被全球开发者疯狂下载超过 **1 亿次** 的前端与 Node.js 圈“绝对基石”——**Axios**，竟然被朝鲜国家级黑客组织 **UNC1069** 成功破防！🏴‍☠️

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHTk9lHEbB2sMS6MqZslRm6kX3JeqPrPmcv6rMxVNFnf44YtXIrlQib0vKhgGMe6x3UbBARIX7o6rO8pCzLaqAPXsHhKAFBF7pWI/640?wx_fmt=png&from=appmsg)

黑客没有动用什么极其复杂的 0-day 漏洞去硬刚底层代码，而是极其狡猾地使用“社会工程学”（通俗点说就是网络钓鱼、套路欺骗），直接拿下了 Axios 核心维护者 Jason Saayman 的 npm 官方账号权限！🔑 拿到这把“最高权杖”后，黑客兵不血刃地向全球发布了两个暗藏剧毒的恶意版本：`1.14.1` 和 `0.30.4`。

很多小白或者跨界的朋友可能会问：**npm、Node.js、Axios 到底是个啥？为什么它被黑了，整个科技圈都要地震？** 🌐 别急，我们用最通俗直白的大白话给你扒得干干净净：

**1. 📦 npm：全球软件供应链的“超级大卖场”**npm（Node Package Manager）就是 Node.js 的官方包管理工具。你可以把它理解为程序员专属的“App Store”。全球几百万开发者都在这里上传自己写的工具包，或者下载别人写好的轮子。

* • **运行机制：** 你在项目里写一个 `package.json` 文件（相当于采购清单），敲一行代码，npm 就会自动去云端把你需要的组件全拉下来。
* • **致命弱点：****信任链条太长！** 🔗 这里任何人都能发包，只要有一个爆款包的作者被黑客搞定，所有引用这个包的项目都会瞬间被“连坐”感染！

**2. ⚙️ Node.js：现代互联网与 AI 的“底座引擎”**如果代码是汽油，Node.js 就是那台疯狂运转的 V8 引擎！🚗 它是一个基于 JavaScript 的服务器运行环境。

* • **广泛应用：** 从你每天刷的网页后端，到企业内部的自动化脚本，再到如今爆火的 **AI Agent（智能体，比如大名鼎鼎的 OpenClaw）**，全都在 Node.js 上跑！
* • **风险雷区：** 生态极其繁荣，依赖像蜘蛛网一样密集，随便一个中型项目都可能嵌套几千个依赖包。这就好比一栋大楼用了几万块不同厂家生产的砖，一块砖是炸弹，整栋楼都得塌！🏢💥

**3. 📡 Axios：全网通用的“快递小哥”**Axios 是什么？它是前端和 Node.js 最常用的 HTTP 网络请求库。

* • **绝对统治力：** 只要你的程序需要联网（比如前端去拿后端数据，或者 AI 去调用 ChatGPT 的接口），99% 的概率都在用 Axios！它支持拦截器、自动 JSON 转换，好用到离谱。
* • **恐怖现实：** 几乎所有 Node.js 项目都在用。这就意味着，Axios 一旦被投毒，就等于全国的自来水厂被下了药，没人能幸免！🚰☠️

---

# 二、🕷️ 瞒天过海：装包即爆的“幽灵剧毒”攻击链拆解

这次朝鲜黑客 UNC1069 的手段，堪称安全界的“完美犯罪”。很多大厂的安全审核员盯着 Axios 的核心代码看了半天，甚至用机器扫描了好几遍，竟然**完全没发现异常**！🤯

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHTCdYoGA2SFUicRNwuZehfBBfh1xWPyyMa5aiclLapYVGQicdT0BnGMLMicVl3UGWian2XJ9uJWDvNSbAqE7g2blBIl2wfo17KSmYBo/640?wx_fmt=png&from=appmsg)

为什么？因为**黑客根本没碰 Axios 的核心源码！** 🔪 这种攻击叫做“依赖劫持”，它把毒药藏在了你根本想不到的盲区里。让我们一步步拆解这场极其凶险的“隐形处决”：

#### 🛡️ 盲点一：狸猫换太子的 `package.json`

黑客上传了 `Axios 1.14.1`，但他们只修改了那个名为 `package.json` 的采购清单文件，在里面强行塞入了一个名为 `plain-crypto-js` 的莫名其妙的依赖包。

**📊 真假 Axios 依赖对比：**

| Axios 版本状态 | `dependencies` (依赖项清单) | 危险程度 |
| --- | --- | --- |
| 🟢 **正常版 (1.14.0)** | 只有正常的 `follow-redirects`, `form-data` 等 | 安全无毒 ✅ |
| 🔴 **剧毒版 (1.14.1)** | 正常依赖 **+ `"plain-crypto-js": "x.x.x"`** | 瞬间暴毙 💀 |

开发者在看代码 diff（差异）时，往往只盯着 `src` 里的业务代码，根本不会注意到清单里多了一个不起眼的“加密工具包”！

#### ⚡ 盲点二：`postinstall` 自动触发机制（装包即送命）

当受害者敲下 `npm install` 时，npm 会尽职尽责地把那个恶意的 `plain-crypto-js` 也下载下来。而在那个恶意包内部，黑客写下了最致命的一行代码：

```
"scripts":{
"postinstall":"node setup.js"
}
```

**`postinstall` 是什么鬼？** 这是 npm 的一个钩子机制，意思是“包下载完后，立刻自动执行后面的命令”。🚨 这就意味着：**你根本不需要在代码里引入（`require`）这个包，你甚至连项目都不用跑起来！只要安装进度条一走完，恶意的 `setup.js` 就已经在你电脑的后台无声无息地执行了！** 没有任何弹窗，没有任何提示，你的机器已经成了肉鸡！🐔

#### 🌍 盲点三：SILKBELL 多平台精准绞杀

不要以为你用 Mac 或者 Linux 就安全了！这个 `setup.js`（也就是名为 SILKBELL 的恶意载荷分发器）极度聪明，它会先摸清你的操作系统，然后精准下发对应的木马：

* • 🪟 **Windows 系统：** 释放隐藏的 VBS 脚本，偷偷拉起 PowerShell，直接绕过杀毒软件执行木马。
* • 🍏 **macOS 系统：** 写入 AppleScript，把编译好的 Mach-O 恶意二进制文件伪装成苹果系统缓存（比如叫 `com.apple.act.mond`），在后台静默狂奔。
* • 🐧 **Linux/服务器：** 针对 CI/CD 构建机，直接下载 Python 后门脚本，用 `nohup` 挂在后台死循环执行。

#### 👻 盲点四：教科书级别的“毁尸灭迹”

最让人头皮发麻的是，这个脚本执行完坏事后，会进行疯狂的反取证操作： 它会**删除恶意脚本自身**，**删掉那个带有恶意 postinstall 的 package.json**，然后**把一个提前准备好的、干干净净的 package.md 替换成真实的 package.json**！🗑️ 这导致安全人员事后去查服务器的 `node_modules` 文件夹时，看到的全是正常文件！完美隐身！

#### 🕹️ 终极后门：WAVESHAPER.V2 降维打击

一旦中招，黑客就会往你机器里植入名为 **WAVESHAPER.V2** 的终极后门。这个后门每 60 秒就会向朝鲜黑客的 C2 服务器发送一次“心跳”信号 💓，它拥有四大恐怖能力：

1. 1. **`kill`**：抹除一切痕迹自毁。
2. 2. **`rundir`**：疯狂扫描你电脑里的所有文件和目录。
3. 3. **`runscript`**：在你的机器上任意执行 Shell、PowerShell 或 AppleScript 命令。
4. 4. **`peinject`**：把更深层的恶意二进制文件直接注入到你电脑的内存里运行，杀软根本扫不到硬盘上有病毒！

---

# 三、🎯 致命暴击！OpenClaw等AI智能体惨遭“夺舍”控制

🎯 **【Agent 安全防护】**

黑客究竟是如何利用一个隐蔽的底层依赖，瞬间接管拥有极高权限的 AI 智能体的？当 AI 的认知逻辑和决策链遭到“降维打击”般的毒化，企业内网与核心数据资产又将面临怎样毁天灭地的灾难？

想要解锁本章深度剖析及 AI 被“夺舍”的四大致命维度拆解，请加入 **Oxo AI Security 知识星球** 获取完整内容！星球内部更沉淀了海量前沿干货

---

* • 📚 **AI 文献解读**：最前沿的 LLM 安全论文深度剖析。
* • 🐛 **AI 漏洞情报**：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。
* • 🛡 **AI 安全体系**：从红队攻击到蓝队防御的全方位知识图谱。
* • 🛠 **AI 攻防工具**：红队专属的自动化测试与扫描工具箱。

🚀 立即加入 **Oxo AI Security 知识星球**，掌握AI安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

Oxo Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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