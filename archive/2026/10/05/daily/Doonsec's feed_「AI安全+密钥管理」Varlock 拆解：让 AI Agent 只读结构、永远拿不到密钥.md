---
title: 「AI安全+密钥管理」Varlock 拆解：让 AI Agent 只读结构、永远拿不到密钥
url: https://mp.weixin.qq.com/s/a2txkgM312_zejyOVd9MlA
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:22:03.861949
---

# 「AI安全+密钥管理」Varlock 拆解：让 AI Agent 只读结构、永远拿不到密钥

# 「AI安全+密钥管理」Varlock 拆解：让 AI Agent 只读结构、永远拿不到密钥

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

给 AI 编码助手读一遍你的项目，它就能翻到 `.env`；你让它顺手改个功能，它可能在生成的代码里写死一个 API Key。这两件事——**把密钥递给 AI**，和**让 AI 把密钥写进代码**——正好是 AI 辅助开发里最常见、也最难靠人眼拦住的两条泄露路径。

`dmno-dev/varlock` 就是冲着这两条路来的。它的自我定位只有一句话：**AI-safe .env files: Schemas for agents, Secrets for humans.**（给 Agent 看的结构，给人类用的密钥。）它没有停在「把 `.env` 加进 `.gitignore`」这一层，而是从「密钥在哪里被读到、在哪里被写出去」重新设计了 `.env` 文件扮演的角色。

## 先核身份

用 GitHub API 当天核实：仓库 `dmno-dev/varlock`，**4665 颗星、130 个 fork、71 个未关闭 issue**，主语言 **TypeScript**，协议 **MIT**。2025 年 4 月 11 日建仓，最近一次提交在 **2026 年 10 月 2 日**，最新发布 `varlock@1.21.1`（2026 年 9 月 29 日）。仓库 topics 挂着 `configuration`、`dotenv`、`env`、`env-vars`、`schema`、`security`、`validation`，官网 `varlock.dev`。

它自己把要解决的问题写成了两条：

1. **Secret exposure（密钥暴露）**：AI 工具会读你的项目文件，包括 `.env`。varlock 让密钥不以明文存在于任何文件里，运行时才从安全来源取。
2. **AI-generated leaks（AI 生成的泄露）**：AI 生成的代码可能硬编码密钥、或把敏感值打进日志。`varlock scan` 在提交前抓泄露，运行时保护负责把日志和响应里的密钥脱敏。

## `.env.schema` 当单源真相

传统做法里 `.env.example` 只是一次性的模板，复制成 `.env` 之后就再没人管它，很容易和真实配置脱节。varlock 把 `.env.schema` 变成**持续生效的单源真相**：它用一套叫 `@env-spec` 的 DSL，在 `.env` 文件里用 JSDoc 风格的注释给每个变量挂上结构化元数据——类型、校验规则、描述、是否敏感、默认值。

```
# @defaultSensitive=false @defaultRequired=infer @currentEnv=$APP_ENV
# ---
# @type=enum(development, preview, production, test)
APP_ENV=development

# @type=port
API_PORT=8080

# @type=url
API_URL=http://localhost:${API_PORT}

# @required @sensitive @type=string(startsWith=sk-)
OPENAI_API_KEY=
```

![Varlock 在编辑器里对 OPENAI_API_KEY 的智能提示：变量名、类型、@sensitive 标记、说明和文档链接都能看到，但看不到值（仓库真实示例图）](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4LftmJHIKRjImvaKOdQpKKwic0VGIicBIIOaWL1qTn59crNdu1xmjp19picKibK3rTRqRnNGccVWzz3GWPN4ggUBJbicKZiabeJTfZ3Me0/640?wx_fmt=png "Varlock 在编辑器里对 OPENAI_API_KEY 的智能提示：变量名、类型、@sensitive 标记、说明和文档链接都能看到，但看不到值（仓库真实示例图）")

