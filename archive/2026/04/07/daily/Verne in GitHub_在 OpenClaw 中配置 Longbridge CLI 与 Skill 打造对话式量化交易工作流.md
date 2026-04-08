---
title: 在 OpenClaw 中配置 Longbridge CLI 与 Skill 打造对话式量化交易工作流
url: https://blog.einverne.info/post/2026/04/openclaw-longbridge-cli-and-skill-setup-guide.html
source: Verne in GitHub
date: 2026-04-07
fetch_date: 2026-04-08T04:30:42.350321
---

# 在 OpenClaw 中配置 Longbridge CLI 与 Skill 打造对话式量化交易工作流

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# 在 OpenClaw 中配置 Longbridge CLI 与 Skill 打造对话式量化交易工作流 用自然语言操作美港 A 三市场行情与交易

Posted on 04/07/2026
, Last modified on 04/08/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-04-07-openclaw-longbridge-cli-and-skill-setup-guide.md)

最近我一直在折腾自己的投资工作流，想把 AI Agent 和真实的行情、持仓、交易动作接到一起。手里一边是 [[Longbridge]] 账户，一边是 [[OpenClaw]] 这类可以扩展 Skill 的开源 Agent，单看都不缺能力，问题是它们原本不在一个工作界面里。查行情要切 App，下单要切网页，想做一点自动化分析还得自己补脚本。直到我把 Longbridge 官方的 longbridge-terminal 和 OpenClaw 里的 Longbridge Skill 接上，这套东西才终于顺了起来。现在我可以直接在终端里问 AI 一句话，让它去查报价、看持仓、整理数据，必要的时候再把下单命令准备好。这篇就把我自己跑通的过程和一些实际感受整理下来。

