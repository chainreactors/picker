---
title: 威胁情报 | 1.3 万刷量 Fork 投毒！装依赖就被攻击
url: https://mp.weixin.qq.com/s/RED0nW9C1aaaicKAes9Itg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:39:14.450863
---

# 威胁情报 | 1.3 万刷量 Fork 投毒！装依赖就被攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCJtwicd6wmxtfyptXkykrSlXcDXMA4Ad6ITL8PJYyxjiaBxvPPiajlLwc1NdUt7PGtLMibq8BFThfDdNFlfdcGQwBodEc4n2zUem7c/0?wx_fmt=jpeg)

# 威胁情报 | 1.3 万刷量 Fork 投毒！装依赖就被攻击

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

********# 背景******

******#

一个开发者在 GitHub 上搜索 Binance 期货交易机器人，找到一个看起来完整的项目。README 要求填入 API key 和 secret，执行 npm install 安装依赖，然后 node index.js 启动。开发者按指引操作——他们不知道的是，项目 package-lock.json 中一个名为 stake-math@3.5.4 的依赖，会在安装阶段自动下载并执行一个专门针对交易机器人开发环境的凭据窃取器。

这不是假设场景。近日，MistEye 安全监控系统在 npm 生态威胁狩猎中确认，stake-math@3.5.4 是一个伪装成 Kelly stake 数学计算工具的恶意 npm 包，目前正通过 1 个固定版本引用和 2 个利用语义化版本范围的高危入口在 GitHub 上传播。背后牵扯出一个拥有约 1.3 万个仓库的批量 fork 网络和一个覆盖多个交易方向的独立传播账号。攻击者不需要入侵任何正版包——这批包本身就是为伪装成数学工具而创建的恶意依赖。

该包的攻击机制为：postinstall 生命周期脚本在安装完成后自动触发，从远程 JSON 配置获取二阶段凭据窃取载荷 stake-peer.tgz，下载到隐藏目录 .peer/ 后再次执行 npm install，最终加载 peer-math.js 启动对 .env、钱包私钥、浏览器扩展、SSH/云凭据和源码密钥的深度采集。这意味着：不需要用户在代码中 require 该包、不需要显式调用任何 API——在未使用 --ignore-scripts / ignore-scripts=true，且恶意包仍可从 registry、镜像缓存或本地缓存取得的情况下，执行 npm install 即触发恶意行为。

# MistEye 响应******

******#

MistEye 是由 SlowMist 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

MistEye 已第一时间通过情报推送与客户告警通道同步风险。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCLXnpcPUtSs9ibNq5q41MgWFPFselVvs2u3cWwvnSB1HntS87xlibgffTYKHDu6yWIBq3SvM7yEibSZWJATibGlF2KYY1cllwHEVHM/640?wx_fmt=png&from=appmsg)

以下为详细技术分析。

# 一、GitHub 入口******

******#

恶意 npm 包要发挥作用，必须先进入开发者的 node\_modules。在本次事件中，GitHub 侧可见 1 个确定入口与 2 个高风险入口。

1. 精确命中：donoaccestag/forex-mt5-trading-bot

donoaccestag/forex-mt5-trading-bot 声称实现 MT5 外汇自动交易，README 引导用户输入 MT5 交易账号、密码和交易服务器地址。其 package-lock.json 精确锁定了 stake-math@3.5.4，且标记 hasInstallScript: true。

这是风险最明确的单一入口：lockfile 排除了版本解析的不确定性，安装脚本标记直接表明生命周期脚本会被执行。在未使用 --ignore-scripts / ignore-scripts=true，且恶意包仍可从 registry、镜像缓存或本地缓存取得的情况下，按照项目流程执行 npm install 的开发者，在安装依赖的同时即触发 postinstall → install-check.cjs → 二阶段 .tgz 下载 → .peer/ 解压与二次安装 → syncSession() 的完整恶意链路。项目要求配置的 MT5 交易凭据与二阶段凭据采集能力精确重合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJGicl09BqatjoSxPtQibsGQVa4cpaEkY7NYAABmeyqElLy6yeXGCc4vrg7555yJpuIbb4GDDxUQ4zHX36zuJcYdl9WPySupqNicA/640?wx_fmt=png&from=appmsg)

