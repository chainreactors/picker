---
title: AgentEscape：MCP服务器如何让AI助手读取你的私钥
url: https://mp.weixin.qq.com/s/Dw-KF6lYU0eRd3zycP_q_A
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:42:48.718210
---

# AgentEscape：MCP服务器如何让AI助手读取你的私钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcEwQSIEVD92B89fpyf4RibTFagUsLX2w4ZJ4aiaSGdxn6VxQomLdcKhyIRXD736ZU52ibSRGxcL8pllvoe2EBib3pPJ1YicuqrJH7g/0?wx_fmt=jpeg)

# AgentEscape：MCP服务器如何让AI助手读取你的私钥

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 一款拥有49k星标的流行MCP服务器项目存在路径穿越漏洞，攻击者可通过AI助手这个“中介”，远程窃取主机上的SSH密钥、数据库密码等敏感文件。这不是孤立事件，扫描发现36%的MCP服务器安全性不及格。本文剖析了这种独特的攻击面，并给出防护建议。

## 一次真实的攻击

攻击者现在可以这样黑掉你的AI助手：

1. 精心构造一个恶意提示，诱使助手去安装一个“技能”或“工作流”。
2. 助手会根据指令，调用MCP服务器的文件操作功能，传入类似 `../../.ssh/id_rsa` 这样的路径。
3. 由于服务器没有任何路径验证，它会直接读取这个文件并返回内容。
4. 你的SSH私钥就这样出现在了对话里，对攻击者一览无余。

这不是什么理论推演。这是在数万开发者使用的项目中真实存在的、可运行的漏洞代码。

## 漏洞的发现

我们的开源安全扫描工具 SpiderShield，发现了 upstash/context7[1] 项目中的一个路径穿越（CWE-22）漏洞。这个项目有超过49,000个GitHub星标，是MCP生态里最热门的周边项目之一。

问题出在技能文件安装的接口上。代码直接把用户输入的 `name` 参数拼接进了文件路径：

```
# 简化后的漏洞模式path = SKILLS_DIR / (name + ".yaml")# 如果 name = "../../.ssh/id_rsa" → 就会读取到预定目录之外的文件
```

没有做 `resolve()` 检查，没有验证上级目录，没有任何字符过滤。任何连接到这个服务器的AI助手，都可能被提示词注入或恶意技能欺骗，读取宿主机器上的任意文件。

## 能偷走什么？

| 文件 | 包含内容 | 带来的影响 |
| --- | --- | --- |
| `~/.ssh/id_rsa` | SSH私钥 | 获得你所有服务器的访问权 |
| `~/.env` | API密钥、数据库密码 | 账户完全沦陷 |
| `~/.aws/credentials` | AWS访问密钥 | 云服务被接管 |
| `~/.kube/config` | Kubernetes凭证 | 整个集群失守 |
| `/etc/passwd` | 系统用户列表 | 为后续攻击侦察开路 |

最要命的是，助手自己并不知道正在被利用。它只是在忠实地执行指令，去读取一个恰好是你私钥的“技能文件”。

## 修复措施

我们通过GitHub Issue #2234[2]报告了漏洞，并在PR #2235[3]提交了修复方案。核心是增加了路径边界校验：

```
resolved = path.resolve()if not resolved.is_relative_to(SKILLS_DIR.resolve()):&ensp;&ensp;raise ValueError("Path traversal detected")
```

这个修复在6天内被维护者审核并合并。如果你在使用context7，请立刻更新到最新版本。

## 这只是冰山一角

我们用SpiderShield扫描了15,923个MCP服务器。结果不太乐观，路径穿越是最常见的漏洞模式之一：

* 757个服务器存在令牌或凭证泄露问题。
* 有36%的MCP服务器拿到了F等级（不及格）。
* 路径穿越漏洞在文件操作工具、工作流管理和技能安装器中尤其普遍。

在那之后，我们在多个其他项目里发现了类似问题，并向28个代码仓库提交了37个修复请求。目前其中5个已被合并，涉及项目的总星标数超过86,000个。

说实话，这个比例和广度说明生态早期的安全盲区很大。

## 为什么MCP服务器格外危险？

传统Web漏洞需要攻击者自己找到并直接利用。MCP服务器的漏洞截然不同：**AI助手本身成了攻击媒介**。

传统Web应用是“攻击者 → 发现漏洞 → 利用它”。

而MCP服务器的情况是“攻击者 → 注入提示词 → AI助手替他去利用漏洞”。

助手对MCP服务器的工具拥有合法的访问权限，并且它天然信任接收到的指令。一旦这些指令被“下毒”——无论是通过提示词注入、恶意工具描述，还是被篡改的上游技能——这个助手就会在毫不知情的情况下成为攻击者的帮凶。

这意味着，每一个MCP服务器漏洞的危害性，都会被连接到它的AI助手数量所放大。

## 如何保护自己

**花30秒扫描你的MCP服务器：**

```
pip install spidershieldspidershield scan /path/to/your/mcp-server
```

**或者快速查看任意服务器的评级：**

```
spidershield check owner/repo
```

**检查你自己的代码时，留意以下几点：**

* **文件操作：**

  任何接收用户或助手输入作为路径的地方，都要加上 `resolve()` 和父目录检查。
* **子进程调用：**

  避免使用 `shell=True`，改用参数数组形式。
* **密钥比较：**

  不要用 `===` 直接比对密钥或令牌，改用恒定时间比较函数，例如 `crypto.timingSafeEqual()`。

## 事件时间线

| 日期 | 事件 |
| --- | --- |
| 2026-03-12 | SpiderShield扫描器在context7中标记出CWE-22漏洞 |
| 2026-03-13 | 提交Issue #2234和PR #2235 |
| 2026-03-19 | 维护者合并PR（处理了4条评审意见） |
| 2026-03-28 | 本文发布公开披露 |

> 所有漏洞均已通过负责任的方式披露，修复在本文发布前完成。SpiderShield[4]是开源且免费的。

---

### 参考资料

[1] https://github.com/upstash/context7

[2] https://github.com/upstash/context7/issues/2234

[3] https://github.com/upstash/context7/pull/2235

[4] https://github.com/teehooai/spidershield

[5] https://spiderrating.com/blog/agent-escape-mcp-servers-leak-your-secrets

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