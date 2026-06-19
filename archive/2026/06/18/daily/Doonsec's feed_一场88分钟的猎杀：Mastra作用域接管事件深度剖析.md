---
title: 一场88分钟的猎杀：Mastra作用域接管事件深度剖析
url: https://mp.weixin.qq.com/s/1fuMqIiNs0fUypY2ziECRQ
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:06:07.728339
---

# 一场88分钟的猎杀：Mastra作用域接管事件深度剖析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOq81ABIb6yrwqJcSNVDVic6ibSH38Udu8tibBt1yjevaa46d5r5DDj3xhr530BiaJqxRb9onl95hCn7FicVYfn3XLI0ibTyprPOWUvwKk/0?wx_fmt=jpeg)

# 一场88分钟的猎杀：Mastra作用域接管事件深度剖析

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 核心发现

2026年6月17日，我们盯上了一场针对AI开发框架Mastra的供应链攻击。攻击者劫持了前贡献者“ehindero”的npm账户，在88分钟内对`@mastra`命名空间下的**144个**软件包进行了重新发布。手法很精炼——没有篡改包内的业务逻辑，而是走“依赖投毒”路线：在每个被攻陷的包里，只注入一个恶意传递依赖——`easy-day-js`。

最终载荷是一个跨平台的信息窃取器，专门盯着开发者和CI/CD环境里的云服务密钥、LLM API密钥和加密货币钱包。这起事件让我想起一句话：在现代软件供应链里，一个被攻陷的账户，一次发布操作，就能把影响范围扩散到数百万次下载量的生态链里。

## 攻击复盘：一场精心策划的渗透

### 第一步：失去信任的账户——“ehindero”的沦陷

攻击链的起点不是什么零日漏洞，而是一个再常见不过的疏忽。前Mastra贡献者“ehindero”的npm账户（发布权限一直没撤销）被攻破了。攻击者直接从他本地环境里用个人npm token发起发布请求，绕过了Mastra官方用来生成SLSA来源验证的CI/CD流水线。这里有个关键差异：标准的npm token `publish`功能本身就无需provenance，所以恶意包不会被来源验证机制拦下。SafeDep的分析也证实了这一点。

### 第二步：伪装下的毒饵——“easy-day-js”

攻击者在npm上发布了一个叫`easy-day-js`的包，是对合法日期库`dayjs`的精准仿冒（typosquatting）。版本1.11.21是干净的诱饵，而1.11.22版本在`package.json`里埋了一个恶意的生命周期钩子：

```
"scripts": {
  "postinstall": "node setup.cjs --no-warnings"
}
```

`setup.cjs`就是第一阶段投放器。一旦发布1.11.22版本，npm安装时就会自动执行这个脚本。

### 第三步：依赖混合与引爆

攻击者把`@mastra/*`下每个受影响的包版本都提升了一级（比如1.42.0 → 1.42.1），然后在它们的`dependencies`里只加了一行：

```
"easy-day-js": "^1.11.21"
```

关键就在这个插入符号`^`上——它要求npm在安装时自动解析为满足该范围的最新版本。当开发者执行`npm install @mastra/core`时，npm会静默地拉取`easy-day-js`的1.11.22版本，从而触发`postinstall`钩子。

### 第四步：从载荷投放到机器接管

`setup.cjs`的执行逻辑很清晰，效率也高：

1. **禁用TLS验证**：设置环境变量`NODE_TLS_REJECT_UNAUTHORIZED=0`，允许后续与任何证书无效的服务器通信。
2. **下载第二阶段载荷**：从C2服务器`23.254.164.92:8000/update/49890878`下载一个JavaScript脚本（`49890878`是这次行动的ID），写入临时目录。
3. **隐蔽执行**：用`child_process.spawn`，以**独立（detached）** 和**隐藏（windowsHide）** 模式启动子进程运行该脚本，并传入第二个C2地址`23.254.164.123:443`作为参数。这么一做，安装进程快速退出，但恶意软件还在后台跑着。
4. **自我清除**：执行完后，`setup.cjs`立刻从磁盘上删掉自己，清除最直接的取证痕迹。