2. 高风险依赖范围：Binance 与 Polymarket 交易机器人

另外两个仓库虽然同样引入 stake-math，但证据形式不同：

daishangona/binance-futures-trading-bot 是一个 Binance 期货交易机器人项目，package.json 声明 "stake-math": "^3.0.0"。Poly-Sports/polymarket-sports-arbitrage-bot 是一个 Polymarket 体育赛事套利工具，同样声明 "stake-math": "^3.0.0"。两个仓库均未在公开页面观察到 lockfile，因此无法直接确认 npm install 最终解析出的具体版本。

semver 版本范围 ^3.0.0 允许解析到 3.x 系列中的任意版本，包括恶意的 3.5.2、3.5.3 和 3.5.4。在恶意版本仍可被 npm registry 解析、镜像缓存或本地缓存命中的情况下，这两个仓库的依赖声明构成实际安装风险。两个项目分别涉及 Binance 期货和 Polymarket sports arbitrage，均属高价值交易场景。

3. 为什么交易机器人仓库是高价值投递场景

交易机器人项目天然要求开发者准备高价值 secret：Polymarket 私钥、Binance API key 和 secret、MT5 交易账号和密码、RPC endpoint、资金账户配置。传统信息窃取攻击通常需要攻击者额外诱导受害者输入凭据，但在交易机器人的 GitHub 工作流中，开发者已经主动配置好了所有这些 secret。

恶意包不需要 phishing，不需要额外交互，不需要用户犯错——安装流程就是触发条件。开发者配置好 .env 后执行 npm install 时，恶意代码就能在同一台机器上搜索并打包这些数据。

# 二、批量 fork 扩散网络******

******#

上述三个上游仓库不是孤立存在的。它们在 GitHub 上共享一个显著异常特征：都被一个名为 poly-stocks 的组织/账号进行了大规模批量 fork，且 fork 行为呈现明显的编号化、低互动和主题错配特征。

1. poly-stocks 的规模与编号模式

截至分析时，poly-stocks拥有约 1.3 万个公开仓库；GitHub 当前公开页面显示约 1.4 万个仓库。其仓库创建模式呈现出高度系统化的特征：多个仓库族使用连续编号命名（如 repo-1、repo-2、repo-3……），像自动化脚本创建的结果，而不是开发者逐个手动 fork 的行为模式。在正常 GitHub 用户或组织中，这种规模的编号化仓库族极为罕见。

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCL69kXAQxdkWrXkId0FGeHgJlEpNnCtjPxsyzt1mIZI67lUdlTicYg5yfOeAjPkOd1fdYEfx80icBEYDxYQ2eKxkv9O6ExPvVicPI/640?wx_fmt=png&from=appmsg)

2. 三组与 stake-math 直接关联的 fork 家族

与 stake-math 恶意依赖直接关联的有三组编号化 fork 家族。以下数据基于当时公开 GitHub 页面可见结果：

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJX5vovdY0NyoW6gQbv9LvMClXF9leGCcLHmqfovss6VqTmsksOnEibxpsTicpx9NRUYdNgNjSRHS22TrYsldOtGtaQTiaVKLuHfM/640?wx_fmt=png&from=appmsg)

三组合计约 5,300 个仓库。其中第一组最危险：由于上游 lockfile 精确锁定了 stake-math@3.5.4 且 hasInstallScript: true，约 1,615 个 fork 仓库均携带该确定证据。fork 仓库继承了上游的完整 lockfile，意味着它们全部具备安装期自动触发的条件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIcXlT1E55Vvsvb3Qe5prmhocWsjPyRnvNmM1PiaXYlrS2D2S1Oz2vZ3TSnE4DZDvApf4vseee5zGsReJvlIBWDCZNYD7ITtHIs/640?wx_fmt=png&from=appmsg)

