---
title: 【提权基础入门第十节】在Windows Credentials Manager里发现的“定时炸弹”
url: https://mp.weixin.qq.com/s/AQUrVeFkWFibQe4oYQpQ1A
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:12:23.325166
---

# 【提权基础入门第十节】在Windows Credentials Manager里发现的“定时炸弹”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibc3GrC3sxx12Vtry7CI3hAdFQxMJWEBpibWnsVa0fmNPYohlB7hrLmRFmgKVNcJ6Tr0Zju5Sh1Q58Zt5UwXt30icgU5esxxytZxQ/0?wx_fmt=jpeg)

# 【提权基础入门第十节】在Windows Credentials Manager里发现的“定时炸弹”

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> Windows凭据管理器本是为了方便，但它保存的密码一旦泄露，就成了攻击者“开箱即用”的提权工具。本文详解了这种名为“Runas存储凭据”的攻击手法，从原理到实践，再到防御，并探讨了其背后更广泛的安全管理问题。

很多人觉得，把密码保存在Windows的凭据管理器里，既安全又省事。

实际上，这常常是个危险的便利。

当你点击“记住此密码”时，系统就把你的登录信息加密后存了起来。下次登录同一网站或网络共享，不用再输密码。这个功能（凭据管理器）本身没问题，问题在于它的使用方式和使用者。

设想一个场景：你在一台共享的工作站上，用管理员权限运行了一个程序并保存了凭据。之后，任何能登录这台机器的普通用户，都能利用这些保存的凭据，直接“变成”管理员。

听起来像电影情节？不，这只是Windows内置的`runas`命令和凭据管理器交互产生的一个经典漏洞。

## 凭据管理器：藏起来的钥匙串

Windows凭据管理器就像系统自带的一个钥匙串。它可以保管三种钥匙：

* 网络地址和共享文件夹的密码（Windows凭据）
* 网站登录信息（Web凭据）
* 应用的证书（基于证书的凭据）

它的设计初衷是好的，减少用户重复输入密码的麻烦，提升体验。

> 但安全领域有句老话：便利性和安全性往往是跷跷板的两端。为了便利，系统记住了密码；为了安全，密码本该被遗忘。

漏洞的核心在于`runas`命令的`/savecred`参数。运行`runas /savecred /user:Administrator cmd.exe`时，如果管理员密码输入正确，这条凭据就会被保存在当前用户的凭据库中。关键在于，之后再次运行带`/savecred`的任何`runas`命令，都**不需要再输入密码**。

这就像是管理员给自己当前用户留了一把万能钥匙，却没管紧谁有机会拿到复制品。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfZzZzUAlS1VDw1PGb3rq0gGPxwmFr4zRLqu91wHZ6cK1ia2SIlpLfInwp8euroWHpejeYDvfm7wZRiaNSWSZfdoOpu4QGxecLsQ/640?wx_fmt=png&from=appmsg)

## 攻击链条：从枚举到接管

整个攻击过程出奇地简单直白，这也是它危险的原因。攻击者几乎不需要高级技巧。

### 第一步：侦察

攻击者拿到一个普通用户权限后，首先会看看有没有“遗落的钥匙”。只需一个命令：

cmdkey /list

这会列出当前用户存储的所有凭据。如果在输出里看到了`Administrator`或者别的管理员账户，那基本就等于中奖了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdG1KJv0W8euh7qsR1zlsExzd6tcDaL47frtqcPsiadJ9fttFpqSpLpFh8fZxPCNWpY1yBewLbx1wW1jiafJUvQ9XSeV7xiaSaReI/640?wx_fmt=png&from=appmsg)

### 第二步：利用