### 第五步：跨平台信息窃取器的獠牙

第二阶段载荷是一个功能完善的远程访问工具（RAT），后来还被替换成了更强的信息窃取器。它的主要能力：

* **凭据收割**：扫描进程环境变量，锁定`OPENAI_API_KEY`、`ANTHROPIC_API_KEY`、`AWS_ACCESS_KEY_ID`、`GITHUB_TOKEN`、`NPM_TOKEN`这些开发者核心密钥。
* **加密资产窃取**：集中扫描Chrome、Brave、Edge等浏览器里安装的MetaMask、Phantom、Coinbase Wallet、OKX等**160余种**加密货币钱包扩展，窃取相关数据。
* **持久化驻留**：跨平台自动启动，具体机制如下：

+ **macOS**: `~/Library/LaunchAgents/com.nvm.protocal.plist` 和 `~/Library/NodePackages/protocal.cjs`
+ **Linux**: `~/.config/systemd/user/nvmconf.service` 和 `~/.config/NodePackages`
+ **Windows**: `C:\ProgramData\NodePackages`

所有窃取到的数据最终都回传给C2服务器。

## 技术深度分析

### “攻击面”的放大效应

这次事件的核心技术特点在于“分离”和“汇聚”。攻击者把恶意载荷（`easy-day-js`）和被污染的分发通道（`@mastra/*`包的依赖关系）完全分开。传统逐包扫描很难发现这种威胁，因为`@mastra`包本身还是“干净的”，恶意代码只藏在它遥远的传递依赖里。这种设计让单个被攻陷的账户能通过一次依赖关系注入，把恶意负载投送到整个生态里。这种手法在“ChromeLoader”等行动里也出现过。

### I/O指标网络拓扑

攻击者的基础设施很精简，只依赖两个IP地址，都由**Hostwinds LLC.** 托管，机房在德克萨斯州达拉斯市。

* **23.254.164.92 (Stage-1 C2)**：载荷下载服务器，用8000端口提供服务。它不参与数据外泄，只负责分发第二阶段脚本。
* **23.254.164.123 (Stage-2 C2)**：主命令与控制终端，接收被感染主机的信标和外泄的敏感数据。

这种分离式架构是成熟攻击者的惯用手法，目的是增加分析人员的溯源难度。

## 组织归因推测

根据攻击手法、目标选择和工具定制化程度，我们初步推断一下攻击者的画像：

* **动机明确**：目标很直接——云密钥、LLM API密钥和加密货币钱包，有明确的经济获益驱动。这符合常见**网络犯罪组织**的行为模式，比如跟加密货币窃取的“CryptoBot”系列工具在战术上就有重叠。
* **复杂度中等**：这次攻击没用零日漏洞或高度复杂的绕过技术，但执行的精细度（精确的依赖混淆、跨平台持久化、自删除）表明攻击者具备专业的威胁分析能力，能熟练利用开源生态的信任机制进行隐蔽攻击。这排除了低级别黑客的可能性。
* **工具开发能力**：`setup.cjs`使用了`javascript-obfuscator`进行高强度混淆（字符串数组旋转、自定义Base64和XOR编码），显示攻击者在开发或定制恶意工具方面有投入。

考虑到攻击的时机、目标行业和基础设施的托管地（Hostwinds），我们目前以**中等置信度**认为，这件事更可能由以经济获利为目的的**技术型网络犯罪团伙**所为，而不是国家支持的APT组织。后者通常倾向于长期潜伏、窃取系统源代码或网络拓扑数据，不会死盯着开发者环境里的加密货币钱包数据。

## 防御建议

1. **（开发者/运维）立即处置**：