后两组 fork 仓库继承的是上游的 "stake-math": "^3.0.0" 声明，最终安装风险取决于 npm 在具体环境中的版本解析结果。但由于数量庞大（合计约 3,700 个仓库），任何仓库被克隆和安装时的潜在面都是显著的。

3. 0 star / 0 issue / 0 PR 的低互动特征

GitHub 列表页中可见的这三组编号化仓库样本普遍呈现 0 stars / 0 issues / 0 pull requests 的一致低互动模式。正常 GitHub 项目——即使是 fork——通常会积累不定量的 star 和互动。大量仓库同时呈现如此一致的低互动特征，不符合正常开发者逐一创建或维护的特征，更符合自动化批量创建的特征。

4. 主题错配：从交易机器人到 free-programming-books 等异常命名

另一个异常模式在 poly-stocks 下非 stake-math 直接关联的仓库族中更为明显：

* boilerplates{,-1..-660}：约 661 个编号化仓库（base + -1..-660）
* free-programming-books{,-1..-662}：约 663 个编号化仓库（base + -1..-662）
* agent-rules{,-1..-659}：约 660 个编号化仓库（base + -1..-659）

其中 free-programming-books 的上游是从交易机器人仓库 fork 而来，最终却被命名为与交易无关的主题，显示出将热门项目重新命名为无关主题进行规模化扩散的行为。agent-rules 的上游是 Poly-Sports/polymarket-sports-arbitrage-bot，同样存在从 Polymarket 套利到 agent-rules 的主题跳跃。这些编号仓库表现出从交易机器人仓库重命名为无关主题的错配现象，可能扩大仓库在不同 GitHub 搜索关键词下的触达面。

# 三、跨题材传播与关联风险******

******#

在 poly-stocks 的批量 fork 网络之外，GitHub 用户 xumoyan 构成了另一条独立的风险线索。同一仓库网络中还存在不直接涉及 stake-math 的关联风险线索。

1. xumoyan：独立于 poly-stocks 的传播分支

xumoyan 是 poly-stocks 之外的另一个关键关联账号。该账号同时 fork 或持有了多个与高风险依赖相关的仓库：

* xumoyan/forex-mt5-trading-bot
* xumoyan/polymarket-sports-arbitrage-bot
* xumoyan/polymarket-arbitrage-trading-bot
* xumoyan/polymarket-fifa-arbitrage

从公开 fork 关系看，xumoyan 是 poly-stocks 之外的独立传播分支。该账号与多组高风险交易机器人仓库存在 fork / 持有关系，其仓库涉及 MT5 外汇、Polymarket sports、Polymarket arbitrage、FIFA arbitrage 等多个交易方向。

2. 从 MT5、Binance 到 Polymarket / FIFA arbitrage 的题材扩展

将 poly-stocks 与 xumoyan 的仓库范围合并来看，该网络覆盖的开发者兴趣面相当广：

* MT5 外汇自动化交易（传统金融交易者）
* Binance 期货交易（加密货币期货交易者）
* Polymarket 体育赛事套利（预测市场交易者）
* Polymarket 套利交易（预测市场高频交易者）
* FIFA 赛事套利（体育预测交易者）

这些题材涵盖传统金融、中心化加密货币交易所和去中心化预测市场，对三类不同背景的开发者均有吸引力。一个开发者可能在任意一个场景下搜索并克隆相关仓库，从而进入同一条恶意依赖链路。

3. Runtime-Trade-Systems 与 @tsjunk/chalk 的关联风险