看到有存储的管理员凭据后，攻击者可以直接用`runas`以管理员身份启动任何程序。假设他上传了一个后门程序`backdoor.exe`到`C:\Windows\Tasks\`目录下（这个目录通常有写入权限），那么执行：

runas /savecred /user:WORKGROUP\Administrator "C:\Windows\Tasks\backdoor.exe"

系统会瞬间以管理员权限启动这个后门，而整个过程完全静默，**不会有任何密码提示框**。

攻击链就此闭合，权限顺利提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcFtWL9sWI4ntTrC8tE6BDYwC8aM9kib64TAjgvicexCfccKiateQyD4sGhNL1rVrQzxaiazcetiaH4mMAomQB6hoCcyObyiaXq3pNibU/640?wx_fmt=png&from=appmsg)

整个流程里，最讽刺的是`/savecred`这个参数。它本意是“为用户保存凭据以方便下次使用”，结果却成了“为攻击者保存凭据以供随时盗用”。

## 为什么这是个棘手的问题？

这种攻击手法之所以难以根除，有几个深层次原因：

首先是功能设计的矛盾。`runas /savecred`的功能逻辑是：第一次验证成功后，后续使用都信任。这在单用户、物理安全有保障的环境下或许可行。但在企业多用户环境、或者终端可能被他人接触的情况下，这种信任模型就崩塌了。

其次是安全意识不足。很多用户，甚至系统管理员，并不知道凭据管理器里具体存了什么，更不了解`cmdkey /list`这个命令。安全风险往往来源于未知。

> 一个常见的坏习惯是：IT管理员为了方便维护，在用户电脑上直接用管理员账户登录操作，为了方便反复操作而保存凭据。这无异于把管理权限的门禁卡忘在了公共休息室。

最后是清理机制的缺失。Windows没有自动清理或定期提示机制。除非用户手动去控制面板删除，否则这些凭据会一直躺在那里，成为一个持续的威胁。

## 如何拆除这颗“定时炸弹”？

防御措施其实很明确，关键在于执行和习惯。

### 1. 定期检查与清理

最直接的方法就是去控制面板清理。路径是“控制面板 > 用户账户 > 凭据管理器”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfsiaSPxAXrsJKtqphzdtWT7ezIicUsVen8JiccLibjfy3ZuRAU9wnpMwb7eGF601pTcKJpWyyTHwDXOSic1o5WtMLJf3aB1x7tf8r4/640?wx_fmt=png&from=appmsg)

在里面找到“Windows凭据”，检查是否有不应存在的管理员级别凭据，果断移除。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibedtBcKFibIEQicmKCibMKRl7yib0JibxzrkfXpxOn6qgWyS4qKibRDTGmOO96iaSGKadkI6BWxpZGqKkrQcSkFibia53dt1NNmcn5ss3QM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeVwSWC7DVBGxqwFKtM3YicyicibobLaZcJhttgic8VYicMoXyRhVeplInXYweh54kgoxvFjpUEictYjbPXPDw2rAlQ9Hok0Blsk6m1I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeAKwNwia6RS13mP74uqyIY7sSE7m25kUiagFX5kjMRN41J0oOuOmiauTb2ayiaeUHYibdWHwQicnu0juPqibbPxxlq9yUG2LmpUGcibyA/640?wx_fmt=png&from=appmsg)

### 2. 改变操作习惯

* **绝不随意使用`/savecred`参数。**

  除非在完全受控的私有环境，否则应避免使用这个功能。
* **使用最小权限原则。**

  日常操作坚决不使用管理员账户登录。需要提权时，使用不带`/savecred`的`runas`或“以管理员身份运行”，每次手动输入密码。
* **清理共享环境。**

  对于公共或共用电脑，每次使用后应主动检查并清理可能遗留的凭据。

### 3. 技术管控（针对企业）

对于企业IT管理员，可以通过组策略来限制或监控：

* 考虑通过组策略禁止存储某些特定类型的凭据，尽管这可能影响部分便利性。
* 部署终端安全产品，监控`cmdkey /list`和`runas /savecred`命令的执行，将其视为可疑行为。
* 定期通过脚本在企业范围内扫描和汇报存在存储凭据的终端。

## 更深一层的思考

“Runas存储凭据”漏洞的本质，其实是一个授权（Authorization）和身份验证（Authentication）边界模糊的问题。

系统第一次验证了你是你（输入了正确密码），然后就把代表“你是你”的凭证（Token）存储起来，并允许用这个凭证去做任何事。但它没有绑定“事”的上下文。第一次可能只是想启动一个管理控制台，存储的凭据却被用来启动了恶意程序。

安全的授权机制应该是情境化的，应该问：“**当前这个动作，在这个时间，在这个环境下，是否被允许？**” 而不是简单地“你有凭证，所以一切放行”。

微软的文档（Interactive Logon Authentication Microsoft（https://learn.microsoft.com/en-us/openspecs/windows\_protocols/ms-authsod/bfc67803-2c41-4fde-8519-adace79465f6））详细描述了交互式登录的认证协议，但协议是理想的，使用方式却是千差万别的。

最后，说点实在的。下次当你图方便点击“记住密码”或者顺手加了`/savecred`参数时，可以先停一秒问自己：我是不是在创造一颗未来可能被他人利用的“定时炸弹”？

在安全的世界里，最危险的漏洞，往往不是那些需要复杂利用的零日漏洞，而是这种被遗忘的、由善意便利功能转化而来的“特性”。管理和使用好自己的凭据，是网络安全最基础，也最容易被忽视的一课。

回到文章开头那句话：密码管理器是安全的，不安全的永远是人使用它的方式。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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