* 对所有安装了受影响`@mastra/*`包（版本号高于安全版本）的系统，立即下线并隔离。
* **优先移除持久化植入物**（macOS的`com.nvm.protocal.plist`、Linux的`nvmconf.service`、Windows的`C:\ProgramData\NodePackages`），然后**再轮换所有凭据**。顺序搞反了，攻击者可能通过新植入的持久化机制再次获取新轮换的凭据。
* 检查`/tmp`目录下有没有`.pkg_history`、`.pkg_logs`文件，以及24位十六进制数字命名的`.js`文件。
* 彻底审计并轮换所有可能已暴露的API密钥（OpenAI、Anthropic、AWS、GitHub、npm Token等）和数据库连接字符串。

2. **（安全团队）增强防护**：

* **网络层**：在DNS和HTTPS代理层面，把`23.254.164.92`和`23.254.164.123`加入黑名单。
* **端点层**：部署能检测`NODE_TLS_REJECT_UNAUTHORIZED=0`环境变量异常修改的行为检测规则。
* **构建系统**：在CI/CD流水线里实施**来源验证（SLSA provenance）强签入策略**，拒绝所有未经签署或来源不匹配的包。
* **依赖管理**：强制用锁文件（`package-lock.json`）进行安装。禁止在关键环境里使用`--ignore-scripts`标志构建，以阻止`postinstall`的执行链。

3. **（开源社区）长期治理**：

* 开源项目要**定期审计贡献者权限**，特别是对有管理员权限的账户，建议启用**双因素认证（MFA）**和**基于角色的最小权限原则**。
* npm及类似生态应该加强账户异常活动检测，比如短时间大规模发布来自不同来源但模式统一的包。

##

## 总结

这次对Mastra框架的供应链攻击，是一次教科书式的“信任投毒”案例。它告诉我们，当网络犯罪的杠杆点从攻击代码本身转向攻击发布者身份时，传统安全防御失效几乎是必然的。开发者环境里被信任的密钥（AI、云、加密资产）已经被明确视为高价值目标，攻击者正在围绕这些资产构建更高效、更隐蔽的攻击链路。对于任何使用开源组件的组织来说，这不再是“如果”的问题，而是“何时”及“如何应对”的问题。

## 技术附录

### MITRE ATT&CK 技术映射

| 战术 | 技术 ID | 技术名称 | 描述 |
| --- | --- | --- | --- |
| 初始访问 | T1195.001 | 供应链攻陷：软件依赖 | 攻陷`ehindero`账户，获得`@mastra`作用域发布权限。 |
| 执行 | T1059.004 | 命令与脚本解释器：Unix Shell | 在`setup.cjs`中调用`child_process.spawn`执行Node.js脚本。 |
| 执行 | T1078 | 有效账户 | 利用被劫持的`ehindero`账户在npm上发布恶意包。 |
| 持久化 | T1543.001 | 创建或修改系统服务：LaunchAgent | 在macOS上创建`com.nvm.protocal.plist`实现重启持久化。 |
| 持久化 | T1543.002 | 创建或修改系统服务：systemd服务 | 在Linux上创建`nvmconf.service`实现重启持久化。 |
| 持久化 | T1547.001 | 启动文件夹：Startup Folder | 在Windows上通过`C:\ProgramData\NodePackages`目录实现启动持久化。 |
| 防御规避 | T1027.002 | 混淆：软件包 | 使用`javascript-obfuscator`对`setup.cjs`进行混淆。 |
| 防御规避 | T1564.001 | 隐藏攻击：隐藏文件和目录 | 在临时目录中创建文件名随机的`.js`文件，并写入`.pkg_history`和`.pkg_logs`等隐藏标记文件。 |
| 防御规避 | T1070.004 | 指示清除：文件删除 | `setup.cjs` 执行后自删除。 |
| 凭证访问 | T1552.001 | 不安全的凭据：环境变量 | 从环境变量中窃取`OPENAI_API_KEY`、`AWS_ACCESS_KEY_ID`等秘密。 |
| 凭证访问 | T1528 | 从系统中窃取凭证 | 窃取浏览器中160余种加密货币钱包扩展的数据。 |
| 命令与控制 | T1102 | Web服务：非标准端口 | 通过`23.254.164.92:8000`下载载荷，通过`23.254.164.123:443`进行后续通信。 |
| 数据外泄 | T1048 | 通过备用协议外泄数据 | 将窃取的数据通过HTTPS回传至C2服务器。 |