关键在于这张图里**没有值**。AI 助手读 `.env.schema` 能拿到变量名、类型、校验规则、描述，以及 `${API_PORT}` 这种变量展开关系，但它读不到 `OPENAI_API_KEY` 的真实内容——因为真实内容根本不在文件里，运行时才从插件或本地加密值里取。

要让 AI 工具能读到 schema，还要在 `.gitignore` 里显式放行 `!.env.schema`（多数 AI 工具默认忽略 `.env.*`），同时 `.env` 本身仍然被忽略。

## 三层防护：扫、脱敏、拦

varlock 把「密钥不落地」拆成三道工序，分别管提交前、运行中输出、运行时出站。

**第一层是 `varlock scan`。** 它加载 varlock 配置、解析出所有 `@sensitive` 的真实值，然后拿这些值去整个项目里搜明文泄露。默认扫所有非 gitignore 的文件，`--include-ignored` 连被忽略的也扫，`--staged` 只扫已暂存的文件，也可以直接指定路径。一旦命中，它报出文件、行号、命中的是哪个密钥，并以非零退出码结束。`varlock scan --install-hook` 能自动装 pre-commit 钩子（识别 husky、lefthook，否则写进 `.git/hooks/pre-commit`），把这道闸门挂在提交前。

![varlock 运行时检测到泄露时抛出的错误：DETECTED LEAKED SENSITIVE CONFIG - SECRET_KEY，附 env.ts:150:15 行号（仓库真实示例图）](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4Lfvf9C2zibwm10dFORnwh9ynibrRpfx3SLFt2fMWDQwvwl3eicia4wslGzDSBFpkHSybpIduqIQt2IFoF1QHE5JgiaF03tcQloLZs71c/640?wx_fmt=png "varlock 运行时检测到泄露时抛出的错误：DETECTED LEAKED SENSITIVE CONFIG - SECRET_KEY，附 env.ts:150:15 行号（仓库真实示例图）")

**第二层是日志脱敏。** CLI 自己的输出就带脱敏，`varlock explain` 用部分掩码（`my▒▒▒▒▒`）显示，让你能核对配置而不把密钥留在终端滚动历史里。`varlock run` 的输出被管道或重定向时（CI 日志、`| tee`、写文件），子进程的 stdout/stderr 会过同一个脱敏引擎，敏感值在落盘前就被掩码；接到交互终端时则直通——因为管道会破坏 `psql`、`claude` 这类靠 TTY 检测的工具，而坐在终端前的人本来就有密钥权限。`--no-redact-stdout` / `--redact-stdout` 可强制开关。

![varlock load 的输出：OPENAI_API_KEY 已被掩码，NUMBER_ITEM 显示由 123.45 强制转换的结果，APP_ENV 为 development（仓库真实示例图）](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4Lfujf3ZMyIeolwCZhxUVtfDwgIfxnRlCibYgjC1eauLeRJC18vicpP6gxufkRpDQicO1CzIDibPr4ybBiaVS2MsdqicY0y80xaMwicdGTU/640?wx_fmt=png "varlock load 的输出：OPENAI_API_KEY 已被掩码，NUMBER_ITEM 显示由 123.45 强制转换的结果，APP_ENV 为 development（仓库真实示例图）")

在 JavaScript/Node 项目里还有运行时脱敏：用 `varlock/auto-load` 或框架集成时，它会 patch 全局 `console` 的 `log/warn/error/debug/info/trace`，把敏感值替换成 `▒` 掩码（`my-secret-value` 变成 `my▒▒▒▒▒`），覆盖字符串、数组、普通对象和 `Error`（含消息、堆栈和嵌套内容）。需要故意在日志里看真值时，用 `revealSensitiveConfig` helper。