Runtime-Trade-Systems/polymarket-arbitrage-trading-bot 及其 xumoyan fork 构成了另一条关联风险线索。该仓库不涉及 stake-math，但直接依赖 @tsjunk/chalk@^5.6.2。对本地样本 @tsjunk/chalk@5.6.2 的源码审计显示，该包并非普通终端颜色库，而是伪装官方 chalk@5.6.2 的恶意仿冒包：它保留了 chalk 的描述、仓库地址、README 风格和版本号，但包名变为 @tsjunk/chalk，并额外新增运行时依赖 log-upgrade@^7.1.0。

这条线索的触发方式不同于 stake-math。@tsjunk/chalk 的风险主要发生在应用运行阶段。该包未定义 postinstall 等安装期脚本，而是在入口文件 source/index.js 顶层导入 log-upgrade，并在颜色等级初始化逻辑中调用 logUpgradeStderr.persist()。这意味着只要业务代码加载 @tsjunk/chalk，其依赖链中的 log-upgrade 就可能被同步加载。对另行获取并核验的 log-upgrade@7.1.0 npm 包源码分析显示，该依赖会在模块初始化阶段执行系统信息上报、读取项目 .env 与配置文件、扫描并上传本地文件，并在 Linux 环境下向 SSH authorized\_keys 写入公钥，具备明确的数据窃取与持久化后门特征。

该风险在 Polymarket 交易机器人场景下尤为敏感。项目要求用户配置 POLYMARKET\_PRIVATE\_KEY，并在服务层将 signer 传入 Polymarket CLOB client。虽然私钥加载和 signer 初始化本身属于交易机器人的正常业务逻辑，但当运行期依赖链中同时存在具备文件读取、环境变量窃取和远程上报能力的恶意包时，钱包私钥、交易凭据及相关配置文件面临显著暴露风险。

4. thombanal/polymarket-fifa-arbitrage 与非官方 tarball 来源

thombanal/polymarket-fifa-arbitrage（后被 xumoyan fork）不涉及 stake-math 主线，但其 package-lock.json 将 @clack/prompts@1.5.1 的 tarball 源指向非官方域名 registrynpmjs[.]to，并标记 hasInstallScript: true。正常情况下，npm 包 tarball 应来自 registry.npmjs.org 或明确配置的可信镜像；但该仓库 .npmrc 仅配置 loglevel=error，未声明自定义 registry。因此，registrynpmjs[.]to 作为依赖下载源本身就是异常信号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIIIQRQVfDXMVbh9P7ZKcOH6fQDzNHpBKE0Q9j9F3g8SwUTttXUgiaKXLFZLegzjlc6qTZicibuvXdcDRjXFSwOwnjickvvhCmn0y0/640?wx_fmt=png&from=appmsg)

后续情报与样本审计进一步确认了这一判断：registrynpmjs[.]to 已在微步情报社区中被标记为恶意；同时，对该 URL 下载得到的 clack-prompts-1.5.1.tgz 进行审计和差异对比后确认，该包并非正常的 @clack/prompts 发布物，而是被投毒的恶意包。

与正常 @clack/prompts 包相比，该样本结构差异显著：正常包应包含用于构建交互式 CLI prompts 的完整组件、类型定义和构建产物；而该恶意 tarball 仅包含 package.json、build-helper.js 和 index.js 三个文件，并新增 postinstall 生命周期脚本。安装时，postinstall 会自动执行混淆 payload，扫描用户主目录中的钱包文件、私钥、.env、文档、项目配置和其他敏感文件，并通过 HTTPS POST 上传至 rabbylgh[.]to:8443/upload。这种安装期窃密行为与 @clack/prompts 官方定位完全不符，属于典型的 npm 供应链投毒。

更高风险的是，该仓库本身是 Polymarket/FIFA 套利机器人项目，README 要求用户配置 PRIVATE\_KEY、DEPOSIT\_WALLET\_ADDRESS、POLY\_API\_KEY、POLY\_API\_SECRET、POLY\_API\_PASSPHRASE 等钱包与交易凭据。而该项目的 lockfile 依赖了一个已被确认恶意的非官方 tarball（@clack/prompts@1.5.1），且该包在安装...