### 失陷指标 (IOCs)

#### 网络指标

| 类型 | 指标内容 | 描述 |
| --- | --- | --- |
| IP | 23.254.164[.]92 | 第一阶段C2，提供恶意载荷下载服务。托管于Hostwinds LLC。 |
| IP | 23.254.164[.]123 | 第二阶段C2，接收被控机器信标及外泄数据。托管于Hostwinds LLC。 |
| URL | hxxps://23[.]254[.]164[.]92:8000/update/49890878 | 第二阶段载荷的下载链接，其中`49890878`为本次行动ID。 |
| Domain | mend.io | 无关指标，安全厂商域名，误列。 |

#### 文件系统指标

| 类型 | 指标内容（路径/文件名） | 描述 |
| --- | --- | --- |
| 安装标记 | `<临时目录>/.pkg_history` | 记录包的安装路径的隐藏文件。 |
| 名称标记 | `<临时目录>/.pkg_logs` | 记录`easy-day-js`包名的隐藏文件（使用XOR-0x80编码）。 |
| 暂存载荷 | `<临时目录>/^[0-9a-f]{24}.js$` （正则匹配） | 从C2下载的第二阶段恶意脚本，文件名是24位随机十六进制。 |
| 持久化 (macOS) | `~/Library/LaunchAgents/com.nvm.protocal.plist` | macOS系统下的持久化LaunchAgent plist文件。 |
| 持久化 (macOS) | `~/Library/NodePackages/protocal.cjs` | macOS系统下的持久化脚本文件。 |
| 持久化 (Linux) | `~/.config/systemd/user/nvmconf.service` | Linux系统下的持久化systemd服务文件。 |
| 持久化 (Linux) | `~/.config/NodePackages` | Linux系统下的持久化目录。 |
| 持久化 (Windows) | `C:\ProgramData\NodePackages` | Windows系统下的持久化目录。 |
| 运行时标志 | `NODE_TLS_REJECT_UNAUTHORIZED=0` | Node.js运行时设置为`0`，禁用TLS验证的环境变量。 |

#### 恶意软件包与哈希

| 类型 | 指标内容 |
| --- | --- |
| 恶意软件包 | `easy-day-js@1.11.22` |
| 诱饵软件包 | `easy-day-js@1.11.21` |
| 受污染依赖声明 | `"easy-day-js": "^1.11.21"` （出现在每个被攻陷的`@mastra`包中） |
| Tarball SHA256 (恶意) | `4a8860240e4231c3a74c81949be655a28e096a7d72f38fbe84e5b37636b98417` |
| Tarball SHA256 (诱饵) | `ae70dd4f6bc0d1c8c2848e4e6b51934626c4818dcb5af99d080ddbd7dc337185` |
| 被劫持的npm账户 | `ehindero` |
| 发布恶意包的npm用户 | `sergey2016` |

##

## 参考来源

* https://www.mend.io/blog/mastra-npm-scope-takeover-easy-day-js/
* https://techsparking.com/144-mastra-npm-packages-corrupted-by-contributor-account-hijacked/
* https://securityintelhub.com/medium-144-mastra-npm-packages-compromised-via-hijacked-contributor-account/
* https://thedailytechfeed.com/mastra-npm-packages-compromised-in-supply-chain-attack/
* https://cyberwebspider.com/mastra-npm-packages-compromised-tech-news/
* https://gbhackers.com/hackers-target-npm-ecosystem/
* https://research.splunk.com/

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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
，...