**第三层是出站泄露拦截。** 它 patch Node 的 `ServerResponse`（拦截 `write`/`end`，扫文本和 JSON 响应体，含压缩体）和全局 `Response` 构造器（覆盖 Cloudflare Workers 这类边缘运行时），如果发现敏感值正要发给客户端，直接抛错、拒绝发送并给出诊断（含配置项 key 和检测位置）。流式响应跨 chunk 边界也扫：当 chunk 末尾看起来像某个敏感值的开头时，这段尾部会先被扣住最多 15ms，等下一个 chunk 到来，好把完整值抓出来再发。

## 凭证代理 + 沙箱：密钥不进 Agent 的进程

这是 varlock 最有意思的一段，也是它对「AI Agent 要**用**密钥」这个真问题的回答。

**它先承认代理本身不是硬边界。** 官方文档写得很直白：代理内建的守卫（占位符隔离、schema 指纹校验）只是抬高门槛，一个铁了心的 agent 可以 `setsid` 另起一个进程、脱离代理的视野去直接找密钥源。

所以它配上 OS 沙箱，给出两层叠加：

```
varlock proxy run --sandbox -- claude
```

在 macOS 上，`--sandbox` 用系统自带的 `sandbox-exec` 把子进程关进一个「凭据 + 出网」牢笼，不用额外安装：

* **出网**只留 loopback，于是 `127.0.0.1` 上的代理成为子进程**唯一**的出网路径。进程就算把 `HTTPS_PROXY` / `HTTP_PROXY` 环境变量清掉想绕过代理，也根本连不出去。
* **凭据材料**：拒读 varlock 用户目录（加密密钥、插件/凭据缓存、代理会话/重载通道），也拒连该目录下的 unix socket——解密本地密钥的守护进程就在那个 socket 上监听，而「拒读文件」管不住 socket 连接，所以这条连接要单独挡。
* **系统 keychain**：拒 `mach-lookup` 到 keychain 守护进程（`securityd` / `SecurityServer`），agent 就不能用 `security` 或 `SecItemCopyMatching` 直接读 keychain 密钥。
* **热的凭据 agent**：拒 `mach-lookup` 到 1Password helper 这类进程，agent 就不能直接驱动一个已经解锁的 `op` 会话。
* 保留 `trustd`，所以 HTTPS 还能正常做信任评估。

Linux 或想要更强隔离时用 `--sandbox=docker`：agent 容器跑在一个 `--internal` 网络上（完全无外网路由，裸出网直接失败），一个不持任何密钥的 `socat` 转发容器当 `varlock-proxy` 桥到主机代理。密钥永远不进任何容器：主机代理解析后只在已验证的上游连接上注入真值，容器里始终只有占位符。

schema 里对应的声明是 `@proxy(domain="api.anthropic.com")`（哪些域名允许拿真密钥）、`@proxyConfig={egress="strict"}`，以及 `@placeholder=«redacted:sk-…»`——给那些启动时要检查 key 形状的 SDK 用。

## 插件系统：密钥从哪来

varlock 的插件负责声明式地从外部来源取值，官方插件覆盖 1Password、AWS Secrets Manager / Parameter Store、Azure Key Vault / App Configuration、Bitwarden、Dashlane、Doppler、Google Secret Manager、HashiCorp Vault、Infisical、KeePass、Keeper、Kubernetes、pass、passbolt、Proton Pass，以及 macOS keychain。插件可以注册新的装饰器和 resolver 函数，例如：

```
# @plugin(@varlock/1password-plugin)
# @initOp(token=$OP_TOKEN, allowAppAuth=forEnv(dev))
# ---
# @sensitive @required
MY_SECRET=op(op://my-vault/item-name/field-name)
```

不想依赖外部 provider，也可以用设备本地加密把值存进 gitignored 的 `.env.local`（`varlock(local:abc123...)`），密钥绑定本机设备，不共享、不提交。`@setValuesBulk()` 则用来一次性灌入一批 key/value，省掉逐条接线的样板。

## 上手

```
npx varlock init            # 安装向导（JS 项目里装成依赖）
brew install dmno-dev/tap/varlock
curl -sSfL https://varlock.dev/install.sh | sh -s
docker pull ghcr.io/dmno-dev/varlock:latest
```