![OpenClaw 配置 Longbridge CLI 与 Skill](https://pic.einverne.info/images/openclaw-longbridge-cli-skill.png)

## 为什么要把 Longbridge 接入 OpenClaw

先说说我为什么会折腾这件事。[[Longbridge]] 的 App 其实已经做得不错，日常看盘、下单都没有问题。但我平时大部分时间都泡在终端和编辑器里，一旦要在写代码的间隙看一眼 NVDA 报价、核对一下持仓盈亏，或者顺手验证一个交易想法，就得把注意力从当前窗口里抽出去。看起来只是多点几下，实际很打断节奏。另一条路是自己写脚本接 OpenAPI，但那又是另一种麻烦，因为每多一个需求，往往就多一段脚本要维护。

OpenClaw 刚好把这个问题接住了。它本身是一个开源的 AI 助手，支持 Skill 机制。只要某个能力最终能落到命令行上，就能被包成一个 Skill 交给 AI 调用。这个思路不复杂，但很好用，因为它把“工具会用”和“AI 会调这个工具”分成了两层。CLI 负责把能力暴露出来，Skill 负责告诉 AI 什么时候该用、该怎么用。对我这种已经有一堆终端工具的人来说，这比重新等一个完整 GUI 产品成熟要现实得多。

把 Longbridge 接进去之后，很多以前要自己动手拼的小动作都可以直接交给 AI 了。比如我会问它“帮我看看现在持仓里 NVDA 是赚是亏”，它就去调用对应命令把结果整理出来。再复杂一点，也可以让它做组合层面的事，比如统计美股持仓的行业分布、汇总这周的持仓变化，或者盯着 TSLA 的盘前价格到某个阈值时提醒我。说到底，这套玩法最吸引我的地方不是“AI 会下单”，而是它终于把查数据、整理数据、准备动作这几个步骤收进了同一个界面里。

## Longbridge CLI 是什么

Longbridge Terminal CLI，也就是 `longbridge-terminal`，是 [[Longbridge]] 官方出的命令行工具。它覆盖的范围很广，基本把 Longbridge OpenAPI 里常用的能力都搬到了命令行上，行情、账户、订单、公告、财务数据这些都在里面。项目本身是 [[Rust]] 写的，更新也比较勤。对我来说，最重要的不是它是不是“AI-native”这种标签，而是它从一开始就把命令行输出做得比较规整，很多命令都能直接吐 JSON，这样 AI 才有东西可读。

它能做的事其实不少。查报价、五档、逐笔、K 线、盘中分时、财务报表、机构持仓、历史分红、账户余额、持仓、订单记录，这些都能直接拉。你如果只是把它当一个终端版行情工具来用，也已经够值了。更重要的是，它和 Skill 机制很搭，因为 Skill 最怕的不是能力少，而是底层工具输出不稳定、不好解析。Longbridge CLI 在这一点上做得还不错。

我自己比较常用的一块是期权链。以前在 App 里来回切期权到期日和行权价，总觉得差点意思。换成 CLI 之后，像 `longbridge option chain AAPL.US --date 2024-01-19` 这种命令，一次就能把完整链条拉出来。做策略筛选的时候，这种效率差别是很明显的。

认证流程走的是 OAuth 2.0 device flow，这一点我也挺喜欢。跑 `longbridge login` 之后，终端会给你一个地址和验证码，你拿任何一台能开浏览器的设备去授权就行。对远程服务器或者没有图形界面的环境特别友好，也省掉了把账号密码塞进脚本里的坏习惯。

## OpenClaw Skill 体系简介

OpenClaw 这边关键的就是 Skill。一个 Skill 说穿了就是一个目录，里面放一个 `SKILL.md`，再带上一些脚本、模板或者参考文件。`SKILL.md` 负责把规则讲清楚：什么场景该触发、该调用哪个底层命令、输出怎么处理。AI 依赖的是这层说明，不是凭空猜测。

OpenClaw 启动时会扫一遍 skills 目录，把这些描述加载起来。等你提问题时，它再去判断要不要用某个 Skill。这个设计我一直挺喜欢，因为它比把所有说明都硬塞进 system prompt 要节省得多，也更容易维护。你哪条规则写得不顺手，改 Skill 就行，不用去碰更底层的配置。

现在社区里已经有人把 Longbridge OpenAPI 做成了现成 Skill，发布在 OpenClaw Skills Marketplace 上，名字是 `openclaw-skills-longbridge-openapi`。它把行情、K 线、账户、订单这些常用动作都封装好了，所以第一次接的人不用从零自己写。

不过这里还是要区分一下 CLI 和 Skill 的职责。CLI 是干活的，Skill 是教 AI 怎么叫人干活的。没有 CLI，Skill 只是空说明；没有 Skill，AI 又不一定知道该在什么场景下调哪条命令。我的做法是尽量让 CLI 保持“纯工具”，把“用户问到行情时优先用 `longbridge quote`”“用户问到 K 线时用 `longbridge kline`”这种映射写进 Skill。这样出问题的时候也比较好查，到底是工具坏了，还是规则写得不够清楚。

## 配置流程详解

整个流程其实就三步：装好 Longbridge CLI、完成登录、再把 Skill 接进 OpenClaw。下面按顺序展开。

### 安装 Longbridge CLI

CLI 的安装非常简单。在 macOS 上推荐使用 [[Homebrew]]：

```
brew install --cask longbridge/tap/longbridge-terminal
```

如果你不想用 Homebrew，或者在 Linux 上使用，可以直接运行官方的安装脚本：

```
curl -sSL https://open.longbridge.com/longbridge/longbridge-terminal/install | sh
```

Windows 用户可以通过 [[Scoop]] 或者 PowerShell 脚本安装：

```
iwr https://open.longbridge.com/longbridge/longbridge-terminal/install.ps1 | iex
```

安装完成后运行 `longbridge --version` 确认安装成功。在 macOS 和 Linux 上，二进制文件会被放到 `/usr/local/bin/longbridge`；在 Windows 上则是 `%LOCALAPPDATA%\Programs\longbridge\longbridge.exe`。

### 完成认证

安装完 CLI 之后第一件事就是登录。运行：

```
longbridge login
```

终端会输出一段类似下面的信息：

```
Visit https://open.longbridge.com/activate
And enter the code: ABCD-1234
```

打开浏览器访问那个 URL，登录你的 [[Longbridge]] 账户，输入终端给出的 code 并点击授权，几秒之后 CLI 那边就会显示登录成功，token 会被自动保存到本地配置目录（macOS 上通常是 `~/.config/longbridge/`）。这种 device flow 的好处是你不需要在终端里输入用户名密码，token 也是按设备颁发的，可以随时通过 `longbridge logout` 注销。

如果你在远程服务器上部署，整个流程也是一样的。即便服务器上没有浏览器，CLI 给出的 URL 你也可以在本地电脑或手机上打开完成授权，授权信息会通过 Longbridge 的服务端同步给 CLI。

### 在 OpenClaw 中安装 Longbridge Skill

OpenClaw 的 Skill 默认安装位置是 `~/.openclaw/skills/`。从 OpenClaw Skills Marketplace 安装 Longbridge OpenAPI Skill 有几种方式。最简单的是通过 OpenClaw 的命令行工具：

```
openclaw skill install openclaw-skills-longbridge-openapi
```

这条命令会从 Marketplace 下载 Skill 包并解压到 `~/.openclaw/skills/longbridge-openapi/` 目录。安装完成后，你可以查看里面的 SKILL.md 文件，了解 Skill 的具体描述和使用方式。

如果你倾向于手动管理，也可以直接从 GitHub 仓库 `openclaw/skills` 的 `skills/genkin-he/longbridge-openapi/` 路径下克隆 Skill 文件夹，放到本地的 skills 目录即可。手动安装的好处是可以根据自己的需要修改 SKILL.md，比如调整某些命令的默认参数、添加自己常用的工作流模板等。

安装完成后需要在 OpenClaw 的配置文件 `~/.openclaw/openclaw.json` 里启用这个 Skill。OpenClaw 使用 JSON5 格式（支持注释和尾随逗号），配置示例如下：

```
{
  // 启用本地 skills 目录
  "skills": {
    "enabled": true,
    "paths": ["~/.openclaw/skills"]
  },
  // 为 Longbridge skill 设置环境变量（如果需要）
  "env": {
    "LONGBRIDGE_APP_KEY": "your_app_key",
    "LONGBRIDGE_APP_SECRET": "your_app_secret",
    "LONGBRIDGE_ACCESS_TOKEN": "your_access_token"
  }
}
```

需要注意的是，如果你已经通过 `longbridge login` 完成了 CLI 端的 OAuth 登录，那么 Skill 中可以直接调用 CLI 命令，无需再单独配置环境变量；但如果你的 Skill 是直接调用 Longbridge OpenAPI（绕过 CLI），那么 App Key、Secret、Access Token 是必须的。这两种调用方式各有优缺点，下面会详细说。

## 实战体验

我配置好之后，先拿最基础的查询试了一圈。比如问它“帮我看一下 NVDA 现在的报价和今天涨跌”，OpenClaw 就会去跑 `longbridge quote NVDA.US`，再把结果整理成我看得懂的格式。这个场景听起来不复杂，但一旦你真的开始这么用，就会发现它很顺手，因为你不用再自己记命令、切窗口、抄代码。

我后来用得最多的是组合查询。比如我会直接问“把 AAPL、NVDA、TSLA、META 今天的表现按涨跌幅排一下”。它会一次把几只股票的报价拉回来，排好序，再给个简单总结。手动做当然也不是不行，但你很难说服自己每天都愿意重复敲这一串。

K 线和财务数据也是类似。我会让它拉 BABA 过去 30 天的日 K，再顺手看看波动区间和最近走势；或者让它把 TSLA 最新一个季度的营收、净利润变化提出来，先做个粗筛。这里 AI 最有用的地方，不是它分析得多深，而是它把“拿数据”和“先整理一遍”这两步顺手做掉了。很多时候我只是想先看个大概，判断值不值得再往下研究，这种轻量整理就很够用了。

至于交易，我目前还是很保守。我只拿小金额做过测试，也只在自己明确下指令的时候才让它准备订单。Longbridge CLI 本身在 `buy`、`sell`、`cancel` 这类操作上会有确认提示，这已经能挡掉不少误操作，但我还是建议在 Skill 里再写死一条规则：除非用户明确要求，否则不要主动下单。行情和分析可以放开一些，交易动作还是得把最后一道闸门握在自己手里。

## 避坑指南

第一个坑是 token 的管理。Longbridge CLI 的 token 默认存储在本地，但 token 是有有效期的，过期之后需要重新登录。如果你在自动化脚本里调用 CLI，建议增加一个 token 刷新的检测逻辑，或者在 Skill 的初始化部分加上 token 校验。我自己写了一个简单的 wrapper 脚本，每次执行 CLI 命令前先检查 token 是否有效，无效时自动触发 `longbridge login` 流程。

第二个坑是 Skill 的描述精度。OpenClaw 的 AI Agent 是根据 Skill 的描述来判断是否调用的，如果描述写得太模糊，AI 可能在不该调用的时候调用，或者在该调用的时候漏掉。我的建议是在 Skill 的 description 字段里明确列出触发关键词，比如「股票」「行情」「报价」「持仓」「订单」等中文词汇，以及对应的英文词汇，提高匹配准确率。

第三个坑是市场代码的格式。Longbridge 使用统一的代码格式，港股是 `XXX.HK`，美股是 `XXX.US`，A 股是 `XXX.SH` 或 `XXX.SZ`。但 AI 有时候会忘记加这个后缀，比如直接说 NVDA 而不是 NVDA.US。在 Skill 里我加了一段说明，要求 AI 在调用 CLI 之前必须把股票代码补全成完整格式，否则 CLI 会报错。

第四个坑是数据频率的限制。Longbridge OpenAPI 对实时行情订阅有 QPS 限制，免费用户和付费用户的额度不一样。如果你让 AI 短时间内查询大量股票，可能会触发限流。建议在 Skill 里加上「同时查询不要超过 N 只股票」之类的约束，避免触发限流导致整个流程失败。

第五个坑是 CLI 与 Skill 的职责划分。我一开始尝试让 Skill 直接调用 Longbridge OpenAPI 的 Python SDK，结果发现需要管理一堆环境变量和 Python 依赖，反而比调用 CLI 更复杂。后来我把所有调用都改成走 CLI，Skill 只负责描述「什么时候用什么命令」，整个架构清爽了很多。所以如果你也是新手，建议优先走 CLI 路线，等熟练之后再考虑直接调用 SDK。

## 进阶玩法

跑通基础流程之后，我开始把它往更像“日常助手”的方向调。第一个比较实用的是盘前简报。我在 OpenClaw 里做了一个 `/morning-brief`，让它每天早上把持仓报价、主要指数、当天财报、我关注股票的公告拉一遍，再汇总成一份 Markdown 放进 [[Obsidian]]。这个东西不花哨，但我现在真的会用，因为它把原来散落在几个地方的信息收拢到了一起。

第二个我常用的是价格提醒和持仓监控。我会让它定时跑 `longbridge positions` 和 `longbridge quote`，算一下当前盈亏比例。如果到达我预设的止损或止盈区间，就通过 [[Telegram]] 发个提醒。这个工作流没有自动交易那么刺激，但对我来说更实用，也更安心。

财报季的时候，这套东西也特别顺手。我会让它盯住几家公司，在财报出来之后立刻拉一遍关键数据，先看营收、净利润和市场预期差多少。很多时候我并不需要第一分钟就做交易决策，但我确实想第一时间知道“这份财报大概好还是坏”。AI 在这里扮演的更像一个替我做初筛的研究助理。

期权筛选也是类似。结合 `longbridge option chain` 和 `longbridge calc-index`，它可以先把满足条件的合约挑出来，我再去看有没有值得进一步研究的标的。这个过程以前不是不能做，只是太碎了。现在我愿意更频繁地试，是因为入口变低了。

如果要说我对这些玩法最看重什么，不是“自动化程度很高”，而是它把很多重复、枯燥、但规则又很明确的工作替我先做了。真正要拍板的时候，还是我自己来。

## 安全性与合规考量

虽然这套工作流很好玩，但只要碰到真实账户，安全和合规就不能只当免责声明看。最先要...