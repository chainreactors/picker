---
title: 在 OpenClaw 中使用 Moomoo API Skills 查看和分析日本股市
url: https://blog.einverne.info/post/2026/04/openclaw-moomoo-api-japan-stock-analysis.html
source: Verne in GitHub
date: 2026-04-29
fetch_date: 2026-04-30T05:23:52.113680
---

# 在 OpenClaw 中使用 Moomoo API Skills 查看和分析日本股市

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

# 在 OpenClaw 中使用 Moomoo API Skills 查看和分析日本股市 用自然语言驱动 AI 查看日股行情、分析持仓、构建投研工作流

Posted on 04/29/2026
, Last modified on 04/29/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-04-29-openclaw-moomoo-api-japan-stock-analysis.md)

上一篇文章里，我介绍了[如何在 OpenClaw 中配置 Longbridge CLI 和 Skill，打通美股、港股、A 股的对话式查询与交易工作流](https://blog.einverne.info/post/2026/04/openclaw-longbridge-cli-and-skill-setup-guide.html)。但是长桥并没有日本市场的行情，也不支持日股交易，所以今天我就再来介绍一下如何在 OpenClaw 中接入 moomoo 日本的 API 以及相应的 Skill 来帮我分析日本股市。

过去几年里，我都是使用其他网页信息来看高配当股、追跟踪日经225的 ETF、分析株主優待，数据来源七零八落，每次要对比几只股票的走势，得分别打开浏览器、moomoo App、再加上自己的笔记，来回切换很耗精力。恰好这段时间我也在用 [[OpenClaw]] 搭建投研工作台，看到 [[Moomoo]] 官方推出了一套专门为 AI 工具设计的 Skills 包，就把两边接到了一起。接上之后，直接在终端里问”帮我看一下丰田最近一个月的日 K 和成交量变化”，AI 就能调起 Moomoo API 把数据拉回来，整理成我看得懂的格式。这篇就把这套工作流的配置过程和实际体验记录下来。

![在 OpenClaw 中使用 Moomoo API Skills 查看和分析日本股市](https://pic.einverne.info/images/openclaw-moomoo-japan-stock-analysis.png)

## 为什么日股研究特别需要 API 工具

先说说为什么我觉得 API 对日股研究特别有价值。日本股市有几个特点，让手动查询变得格外低效。一是标的数量多，东证（TSE）挂牌的上市公司超过 3900 家，光是做初步的行业筛选和财务比较，手动一家家看就很花时间；二是日本公司的财报、公告大量是日文，不顺手的人光是找关键数据就要花不少功夫；三是如果你同时持有日本股票和美股，两个市场时区不同，盯盘和整理数据的节奏很难统一。

通过 API 工具，这些问题大多可以用程序化的方式解决。我可以让 AI 一次性拉十几只候选股的 K 线，按波动率或换手率初步排序，把不符合条件的先过滤掉，再逐一深入研究。数据整理这个环节是最枯燥的，也是最适合交给 AI 的部分，把它解放出来之后，我的注意力才能真正放在判断和决策上。

[[Moomoo]] 的 OpenAPI 在这里是个合适的基础设施。它的行情数据覆盖美股、港股、A 股、日本、新加坡、澳大利亚等多个市场，架构上用本地运行的 [[OpenD]] 网关做中转，SDK 支持 Python、Java、C#、C++、JavaScript 五种语言。更重要的是，官方最近专门为 AI Agent 工具发布了一套 Skills 包，让 [[OpenClaw]] 这类工具可以直接调用，不需要自己写适配层。

## Moomoo OpenD 与 API 架构

在配置之前，先说清楚 Moomoo OpenAPI 的架构，因为理解这两层的分工对后面的调试很有帮助。

第一层是 moomoo OpenD，一个轻量的本地网关程序，需要运行在你的本地电脑或云服务器上。你的所有 API 请求，不管是查行情还是查持仓，都要先经过这个网关，再由它转发到 Moomoo 的后端服务器。OpenD 支持 Windows、macOS、Ubuntu 和 CentOS，启动之后需要用你的 Moomoo 账号登录一次完成授权，之后的 API 调用就在这个授权会话里进行。

第二层是各语言的 SDK，也就是 moomoo-api。以 Python 为例，`pip install moomoo-api` 之后就能用代码连接本地的 OpenD，发起行情订阅或者交易指令。SDK 和 OpenD 之间走的是自定义 TCP 协议，和语言无关。

这套架构对安全性和稳定性都有考量：账户凭证在 OpenD 里管理，你的脚本和 AI 工具只和本地 OpenD 交互，不直接接触账号密码；即便 AI 误操作，也只能在 OpenD 授权范围内行事。对于日常的行情查询和分析任务来说，这个结构已经足够顺手了。

## OpenClaw Skills 体系

[[OpenClaw]] 的 Skills 机制我在之前介绍 Longbridge 配置的文章里提到过。简单说，一个 Skill 就是一个目录，里面放了 SKILL.md 和若干脚本。SKILL.md 告诉 AI 这个 Skill 能干什么、什么场景下该用、底层命令怎么调用。OpenClaw 启动时扫描 skills 目录，把这些说明加载到上下文里，之后用户提问时它会判断要不要用某个 Skill 来响应。

Moomoo 官方提供的 AI Skills 包里包含两个模块：`install-moomoo-opend`（安装助手，负责检测操作系统并自动完成 OpenD 的下载、解压和启动）和 `moomooapi`（行情交易助手，内置 25 个脚本和 65 条 API 接口签名，覆盖行情查询、账户管理、交易操作等核心场景）。两个模块分工明确，前者解决”跑起来”的问题，后者解决”怎么用”的问题。

## 配置流程

整个配置分三步：安装 OpenD、完成登录授权、把 Skills 接进 OpenClaw。

### 安装 moomoo OpenD

最省事的方式是直接在 OpenClaw 里用自然语言触发安装助手。向 OpenClaw 发送以下提示：

```
阅读文档中的一键安装步骤，安装 moomoo OpenD 和相关 skills
https://openapi.moomoo.com/moomoo-api-doc/intro/ai.html
```

OpenClaw 会自动读取文档，识别你的操作系统并下载对应版本的 OpenD，完成解压和启动。这条路径对大多数人最省事。

如果你倾向于手动控制，也可以直接去 [Moomoo OpenAPI 页面](https://www.moomoo.com/ja/OpenAPI) 下载 OpenD，选择对应系统版本安装，然后启动并登录账号完成授权。还没有 Moomoo 日本账户的话，可以通过[这个链接](https://gtk.pw/moomoojp)注册，日股交易佣金免费，美股 NISA 账户佣金也免费。

OpenD 启动后需要手动登录 [[Moomoo]] 账号——可以通过 OpenD 自带的 Web 管理界面完成，也可以通过客户端扫码授权。这一步是每次重启 OpenD 后都要做的，不提供免登录的持久会话。

### 安装 Moomoo API Skills

Skills 的手动安装流程和 Futu API 类似：

```
# 下载 Skills 包
curl -L https://openapi.moomoo.com/skills/opend-skills.zip -o /tmp/moomoo-skills.zip

# 解压到临时目录
unzip /tmp/moomoo-skills.zip -d /tmp/moomoo-skills

# 复制到 OpenClaw 全局 skills 目录
cp -r /tmp/moomoo-skills/skills/* ~/.openclaw/skills/

# 清理临时文件
rm -rf /tmp/moomoo-skills /tmp/moomoo-skills.zip
```

如果你用的是 [[Claude Code]]，Skills 目录则是 `~/.claude/skills/`，两边的 Skills 格式是通用的，同一套文件可以同时放进两个目录使用。安装完成后在 OpenClaw 的对话框里输入 `/`，能看到 `moomooapi` 和 `install-moomoo-opend` 出现在补全列表里，就说明安装成功了。

## 实战体验：查看日股行情

配置好之后，我先从最基础的日股行情查询开始测试。

日本股票在 Moomoo API 里的代码格式是 `JP.XXXX`，比如丰田汽车（7203）是 `JP.7203`，索尼集团（6758）是 `JP.6758`，日本银行股里常被讨论的三菱UFJ金融集团（8306）是 `JP.8306`。这个代码格式和 Moomoo App 里显示的一致，一般不会搞混。

我最常用的几种查询方式大概是这样的：

查单只股票的实时报价和今日涨跌，直接说”帮我看一下日本株 JP.7203 丰田的现价和今天的表现”，它就会去拉实时报价，给出当前价格、涨跌幅、成交量，附带一段简短的数字总结。

对比多只股票的时候，我会说”把丰田（JP.7203）、本田（JP.7267）、日产（JP.7201）三只汽车股今天的涨跌幅排一下”，AI 会批量拉报价、排好序、输出一个简洁的比较列表。这种多标的并行查询以前要自己切 App 来回看，现在一句话就出来了。

K 线数据是我研究技术形态时用得最多的。让它拉某只股票过去 30 天的日 K 或者过去 3 个月的周 K，它会返回 OHLCV 数据，同时顺手做个简单的走势描述，比如”过去 30 天整体呈上升趋势，最近一周有高位震荡”之类的初步判断。这种初筛是最省时间的，因为它把”先看一眼值不值得继续研究”这个步骤替我做掉了。

日经 225 相关的查询也很常见。我会问”日经 225 今天的整体走势和成分股里涨幅最大的是哪几只”，这种跨标的的信息整合在 App 里翻是比较麻烦的，用对话的方式反而顺手。

## 避坑指南

第一个要注意的是 OpenD 必须保持运行。和 Longbridge CLI 不同，moomoo API 的所有请求都依赖本地的 OpenD 网关，如果 OpenD 停了，所有 API 调用都会失败。我的建议是把 OpenD 作为后台服务配置，开机自启动，或者在云服务器上部署，避免本地关机导致工作流中断。

第二个坑是 OpenD 登录有效期。Moomoo 的 OpenD 登录状态不是永久的，有时候会因为长时间未使用或者账号安全策略而失效，需要重新登录授权。如果 AI 突然报错说”连接失败”或者”未授权”，第一步先去检查 OpenD 是不是需要重新登录。

第三个是股票代码格式。Moomoo API 的日本股票代码必须带 `JP.` 前缀，直接说”7203”是查不到的。在 Skill 的描述里加上这条规则，让 AI 在构建查询时自动补全代码格式，可以省掉很多来回纠错的时间。

第四个是行情订阅有配额。根据账户等级，实时行情订阅的并发数量从 100 到 2000 个不等。如果在脚本或自动化工作流里订阅了大量标的，记得定期释放不用的订阅，不然跑满之后新的订阅请求会失败。

第五个是关于日本账户的使用范围。目前通过 Moomoo 日本账户的 API 接口，交易功能仅支持美国股票和美国期权；如果你想通过 API 查询日本股票的行情数据，建议确认你的账户权限是否包含日股数据订阅，或者联系 Moomoo 客服了解具体的开通方式。查询数据和执行交易在权限上是分开的，数据查询通常比交易的开通门槛低。

## 进阶玩法

基础流程跑通之后，我开始做一些更贴近日常研究的组合。

第一个是高配当股筛选辅助。我会让 AI 先批量拉一批候选标的的基本面数据，然后按股息率、PE、市净率做初步排序。光是这个环节，以前我要手动在多个数据源之间切换，现在可以用对话的方式驱动。

第二个是株主優待相关的分析。日本上市公司里有大量提供株主優待的公司，我在研究某只股票的時候，会让 AI 结合 K 线数据和配息时间点，看看権利確定日前后的价格走势有没有规律性的变化。这种分析以前是手工标注图表，现在可以让 AI 先做一遍初步整理，我再判断有没有值得深入的信号。

第三个是盘前晨报。我做了一个简单的工作流，每天开盘前让 AI 把我持仓的几只日本股票和关注的标的报价都拉一遍，顺手看看当天有没有重要的财报或者公告，再汇总成一份 Markdown 推送到我的 [[Obsidian]] 笔记里。这个工作流最值钱的不是有多先进，而是它真的每天在用，把原本分散在几个 App 里的晨报信息集中到了一个地方。

如果你对 AI 辅助量化有更深的兴趣，社区里已经有人基于 Moomoo API 开发了 MCP Server（`moomoo-api-mcp`），可以让 [[Claude]] 直接通过 MCP 协议调用 Moomoo 的行情和账户接口：

```
uvx --refresh moomoo-api-mcp
```

这条路对已经在用 Claude API 做定制开发的人比较实用，配合 Skills 的使用场景有所不同，具体选哪条路可以根据自己的工具链来判断。

## 最后

把 Moomoo API Skills 接进 OpenClaw 之后，我对日股研究工作流的感受变化主要体现在两点。第一是查数据这件事变轻了，不是因为 AI 能帮我做决策，而是它把”拿数据、整理一遍”这两步顺手做掉了，让我可以更快地进入真正需要判断的部分。第二是研究密度提高了，以前觉得”顺手看一下这只股票”成本不低，现在直接说一句就有结果，我自然就更愿意多比、多看。

日本股市本身还有很多值得深挖的地方，高配当、株主優待、小型价值股，不少机会是被散户投资者低估的。[[Moomoo]] 的 OpenAPI 加上 [[OpenClaw]] 的 Skills 机制，算是给这块研究工作提供了一个顺手的基础设施。如果你本来就在用 OpenClaw，Skills 包装好之后五分钟内可以开始第一个查询。对于日股研究这件事来说，工具的顺手程度往往直接影响研究的深度，这一点我越来越有体会。

如果你对日本股市本身感兴趣，除了这个博客，我也在 [EV 的日本生活记录](https://evjp.life) 持续写在日本生活和投资的一些观察，涵盖高配当股、株主優待、ETF 等话题，欢迎关注。

## Related Posts

* [在 OpenClaw 中使用 Moomoo API Skills 查看和分析日本股市](/post/2026/04/openclaw-moomoo-api-japan-stock-analysis.html) - 04/29/2026
* [OpenClaw 浏览器自动化方案对比：内置 browser 插件与 agent-browser 该怎么选](/post/2026/04/openclaw-browser-vs-agent-browser.html) - 04/28/2026
* [在 OpenClaw 中配置 Longbridge CLI 与 Skill 打造对话式量化交易工作流](/post/2026/04/openclaw-longbridge-cli-and-skill-setup-guide.html) - 04/07/2026

---

* [← Previous（前一篇）](/post/2026/04/openclaw-browser-vs-agent-browser.html "OpenClaw 浏览器自动化方案对比：内置 browser 插件与 agent-browser 该怎么选")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/04/openclaw-moomoo-api-japan-stock-analysis.html)评论。

* [经验总结 595](/categories.html#经验总结)

* [moomoo 1](/tags.html#moomoo)
* [openclaw 4](/tags.html#openclaw)
* [japan-stock 1](/tags.html#japan-stock)
* [ai-agent 10](/tags.html#ai-agent)
* [quantitative-trading 1](/tags.html#quantitative-trading)
* [skill 4](/tags.html#skill)
* [openapi 1](/tags.html#openapi)
* [moomoo-api 1](/tags.html#moomoo-api)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.inf...