```
varlock load                 # 校验并打印环境变量（脱敏）
varlock run -- python script.py   # 把解析后的变量注入子进程
varlock scan --install-hook   # 装 pre-commit 泄露钩子
varlock proxy run --sandbox -- claude
```

给 agent 用还有一套非交互模式：`varlock init --agent` 跳过交互确认、用确定性默认值；`varlock load --agent` 默认 JSON 输出并脱敏 `@sensitive` 值，可以安全留在 agent 转录里；需要判断「为什么非法」时用 `--format json-full`（带 `--agent`，否则会吐出裸密钥，官方明确警告不要放进 agent 转录）。真正该拿来分支的是**退出码**：`varlock load` 配置非法时非零，`varlock run` 转发子进程退出码，`varlock scan` 发现泄露返回 1。

## 避坑

1. **`@sensitive` 不是万能的。** 官方专门列了一张「varlock 保护不了的值」的表：少于 12 字符的敏感值只会警告——脱敏没有 token 边界，一个叫 `acmeco` 的敏感值会把日志里所有 `acmeco` 都替换掉，包括本来不是密钥的普通文本；少于 3 字符直接报错；布尔值（只有 1 bit，脱敏还会把所有 `true`/`false` 改写）、数字（脱敏只替换字符串，数字根本不脱敏）、以及含非字符串元素的数组/对象都保护不了。数字密钥要么 `@type=string`，要么加引号（`PIN="007123"`），顺便保住前导零和 2^53 之后的精度。真要用短值，得显式 `@sensitive={allowShortValue=true}`，表示你读过并接受碰撞风险。
2. **`varlock scan` 的前提是配置能解析。** 它要先加载配置、解析出所有敏感值，才能拿去比对；如果密钥本身取不到（凭据过期、provider 不通），扫描也跑不起来。
3. **扫描是明文比对，不是模式识别。** 它不猜「哪个字符串像密钥」，而是拿你真实的敏感值全文匹配。所以它抓不到「你没在 schema 里标成敏感」的密钥——标漏了，扫描就看不见。
4. **运行时脱敏和防泄露只覆盖 JS/Node 项目**（用 varlock 运行时集成时）。其他语言没有这层运行时保护。
5. **`--sandbox` 是 opt-in 的。** 官方说得很实在：太紧的沙箱会悄悄把 agent 弄坏，所以默认不开；裸 `--sandbox` 目前只支持 macOS，Linux 用 `--sandbox=docker`（还要自己提供含命令的 `--sandbox-image`）。
6. **代理不是硬边界。** 只有叠上 OS 沙箱才把「能力」也拿走；否则一个 `setsid` 起的新进程就能绕过进程检测去直接找密钥源。
7. **本地加密的值绑定设备**，不能共享、不能提交，不是团队共享方案。
8. **性能取舍。**`@preventLeaks` 和 `@redactLogs` 默认开，要检查 console 输出和响应体，官方自己提醒有性能开销，需要时可选关。

## 适合谁

适合：重度使用 AI 编码助手、又不想把真实密钥交给它的开发者；要把 API key 安全注入 MCP server 的场景；想给 AI 生成的代码加一道「提交前泄露闸门」的项目；以及需要「给 Agent 看结构、不给密钥」这类最小权限配置的团队。

不太适合：指望一个工具包圆密钥治理全流程的团队——varlock 主要管的是 env / 密钥这一层（校验、脱敏、扫描、代理注入）；或者只想用模式匹配猜密钥、不打算维护 schema 的人。

如果你现在还在把 `.env` 直接交给 AI 助手，最小的一步是把 `.env.example` 换成 `.env.schema`，标好 `@sensitive`，再跑一次 `varlock scan --install-hook`。

预览时标签不可点

作者提示: 内容由AI生成

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hHXiayYmia1LqLl6UmtMH3DtucaIaicr9HY5ffO5ckGVia3LvuCPCDNRNAX9fEmhic...